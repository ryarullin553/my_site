from django.urls import path
from .views import *

urlpatterns = [
    path('', articles, name='articles_page'),
    path('article/<slug:article_slug>/', open_article, name='article'),
    path('category/<slug:category_slug>/', open_category, name='category'),
]
