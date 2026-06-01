import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 100)
    print(f"🎓 {title.upper()} 🎓")
    print("=" * 100)
    print()

def show_introduction():
    """Introduce el concepto de falacias lógicas y su importancia."""
    show_header("Introducción: ¿Qué Son las Falacias Lógicas?")
    print("¡Hola, jóvenes lógicos! 💡")
    print("A lo largo de los años, hemos aprendido a pensar con claridad y a identificar argumentos débiles.")
    print("Ahora, vamos a ponerles nombre a esas trampas en el razonamiento que nos engañan: ¡las **Falacias Lógicas**!\n")
    
    print("Una **falacia lógica** es un error en la forma en que se construye un argumento, lo que hace que el argumento sea inválido, incluso si la conclusión *parece* correcta.")
    print("Identificarlas es clave para:")
    print("   ✅ Entender mejor lo que otros dicen.")
    print("   ✅ Construir argumentos más sólidos para tus propias ideas.")
    print("   ✅ Evitar ser engañado por información falsa o manipuladora.\n")
    
    print("Hoy exploraremos algunas de las falacias más comunes que ya hemos visto de otra forma, ¡pero ahora con sus nombres 'oficiales'!\n")
    input("Presiona ENTER para conocerlas...")

def show_fallacies():
    """Define y ejemplifica varias falacias lógicas."""
    show_header("Falacias Lógicas Comunes")
    
    fallacies = [
        {"name": "Ad Hominem (Ataque Personal)", 
         "definition": "Atacar a la persona que presenta el argumento, en lugar de refutar el argumento mismo.", 
         "example": "Juan dice que deberíamos reciclar más, pero Juan es muy desordenado, así que su idea no vale.",
         "why_fallacy": "El desorden de Juan no tiene nada que ver con la validez de la idea de reciclar."},
        
        {"name": "Ad Populum (Apelación a la Popularidad)", 
         "definition": "Afirmar que algo es verdad o correcto porque muchas personas lo creen o lo hacen.", 
         "example": "Debes comprar este nuevo teléfono, ¡todos tus amigos ya lo tienen y es lo más popular!",
         "why_fallacy": "La popularidad no garantiza que sea la mejor opción para *ti* o que sea intrínsecamente bueno."},
        
        {"name": "Falsa Causa (Post Hoc Ergo Propter Hoc)", 
         "definition": "Asumir que si un evento ocurre después de otro, el primero debe ser la causa del segundo.", 
         "example": "Desde que me puse mi amuleto de la suerte, he tenido buenas notas. Mi amuleto me hace inteligente.",
         "why_fallacy": "La buena suerte o el amuleto no son la causa de las buenas notas; el esfuerzo y el estudio sí lo son. Es una coincidencia."},
        
        {"name": "Falso Dilema / Falsa Dicotomía", 
         "definition": "Presentar solo dos opciones como si fueran las únicas posibles, cuando en realidad existen más alternativas.", 
         "example": "O apoyas completamente nuestra propuesta, o estás en contra del progreso.",
         "why_fallacy": "Puede haber otras formas de progreso, o puedes estar de acuerdo con partes de la propuesta pero no con todo."},
        
        {"name": "Generalización Apresurada", 
         "definition": "Llegar a una conclusión amplia o general basándose en una evidencia insuficiente o muy limitada.", 
         "example": "Conocí a dos adolescentes que eran muy groseros. Por lo tanto, todos los adolescentes son groseros.",
         "why_fallacy": "Dos ejemplos son insuficientes para generalizar a toda una población de adolescentes."},
        
        {"name": "Pendiente Resbaladiza (Slippery Slope)", 
         "definition": "Afirmar que un primer paso, aparentemente inocente, inevitablemente conducirá a una serie de consecuencias negativas y desastrosas, sin pruebas suficientes.", 
         "example": "Si permitimos que los estudiantes coman chicle en clase, luego querrán comer en todo momento, y la escuela se convertirá en un caos de basura y ruido.",
         "why_fallacy": "Comer chicle no necesariamente lleva a un colapso total del orden escolar. Se exagera la cadena de consecuencias."},
    ]

    print("Aquí están algunas de las falacias lógicas más importantes:\n")
    for i, f in enumerate(fallacies):
        print(f"--- {i+1}. {f['name'].upper()} ---")
        print(f"   **Definición:** {f['definition']}")
        print(f"   **Ejemplo:** '{f['example']}'")
        print(f"   **¿Por qué es una falacia?** {f['why_fallacy']}\n")
        time.sleep(8)
        input("Presiona ENTER para ver la siguiente falacia...")
        print("=" * 65)
    
    print("\n¡Ahora que conoces sus nombres y cómo funcionan, vamos a practicar detectándolas!\n")
    input("Presiona ENTER para ir a los juegos...")

def game_identify_fallacy():
    """Juego de identificar la falacia presente en un argumento."""
    show_header("Juego 1: ¡El Detective de Falacias!")
    print("Te daré una frase o argumento. Tienes que identificar qué **falacia lógica** contiene.")
    print("Elige la opción correcta entre las que te daré.\n")

    questions = [
        {"text": "Mi profesor no sabe nada de historia porque usa gafas viejas.", 
         "options": ["A) Ad Hominem", "B) Falsa Causa", "C) Ad Populum"], 
         "answer": "A", "correct_name": "Ad Hominem", "explanation": "Ataca al profesor por sus gafas, no a su conocimiento de historia."},
        
        {"text": "Todos los estudiantes de mi clase están usando esta aplicación, así que debe ser la mejor para estudiar.", 
         "options": ["A) Pendiente Resbaladiza", "B) Ad Populum", "C) Falso Dilema"], 
         "answer": "B", "correct_name": "Ad Populum", "explanation": "Asume que es lo mejor solo por su popularidad entre los compañeros."},
        
        {"text": "Me caí al salir de casa hoy, seguro es porque el gato negro se cruzó en mi camino.", 
         "options": ["A) Generalización Apresurada", "B) Falsa Causa", "C) Ad Hominem"], 
         "answer": "B", "correct_name": "Falsa Causa", "explanation": "Cree que el gato negro causó su caída, sin conexión lógica real."},
        
        {"text": "O estás conmigo en esto, o eres mi enemigo.", 
         "options": ["A) Falso Dilema", "B) Pendiente Resbaladiza", "C) Ad Populum"], 
         "answer": "A", "correct_name": "Falso Dilema", "explanation": "Presenta solo dos opciones extremas, cuando hay más posibilidades."},
        
        {"text": "Probé dos restaurantes de esta ciudad y la comida era horrible. Toda la comida de esta ciudad es horrible.", 
         "options": ["A) Falsa Causa", "B) Ad Hominem", "C) Generalización Apresurada"], 
         "answer": "C", "correct_name": "Generalización Apresurada", "explanation": "Dos ejemplos son insuficientes para generalizar sobre toda la comida de la ciudad."},
        
        {"text": "Si bajamos los precios del autobús escolar un poco, nadie querrá pagar nunca, las rutas se cerrarán y los estudiantes no podrán ir a la escuela.", 
         "options": ["A) Ad Populum", "B) Pendiente Resbaladiza", "C) Falso Dilema"], 
         "answer": "B", "correct_name": "Pendiente Resbaladiza", "explanation": "Sugiere una cadena de eventos negativos sin pruebas lógicas."},
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
        time.sleep(6)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Eres un excelente detective de falacias! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente juego...")

def game_reframe_argument():
    """Juego de transformar un argumento falaz en uno lógico."""
    show_header("Juego 2: ¡Argumentos Bien Construidos!")
    print("Te daré un argumento que contiene una falacia. Tu misión es **refrasearlo** para que sea un argumento lógico y válido.\n")

    corrections = [
        {"original": "El entrenador es demasiado viejo para entender las estrategias modernas de fútbol, así que sus ideas no sirven.", 
         "type": "Ad Hominem", 
         "corrected_hint": "Las ideas del entrenador sobre las estrategias modernas de fútbol deberían ser evaluadas por su contenido, no por su edad. ¿Qué proponemos para mejorarlas?",
         "explanation": "Hay que centrarse en las ideas, no en la edad."},
        {"original": "Todo el mundo está comprando boletos para este concierto, ¡así que debe ser el mejor evento del año!", 
         "type": "Ad Populum", 
         "corrected_hint": "Muchos están comprando boletos para este concierto. Podríamos investigar qué artistas se presentarán y si su música nos gusta, para decidir si es un buen evento para nosotros.",
         "explanation": "La popularidad no es prueba de calidad personal. Hay que buscar razones propias."},
        {"original": "Desde que me gradué de la primaria, las cosas me han ido mal. La primaria era mi amuleto de la suerte.", 
         "type": "Falsa Causa", 
         "corrected_hint": "Las cosas en la vida pueden ser complejas. Mis experiencias después de la primaria son resultados de mis decisiones, el contexto, y otros factores, no de mi graduación.",
         "explanation": "No hay relación causal entre graduarse y tener 'mala suerte'."},
        {"original": "O apoyas la construcción del nuevo centro comercial, o no te importa el desarrollo económico de nuestra ciudad.", 
         "type": "Falso Dilema", 
         "corrected_hint": "Apoyo el desarrollo económico de la ciudad, pero creo que deberíamos considerar otras opciones además del centro comercial, como invertir en negocios locales o mejorar la infraestructura existente.",
         "explanation": "Existen más opciones para el desarrollo económico que solo la construcción del centro comercial."},
    ]
    
    random.shuffle(corrections)
    num_questions = 3 # Limitamos a 3

    for i in range(num_questions):
        c = corrections[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Argumento falaz: '{c['original']}'")
        print(f"Tipo de falacia: **{c['type']}**")
        print(f"Pista para pensar: {c['explanation']}")
        
        user_fixed_argument = input("Escribe cómo lo refrasearías lógicamente: ").strip()
        
        print(f"\nTu respuesta: '{user_fixed_argument}'")
        print(f"Una forma de refrasearlo: '{c['corrected_hint']}'")
        print("\n¡Excelente! ¡Has transformado argumentos falaces en lógicos! 🎉")
        time.sleep(7)
    
    print(f"\nJuego terminado. ¡Eres un maestro construyendo argumentos válidos!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_fallacy_example():
    """Permite al usuario crear su propio ejemplo de falacia y corregirlo."""
    show_header("✍️ ¡Crea y Corrige Tus Propias Falacias! ✍️")
    print("Vamos a crear un ejemplo de una de las falacias aprendidas.")
    print("Luego, tú la corregirás para que sea un argumento sólido.\n")

    fallacy_types = ["Ad Hominem", "Ad Populum", "Falsa Causa", "Falso Dilema", "Generalización Apresurada", "Pendiente Resbaladiza"]
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
        fixed_sentence = input("2. Ahora, refrasea ese argumento para que sea lógico y válido: ").strip()
        if fixed_sentence:
            break
        else:
            print("Por favor, escribe el argumento corregido.")

    print("\n--- ¡Tu Ejemplo Creado y Corregido! ---")
    print(f"Tu argumento falaz ({chosen_fallacy}): '{original_sentence}' 🚫")
    print(f"Tu argumento lógico: '{fixed_sentence}' ✅")
    print("\n¡Qué trabajo tan increíble! ¡Dominas la identificación y corrección de falacias! 🎉")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: Descubriendo Falacias Lógicas (10º Grado)")
        print("1. Introducción: ¿Qué Son las Falacias Lógicas?")
        print("2. Conocer las Falacias Lógicas Comunes")
        print("3. Jugar: ¡El Detective de Falacias!")
        print("4. Jugar: ¡Argumentos Bien Construidos!")
        print("5. ✍️ ¡Crea y Corrige Tus Propias Falacias! ✍️")
        print("6. Salir de la Lección")
        print("=" * 100)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_fallacies()
        elif choice == '3':
            game_identify_fallacy()
        elif choice == '4':
            game_reframe_argument()
        elif choice == '5':
            create_own_fallacy_example()
        elif choice == '6':
            print("¡Adiós, futuro pensador crítico! Sigue aplicando la lógica en tu vida diaria. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
