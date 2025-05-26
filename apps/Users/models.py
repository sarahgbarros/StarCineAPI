from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class TypeUser(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Usuário'
        verbose_name_plural = 'Tipos de Usuário'

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='user_profile_photo/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.ForeignKey(TypeUser, on_delete=models.CASCADE, related_name='users')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    
    def is_moderador(self):
        return self.user_type.name.lower() == 'moderador'

    def is_admin(self):
        return self.user_type.name.lower() == 'admin'

    def is_comum(self):
        return self.user_type.name.lower() == 'comum'
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'