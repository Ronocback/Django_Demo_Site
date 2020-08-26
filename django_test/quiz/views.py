from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question, Option
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    latest_question_list = Question.objects.all()
    latest_option_list = Option.objects.all()
    context = {'latest_question_list': latest_question_list, 'latest_option_list': latest_option_list}        
    if request.method == "POST":
        print(request.POST)
    return  render(request, 'quiz/index.html', context)


def detail(request, question_id):
    print(str(Question.objects.all()))
    question = Question.objects.get(id=question_id)
    context = { 'requested_question' : question }
    if context:
        print(context)
    return render(request, 'details/index.html', context)

# Create your views here.
