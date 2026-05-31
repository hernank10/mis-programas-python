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

# Cuestionarios de predicado en español
def cuestionario_predicado_espanol():
    return [
        ("¿Qué es el predicado en una oración?", 
         ["El sujeto de la oración.", "El núcleo que expresa la acción o el estado del sujeto.", 
          "El complemento que modifica al verbo.", "El lugar donde ocurre la acción."], 2),
        ("Identifica el predicado en: 'María canta una canción.'", 
         ["María", "canta una canción", "canta", "una canción"], 2),
        ("¿Cuál es un ejemplo de predicado nominal?", 
         ["Pedro corre rápido.", "La casa es grande.", 
          "Ellos bailaron toda la noche.", "El niño juega en el parque."], 2),
        ("Selecciona el núcleo del predicado en: 'El perro ladra fuerte.'", 
         ["El perro", "ladra", "fuerte", "Ninguno"], 2),
        ("¿Qué tipo de predicado tiene esta oración: 'Ella camina rápidamente'?", 
         ["Predicado nominal", "Predicado verbal", "Predicado compuesto", "Predicado incompleto"], 2),
    ]

# Cuestionarios de predicado en inglés
def cuestionario_predicado_ingles():
    return [
        ("What is the predicate in a sentence?", 
         ["The subject of the sentence.", "The part that expresses the action or state of the subject.", 
          "The object of the action.", "The description of the subject."], 2),
        ("Identify the predicate in: 'She sings beautifully.'", 
         ["She", "sings beautifully", "sings", "beautifully"], 2),
        ("What is an example of a nominal predicate?", 
         ["The boy runs fast.", "The house is beautiful.", 
          "They danced all night.", "The child plays in the park."], 2),
        ("Select the predicate verb in: 'The cat sleeps on the mat.'", 
         ["The cat", "sleeps", "on the mat", "None"], 2),
        ("What type of predicate is in the sentence: 'He is very tired'?", 
         ["Nominal predicate", "Verbal predicate", "Compound predicate", "Incomplete predicate"], 1),
    ]

# Guardar progreso
def guardar_progreso(usuario, idioma, tipo, puntuacion, total):
    with open("progreso_predicado.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Idioma: {idioma}, Tipo: {tipo}, Puntuación: {puntuacion}/{total}\n")

# Función principal para cuestionarios
def iniciar_cuestionario(tipo, preguntas, idioma):
    print(f"\n--- Cuestionario de Predicado: {tipo} ({idioma}) ---")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    print(f"\nTu puntuación final en {tipo} ({idioma}) es: {puntuacion}/{len(preguntas)}.")
    return puntuacion, len(preguntas)

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario sobre el Predicado en Español e Inglés!")
    playsound("introduccion_predicado.mp3")  # Introducción con sonido

    try:
        img = Image.open("predicado.jpg")
        img.show()
    except FileNotFoundError:
        print("No se encontró la imagen introductoria.")

    usuario = input("\nPor favor, ingresa tu nombre: ")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Predicado en Español")
        print("2. Predicado en Inglés")
        print("3. Salir")
        idioma = input("Elige una opción (1-3): ")

        if idioma == "1":
            preguntas = cuestionario_predicado_espanol()
            puntuacion, total = iniciar_cuestionario("Predicado", preguntas, "Español")
            guardar_progreso(usuario, "Español", "Predicado", puntuacion, total)

        elif idioma == "2":
            preguntas = cuestionario_predicado_ingles()
            puntuacion, total = iniciar_cuestionario("Predicado", preguntas, "Inglés")
            guardar_progreso(usuario, "Inglés", "Predicado", puntuacion, total)

        elif idioma == "3":
            print("\n¡Gracias por participar! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

# Ejecutar el programa
menu_principal()
