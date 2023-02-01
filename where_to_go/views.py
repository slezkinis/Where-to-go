from django.shortcuts import render, get_object_or_404, HttpResponse
from places.models import Place, Image
from django.http.response import JsonResponse



def index(request):
    output_data = {
      "type": "FeatureCollection",
      "features": []
    }
    for place in Place.objects.all().iterator():
        place_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        }
        output_data['features'].append(place_data)
    return render(request, 'index.html', {'geo_points' : output_data})

def about_place(request, place_id):
    place = get_object_or_404(Place, place_id=place_id)
    imgs = []
    for image in Image.objects.filter(place_id=place_id).iterator():
        imgs.append(request.build_absolute_uri(image.file.url))
    response_data = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})