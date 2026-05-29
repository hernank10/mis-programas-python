def mostrar_menu():
    print("\n--- Menú de Práctica: Uso de 'cualquiera' (CUALQUIERA-1 y CUALQUIERA-2) ---")
    print("1. Ver ejemplos de 'cualquiera'")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de 'cualquiera' ---")
    ejemplos = [
        "Puedes consultar a cualquier médico.",  # CUALQUIERA-1 (prenominal)
        "Puedes consultar a un médico cualquiera.",  # CUALQUIERA-2 (posnominal)
        "Elige cualquier libro de la estantería.",  # CUALQUIERA-1
        "Elige un libro cualquiera de la estantería.",  # CUALQUIERA-2
        "Cualquier estudiante puede participar.",  # CUALQUIERA-1
        "Un estudiante cualquiera puede participar."  # CUALQUIERA-2
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "Puedes consultar a ___ médico.", "respuesta": "cualquier"},  # CUALQUIERA-1
        {"oracion": "Puedes consultar a un médico ___.", "respuesta": "cualquiera"},  # CUALQUIERA-2
        {"oracion": "Elige ___ libro de la estantería.", "respuesta": "cualquier"},  # CUALQUIERA-1
        {"oracion": "Elige un libro ___ de la estantería.", "respuesta": "cualquiera"},  # CUALQUIERA-2
        {"oracion": "___ estudiante puede participar.", "respuesta": "Cualquier"},  # CUALQUIERA-1
        {"oracion": "Un estudiante ___ puede participar.", "respuesta": "cualquiera"}  # CUALQUIERA-2
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
