from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def articles(request):
    articles_list = Article.objects.all()
    category_list = Category.objects.all()
    temps = {'title': 'Статьи', 'articles': articles_list, 'categories': category_list}
    return render(request, 'articles/index.html', temps)


def open_article(request, article_id):
    return HttpResponse(article_id)


def open_category(request, category_id):
    articles_list = Article.objects.filter(category_id=category_id)
    category_list = Category.objects.all()
    temps = {'title': f'Статьи {Category.objects.get(pk=category_id)}',
             'articles': articles_list,
             'categories': category_list,
             }
    return render(request, 'articles/index.html', temps)
