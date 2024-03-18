from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question

def index(request ):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    ##return HttpResponse('<h1>Desenvolvimento de Sistemas WEB</h1><h2>3o Período</h2><h3>20231014040010</h3><h3>Leonardo Viana Brito</h3>')

##Adiantando aula views e templates
def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    response = "Resultados da questao %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "Votacao para a questao %s."
    return HttpResponse(response % question_id)