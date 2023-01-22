from django.db import models

class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=200)
    place_id = models.CharField(verbose_name='ID места', max_length=200)
    lat = models.FloatField(verbose_name='Геог. ширина')
    lon = models.FloatField(verbose_name='Геог. долгота')

    def __str__(self) -> str:
        return self.title