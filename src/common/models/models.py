from django.db import models


class videos(models.Model):
    videoId = models.CharField(max_length=50, primary_key=True)
    channelId = models.CharField(max_length=50)
    title = models.CharField(max_length=200, default='')
    description = models.TextField()

