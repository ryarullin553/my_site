from django.urls import path
from .views import *

urlpatterns = [
    path('', articles, name='articles'),
    path('article/<int:article_id>/', open_article, name='article'),
    path('category/<int:category_id>/', open_category, name='category'),
]
