#from rest_framework.response import Response

from authApp import views
from authApp.serializers.cocinaSerializer import CocinaSerializer
from rest_framework.response import Response

"""class cocinaCreateView(views):
    def create_cocina(self, request, *args, **kwargs):
        serializer = CocinaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Modulo de registro de cocina', serializer.validated_data)"""