from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return all the published questions"""
        return Question.objects.order_by('question_text')
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
def vote(request, question_id):
    p = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':p,
            'error_message':'You didn\'t select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

