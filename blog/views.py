from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models


# 首页
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


# 文章内容页面
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article.html', {'article': article})


# 文章编辑页面
def edit_article_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'edit_article.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_article.html', {'article': article})


# 添加/更新
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
    return HttpResponseRedirect('/index/index')
