from django.shortcuts import render
from django.http import HttpResponse

def index(request ):
    return HttpResponse('<h1>Desenvolvimento de Sistemas WEB</h1><h2>3o Período</h2><h3>20231014040010</h3><h3>Leonardo Viana Brito</h3>')


##Adiantando aula views e templates
def detail(request, question_id):
    response = "Voce esta visualizando a questao %s."
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "Resultados da questao %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "Votacao para a questao %s."
    return HttpResponse(response % question_id)