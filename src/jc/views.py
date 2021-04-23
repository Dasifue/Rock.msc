from django.shortcuts import render
from .models import Person, Song, Band, Genre, Album

#   BANDS
def all_bands(request):
    genres = Genre.objects.all()
    bands = Band.objects.all()
    return render(request, 'all_bands.html', {'bands':bands,'genres':genres})

def band_info(request, band_id):
    band = Band.objects.get(id = band_id)
    members = Person.objects.filter(band=band_id)
    albums = Album.objects.filter(band=band_id)
    return render(request, 'band_info.html', {'band':band, 'albums':albums, 'members':members})



#   GENRES
def all_genres(request):
    genres = Genre.objects.all()
    return render(request, 'all_bands.html', {'genres':genres})



#   SONGS
def song_info(request, song_id):
    song_inf = Song.objects.filter(id=song_id)
    return render(request, 'song_info.html', {'song_inf':song_inf})

def song_filter(request, genre_id):
    songs = Song.objects.filter(genre = genre_id)
    return render(request, 'song_filter.html', {'songs':songs})

def album_info(request, album_id):
    songs = Song.objects.filter(album = album_id)
    album = Album.objects.get(id=album_id)
    return render(request, 'album_info.html', {'songs':songs, 'album':album})    
