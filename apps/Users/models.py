from django.db import models
from django.contrib.auth.models import BaseUserManager


class Type(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

class User(BaseUserManager):
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='user_profile_photo/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='users') 
    
    def __str__(self):
        return self.username
    


