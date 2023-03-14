from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticlesList.as_view(), name='articles_page'),
    path('category/<slug:category_slug>/', CategoryArticlesList.as_view(), name='category'),
    path('article/<slug:article_slug>/', ArticleShow.as_view(), name='article'),
    path('add/', AddArticle.as_view(), name='add_article')
]
