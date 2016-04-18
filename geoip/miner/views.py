from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def index_view(request, *args, **kwargs):
    return render(request, "miner/index.html", {})

def form_submission(request, *args, **kwargs):
    url = request.GET.get('url', False)
    if url:
        return render(request, "miner/results.html", {"url": url})
    return redirect("index")
