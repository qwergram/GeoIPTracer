from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
import socket
from urllib.parse import urlparse
from .models import URL_Log, IP_Geo, IPConnections
import requests

# Create your views here.

# API_ENDPOINT = "http://ip-api.com/json/" # went offline
API_ENDPOINT = 'http://api.db-ip.com/addrinfo?api_key=2faad936d61df0c9bab30fff367490e5007d2ef5&addr='


def index_view(request, *args, **kwargs):
    return render(request, "miner/index.html", {})


def api_ip(request):
    raise Http404

def new_path(request):

    # I should make an actual form for this
    from_ip = request.GET.get('from_ip')
    to_ip = request.GET.get('to_ip')

    for ip in (from_ip, to_ip):
        api_data = requests.get(API_ENDPOINT + ip).json()
        geo_data = requests.get('http://nominatim.openstreetmap.org/search?format=json&q={}'.format("%20".join(api_data['city'].split() + [api_data['stateprov']])), headers={'User-agent': "CodeFellows App"}).json()
        geo_data.append({})
        IP_Geo.objects.get_or_create(
            ip=ip,
            city=api_data.get('city', 'na'),
            region=api_data.get('stateprov', 'na'),
            country=api_data.get('country', 'na'),
            zipcode=0,
            lat=geo_data[0].get('lat', 0),
            lon=geo_data[0].get('lon', 0),
            isp='na',
            org='na',
        )

    new_connection = IPConnections(
        from_ip=from_ip,
        to_ip=to_ip
    )
    new_connection.save()


    return JsonResponse({"status": "ok"}, safe=False)


def current_geojson(request):

    to_return = {
        "type": "FeatureCollection",
        "features": []
    }

    # for ipgeo in IP_Geo.objects.all():
    #     to_return['features'].append({
    #         "type": "Feature",
    #         "properties": {},
    #         "geometry": {
    #             "type": "Point",
    #             "coordinates": [
    #                 ipgeo.lon,
    #                 ipgeo.lat
    #             ]
    #         }
    #     })
    for ipconn in IPConnections.objects.all():
        if (IP_Geo.objects.get(ip=ipconn.from_ip).lon and IP_Geo.objects.get(ip=ipconn.from_ip).lat and IP_Geo.objects.get(ip=ipconn.to_ip).lon and IP_Geo.objects.get(ip=ipconn.to_ip).lat):
            to_return['features'].append({
                "type": "Feature",
                "properties": {
                    "from_ip": ipconn.from_ip,
                    "to_ip": ipconn.to_ip,
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [
                            IP_Geo.objects.get(ip=ipconn.from_ip).lon,
                            IP_Geo.objects.get(ip=ipconn.from_ip).lat
                        ],
                        [
                            IP_Geo.objects.get(ip=ipconn.to_ip).lon,
                            IP_Geo.objects.get(ip=ipconn.to_ip).lat
                        ]
                    ]
                }
            })

    return JsonResponse(to_return)
