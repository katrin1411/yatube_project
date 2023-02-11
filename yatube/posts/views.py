from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse('Список мороженого')


#def ice_cream_detail(request, pk):
#    return HttpResponse(f'Мороженое номер {pk}')