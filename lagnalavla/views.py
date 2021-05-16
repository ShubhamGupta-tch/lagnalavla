from django.http import HttpResponse
from .htmlpagerender import htmlcode

def home(request):
    return HttpResponse(htmlcode('lagnalavla/templates/index.html'))

def greet(request, name):
    return HttpResponse(htmlcode('lagnalavla/templates/greet.html').replace('--NAME--', name))
