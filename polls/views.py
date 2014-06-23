from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from polls.models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('question_text')
    context =  {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)
def detail(request, question_id):
    response = 'You\'re looking at the question %s!!!!!'
    return HttpResponse(response % question_id)
def results(request, question_id):
    response = 'You\'re lookng at the reuslts of question %s.'
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s.' % question_id)

