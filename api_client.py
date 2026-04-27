import requests
import sys

def get_games(api_key):
    """
    obtenga la información sobre los primeros 5 videojuegos de la respuesta
    """
    url = "https://api.rawg.io/api/games"
    
    parametros = {
        "key": api_key,
        "page_size": 5
    }
    
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
        respuesta.raise_for_status()
        
        datos = respuesta.json()
        return datos.get("results", [])
        
    except requests.exceptions.Timeout:
        print("La API de RAWG tardo demasiado en responder")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Fallo la comunicación con la API de RAWG.\nDetalle técnico: {e}")
        sys.exit(1)