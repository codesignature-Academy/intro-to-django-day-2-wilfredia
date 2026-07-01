from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome to my Webpage</h1>')

def about(request):
    return HttpResponse('<p> This is professional Portfolio page</p>')

def contact(request):
    return HttpResponse('<p> This is my contact page</p>')