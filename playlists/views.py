from django.shortcuts import render
from .models import Playlist

def home(request):
    context = {'playlists': Playlist.objects.all()}
    return render(request, 'playlists/home.html', context)

def about(request):
    return render(request, 'playlists/about.html')
