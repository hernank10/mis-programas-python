def mostrar_menu():
    print("\n--- Menú de Práctica: Distribución de cuantificadores imprecisos con 'otro' ---")
    print("1. Ver ejemplos de distribución de cuantificadores imprecisos")
    print("2. Practicar con ejercicios")
    print("3. Salir")

def mostrar_ejemplos():
    print("\n--- Ejemplos de distribución de cuantificadores imprecisos ---")
    ejemplos = [
        "He recibido muchos otros regalos.",  # "muchos" antes de "otros"
        "He recibido otros muchos regalos.",  # "muchos" después de "otros"
        "Me quedan ya pocas otras cosas.",  # "pocas" antes de "otras"
        "Me quedan ya otras pocas cosas.",  # "pocas" después de "otras"
        "He recibido bastantes otros regalos.",  # "bastantes" antes de "otros"
        "*He recibido otros bastantes regalos.",  # Incorrecto: "bastantes" después de "otros"
        "He visto demasiadas otras desgracias.",  # "demasiadas" antes de "otras"
        "*He visto otras demasiadas desgracias."  # Incorrecto: "demasiadas" después de "otras"
    ]
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. {ejemplo}")
    input("\nPresiona Enter para volver al menú principal.")

def practicar_ejercicios():
    print("\n--- Practica con ejercicios ---")
    ejercicios = [
        {"oracion": "He recibido ___ otros regalos.", "respuesta": "muchos"},
        {"oracion": "He recibido otros ___ regalos.", "respuesta": "muchos"},
        {"oracion": "Me quedan ya ___ otras cosas.", "respuesta": "pocas"},
        {"oracion": "Me quedan ya otras ___ cosas.", "respuesta": "pocas"},
        {"oracion": "He recibido ___ otros regalos.", "respuesta": "bastantes"},
        {"oracion": "*He recibido otros ___ regalos.", "respuesta": "bastantes"},  # Incorrecto
        {"oracion": "He visto ___ otras desgracias.", "respuesta": "demasiadas"},
        {"oracion": "*He visto otras ___ desgracias.", "respuesta": "demasiadas"}  # Incorrecto
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
