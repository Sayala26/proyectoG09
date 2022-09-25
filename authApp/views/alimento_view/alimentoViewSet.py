from rest_framework import viewsets, permissions
from authApp.models.alimento import Alimento
from authApp.serializers.alimentoSerializer import AlimentoSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    permission_classes = [permissions.AllowAny]