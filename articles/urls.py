from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    url(r'^$',views.article_list,name='list'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name='detail'),
]