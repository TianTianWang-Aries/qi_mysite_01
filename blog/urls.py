# _*_ coding:utf-8 _*_
__author__ = "Aries"
__date__ = "DATE 17:04"
from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog_title, name="blog_title"),

    # re_path此处需要补充content
    re_path('content/(?P<article_id>\d+)/', views.blog_article, name="blog_detail"),

]