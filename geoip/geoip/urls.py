"""geoip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from miner.views import (
    index_view,
    form_submission,
    test,
    query,
    get_urls,
    api_ip
)

bot_api_endpoints = [
    url(r'^api/ip/$', api_ip),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index"),
    url(r'^submit/$', form_submission, name="submit"),
    url(r'^test/$', test, name="test"),
    url(r'^query/', query, name="query"),
    url(r'^urls/', get_urls, name="urls"),
] + bot_api_endpoints
