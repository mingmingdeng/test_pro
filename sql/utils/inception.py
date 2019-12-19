#!/usr/bin/env python
# -*- coding:utf-8 -*-
def inception(user,password,host,port,db,sql):
        import pymysql
        sql1='/*--user='+ user +';--password='+ password +';--host='+ host +';--execute=1;--port='+ port +';*/inception_magic_start;use '+ db +';'+ sql +';inception_magic_commit;'
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123123',db='test', port=4000, charset="utf8mb4")
        cur = conn.cursor()
        ret = cur.execute(sql1)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return(result)
if __name__ == '__main__':
    res=inception('root','123123','127.0.0.1','3306','test','afdafas')
    print(res)
