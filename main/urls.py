from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('greet/<name>/', views.greet, name='greet'),
    path('todo/', views.todo, name="todo"),
]
