# Juego de gramática inglesa: Aventura en la Biblioteca de Marte

import random

# Bienvenida e introducción al juego
def bienvenida():
    print("🚀 Bienvenido a la Aventura en la Biblioteca de Marte 🚀")
    print("Explora los misterios de la gramática inglesa mientras ayudas a los habitantes marcianos.")
    print("Tu misión: Completar desafíos de gramática inglesa en cada nivel. ¡Buena suerte!\n")

# Menú principal del juego
def menu_principal():
    print("Elige una opción:")
    print("1. Conocer la Biblioteca de Marte y sus personajes")
    print("2. Aprender conceptos de gramática inglesa")
    print("3. Ejercicios de gramática - Nivel Básico")
    print("4. Ejercicios de gramática - Nivel Intermedio")
    print("5. Ejercicios de gramática - Nivel Avanzado")
    print("6. Salir del juego")

# Introducción a la Biblioteca de Marte y sus personajes
def conocer_personajes():
    print("\n📚 Estás en la Gran Biblioteca de Marte, un centro de conocimiento interplanetario 📚")
    print("Aquí encontrarás a:\n")
    print("- Dr. Lexicon, un sabio lingüista que te guiará en los misterios de la gramática inglesa.")
    print("- Astrid, la robot bibliotecaria, que te ofrece pistas y te recompensa con insignias.")
    print("- Max, un joven marciano que te desafiará con pruebas especiales.")
    print("¡Explora y aprende mientras ayudas a estos personajes a preservar el conocimiento del idioma inglés!\n")

# Ejercicios de gramática por niveles
def nivel_basico():
    print("\n🌌 Nivel Básico: Identificación de Sustantivos y Verbos 🌌")
    print("Dr. Lexicon: 'Identifica si la palabra es un sustantivo o un verbo. Buena suerte!'")
    palabras = {'run': 'verbo', 'book': 'sustantivo', 'jump': 'verbo', 'apple': 'sustantivo'}
    palabra, respuesta = random.choice(list(palabras.items()))
    user_input = input(f"¿'{palabra}' es un sustantivo o un verbo? ").lower()
    if user_input == respuesta:
        print("¡Correcto! Has ganado una insignia de principiante 🎖️")
    else:
        print("Incorrecto. ¡Sigue intentando para dominar este nivel!\n")

def nivel_intermedio():
    print("\n🌠 Nivel Intermedio: Tiempo Verbal 🌠")
    print("Astrid: 'Indica si la frase está en presente, pasado o futuro.'")
    frases = {'I am eating': 'presente', 'She will travel': 'futuro', 'They played': 'pasado'}
    frase, respuesta = random.choice(list(frases.items()))
    user_input = input(f"¿La frase '{frase}' está en presente, pasado o futuro? ").lower()
    if user_input == respuesta:
        print("¡Bien hecho! Has ganado una insignia de explorador 🌟")
    else:
        print("Incorrecto. ¡Sigue practicando para mejorar!\n")

def nivel_avanzado():
    print("\n🚀 Nivel Avanzado: Estructura de la Oración 🚀")
    print("Max: 'Identifica la estructura de la oración (sujeto, verbo, objeto).'")
    oraciones = {'The cat chased the mouse': 'sujeto, verbo, objeto', 'He loves pizza': 'sujeto, verbo, objeto'}
    oracion, respuesta = random.choice(list(oraciones.items()))
    user_input = input(f"¿Cuál es la estructura de la oración '{oracion}'? ").lower()
    if user_input == respuesta:
        print("¡Fantástico! Has ganado la insignia de maestro 🏆")
    else:
        print("Incorrecto. ¡No te rindas, dominarás este nivel!\n")

# Función principal para ejecutar el juego
def ejecutar_juego():
    bienvenida()
    while True:
        menu_principal()
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == '1':
            conocer_personajes()
        elif opcion == '2':
            print("\nConceptos básicos de gramática inglesa:")
            print("- Noun (Sustantivo): persona, lugar, cosa o idea.")
            print("- Verb (Verbo): acción o estado.")
            print("- Tense (Tiempo Verbal): indica el tiempo de la acción.")
            print("- Subject-Verb-Object: estructura básica de las oraciones.")
        elif opcion == '3':
            nivel_basico()
        elif opcion == '4':
            nivel_intermedio()
        elif opcion == '5':
            nivel_avanzado()
        elif opcion == '6':
            print("Gracias por jugar. ¡Hasta la próxima aventura en Marte!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Iniciar el juego
ejecutar_juego()
