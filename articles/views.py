from django.shortcuts import render
from .models import *


def create_articles(request):
    posts = Article.objects.all()
    digits = range(150)
    temps = {'title': 'Статьи', 'posts': posts, 'digits': digits}
    return render(request, 'articles/index.html', temps)

