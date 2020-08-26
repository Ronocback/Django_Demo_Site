from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from quiz.models import Question, Option

@csrf_exempt
def index(request):
    print("scoring")
    score = 0
    points = 0
    latest_option_list = Option.objects.all()
    latest_question_list = Question.objects.all()
    for question in request.POST:
        for ls_question in latest_question_list:
            q = question.split('-')[0]
            print(q + " " + str(ls_question.id))
            if q == str(ls_question.id):
                points = ls_question.points
                print("ls_quest")
        answer = request.POST.get(question)
        for option in latest_option_list:
            if option.choice_text == answer:
                score += points
                print("ls_opt")
    context = {"score":str(score)}



    print(request.POST)
    return render(request, 'score_preview/index.html', context)