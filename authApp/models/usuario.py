from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=50)