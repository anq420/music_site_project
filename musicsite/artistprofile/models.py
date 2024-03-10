from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Artist(models.Model):
    nickname = models.CharField(max_length=100, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.nickname} {self.first_name if self.first_name else ""} {self.last_name if self.last_name else ""}'


class Song(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    genres = models.ManyToManyField(Genre, null=True, blank=True)
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.artist} - {self.title}'


class Album(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    songs = models.ManyToManyField(Song, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    genres = models.ManyToManyField(Genre, null=True, blank=True)
    image = models.ImageField(upload_to='static/images', null=True)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
