from authApp.models.alimento import Alimento
from rest_framework import serializers

class AlimentoSerializer(serializers.ModelSerializer):
 class Meta:
    model = Alimento
    fields = ['nombre', 'categoria', 'cantidad','precio','proveedor']