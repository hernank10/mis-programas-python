import time
import os
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("=" * 120)
    print(f"🌟 {title.upper()} 🌟")
    print("=" * 120)
    print()

def show_introduction():
    """Introduce el concepto de falacias avanzadas y su relevancia en el nivel preuniversitario."""
    show_header("Introducción: Maestría en el Análisis de Argumentos")
    print("¡Felicidades, futuros líderes y pensadores! 🚀")
    print("Han llegado a un nivel donde el pensamiento crítico es una habilidad esencial para el éxito académico y profesional.")
    print("En esta lección final sobre falacias, exploraremos errores lógicos que son particularmente comunes en la **argumentación sofisticada** y que a menudo pasan desapercibidos.\n")
    
    print("Dominar estas falacias les permitirá:")
    print("   ✅ Evaluar con rigor ensayos, discursos y artículos académicos.")
    print("   ✅ Construir argumentos impecables en sus propios trabajos y debates.")
    print("   ✅ Identificar la manipulación retórica en los medios y la política.\n")
    
    input("Presiona ENTER para desglosar estas falacias avanzadas...")

def show_fallacies():
    """Define y ejemplifica falacias lógicas avanzadas para este nivel."""
    show_header("Falacias Lógicas para Pensadores Avanzados")
    
    fallacies = [
        {"name": "Apelación a la Novedad (Argumentum ad Novitatem)", 
         "definition": "Sostener que algo es mejor o verdadero simplemente porque es nuevo, moderno o innovador, sin proporcionar pruebas de su superioridad real.", 
         "example": "Debemos adoptar el nuevo sistema educativo solo porque utiliza la tecnología más reciente; lo nuevo siempre es mejor.",
         "why_fallacy": "La novedad no es una prueba de eficacia o superioridad. Un sistema educativo debe evaluarse por sus resultados y fundamentos pedagógicos, no por su fecha de creación."},
        
        {"name": "Apelación a la Antigüedad/Tradición (Argumentum ad Antiquitatem)", 
         "definition": "Sostener que algo es bueno, correcto o verdadero simplemente porque se ha hecho de esa manera por mucho tiempo o porque es tradicional, sin justificar su validez actual.", 
         "example": "Siempre hemos impartido las clases de esta manera, y no hay razón para cambiarla ahora que tenemos nuevas herramientas; la tradición es sabiduría.",
         "why_fallacy": "La antigüedad o tradición no garantizan validez, eficiencia o relevancia en el presente. Las circunstancias cambian y nuevas soluciones pueden ser superiores."},
        
        {"name": "Alegato Especial (Special Pleading)", 
         "definition": "Aplicar un estándar o una regla a otros mientras se reclama una excepción para uno mismo o para el grupo propio, sin una justificación razonable para dicha excepción.", 
         "example": "Sé que las reglas de la escuela prohíben el uso de teléfonos en el examen, pero mi caso es diferente: necesito el mío para una emergencia familiar muy importante que nadie más tiene.",
         "why_fallacy": "Se pide una excepción personal sin una base objetiva que la justifique más allá del interés propio o una situación no generalizable."},
        
        {"name": "Carga de la Prueba (Shifting the Burden of Proof)", 
         "definition": "Afirmar una proposición y luego exigir al oponente que demuestre que es falsa, en lugar de que el que hizo la afirmación inicial sea quien presente la evidencia de su veracidad.", 
         "example": "Yo afirmo que existen civilizaciones avanzadas en otros planetas, y si no puedes probar que no existen, entonces mi afirmación es válida.",
         "why_fallacy": "Quien hace una afirmación extraordinaria es quien tiene la responsabilidad de proporcionar pruebas. La ausencia de contraprueba no es una prueba."},
        
        {"name": "Falacia de la Falacia (Argumentum ad Logicam)", 
         "definition": "Asumir que si un argumento utilizado para apoyar una conclusión es falaz, entonces la conclusión en sí misma debe ser falsa. La conclusión podría ser verdadera, pero el argumento no es válido.", 
         "example": "El argumento de Juan sobre por qué deberíamos estudiar más para el examen contenía una generalización apresurada. Por lo tanto, no es cierto que debamos estudiar más.",
         "why_fallacy": "La conclusión ('debemos estudiar más') podría ser verdadera y estar respaldada por otras razones válidas, incluso si el argumento particular de Juan fue débil. Atacar el argumento no invalida la conclusión."},
        
        {"name": "Argumento Circular / Petición de Principio (Begging the Question)", 
         "definition": "Un argumento donde la verdad de la conclusión ya se asume en una o más de las premisas, creando un bucle donde el argumento se prueba a sí mismo sin nueva evidencia.", 
         "example": "Fumar marihuana debería ser ilegal porque es perjudicial para la sociedad. Sabemos que es perjudicial porque es ilegal.",
         "why_fallacy": "La ilegalidad se usa para justificar que es perjudicial, y ser perjudicial se usa para justificar la ilegalidad. No hay una razón externa o independiente."},
    ]

    print("Profundicemos en estas falacias más complejas:\n")
    for i, f in enumerate(fallacies):
        print(f"--- {i+1}. {f['name'].upper()} ---")
        print(f"   **Definición:** {f['definition']}")
        print(f"   **Ejemplo:** '{f['example']}'")
        print(f"   **Análisis Crítico (¿Por qué es una falacia?):** {f['why_fallacy']}\n")
        time.sleep(12)
        input("Presiona ENTER para ver la siguiente falacia...")
        print("=" * 80)
    
    print("\n¡Ahora que están armados con este conocimiento, es momento de un verdadero desafío!\n")
    input("Presiona ENTER para ir a los ejercicios...")

def game_identify_and_analyze_fallacy():
    """Juego de identificar la falacia y explicar por qué es falaz."""
    show_header("Juego 1: ¡El Gurú de las Falacias!")
    print("Te presentaré un argumento complejo. Tu tarea es:")
    print("1. Identificar la **falacia lógica** presente.")
    print("2. Explicar brevemente **por qué** es una falacia.\n")

    questions = [
        {"text": "Mi nuevo teléfono con inteligencia artificial es el mejor porque es el más innovador y recién salido al mercado.", 
         "correct_name": "Apelación a la Novedad", 
         "explanation_hint": "La novedad no garantiza superioridad. Podría tener fallos o no adaptarse a tus necesidades."},
        
        {"text": "Las clases universitarias siempre se han dado de forma presencial, por lo tanto, las clases en línea no son una forma válida de educación superior.", 
         "correct_name": "Apelación a la Antigüedad/Tradición", 
         "explanation_hint": "La validez de un método educativo no se basa en su antigüedad, sino en su eficacia y adaptabilidad a nuevas circunstancias."},
        
        {"text": "Yo tengo derecho a copiar en el examen porque tuve una semana muy estresante y, por lo tanto, las reglas normales no aplican para mí.", 
         "correct_name": "Alegato Especial", 
         "explanation_hint": "Las reglas del examen aplican a todos. Tus circunstancias personales, aunque difíciles, no te eximen de ellas sin una justificación formal y justa para todos."},
        
        {"text": "Demuéstrame que los fantasmas no existen, y solo entonces creeré que no hay fantasmas.", 
         "correct_name": "Carga de la Prueba", 
         "explanation_hint": "Quien afirma la existencia de algo (los fantasmas) es quien debe probarlo, no el oponente probar la no existencia."},
        
        {"text": "Su argumento de que necesitamos más fondos para la investigación fue refutado porque usó un ejemplo irrelevante. Por lo tanto, no necesitamos más fondos para la investigación.", 
         "correct_name": "Falacia de la Falacia", 
         "explanation_hint": "Un argumento mal construido no invalida la conclusión. La necesidad de fondos podría ser verdadera por otras razones válidas."},
        
        {"text": "Sabemos que el arte moderno carece de valor estético porque no es bello, y la falta de belleza lo hace inútil como arte.", 
         "correct_name": "Argumento Circular / Petición de Principio", 
         "explanation_hint": "Define 'falta de valor estético' como 'no es bello' y luego usa 'no es bello' para probar que 'carece de valor estético'. No hay una razón externa para la afirmación."},
    ]
    
    random.shuffle(questions)
    score = 0
    num_questions = 3 # Limitamos a 3

    for i in range(num_questions):
        q = questions[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Argumento: '{q['text']}'")
        
        user_identified_fallacy = input("1. ¿Qué falacia lógica contiene este argumento?: ").strip()
        print(f"   (Respuesta esperada: {q['correct_name']})")
        
        user_explanation = input("2. ¿Por qué es una falacia? (Explica brevemente): ").strip()
        print(f"   (Pista: {q['explanation_hint']})")

        # Simplificación de la evaluación para la consola
        if q['correct_name'].lower() in user_identified_fallacy.lower():
            print("¡Identificación CORRECTA! 🎉")
            score += 1
        else:
            print(f"¡Oops! La falacia principal era **{q['correct_name']}**. 🤔")
        
        print("\n--- Evaluación de tu explicación ---")
        print("Recuerda que lo importante es que tu explicación capture la esencia de por qué es una falacia.")
        time.sleep(10)
    
    print(f"\nJuego terminado. ¡Has demostrado ser un experto en la identificación y análisis de falacias! 🕵️‍♂️")
    input("Presiona ENTER para el siguiente juego...")

def game_refute_and_reconstruct():
    """Juego de refutar una falacia y reconstruir un argumento válido."""
    show_header("Juego 2: ¡Refuta y Construye Argumentos Maestros!")
    print("Te daré un argumento falaz. Tu misión es:")
    print("1. Refutar la falacia de forma concisa.")
    print("2. Reconstruir un argumento válido y lógico sobre el mismo tema, si es posible.\n")

    corrections = [
        {"original": "Los nuevos descubrimientos científicos sobre el espacio deben ser verdaderos porque son el resultado de la tecnología más avanzada.", 
         "type": "Apelación a la Novedad", 
         "refutation_hint": "La validez de los descubrimientos científicos se basa en la evidencia empírica y la reproducibilidad, no en la novedad de la tecnología utilizada.",
         "reconstruction_hint": "Los descubrimientos científicos deben ser evaluados por la solidez de su metodología, la consistencia de los datos y la revisión por pares, independientemente de la antigüedad o novedad de la tecnología que los facilita."},
        
        {"original": "No puedo ser culpable de plagio, porque mi profesor nunca me ha demostrado que yo haya plagiado.", 
         "type": "Carga de la Prueba", 
         "refutation_hint": "La carga de la prueba recae en la persona que está siendo acusada de plagio para demostrar su inocencia o la originalidad de su trabajo.",
         "reconstruction_hint": "Para demostrar que no hay plagio, se requiere presentar las fuentes originales, citar correctamente y mostrar el proceso de elaboración del trabajo, no esperar que el profesor demuestre el plagio."},
        
        {"original": "Los medicamentos genéricos son de baja calidad porque mi abuela siempre ha dicho que solo los medicamentos de marca son efectivos.", 
         "type": "Apelación a la Antigüedad/Tradición", 
         "refutation_hint": "La eficacia de los medicamentos genéricos está respaldada por estudios científicos y regulaciones, no por opiniones personales o tradiciones.",
         "reconstruction_hint": "La calidad y eficacia de los medicamentos genéricos están garantizadas por pruebas de bioequivalencia y la regulación de las autoridades sanitarias, asegurando que funcionan igual que los de marca."},
        
        {"original": "Decir que los videojuegos causan violencia es absurdo. Un estudio de mi primo, que es informático, dijo que no hay conexión, así que no la hay.", 
         "type": "Ad Verecundiam (falsa autoridad)", 
         "refutation_hint": "La opinión de un informático, aunque válido en su campo, no es una autoridad experta en psicología, sociología o neurociencia para determinar la relación entre videojuegos y violencia.",
         "reconstruction_hint": "Para determinar si los videojuegos causan violencia, es necesario consultar investigaciones realizadas por psicólogos, sociólogos y neurocientíficos, basándose en estudios empíricos y revisión por pares."},
    ]
    
    random.shuffle(corrections)
    num_questions = 2 # Limitamos a 2

    for i in range(num_questions):
        c = corrections[i]
        print(f"\n--- Pregunta {i+1} de {num_questions} ---")
        print(f"Argumento falaz: '{c['original']}'")
        print(f"Falacia identificada (para tu referencia): **{c['type']}**")
        
        user_refutation = input("1. Refuta la falacia en una frase concisa: ").strip()
        print(f"   (Sugerencia de refutación: {c['refutation_hint']})")
        
        input("\nPresiona ENTER para reconstruir el argumento...")
        
        user_reconstruction = input("2. Ahora, reconstruye un argumento lógico y válido sobre el mismo tema: ").strip()
        print(f"   (Sugerencia de reconstrucción: {c['reconstruction_hint']})")
        
        print("\n--- ¡Análisis Completo! ---")
        print("Tu refutación y reconstrucción demuestran un pensamiento crítico de alto nivel. ¡Excelente trabajo! 🎉")
        time.sleep(12)
    
    print(f"\nJuego terminado. ¡Has dominado la refutación y la construcción de argumentos maestros!")
    input("Presiona ENTER para volver al menú principal...")


def create_own_complex_argument():
    """Permite al usuario crear un argumento complejo con una falacia y luego refutarlo y reconstruirlo."""
    show_header("✍️ ¡Desafío Final: Crea, Desmantela y Construye! ✍️")
    print("Esta es tu prueba final. Crea un argumento complejo que contenga una de las falacias avanzadas.")
    print("Luego, desmantélala y reconstruye un argumento sólido.\n")

    fallacy_types = ["Apelación a la Novedad", "Apelación a la Antigüedad/Tradición", "Alegato Especial", "Carga de la Prueba", "Falacia de la Falacia", "Argumento Circular"]
    
    print("Elige una de estas falacias para tu argumento:")
    for f in fallacy_types:
        print(f"- {f}")
    
    while True:
        chosen_fallacy = input("Escribe el nombre de la falacia que usarás: ").strip()
        if chosen_fallacy in fallacy_types:
            break
        else:
            print("Por favor, elige una falacia de la lista.")

    while True:
        original_argument = input(f"\n1. Escribe tu argumento complejo que contenga la falacia de **{chosen_fallacy}**: ").strip()
        if original_argument:
            break
        else:
            print("Por favor, escribe un argumento.")
    
    print(f"\nTu argumento falaz: '{original_argument}'")
    print(f"Falacia que contiene (según tu elección): **{chosen_fallacy}**")

    user_refutation = input("\n2. Ahora, refuta concisamente la falacia en tu propio argumento: ").strip()
    
    user_reconstruction = input("3. Finalmente, reconstruye un argumento lógico y válido sobre el mismo tema: ").strip()

    print("\n--- ¡TU PROYECTO FINAL EN PENSAMIENTO CRÍTICO! ---")
    print(f"Argumento original falaz ({chosen_fallacy}): '{original_argument}' 🚫")
    print(f"Tu refutación: '{user_refutation}'")
    print(f"Tu argumento lógico reconstruido: '{user_reconstruction}' ✅")
    print("\n¡Qué logro! Has demostrado un nivel excepcional de pensamiento crítico y argumentación. ¡Estás listo para cualquier desafío intelectual! 🏆")
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 8: Falacias Lógicas y Argumentación Sofisticada (12º Grado/Preuniversitario)")
        print("1. Introducción: Maestría en el Análisis de Argumentos")
        print("2. Conocer las Falacias Lógicas para Pensadores Avanzados")
        print("3. Jugar: ¡El Gurú de las Falacias!")
        print("4. Jugar: ¡Refuta y Construye Argumentos Maestros!")
        print("5. ✍️ ¡Desafío Final: Crea, Desmantela y Construye! ✍️")
        print("6. Salir de la Lección")
        print("=" * 120)

        choice = input("Elige un número (1-6): ")

        if choice == '1':
            show_introduction()
        elif choice == '2':
            show_fallacies()
        elif choice == '3':
            game_identify_and_analyze_fallacy()
        elif choice == '4':
            game_refute_and_reconstruct()
        elif choice == '5':
            create_own_complex_argument()
        elif choice == '6':
            print("¡Adiós, campeón del pensamiento crítico! El mundo necesita mentes como la tuya. Sigue cuestionando y argumentando con verdad y lógica. ¡Te deseamos mucho éxito en tus estudios universitarios y en la vida! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
