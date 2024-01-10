# catalog/urls.py
from django.urls import path
from .views import game_list, GameDetailView

urlpatterns = [
    path('games/', game_list, name='game-list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
]