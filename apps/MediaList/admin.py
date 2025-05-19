from django.contrib import admin
from .models import Media, MediaCategory, MediaProduction

@admin.register(Media)
class MediaList(admin.ModelAdmin):
    list_display = ('title', 'category', 'production', 'classification')
    list_filter = ('title', 'category')
    list_per_page = 100


@admin.register(MediaCategory)
class MediaCategoryList(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_per_page = 100


@admin.register(MediaProduction)
class MediaProductionList(admin.ModelAdmin):
    list_display = ('actor', 'director', 'studio')
    list_filter = ('actor', 'director', 'studio')
    list_per_page = 100


admin.register(Media, MediaList)
admin.register(MediaCategory, MediaCategoryList)
admin.register(MediaProduction, MediaProductionList)