import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 90)
    print(f"🧠 {title.upper()} 🧠")
    print("=" * 90)
    print()

def show_introduction():
    """Introduce los conceptos de estructuras textuales y organización de argumentos."""
    show_header("Introducción: ¡Arquitectos del Conocimiento!")
    print("¡Hola, jóvenes arquitectos de ideas! 🏗️")
    print("Ya sabemos que los textos tienen patrones, pero ¿sabían que los autores los usan a propósito para convencernos o informarnos de una manera especial?")
    print("Hoy, vamos a ser detectives de cómo se construyen los textos y aprenderemos a construir los nuestros de forma muy inteligente.\n")
    
    print("En esta lección, aprenderán a:")
    print("   ✅ Reconocer cómo el autor organiza sus ideas y por qué.")
    print("   ✅ Organizar sus propios argumentos para que sean muy claros y convincentes.")
    print("   ✅ Notar si la forma en que se presenta la información nos quiere hacer pensar algo específico.\n")
    
    print("¡Prepárense para construir y desmantelar textos con su mente crítica!\n")
    input("Presiona ENTER para comenzar a explorar...")

def show_textual_structures_concept():
    """Explica los tipos de estructuras textuales y su propósito."""
    show_header("Estructuras Textuales: ¡El Esqueleto de las Ideas!")
    print("Así como un edificio tiene un esqueleto, los textos tienen una estructura que organiza sus ideas.\n")
    print("Vamos a repasar y añadir algunas formas clave en que los autores organizan lo que escriben:\n")
    
    print("--- 1. **Secuencia o Cronológica (¿Cuándo o en qué orden?)** ⏳")
    print("   **Propósito:** Contar una historia, explicar un proceso, mostrar la evolución de algo.")
    print("   **Ejemplo de uso:** Recetas de cocina, biografías, pasos de un experimento científico.")
    print("   **Pistas:** Fechas, números de pasos, palabras como 'primero', 'luego', 'después', 'finalmente'.")

    print("\n--- 2. **Causa y Efecto (¿Por qué pasó? ¿Qué resultados tuvo?)** ➡️")
    print("   **Propósito:** Explicar las razones de un suceso y sus consecuencias.")
    print("   **Ejemplo de uso:** Artículos sobre el cambio climático, explicación de fenómenos naturales, resultados de experimentos.")
    print("   **Pistas:** 'Porque', 'debido a', 'por eso', 'resultó en', 'como consecuencia'.")

    print("\n--- 3. **Comparación y Contraste (¿En qué se parecen y en qué son diferentes?)** ⚖️")
    print("   **Propósito:** Analizar las similitudes y diferencias entre dos o más cosas, ideas o personas.")
    print("   **Ejemplo de uso:** Artículos comparando especies de animales, textos que contrastan culturas, análisis de productos.")
    print("   **Pistas:** 'Similar a', 'ambos', 'en contraste con', 'a diferencia de', 'mientras que', 'por otro lado'.")

    print("\n--- 4. **Problema y Solución (¿Qué está mal y cómo lo arreglamos?)** 🛠️")
    print("   **Propósito:** Presentar un problema o desafío y luego proponer una o varias formas de resolverlo.")
    print("   **Ejemplo de uso:** Artículos sobre contaminación, propuestas para mejorar la escuela, campañas sociales.")
    print("   **Pistas:** 'El problema es', 'la cuestión principal', 'una solución es', 'para resolver esto', 'se propone'.")
    
    print("\n¡Entender la estructura nos ayuda a comprender mejor el mensaje del autor!\n")
    input("Presiona ENTER para el juego de estructuras...")

def game_identify_structure_and_purpose():
    """Juego de identificar la estructura textual y su propósito."""
    show_header("Juego 1: ¡El Ingeniero de Textos!")
    print("Lee el texto. Identifica qué **estructura principal** usa y cuál crees que es su **propósito**.\n")
    print("Elige la letra de la estructura: S (Secuencia), CE (Causa/Efecto), CC (Comparación/Contraste), PS (Problema/Solución).\n")

    questions = [
        {"text": "El aumento de la temperatura global está causando el derretimiento de los glaciares. Como resultado, el nivel del mar sube, amenazando las ciudades costeras y alterando los ecosistemas marinos.", 
         "correct_structure": "CE", "structure_name": "Causa y Efecto", "purpose_hint": "Explicar las consecuencias del calentamiento global."},
        
        {"text": "Primero, se diseñó el nuevo edificio con materiales ecológicos. Luego, los trabajadores usaron técnicas de construcción que reducen el desperdicio. Finalmente, el edificio recibió una certificación verde por su eficiencia energética.", 
         "correct_structure": "S", "structure_name": "Secuencia Cronológica", "purpose_hint": "Describir los pasos para construir un edificio ecológico."},
        
        {"text": "Mientras que los perros son animales gregarios que disfrutan la compañía humana y aprenden rápido, los gatos son más independientes y prefieren su propio espacio. Ambos pueden ser grandes mascotas, pero sus necesidades de atención son muy diferentes.", 
         "correct_structure": "CC", "structure_name": "Comparación y Contraste", "purpose_hint": "Mostrar diferencias en el comportamiento y cuidado de perros y gatos."},
        
        {"text": "El problema de la basura en nuestras calles ha aumentado debido a la falta de cestos y la poca conciencia ciudadana. Una posible solución sería implementar un programa de reciclaje más amplio y educar a la comunidad sobre la importancia de no tirar residuos.", 
         "correct_structure": "PS", "structure_name": "Problema y Solución", "purpose_hint": "Proponer maneras de mejorar la limpieza de las calles."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 3 # Limitamos a 3 preguntas

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Texto: '{q['text']}'")
        
        while True:
            user_structure = input("¿Qué estructura usa? (S/CE/CC/PS): ").upper().strip()
            if user_structure in ['S', 'CE', 'CC', 'PS']:
                break
            else:
                print("Opción no válida. Escribe S, CE, CC o PS.")
        
        if user_structure == q['correct_structure']:
            print(f"¡Correcto! 🎉 Es una estructura de **{q['structure_name']}**.")
            print(f"Su propósito principal es: {q['purpose_hint']}")
            score += 1
        else:
            print(f"¡Oops! No es correcto. 🤔 La estructura era **{q['structure_name']}**.")
            print(f"Su propósito principal es: {q['purpose_hint']}")
        time.sleep(8)
    
    print(f"\nJuego terminado. Conseguiste {score} de {num_questions} respuestas correctas. ¡Excelente, ingeniero de textos! 🏗️")
    input("Presiona ENTER para el siguiente paso...")

def show_organizing_own_arguments_concept():
    """Explica cómo organizar argumentos propios y la identificación de sesgo."""
    show_header("Organizando Tus Argumentos y Detectando el Sesgo")
    print("Cuando escribes, tú también eliges cómo organizar tus ideas para que sean claras y convenzan a tu lector.\n")
    print("Para que tus argumentos sean fuertes:")
    print("  ✅ Elige la estructura que mejor se adapte a lo que quieres decir (¿es una historia? ¿un problema? ¿una comparación?).")
    print("  ✅ Usa palabras de transición para guiar al lector de una idea a otra (ej. 'por un lado', 'además', 'sin embargo').\n")
    
    print("--- **Detectando el Sesgo por Organización** ---")
    print("A veces, un autor puede organizar la información de una forma que favorece su punto de vista, ¡y es importante notarlo!")
    print("**Pregúntate:**")
    print("  🤔 ¿Solo me está mostrando un lado de la historia?")
    print("  🤔 ¿Hay información importante que omitió o puso al final donde casi no se ve?")
    print("  🤔 ¿Cómo afecta el orden de las ideas lo que siento o pienso sobre el tema?\n")
    
    print("**Ejemplo:** Un artículo sobre la necesidad de un nuevo parque que solo menciona los beneficios y no los posibles costos o problemas de construcción está mostrando un sesgo al omitir información clave.\n")
    
    print("¡Ser conscientes de cómo se organiza la información nos hace pensadores más críticos!\n")
    input("Presiona ENTER para el desafío de organizar y analizar...")

def game_organize_and_detect_bias():
    """Juego donde el estudiante organiza un argumento y detecta sesgo por organización."""
    show_header("Juego 2: ¡El Arquitecto Persuasivo y Detector de Sesgos!")
    print("Lee el problema. Primero, piensa cómo organizarías un argumento. Luego, detecta un posible sesgo en un argumento dado.\n")
    
    challenges = [
        {"topic": "Escribe un argumento para convencer a tus padres de que te compren una mascota.",
         "hint_organize": "Piensa en el patrón 'Problema/Solución' (problema: no tengo mascota; solución: la mascota). ¿Qué beneficios tendría la mascota para TI y para LA FAMILIA? ¿Cómo resolverías los posibles problemas (cuidado, limpieza)?",
         "biased_argument": "Nuestro equipo de fútbol es el mejor porque nunca hemos perdido un partido en casa. Además, todos los jugadores son excelentes anotadores, ¡y eso es lo único que importa en el fútbol!",
         "bias_explanation": "El argumento se enfoca solo en los partidos en casa y en la capacidad de anotar, ignorando los partidos fuera de casa o la defensa, mostrando un sesgo para hacer que el equipo parezca invencible."},
        
        {"topic": "Escribe un argumento sobre por qué los estudiantes deberían tener menos tarea.",
         "hint_organize": "Podrías usar 'Causa y Efecto' (demasiada tarea causa estrés, poco tiempo libre) o 'Problema/Solución' (problema: mucha tarea; solución: reducirla). ¿Qué argumentos usarías para defender que la tarea extra no siempre es beneficiosa?",
         "biased_argument": "La nueva tienda de comestibles es terrible. Primero, los estacionamientos son pequeños. Además, las filas son siempre largas. Por último, ¡un amigo me dijo que los precios son más altos que en otros lugares!",
         "bias_explanation": "El argumento se enfoca solo en los aspectos negativos (estacionamiento, filas, precios por rumor), sin mencionar posibles beneficios o la experiencia general, mostrando un sesgo negativo."},
    ]
    
    random.shuffle(challenges)
    num_challenges = 1 # Limitamos a 1 desafío para profundidad

    for i in range(num_challenges):
        c = challenges[i]
        print(f"\n--- Desafío {i+1} de {num_challenges} ---")
        print(f"**Parte 1: Organiza tu Argumento**")
        print(f"Tema: '{c['topic']}'")
        print(f"Consejo para organizar tu argumento: {c['hint_organize']}")
        
        user_organization_plan = input("Describe brevemente cómo organizarías tu argumento (ej. 'Primero el problema, luego 3 soluciones'): ").strip()
        print(f"Tu plan de organización: '{user_organization_plan}'")
        print("\n¡Excelente! Pensar en la estructura es el primer paso para un argumento claro.")
        
        input("\nPresiona ENTER para la Parte 2: ¡Detectar el Sesgo!")
        
        print(f"\n**Parte 2: Detecta el Sesgo por Organización**")
        print(f"Lee este argumento: '{c['biased_argument']}'")
        
        user_bias_detection = input("¿Crees que este argumento tiene un sesgo en cómo organiza o presenta la información? ¿Por qué?: ").strip()
        print(f"Tu análisis del sesgo: '{user_bias_detection}'")
        print(f"Análisis esperado: {c['bias_explanation']}")
        
        print("\n¡Has demostrado una habilidad crucial para analizar y construir argumentos de forma inteligente! 🎉")
        time.sleep(10)
    
    print(f"\nDesafío terminado. ¡Eres un maestro en estructurar y analizar argumentos! 🏆")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 9: Estructurando Argumentos y Perspectivas en Textos (6º Grado)")
        print("1. Introducción: ¡Arquitectos del Conocimiento!")
        print("2. Estructuras Textuales: ¡El Esqueleto de las Ideas!")
        print("3. Jugar: ¡El Ingeniero de Textos!")
        print("4. Organizando Tus Argumentos y Detectando el Sesgo")
        print("5. Jugar: ¡El Arquitecto Persuasivo y Detector de Sesgos!")
        print("6. Salir de la Lección")
        print("=" * 90)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_textual_structures_concept()
        elif choice == '3':
            game_identify_structure_and_purpose()
        elif choice == '4':
            show_organizing_own_arguments_concept()
        elif choice == '5':
            game_organize_and_detect_bias()
        elif choice == '6':
            print("¡Adiós, futuros líderes y pensadores! ¡Sigan construyendo ideas sólidas! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
