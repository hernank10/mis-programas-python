import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    clear_screen()
    print("=" * 100)
    print(f"🏛️ {title.upper()} 🏛️")
    print("=" * 100)
    print()

def show_introduction_l8():
    show_header("Introducción: ¡Arquitectos del Discurso!")
    print("¡Hola, jóvenes pensadores y futuros oradores! 📣")
    print("Hemos aprendido a organizar ideas, pero hoy daremos un paso más: ¡vamos a entender CÓMO la forma en que organizamos las ideas puede cambiar lo que la gente piensa o siente!")
    print("Seremos detectives del 'porqué' los autores eligen una estructura y, más importante, ¡aprenderemos a usar esa magia en nuestros propios escritos y discursos!\n")
    
    print("En esta lección, ustedes serán capaces de:")
    print("   ✅ Analizar cómo la organización de un texto persuade o informa de manera más efectiva.")
    print("   ✅ Diseñar sus propios textos para lograr un impacto específico en su audiencia.")
    print("   ✅ Conectar sus ideas de forma impecable en escritos largos.\n")
    
    print("¡Prepárense para construir argumentos inquebrantables y analizar la maestría de otros!\n")
    input("Presiona ENTER para desentrañar los secretos de la estructura retórica...")

def show_rhetorical_function_concept_l8():
    show_header("Función Retórica de la Organización: ¿Por Qué en Ese Orden?")
    print("Cada decisión que toma un autor al organizar su texto tiene un propósito, ¡especialmente en la persuasión!\n")
    print("Piénsenlo así:")
    print("  ➡️ **¿Punto más fuerte al principio (deductivo) o al final (inductivo)?**")
    print("    * **Principio (deductivo):** Si tu audiencia ya está de acuerdo o necesitas captar su atención de inmediato con tu idea principal. (Ej. 'Tienes que venir, hay pastel GRATIS. Y además, hay música y amigos.')")
    print("    * **Final (inductivo):** Si necesitas construir la confianza, presentar mucha evidencia o quieres un impacto final memorable. (Ej. 'Hay música, hay amigos, hay buen ambiente... ¡y, por cierto, hay pastel GRATIS!')\n")
    
    print("  ➡️ **Secuencia Cronológica o por Temas?**")
    print("    * **Cronológica:** Para narrar historias o procesos, mostrando evolución. (Ej. Biografías)")
    print("    * **Por Temas:** Para analizar diferentes aspectos de un asunto, permitiendo profundidad en cada punto. (Ej. Investigación sobre diferentes aspectos del cambio climático: el deshielo, la acidificación del océano, etc.)\n")
    
    print("  ➡️ **Problema/Solución vs. Causa/Efecto:**")
    print("    * **Problema/Solución:** Si tu objetivo es proponer una acción, presentando el problema y luego tu propuesta. (Ej. Propuesta para resolver la basura en el colegio)")
    print("    * **Causa/Efecto:** Si tu objetivo es explicar las razones y consecuencias de un fenómeno, sin necesariamente pedir una acción específica. (Ej. Explicación de las causas de la erosión del suelo y sus efectos).\n")
    
    print("La clave es que la **elección de la estructura no es arbitraria; es una herramienta retórica**.\n")
    input("Presiona ENTER para analizar la organización en textos reales...")

def game_analyze_organizational_function_l8():
    show_header("Juego 1: ¡El Crítico Textual!")
    print("Lee el extracto. Identifica la estructura principal y piensa en el posible propósito del autor al usarla.\n")
    print("Elige la letra de la estructura principal: S (Secuencia), CE (Causa/Efecto), CC (Comparación/Contraste), PS (Problema/Solución).\n")

    questions = [
        {"text": "El problema de la brecha digital, que excluye a muchos estudiantes del acceso a la educación en línea, requiere una acción urgente. Una solución multifacética sería la inversión pública en infraestructura de internet en zonas rurales y programas de subsidio para dispositivos electrónicos.", 
         "correct_structure": "PS", "structure_name": "Problema/Solución", "purpose_analysis": "El autor usa Problema/Solución para primero establecer la gravedad de una situación y luego ofrecer una solución clara y viable, buscando persuadir a la acción o la inversión."},
        
        {"text": "A diferencia de la narrativa tradicional, que sigue una línea temporal lineal, la ficción experimental a menudo fragmenta el tiempo, saltando hacia adelante y hacia atrás. Esto busca desorientar al lector y forzarlo a reconstruir el significado, desafiando sus expectativas.", 
         "correct_structure": "CC", "structure_name": "Comparación/Contraste", "purpose_analysis": "El autor usa Comparación/Contraste para resaltar las diferencias entre dos formas de narrativa y explicar cómo esas diferencias afectan la experiencia del lector, informando sobre técnicas literarias."},
        
        {"text": "El descubrimiento de la penicilina por Alexander Fleming en 1928 marcó un antes y un después en la medicina. Posteriormente, su producción masiva durante la Segunda Guerra Mundial salvó incontables vidas. Hoy, enfrentamos el reto de la resistencia a los antibióticos, un efecto de su uso excesivo a lo largo de décadas.", 
         "correct_structure": "S", "structure_name": "Secuencia Cronológica", "purpose_analysis": "Aunque tiene un elemento de Causa/Efecto al final, la estructura predominante es Secuencia Cronológica para mostrar la evolución histórica de un hito científico y sus consecuencias a lo largo del tiempo."},
    ]
    
    random.shuffle(questions)
    num_questions = 2 

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"**Extracto:** '{q['text']}'")
        
        while True:
            user_structure = input("Estructura principal (S/CE/CC/PS): ").upper().strip()
            if user_structure in ['S', 'CE', 'CC', 'PS']:
                break
            else:
                print("Opción no válida. Escribe S, CE, CC o PS.")
        
        print("\nAhora, reflexiona: ¿Cuál crees que es el propósito del autor al usar ESTA estructura?")
        user_purpose_reflection = input("Tu análisis del propósito (breve): ").strip()
        
        if user_structure == q['correct_structure']:
            print(f"\n¡Correcto en la estructura! 🎉 Es **{q['structure_name']}**.")
        else:
            print(f"\n¡Uhm, no en la estructura! 🤔 Era **{q['structure_name']}**.")
        
        print(f"**Análisis del propósito:** {q['purpose_analysis']}")
        print(f"Tu análisis: '{user_purpose_reflection}'")
        print("Compara tu reflexión con el análisis dado. ¡Ambos pueden ser válidos si están bien argumentados!\n")
        time.sleep(10)
    
    print(f"\nJuego terminado. ¡Estás desarrollando una visión crítica de la estructura textual! 🧐")
    input("Presiona ENTER para el siguiente paso...")

def show_organizing_for_purpose_concept_l8():
    show_header("Organizando para Propósitos Específicos: ¡Sé el Estratega!")
    print("Así como los autores que analizamos, tú también debes decidir la mejor organización para tus propios textos, ¡pensando en tu audiencia y en lo que quieres lograr!\n")
    
    print("--- **Planificando tu Estrategia de Organización:** ---")
    print("  1. **Define tu Propósito:** ¿Quieres informar, persuadir, entretener, explicar un proceso, resolver un problema?")
    print("  2. **Conoce a tu Audiencia:** ¿Qué saben ya? ¿Están de acuerdo contigo? ¿Qué necesitan escuchar primero?")
    print("  3. **Elige la Estructura Dominante:** Secuencia, Causa/Efecto, Problema/Solución, Comparación/Contraste... ¿Cuál encaja mejor?")
    print("  4. **Usa Transiciones Avanzadas:** Para textos más largos, necesitas puentes claros entre párrafos y secciones. No solo 'luego', sino 'Además', 'Por otro lado', 'En consecuencia', 'No obstante'.")
    print("  5. **Cohesión y Coherencia:** Asegúrate de que todas las partes de tu texto fluyan lógicamente y se conecten con tu tesis principal.\n")
    
    print("**Ejemplo:** Si tu propósito es persuadir a la comunidad para que separe la basura:")
    print("  * Podrías empezar con el **Problema** (acumulación de basura, impacto ambiental) para generar preocupación.")
    print("  * Luego, pasar a la **Solución** (beneficios del reciclaje, cómo implementarlo).")
    print("  * Finalmente, terminar con una **Conclusión fuerte** que apele a la acción y a la responsabilidad comunitaria.\n")
    
    print("¡La organización no es solo orden, es estrategia!\n")
    input("Presiona ENTER para el desafío de planificación y cohesión...")

def game_organize_for_purpose_and_cohesion_l8():
    show_header("Juego 2: ¡El Maestro Constructor de Textos!")
    print("Te daré un escenario. Primero, planifica la mejor estructura. Luego, piensa en transiciones para conectar ideas.\n")
    
    challenges = [
        {"scenario": "Debes escribir un artículo para el periódico escolar explicando por qué la nueva norma de no usar celulares en clase es beneficiosa para los estudiantes, a pesar de la resistencia inicial.",
         "purpose": "Persuadir a los estudiantes sobre los beneficios de la norma.",
         "suggested_structure": "Problema/Solución (resistencia es el 'problema', beneficios son la 'solución') o Causa/Efecto (norma como causa, beneficios como efectos).",
         "transition_example": "Inicialmente, muchos se sintieron molestos. **Sin embargo**, con el tiempo, hemos observado mejoras significativas. **Por ejemplo**, la atención en clase ha aumentado. **Además**, el tiempo libre se aprovecha mejor en interacciones personales."
        },
        
        {"scenario": "Estás preparando una presentación oral para una clase de ciencias sobre los diferentes tipos de energía renovable (solar, eólica, hidráulica) y sus ventajas y desventajas.",
         "purpose": "Informar y comparar de manera objetiva.",
         "suggested_structure": "Comparación/Contraste (entre los tipos de energía) y luego Descripción para cada una. Podría también tener un elemento de Problema/Solución (problema de energía, solución con renovables).",
         "transition_example": "Comenzaremos con la energía solar. **En contraste**, la energía eólica presenta características distintas. **Además**, la energía hidráulica ofrece sus propias particularidades. **Finalmente**, analizaremos las implicaciones de cada una."
        },
    ]
    
    random.shuffle(challenges)
    num_challenges = 1 

    for i in range(num_challenges):
        c = challenges[i]
        print(f"\n--- Desafío {i+1} de {num_challenges} ---")
        print(f"**Escenario:** '{c['scenario']}'")
        print(f"**Tu Propósito Principal:** '{c['purpose']}'")
        
        print("\n**Parte 1: Planifica tu Estructura (Piensa en el patrón y por qué lo eliges)**")
        user_structure_plan = input("Describe cómo organizarías tu texto/discurso y por qué esa estructura (ej. 'Empezaría con el problema para impactar y luego dar soluciones'): ").strip()
        print(f"Tu plan: '{user_structure_plan}'")
        print(f"Sugerencia de estructura: {c['suggested_structure']}")
        
        input("\nPresiona ENTER para la Parte 2: ¡Transiciones y Cohesión!")
        
        print(f"\n**Parte 2: Usa Transiciones para la Cohesión**")
        print("Imagina que ya tienes tus ideas principales. ¿Qué frases de transición usarías para conectar fluidamente los párrafos o secciones?")
        print(f"Piensa en la fluidez de un texto extenso. El propósito es '{c['purpose']}'.")
        
        user_transitions = input("Escribe 2-3 frases de transición que usarías: ").strip()
        print(f"\nTus transiciones: '{user_transitions}'")
        print(f"Ejemplo de transiciones: '{c['transition_example']}'")
        
        print("\n¡Has demostrado una maestría en la planificación estratégica de textos y la cohesión! 🏆")
        time.sleep(12)
    
    print(f"\nDesafío terminado. ¡Sigue aplicando la organización estratégica en todos tus trabajos! ✍️")
    input("Presiona ENTER para volver al menú principal...")


# --- NUEVOS EJERCICIOS PARA LECCIÓN 9 (8.º Grado) ---
def exercise_design_and_write_argument_l8():
    show_header("Ejercicio: ¡Diseña y Escribe tu Argumento Estratégico!")
    print("¡Ahora eres el estratega y el autor! Vamos a poner en práctica todo lo aprendido.")
    print("Elige uno de los siguientes escenarios para escribir una sección corta de un texto:")
    print("  1. Un argumento para persuadir a tus compañeros de clase sobre la importancia de la lectura diaria.")
    print("  2. Una explicación clara de las causas y efectos de la contaminación del aire en tu ciudad.")
    print("  3. Una comparación entre dos métodos de estudio (ej. individual vs. grupal) para ayudar a otros a elegir.")

    while True:
        scenario_choice = input("Elige el número del escenario (1, 2 o 3): ").strip()
        if scenario_choice in ['1', '2', '3']:
            break
        else:
            print("Opción inválida. Por favor, escribe 1, 2 o 3.")

    scenario_details = {
        '1': {"purpose": "Persuadir", "suggested_pattern": "Problema/Solución (falta de lectura / beneficios de leer) o Argumento Deductivo (tesis al inicio, luego evidencias).", "example_start": "Para convencerlos de la lectura..."},
        '2': {"purpose": "Informar/Explicar", "suggested_pattern": "Causa/Efecto (causas de la contaminación / efectos).", "example_start": "Para explicar la contaminación..."},
        '3': {"purpose": "Informar/Comparar", "suggested_pattern": "Comparación/Contraste (similitudes y diferencias).", "example_start": "Para comparar los métodos de estudio..."},
    }
    chosen_scenario = scenario_details[scenario_choice]

    print(f"\n¡Excelente elección! Tu propósito es **{chosen_scenario['purpose']}**.")
    print(f"Una estructura sugerida para este propósito es: **{chosen_scenario['suggested_pattern']}**.")
    
    print(f"\n**Parte 1: Planificación (no la escribes, solo la piensas):**")
    print(f"Piensa: ¿Cómo organizarías las ideas principales de tu texto para lograr tu propósito? ¿Qué iría primero, qué después y por qué? ¿Qué tipo de evidencia usarías?")
    input("Cuando estés listo para escribir una sección, presiona ENTER...")

    print(f"\n**Parte 2: Escribe una Sección Clave (1-2 párrafos, 5-8 oraciones en total):**")
    print(f"Ahora, escribe una parte importante de tu argumento o explicación. ¡Intenta aplicar tu plan de organización!")
    print(f"({chosen_scenario['example_start']} usa un ejemplo, o empieza con tu propia idea principal/problema.)\n")
    
    user_text_section = ""
    print("Escribe aquí tu sección (presiona ENTER dos veces para terminar):")
    while True:
        line = input()
        if not line:
            break
        user_text_section += line + "\n"
    user_text_section = user_text_section.strip()

    print("\n--- ¡Tu Sección Escrita! ---")
    print(user_text_section)
    
    print("\n--- Reflexión Guiada ---")
    print("Ahora, ¡analiza tu propia obra maestra!")
    print(f"Tu propósito era: **{chosen_scenario['purpose']}**.")
    print(f"La estructura sugerida era: **{chosen_scenario['suggested_pattern']}**.\n")
    
    print("1. **Intención Retórica:** ¿Por qué elegiste poner ciertas ideas al principio o al final de tu sección? ¿Qué efecto querías lograr en el lector/oyente?")
    user_reflection_intent = input("> Tu reflexión: ").strip()

    print("\n2. **Conexión de Ideas:** ¿Cómo conectaste las oraciones y los párrafos (si escribiste más de uno) para que fluyeran bien? (Piensa en tus transiciones, si las usaste).")
    user_reflection_cohesion = input("> Tu reflexión: ").strip()

    print("\n3. **Claridad del Argumento:** ¿Crees que tu organización hace que tu punto sea muy claro y fácil de seguir para tu audiencia?")
    user_reflection_clarity = input("> Tu reflexión: ").strip()

    print("\n¡Excelente! Reflexionar sobre estas decisiones te convierte en un escritor y pensador mucho más estratégico. ¡Sigue practicando esta auto-crítica constructiva!\n")
    input("Presiona ENTER para continuar...")


def show_main_menu_l8():
    while True:
        show_header("Lección 9: La Maestría en la Estructura Argumentativa y el Análisis Retórico (8º Grado)")
        print("1. Introducción: ¡Arquitectos del Discurso!")
        print("2. Función Retórica de la Organización: ¿Por Qué en Ese Orden?")
        print("3. Jugar: ¡El Crítico Textual!")
        print("4. Organizando para Propósitos Específicos: ¡Sé el Estratega!")
        print("5. Jugar: ¡El Maestro Constructor de Textos!")
        print("6. **NUEVO:** Ejercicio: ¡Diseña y Escribe tu Argumento Estratégico!")
        print("7. Salir de la Lección")
        print("=" * 100)

        choice = input("Elige un número (1-7): ")

        if choice == '1':
            show_introduction_l8()
        elif choice == '2':
            show_rhetorical_function_concept_l8()
        elif choice == '3':
            game_analyze_organizational_function_l8()
        elif choice == '4':
            show_organizing_for_purpose_concept_l8()
        elif choice == '5':
            game_organize_for_purpose_and_cohesion_l8()
        elif choice == '6':
            exercise_design_and_write_argument_l8()
        elif choice == '7':
            print("¡Adiós, futuros maestros de la comunicación y el análisis crítico! ¡Su mente organizada es su mejor herramienta! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 7.")
            time.sleep(1)

# Comentado para no ejecutar automáticamente
# if __name__ == "__main__":
#     show_main_menu_l8()
