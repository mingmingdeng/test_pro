from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from app.views import *

rou = DefaultRouter()
rou.register(r'ip',InstanceView)

urlpatterns=[
    url('',include(rou.urls)),
    url(r'contest',ConTestView.as_view()),
    url(r'sqlscore',SqlScore.as_view()),
    url(r'inception',Inception.as_view()),
    url(r'sqlexec',SqlExec.as_view()),
    url(r'testdb',Testdb.as_view()),
    url(r'proddb',Proddb.as_view()),
    url('docs',include_docs_urls(title='接口展示')),
]
