from authApp.models.proveedor import Proveedor
from rest_framework import serializers

class ProveedorSerializer(serializers.ModelSerializer):
 class Meta:
    model = Proveedor
    # (va entre parentesis provemos con[])
    fields = ['nombre','telefono', 'direccion', 'correo','producto','fecha_compra','precio_total']