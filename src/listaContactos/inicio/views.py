from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText' : 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList' : {33,44,55,66,77},
        'myDict': {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'},
    }
    return render(request, "home.html", myContext)

def anotherView(request):
    return HttpResponse('<h1>Solo otra pagina</h1>')