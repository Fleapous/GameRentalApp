from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RentalForm
from catalog.models import Game


# Create your views here.

@login_required(login_url='login')
def rent_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.method == 'POST':
        form = RentalForm(request.POST, initial={'game': game, 'user': request.user})
        if form.is_valid():
            form.instance.user = request.user
            form.instance.status = 'pending'
            form.instance.game = game
            form.save()
            return redirect('home')
    else:
        form = RentalForm(initial={'game': game, 'user': request.user})
    return render(request, 'rent_game.html', {'form': form, 'game': game})
