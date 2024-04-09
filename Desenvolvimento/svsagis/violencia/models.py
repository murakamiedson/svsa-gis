from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Person(models.Model):
    '''Classe que representa as pessoas presentes no banco de dados.
    def __str__() ->
    def coordinates -> deve fazer o geocoding do endereço e retornar as coordenadas do local onde vive.
    '''
    name = models.CharField(max_length=100)
    abuse_description = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Location(models.Model):
    point = gis_models.PointField()
    address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=100)

    def __str__(self):
        return self.name
