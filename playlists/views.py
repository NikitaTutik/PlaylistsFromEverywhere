import datetime
from django.shortcuts import render
from .models import Playlist
import requests
from django.conf import settings
from django.contrib.auth.models import User


def home(request):
    playlist_content = []

    if request.method == 'POST':
        playlist_url = 'https://www.googleapis.com/youtube/v3/playlists'
        URL = 'https://www.googleapis.com/youtube/v3/playlistItems'

        search_params = {
            'part': 'snippet',
            'key': settings.YOUTUBE_DATA_API_KEY,
            'type': 'video',
            'id': request.POST['search']
        }

        playlist_ids = []
        playlist_title = []
        r = requests.get(playlist_url, params=search_params)
        results = r.json()['items']

        for result in results:
            playlist_ids.append(result['id'])
            playlist_title.append(result['snippet']['title'])

        params = {'part': 'snippet',
                  'playlistId': "".join(playlist_ids),
                  'q': request.POST['search'],
                  'key': settings.YOUTUBE_DATA_API_KEY,
                  'maxResults': 25}

        r = requests.get(URL, params=params)
        results = r.json()['items']

        for result in results:
            video_data = {

                'title': result['snippet']['title'],
                'url': result['id'],
                'thumbnail': result['snippet']['thumbnails']['high']['url']
            }

            playlist_content.append(video_data)
            Playlist.objects.create(playlist_name="".join(playlist_title),
                                    title=result['snippet']['title'],
                                    content=result['id'],
                                    thumbnail=result['snippet']['thumbnails']['high']['url'],
                                    author_id=request.user.id,
                                    date_added=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    context = {'playlist': playlist_content}
    return render(request, 'playlists/home.html', context)

def about(request):
    return render(request, 'playlists/about.html')
