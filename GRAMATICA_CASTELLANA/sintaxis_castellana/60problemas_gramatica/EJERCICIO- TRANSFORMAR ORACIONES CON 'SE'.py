def ejercicio_transformacion():
    print("""
    ============================================
    EJERCICIO: TRANSFORMAR ORACIONES CON 'SE'
    ============================================

    En este ejercicio, deberás transformar las siguientes oraciones para que incluyan el pronombre 'se'
    con el valor que se te indique. Las opciones son:
    1. Reflexivo
    2. Recíproco
    3. Pasivo reflejo
    4. Impersonal
    5. Medio o anticausativo
    6. Aspectual (sespectual)
    """)

    oraciones = [
        "Juan lava el coche.",
        "María y Pedro abrazan a sus hijos.",
        "Venden casas en el centro.",
        "Dicen que va a llover.",
        "La ventana rompió por el viento.",
        "Juan comió la manzana."
    ]

    valores = [1, 2, 3, 4, 5, 6]

    for i, oracion in enumerate(oraciones):
        print(f"\nOración {i+1}: {oracion}")
        print(f"Transforma esta oración para que incluya 'se' con valor {valores[i]}.")
        oracion_transformada = input("Escribe tu oración transformada: ")
        print(f"Has escrito: {oracion_transformada}")
        print(f"Revisa si tu oración cumple con el valor {valores[i]} de 'se'.")

def ejercicio_completar_oraciones():
    print("""
    ============================================
    EJERCICIO: COMPLETAR ORACIONES CON 'SE'
    ============================================

    En este ejercicio, deberás completar las siguientes oraciones con el pronombre 'se' y el verbo adecuado,
    asegurándote de que el valor de 'se' sea el correcto según el contexto.
    """)

    oraciones_incompletas = [
        "Juan ___ las manos antes de comer.",
        "María y Pedro ___ cuando se encontraron.",
        "___ casas en el centro a buen precio.",
        "___ que el concierto fue increíble.",
        "La puerta ___ sola durante la noche.",
        "Juan ___ toda la pizza en cinco minutos."
    ]

    verbos = ["lavar", "abrazar", "vender", "decir", "abrir", "comer"]

    for i, oracion in enumerate(oraciones_incompletas):
        print(f"\nOración {i+1}: {oracion}")
        verbo = input(f"Completa la oración con el verbo '{verbos[i]}' y el pronombre 'se': ")
        oracion_completa = oracion.replace("___", f"se {verbo}")
        print(f"Has escrito: {oracion_completa}")
        print(f"Revisa si tu oración tiene el valor correcto de 'se'.")

def main():
    print("Bienvenido al programa de teoría y ejercicios sobre los valores de 'se' en español.")
    while True:
        print("\nMenú:")
        print("1. Mostrar teoría")
        print("2. Ejercicio: Identificar el valor de 'se'")
        print("3. Ejercicio: Construir oraciones con 'se'")
        print("4. Ejercicio: Transformar oraciones con 'se'")
        print("5. Ejercicio: Completar oraciones con 'se'")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")

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
            print("¡Gracias por usar el programa! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()
