from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [

     url(r'^(?P<CatHead>[\w-]+)/$',views.cat, name='categories')
    
]