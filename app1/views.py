from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_first(request):
    return HttpResponse('this is first view in app1')

def app1_second(response):
    return HttpResponse('<h1> this is second view in app1</h1>')   
