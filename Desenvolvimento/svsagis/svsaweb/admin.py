from django.contrib import admin
from .models import MapLocation, City, Neighborhood
# Register your models here.

admin.site.register(MapLocation)
admin.site.register(City)
admin.site.register(Neighborhood)