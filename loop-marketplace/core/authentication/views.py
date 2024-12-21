# We import the libraries.
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoginSerializer, UserSerializer

# Clase de inicio de seccion. 
class LoginView(APIView):
    """def get(self, request):
        return Response({}, status.HTTP_405_METHOD_NOT_ALLOWED)
    """
    serializer_class = LoginSerializer
    
    # Método POST.
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        
        # Nos ayuda a iniciar sección. 
        user = authenticate(
            request, 
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password']
            )
        
        #Validamos el inicio de sección. 
        if user is not None:
            user.last_login = datetime.now()
            user.save()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        else: 
            return Response(
                {
                    "error": "401 Unauthorized",   
                    "message": "The credentiales provided are not valid. Please review your information and try again"              
                },
                status = status.HTTP_401_UNAUTHORIZED)
    
    