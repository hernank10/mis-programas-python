# Base de datos de palabras con su acentuación correcta y explicación
palabras_tilde = {
    "camion": ("camión", "Es una palabra aguda terminada en 'n'."),
    "lapiz": ("lápiz", "Es una palabra grave terminada en consonante distinta de 'n' o 's'."),
    "arbol": ("árbol", "Es una palabra grave terminada en consonante distinta de 'n' o 's'."),
    "sofá": ("sofá", "Es una palabra aguda terminada en vocal."),
    "jovenes": ("jóvenes", "Es una palabra esdrújula que siempre lleva tilde."),
    "tomo": ("tomó", "Es una palabra aguda terminada en vocal."),
    "ingles": ("inglés", "Es una palabra aguda terminada en 's'."),
    "pared": ("pared", "Es una palabra aguda terminada en consonante distinta de 'n' o 's'."),
    "cafe": ("café", "Es una palabra aguda terminada en vocal."),
    "calculo": ("cálculo", "Es una palabra esdrújula que siempre lleva tilde.")
}

# Función para practicar el uso de la tilde
def practicar_tilde():
    print("\n--- Práctica de Uso Correcto de la Tilde ---")
    correctas = 0
    total = len(palabras_tilde)

    for palabra, (correcta, explicacion) in palabras_tilde.items():
        print(f"\nPalabra: {palabra}")
        respuesta = input("¿Lleva tilde? (sí/no): ").strip().lower()
        if (respuesta == "sí" and palabra != correcta) or (respuesta == "no" and palabra == correcta):
            print(f"¡Correcto! {explicacion}")
            correctas += 1
        else:
            print(f"Incorrecto. La forma correcta es '{correcta}'. {explicacion}")

    print(f"\nTu puntuación final es: {correctas}/{total}")
    guardar_progreso("Práctica de tilde", correctas, total)

# Función para guardar el progreso en un archivo
def guardar_progreso(actividad, correctas, total):
    from datetime import datetime
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("progreso_tilde.txt", "a") as archivo:
        archivo.write(f"{fecha} - Actividad: {actividad} - Correctas: {correctas}/{total}\n")
    print("\nProgreso guardado con éxito en 'progreso_tilde.txt'.")

# Menú principal para esta aplicación específica
def menu_tilde():
    while True:
        print("\n--- Menú: Práctica de la Tilde ---")
        print("1. Practicar el uso correcto de la tilde")
        print("2. Ver progreso")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            practicar_tilde()
        elif opcion == "2":
            try:
                with open("progreso_tilde.txt", "r") as archivo:
                    print("\n--- Progreso del Usuario ---")
                    print(archivo.read())
            except FileNotFoundError:
                print("\nAún no hay progreso guardado. Realiza la práctica para comenzar.")
        elif opcion == "3":
            print("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu_tilde()
