def mostrar_menu():
    print("\n--- Menú de Práctica: Construcciones Exceptivas ---")
    print("1. Ver ejemplos de construcciones exceptivas")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de Construcciones Exceptivas ---")
    ejemplos = [
        "Bailé con todos, excepto con Juan.",
        "Eso supone un cambio muy grande para todos los niños, salvo él.",
        "Visítame cualquier día, a excepción de los lunes.",
        "Ana es la mejor en su campo, con la única excepción de Eva.",
        "Exceptuando esta falda, mi ropa está para tirar."
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "Bailé con todos, ___ con Juan.", "respuesta": "excepto"},
        {"oracion": "Eso supone un cambio muy grande para todos los niños, ___ él.", "respuesta": "salvo"},
        {"oracion": "Visítame cualquier día, a ___ de los lunes.", "respuesta": "excepción"},
        {"oracion": "Ana es la mejor en su campo, con la ___ excepción de Eva.", "respuesta": "única"},
        {"oracion": "___ esta falda, mi ropa está para tirar.", "respuesta": "Exceptuando"}
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
