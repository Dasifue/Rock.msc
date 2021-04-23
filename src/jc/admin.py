from django.contrib import admin
from .models import Person, Song, Band, Genre, Album
# Register your models here.


admin.site.register(Person)
admin.site.register(Song)
admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Album)