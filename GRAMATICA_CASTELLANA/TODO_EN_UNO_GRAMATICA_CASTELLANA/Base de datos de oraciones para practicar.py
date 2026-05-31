import random

# Variables para registrar progreso
progreso_espanol = []
progreso_ingles = []
total_combinaciones = 24

# Base de datos de oraciones para practicar
oraciones_espanol = [
    ("El mensajero", "llevó", "las cartas", "al correo")
]
oraciones_ingles = [
    ("The messenger", "delivered", "the letters", "to the post office")
]

def mostrar_introduccion():
    print("\n=== Introducción ===")
    print("Este programa te ayudará a practicar la movilidad de grupos sintácticos en oraciones.")
    print("Podrás practicar en español o en inglés, reorganizando los grupos para crear nuevas oraciones.")
    print("También puedes añadir más oraciones y guardar tu progreso en un archivo.")
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
        oraciones = oraciones_espanol
        progreso = progreso_espanol
    elif idioma == "inglés":
        print("\n=== Ejercicios Prácticos en Inglés ===")
        oraciones = oraciones_ingles
        progreso = progreso_ingles

    # Seleccionar una oración al azar
    sujeto, verbo, complemento_directo, complemento_indirecto = random.choice(oraciones)
    print(f"\nOración original: '{sujeto} {verbo} {complemento_directo} {complemento_indirecto}.'")

    opciones = {
        "1": sujeto,
        "2": verbo,
        "3": complemento_directo,
        "4": complemento_indirecto
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
    
    combinacion_actual = " ".join(nueva_oracion)
    if combinacion_actual not in progreso:
        progreso.append(combinacion_actual)
        print("\nNueva oración creada:")
        print(combinacion_actual + ".\n")
    else:
        print("\nYa creaste esta combinación antes. Intenta otra.\n")

    input("Presiona Enter para volver al menú principal.\n")

def agregar_oraciones():
    print("\n=== Añadir Nuevas Oraciones ===")
    print("Puedes añadir nuevas oraciones con sus grupos sintácticos para español o inglés.")
    idioma = input("¿En qué idioma deseas añadir oraciones? (español/inglés): ").strip().lower()

    if idioma not in ["español", "inglés"]:
        print("Idioma no válido. Regresando al menú principal.")
        return

    oraciones = oraciones_espanol if idioma == "español" else oraciones_ingles

    while True:
        sujeto = input("\nIngresa el sujeto: ").strip()
        verbo = input("Ingresa el verbo: ").strip()
        complemento_directo = input("Ingresa el complemento directo: ").strip()
        complemento_indirecto = input("Ingresa el complemento indirecto: ").strip()
        oraciones.append((sujeto, verbo, complemento_directo, complemento_indirecto))
        print("\nOración añadida con éxito.")
        continuar = input("¿Deseas añadir otra oración? (s/n): ").strip().lower()
        if continuar != "s":
            break

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

    guardar = input("\n¿Deseas guardar tu progreso en un archivo? (s/n): ").strip().lower()
    if guardar == "s":
        with open("progreso.txt", "w") as archivo:
            archivo.write("Progreso en Español:\n")
            archivo.writelines(f"- {oracion}\n" for oracion in progreso_espanol)
            archivo.write("\nProgreso en Inglés:\n")
            archivo.writelines(f"- {oracion}\n" for oracion in progreso_ingles)
        print("Progreso guardado en 'progreso.txt'.")
    input("\nPresiona Enter para volver al menú principal.\n")

def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Introducción")
        print("2. Cuestionario Teórico")
        print("3. Ejercicios en Español")
        print("4. Ejercicios en Inglés")
        print("5. Añadir Nuevas Oraciones")
        print("6. Ver y Guardar Progreso")
        print("7. Salir")

        opcion = input("\nElige una opción (1-7): ")
        if opcion == "1":
            mostrar_introduccion()
        elif opcion == "2":
            cuestionario_teorico()
        elif opcion == "3":
            ejercicios_practicos("español")
        elif opcion == "4":
            ejercicios_practicos("inglés")
        elif opcion == "5":
            agregar_oraciones()
        elif opcion == "6":
            mostrar_progreso()
        elif opcion == "7":
            print("¡Gracias por practicar! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
