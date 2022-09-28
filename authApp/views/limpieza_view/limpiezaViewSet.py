from rest_framework import viewsets, permissions
from authApp.models.limpieza import Limpieza
from authApp.serializers.limpiezaSerializer import LimpiezaSerializer

class LimpiezaViewSet(viewsets.ModelViewSet):
    queryset = Limpieza.objects.all()
    serializer_class = LimpiezaSerializer
    permission_classes = [permissions.AllowAny]