from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=500)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    thumbnail = models.URLField()
    date_added = models.DateTimeField(timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




