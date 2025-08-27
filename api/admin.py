from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_year', 'rating', 'created_at']
    list_filter = ['genre', 'release_year', 'rating']
    search_fields = ['title', 'genre']
    ordering = ['-created_at']
