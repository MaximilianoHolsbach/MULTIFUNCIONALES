from django.db import models

class Equipo(models.Model):
    modelo = models.CharField(max_length=40)
    serie = models.CharField(max_length=40)
    contador = models.IntegerField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField()

class Tecnico(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField()

# Create your models here.
