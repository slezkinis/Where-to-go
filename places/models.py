from django.db import models

class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=200)
    place_id = models.CharField(verbose_name='ID места', max_length=200, blank=True)
    description_short = models.CharField(verbose_name='Короткое описание', max_length=200, blank=True)
    description_long = models.TextField(verbose_name='Описание', blank=True)
    lat = models.FloatField(verbose_name='Геог. ширина')
    lon = models.FloatField(verbose_name='Геог. долгота')

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    title = models.CharField(verbose_name='Имя картинки', max_length=200)
    place = models.ForeignKey(Place, verbose_name='Место', related_name='images', on_delete=models.CASCADE, blank=True, default=0)
    file = models.ImageField(verbose_name='Картика')
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']    

    def __str__(self) -> str:
        return self.title
