from django.shortcuts import render
from gameplay.models import Game
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    draw_games = my_games.draw()
    
    return render(request, "player/home.html",
    {'games': active_games, 'draw_games': draw_games } )
    
    #return render (request, 'player/home.html',
    #{ 'ngames': Game.objects.count()})