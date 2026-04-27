import os
import sys
from dotenv import load_dotenv #para no escribir directamente la api key en el codigo
from api_client import get_games

def main():
    load_dotenv() #buscamos en el .env la api key  
    api_key = os.getenv("RAWG_API_KEY")
    if not api_key:
        print("No se encontró la variable 'RAWG_API_KEY' ")
        sys.exit(1)
    
    print("configuración exitosa: API key detectada.")
    print("\n conectando con la API de RAWG...")
    juegos_crudos = get_games(api_key)
    print(f"se obtuvieron {len(juegos_crudos)} juegos de la API.")
    print("-" * 30)
    
    for juego in juegos_crudos:
        print(f"{juego.get('name')}")

if __name__ == "__main__":
    main()