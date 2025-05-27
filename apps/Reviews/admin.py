from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewList(admin.ModelAdmin):
    list_display = ('rate', 'media', 'user', 'comment')
    list_per_page = 100 

admin.register(Review, ReviewList)
