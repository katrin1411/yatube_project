from django.shortcuts import render



def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    text = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    text = 'Здесь будет информация о группах проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)

