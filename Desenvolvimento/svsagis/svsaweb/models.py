from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class MapLocation(models.Model):
    #Localização no mapa
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    zoom = models.IntegerField()
  
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    cd_mun = models.CharField(max_length=7)
    nm_mun = models.CharField(max_length=50)
    sigla_uf = models.CharField(max_length=2)
    area_km2 = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    location = models.OneToOneField(MapLocation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(null = True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
