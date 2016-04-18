from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def query(request, *args, **kwargs):
    return HttpResponse(request.GET.get('url', "whoops!"))


def test(request):
    return HttpResponse("test")


def index_view(request, *args, **kwargs):
    return render(request, "miner/index.html", {})


def form_submission(request, *args, **kwargs):
    url = request.GET.get('url', False)
    if url:
        return render(request, "miner/results.html", {"url": url})
    return redirect("index")
