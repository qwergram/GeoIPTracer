from django.db import models

# Create your models here.


class IP_Geo(models.Model):

    class Meta:
        verbose_name = "IP Record"

    def __str__(self):
        return self.ip

    ip = models.GenericIPAddressField(unique=True)
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

class IPConnections(models.Model):

    # class Meta:
        # unique_together = (from_ip, to_ip,)

    from_ip = models.GenericIPAddressField()
    to_ip = models.GenericIPAddressField()

    def __str__(self):
        return self.from_ip + ' -> ' + self.to_ip


class URL_Log(models.Model):

    class Meta:
        verbose_name = "URL Record"

    url = models.URLField(unique=True)
    ip = models.ManyToManyField("IP_Geo", related_name="urls")
    connections = models.ManyToManyField("URL_Log")


class HTML_Log(models.Model):

    class Meta:
        verbose_name = "HTML Record"

    url = models.ForeignKey("URL_Log", related_name="html")
    html = models.TextField()
    urls = models.ManyToManyField("URL_Log", related_name="appears_in")
    time_taken = models.DateTimeField(auto_now=True)
