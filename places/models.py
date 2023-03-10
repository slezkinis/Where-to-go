from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=200)
    short_description = models.CharField(verbose_name='Короткое описание', max_length=1000, blank=True)
    long_description = HTMLField(verbose_name='Описание', blank=True)
    lat = models.FloatField(verbose_name='Геог. широта')
    lon = models.FloatField(verbose_name='Геог. долгота')

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='Место', related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(verbose_name='Картика')
    order = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=False,
    )

    class Meta:
        ordering = ['order']    

    def __str__(self) -> str:
        return self.place.title
