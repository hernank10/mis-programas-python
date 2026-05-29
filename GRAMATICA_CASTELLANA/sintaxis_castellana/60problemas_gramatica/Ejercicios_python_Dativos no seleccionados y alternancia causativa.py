import random

# Lista de ejemplos de oraciones con modificadores locativos
ejemplos_locativos = [
    "Tengo un coche en el garaje.",
    "Es catedrático en la Complutense.",
    "Tengo el libro en la mesa.",
    "Es profesor en la universidad.",
    "Tengo coches en el estacionamiento.",
    "Es médico en el hospital.",
    "Tengo una bicicleta en el patio.",
    "Es estudiante en la facultad."
]

# Función para generar un ejemplo aleatorio
def generar_ejemplo():
    ejemplo = random.choice(ejemplos_locativos)
    print(f"\nEjemplo de oración con modificador locativo:\n{ejemplo}\n")

# Función para completar una oración
def completar_oracion():
    sujetos = ["Tengo", "Es"]
    sustantivos = ["coche", "catedrático", "libro", "profesor", "bicicleta", "médico", "estudiante"]
    locativos = ["en el garaje", "en la Complutense", "en la mesa", "en la universidad", "en el estacionamiento", "en el hospital", "en el patio", "en la facultad"]

    sujeto = random.choice(sujetos)
    sustantivo = random.choice(sustantivos)
    locativo = random.choice(locativos)

    print(f"\nCompleta la siguiente oración:\n{sujeto} _____ {locativo}.")
    respuesta = input("Escribe el sustantivo con o sin determinante (por ejemplo, 'un coche', 'catedrático'): ").strip()

    if respuesta:
        oracion_completa = f"{sujeto} {respuesta} {locativo}."
        print(f"\nTu oración completa es:\n{oracion_completa}")
        print(f"\n¡Buen trabajo! Aquí tienes un ejemplo similar:\n{random.choice(ejemplos_locativos)}\n")
    else:
        print("\nDebes completar la oración.\n")

# Función para verificar si una oración es correcta
def verificar_oracion():
    print("\nEscribe una oración con un modificador locativo:")
    print("Por ejemplo, 'Tengo un coche en el garaje' o 'Es catedrático en la Complutense'.")
    oracion_usuario = input("Tu oración: ").strip()

    if oracion_usuario:
        if ("Tengo" in oracion_usuario or "Es" in oracion_usuario) and " en " in oracion_usuario:
            print("\n¡Correcto! Es una oración con modificador locativo válida.\n")
        else:
            print("\nLa oración no es válida. Asegúrate de usar un modificador locativo.\n")
    else:
        print("\nDebes escribir una oración.\n")

# Función para practicar con ejercicios personalizados
def practicar_ejercicios():
    print("\nVamos a practicar con ejercicios personalizados.")
    print("Completa las siguientes oraciones con modificadores locativos:\n")

    ejercicios = [
        ("Tengo _____ en el garaje.", "un coche"),
        ("Es _____ en la Complutense.", "catedrático"),
        ("Tengo _____ en la mesa.", "el libro"),
        ("Es _____ en la universidad.", "profesor"),
        ("Tengo _____ en el estacionamiento.", "coches")
    ]

    for ejercicio, respuesta_correcta in ejercicios:
        print(ejercicio)
        respuesta_usuario = input("Escribe el sustantivo con o sin determinante: ").strip()

        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}\n")

# Menú principal
def mostrar_menu():
    while True:
        print("\n--- Menú de Práctica: Modificadores Locativos ---")
        print("1. Generar un ejemplo aleatorio")
        print("2. Completar una oración")
        print("3. Verificar si una oración es correcta")
        print("4. Practicar con ejercicios personalizados")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            generar_ejemplo()
        elif opcion == "2":
            completar_oracion()
        elif opcion == "3":
            verificar_oracion()
        elif opcion == "4":
            practicar_ejercicios()
        elif opcion == "5":
            print("\n¡Gracias por practicar! Hasta luego.\n")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 5.\n")

# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()
