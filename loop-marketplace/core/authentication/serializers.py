#We import the libraries.
from rest_framework import serializers
from .models import CustomUser

# Clase iniciar sección. 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

# Clase de usuario.    
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True)
    #last_login = serializers.CharField(required=True) Para el signup
    profile_type = serializers.CharField(required=True, write_only = True)
    
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    # Funcion que nos ayuda a validar si se crea el usuario. 
    def create(self, validated_data):
        print("Creando un usuario")
        profile_type = validated_data.pop('profile_type', None) 
        #print(profile_type)
        return super().create(validated_data), profile_type
