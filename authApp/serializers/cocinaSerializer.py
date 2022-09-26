from authApp.models.cocina import Cocina 
from rest_framework import serializers

class CocinaSerializer(serializers.ModelSerializer):
 class Meta:
    model = Cocina
    fields = ['nombre', 'cantidad', 'precio','proveedor']