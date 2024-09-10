from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Welcome to My Website </h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Contact Page</h1>")
