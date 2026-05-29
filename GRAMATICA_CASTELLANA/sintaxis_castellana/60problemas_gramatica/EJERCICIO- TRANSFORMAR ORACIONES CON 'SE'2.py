def ejercicio_correccion():
    print("""
    ============================================
    EJERCICIO: CORREGIR ORACIONES CON 'SE'
    ============================================

    En este ejercicio, deberás corregir las siguientes oraciones que contienen errores en el uso del pronombre 'se'.
    Asegúrate de que el valor de 'se' sea el correcto según el contexto.
    """)

    oraciones_incorrectas = [
        "Juan se lavó las manos antes de comer, pero no se las secó.",
        "María y Pedro se abrazaron, pero no se dijeron nada.",
        "Se venden casas en el centro, pero no se sabe el precio.",
        "Se dice que va a llover, pero no se cree.",
        "La ventana se rompió, pero no se sabe cómo.",
        "Juan se comió la manzana, pero no se la disfrutó."
    ]

    correcciones = [
        "Juan se lavó las manos antes de comer, pero no las secó.",
        "María y Pedro se abrazaron, pero no se dijeron nada.",
        "Se venden casas en el centro, pero no se sabe el precio.",
        "Se dice que va a llover, pero no se cree.",
        "La ventana se rompió, pero no se sabe cómo.",
        "Juan se comió la manzana, pero no la disfrutó."
    ]

    for i, oracion in enumerate(oraciones_incorrectas):
        print(f"\nOración {i+1}: {oracion}")
        correccion = input("Escribe tu corrección: ")
        if correccion == correcciones[i]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La corrección adecuada es: {correcciones[i]}")

def ejercicio_identificacion_contexto():
    print("""
    ============================================
    EJERCICIO: IDENTIFICAR VALORES DE 'SE' EN CONTEXTO
    ============================================

    En este ejercicio, deberás identificar el valor de 'se' en las siguientes oraciones más complejas.
    Las opciones son:
    1. Reflexivo
    2. Recíproco
    3. Pasivo reflejo
    4. Impersonal
    5. Medio o anticausativo
    6. Aspectual (sespectual)
    """)

    oraciones = [
        "Juan se lavó las manos antes de comer, pero no las secó.",
        "María y Pedro se abrazaron, pero no se dijeron nada.",
        "Se venden casas en el centro, pero no se sabe el precio.",
        "Se dice que va a llover, pero no se cree.",
        "La ventana se rompió, pero no se sabe cómo.",
        "Juan se comió la manzana, pero no la disfrutó."
    ]

    respuestas_correctas = [1, 2, 3, 4, 5, 6]

    for i, oracion in enumerate(oraciones):
        print(f"\nOración {i+1}: {oracion}")
        respuesta = int(input("¿Cuál es el valor de 'se' en esta oración? (1-6): "))
        if respuesta == respuestas_correctas[i]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuestas_correctas[i]}")

def main():
    print("Bienvenido al programa de teoría y ejercicios sobre los valores de 'se' en español.")
    while True:
        print("\nMenú:")
        print("1. Mostrar teoría")
        print("2. Ejercicio: Identificar el valor de 'se'")
        print("3. Ejercicio: Construir oraciones con 'se'")
        print("4. Ejercicio: Transformar oraciones con 'se'")
        print("5. Ejercicio: Completar oraciones con 'se'")
        print("6. Ejercicio: Corregir oraciones con 'se'")
        print("7. Ejercicio: Identificar valores de 'se' en contexto")
        print("8. Salir")
        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_identificar_se()
        elif opcion == "3":
            ejercicio_construir_oraciones()
        elif opcion == "4":
            ejercicio_transformacion()
        elif opcion == "5":
            ejercicio_completar_oraciones()
        elif opcion == "6":
            ejercicio_correccion()
        elif opcion == "7":
            ejercicio_identificacion_contexto()
        elif opcion == "8":
            print("¡Gracias por usar el programa! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 8.")

if __name__ == "__main__":
    main()
