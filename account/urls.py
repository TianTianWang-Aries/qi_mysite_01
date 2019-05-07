# _*_ coding:utf-8 _*_
__author__ = "Aries"
__date__ = "DATE 18:25"
from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name = "user_login" ),

]
