import os
import sys
from dotenv import load_dotenv #para no escribir directamente la api key en el codigo

def main():
    load_dotenv() #buscamos en el .env la api key  
    api_key = os.getenv("RAWG_API_KEY")
    if not api_key:
        print("No se encontró la variable 'RAWG_API_KEY' ")
        sys.exit(1)
    
    print("configuración exitosa: API key detectada.")

if __name__ == "__main__":
    main()