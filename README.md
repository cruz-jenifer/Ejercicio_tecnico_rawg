# Ejercicio Técnico RAWG

## Descripción General
...

---

## Stack y Librerías
* **Lenguaje:** Python 3.10+ 
* **Peticiones HTTP:** `requests` (para la consulta GET a la API)
* **Gestión de Entorno:** `python-dotenv` (para aislar credenciales de forma segura)
* **Reportes:** `openpyxl` (para generar el archivo Excel formateado)
* **Librerías Estándar:** `csv`, `json`, `os`.

---

## Instalación y Configuración

1. **Obtener la API Key:**
   obtencion de api key en [RAWG API Docs](https://rawg.io/apidocs)

2. **Instalar Dependencias:**
   Ejecuta el siguiente comando en tu terminal para instalar las librerías necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar Variables de Entorno:**
   Crear un archivo llamado `.env` en la raíz del proyecto.
   Usar el archivo `.env.example` como referencia y agregar tu clave:
   ```env
   RAWG_API_KEY=api_key_ejemplo
   ```

---

## Ejecución
Para correr el script, simplemente ejecuta:
```bash
python main.py
```

El sistema realizará una validación del entorno antes de intentar cualquier conexión.

---

## Archivos de Salida


Al finalizar la ejecución, el script generará la carpeta `output/` con los siguientes archivos:
* **videojuegos.csv:** Datos limpios y procesados.
* **reporte_videojuegos.xlsx:** Reporte en formato tabla, ordenado por requerimientos mínimos.

---

## Estado del Proyecto (Commits)
- [x] **Commit 1:** Setup, proyecto base y configuración.
- [x] **Commit 2:** Cliente HTTP y consulta GET a la API de RAWG.
- [ ] **Commit 3:** Procesamiento y extracción de datos (Filtrado de JSON).
- [ ] **Commit 4:** Generación del archivo CSV.
- [ ] **Commit 5:** Generación del reporte en Excel y ordenamiento.
