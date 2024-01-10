from django.shortcuts import render, get_object_or_404
from .models import Game
from django.views.generic import DetailView


# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'catalog/game_list.html', {'games': games})


class GameDetailView(DetailView):
    model = Game
    templates = 'game_detail.html'
    context_object_name = 'game'

    def get_object(self, queryset=None):
        game_id = self.kwargs.get('pk')
        return get_object_or_404(Game, id=game_id)
