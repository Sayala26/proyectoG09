from rest_framework import serializers
from authApp.models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id_proveedor', 'nombre', 'telefono', 'direccion', 'correo', 'producto', 'fecha', 'precio_total')
        extra_kwargs = {
            'nombre': {'required': True},
            'telefono': {'required': True},
            'direccion': {'required': True},
            'correo': {'required': True},
            'producto': {'required': True},
            'fecha': {'required': True},
            'precio_total': {'required': True},
        }