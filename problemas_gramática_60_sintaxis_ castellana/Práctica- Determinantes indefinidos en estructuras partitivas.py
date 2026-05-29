def mostrar_menu():
    print("\n--- Menú de Práctica: Determinantes indefinidos en estructuras partitivas ---")
    print("1. Ver ejemplos de estructuras partitivas")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de estructuras partitivas ---")
    ejemplos = [
        "Algunas de esas propuestas son interesantes.",
        "Dos de esos libros están en oferta.",
        "Varias de esas ideas fueron descartadas.",
        "*Ciertas de esas personas lo saben.",  # Incorrecto
        "*Distintas de esas ideas fueron discutidas."  # Incorrecto
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "___ de esas propuestas son interesantes.", "respuesta": "Algunas"},
        {"oracion": "___ de esos libros están en oferta.", "respuesta": "Dos"},
        {"oracion": "___ de esas ideas fueron descartadas.", "respuesta": "Varias"},
        {"oracion": "*___ de esas personas lo saben.", "respuesta": "Ciertas"},  # Incorrecto
        {"oracion": "*___ de esas ideas fueron discutidas.", "respuesta": "Distintas"}  # Incorrecto
    ]
    for i, ejercicio in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}:")
        print(f"Completa la oración: {ejercicio['oracion']}")
        respuesta_usuario = input("Tu respuesta: ").strip()
        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("¡Correcto! 🎉")
        else:
            print(f"Incorrecto. La respuesta correcta es: '{ejercicio['respuesta']}'.")
    input("\nPresiona Enter para volver al menú principal.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ").strip()
        if opcion == "1":
            mostrar_ejemplos()
        elif opcion == "2":
            practicar_ejercicios()
        elif opcion == "3":
            print("\n¡Gracias por practicar! Hasta pronto. 👋")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 3.")

if __name__ == "__main__":
    main()
