from rest_framework import serializers
from authApp.models import Cocina

class CocinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocina
        fields = ('id_pro_cocina', 'nombre', 'cantidad', 'precio', 'proveedor')
        extra_kwargs = {
            'nombre': {'required': True},
            'cantidad': {'required': True},
            'precio': {'required': True},
            'proveedor': {'required': True},
        }