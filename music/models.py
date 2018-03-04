# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Album(models.Model):
    artist_Name = models.CharField(max_length=100)
    album_tittle = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    album_logo = models.CharField(max_length=500)

    def __str__(self):
        return "Artist Name : "+self.artist_Name+" Album tittle :  "+self.album_tittle


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=50)
    artist = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return "Song Name : "+self.song_name
