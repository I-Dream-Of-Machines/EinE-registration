from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Python Functions that respond to user requests


def index(request):
    return HttpResponse('<h1>This is the user account home page</h1>')
