from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_view(request, *args, **kwargs):
    return render(request, "miner/index.html", {})
