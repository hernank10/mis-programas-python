import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 110)
    print(f"🔬 {title.upper()} 🔬")
    print("=" * 110)
    print()

def show_introduction():
    """Introduce el concepto de falacias avanzadas y su relevancia."""
    show_header("Introducción: Analizando la Retórica y la Argumentación Compleja")
    print("¡Bienvenidos, analistas avanzados del pensamiento! 🧠")
    print("En esta lección, llevaremos nuestras habilidades de detección de falacias al siguiente nivel.")
    print("Nos enfrentaremos a argumentos que no solo son erróneos, sino que a menudo buscan engañar de formas más sofisticadas, desviando el foco o apelando a la credulidad.\n")
    
    print("El objetivo es que puedan desentrañar la **retórica engañosa** en los debates, los medios de comunicación y las discusiones académicas, para que puedan formar opiniones verdaderamente informadas y argumentar con solidez.\n")
    
    input("Presiona ENTER para conocer estas falacias avanzadas...")

def show_fallacies():
    """Define y ejemplifica falacias lógicas avanzadas."""
    show_header("Falacias Lógicas Avanzadas")
    
    fallacies = [
        {"name": "Hombre de Paja (Straw Man)", 
         "definition": "Distorsionar, exagerar o tergiversar intencionadamente el argumento de un oponente para que sea más fácil de atacar o refutar, en lugar de abordar el argumento real.", 
         "example": "El candidato propone reducir el presupuesto militar para invertir en educación. Su oponente responde: '¡Así que el candidato quiere dejar a nuestro país indefenso y vulnerable ante nuestros enemigos!'",
         "why_fallacy": "Reducir el presupuesto no significa eliminarlo ni dejar al país indefenso. El oponente distorsionó el argumento original para atacarlo más fácilmente."},
        
        {"name": "Apelación a la Ignorancia (Argumentum ad Ignorantiam)", 
         "definition": "Afirmar que una proposición es verdadera porque no se ha probado que sea falsa, o que es falsa porque no se ha probado que sea verdadera.", 
         "example": "Como nadie ha podido probar que los ovnis no existen, es una prueba de que sí existen.",
         "why_fallacy": "La ausencia de evidencia en contra no es evidencia a favor. La carga de la prueba recae en quien afirma la existencia."},
        
        {"name": "Ad Verecundiam (Apelación a la Falsa Autoridad)", 
         "definition": "Apelar a la opinión de una autoridad que no es experta o relevante en el tema que se discute.", 
         "example": "Mi actor favorito dice que esta nueva dieta es la mejor para la salud, así que debe ser cierto.",
         "why_fallacy": "Un actor, aunque sea famoso, no es una autoridad en nutrición o salud. Su opinión no tiene peso experto en este campo."},
        
        {"name": "Tu Quoque (Tú También)", 
         "definition": "Desviar una crítica o un argumento atacando al acusador por haber hecho lo mismo o algo similar, en lugar de responder a la crítica.", 
         "example": "Padre: 'No deberías fumar, es malo para tu salud.' Hijo: '¡Pero tú fumas también, así que no puedes decirme nada!'",
         "why_fallacy": "El hecho de que el padre fume no invalida la verdad de que fumar es malo para la salud del hijo. Es un intento de desviar la atención de la crítica."},
        
        {"name": "Causa Cuestionable / Causa Única Excesiva", 
         "definition": "Atribuir un efecto complejo a una única causa simple, o confundir correlación con causalidad, ignorando otras causas o la interconexión de factores.", 
         "example": "El bajo rendimiento académico de los estudiantes se debe *únicamente* a que usan sus teléfonos móviles en clase.",
         "why_fallacy": "El rendimiento académico es multifactorial: calidad de enseñanza, motivación, entorno familiar, salud mental, métodos de estudio, etc. Los móviles son un factor, no la única causa."},
        
        {"name": "Falacia de la Composición / División", 
         "definition": "**Composición:** Asumir que lo que es cierto para las partes de un todo debe ser cierto para el todo mismo. / **División:** Asumir que lo que es cierto para el todo debe ser cierto para cada una de sus partes individuales.", 
         "example": "Composición: 'Cada jugador de nuestro equipo es un excelente atleta, así que nuestro equipo es el mejor del torneo.' / División: 'Nuestro equipo de baloncesto es el mejor de la liga, por lo tanto, cada jugador de nuestro equipo es el mejor jugador de baloncesto.'",
         "why_fallacy": "Composición: Un equipo necesita más que atletas individuales excelentes (trabajo en equipo, estrategia, etc.). / División: Ser parte del mejor equipo no significa que cada individuo sea el mejor en solitario."},
    ]

    print("Aquí están algunas falacias más complejas que exigen un análisis cuidadoso:\n")
    for i, f in enumerate(fallacies):
        print(f"--- {i+1}. {f['name'].upper()} ---")
        print(f"   **Definición:** {f['definition']}")
        print(f"   **Ejemplo:** '{f['example']}'")
        print(f"   **¿Por qué es una falacia?** {f['why_fallacy']}\n")
        time.sleep(10)
        input("Presiona ENTER para ver la siguiente falacia...")
        print("=" * 70)
    
    print("\n¡Ahora que tienes estas herramientas, es hora de ponerlas a prueba!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_advanced_fallacy():
    """Juego de identificar la falacia avanzada presente en un argumento."""
    show_header("Juego 1: ¡El Detective de Falacias Avanzadas!")
    print("Te presentaré un argumento complejo. Identifica qué **falacia lógica avanzada** se utiliza.")
    print("Elige la opción correcta entre las que te daré.\n")

    questions = [
        {"text": "El Dr. Pérez, famoso astronauta, apoya la homeopatía. Por lo tanto, la homeopatía debe ser una medicina eficaz.", 
         "options": ["A) Apelación a la Ignorancia", "B) Ad Verecundiam", "C) Hombre de Paja"], 
         "answer": "B", "correct_name": "Ad Verecundiam", "explanation": "El Dr. Pérez es autoridad en astronomía, no en medicina."},
        
        {"text": "Si implementamos el uso de computadoras en todas las aulas, los estudiantes se volverán adictos a las pantallas, dejarán de socializar, y la educación tradicional desaparecerá por completo.", 
         "options": ["A) Tu Quoque", "B) Causa Cuestionable", "C) Pendiente Resbaladiza"], 
         "answer": "C", "correct_name": "Pendiente Resbaladiza", "explanation": "Exagera las consecuencias de un paso inicial sin pruebas de su inevitabilidad."},
        
        {"text": "Tú dices que los coches eléctricos son el futuro. Pero ¿cómo puedes decir eso si tú mismo conduces un coche de gasolina?", 
         "options": ["A) Tu Quoque", "B) Falacia de la Composición", "C) Apelación a la Ignorancia"], 
         "answer": "A", "correct_name": "Tu Quoque", "explanation": "Desvía la crítica al señalar la hipocresía del oponente, sin refutar la idea de los coches eléctricos."},
        
        {"text": "Nadie ha demostrado que la telepatía no exista, por lo tanto, es posible comunicarse telepáticamente.", 
         "options": ["A) Apelación a la Ignorancia", "B) Hombre de Paja", "C) Ad Verecundiam"], 
         "answer": "A", "correct_name": "Apelación a la Ignorancia", "explanation": "La falta de prueba en contra no es prueba a favor."},
        
        {"text": "El equipo de fútbol de la escuela es el mejor del estado, así que cada jugador del equipo es el mejor jugador individual en su posición.", 
         "options": ["A) Falacia de la División", "B) Causa Cuestionable", "C) Generalización Apresurada"], 
         "answer": "A", "correct_name": "Falacia de la División", "explanation": "Lo que es cierto para el todo (el equipo) no necesariamente es cierto para cada una de sus partes (cada jugador individualmente)."},
        
        {"text": "Propuesta: 'Deberíamos establecer un comité estudiantil para mejorar la comunicación con los profesores.' Oponente: '¡Ah, así que quieren un grupo de estudiantes mandones que tomen todas las decisiones en la escuela!'", 
         "options": ["A) Tu Quoque", "B) Hombre de Paja", "C) Causa Cuestionable"], 
         "answer": "B", "correct_name": "Hombre de Paja", "explanation": "Distorsiona la idea de un comité para mejorar la comunicación en un 'grupo de estudiantes mandones' que 'toman todas las decisiones'."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 5 # Limitamos a 5

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Argumento: '{q['text']}'")
        for option in q['options']:
            print(f"   {option}")
        
        while True:
            user_input = input("Tu respuesta (A, B o C): ").upper().strip()
            if user_input in ['A', 'B', 'C']:
                break
            else:
                print("Opción no válida. Por favor, escribe A, B o C.")
        
        if user_input == q['answer']:
            print(f"¡Correcto! Es una **{q['correct_name']}**. 🎉")
            print(f"Explicación: {q['explanation']}")
            score += 1
        else:
            print(f"¡Oops! No es correcto. 🤔")
            print(f"La respuesta correcta era {q['answer']} (**{q['correct_name']}**). Explicación: {q['explanation']}")
        time.sleep(7)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un maestro detectando falacias avanzadas! 🕵️‍♂️")
    input("Presiona ENTER para el siguiente juego...")

def game_deconstruct_and_reconstruct():
    """Juego de deconstruir un argumento falaz y reconstruirlo lógicamente."""
    show_header("Juego 2: ¡Deconstruye y Reconstruye!")
    print("Te daré un argumento que contiene una falacia. Tu misión es primero identificar la falacia y luego **reconstruir un argumento lógico y válido** que aborde el tema de manera justa.\n")

    corrections = [
        {"original": "Nuestro director de escuela no es un buen líder porque no es popular entre los estudiantes.", 
         "type": "Ad Populum", 
         "corrected_hint": "La capacidad de liderazgo de un director debería evaluarse por su visión, su gestión y su impacto en el ambiente educativo, no solo por su popularidad entre los estudiantes.",
         "explanation": "La popularidad no define el liderazgo efectivo. Hay que evaluar acciones y resultados."},
        {"original": "El problema de la contaminación del río es *solo* por la fábrica que construyeron el año pasado.", 
         "type": "Causa Cuestionable", 
         "corrected_hint": "La contaminación del río es un problema complejo que puede tener múltiples causas, como residuos agrícolas, aguas residuales urbanas y, además de la fábrica, otros factores ambientales. Necesitamos una investigación integral.",
         "explanation": "Un problema complejo rara vez tiene una única causa simple."},
        {"original": "Si la escuela permite a los estudiantes usar gorras en el aula, la disciplina se derrumbará por completo, los estudiantes ignorarán todas las reglas y la escuela se convertirá en un caos anárquico.", 
         "type": "Pendiente Resbaladiza", 
         "corrected_hint": "Permitir gorras en el aula es un cambio menor. Se pueden establecer reglas claras para su uso y evaluar su impacto en la disciplina sin asumir un colapso total del orden escolar.",
         "explanation": "No hay una conexión inevitable entre el uso de gorras y el colapso total de la disciplina."},
        {"original": "Tú criticas mi propuesta de proyecto, pero la tuya tiene fallos también. Así que mi propuesta no es tan mala.", 
         "type": "Tu Quoque", 
         "corrected_hint": "Mi propuesta de proyecto debe ser evaluada por sus propios méritos y fallos, independientemente de los fallos que pueda tener la tuya. Discutamos cada una de forma individual.",
         "explanation": "La validez de un argumento no depende de los defectos del argumento o del proponente del otro."},
    ]
    
    random.shuffle(corrections)
    num_questions = 2 # Limitamos a 2

    for i in range(num_questions):
        c = corrections[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Argumento falaz: '{c['original']}'")
        print(f"Tipo de falacia: **{c['type']}**")
        print(f"Pista para deconstruir: {c['explanation']}")
        
        input("\nPresiona ENTER para continuar y reconstruir el argumento...")
        
        user_reconstructed_argument = input("Ahora, reconstruye un argumento lógico y válido sobre el mismo tema: ").strip()
        
        print(f"\nTu reconstrucción: '{user_reconstructed_argument}'")
        print(f"Una forma de reconstruirlo: '{c['corrected_hint']}'")
        print("\n¡Magnífico! ¡Has deconstruido el engaño y reconstruido la lógica! 🎉")
        time.sleep(8)
    
    print(f"\nJuego terminado. ¡Eres un maestro en la construcción de argumentos válidos!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_advanced_fallacy_example():
    """Permite al usuario crear su propio ejemplo de falacia avanzada y corregirlo."""
    show_header("✍️ ¡Crea y Analiza Tus Propias Falacias Avanzadas! ✍️")
    print("Vamos a crear un ejemplo de una de las falacias avanzadas aprendidas.")
    print("Luego, la identificarás y la reescribirás como un argumento sólido.\n")

    fallacy_types = ["Hombre de Paja", "Apelación a la Ignorancia", "Ad Verecundiam", "Tu Quoque", "Causa Cuestionable", "Falacia de la Composición / División"]
    chosen_fallacy = random.choice(fallacy_types)
    
    print(f"Vamos a crear un ejemplo de la falacia: **{chosen_fallacy}**.")
    
    while True:
        original_sentence = input(f"1. Escribe un argumento que sea un ejemplo de **{chosen_fallacy}**: ").strip()
        if original_sentence:
            break
        else:
            print("Por favor, escribe un argumento.")
    
    print(f"\nTu argumento falaz: '{original_sentence}'")
    
    while True:
        identified_type = input(f"¿Qué falacia identificas en tu propio argumento? (Escribe el nombre completo de la falacia): ").strip()
        if identified_type:
            break
        else:
            print("Por favor, identifica la falacia.")

    while True:
        fixed_sentence = input("2. Ahora, refrasea ese argumento para que sea lógico y válido: ").strip()
        if fixed_sentence:
            break
        else:
            print("Por favor, escribe el argumento corregido.")

    print("\n--- ¡Tu Ejemplo Creado, Analizado y Corregido! ---")
    print(f"Tu argumento falaz ({chosen_fallacy}): '{original_sentence}' 🚫")
    print(f"Identificaste: '{identified_type}'")
    print(f"Tu argumento lógico: '{fixed_sentence}' ✅")
    print("\n¡Qué nivel de análisis! ¡Has demostrado un dominio excepcional de las falacias lógicas! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: Falacias Avanzadas (11º Grado)")
        print("1. Introducción: Analizando la Retórica y la Argumentación Compleja")
        print("2. Conocer las Falacias Lógicas Avanzadas")
        print("3. Jugar: ¡El Detective de Falacias Avanzadas!")
        print("4. Jugar: ¡Deconstruye y Reconstruye!")
        print("5. ✍️ ¡Crea y Analiza Tus Propias Falacias Avanzadas! ✍️")
        print("6. Salir de la Lección")
        print("=" * 110)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_fallacies()
        elif choice == '3':
            game_identify_advanced_fallacy()
        elif choice == '4':
            game_deconstruct_and_reconstruct()
        elif choice == '5':
            create_own_advanced_fallacy_example()
        elif choice == '6':
            print("¡Adiós, crítico del pensamiento! Sigue cuestionando, analizando y argumentando con lógica. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
