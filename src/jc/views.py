import requests
import datetime
from django.shortcuts import render, redirect
from .models import Person, Song, Band, Genre, Album, Comment
from jc.forms import CreateCommentForm
from django.conf import settings

#   BANDS
def get_core_html_data():
    genres = Genre.objects.all()
    bands = Band.objects.all()
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")
    return {'bands':bands, 'genres':genres, 'time':time}

def all_bands(request):
    bands = Band.objects.all()
    songs = Song.objects.all()
    return render(request, 'all_bands.html', {'dropdown': get_core_html_data(), 'songs':songs, 'bands':bands})

def band_info(request, band_id):
    band = Band.objects.get(id = band_id)
    members = Person.objects.filter(band = band_id)   
    albums = Album.objects.filter(band = band_id)
    return render(request, 'band_info.html', {'band':band, 'albums':albums, 'members':members, 'dropdown': get_core_html_data()})

#   SONGS
def song_playlist(request, band_id):
    songs = Song.objects.filter(album__band_id = band_id)
    all_songs = Song.objects.all()
    return render(request, 'playlist.html', {'songs':songs, 'all_songs':all_songs, 'dropdown': get_core_html_data()})

def all_songs(request):
    songs = Song.objects.all()
    return render(request, 'playlist.html', {'songs':songs, 'dropdown': get_core_html_data()})
    
def song_info(request, song_id):
    song_inf = Song.objects.filter(id=song_id)
    return render(request, 'song_info.html', {'song_inf':song_inf, 'dropdown': get_core_html_data()})

def song_filter(request, genre_id):
    songs = Song.objects.filter(genre = genre_id)
    genre = Genre.objects.get(id = genre_id)
    return render(request, 'song_filter.html', {'songs':songs, 'genre':genre, 'dropdown': get_core_html_data()})

def album_info(request, album_id):
    songs = Song.objects.filter(album = album_id)
    album = Album.objects.get(id=album_id)
    return render(request, 'album_info.html', {'songs':songs, 'album':album, 'dropdown': get_core_html_data()})    

#Create comment
def create_comment(request):
    form = CreateCommentForm()
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        save_form = CreateCommentForm(request.POST)
        if save_form.is_valid():
            note = save_form.save(commit=False)
            note.save()
            print(settings.URL+'author'+'text')
            res = requests.get(settings.URL+f'{author}\n{text}')
            print(res)
            return redirect('jc:all_bands')
    return render(request, 'create_comment.html', {'form':form, 'dropdown': get_core_html_data() })


#   persons

def person_info(request, person_id):
    person = Person.objects.get(id = person_id)
    return render(request, 'person_info.html', {'person':person, 'dropdown': get_core_html_data()})

# search
def search(request):
    query = request.GET.get('q')
    bands = Band.objects.filter(name__icontains=query)
    songs = Song.objects.filter(name__icontains=query)
    return render(request, 'search_result.html', {'bands':bands, 'songs':songs})