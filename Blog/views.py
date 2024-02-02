from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    render(request, 'contact.html')


def galery(request):
    render(request, 'galery.html')