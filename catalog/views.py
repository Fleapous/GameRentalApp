from django.shortcuts import render
from .models import Game


# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'catalog/game_list.html', {'games': games})
