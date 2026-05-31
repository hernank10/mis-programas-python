import random

# Base de datos ampliada de verbos con tiempos, modos y conjugaciones
verbos = {
    "hablar": {
        "indicativo": ["hablo", "hablas", "habla", "hablamos", "habláis", "hablan"],
        "subjuntivo": ["hable", "hables", "hable", "hablemos", "habléis", "hablen"],
        "imperativo": ["-", "habla", "hable", "hablemos", "hablad", "hablen"],
        "condicional": ["hablaría", "hablarías", "hablaría", "hablaríamos", "hablaríais", "hablarían"],
        "futuro": ["hablaré", "hablarás", "hablará", "hablaremos", "hablaréis", "hablarán"]
    },
    "comer": {
        "indicativo": ["como", "comes", "come", "comemos", "coméis", "comen"],
        "subjuntivo": ["coma", "comas", "coma", "comamos", "comáis", "coman"],
        "imperativo": ["-", "come", "coma", "comamos", "comed", "coman"],
        "condicional": ["comería", "comerías", "comería", "comeríamos", "comeríais", "comerían"],
        "futuro": ["comeré", "comerás", "comerá", "comeremos", "comeréis", "comerán"]
    },
    "vivir": {
        "indicativo": ["vivo", "vives", "vive", "vivimos", "vivís", "viven"],
        "subjuntivo": ["viva", "vivas", "viva", "vivamos", "viváis", "vivan"],
        "imperativo": ["-", "vive", "viva", "vivamos", "vivid", "vivan"],
        "condicional": ["viviría", "vivirías", "viviría", "viviríamos", "viviríais", "vivirían"],
        "futuro": ["viviré", "vivirás", "vivirá", "viviremos", "viviréis", "vivirán"]
    },
    "escribir": {
        "indicativo": ["escribo", "escribes", "escribe", "escribimos", "escribís", "escriben"],
        "subjuntivo": ["escriba", "escribas", "escriba", "escribamos", "escribáis", "escriban"],
        "imperativo": ["-", "escribe", "escriba", "escribamos", "escribid", "escriban"],
        "condicional": ["escribiría", "escribirías", "escribiría", "escribiríamos", "escribiríais", "escribirían"],
        "futuro": ["escribiré", "escribirás", "escribirá", "escribiremos", "escribiréis", "escribirán"]
    }
}

# Función para practicar conjugaciones
def practicar_conjugacion():
    print("\n--- Práctica de Conjugaciones Verbales ---")
    puntuacion = 0
    total = 5  # Número de preguntas por ronda

    for _ in range(total):
        verbo, conjugaciones = random.choice(list(verbos.items()))
        modo = random.choice(list(conjugaciones.keys()))
        persona = random.randint(0, 5)  # Índice de persona (0 = yo, 1 = tú, etc.)

        personas = ["yo", "tú", "él/ella/usted", "nosotros/nosotras", "vosotros/vosotras", "ellos/ellas/ustedes"]
        respuesta_correcta = conjugaciones[modo][persona]

        print(f"\nConjuga el verbo '{verbo}' en {modo}, para la persona: {personas[persona]}")
        respuesta = input("Escribe la conjugación: ").strip()

        if respuesta.lower() == respuesta_correcta.lower():
            print("¡Correcto!")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: '{respuesta_correcta}'.")

    print(f"\nTu puntuación final es: {puntuacion}/{total}")
    guardar_progreso("Conjugaciones Verbales", puntuacion, total)

# Función para ver conjugaciones con filtros
def ver_conjugaciones():
    print("\n--- Tabla de Conjugaciones ---")
    verbo = input("Escribe un verbo para ver sus conjugaciones (o deja vacío para ver todos): ").strip().lower()
    for verbo_actual, conjugaciones in verbos.items():
        if verbo and verbo_actual != verbo:
            continue
        print(f"\nVerbo: {verbo_actual}")
        for modo, formas in conjugaciones.items():
            print(f"  Modo: {modo.capitalize()}")
            print(f"    {', '.join(formas)}")
    if verbo and verbo not in verbos:
        print(f"El verbo '{verbo}' no está en la base de datos.")

# Función para agregar verbos personalizados
def agregar_verbo():
    print("\n--- Agregar un nuevo verbo ---")
    verbo = input("Escribe el infinitivo del verbo: ").strip().lower()
    if verbo in verbos:
        print(f"El verbo '{verbo}' ya existe.")
        return

    conjugaciones = {}
    for modo in ["indicativo", "subjuntivo", "imperativo", "condicional", "futuro"]:
        formas = input(f"Escribe las formas del verbo en {modo}, separadas por comas: ").strip().split(",")
        if len(formas) != 6:
            print("Debe haber exactamente 6 formas (o usa '-' para el imperativo en 1ª persona).")
            return
        conjugaciones[modo] = [forma.strip() for forma in formas]

    verbos[verbo] = conjugaciones
    print(f"Verbo '{verbo}' agregado con éxito.")

# Función para guardar progreso
def guardar_progreso(actividad, correctas, total):
    from datetime import datetime
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("progreso_conjugaciones.txt", "a") as archivo:
        archivo.write(f"{fecha} - Actividad: {actividad} - Correctas: {correctas}/{total}\n")
    print("\nProgreso guardado con éxito en 'progreso_conjugaciones.txt'.")

# Menú principal
def menu_conjugaciones():
    while True:
        print("\n--- Menú: Práctica de Conjugaciones Verbales ---")
        print("1. Practicar conjugaciones")
        print("2. Ver tabla de conjugaciones")
        print("3. Agregar un verbo nuevo")
        print("4. Ver progreso")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            practicar_conjugacion()
        elif opcion == "2":
            ver_conjugaciones()
        elif opcion == "3":
            agregar_verbo()
        elif opcion == "4":
            try:
                with open("progreso_conjugaciones.txt", "r") as archivo:
                    print("\n--- Progreso del Usuario ---")
                    print(archivo.read())
            except FileNotFoundError:
                print("\nAún no hay progreso guardado. Realiza la práctica para comenzar.")
        elif opcion == "5":
            print("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu_conjugaciones()
