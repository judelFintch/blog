from django.http import HttpResponse
from django.shortcuts import render
from .postArticles import postArticles
from lorem_text import lorem


def index(request):
    #return HttpResponse(postArticles)
   return render(request, 'index.html', context={'postArticles': postArticles})

def about(request):
    paragraph = lorem.words(80)
    return render(request, 'about.html', context={'paragraph': paragraph})

def contact_us(request):
   return render(request, 'contact.html')


