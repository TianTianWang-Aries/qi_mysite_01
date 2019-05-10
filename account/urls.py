# _*_ coding:utf-8 _*_
__author__ = "Aries"
__date__ = "DATE 18:25"
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views


app_name = 'account'
urlpatterns = [
    # path('login/', views.user_login, name = "user_login" ),  # 自定义的登录
    path('login/', auth_views.login, name = 'user_login' ),      # django的内置登录
    path('new-login/', auth_views.login, {"template_name": "account/login.html"})
]
