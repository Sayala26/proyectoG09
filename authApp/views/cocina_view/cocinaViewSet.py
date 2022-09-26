from rest_framework import viewsets, permissions
from authApp.models.cocina import Cocina
from authApp.serializers.cocinaSerializer import CocinaSerializer

class CocinaViewSet(viewsets.ModelViewSet):
    queryset = Cocina.objects.all()
    serializer_class = CocinaSerializer
    permission_classes = [permissions.AllowAny]