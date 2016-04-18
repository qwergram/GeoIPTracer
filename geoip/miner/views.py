from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import requests
import socket

# Create your views here.

API_ENDPOINT = "http://ip-api.com/json/"


def query(request, *args, **kwargs):
    url = request.GET.get('url')
    if url:
        url = url.replace("http://", "")
        url = url.replace("https://", "")
        ips = socket.gethostbyname_ex(url)[2]
        data = []
        for ip in ips:
            api_data = requests.get(API_ENDPOINT + ip).json()
            data.append({
                "url": url,
                "ip": ip,
                "lat": api_data['lat'],
                "lon": api_data['lon'],
                "co": api_data['country']
            })
        return render(request, "miner/query.html", {"data": data})
    raise Http404("url not included")


def test(request):
    return HttpResponse("test")


def index_view(request, *args, **kwargs):
    return render(request, "miner/index.html", {})


def form_submission(request, *args, **kwargs):
    url = request.GET.get('url', False)
    if url:
        return render(request, "miner/results.html", {"url": url})
    return redirect("index")
