from rest_framework import serializers
from authApp.models import Limpieza

class LimpiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limpieza
        fields = ('id_pro_limpieza', 'nombre', 'cantidad', 'precio', 'proveedor')
        extra_kwargs = {
            'nombre': {'required': True},
            'cantidad': {'required': True},
            'precio': {'required': True},
            'proveedor': {'required': True},
        }