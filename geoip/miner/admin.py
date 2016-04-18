from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Location)
admin.site.register(IP_Geo)
admin.site.register(URL_Log)
admin.site.register(HTML_Log)
