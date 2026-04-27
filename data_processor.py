import re

def limpiar_html(texto):
    """
    Limpia etiquetas HTML de un texto, reemplazando saltos de línea y listas por espacios
    y normalizando los espacios en blanco.
    """
    if not texto:
        return "N/A"
    
    texto_con_espacios = re.sub(r'(?i)<br[^>]*>|<li>', ' ', str(texto))
    sin_html = re.sub(r'<[^>]+>', '', texto_con_espacios)
    return re.sub(r'\s+', ' ', sin_html).strip()

def procesar_juegos(juegos_crudos):
    """
    Filtra y extrae los datos requeridos de la respuesta JSON cruda
    """
    juegos_procesados = []

    for juego in juegos_crudos:
        # Extracción de datos
        nombre = juego.get("name", "Desconocido")
        rating = juego.get("rating", "N/A")
        fecha = juego.get("released", "N/A")

        # Busqueda de requerimientos mínimos
        requerimientos_minimos = "N/A"
        plataformas = juego.get("platforms", [])
        
        for plataforma_info in plataformas:
            plataforma = plataforma_info.get("platform", {})
            if plataforma.get("slug") == "pc":
                reqs = plataforma_info.get("requirements_en")
                
                # Validación
                if isinstance(reqs, dict):
                    minimo = reqs.get("minimum")
                    if minimo:
                        requerimientos_minimos = limpiar_html(minimo)
                        break  # Detenemos la búsqueda al encontrar el primer requerimiento válido

        # Contrato de datos: nombres de columnas estrictos
        juego_limpio = {
            "Nombre del videojuego": nombre,
            "Rating": rating,
            "Fecha de lanzamiento": fecha,
            "Requerimientos mínimos": requerimientos_minimos
        }
        
        juegos_procesados.append(juego_limpio)

    return juegos_procesados