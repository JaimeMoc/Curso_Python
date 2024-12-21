from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'date_joined')
    list_filter = ('date_joined',) # Creamos un filtro por fecha 
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number') 
    date_hierarchy = 'date_joined' #Mostramos el orden que se creó
    ordering = ('-id',) # Hacemos que el id aparezca el mas reciente en la tabla users.
    
    fieldsets = (
        ( None, {
               "fields": ('username', 'password')
            }
        ),
        (
            ("User Info"), {
                'fields':('first_name', 'last_name', 'email', 'phone_number')
            }
        ),
        (   ("Metadata"), {
                'fields': ('last_login', 'date_joined')
            }
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)    