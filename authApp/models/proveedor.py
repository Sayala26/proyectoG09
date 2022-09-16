from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono=models.IntegerField()
    direccion= models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    producto=models.CharField(max_length=100)
    fecha_compra= models.DateField()
    precio_total = models.IntegerField()
    