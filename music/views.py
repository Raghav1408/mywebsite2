from django.http import HttpResponse
from models import  Album, Song
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.conf.urls import include


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except:
            raise Http404("Album not found")
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist) :
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You didn't select a song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
