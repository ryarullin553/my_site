from django.urls import path
from .views import *

urlpatterns = [
    path('', test),
    path('cats/<int:catid>/', categories)
]
