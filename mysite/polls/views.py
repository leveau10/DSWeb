from django.shortcuts import render
from django.http import HttpResponse

def index(request ):
    return HttpResponse('<h1>Desenvolvimento de Sistemas WEB</h1><h2>3o Período</h2><h3>20231014040010</h3><h3>Leonardo Viana Brito</h3>')