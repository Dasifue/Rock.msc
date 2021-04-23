from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'жанр')
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Band(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    name = models.CharField(max_length=50, verbose_name='название группы')
    description = models.TextField(max_length=2000, verbose_name = 'описание')
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'имя')
    last_name = models.CharField(max_length=50, verbose_name = 'фамилия')
    instrument = models.CharField(max_length=30, verbose_name = 'инструмент')
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'

class Album(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'название альбома')
    band = models.ForeignKey(Band, related_name='albums', on_delete = models.CASCADE)
    description = models.TextField(max_length=2000, verbose_name='описание', null=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"


class Song(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'название песни')
    genre = models.ManyToManyField(Genre, max_length=200, verbose_name = 'жанр')
    lyrics = models.TextField(max_length=3000, verbose_name = 'текст')
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    description = models.TextField(max_length=4000, verbose_name = 'описание', blank=True, null=True)
    audio_file = models.FileField(upload_to='music', blank=True, null=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'песня'
        verbose_name_plural = 'песни'


    