"""Geocoding dos dados."""

import requests

def get_neighborhood(address):
    """
    Acha o bairro ao qual pertence o endereço utilizando o OpenStreetMap Nominatim API.

    Args:
        address (str): Endereço de pesquisa.

    Returns:
        str: Se encontrar, retorna o bairro ao qual pertence o endereço, caso contrário retorna None.
    """

    base_url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": address,
        "format": "json",
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data:
            neighborhood = data[0].get('address', {}).get('neighbourhood')
            return neighborhood
        else:
            print("Nenhum resultado encontrado.")
            return None

    except Exception as e:
        print("Ocorreu um erro:", e)
        return None
    

def geocode_address(address):
    """
    Geocoding de endereço utilizando OpenStreetMap Nominatim API.

    Args:
        address (str): Endereço para ser codificado.

    Returns:
        tuple: Latitude e longitude -> (latitude, longitude).
    """

    base_url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": address,
        "format": "json",
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data:
            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])
            return latitude, longitude
        else:
            print("Geocoding falhou. Nenhum resultado encontrado.")
            return None, None
    except Exception as e:
        print("Ocorreu um erro:", e)
        return None, None