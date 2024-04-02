from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        if not password:
            raise ValueError('Password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Artist(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, default='')
    nickname = models.CharField(max_length=100, unique=True, null=True, blank=True, default=None)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='artist')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='artist_user_permissions',
        blank=True,
        help_text="Specific permissions for this artist.",
        verbose_name='user permissions',
    )

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} {self.nickname if self.nickname else ""} {self.is_active}'


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    song_file = models.FileField(upload_to='static/songs', null=False, blank=False, default='')

    def __str__(self):
        return f'{self.artist} - {self.title}'


class Album(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    songs = models.ManyToManyField(Song, null=False, blank=False, default='')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images', null=True)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'


class Playlist(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
