from django.shortcuts import render
from django.http import HttpResponse
from .htmlpagerender import htmlcode

def home(request):
    return render(request, 'main/index.html')

def greet(request, name):
    return render(request, 'main/greet.html', {
            'name': name,
        })
