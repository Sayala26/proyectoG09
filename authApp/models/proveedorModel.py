from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    fecha = models.DateField()
    precio_total = models.IntegerField()