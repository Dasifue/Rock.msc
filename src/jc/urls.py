from .views import all_bands, band_info, song_info, song_filter, album_info
from django.urls import path, include

app_name = 'jc'

urlpatterns = [
    path('all_bands/', all_bands, name='all_bands'),
    path('band_info/<int:band_id>', band_info, name = 'band_info'),
    path('song_info/<int:song_id>', song_info, name = 'song_info'),
    path('song_filter/<int:genre_id>', song_filter, name='song_filter'),
    path('album_info/<int:album_id>', album_info, name = 'album_info'),
]