from .views import all_bands, band_info, song_info, song_filter, album_info, create_comment, person_info, song_playlist, all_songs
from django.urls import path, include

app_name = 'jc'

urlpatterns = [
    path('all_bands/', all_bands, name='all_bands'),
    path('band_info/<int:band_id>', band_info, name = 'band_info'),
    path('song_info/<int:song_id>', song_info, name = 'song_info'),
    path('song_filter/<int:genre_id>', song_filter, name='song_filter'),
    path('album_info/<int:album_id>', album_info, name = 'album_info'),
    path('create_comment/', create_comment, name='create_comment'),
    path('person/<int:person_id>', person_info, name= 'person_info'),
    path('playlist/<int:band_id>', song_playlist, name='song_playlist'),
    path('playlist/', all_songs, name = 'all_songs')
]