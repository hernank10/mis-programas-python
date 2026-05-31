import random

# Variables para registrar progreso
progreso_espanol = []
progreso_ingles = []
total_combinaciones = 24

def mostrar_introduccion():
    print("\n=== Introducción ===")
    print("Este programa te ayudará a practicar la movilidad de grupos sintácticos en oraciones.")
    print("Podrás practicar en español o en inglés, reorganizando los grupos para crear nuevas oraciones.")
    print("Grupos sintácticos: Sujeto, Verbo, Complemento directo, Complemento indirecto.")
    print("¡Vamos a aprender y practicar juntos!")
    input("\nPresiona Enter para volver al menú principal.\n")

def cuestionario_teorico():
    print("\n=== Cuestionario Teórico ===")
    preguntas = [
        ("¿Qué es el sujeto en una oración?", "El elemento que realiza la acción."),
        ("¿Qué es el complemento directo?", "El objeto que recibe directamente la acción."),
        ("¿Qué es el complemento indirecto?", "El destinatario o beneficiario de la acción."),
        ("¿Qué es el verbo en una oración?", "La acción principal realizada por el sujeto.")
    ]
    puntaje = 0

    for i, (pregunta, respuesta) in enumerate(preguntas, 1):
        print(f"\n{i}. {pregunta}")
        user_respuesta = input("Tu respuesta: ").strip().lower()
        if user_respuesta in respuesta.lower():
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {respuesta}")

    print(f"\nTu puntaje: {puntaje}/{len(preguntas)}")
    input("\nPresiona Enter para volver al menú principal.\n")

def ejercicios_practicos(idioma):
    if idioma == "español":
        print("\n=== Ejercicios Prácticos en Español ===")
        print("Oración original: 'El mensajero llevó las cartas al correo.'")
        opciones = {
            "1": "El mensajero",  # Sujeto
            "2": "llevó",         # Verbo
            "3": "las cartas",    # Complemento directo
            "4": "al correo"      # Complemento indirecto
        }
        progreso = progreso_espanol
    elif idioma == "inglés":
        print("\n=== Ejercicios Prácticos en Inglés ===")
        print("Original sentence: 'The messenger delivered the letters to the post office.'")
        opciones = {
            "1": "The messenger",  # Subject
            "2": "delivered",      # Verb
            "3": "the letters",    # Direct object
            "4": "to the post office"  # Indirect object
        }
        progreso = progreso_ingles

    print("\nOpciones:")
    for key, value in opciones.items():
        print(f"{key}: {value}")
    
    # Crear una nueva oración
    nueva_oracion = []
    for i in range(4):
        eleccion = input(f"Selecciona el grupo {i + 1} (1-4): ")
        while eleccion not in opciones:
            eleccion = input("Opción no válida. Selecciona nuevamente (1-4): ")
        nueva_oracion.append(opciones[eleccion])
    
    # Verificar si la combinación ya se realizó
    combinacion_actual = " ".join(nueva_oracion)
    if combinacion_actual not in progreso:
        progreso.append(combinacion_actual)
        print("\nNueva oración creada:")
        print(combinacion_actual + ".\n")
    else:
        print("\nYa creaste esta combinación antes. Intenta otra.\n")

    input("Presiona Enter para volver al menú principal.\n")

def mostrar_progreso():
    print("\n=== Progreso ===")
    print("En Español:")
    print(f"Combinaciones realizadas: {len(progreso_espanol)}/{total_combinaciones}")
    if progreso_espanol:
        print("Oraciones creadas:")
        for oracion in progreso_espanol:
            print(f"- {oracion}")

    print("\nEn Inglés:")
    print(f"Combinaciones realizadas: {len(progreso_ingles)}/{total_combinaciones}")
    if progreso_ingles:
        print("Oraciones creadas:")
        for oracion in progreso_ingles:
            print(f"- {oracion}")
    input("\nPresiona Enter para volver al menú principal.\n")

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Introducción")
        print("2. Cuestionario Teórico")
        print("3. Ejercicios en Español")
        print("4. Ejercicios en Inglés")
        print("5. Ver Progreso")
        print("6. Salir")

        opcion = input("\nElige una opción (1-6): ")
        if opcion == "1":
            mostrar_introduccion()
        elif opcion == "2":
            cuestionario_teorico()
        elif opcion == "3":
            ejercicios_practicos("español")
        elif opcion == "4":
            ejercicios_practicos("inglés")
        elif opcion == "5":
            mostrar_progreso()
        elif opcion == "6":
            print("¡Gracias por practicar! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
