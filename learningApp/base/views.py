from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    return HttpResponse('<h1>Home Page</h1>')

def room(req):
    return HttpResponse('<h1>Room Page</h1>')