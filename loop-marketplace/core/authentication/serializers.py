from rest_framework import serializers

from .models import CustomUser

# Clase iniciar sección. 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only =True)

# Clase de usuario.    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'last_login', 'date_joined']
        