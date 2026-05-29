import json
import os
import random

FILE_NAME = "ejemplos.json"

def cargar_ejemplos():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_ejemplos(ejemplos):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, indent=4, ensure_ascii=False)
    print("Ejemplos guardados correctamente.")

def mostrar_menu():
    print("\n--- Menú de Ejemplos ---")
    print("1. Agregar nuevo ejemplo")
    print("2. Ver todos los ejemplos")
    print("3. Editar un ejemplo")
    print("4. Practicar/Memorizar")
    print("5. Salir")

def agregar_ejemplo(ejemplos):
    print("\n--- Agregar nuevo ejemplo ---")
    es = input("Introduce la frase en español: ")
    en = input("Introduce la traducción en inglés: ")
    fr = input("Introduce la traducción en francés: ")
    
    nuevo_id = 1
    if ejemplos:
        nuevo_id = max(e['id'] for e in ejemplos) + 1
    
    ejemplos.append({
        "id": nuevo_id,
        "es": es,
        "en": en,
        "fr": fr
    })
    guardar_ejemplos(ejemplos)

def ver_ejemplos(ejemplos):
    print("\n--- Lista de Ejemplos ---")
    if not ejemplos:
        print("No hay ejemplos guardados.")
        return
    for ejemplo in ejemplos:
        print(f"ID: {ejemplo['id']}")
        print(f"  Español: {ejemplo['es']}")
        print(f"  Inglés: {ejemplo['en']}")
        print(f"  Francés: {ejemplo['fr']}\n")

def editar_ejemplo(ejemplos):
    ver_ejemplos(ejemplos)
    try:
        ejemplo_id = int(input("Introduce el ID del ejemplo a editar: "))
        ejemplo_encontrado = None
        for ejemplo in ejemplos:
            if ejemplo['id'] == ejemplo_id:
                ejemplo_encontrado = ejemplo
                break
        
        if ejemplo_encontrado:
            print(f"Editando ejemplo con ID: {ejemplo_id}")
            ejemplo_encontrado['es'] = input(f"Nuevo español ({ejemplo_encontrado['es']}): ") or ejemplo_encontrado['es']
            ejemplo_encontrado['en'] = input(f"Nuevo inglés ({ejemplo_encontrado['en']}): ") or ejemplo_encontrado['en']
            ejemplo_encontrado['fr'] = input(f"Nuevo francés ({ejemplo_encontrado['fr']}): ") or ejemplo_encontrado['fr']
            guardar_ejemplos(ejemplos)
        else:
            print("ID no encontrado.")
    except ValueError:
        print("ID inválido.")

def practicar(ejemplos):
    print("\n--- Modo de Práctica ---")
    if not ejemplos:
        print("No hay ejemplos para practicar.")
        return

    while True:
        ejemplo = random.choice(ejemplos)
        
        print(f"\nTraduce la siguiente frase:")
        print(f"Español: {ejemplo['es']}")
        
        input("Presiona Enter para ver las traducciones...")
        
        print(f"  Inglés: {ejemplo['en']}")
        print(f"  Francés: {ejemplo['fr']}")
        
        continuar = input("\n¿Quieres practicar con otro ejemplo? (s/n): ")
        if continuar.lower() != 's':
            break

def main():
    ejemplos = cargar_ejemplos()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_ejemplo(ejemplos)
        elif opcion == '2':
            ver_ejemplos(ejemplos)
        elif opcion == '3':
            editar_ejemplo(ejemplos)
        elif opcion == '4':
            practicar(ejemplos)
        elif opcion == '5':
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
