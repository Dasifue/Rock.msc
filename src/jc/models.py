from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'жанр')
    description = models.TextField(max_length=2000, verbose_name = 'описание', blank=True, null=True)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return f'{self.name}'


class Band(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    name = models.CharField(max_length=50, verbose_name='название группы')
    description = models.TextField(max_length=2000, verbose_name = 'описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
    
    def __str__(self):
        return f"{self.name}"

class Person(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    name = models.CharField(max_length=50, verbose_name = 'имя')
    last_name = models.CharField(max_length=50, verbose_name = 'фамилия')
    instrument = models.CharField(max_length=30, verbose_name = 'инструмент')
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    info = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'

    def __str__(self):
        return f"{self.name, self.last_name}"   

class Album(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    name = models.CharField(max_length=100, verbose_name = 'название альбома')
    band = models.ForeignKey(Band, related_name='albums', on_delete = models.CASCADE)
    description = models.TextField(max_length=2000, verbose_name='описание', null=True)
    
    class Meta:
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"

    def __str__(self):
        return f"{self.name}"


class Song(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'название песни')
    genre = models.ManyToManyField(Genre, max_length=200, verbose_name = 'жанр')
    lyrics = models.TextField(max_length=3000, verbose_name = 'текст')
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    description = models.TextField(max_length=4000, verbose_name = 'описание', blank=True, null=True)
    audio_file = models.FileField(upload_to='music', blank=True, null=True)
    
    class Meta:
        verbose_name = 'песня'
        verbose_name_plural = 'песни'
    
    def __str__(self):
        return f"{self.name}"



class Comment(models.Model):
    author = models.CharField(max_length = 50, verbose_name='автор')
    text = models.TextField(max_length=500, verbose_name='текст')
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
    
    def __str__(self):
        return f"{self.author}"
    