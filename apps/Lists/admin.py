from django.contrib import admin
from apps.MediaList.models import Media
from .models import List, ListCategory

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'get_media')
    filter_horizontal = ['media'] 

    def get_media(self, obj):
        return ", ".join([m.title for m in obj.media.all()])
    get_media.short_description = 'Media'

@admin.register(ListCategory)
class ListCategoryList(admin.ModelAdmin):
    list_display = ('name',)

admin.register(List, ListAdmin)
admin.register(ListCategory, ListCategoryList)