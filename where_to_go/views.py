from django.shortcuts import render
from places.models import Place, Image


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
                "coordinates": [place.lat, place.lon],
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        }
        output_data['features'].append(place_data)
    return render(request, 'index.html', {'geo_points' : output_data})




#     {
#       "type": "FeatureCollection",
#       "features": [
#         {
#           "type": "Feature",
#           "geometry": {
#             "type": "Point",
#             "coordinates": [37.62, 55.793676]
#           },
#           "properties": {
#             "title": "«Легенды Москвы",
#             "placeId": "moscow_legends",
#             "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
#           }
#         },
#         {
#           "type": "Feature",
#           "geometry": {
#             "type": "Point",
#             "coordinates": [37.64, 55.753676]
#           },
#           "properties": {
#             "title": "Крыши24.рф",
#             "placeId": "roofs24",
#             "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
#           }
#         }
#       ]
#     }