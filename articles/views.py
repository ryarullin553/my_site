from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def articles(request):
    articles_list = Article.objects.all()
    temps = {'title': 'Статьи',
             'articles': articles_list,
             }
    return render(request, 'articles/index.html', temps)


def open_article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    temps = {'article': article,
             'title': article.title,
             }
    return render(request, 'articles/article.html', temps)


def open_category(request, category_slug):
    articles_list = Article.objects.filter(category__slug=category_slug)
    temps = {'title': f'Статьи {Category.objects.get(slug=category_slug)}',
             'articles': articles_list,
             }
    return render(request, 'articles/index.html', temps)
