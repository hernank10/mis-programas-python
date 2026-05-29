# -*- coding: utf-8 -*-
import sys

# Define las preguntas y respuestas para cada nivel.
# Las respuestas se almacenan en minúsculas para una comparación más fácil.

NIVEL_1_PREGUNTAS = {
    "He is a student.": "Is he a student?",
    "They are from Spain.": "Are they from Spain?",
    "She is happy.": "Is she happy?",
    "I am a teacher.": "Am I a teacher?",
    "You are a doctor.": "Are you a doctor?",
}

NIVEL_2_PREGUNTAS = {
    "She is a lawyer.": "Is she a lawyer?",
    "He is your brother.": "Is he your brother?",
    "They are our friends.": "Are they our friends?",
    "You are my hope.": "Are you my hope?",
    "That is his car.": "Is that his car?",
}

NIVEL_3_PREGUNTAS = {
    "She is a software developer.": "Is she a software developer?",
    "He is a hope for the family.": "Is he a hope for the family?",
    "This is a complex problem.": "Is this a complex problem?",
    "That is her new laptop.": "Is that her new laptop?",
    "They are creative artists.": "Are they creative artists?",
}

def limpiar_respuesta(respuesta):
    """
    Limpia la respuesta del usuario para una comparación más precisa.
    Elimina signos de puntuación y espacios, y convierte a minúsculas.
    """
    respuesta_limpia = respuesta.strip().lower()
    respuesta_limpia = respuesta_limpia.replace("?", "").replace("¿", "").replace(".", "").replace(",", "")
    return respuesta_limpia

def ejecutar_nivel(nivel, preguntas, reglas):
    """
    Función genérica para ejecutar los ejercicios de cada nivel.
    Muestra las reglas, solicita la respuesta y verifica si es correcta.
    """
    print(f"\n--- Nivel {nivel}: {reglas['titulo']} ---")
    print(reglas['descripcion'])
    print(f"Ejemplo: {reglas['ejemplo']}")

    for afirmacion, respuesta_correcta in preguntas.items():
        print(f"\nAfirmación: '{afirmacion}'")
        respuesta_usuario = input("Tu pregunta: ")

        if limpiar_respuesta(respuesta_usuario) == limpiar_respuesta(respuesta_correcta):
            print("¡Correcto! ✅")
        else:
            print(f"Incorrecto. La respuesta correcta es: '{respuesta_correcta}' ❌")

    input("\nPresiona Enter para volver al menú...")

def mostrar_menu():
    """
    Muestra el menú principal y maneja la navegación entre los niveles.
    """
    while True:
        print("\n--- Curso de Formación de Preguntas en Inglés ---")
        print("Elige un nivel de dificultad para comenzar:")
        print("1. Nivel 1: Pronombres + 'to be'")
        print("2. Nivel 2: Pronombres + 'to be' + Sustantivos Comunes")
        print("3. Nivel 3: Pronombres + 'to be' + Sustantivos Compuestos/Abstractos")
        print("4. Salir")

        opcion = input("Tu opción: ")

        if opcion == '1':
            reglas = {
                'titulo': "Pronombres + 'to be'",
                'descripcion': "Regla: Invierte el orden de la afirmación. El verbo 'to be' va al principio.",
                'ejemplo': "'He is a student.' -> 'Is he a student?'"
            }
            ejecutar_nivel(1, NIVEL_1_PREGUNTAS, reglas)
        elif opcion == '2':
            reglas = {
                'titulo': "Pronombres + 'to be' + Sustantivos Comunes",
                'descripcion': "Regla: La estructura es 'to be' + pronombre + artículo/posesivo + sustantivo. Presta atención a los artículos 'a'/'an' y a los posesivos.",
                'ejemplo': "'She is a lawyer.' -> 'Is she a lawyer?'"
            }
            ejecutar_nivel(2, NIVEL_2_PREGUNTAS, reglas)
        elif opcion == '3':
            reglas = {
                'titulo': "Pronombres + 'to be' + Sustantivos Compuestos/Abstractos",
                'descripcion': "Regla: La misma estructura anterior, pero con sustantivos más complejos o abstractos.",
                'ejemplo': "'He is a software developer.' -> 'Is he a software developer?'"
            }
            ejecutar_nivel(3, NIVEL_3_PREGUNTAS, reglas)
        elif opcion == '4':
            print("¡Adiós! ¡Sigue practicando! 👋")
            sys.exit()
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 4.")

if __name__ == "__main__":
    mostrar_menu()
