from rest_framework import serializers
from authApp.models import Usuario
from authApp.models import Cuenta
from authApp.serializers.cuentaSerializer import CuentaSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    cuenta = CuentaSerializer()
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'password', 'name', 'email', 'cuenta')

    # create
    def create(self, validated_data):
        cuenta_data = validated_data.pop('cuenta')
        userInstance = Usuario.objects.create(**validated_data)
        Cuenta.objects.create(user=userInstance, **cuenta_data)
        return userInstance
    
    # read
    def to_representation(self, obj):
        user = Usuario.objects.get(id=obj.id)
        account = Cuenta.objects.get(user=obj.id)       
        return {
                    'id': user.id, 
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'account': {
                        'id': account.id,
                        'lastChangeDate': account.lastChangeDate,
                        'isActive': account.isActive
                    }
                }
    # update
    def update(self, instance, validated_data):
        cuenta_data = validated_data.pop('cuenta')
        cuenta = instance.cuenta
        CuentaSerializer.update(CuentaSerializer(), instance=cuenta, validated_data=cuenta_data)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    # delete
    def delete(self, instance):
        instance.delete()