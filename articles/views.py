from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *


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


def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Создается новый экземпляр Article с данными из формы
            return redirect('articles_page')  # Возвращает на страницу со статьями
    else:
        form = AddArticleForm()

    temps = {'title': 'Добавить статью',
             'form': form,
             }
    return render(request, 'articles/add.html', temps)
