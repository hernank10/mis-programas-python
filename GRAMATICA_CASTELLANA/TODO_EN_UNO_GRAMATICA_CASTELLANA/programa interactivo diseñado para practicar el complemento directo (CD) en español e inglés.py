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

# Cuestionarios de complemento directo en español
def cuestionario_complemento_directo_espanol():
    return [
        ("¿Cuál de las siguientes oraciones contiene un complemento directo?", 
         ["María canta una canción.", "Pedro corre rápido.", "Ellos están felices.", "El libro está en la mesa."], 1),
        ("¿Qué es un complemento directo?", 
         ["El sujeto de la oración.", "El objeto que recibe la acción del verbo.", 
          "El lugar donde ocurre la acción.", "La persona que realiza la acción."], 2),
        ("Identifica el complemento directo: 'Juan compró un coche.'", 
         ["Juan", "compró", "un coche", "Ninguno"], 3),
        ("¿Cuál oración tiene un complemento directo implícito?", 
         ["¿Quieres café?", "María está leyendo un libro.", "Ellos caminaron al parque.", "Vimos la película ayer."], 1),
        ("Selecciona el pronombre que sustituye al complemento directo: 'Juan compró el coche.'", 
         ["le", "lo", "la", "se"], 2),
    ]

# Cuestionarios de complemento directo en inglés
def cuestionario_complemento_directo_ingles():
    return [
        ("Which of the following sentences contains a direct object?", 
         ["He runs fast.", "She bought a car.", "The cat is sleeping.", "They are happy."], 2),
        ("What is a direct object?", 
         ["The person performing the action.", "The receiver of the action.", 
          "The subject of the sentence.", "The action itself."], 2),
        ("Identify the direct object: 'She reads a book.'", 
         ["She", "reads", "a book", "None"], 3),
        ("Choose the sentence with an implied direct object:", 
         ["Do you understand?", "She is eating an apple.", "They went to the park.", "We saw the movie yesterday."], 1),
        ("Select the correct pronoun for the direct object: 'She bought the car.'", 
         ["her", "it", "them", "he"], 2),
    ]

# Guardar progreso
def guardar_progreso(usuario, idioma, tipo, puntuacion, total):
    with open("progreso_complemento_directo.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Idioma: {idioma}, Tipo: {tipo}, Puntuación: {puntuacion}/{total}\n")

# Función principal para cuestionarios
def iniciar_cuestionario(tipo, preguntas, idioma):
    print(f"\n--- Cuestionario de Complemento Directo: {tipo} ({idioma}) ---")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    print(f"\nTu puntuación final en {tipo} ({idioma}) es: {puntuacion}/{len(preguntas)}.")
    return puntuacion, len(preguntas)

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario de Complemento Directo en Español e Inglés!")
    playsound("introduccion_complemento_directo.mp3")  # Introducción con sonido

    try:
        img = Image.open("complemento_directo.jpg")
        img.show()
    except FileNotFoundError:
        print("No se encontró la imagen introductoria.")

    usuario = input("\nPor favor, ingresa tu nombre: ")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Complemento Directo en Español")
        print("2. Complemento Directo en Inglés")
        print("3. Salir")
        idioma = input("Elige una opción (1-3): ")

        if idioma == "1":
            preguntas = cuestionario_complemento_directo_espanol()
            puntuacion, total = iniciar_cuestionario("Complemento Directo", preguntas, "Español")
            guardar_progreso(usuario, "Español", "Complemento Directo", puntuacion, total)

        elif idioma == "2":
            preguntas = cuestionario_complemento_directo_ingles()
            puntuacion, total = iniciar_cuestionario("Complemento Directo", preguntas, "Inglés")
            guardar_progreso(usuario, "Inglés", "Complemento Directo", puntuacion, total)

        elif idioma == "3":
            print("\n¡Gracias por participar! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

# Ejecutar el programa
menu_principal()
