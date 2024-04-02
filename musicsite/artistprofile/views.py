from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.utils import IntegrityError
from artistprofile.models import Song, Artist, Album, Genre, Playlist
from artistprofile.forms import RegistrationForm, LoginForm, EditProfileForm, PlaylistForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


class MainView(View):
    def get(self, request):
        songs = Song.objects.all()
        albums = Album.objects.all()
        return render(request, 'main.html', context={'songs': songs[::-1], 'albums': albums[::-1]})


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            already_exists = Artist.objects.filter(email=email)

            if not already_exists and password == confirm_password:
                user = Artist.objects.create_user(email=email, password=password)
                user.set_password(password)
                user.save()
                return redirect('main')

            if already_exists:
                messages.error(request, 'Email already is in use')

            if password != confirm_password:
                messages.error(request, 'Passwords are not the same. Have another try.')

        return render(request, 'registration.html', context={'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)

            try:
                Artist.objects.get(email=email)
            except Artist.DoesNotExist:
                messages.error(request, 'Email is not activated')

            if user:
                login(request, user)
                print('Logged in successfully!')
                return redirect('main')

            if not user:
                messages.error(request, 'Check your password and try again')

            else:
                messages.error(request, 'It seems you entered incorrect email or password')

        return render(request, 'login.html', context={'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')


class ProfileView(View):
    def get(self, request, id, *args, **kwargs):
        artist = Artist.objects.get(id=id)
        songs = Song.objects.filter(artist__id=id)
        albums = Album.objects.filter(artist__id=id)
        return render(request, 'profile.html', context={'songs': songs, 'artist': artist, 'albums': albums})


class SettingsView(View):
    def get(self, request, *args, **kwargs):
        id = request.user.id
        artist = Artist.objects.get(id=id)
        form = EditProfileForm(initial={
            'email': artist.email,
            'nickname': artist.nickname,
            'first_name': artist.first_name,
            'last_name': artist.last_name,
            'country': artist.country,
            'city': artist.city
        })
        return render(request, 'editprofile.html', context={'form': form, 'artist': artist})

    def post(self, request, *args, **kwargs):
        form = EditProfileForm(request.POST)
        artist = Artist.objects.get(id=request.user.id)

        if form.is_valid():
            try:
                if form.cleaned_data['nickname'] == artist.nickname:
                    artist.email = form.cleaned_data['email']
                    artist.first_name = form.cleaned_data['first_name']
                    artist.last_name = form.cleaned_data['last_name']
                    artist.city = form.cleaned_data['city']
                    artist.country = form.cleaned_data['country']
                    artist.save()
                    return redirect('main')

                if form.cleaned_data['email'] == artist.email:
                    artist.nickname = form.cleaned_data['nickname']
                    artist.first_name = form.cleaned_data['first_name']
                    artist.last_name = form.cleaned_data['last_name']
                    artist.city = form.cleaned_data['city']
                    artist.country = form.cleaned_data['country']
                    artist.save()
                    return redirect('main')

                if form.cleaned_data['email'] == artist.email and form.cleaned_data['nickname'] == artist.nickname:
                    artist.first_name = form.cleaned_data['first_name']
                    artist.last_name = form.cleaned_data['last_name']
                    artist.city = form.cleaned_data['city']
                    artist.country = form.cleaned_data['country']
                    artist.save()
                    return redirect('main')

            except IntegrityError:
                messages.error(request, 'Email or nickname is already in use')

        return render(request, 'editprofile.html', context={'form': form, 'artist': artist})


class MakePlaylistView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PlaylistForm()
        return render(request, 'makeplaylist.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save()
            return redirect('playlist', playlist=playlist.id)
        else:
            form = PlaylistForm()

        return render(request, 'makeplaylist.html', context={'form': form})


class AllPlaylistsView(View):
    def get(self, request, *args, **kwargs):
        all_playlists = Playlist.objects.all()
        return render(request, 'allplaylists.html', context={'all_playlists': all_playlists})


class PlaylistView(View):
    def get(self, request, id, *args, **kwargs):
        playlist = Playlist.objects.get(id=id)
        return render(request, 'playlist.html', context={'playlist': playlist})
