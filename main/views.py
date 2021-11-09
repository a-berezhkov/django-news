from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h2> Привет! </h2>")


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html',{'values': ["first", "second"]})
