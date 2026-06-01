def mostrar_teoria():
    print("\n--- TEORÍA: Estructura de la oración ---")
    print("""
1. Sujeto:
   - Explícito: aparece en la oración. Ej: 'Pedro juega.'
   - Implícito: se deduce. Ej: 'Voy al cine.' (yo)

2. Predicado:
   - Verbal: núcleo es un verbo. Ej: 'Ella canta.'
   - Nominal: verbo copulativo + atributo. Ej: 'Él es médico.'

3. Modalidades oracionales:
   - Enunciativa: 'Él vino ayer.'
   - Interrogativa: '¿Vendrás mañana?'
   - Exclamativa: '¡Qué bonito día!'
   - Exhortativa: '¡Corre!'
   - Desiderativa: 'Ojalá apruebe.'
   - Dubitativa: 'Quizá llegue tarde.'
""")


def ejemplos():
    print("\n--- EJEMPLOS DE ANÁLISIS ---")
    print("1. Oración: 'Laura lee un libro.'")
    print("   - Sujeto: Laura (explícito, simple)")
    print("   - Predicado: lee un libro (verbal)")
    print("   - Modalidad: enunciativa afirmativa")
    print()
    print("2. Oración: '¡Qué sorpresa!'")
    print("   - Sujeto: implícito")
    print("   - Predicado: ¡Qué sorpresa! (nominal)")
    print("   - Modalidad: exclamativa")


def actividades_practicas():
    print("\n--- ACTIVIDADES PRÁCTICAS ---")
    print("1. Escribe un cuento corto (3 a 5 líneas) e identifica:")
    print("   - El sujeto y el predicado de al menos 3 oraciones.")
    print("   - La modalidad de cada oración.")
    print()
    print("2. Juego de rol:")
    print("   - Actúa una oración con sujeto implícito. Tus compañeros deben adivinar el sujeto.")
    print()
    print("3. Lectura comprensiva:")
    print("   - Lee un texto breve y subraya los sujetos y predicados. Clasifica su modalidad.")

def practica_usuario():
    print("\n--- PRÁCTICA INTERACTIVA ---")
    oracion = input("Escribe una oración para analizar: ")
    sujeto = input("¿Cuál es el sujeto?: ")
    predicado = input("¿Cuál es el predicado?: ")
    modalidad = input("¿Qué tipo de modalidad tiene esta oración?: ")
    guardar = input("¿Quieres guardar este análisis? (s/n): ")
    if guardar.lower() == "s":
        with open("analisis_6grado.txt", "a", encoding="utf-8") as f:
            f.write(f"Oración: {oracion}\nSujeto: {sujeto}\nPredicado: {predicado}\nModalidad: {modalidad}\n---\n")
        print("¡Guardado con éxito!")


def menu():
    while True:
        print("\n🌟 LECCIÓN 11 - 6º GRADO 🌟")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Actividades sugeridas")
        print("4. Práctica interactiva")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejemplos()
        elif opcion == "3":
            actividades_practicas()
        elif opcion == "4":
            practica_usuario()
        elif opcion == "5":
            print("¡Hasta la próxima lección!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar el menú
menu()
