from django.db import models
from .usuario import Usuario

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Usuario, related_name='account', on_delete=models.CASCADE)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)