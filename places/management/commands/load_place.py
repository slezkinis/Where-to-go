from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image
import requests
from where_to_go.settings import BASE_DIR
from os.path import join


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('json_url', nargs='+', type=str)

    def handle(self, *args, **options):
        url = options['json_url'][0]
        response = requests.get(url)
        response.raise_for_status()
        about_place = response.json()
        place, created = Place.objects.get_or_create(
            title=about_place['title'],
            lat=about_place['coordinates']['lat'],
            lon=about_place['coordinates']['lng']
        )
        place.place_id = about_place['title']
        place.description_short = about_place['description_short']
        place.description_long = about_place['description_long']
        for image in Image.objects.filter(place=place):
            image.delete()
        place.save()
        for img_url in about_place['imgs']:
            img = Image.objects.create(
                title=about_place['title'],
                place=place            
            )
            response = requests.get(img_url)
            response.raise_for_status()
            content = ContentFile(response.content)
            with open(join(BASE_DIR, f'media/{about_place["title"]}.jpg'), 'wb') as file:
                file.write(response.content)
            img.file.save(f'{about_place["title"]}.jpg', content, True)
        
