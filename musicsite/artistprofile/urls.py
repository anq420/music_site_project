from django.urls import path
from artistprofile.views import MainView, RegistrationView, LoginView, LogOutView, ProfileView, SettingsView, MakePlaylistView, PlaylistView, AllPlaylistsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('sign-up/', RegistrationView.as_view(), name='sign-up'),
    path('sign-in/', LoginView.as_view(), name='sign-in'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/<int:id>/', ProfileView.as_view(), name='profile'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('create/', MakePlaylistView.as_view(), name='makeplaylist'),
    path('playlist/<int:id>/', PlaylistView.as_view(), name='playlist'),
    path('playlists/', AllPlaylistsView.as_view(), name='allplaylists'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
