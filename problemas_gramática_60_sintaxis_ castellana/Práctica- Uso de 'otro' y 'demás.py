def mostrar_menu():
    print("\n--- Menú de Práctica: Uso de 'otro' y 'demás' ---")
    print("1. Ver ejemplos de 'otro' y 'demás'")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de 'otro' y 'demás' ---")
    ejemplos = [
        "Juan y Pedro fueron al cine, y los otros se quedaron en casa.",  # "otros"
        "Juan y Pedro fueron al cine, y los demás se quedaron en casa.",  # "demás"
        "Ya pueden servir los demás platos.",  # "demás"
        "Ya pueden servir los otros platos.",  # "otros"
        "Otros días llega tarde.",  # "otros"
        "*Demás días llega tarde.",  # Incorrecto
        "Me gustó más el otro libro.",  # "otro"
        "*Me gustó más el demás libro.",  # Incorrecto
        "Compra aquellos otros libros.",  # "otros"
        "*Compra aquellos demás libros."  # Incorrecto
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "Juan y Pedro fueron al cine, y los ___ se quedaron en casa.", "respuesta": "otros"},
        {"oracion": "Juan y Pedro fueron al cine, y los ___ se quedaron en casa.", "respuesta": "demás"},
        {"oracion": "Ya pueden servir los ___ platos.", "respuesta": "demás"},
        {"oracion": "Ya pueden servir los ___ platos.", "respuesta": "otros"},
        {"oracion": "___ días llega tarde.", "respuesta": "Otros"},
        {"oracion": "*___ días llega tarde.", "respuesta": "Demás"},  # Incorrecto
        {"oracion": "Me gustó más el ___ libro.", "respuesta": "otro"},
        {"oracion": "*Me gustó más el ___ libro.", "respuesta": "demás"},  # Incorrecto
        {"oracion": "Compra aquellos ___ libros.", "respuesta": "otros"},
        {"oracion": "*Compra aquellos ___ libros.", "respuesta": "demás"}  # Incorrecto
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
