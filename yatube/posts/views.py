from django.shortcuts import render
from django.http import HttpResponse
from django .template import loader


def index(request):
    template = loader.get_template('posts/index.html')
    return HttpResponse(template.render({}, request))


def group_posts(request, slug):
    return HttpResponse('Список мороженого')

