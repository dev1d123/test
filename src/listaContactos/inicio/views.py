from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myHomeView(request, *args, **kwargs):
    return render(request, "home.html", {})

def anotherView(request):
    return HttpResponse('<h1>Solo otra pagina</h1>')

def template1(request):
    return render(request, "template1.html", {})
