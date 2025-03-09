# Importing library in python be like: from library-name.its-module import its-component
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Create a function in python be like:
# def function-name(parameter):
# return something
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")