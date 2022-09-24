
#from rest_framework.response import Response

from authApp import views
from authApp.serializers.alimentoSerializer import AlimentoSerializer
from rest_framework.response import Response


"""class alimentoCreateView(views):
    def create_alimento(self, request, *args, **kwargs):
        serializer = AlimentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Modulo de registro de alimentos', serializer.validated_data)"""