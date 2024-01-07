from django.urls import path
from .views import rent_game

urlpatterns = [
    path('rent_game/<int:game_id>/', rent_game, name='rent_game'),
]

