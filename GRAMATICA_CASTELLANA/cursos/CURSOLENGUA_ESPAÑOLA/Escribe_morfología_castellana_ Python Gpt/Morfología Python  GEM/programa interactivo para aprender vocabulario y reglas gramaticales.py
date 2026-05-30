import random

# Diccionario para almacenar palabras y sus significados
vocabulario = {
    "palabra1": "definición de palabra1",
    "palabra2": "definición de palabra2",
    # ... agregar más palabras
}

def generar_ejercicio():
    # Seleccionar una palabra aleatoria del diccionario
    palabra_aleatoria = random.choice(list(vocabulario.keys()))

    # Presentar la palabra y pedir la definición
    print(f"¿Cuál es el significado de '{palabra_aleatoria}'?")
    respuesta = input()

    # Verificar la respuesta
    if respuesta.lower() == vocabulario[palabra_aleatoria].lower():
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La definición correcta es: {vocabulario[palabra_aleatoria]}")

# Función para generar ejercicios de composición de palabras
def ejercicio_composicion():
    # ... implementar la lógica para generar ejercicios de composición
    pass

# Función principal
def main():
    while True:
        print("1. Practicar vocabulario")
        print("2. Practicar composición de palabras")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            generar_ejercicio()
        elif opcion == "2":
            ejercicio_composicion()
        else:
            print("Opción inválida.")

        continuar = input("¿Quieres continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
