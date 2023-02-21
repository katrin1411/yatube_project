from django.contrib import admin
from django.urls import path, include

app_name = 'posts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
]
