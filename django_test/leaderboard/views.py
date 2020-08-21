from django.shortcuts import render
from .models import Record

def index(request):
    leaderboard_list = Record.objects.all()
    context = {"leaderboard_list": leaderboard_list}
    return  render(request, 'leaderboard/index.html', context)
