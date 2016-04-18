from django.db import models

# Create your models here.


class Location(models.Model):

    class Meta:
        unique_together = ("lat", "lon")

    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipcode = models.IntegerField()

    lat = models.FloatField()
    lon = models.FloatField()

    isp = models.CharField(max_length=255)
    org = models.CharField(max_length=255)


class IP_Geo(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    location = models.ForeignKey(Location)


class URL_Log(models.Model):
    url = models.URLField(unique=True)
    ip = models.ManyToManyField(IP_Geo)


class HTML_Log(models.Model):
    url = models.ForeignKey(URL_Log)
    html = models.TextField()
    URLS = models.ManyToManyField(URL_Log)
    time_taken = models.DateTimeField(auto_now=True)
