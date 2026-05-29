def mostrar_menu():
    print("\n--- Menú de Práctica: Uso de 'que' y 'como' en contextos anómalos ---")
    print("1. Ver ejemplos de 'que' y 'como'")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de 'que' y 'como' en contextos anómalos ---")
    ejemplos = [
        "Pienso que está lloviendo.",  # Uso tradicional de "que"
        "Todos estamos como que comiendo.",  # Uso anómalo de "como" y "que"
        "*Todos estamos que comiendo."  # Uso incorrecto sin "como"
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "Pienso ___ está lloviendo.", "respuesta": "que"},
        {"oracion": "Todos estamos ___ que comiendo.", "respuesta": "como"},
        {"oracion": "*Todos estamos ___ comiendo.", "respuesta": "como"},
        {"oracion": "Ella actúa ___ que supiera la respuesta.", "respuesta": "como"},
        {"oracion": "Estamos ___ que hablando, pero no es serio.", "respuesta": "como"}
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
