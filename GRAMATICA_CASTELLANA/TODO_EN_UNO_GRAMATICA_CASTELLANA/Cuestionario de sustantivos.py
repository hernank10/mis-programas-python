import os
from playsound import playsound
from PIL import Image

# Función para mostrar una pregunta
def mostrar_pregunta(pregunta, opciones, respuesta_correcta):
    """Muestra una pregunta y evalúa la respuesta del usuario."""
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

# Cuestionario de sustantivos
def cuestionario_sustantivos():
    preguntas = [
        ("¿Cuál es el sustantivo correcto para 'perro' en inglés?",
         ["Cat", "Dog", "Bird", "Fish"], 2),
        ("¿Cuál es el sustantivo correcto para 'libro' en inglés?",
         ["Book", "Table", "Chair", "Pen"], 1),
        ("¿Cuál es el sustantivo correcto para 'mesa' en inglés?",
         ["Lamp", "Table", "Couch", "Desk"], 2),
        ("¿Cuál es el sustantivo correcto para 'casa' en inglés?",
         ["Home", "Car", "Tree", "Street"], 1),
        ("¿Cuál es el sustantivo correcto para 'agua' en inglés?",
         ["Milk", "Juice", "Water", "Tea"], 3),
        # Agrega más preguntas aquí...
    ]
    return preguntas

# Guardar progreso del usuario
def guardar_progreso(usuario, puntuacion, total):
    """Guarda el progreso del usuario en un archivo de texto."""
    with open("progreso_sustantivos.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Puntuación: {puntuacion}/{total}\n")

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario de Sustantivos en Inglés!")
    playsound("introduccion_sustantivos.mp3")  # Archivo de sonido introductorio
    
    try:
        img = Image.open("sustantivos.jpg")
        img.show()
    except FileNotFoundError:
        print("No se encontró la imagen introductoria.")
    
    usuario = input("Por favor, ingresa tu nombre: ")
    print(f"\nHola {usuario}, ¡vamos a practicar sustantivos en inglés!")
    
    preguntas = cuestionario_sustantivos()
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    
    print(f"\n¡Has completado el cuestionario! Tu puntuación final es {puntuacion}/{len(preguntas)}.")
    guardar_progreso(usuario, puntuacion, len(preguntas))

# Ejecutar el programa
menu_principal()
