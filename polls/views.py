from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello,Songchenglin add here!!!!.')
def detail(request, question_id):
    response = 'You\'re looking at the question %s!!!!!'
    return HttpResponse(response % question_id)
def results(request, question_id):
    response = 'You\'re lookng at the reuslts of question %s.'
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s.' % question_id)

