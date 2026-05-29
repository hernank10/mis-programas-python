# -*- coding: utf-8 -*-
import sys

# Define las preguntas y respuestas para cada ejercicio.
# Las respuestas se almacenan en minúsculas para facilitar la comparación.

EJERCICIO1_PREGUNTAS = {
    "She is a lawyer.": "¿Is she a lawyer?",
    "They are from Colombia.": "¿Are they from Colombia?",
    "I am a student.": "¿Am I a student?",
    "You are a teacher.": "¿Are you a teacher?",
    "He is happy.": "¿Is he happy?",
}

EJERCICIO2_PREGUNTAS = {
    "They like pizza.": "Do they like pizza?",
    "She works in a hospital.": "Does she work in a hospital?",
    "You speak English.": "Do you speak English?",
    "He plays soccer.": "Does he play soccer?",
    "We study for the exam.": "Do we study for the exam?",
}

EJERCICIO3_PREGUNTAS = {
    "They went to the store.": "Did they go to the store?",
    "She ate dinner.": "Did she eat dinner?",
    "He finished the book.": "Did he finish the book?",
    "You traveled to Spain.": "Did you travel to Spain?",
    "I studied for the test.": "Did I study for the test?",
}

EJERCICIO4_PREGUNTAS = [
    {"afirmacion": "My friend is a musician.", "pregunta": "¿Who is your friend?", "palabra": "who"},
    {"afirmacion": "She is in Paris.", "pregunta": "¿Where is she?", "palabra": "where"},
    {"afirmacion": "That is my sister.", "pregunta": "¿Who is that?", "palabra": "who"},
    {"afirmacion": "He is a firefighter.", "pregunta": "¿What is he?", "palabra": "what"},
]

def limpiar_respuesta(respuesta):
    """Limpia la respuesta del usuario para una comparación más precisa."""
    # Elimina los signos de interrogación y los espacios en blanco.
    return respuesta.strip().replace("?", "").replace("¿", "").lower()

def ejecutar_ejercicio(titulo, reglas, preguntas):
    """Función genérica para ejecutar los ejercicios."""
    print("\n--- " + titulo + " ---")
    print(reglas)
    
    # Bucle para cada pregunta del ejercicio
    for afirmacion, respuesta_correcta in preguntas.items():
        print(f"\nAfirmación: '{afirmacion}'")
        respuesta_usuario = input("Tu pregunta: ")
        
        # Compara la respuesta del usuario con la respuesta correcta
        if limpiar_respuesta(respuesta_usuario) == limpiar_respuesta(respuesta_correcta):
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: '{respuesta_correcta}'")
    
    input("\nPresiona Enter para volver al menú principal...")

def ejecutar_ejercicio4():
    """Función específica para el ejercicio de palabras de pregunta."""
    print("\n--- Ejercicio 4: Palabras de Pregunta (who, what, where) ---")
    print("Regla: Usa 'who' para personas, 'what' para profesiones, 'where' para lugares.")
    
    for item in EJERCICIO4_PREGUNTAS:
        print(f"\nAfirmación: '{item['afirmacion']}'")
        
        # Le pide al usuario que ingrese la palabra de pregunta
        respuesta_usuario = input("Ingresa la palabra de pregunta (who, what, where): ")
        
        # Compara la respuesta
        if limpiar_respuesta(respuesta_usuario) == item['palabra']:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La palabra correcta es: '{item['palabra']}'")
    
    input("\nPresiona Enter para volver al menú principal...")

def mostrar_menu():
    """Muestra el menú principal y maneja la navegación."""
    while True:
        print("\n--- ---")
        print("1. Ejercicio 1: Preguntas con el verbo 'to be'")
        print("2. Ejercicio 2: Preguntas con 'do' y 'does'")
        print("3. Ejercicio 3: Preguntas con 'did'")
        print("4. Ejercicio 4: Palabras de Pregunta (who, what, where)")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            reglas = "Regla: Invierte el orden de la afirmación. El verbo 'to be' va al principio. Ejemplo: 'He is happy' -> 'Is he happy?'"
            ejecutar_ejercicio("Ejercicio 1: Preguntas con 'to be'", reglas, EJERCICIO1_PREGUNTAS)
        elif opcion == '2':
            reglas = "Regla: Usa 'do' (para I, you, we, they) o 'does' (para he, she, it) al principio. Ejemplo: 'You speak English' -> 'Do you speak English?'"
            ejecutar_ejercicio("Ejercicio 2: Preguntas con 'do' y 'does'", reglas, EJERCICIO2_PREGUNTAS)
        elif opcion == '3':
            reglas = "Regla: Usa 'did' al principio para todos los pronombres. El verbo principal vuelve a su forma base. Ejemplo: 'She ate dinner' -> 'Did she eat dinner?'"
            ejecutar_ejercicio("Ejercicio 3: Preguntas con 'did'", reglas, EJERCICIO3_PREGUNTAS)
        elif opcion == '4':
            ejecutar_ejercicio4()
        elif opcion == '5':
            print("¡Adiós! ¡Sigue practicando!")
            sys.exit()
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")

# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()
