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

class DataProcesser():
    def __init__():
        pass

    def ProcessNumbers(self, string):
        """Trata os endereços nos quais o número está na mesma string. Remove o número dessa string e coloca na coluna 'numero' 
        
        Args: 
            string: endereço

        Returns:
            string: endereço tratado
            int: número correspondente ao endereço
        """
        index = 0
        number = ""
        for index, char in enumerate(string):
            if char.isdigit():
                break
        if index < len(string):
            number = int(string[index:])
            string = string[:index].strip()

        return string, number
        
    def NanValueAddresses(self, data):
        """Tratamento dos registros de endereço sem valor, seja número ou rua.
        Args:
            data (dataframe): Dataframe com os dados
        """
        for row in data:
            if not (pd.isna(row['endereco']) or row['endereco'] is None or
                pd.isna(row['numero']) or row['numero'] is None or row['numero']==0):
                data.dropna(subset = ['numero', 'endereco'], inplace = True)

    def FormatAddressesNames(self, data):



