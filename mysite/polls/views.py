from django.shortcuts import render
from django.http import HttpResponse

def index(request ):
    return HttpResponse('Pools app DSWeb 2024.1')