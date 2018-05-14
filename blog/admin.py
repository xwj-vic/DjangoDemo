from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


# 配置后台管理应用
admin.site.register(models.Article, ArticleAdmin)
