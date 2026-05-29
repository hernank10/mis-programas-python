def mostrar_menu():
    print("\n--- Menú de Práctica: 'Cuando' como adverbio relativo ---")
    print("1. Ver ejemplos de 'cuando' como adverbio relativo")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de 'cuando' como adverbio relativo ---")
    ejemplos = [
        "Recuerdo el día **cuando** llegaste.",
        "No sé **cuando** volverá a llover.",
        "Esa fue la época **cuando** todo cambió.",
        "¿Recuerdas el momento **cuando** nos conocimos?"
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "No recuerdo el día ___ llegaste.", "respuesta": "cuando"},
        {"oracion": "Esa fue la época ___ todo cambió.", "respuesta": "cuando"},
        {"oracion": "¿Sabes ___ volverá a llover?", "respuesta": "cuando"},
        {"oracion": "El momento ___ nos conocimos fue mágico.", "respuesta": "cuando"}
    ]
    for i, ejercicio in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}:")
        print(f"Completa la oración: {ejercicio['oracion']}")
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        if respuesta_usuario == ejercicio["respuesta"]:
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
