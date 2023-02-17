from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', index,  name = 'group_list'),
    path('group/<slug:slug>/', group_posts, name = 'group_list'),
    
]
