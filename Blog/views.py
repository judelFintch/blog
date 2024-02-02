from django.http import HttpResponse
from django.shortcuts import render
from .postArticles import postArticles


def index(request):
    #return HttpResponse(postArticles)
   return render(request, 'index.html', context={'postArticles': postArticles})

def about(request):
    return render(request, 'about.html')

def contact_us(request):
   return render(request, 'contact.html')


