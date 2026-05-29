import json

def mostrar_menu():
    print("\n--- Menú de Práctica ---")
    print("1. Introducción")
    print("2. Teoría")
    print("3. Ejemplos y análisis")
    print("4. Ejercicios de escritura y tematización")
    print("5. Agregar nuevo ejemplo")
    print("6. Comparar formas plenas y reducidas")
    print("7. Salir")
    
    return input("Seleccione una opción: ")

def mostrar_introduccion():
    print("\nLos adjetivos desnudos y los sintagmas nominales sin determinación tienen restricciones en su uso.")
    print("Este programa te ayudará a comprender y practicar estos conceptos con ejemplos, análisis y ejercicios.")

def mostrar_teoria():
    print("\nLos adjetivos desnudos son adjetivos con función adverbial, como en 'Julio escribe claro'.")
    print("Los sintagmas nominales sin determinación son aquellos que no llevan artículo, como en 'Julio escribe cartas'.")
    print("Ambos comparten restricciones gramaticales y semánticas en cuanto a flexión y tematización.")

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
    print("\n--- Ejemplos y Análisis ---")
    for i, ej in enumerate(ejemplos, 1):
        print(f"{i}. Adjetivo desnudo: {ej['adjetivo']} | Sintagma nominal: {ej['nominal']}")
        print("   - Análisis: Ambos casos presentan restricciones en flexión y tematización.")

def ejercicio_escritura():
    print("\n--- Ejercicio de Escritura y Tematización ---")
    respuesta1 = input("Escribe una oración con un adjetivo desnudo y luego tematízala: ")
    respuesta2 = input("Escribe una oración con un sintagma nominal sin determinación y tematízala: ")
    print("¡Bien hecho! Revisa tus respuestas y compáralas con los ejemplos.")

def agregar_ejemplo(ejemplos):
    print("\n--- Agregar Nuevo Ejemplo ---")
    adjetivo = input("Ingrese un ejemplo con un adjetivo desnudo: ")
    nominal = input("Ingrese un ejemplo con un sintagma nominal sin determinación: ")
    ejemplos.append({"adjetivo": adjetivo, "nominal": nominal})
    guardar_ejemplos(ejemplos)
    print("Ejemplo agregado correctamente.")

def comparar_formas():
    print("\n--- Comparación de Formas Plenas y Reducidas ---")
    print("Ejemplo 1: Julio escribe claramente. (pleno) vs. Julio escribe claro. (reducido)")
    print("Ejemplo 2: Julio escribe las cartas. (pleno) vs. Julio escribe cartas. (reducido)")
    print("Las formas plenas permiten más flexión y tematización, mientras que las reducidas tienen restricciones sintácticas.")

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
            comparar_formas()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
