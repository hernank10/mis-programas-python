def mostrar_menu():
    print("\n--- Menú de Práctica: Interpretaciones de 'mucho' ---")
    print("1. Ver ejemplos de interpretaciones de 'mucho'")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de interpretaciones de 'mucho' ---")
    ejemplos = [
        "María ha sufrido mucho en su vida.",  # Intensidad
        "Antonio piensa mucho en ella.",  # Frecuencia o duración
        "Ha comido mucho.",  # Cantidad
        "*Ana viene mucho de familia aristocrática."  # Agramaticalidad
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "María ha sufrido ___ en su vida.", "respuesta": "mucho", "interpretacion": "intensidad"},
        {"oracion": "Antonio piensa ___ en ella.", "respuesta": "mucho", "interpretacion": "frecuencia o duración"},
        {"oracion": "Ha comido ___.", "respuesta": "mucho", "interpretacion": "cantidad"},
        {"oracion": "*Ana viene ___ de familia aristocrática.", "respuesta": "mucho", "interpretacion": "agramaticalidad"}
    ]
    for i, ejercicio in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}:")
        print(f"Completa la oración: {ejercicio['oracion']}")
        respuesta_usuario = input("Tu respuesta: ").strip()
        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print(f"¡Correcto! 🎉 Interpretación: {ejercicio['interpretacion']}")
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
