import json
import os

# Función para cargar teoría desde JSON
def cargar_teoria():
    archivo = "teoria.json"
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        print("Archivo de teoría no encontrado.")
        return {}

# Función para mostrar teoría de una categoría
def mostrar_teoria_categoria(teoria, categoria):
    if categoria in teoria:
        print(f"\n--- {categoria} ---")
        print(f"Descripción: {teoria[categoria]['descripcion']}\n")
        print("Reglas:")
        for regla in teoria[categoria]["reglas"]:
            print(f"  - {regla}")
        print("\nEjemplos:")
        for ejemplo in teoria[categoria]["ejemplos"]:
            print(f"  * {ejemplo}")
    else:
        print("Categoría no encontrada.")

# Función para mostrar el menú de categorías
def mostrar_teoria(teoria):
    categorias = list(teoria.keys())
    while True:
        print("\n--- Categorías de Gramática ---")
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")
        print(f"{len(categorias) + 1}. Volver al menú principal")
        
        opcion = input("Selecciona una categoría: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(categorias):
                mostrar_teoria_categoria(teoria, categorias[opcion - 1])
            elif opcion == len(categorias) + 1:
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
        else:
            print("Por favor, introduce un número.")

# Programa principal
def main():
    teoria = cargar_teoria()
    if not teoria:
        print("No se pudo cargar el contenido teórico. Verifica el archivo.")
        return

    while True:
        print("\n--- Aprende Gramática Española ---")
        print("1. Ver teoría")
        print("2. Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_teoria(teoria)
        elif opcion == "2":
            print("¡Gracias por aprender con nosotros!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
