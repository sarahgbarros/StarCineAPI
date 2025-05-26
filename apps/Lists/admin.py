from django.contrib import admin
from .models import List, ListCategory

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('user', 'media',)

@admin.register(ListCategory)
class ListCategoryList(admin.ModelAdmin):
    list_display = ('name',)

admin.register(List, ListAdmin)
admin.register(ListCategory, ListCategoryList)