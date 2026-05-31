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

# Cuestionarios sobre la oración compuesta en español
def cuestionario_oracion_compuesta_espanol():
    return [
        ("¿Qué es una oración compuesta?", 
         ["Una oración con un solo sujeto y predicado.", 
          "Una oración formada por dos o más proposiciones unidas.", 
          "Una oración con un verbo principal y un verbo auxiliar.", 
          "Una oración sin verbo."], 2),
        ("¿Cuál es un ejemplo de oración compuesta subordinada?", 
         ["Me gusta el café y el té.", 
          "Salí de casa cuando empezó a llover.", 
          "Juan estudia mucho, pero no aprueba.", 
          "Ellos llegaron temprano."], 2),
        ("Identifica la oración compuesta coordinada:", 
         ["Hizo sol toda la mañana.", 
          "Estaba cansado porque trabajó hasta tarde.", 
          "Juan lee y María escribe.", 
          "Aunque llueva, iremos al parque."], 3),
        ("Selecciona la proposición subordinada en: 'Creo que él llegará tarde.'", 
         ["Creo", "que él llegará tarde", "él llegará tarde", "Ninguna"], 3),
        ("¿Qué tipo de oración compuesta es: 'No sólo canta, sino que también baila.'?", 
         ["Coordinada adversativa", 
          "Coordinada copulativa", 
          "Coordinada disyuntiva", 
          "Coordinada distributiva"], 2),
    ]

# Cuestionarios sobre la oración compuesta en inglés
def cuestionario_oracion_compuesta_ingles():
    return [
        ("What is a compound sentence?", 
         ["A sentence with one subject and one predicate.", 
          "A sentence formed by two or more clauses connected.", 
          "A sentence with a main verb and an auxiliary verb.", 
          "A sentence without a verb."], 2),
        ("Which is an example of a subordinate compound sentence?", 
         ["I like coffee and tea.", 
          "I left the house when it started raining.", 
          "John studies a lot but doesn't pass.", 
          "They arrived early."], 2),
        ("Identify the coordinated compound sentence:", 
         ["It was sunny all morning.", 
          "He was tired because he worked late.", 
          "John reads, and Mary writes.", 
          "Although it rains, we will go to the park."], 3),
        ("Select the subordinate clause in: 'I think that he will be late.'", 
         ["I think", "that he will be late", "he will be late", "None"], 3),
        ("What type of compound sentence is: 'Not only does she sing, but she also dances.'?", 
         ["Adversative coordination", 
          "Copulative coordination", 
          "Disjunctive coordination", 
          "Distributive coordination"], 2),
    ]

# Guardar progreso
def guardar_progreso(usuario, idioma, tipo, puntuacion, total):
    with open("progreso_oracion_compuesta.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Idioma: {idioma}, Tipo: {tipo}, Puntuación: {puntuacion}/{total}\n")

# Función principal para cuestionarios
def iniciar_cuestionario(tipo, preguntas, idioma):
    print(f"\n--- Cuestionario sobre la Oración Compuesta: {tipo} ({idioma}) ---")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    print(f"\nTu puntuación final en {tipo} ({idioma}) es: {puntuacion}/{len(preguntas)}.")
    return puntuacion, len(preguntas)

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario sobre la Oración Compuesta!")
    playsound("introduccion_oracion_compuesta.mp3")  # Introducción con sonido

    try:
        img = Image.open("oracion_compuesta.jpg")
        img.show()
    except FileNotFoundError:
        print("No se encontró la imagen introductoria.")

    usuario = input("\nPor favor, ingresa tu nombre: ")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Oración Compuesta en Español")
        print("2. Oración Compuesta en Inglés")
        print("3. Salir")
        idioma = input("Elige una opción (1-3): ")

        if idioma == "1":
            preguntas = cuestionario_oracion_compuesta_espanol()
            puntuacion, total = iniciar_cuestionario("Oración Compuesta", preguntas, "Español")
            guardar_progreso(usuario, "Español", "Oración Compuesta", puntuacion, total)

        elif idioma == "2":
            preguntas = cuestionario_oracion_compuesta_ingles()
            puntuacion, total = iniciar_cuestionario("Oración Compuesta", preguntas, "Inglés")
            guardar_progreso(usuario, "Inglés", "Oración Compuesta", puntuacion, total)

        elif idioma == "3":
            print("\n¡Gracias por participar! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

# Ejecutar el programa
menu_principal()
