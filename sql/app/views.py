from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from pymysql import connect

from utils.inception import inception

import os
import math
from time import time

from .serializers import *

class InstanceView(ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('db_name','env')
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = self.filter_queryset(self.get_queryset()).count()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'table_data':serializer.data,'total_count':count})

class SqlExec(APIView):
    def post(self,request,*args,**kwargs):
        sql=request.data['sql']
        db_name=request.data['db_name']
        env=request.data['env']
        ins=Instance.objects.filter(db_name=db_name,env=env).first()
        if not ins:
            return Response({'table_label': None, 'table_data': None, 'is_query': 0})
        try:
            con=connect(user=ins.account,password=ins.password,host=ins.db_ip,port=ins.db_port,database=ins.db_name)
            cur=con.cursor()
            cou=cur.execute(sql)
            res=cur.fetchall()
            col=cur.description
            cur.close()
            table_data=[]
            table_label=[{'label': column[0],'prop':column[0]} for column in col]
            for i in res:
                tmp={}
                for j in col:
                            tmp[str(j[0])]=i[col.index(j)]
                table_data.append(tmp)
            print(table_data)
            return Response({'table_label': table_label, 'table_data': table_data, 'is_query': 1})
        except Exception as e:
            print(e)
            return Response({'table_label': None, 'table_data': '执行失败', 'is_query': 0})

class Testdb(APIView):
    def get(self,request,*args,**kwargs):
        ret = [{'value': i['db_name'],'label': i['db_name']} for i in Instance.objects.filter(env="测试").values('db_name')]
        return Response({'db_data': ret})

class Proddb(APIView):
    def get(self,request,*args,**kwargs):
        ret = [{'value': i['db_name'],'label': i['db_name']} for i in Instance.objects.filter(env="生产").values('db_name')]
        return Response({'db_data': ret})

class ConTestView(APIView):
    def post(self,request,*args,**kwargs):
        ret = {
            "data": "",
            "msg":"success"
        }
        try:
            con = connect(user=request.data['username'],password=request.data['password'],host=request.data['host'],port=request.data['port'])
            return Response(request.data)
        except Exception as e:
            ret['data']=request.data
            ret['msg']=e
            return Response(ret)

class SqlScore(APIView):
    def post(self,request,*args,**kwargs):
        ret = {
            "data":"",
            "msg":"success"
        }
        file_pre = str(math.floor(time()))
        print(request.data)
        command ="soar --query '" + request.data['sql'] + "'"
        try:
            res = os.popen(command)
            ret["data"]=res
            return Response(ret)
        except Exception as e:
            ret['data']=request.data['sql']
            ret['msg']=e
            return Response(ret)

class Inception(APIView):
    def post(self,request,*args,**kwargs):
        ret = {
            "data":"",
            "msg":"success"
        }
        print(request.data)
        try:
            sql = request.data['sql']
            env = request.data['env']
            db = request.data['db']
            obj = Instance.objects.filter(db_name=db,env=env).first()
            user = obj.account
            password = obj.password
            host = obj.db_ip
            port = obj.db_port
            res = inception(user,password,host,str(port),db,sql)
            list_res=list(res)
            list_res.pop(0)
            res = ['<span><strong style="color:black">sql:</strong> {}</span><br><span style="color:teal"><strong style="color:black">result:</strong> {}</span><hr>'.format(i[5], i[4] if i[4] else 'success') for i in list_res]
            ret["data"]=res
            return Response(ret)
        except Exception as e:
            ret["msg"]=str(e)
            print(ret)
            return Response(ret)

