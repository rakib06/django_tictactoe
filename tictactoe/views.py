from django.http import HttpResponse

def welcome(requerst):
    return HttpResponse("Hello, world")