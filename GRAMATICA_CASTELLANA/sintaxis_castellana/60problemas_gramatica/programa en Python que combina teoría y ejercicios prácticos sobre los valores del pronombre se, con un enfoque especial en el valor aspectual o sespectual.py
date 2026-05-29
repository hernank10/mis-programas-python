def mostrar_teoria():
    print("""
    ============================================
    TEORÍA SOBRE LOS VALORES DE 'SE' EN ESPAÑOL
    ============================================

    El pronombre 'se' en español tiene múltiples valores, entre los cuales destacan:
    1. Reflexivo: Indica que la acción recae sobre el sujeto (Ej: Juan se lava).
    2. Recíproco: Indica que la acción es mutua entre dos o más sujetos (Ej: María y Pedro se abrazan).
    3. Pasivo reflejo: Indica una acción pasiva sin sujeto agente explícito (Ej: Se venden casas).
    4. Impersonal: Indica una acción sin sujeto específico (Ej: Se dice que...).
    5. Medio o anticausativo: Indica que la acción ocurre sin un agente directo (Ej: La ventana se rompió).
    6. Aspectual (sespectual): Añade un matiz de completitud o intensidad a la acción (Ej: Juan se comió la manzana).

    El valor aspectual o 'sespectual' es particularmente interesante porque modifica el aspecto del verbo,
    enfatizando la culminación o intensidad de la acción. Sin embargo, no todas las construcciones con 'se'
    que parecen aspectuales lo son realmente. Es importante analizar el contexto y aplicar criterios claros
    para identificar este valor.
    """)

def ejercicio_identificar_se():
    print("""
    ============================================
    EJERCICIO: IDENTIFICAR EL VALOR DE 'SE'
    ============================================

    A continuación, se presentan varias oraciones con el pronombre 'se'. Tu tarea es identificar
    el valor de 'se' en cada una de ellas. Las opciones son:
    1. Reflexivo
    2. Recíproco
    3. Pasivo reflejo
    4. Impersonal
    5. Medio o anticausativo
    6. Aspectual (sespectual)
    """)

    oraciones = [
        "Juan se lava las manos.",
        "María y Pedro se abrazan.",
        "Se venden casas en el centro.",
        "Se dice que va a llover.",
        "La ventana se rompió.",
        "Juan se comió la manzana."
    ]

    respuestas_correctas = [1, 2, 3, 4, 5, 6]

    for i, oracion in enumerate(oraciones):
        print(f"\nOración {i+1}: {oracion}")
        respuesta = int(input("¿Cuál es el valor de 'se' en esta oración? (1-6): "))
        if respuesta == respuestas_correctas[i]:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuestas_correctas[i]}")

def ejercicio_construir_oraciones():
    print("""
    ============================================
    EJERCICIO: CONSTRUIR ORACIONES CON 'SE'
    ============================================

    En este ejercicio, deberás construir oraciones utilizando el pronombre 'se' con el valor que se te indique.
    Las opciones son:
    1. Reflexivo
    2. Recíproco
    3. Pasivo reflejo
    4. Impersonal
    5. Medio o anticausativo
    6. Aspectual (sespectual)
    """)

    valores = [
        "reflexivo",
        "recíproco",
        "pasivo reflejo",
        "impersonal",
        "medio o anticausativo",
        "aspectual (sespectual)"
    ]

    for i, valor in enumerate(valores):
        print(f"\nConstruye una oración con 'se' de valor {valor}:")
        oracion = input("Escribe tu oración: ")
        print(f"Has escrito: {oracion}")
        print(f"Revisa si tu oración cumple con el valor {valor} de 'se'.")

def main():
    print("Bienvenido al programa de teoría y ejercicios sobre los valores de 'se' en español.")
    while True:
        print("\nMenú:")
        print("1. Mostrar teoría")
        print("2. Ejercicio: Identificar el valor de 'se'")
        print("3. Ejercicio: Construir oraciones con 'se'")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_identificar_se()
        elif opcion == "3":
            ejercicio_construir_oraciones()
        elif opcion == "4":
            print("¡Gracias por usar el programa! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    main()
