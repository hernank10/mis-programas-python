def mostrar_menu():
    print("\n--- Menú de Práctica: Uso de 'Ojalá' ---")
    print("1. Ver ejemplos de 'ojalá'")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de 'Ojalá' ---")
    ejemplos = [
        "Ojalá llegue a tiempo.",
        "Ojalá no llueva mañana.",
        "Ojalá tengas un buen día.",
        "Ojalá todo salga bien.",
        "Ojalá pudiera ayudarte."
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "___ llegue a tiempo.", "respuesta": "Ojalá"},
        {"oracion": "___ no llueva mañana.", "respuesta": "Ojalá"},
        {"oracion": "___ tengas un buen día.", "respuesta": "Ojalá"},
        {"oracion": "___ todo salga bien.", "respuesta": "Ojalá"},
        {"oracion": "___ pudiera ayudarte.", "respuesta": "Ojalá"}
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
