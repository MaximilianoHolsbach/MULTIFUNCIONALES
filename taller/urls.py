from taller.views import *
from django.urls import path

urlpatterns = [
    path('',index, name="inicio"),
    path('cliente/',Cliente, name="Cliente"),
    path('equipo/',Equipo, name="Equipo"),
    path('tecnico/',Tecnico, name="Tecnico"),
]