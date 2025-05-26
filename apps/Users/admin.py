from django.contrib import admin
from .models import User, TypeUser

@admin.register(TypeUser)
class TypeUserList(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(User)
class UserList(admin.ModelAdmin):
    list_display = ('username', 'name', 'email')
    list_per_page = 50

admin.register(TypeUser, TypeUserList)
admin.register(User, UserList)
