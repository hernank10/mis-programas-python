import json

def mostrar_menu():
    print("\n--- Menú de Práctica ---")
    print("1. Introducción")
    print("2. Teoría")
    print("3. Ejemplos")
    print("4. Ejercicios de escritura")
    print("5. Agregar nuevo ejemplo")
    print("6. Salir")
    
    return input("Seleccione una opción: ")

def mostrar_introduccion():
    print("\nLos adjetivos desnudos y los sintagmas nominales sin determinación tienen restricciones en su uso.")
    print("Este programa te ayudará a comprender y practicar estos conceptos con ejemplos y ejercicios.")

def mostrar_teoria():
    print("\nLos adjetivos desnudos son adjetivos con función adverbial, como en 'Julio escribe claro'.")
    print("Los sintagmas nominales sin determinación son aquellos que no llevan artículo, como en 'Julio escribe cartas'.")

def cargar_ejemplos():
    try:
        with open("ejemplos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"adjetivo": "Julio habla claro.", "nominal": "Julio compra libros."},
            {"adjetivo": "Ana canta fuerte.", "nominal": "Pedro vende frutas."}
        ]

def guardar_ejemplos(ejemplos):
    with open("ejemplos.json", "w") as file:
        json.dump(ejemplos, file, indent=4)

def mostrar_ejemplos(ejemplos):
    print("\n--- Ejemplos ---")
    for i, ej in enumerate(ejemplos, 1):
        print(f"{i}. Adjetivo desnudo: {ej['adjetivo']} | Sintagma nominal: {ej['nominal']}")

def ejercicio_escritura():
    print("\n--- Ejercicio de Escritura ---")
    respuesta1 = input("Escribe una oración con un adjetivo desnudo: ")
    respuesta2 = input("Escribe una oración con un sintagma nominal sin determinación: ")
    print("¡Bien hecho! Revisa tus respuestas y compáralas con los ejemplos.")

def agregar_ejemplo(ejemplos):
    print("\n--- Agregar Nuevo Ejemplo ---")
    adjetivo = input("Ingrese un ejemplo con un adjetivo desnudo: ")
    nominal = input("Ingrese un ejemplo con un sintagma nominal sin determinación: ")
    ejemplos.append({"adjetivo": adjetivo, "nominal": nominal})
    guardar_ejemplos(ejemplos)
    print("Ejemplo agregado correctamente.")

def main():
    ejemplos = cargar_ejemplos()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            mostrar_introduccion()
        elif opcion == "2":
            mostrar_teoria()
        elif opcion == "3":
            mostrar_ejemplos(ejemplos)
        elif opcion == "4":
            ejercicio_escritura()
        elif opcion == "5":
            agregar_ejemplo(ejemplos)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
