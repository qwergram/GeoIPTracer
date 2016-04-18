from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
import requests
import socket
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Create your views here.

API_ENDPOINT = "http://ip-api.com/json/"


def get_urls(request, *args, **kwargs):
    url = request.GET.get('url')
    if url:
        data = requests.get(url)
        if not data.ok:
            raise Http404("Bad url")
        soup = BeautifulSoup(data.text)
        urls = soup.find_all("a", href=True)
        to_return = []
        for url in urls:
            url = url.get("href")
            if url.startswith('http'):
                to_return.append(url)
        return JsonResponse(to_return, safe=False)
    raise Http404("no url")

def query(request, *args, **kwargs):
    url = request.GET.get('url')
    if url:
        url = urlparse(url).netloc
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
