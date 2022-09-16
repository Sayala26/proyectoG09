from django.db import models

class Limpieza(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=100)
