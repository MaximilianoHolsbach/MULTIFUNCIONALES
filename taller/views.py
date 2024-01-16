from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Template, Context, loader 
from django.shortcuts import render
from taller.forms import * #En el caso que se use formulario importar el archivo
from taller.models import *
import datetime

def index(request):
    inicio = Tecnico.objects.all()
    plantilla = loader.get_template("taller/index.html")
    context = {
        'Tecnico' : Tecnico,
    }
    return HttpResponse(plantilla.render(context, request))

def Cliente(request):
    return render(request, 'taller/cliente.html')

def Equipo(request):
    return render(request, 'taller/equipo.html')

def Tecnico(request):
    return render(request, 'taller/tecnico.html')



# Create your views here.
