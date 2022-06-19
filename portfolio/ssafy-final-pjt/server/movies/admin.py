from django.contrib import admin
from .models import Genre, Movie
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    fields = ['name',]

class MovieAdmin2(admin.ModelAdmin):
    fields = ['id', 'title', 'genre_ids', 'release_date', 'overview', 'poster_path',]

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin2)
