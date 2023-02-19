from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.http.response import JsonResponse
from django.urls import reverse


def index(request):
    output_data = {
      "type": "FeatureCollection",
      "features": []
    }
    for place in Place.objects.all():
        place_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place-json', args=[place.id])
            }
        }
        output_data['features'].append(place_data)
    return render(request, 'index.html', {'geo_points' : output_data})

def about_place(request, id):
    place = get_object_or_404(Place.objects.prefetch_related(), id=id)
    imgs = []
    for image in Image.objects.filter(place=place):
        imgs.append(image.file.url)
    response_data = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})