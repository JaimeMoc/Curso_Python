from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create Model CustomUser 
class CustomUser(AbstractUser):
    
    class Meta:
        ordering = ['pk']
    
    username = models.CharField(max_length = 50, unique = True, null = False)
    email = models.EmailField(max_length = 130, unique = True, null = False) # Verifica si el correo es válido.
    phone_number = models.CharField(max_length = 13, null = True , blank = True)
    
    USERNAME_FIELD= 'email' #Modificamos para que el acceso sea con el correo y no con el nombre de usuario.
    REQUIRED_FIELDS = ['username', 'password']
    
    def __str__(self):
        return f"{self.username} - {self.email}"
