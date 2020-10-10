from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser



# Register your models here.
class CustomUserAdmin(UserAdmin):
    
admin.site.register(get_user_model(), CustomUserAdmin)