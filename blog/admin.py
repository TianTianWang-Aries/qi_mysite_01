# _*_ coding:utf-8 _*_
from django.contrib import admin

from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish", "body")
    list_filter = ("publish", "title")
    search_fields = ('title', "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish', 'author']


admin.site.register(BlogArticles, BlogArticlesAdmin)

