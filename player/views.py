from django.shortcuts import render
from gameplay.models import Game

# Create your views here.
def home(request):
    
    game_first_player = Game.objects.filter(
        first_player = request.user,
        status='F'
    )

    game_second_player = Game.objects.filter(
        second_player = request.user,
        status='S'
    )

    all_my_games = list(game_first_player) + \
        list(game_second_player)
    
    return render(request, "player/home.html",
    {'games': all_my_games})
    
    #return render (request, 'player/home.html',
    #{ 'ngames': Game.objects.count()})