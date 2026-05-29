import json
import random

# Función para cargar oraciones desde el archivo JSON
def cargar_oraciones(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            oraciones = json.load(f)
        return oraciones
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

# Función principal del programa
def practicar_oraciones(oraciones):
    if not oraciones:
        print("No hay oraciones disponibles.")
        return

    puntuacion = 0
   import json
import random

# Función para cargar oraciones desde el archivo JSON
def cargar_oraciones(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            oraciones = json.load(f)
        return oraciones
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

# Función principal del programa
def practicar_oraciones(oraciones):
    if not oraciones:
        print("No hay oraciones disponibles.")
        return

    puntuacion = 0
    total = len(oraciones)

    print("\n--- Práctica de Anticipación del Infinitivo ---\n")

    for i, entrada in enumerate(oraciones):
        print(f"{i+1}. {entrada['oracion']}")
        print(f"Pregunta: {entrada['pregunta']}")
        respuesta = input("Tu respuesta: ").strip().lower()

        if "infinitivo" in respuesta:
            print("✅ ¡Buena respuesta!\n")
            puntuacion += 1
        else:
            print("❌ Respuesta incorrecta. Intenta observar la anticipación del infinitivo.\n")

    print(f"\nTu puntuación final: {puntuacion}/{total}")

# Ruta del archivo
archivo_json = "oraciones_anticipacion.json"

# Cargar y ejecutar
oraciones = cargar_oraciones(archivo_json)
practicar_oraciones(oraciones)

