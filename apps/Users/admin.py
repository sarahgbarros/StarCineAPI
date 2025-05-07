from django.contrib import admin
from apps.Users.models import User, Type

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active',)
    list_filter = ('id', 'username',)
    search_fields = ('id', 'username',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)

admin.site.register(User, UserAdmin)
admin.site.register(Type, TypeAdmin)