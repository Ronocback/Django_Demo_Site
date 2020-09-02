from django.shortcuts import render
from .models import Record
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print("leaderboard_post")
        print(request.POST)
        name = request.POST.get('username')
        print(name)
        score = int(request.POST.get("score"))
        Record.objects.create(username=name, score=score)
    leaderboard_list = Record.objects.all()
    print("board")
    print(leaderboard_list)
    leaderboard_list_ls = []
    for record in leaderboard_list:
        leaderboard_list_ls.append(record)
    max_scoring = None
    board = []
    while len(leaderboard_list_ls) > 0:
        for record in leaderboard_list_ls:
            if max_scoring is None or max_scoring.score < record.score:
                max_scoring = record
        board.append(max_scoring)
        print(max_scoring)
        print(leaderboard_list_ls)
        leaderboard_list_ls.remove(max_scoring)
        max_scoring = None
    context = {"leaderboard_list": board}
    print(leaderboard_list)
    return  render(request, 'leaderboard/index.html', context)
