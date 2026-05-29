def mostrar_menu():
    print("\n--- Menú de Práctica: Alternancia artículo determinado/indeterminado ---")
    print("1. Ver ejemplos de alternancia artículo determinado/indeterminado")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de alternancia artículo determinado/indeterminado ---")
    ejemplos = [
        "Vino el amigo de Pedro.",  # Artículo determinado
        "Vino un amigo de Pedro.",  # Artículo indeterminado
        "Votó el ochenta por ciento.",  # Artículo determinado
        "Votó un ochenta por ciento.",  # Artículo indeterminado
        "Votó una minoría.",  # Artículo indeterminado
        "*Votó una mayoría."  # Incorrecto
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "Vino ___ amigo de Pedro.", "respuesta": "un"},
        {"oracion": "Vino ___ amigo de Pedro.", "respuesta": "el"},
        {"oracion": "Votó ___ ochenta por ciento.", "respuesta": "el"},
        {"oracion": "Votó ___ ochenta por ciento.", "respuesta": "un"},
        {"oracion": "Votó ___ minoría.", "respuesta": "una"},
        {"oracion": "*Votó ___ mayoría.", "respuesta": "una"}  # Incorrecto
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
