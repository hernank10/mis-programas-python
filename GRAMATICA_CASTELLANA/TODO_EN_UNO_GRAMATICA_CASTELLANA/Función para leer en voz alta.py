import random
import pyttsx3
from datetime import datetime

# Configuración de pyttsx3 para la lectura de voz
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Velocidad de lectura
engine.setProperty("volume", 1.0)  # Volumen

# Función para leer en voz alta
def leer_en_voz_alta(texto):
    engine.say(texto)
    engine.runAndWait()

# Base de datos de verbos
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
    }
}

# Base de datos de abreviaturas
abreviaturas = {
    "Sr.": "Señor",
    "Sra.": "Señora",
    "Dr.": "Doctor",
    "Dra.": "Doctora",
    "etc.": "et cetera",
    "U. de G.": "Universidad de Guadalajara"
}

# Función para practicar conjugaciones verbales
def practicar_conjugacion():
    print("\n--- Práctica de Conjugaciones Verbales ---")
    puntuacion = 0
    total = 5  # Número de preguntas por ronda

    for _ in range(total):
        verbo, conjugaciones = random.choice(list(verbos.items()))
        modo = random.choice(list(conjugaciones.keys()))
        persona = random.randint(0, 5)  # Índice de persona (0 = yo, 1 = tú, etc.)

        personas = ["yo", "tú", "él/ella/usted", "nosotros/nosotras", "vosotros/vosotras", "ellos/ellas/ustedes"]
        pregunta = f"Conjuga el verbo '{verbo}' en {modo}, para la persona: {personas[persona]}"
        respuesta_correcta = conjugaciones[modo][persona]

        print(f"\n{pregunta}")
        leer_en_voz_alta(pregunta)  # Leer la pregunta en voz alta
        respuesta = input("Escribe la conjugación: ").strip()

        if respuesta.lower() == respuesta_correcta.lower():
            print("¡Correcto!")
            leer_en_voz_alta("¡Correcto!")
            puntuacion += 1
        else:
            mensaje_error = f"Incorrecto. La respuesta correcta es: '{respuesta_correcta}'."
            print(mensaje_error)
            leer_en_voz_alta(mensaje_error)

    resultado = f"Tu puntuación final es: {puntuacion}/{total}"
    print(f"\n{resultado}")
    leer_en_voz_alta(resultado)
    guardar_progreso("Conjugaciones Verbales", puntuacion, total)

# Función para ver conjugaciones
def ver_conjugaciones():
    print("\n--- Tabla de Conjugaciones ---")
    verbo = input("Escribe un verbo para ver sus conjugaciones (o deja vacío para ver todos): ").strip().lower()
    for verbo_actual, conjugaciones in verbos.items():
        if verbo and verbo_actual != verbo:
            continue
        print(f"\nVerbo: {verbo_actual}")
        leer_en_voz_alta(f"Verbo: {verbo_actual}")
        for modo, formas in conjugaciones.items():
            print(f"  Modo: {modo.capitalize()}")
            leer_en_voz_alta(f"Modo: {modo.capitalize()}")
            print(f"    {', '.join(formas)}")
            leer_en_voz_alta(f"{', '.join(formas)}")
    if verbo and verbo not in verbos:
        mensaje = f"El verbo '{verbo}' no está en la base de datos."
        print(mensaje)
        leer_en_voz_alta(mensaje)

# Función para practicar abreviaturas
def practicar_abreviaturas():
    print("\n--- Práctica de Abreviaturas ---")
    puntuacion = 0
    total = 5  # Número de preguntas por ronda

    for _ in range(total):
        abreviatura, significado = random.choice(list(abreviaturas.items()))
        pregunta = f"¿Qué significa la abreviatura '{abreviatura}'?"
        
        print(f"\n{pregunta}")
        leer_en_voz_alta(pregunta)  # Leer la pregunta en voz alta
        respuesta = input("Escribe el significado: ").strip()

        if respuesta.lower() == significado.lower():
            print("¡Correcto!")
            leer_en_voz_alta("¡Correcto!")
            puntuacion += 1
        else:
            mensaje_error = f"Incorrecto. La respuesta correcta es: '{significado}'."
            print(mensaje_error)
            leer_en_voz_alta(mensaje_error)

    resultado = f"Tu puntuación final es: {puntuacion}/{total}"
    print(f"\n{resultado}")
    leer_en_voz_alta(resultado)
    guardar_progreso("Abreviaturas", puntuacion, total)

# Función para guardar progreso
def guardar_progreso(actividad, correctas, total):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("progreso_actividad.txt", "a") as archivo:
        archivo.write(f"{fecha} - Actividad: {actividad} - Correctas: {correctas}/{total}\n")
    print("\nProgreso guardado con éxito en 'progreso_actividad.txt'.")
    leer_en_voz_alta("Progreso guardado con éxito.")

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Practicar conjugaciones verbales")
        print("2. Ver conjugaciones de verbos")
        print("3. Practicar abreviaturas")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            practicar_conjugacion()
        elif opcion == "2":
            ver_conjugaciones()
        elif opcion == "3":
            practicar_abreviaturas()
        elif opcion == "4":
            print("¡Gracias por practicar!")
            leer_en_voz_alta("¡Gracias por practicar!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")
            leer_en_voz_alta("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu_principal()
