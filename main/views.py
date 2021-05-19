from django.shortcuts import render
from django.http import HttpResponse
from .htmlpagerender import htmlcode

def home(request):
    return render(request, 'main/index.html')

def greet(request, name):
    return render(request, 'main/greet.html', {
            'name': name,
        })

def todo(request):
    if request.method == 'POST':
        request.session['todos'] += [request.POST['todo']]

    try:
        todos = request.session['todos']

    except:
        request.session['todos'] = []
        todos = request.session['todos']

    return render(request, 'main/todo.html', {
            'todos': todos,
        })
