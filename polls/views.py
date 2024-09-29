from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question, Choice


def index(request):
	obj = Question.objects
	return render(request, "polls/index.html", { "question": obj })

def detail(request, question_id):
	obj = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", { "question": obj})