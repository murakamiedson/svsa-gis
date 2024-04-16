from django.contrib.gis.utils import LayerMapping
from .models import City
from django.contrib.gis.gdal import DataSource
from pathlib import Path
from svsaweb import City

city_mapping = {
    'cd_mun': 'CD_MUN',
    'nm_mun': 'NM_MUN',
    'sigla_uf': 'SIGLA_UF',
    'area_km2': 'AREA_KM2',
    'geom': 'MULTIPOLYGON',
}

city_shp = Path(City.__file__).resolve().parent.parent / 'data' / 'mapa-salto.shp'
ds = DataSource(city_shp)

def run(verbose=True):
    lm = LayerMapping(
        City, city_shp, city_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)