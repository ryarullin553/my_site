from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    temps = {'title': 'Главная',
            }
    return render(request, 'articles/base.html', temps)
