"""
URL configuration for listaContactos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView
from inicio.views import anotherView
from personas.views import personaTestView
from personas.views import personaCreateView, searchForHelp
from personas.views import personasAnotherCreateView, personasShowObject, personasListView
urlpatterns = [
    path('', myHomeView, name='Pagina de Inicio'),
    path('another/', anotherView),
    path('persona/', personaTestView, name='otro'),
    path('agregar/', personaCreateView, name='createPersona'),
    path('anotherAdd/', personasAnotherCreateView, name='OtroAgregarPersona'),

    path('search/', searchForHelp, name='buscar'),

    path('admin/', admin.site.urls),

    path('personas/<int:myID>/', personasShowObject, name='browsing'),
    path('personas/', personasListView, name='listing'),

]
