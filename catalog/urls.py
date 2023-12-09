# catalog/urls.py
from django.urls import path
from .views import game_list

urlpatterns = [
    path('games/', game_list, name='game-list'),
    # Add more paths as needed
]