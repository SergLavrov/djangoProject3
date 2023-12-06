from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Home page for django project")
