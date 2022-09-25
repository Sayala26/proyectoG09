
#from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.response import Response

from authApp.serializers.alimentoSerializer import AlimentoSerializer

class AlimentoCreateView(views.APIView):
     def post(self, request, *args, **kwargs):
        serializer = AlimentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

