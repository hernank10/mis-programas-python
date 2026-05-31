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

# Cuestionarios por tipo de sustantivo
def cuestionario_comunes():
    return [
        ("¿Cuál es el sustantivo común para 'perro'?", ["Dog", "Fido", "Poodle", "Bulldog"], 1),
        ("¿Cuál es el sustantivo común para 'libro'?", ["Book", "Bible", "Dictionary", "Notebook"], 1),
    ]

def cuestionario_propios():
    return [
        ("¿Cuál es el sustantivo propio para 'un país'?", ["Country", "America", "Land", "Region"], 2),
        ("¿Cuál es el sustantivo propio para 'un nombre'?", ["Person", "John", "Human", "Teacher"], 2),
    ]

def cuestionario_contables():
    return [
        ("¿Cuál es un sustantivo contable?", ["Apple", "Water", "Rice", "Sugar"], 1),
        ("¿Cuál es un sustantivo contable?", ["Car", "Freedom", "Happiness", "Love"], 1),
    ]

def cuestionario_incontables():
    return [
        ("¿Cuál es un sustantivo incontable?", ["Money", "Chair", "Pen", "Table"], 1),
        ("¿Cuál es un sustantivo incontable?", ["Milk", "Orange", "Bottle", "Book"], 1),
    ]

def cuestionario_abstractos():
    return [
        ("¿Cuál es un sustantivo abstracto?", ["Love", "Tree", "Car", "House"], 1),
        ("¿Cuál es un sustantivo abstracto?", ["Freedom", "Table", "Apple", "Chair"], 1),
    ]

def cuestionario_concretos():
    return [
        ("¿Cuál es un sustantivo concreto?", ["Table", "Freedom", "Happiness", "Idea"], 1),
        ("¿Cuál es un sustantivo concreto?", ["Chair", "Liberty", "Justice", "Honesty"], 1),
    ]

# Función para guardar progreso
def guardar_progreso(usuario, tipo, puntuacion, total):
    with open("progreso_sustantivos_tipos.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Tipo: {tipo}, Puntuación: {puntuacion}/{total}\n")

# Función principal para cuestionarios
def iniciar_cuestionario(tipo, preguntas):
    print(f"\n--- Cuestionario de {tipo} ---")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    print(f"\nTu puntuación final en {tipo} es: {puntuacion}/{len(preguntas)}.")
    return puntuacion, len(preguntas)

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario de Sustantivos en Inglés!")
    playsound("introduccion_sustantivos.mp3")  # Introducción con sonido

    try:
        img = Image.open("sustantivos.jpg")
        img.show()
    except FileNotFoundError:
        print("No se encontró la imagen introductoria.")

    usuario = input("\nPor favor, ingresa tu nombre: ")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Sustantivos Comunes")
        print("2. Sustantivos Propios")
        print("3. Sustantivos Contables")
        print("4. Sustantivos Incontables")
        print("5. Sustantivos Abstractos")
        print("6. Sustantivos Concretos")
        print("7. Salir")
        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            preguntas = cuestionario_comunes()
            puntuacion, total = iniciar_cuestionario("Sustantivos Comunes", preguntas)
        elif opcion == "2":
            preguntas = cuestionario_propios()
            puntuacion, total = iniciar_cuestionario("Sustantivos Propios", preguntas)
        elif opcion == "3":
            preguntas = cuestionario_contables()
            puntuacion, total = iniciar_cuestionario("Sustantivos Contables", preguntas)
        elif opcion == "4":
            preguntas = cuestionario_incontables()
            puntuacion, total = iniciar_cuestionario("Sustantivos Incontables", preguntas)
        elif opcion == "5":
            preguntas = cuestionario_abstractos()
            puntuacion, total = iniciar_cuestionario("Sustantivos Abstractos", preguntas)
        elif opcion == "6":
            preguntas = cuestionario_concretos()
            puntuacion, total = iniciar_cuestionario("Sustantivos Concretos", preguntas)
        elif opcion == "7":
            print("\n¡Gracias por participar! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        guardar_progreso(usuario, opcion, puntuacion, total)

# Ejecutar el programa
menu_principal()
