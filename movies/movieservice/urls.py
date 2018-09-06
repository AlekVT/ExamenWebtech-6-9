from django.urls import path

from . import views

app_name = 'movieservice'
urlpatterns = [
    path('', views.index, name='index'),
    path('actors', views.actors, name='actors'),
]