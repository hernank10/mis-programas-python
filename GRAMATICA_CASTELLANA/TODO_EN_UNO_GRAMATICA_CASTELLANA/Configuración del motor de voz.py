import random
from datetime import datetime
import pyttsx3

# Configuración del motor de voz
motor_voz = pyttsx3.init()
motor_voz.setProperty("rate", 150)  # Velocidad de la voz
motor_voz.setProperty("volume", 1.0)  # Volumen de la voz (1.0 es el máximo)

# Base de datos de palabras y oraciones predispuestas en español
oraciones_espanol = {
    "sol": {
        "simple": "El sol brilla en el cielo.",
        "compuesta": "El sol brilla en el cielo, y las nubes flotan tranquilamente."
    },
    "niño": {
        "simple": "El niño juega en el parque.",
        "compuesta": "El niño juega en el parque mientras su madre lo observa."
    },
    "libro": {
        "simple": "El libro está sobre la mesa.",
        "compuesta": "El libro está sobre la mesa porque lo dejé ahí después de leer."
    }
}

# Base de datos de palabras y oraciones predispuestas en inglés
oraciones_ingles = {
    "sun": {
        "simple": "The sun shines in the sky.",
        "compuesta": "The sun shines in the sky, and the clouds drift peacefully."
    },
    "child": {
        "simple": "The child plays in the park.",
        "compuesta": "The child plays in the park while his mother watches."
    },
    "book": {
        "simple": "The book is on the table.",
        "compuesta": "The book is on the table because I left it there after reading."
    }
}

# Función para sintetizar voz
def leer_texto(texto):
    motor_voz.say(texto)
    motor_voz.runAndWait()

# Función para guardar progreso
def guardar_progreso(palabra, tipo, correcta, usuario, idioma):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultado = "correcto" if correcta else "incorrecto"
    with open("progreso_redaccion.txt", "a") as archivo:
        archivo.write(f"{fecha} - Idioma: {idioma} - Palabra: {palabra} - Oración {tipo}: {resultado} - Usuario: {usuario}\n")

# Función para practicar con una palabra
def practicar_palabra(palabra, idioma, oraciones):
    leer_texto(f"La palabra seleccionada es: {palabra}.")
    print(f"\nPalabra seleccionada: {palabra}")
    print("1. Redacta una oración simple.")
    leer_texto("Redacta una oración simple.")
    usuario_simple = input("Escribe tu oración simple: ").strip()
    print("2. Redacta una oración compuesta.")
    leer_texto("Redacta una oración compuesta.")
    usuario_compuesta = input("Escribe tu oración compuesta: ").strip()

    simple_correcta = oraciones.get(palabra, {}).get("simple", "").lower()
    compuesta_correcta = oraciones.get(palabra, {}).get("compuesta", "").lower()

    if simple_correcta:
        correcta_simple = usuario_simple.lower() == simple_correcta
        print(f"Oración simple: {'Correcto' if correcta_simple else 'Incorrecto'}")
        leer_texto("Correcto." if correcta_simple else "Incorrecto.")
        if not correcta_simple:
            print(f"Oración correcta: {simple_correcta}")
            leer_texto(f"La oración correcta es: {simple_correcta}")
        guardar_progreso(palabra, "simple", correcta_simple, usuario_simple, idioma)

    if compuesta_correcta:
        correcta_compuesta = usuario_compuesta.lower() == compuesta_correcta
        print(f"Oración compuesta: {'Correcto' if correcta_compuesta else 'Incorrecto'}")
        leer_texto("Correcto." if correcta_compuesta else "Incorrecto.")
        if not correcta_compuesta:
            print(f"Oración correcta: {compuesta_correcta}")
            leer_texto(f"La oración correcta es: {compuesta_correcta}")
        guardar_progreso(palabra, "compuesta", correcta_compuesta, usuario_compuesta, idioma)

# Mostrar la lista completa de palabras y sus oraciones predispuestas
def mostrar_lista(oraciones, idioma):
    print(f"\nLista de palabras y sus oraciones predispuestas en {idioma.capitalize()}:")
    leer_texto(f"A continuación se muestra la lista de palabras en {idioma}.")
    for palabra, oraciones in oraciones.items():
        print(f"\nPalabra: {palabra}")
        print(f"- Oración simple: {oraciones['simple']}")
        print(f"- Oración compuesta: {oraciones['compuesta']}")
        leer_texto(f"Palabra: {palabra}. Oración simple: {oraciones['simple']}. Oración compuesta: {oraciones['compuesta']}.")
    input("\nPresiona Enter para volver al menú principal...\n")

# Menú principal
def menu_principal():
    while True:
        print("=== Menú Principal ===")
        leer_texto("Bienvenido al programa. Seleccione una opción.")
        print("1. Practicar en Español")
        print("2. Practicar en Inglés")
        print("3. Ver lista de palabras en Español")
        print("4. Ver lista de palabras en Inglés")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            palabras_seleccionadas = random.sample(list(oraciones_espanol.keys()), 3)  # Selecciona 3 palabras al azar
            for palabra in palabras_seleccionadas:
                practicar_palabra(palabra, "español", oraciones_espanol)
                print("-" * 40)
            print("\n¡Has terminado la práctica en español! Revisa tu progreso en 'progreso_redaccion.txt'.")
            leer_texto("Has terminado la práctica en español.")
        elif opcion == "2":
            palabras_seleccionadas = random.sample(list(oraciones_ingles.keys()), 3)  # Selecciona 3 palabras al azar
            for palabra in palabras_seleccionadas:
                practicar_palabra(palabra, "inglés", oraciones_ingles)
                print("-" * 40)
            print("\n¡Has terminado la práctica en inglés! Revisa tu progreso en 'progreso_redaccion.txt'.")
            leer_texto("Has terminado la práctica en inglés.")
        elif opcion == "3":
            mostrar_lista(oraciones_espanol, "español")
        elif opcion == "4":
            mostrar_lista(oraciones_ingles, "inglés")
        elif opcion == "5":
            print("¡Gracias por usar el programa! Hasta pronto.")
            leer_texto("Gracias por usar el programa. Hasta pronto.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            leer_texto("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
menu_principal()

