import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 95)
    print(f"🧠 {title.upper()} 🧠")
    print("=" * 95)
    print()

def show_introduction():
    """Introduce los conceptos de petición de principio, apelación a la tradición y causa falsa/simplificada."""
    show_header("Introducción: Razonamiento Engañoso y Causas Complejas")
    print("¡Hola, pensadores avanzados! 🚀")
    print("En esta lección, vamos a afinar nuestra habilidad para detectar argumentos que, aunque suenen bien, nos engañan.")
    print("Aprenderemos a cuestionar tres formas de 'lógica' defectuosa:\n")
    
    print("1. 🔄 **'Girar en Círculos' (Petición de Principio):**")
    print("   Imagina que alguien dice: 'La honestidad es lo mejor, porque es bueno ser honesto.'")
    print("   ¿Te está dando una razón nueva? No, ¡está usando la misma idea para probarse a sí misma!")
    print("   Es como si dijeran: 'Esto es verdad porque es verdad'. No hay una razón real detrás.\n")
    
    print("2. ⏳ **'Porque Siempre se Hizo Así' (Apelación a la Tradición):**")
    print("   Alguien insiste: 'Debemos usar lápiz y papel para tomar apuntes en clase porque así se ha hecho siempre.'")
    print("   ¿Es eso una buena razón para no usar una tablet o un computador, si son más eficientes ahora?")
    print("   Que algo sea **viejo o tradicional** no lo hace automáticamente **mejor o correcto** hoy.\n")

    print("3. 🧩 **'Un Problema, Una Sola Causa' (Causa Falsa Simplificada):**")
    print("   Si el promedio de notas de la clase bajó, y alguien dice: 'La culpa es solo del profesor, él no explica bien.'")
    print("   ¿Es probable que un problema así de grande tenga solo *una* causa? ¿Y si los estudiantes no estudiaron, o hubo problemas en casa?")
    print("   Los problemas suelen tener **muchas causas**, no solo una simple. Hay que ver el panorama completo.\n")
    
    print("¡Afina tu mente para detectar estos argumentos y buscar la verdadera lógica!\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de petición de principio, apelación a la tradición y causa falsa/simplificada."""
    show_header("Ejemplos: ¿Círculo, Tradición o Causa Simple?")
    
    examples = [
        {"text": "La Biblia es la palabra de Dios, porque lo dice la Biblia.", 
         "type": "CIRCULAR", "explanation": "La prueba de la Biblia es la Biblia misma. No se da una razón externa."},
        {"text": "Debemos seguir el plan de estudios antiguo porque siempre ha funcionado para nuestros abuelos.", 
         "type": "TRADICION", "explanation": "Que haya funcionado antes no significa que sea el mejor o el más relevante para las necesidades actuales."},
        {"text": "El bajo rendimiento de los estudiantes se debe únicamente a que pasan demasiado tiempo en redes sociales.", 
         "type": "CAUSA_SIMPLE", "explanation": "El rendimiento es complejo: influyen estudio, descanso, motivación, calidad de enseñanza, problemas personales, etc. No es solo las redes."},
        {"text": "Es importante practicar deporte porque el ejercicio es fundamental.", 
         "type": "CIRCULAR", "explanation": "Practicar deporte es ejercicio. La frase se prueba a sí misma."},
        {"text": "Siempre hemos celebrado las fiestas de esta manera, así que es la única forma correcta de celebrarlas.", 
         "type": "TRADICION", "explanation": "Las tradiciones son valiosas, pero no excluyen otras formas igualmente válidas o nuevas."},
        {"text": "La crisis económica del país es solo culpa del presidente actual.", 
         "type": "CAUSA_SIMPLE", "explanation": "Las crisis económicas tienen múltiples causas: políticas pasadas, factores globales, mercados, etc., no solo una persona."},
    ]

    print("Lee cada frase y piensa si 'gira en círculos', 'apela a la tradición' o simplifica una 'causa compleja'.\n")
    for i, ex in enumerate(examples):
        print(f"\n--- Ejemplo {i+1} ---")
        print(f"Frase: '{ex['text']}'")
        input("Presiona ENTER para ver la respuesta...")
        
        if ex['type'] == "CIRCULAR":
            print(f"¡Es 'GIRAR EN CÍRCULOS' (Petición de Principio)! 🔄 {ex['explanation']}\n")
        elif ex['type'] == "TRADICION":
            print(f"¡Es 'PORQUE SIEMPRE SE HIZO ASÍ' (Apelación a la Tradición)! ⏳ {ex['explanation']}\n")
        else: # CAUSA_SIMPLE
            print(f"¡Es 'UNA SOLA CAUSA' (Causa Falsa Simplificada)! 🧩 {ex['explanation']}\n")
        time.sleep(6)
        print("=" * 60)

    print("\n¡Ahora es tu turno de ser un verdadero detective de argumentos complejos!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_fallacy_type():
    """Juego de identificar el tipo de error lógico."""
    show_header("Juego 1: ¡El Detector de Argumentos Tramposos!")
    print("Te daré una situación. Dime si es 'CIRCULAR' (C), 'TRADICIÓN' (T) o 'CAUSA SIMPLE' (S).\n")
    print("Escribe 'C', 'T' o 'S'.\n")

    questions = [
        {"text": "El libro es un best-seller porque es el libro más vendido.", 
         "answer": "C", "explanation": "Ser un best-seller y ser el más vendido es lo mismo, no hay una nueva razón."},
        {"text": "Los matrimonios siempre deben ser entre un hombre y una mujer porque así ha sido la tradición por siglos.", 
         "answer": "T", "explanation": "La tradición no es la única base para definir una institución social hoy en día."},
        {"text": "El aumento de la delincuencia se debe solo a la falta de policías en las calles.", 
         "answer": "S", "explanation": "La delincuencia es un problema complejo con múltiples causas: economía, educación, oportunidades, etc."},
        {"text": "Debemos seguir las reglas porque las reglas son importantes para el orden.", 
         "answer": "C", "explanation": "Se usa la importancia de las reglas para justificar las reglas mismas."},
        {"text": "Mis padres me educaron de esta manera, y yo educaré a mis hijos igual, porque es la forma correcta de educar.", 
         "answer": "T", "explanation": "Lo que fue 'correcto' en el pasado puede no ser lo ideal hoy, la sociedad y el conocimiento evolucionan."},
        {"text": "El calentamiento global es solo culpa de las fábricas.", 
         "answer": "S", "explanation": "El calentamiento global tiene muchas causas: deforestación, transporte, agricultura, consumo energético, etc."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 4 # Limitamos a 4

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Frase: '{q['text']}'")
        
        while True:
            user_input = input("¿'CIRCULAR' (C), 'TRADICIÓN' (T) o 'CAUSA SIMPLE' (S)?: ").upper().strip()
            if user_input in ['C', 'T', 'S']:
                break
            else:
                print("Por favor, escribe 'C', 'T' o 'S'.")
        
        if user_input == q['answer']:
            print("¡Correcto! 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print("¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era '{q['answer']}'. Explicación: {q['explanation']}")
        time.sleep(6)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un gran detector de argumentos tramposos! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_improve_the_argument():
    """Juego de mejorar un argumento que contiene una de las falacias."""
    show_header("Juego 2: ¡Mejora el Argumento!")
    print("Te daré un argumento con un error lógico. Tu misión es mejorarlo, dándole una razón real, considerando múltiples causas o evaluando la tradición.\n")

    corrections = [
        {"original": "Los buenos estudiantes obtienen buenas notas porque son buenos estudiantes.", 
         "type": "CIRCULAR", "corrected_hint": "Los buenos estudiantes obtienen buenas notas porque son disciplinados, estudian con constancia y prestan atención en clase.",
         "explanation": "Hay que dar razones concretas de por qué son 'buenos estudiantes'."},
        {"original": "Siempre hemos tenido dos recreos al día, así que es la mejor manera de organizar el horario escolar.", 
         "type": "TRADICION", "corrected_hint": "Podríamos evaluar si dos recreos siguen siendo la mejor opción para las necesidades de aprendizaje y energía de los estudiantes hoy en día.",
         "explanation": "No basta con la tradición, hay que evaluar la utilidad actual."},
        {"original": "El aumento del acoso escolar se debe solo a los videojuegos violentos.", 
         "type": "CAUSA_SIMPLE", "corrected_hint": "El acoso escolar es un problema complejo que puede tener muchas causas: ambiente familiar, presión de grupo, problemas emocionales, falta de empatía, etc.",
         "explanation": "Se deben considerar múltiples factores para un problema complejo."},
        {"original": "Confío en él porque es digno de confianza.", 
         "type": "CIRCULAR", "corrected_hint": "Confío en él porque siempre cumple su palabra y demuestra responsabilidad en lo que hace.",
         "explanation": "Dar razones específicas que construyan confianza."},
    ]
    
    random.shuffle(corrections)
    num_questions = 2 # Limitamos a 2

    for i in range(num_questions):
        c = corrections[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Argumento con error: '{c['original']}'")
        print(f"Tipo de error: {'Circular' if c['type'] == 'CIRCULAR' else ('Tradición' if c['type'] == 'TRADICION' else 'Causa Simplificada')}")
        print(f"Pista para pensar: {c['explanation']}")
        
        user_improved_argument = input("Escribe cómo mejorarías este argumento: ").strip()
        
        print(f"\nTu respuesta: '{user_improved_argument}'")
        print(f"Una forma de mejorarlo: '{c['corrected_hint']}'")
        print("\n¡Impresionante! ¡Has aprendido a construir argumentos más fuertes y claros! 🎉")
        time.sleep(7)
    
    print(f"\nJuego terminado. ¡Eres un maestro mejorando la lógica!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_fallacy_example():
    """Permite al usuario crear su propio ejemplo de falacia y corregirlo."""
    show_header("✍️ ¡Crea y Corrige Tus Propios Argumentos Engañosos! ✍️")
    print("Vamos a crear una frase con 'razonamiento circular', 'apelación a la tradición' o 'causa falsa simplificada'.")
    print("Luego, tú la corregirás para que sea lógicamente más sólida.\n")

    while True:
        original_sentence = input("1. Escribe una frase con un argumento tramposo (Ej: 'Este auto es el mejor porque es superior a los demás'): ").strip()
        if original_sentence:
            break
        else:
            print("Por favor, escribe una frase.")
    
    print(f"\nTu frase original con el error: '{original_sentence}'")

    while True:
        fixed_sentence = input("2. Ahora, escribe cómo la mejorarías con una lógica más sólida (Ej: 'Este auto es el mejor porque tiene mayor eficiencia de combustible y es muy seguro según las pruebas'): ").strip()
        if fixed_sentence:
            break
        else:
            print("Por favor, escribe la frase corregida.")

    print("\n--- ¡Tu Ejemplo Creado y Corregido! ---")
    print(f"Tu frase con argumento tramposo: '{original_sentence}' 🔄⏳🧩")
    print(f"Tu frase con lógica sólida: '{fixed_sentence}' ✅")
    print("\n¡Qué buen trabajo! ¡Has aprendido a construir y analizar argumentos con un pensamiento crítico agudo! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: ¡No es tan Obvio! (9º Grado)")
        print("1. Introducción: Razonamiento Engañoso y Causas Complejas")
        print("2. Ver Ejemplos")
        print("3. Jugar: ¡El Detector de Argumentos Tramposos!")
        print("4. Jugar: ¡Mejora el Argumento!")
        print("5. ✍️ ¡Crea y Corrige Tus Propios Argumentos Engañosos! ✍️")
        print("6. Salir de la Lección")
        print("=" * 95)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            game_identify_fallacy_type()
        elif choice == '4':
            game_improve_the_argument()
        elif choice == '5':
            create_own_fallacy_example()
        elif choice == '6':
            print("¡Adiós! Sigue buscando la lógica real y no te dejes engañar por las apariencias. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
