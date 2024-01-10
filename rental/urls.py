from django.urls import path
from .views import rent_game, get_address_details, get_rental_history

urlpatterns = [
    path('rent_game/<int:game_id>/', rent_game, name='rent_game'),
    path('get_address_details/<int:address_id>/', get_address_details, name='get_address_details'),
    path('get_rental_history/', get_rental_history, name='get_rental_history'),
]

