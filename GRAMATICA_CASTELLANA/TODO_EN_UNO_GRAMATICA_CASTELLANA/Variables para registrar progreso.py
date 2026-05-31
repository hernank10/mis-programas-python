import random

# Variables para registrar progreso
progreso_completado = []
total_combinaciones = 24

def mostrar_introduccion():
    print("\n=== Introducción ===")
    print("En este programa practicarás la movilidad de grupos sintácticos dentro de una oración.")
    print("Grupos sintácticos: Sujeto, Verbo, Complemento directo, Complemento indirecto.")
    print("Podrás reorganizar estos grupos para crear nuevas oraciones.")
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

def ejercicios_practicos():
    print("\n=== Ejercicios Prácticos ===")
    print("Oración original: 'El mensajero llevó las cartas al correo.'")
    
    # Opciones de grupos sintácticos
    opciones = {
        "1": "El mensajero",  # Sujeto
        "2": "llevó",         # Verbo
        "3": "las cartas",    # Complemento directo
        "4": "al correo"      # Complemento indirecto
    }
    
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
    if combinacion_actual not in progreso_completado:
        progreso_completado.append(combinacion_actual)
        print("\nNueva oración creada:")
        print(combinacion_actual + ".\n")
    else:
        print("\nYa creaste esta combinación antes. Intenta otra.\n")

    input("Presiona Enter para volver al menú principal.\n")

def mostrar_progreso():
    print("\n=== Progreso ===")
    print(f"Combinaciones realizadas: {len(progreso_completado)}/{total_combinaciones}")
    if progreso_completado:
        print("Oraciones creadas:")
        for oracion in progreso_completado:
            print(f"- {oracion}")
    else:
        print("Aún no has creado ninguna combinación.")
    input("\nPresiona Enter para volver al menú principal.\n")

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Introducción")
        print("2. Cuestionario Teórico")
        print("3. Ejercicios Prácticos")
        print("4. Ver Progreso")
        print("5. Salir")

        opcion = input("\nElige una opción (1-5): ")
        if opcion == "1":
            mostrar_introduccion()
        elif opcion == "2":
            cuestionario_teorico()
        elif opcion == "3":
            ejercicios_practicos()
        elif opcion == "4":
            mostrar_progreso()
        elif opcion == "5":
            print("¡Gracias por practicar! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
