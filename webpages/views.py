from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<html><body>It is now %s.</body></html>")

def about(request):
    pass

def services(request):
    pass

def contact(request):
    pass