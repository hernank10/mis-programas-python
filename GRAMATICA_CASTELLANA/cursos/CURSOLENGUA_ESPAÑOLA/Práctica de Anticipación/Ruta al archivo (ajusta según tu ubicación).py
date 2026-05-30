import json

# Ruta al archivo (ajusta según tu ubicación)
ruta_archivo = 'oraciones_anticipacion.json'

try:
    # Abrir y cargar el archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        
    # Mostrar contenido cargado
    print("¡Archivo cargado correctamente!")
    print(f"Número de categorías: {len(datos['categorias'])}")
    
except FileNotFoundError:
    print("Error: El archivo no existe en la ruta especificada.")
except json.JSONDecodeError:
    print("Error: El archivo no tiene formato JSON válido.")
