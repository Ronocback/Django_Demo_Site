from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return  render(request, 'quiz/index.html', context)


def detail(request, question_id):
    print(question_id)
    return HttpResponse( question_id)

# Create your views here.
