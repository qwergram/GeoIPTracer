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

    def as_geojson(self):
        return {
            "type": "Feature",
            "properties": {},
            "type": "Point",
            "coordinates": [
                self.lon,
                self.lat
            ]
        }

class IP_Geo(models.Model):

    class Meta:
        verbose_name = "IP Record"

    ip = models.GenericIPAddressField(unique=True)
    location = models.ForeignKey("Location")


class URL_Log(models.Model):

    class Meta:
        verbose_name = "URL Record"

    url = models.URLField(unique=True)
    ip = models.ManyToManyField("IP_Geo", related_name="urls")


class HTML_Log(models.Model):

    class Meta:
        verbose_name = "HTML Record"

    url = models.ForeignKey("URL_Log", related_name="html")
    html = models.TextField()
    urls = models.ManyToManyField("URL_Log", related_name="appears_in")
    time_taken = models.DateTimeField(auto_now=True)
