from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image
import requests
from where_to_go.settings import BASE_DIR
from os.path import join


class Command(BaseCommand):
    help = 'Add place and images to db from json.'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        url = options['json_url']
        response = requests.get(url)
        response.raise_for_status()
        about_place = response.json()
        place, created = Place.objects.update_or_create(
            title=about_place['title'],
            lat=about_place['coordinates']['lat'],
            lon=about_place['coordinates']['lng'],
            short_description=about_place['description_short'],
            long_description=about_place['description_long']
        )
        for image in place.images.all():
            image.delete()
        for img_url in about_place['imgs']:
            response = requests.get(img_url)
            response.raise_for_status()
            content = ContentFile(response.content)
            img = Image.objects.create(
                place=place, 
            )
            img.file.save(name='img', content=content, save=True)
        
