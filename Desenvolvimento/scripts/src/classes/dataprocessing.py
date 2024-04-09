"""Este módulo é responsável por carregar, fazer a limpeza e adequar os dados ao padrão que será utilizado no projeto.
"""
#Biblioteca padrão
import json
import csv
import shapefile
#Módulos de terceiros
import pandas as pd

class DataContainer():
    def __init__(self):
        pass
    
    def read_json(self, file_path):
        """
        Lê arquivo JSON.

        Args:
            file_path (str): Caminho para o arquivo JSON

        Returns:
            dict: Dados lidos do arquivo JSON
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    
    def read_csv(self, file_path, *,as_dataframe=False):
        """
        Lê dados de arquivo CSV
        
        Args:
            file_path (str): Caminho para o arquivo CSV  

        Returns:
            list: Dados lidos do .CSV
        """
        if as_dataframe:
            data = pd.read_csv(file_path)
        else:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
        return data
    
    def read_shapefile(self, file_path):
        """
        Lê dados de arquivo Shapefile
    
        Args:
            file_path (str): Caminho para o arquivo .shp 

        Returns:
            list: Dados lidos do .shp
        """
        sf = shapefile.Reader(file_path)
        data = []
        for shape in sf.shapes():
            attributes = dict(zip([field[0] for field in sf.fields[1:]], shape.record)) #dict de atributos contidos no shapefile
            geometry = shape.__geo_interface__ #Protocolo Python para representar geometria
            data.append({'geometry': geometry, 'attributes': attributes})
        return data

class Cleanser():
    def __init__():
        pass
    
    def NanValueAddresses():
        """Tratamento dos registros de endereço sem valor, seja número ou rua.
        """

class Formatter():
    pass