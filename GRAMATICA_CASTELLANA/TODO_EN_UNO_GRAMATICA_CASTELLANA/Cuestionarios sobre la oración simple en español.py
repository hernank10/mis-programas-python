import os
from playsound import playsound
from PIL import Image

# Función para mostrar una pregunta
def mostrar_pregunta(pregunta, opciones, respuesta_correcta):
    print("\n" + pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    try:
        respuesta_usuario = int(input("Elige la opción correcta (1/2/3/4): "))
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
            return True
        else:
            print(f"Incorrecto. La respuesta correcta era: {opciones[respuesta_correcta - 1]}")
            return False
    except ValueError:
        print("Entrada inválida. Por favor, selecciona una opción válida.")
        return False

# Cuestionarios sobre la oración simple en español
def cuestionario_oracion_simple_espanol():
    return [
        ("¿Qué es una oración simple?", 
         ["Una oración con un solo sujeto y predicado.", 
          "Una oración con varios verbos principales.", 
          "Una oración compuesta por varias proposiciones.", 
          "Una oración sin verbo."], 1),
        ("Identifica la oración simple:", 
         ["Los niños juegan en el parque.", 
          "Los niños juegan y cantan en el parque.", 
          "Aunque llueve, salieron a jugar.", 
          "Ellos jugaron y luego cantaron."], 1),
        ("¿Cuál es un ejemplo de oración simple atributiva?", 
         ["El coche es rojo.", 
          "Compraron un coche nuevo.", 
          "El coche y la bicicleta están aquí.", 
          "Cuando llegó, el coche ya no estaba."], 1),
        ("Selecciona el núcleo verbal en: 'Ana escribe un poema.'", 
         ["Ana", "escribe", "un poema", "Ninguno"], 2),
        ("¿Qué tipo de oración simple es: 'Tráeme un vaso de agua.'?", 
         ["Declarativa", "Interrogativa", "Imperativa", "Exclamativa"], 3),
    ]

# Cuestionarios sobre la oración simple en inglés
def cuestionario_oracion_simple_ingles():
    return [
        ("What is a simple sentence?", 
         ["A sentence with one subject and one predicate.", 
          "A sentence with multiple main verbs.", 
          "A sentence composed of several clauses.", 
          "A sentence without a verb."], 1),
        ("Identify the simple sentence:", 
         ["The children play in the park.", 
          "The children play and sing in the park.", 
          "Although it rains, they went out to play.", 
          "They played and then sang."], 1),
        ("Which is an example of an attributive simple sentence?", 
         ["The car is red.", 
          "They bought a new car.", 
          "The car and the bike are here.", 
          "When he arrived, the car was gone."], 1),
        ("Select the verbal nucleus in: 'Sarah writes a poem.'", 
         ["Sarah", "writes", "a poem", "None"], 2),
        ("What type of simple sentence is: 'Bring me a glass of water.'?", 
         ["Declarative", "Interrogative", "Imperative", "Exclamatory"], 3),
    ]

# Guardar progreso
def guardar_progreso(usuario, idioma, tipo, puntuacion, total):
    with open("progreso_oracion_simple.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Idioma: {idioma}, Tipo: {tipo}, Puntuación: {puntuacion}/{total}\n")

# Función principal para cuestionarios
def iniciar_cuestionario(tipo, preguntas, idioma):
    print(f"\n--- Cuestionario sobre la Oración Simple: {tipo} ({idioma}) ---")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    print(f"\nTu puntuación final en {tipo} ({idioma}) es: {puntuacion}/{len(preguntas)}.")
    return puntuacion, len(preguntas)

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario sobre la Oración Simple!")
    playsound("introduccion_oracion_simple.mp3")  # Introducción con sonido

    try:
        img = Image.open("oracion_simple.jpg")
        img.show()
    except FileNotFoundError:
        print("No se encontró la imagen introductoria.")

    usuario = input("\nPor favor, ingresa tu nombre: ")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Oración Simple en Español")
        print("2. Oración Simple en Inglés")
        print("3. Salir")
        idioma = input("Elige una opción (1-3): ")

        if idioma == "1":
            preguntas = cuestionario_oracion_simple_espanol()
            puntuacion, total = iniciar_cuestionario("Oración Simple", preguntas, "Español")
            guardar_progreso(usuario, "Español", "Oración Simple", puntuacion, total)

        elif idioma == "2":
            preguntas = cuestionario_oracion_simple_ingles()
            puntuacion, total = iniciar_cuestionario("Oración Simple", preguntas, "Inglés")
            guardar_progreso(usuario, "Inglés", "Oración Simple", puntuacion, total)

        elif idioma == "3":
            print("\n¡Gracias por participar! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

# Ejecutar el programa
menu_principal()
