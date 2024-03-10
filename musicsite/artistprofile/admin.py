from django.contrib import admin
from artistprofile.models import Genre, Artist, Album, Song


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'nickname', 'city', 'country')
    search_fields = ('first_name', 'last_name', 'nickname', 'city', 'country')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title','release_date')
    search_fields = ('artist', 'title', 'songs')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title')
    search_fields = ('artist', 'title', 'genres')
