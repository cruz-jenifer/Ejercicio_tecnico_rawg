import os
import csv

def generar_csv(juegos, ruta_archivo="output/videojuegos.csv"):
    """guarda lista de diccionarios en archivo csv"""
    
    
    directorio = os.path.dirname(ruta_archivo)
    
    # crea carpeta si no existe
    if directorio:
        os.makedirs(directorio, exist_ok=True)

    # se detienesi la lista esta vacia
    if not juegos:
        print("error: no hay juegos para guardar")
        return

    # abre archivo 
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        
        # extrae cabeceras del primer elemento
        cabeceras = list(juegos[0].keys())
        
        # inicializa el escritor
        escritor = csv.DictWriter(archivo_csv, fieldnames=cabeceras)
        
        # escribe titulos
        escritor.writeheader()
        
        # escribe los datos
        escritor.writerows(juegos)