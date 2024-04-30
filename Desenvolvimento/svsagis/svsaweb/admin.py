from django.contrib import admin
from .models import MapLocation, City, Neighborhood, Incidence
# Register your models here.

class IncidenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')



admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(MapLocation)
admin.site.register(City)
admin.site.register(Neighborhood)