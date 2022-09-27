from authApp.models.limpieza import Limpieza
from rest_framework import serializers

class LimpiezaSerializer(serializers.ModelSerializer):
 class Meta:
    model = Limpieza
    fields = ['nombre', 'cantidad', 'precio','proveedor']