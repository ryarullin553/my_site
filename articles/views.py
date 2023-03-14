from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *


class ArticlesList(ListView):
    model = Article
    template_name = 'articles/index.html'  # Явно указываем собственный шаблон
    context_object_name = 'articles'  # Указываем контекст для обращения к экземплярам в шаблоне
    extra_context = {'title': 'Статьи'}  # Передает только статический контекст: строки и цифры

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class CategoryArticlesList(ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'
    allow_empty = False                    # Ошибка 404 при несуществующей категории

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Статьи {Category.objects.get(slug=self.kwargs['category_slug'])}"
        return context

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class ArticleShow(DetailView):
    model = Article
    template_name = 'articles/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['article']
        return context


class AddArticle(CreateView):
    form_class = AddArticleForm
    template_name = 'articles/add.html'
    success_url = reverse_lazy('articles_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить статью'
        return context

