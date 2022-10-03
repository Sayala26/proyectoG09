from rest_framework import serializers
from authApp.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('usuario_id', 'nombre', 'usuario', 'correo', 'contraseña')