from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CommentForm
from .models import Game, Comment
from django.views.generic import DetailView


# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})


class GameDetailView(View):
    template_name = 'game_detail.html'

    def get(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        comments = Comment.objects.filter(gameId=pk)

        form = CommentForm(initial={'gameId': pk})

        context = {
            'game': game,
            'comments': comments,
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        comments = Comment.objects.filter(gameId=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.gameId = game
            comment.userId = request.user
            comment.save()
            form = CommentForm()

        context = {
            'game': game,
            'comments': Comment.objects.filter(gameId=pk),
            'form': form,
        }

        return render(request, self.template_name, context)
