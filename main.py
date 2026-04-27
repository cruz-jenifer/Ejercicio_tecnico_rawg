import os
import sys
from dotenv import load_dotenv #para no escribir directamente la api key en el codigo
from api_client import get_games
from data_processor import procesar_juegos
from csv_generator import generar_csv

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

 # PROCESAMIENTO DE DATOS 
    print("\n Procesando y limpiando datos...")
    juegos_limpios = procesar_juegos(juegos_crudos)
    
    print("-" * 30)
    for juego in juegos_limpios:
        print(f"{juego['Nombre del videojuego']} | {juego['Rating']} | {juego['Fecha de lanzamiento']}")
        print(f"   Reqs: {str(juego['Requerimientos mínimos'])[:60]}...")
    print("-" * 30)

 # GENERACIÓN DEL ARCHIVO CSV 
    print("\n Generando archivo CSV...")
    ruta_csv = "output/videojuegos.csv"
    generar_csv(juegos_limpios, ruta_csv)
    
    # verificamos que el archivo csv se haya creado 
    if os.path.exists(ruta_csv):
        print(f"CSV guardado correctamente en: {ruta_csv}")
    else:
        print("ERROR: No se pudo generar el archivo CSV")

if __name__ == "__main__":
    main()