from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Persona
from .forms import PersonaForm, RawPersonaForm
from django.urls import reverse_lazy
from django.views.generic.list import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
def personasAnotherCreateView(request):
    form = RawPersonaForm() #request.GET
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'personas/personasCreate.html', context)

def personaCreateView(request):
    initialValues={
        'nombres': 'Sin Nombre'
    }
    form = PersonaForm(request.POST or None, initial=initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
        'form': form
    }
    return render(request, 'personas/personasCreate.html', context)

def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id=myID)
    context={
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)


def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'objeto': obj
    }
    return render(request, 'personas/descripcion.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})

class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte='40')

class PersonaDetailView(DetailView):
    model = Persona

class PersonaCreateView(CreateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador'
    ]
class PersonaUpdateView(UpdateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador'
    ]

class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')

class PersonaQueryView(View):
    def get(self, reuquest, *args, **kwargs):
        queryset = Persona.object.filter(edad_lte='40')
        return JsonResponse(list(queryset.values()), safe = False)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    if request.method == 'POST':
        print("Lo borro")
        obj.delete()
        #redirecionando!
        return redirect('../')
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/personasBorrar.html', context)
