from django.urls import path
from .views import (rent_game, get_address_details, get_rental_history, upload_rental_history_xml
, generate_rental_history_xml)

urlpatterns = [
    path('rent_game/<int:game_id>/', rent_game, name='rent_game'),
    path('get_address_details/<int:address_id>/', get_address_details, name='get_address_details'),
    path('get_rental_history/', get_rental_history, name='get_rental_history'),
    path('upload_rental_history_xml/', upload_rental_history_xml, name='upload_rental_history_xml'),
    path('generate_renatl_history_xml/', generate_rental_history_xml, name='generate_rental_history_xml')
]

