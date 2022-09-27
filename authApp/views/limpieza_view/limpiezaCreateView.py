#from rest_framework.response import Response

from authApp import views
from authApp.serializers.limpiezaSerializer import LimpiezaSerializer
from rest_framework.response import Response

class limpiezaCreateView(views):
    def create_limpieza(self, request, *args, **kwargs):
        serializer = LimpiezaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Modulo de registro de limpieza', serializer.validated_data)