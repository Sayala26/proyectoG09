from rest_framework import viewsets, permissions
from authApp.models.proveedor import Proveedor
from authApp.serializers.proveedorSerializer import ProveedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    #cuando usemos tokens
    permission_classes = [permissions.AllowAny]