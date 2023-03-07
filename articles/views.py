from django.shortcuts import render
from models import *


def test(request):
    lst = ['_____'.join(['(^_^)' for _ in range(5)]) for _ in range(5)]
    temps = {'title': 'Страница сайта', 'lst': lst}
    return render(request, 'articles/index.html', temps)

