from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

def index(request ):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['option']
        alt = question.choice_set.get(pk=choice_id)
    except(KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error': 'Você precisa escolher uma alternativa.'
            }
        return render(request, 'polls/detail.html', context)
    else:
        alt.votes += 1
        alt.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))