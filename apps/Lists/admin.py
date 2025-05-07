from django.contrib import admin
from .models import List, ListCategory

class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'media', 'is_active',)
    list_filter = ('id', 'category', 'media', 'is_active',)
    search_fields = ('id', 'category', 'media', 'is_active',)

class ListCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)

admin.site.register(List, ListAdmin)
admin.site.register(ListCategory, ListCategoryAdmin)