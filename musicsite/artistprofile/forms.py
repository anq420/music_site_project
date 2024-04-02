from django import forms
from artistprofile.models import Playlist


class RegistrationForm(forms.Form):
    email = forms.EmailField(help_text='Your email address here')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Your password here')
    confirm_password = forms.CharField(widget=forms.PasswordInput, help_text='Confirm your password')

    class Meta:
        fields = ['email', 'password', 'confirm_password']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'password']


class EditProfileForm(forms.Form):
    email = forms.EmailField()
    nickname = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    city = forms.CharField(required=False)
    country = forms.CharField(required=False)

    class Meta:
        fields = ['email', 'nickname', 'first_name', 'last_name', 'city', 'country']


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'songs']
