from django.db import models

class Cocina(models.Model):
    id_pro_cocina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=100)