from django.urls import path
from .views import PlaylistGetView

urlpatterns = [
    path('',PlaylistGetView.as_view(),name = "playlists")
]
