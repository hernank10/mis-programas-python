import random
import os
import time

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("-" * 60)
    print(f"🧐 {title.upper()} 🧐")
    print("-" * 60)
    print()

def show_theory():
    """Muestra la sección de teoría sobre hechos, opiniones y evidencia."""
    show_header("Teoría: Hechos, Opiniones y Evidencia")
    print("¡Hola! En la argumentación, es fundamental distinguir lo que es verdad de lo que es una creencia.")
    print("Hoy aprenderemos sobre los **hechos**, las **opiniones** y la **evidencia**.\n")
    
    print("⭐ 1. HECHO:")
    print("   Es una afirmación que puede ser **probada o verificada** como verdadera o falsa.")
    print("   Son datos, sucesos o realidades objetivas. No dependen de lo que alguien piense.")
    print("   Ejemplo: 'El agua hierve a 100 grados Celsius al nivel del mar.' (Se puede probar)\n")
    
    print("⭐ 2. OPINIÓN:")
    print("   Es una afirmación que expresa un **juicio personal**, un sentimiento o una creencia.")
    print("   No puede ser probada o desmentida objetivamente. Depende de la perspectiva de una persona.")
    print("   Ejemplo: 'El helado de chocolate es el más delicioso.' (Es un gusto personal)\n")
    
    print("⭐ 3. EVIDENCIA:")
    print("   Son los **datos, ejemplos, estadísticas, citas de expertos o resultados de estudios** que se usan para APOYAR una tesis o una razón.")
    print("   La evidencia convierte una opinión en un argumento más sólido, o demuestra la veracidad de un hecho.")
    print("   Ejemplo (evidencia para 'Los estudiantes con menos horas de sueño rinden menos'):")
    print("   'Un estudio de la Universidad X mostró que los alumnos que duermen menos de 7 horas obtienen un 15% menos de calificaciones en promedio.'\n")
    
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de hechos, opiniones y cómo la evidencia apoya."""
    show_header("Ejemplos: Identificando y Usando Evidencia")
    
    examples = [
        {"type": "OPINIÓN", "statement": "El rojo es el mejor color.", "explanation": "Es un gusto personal, no se puede probar."},
        {"type": "HECHO", "statement": "Bogotá es la capital de Colombia.", "explanation": "Se puede verificar en un mapa o enciclopedia."},
        {"type": "OPINIÓN", "statement": "Los perros pequeños son más traviesos.", "explanation": "Es una percepción, no una verdad universal."},
        {"type": "HECHO", "statement": "La Tierra gira alrededor del Sol.", "explanation": "Confirmado por la ciencia y la observación."},
        {"type": "AFIRMACIÓN + EVIDENCIA", 
         "statement": "El cambio climático es una realidad y afecta al planeta.", 
         "evidence": "Los datos de la NASA muestran un aumento constante de la temperatura global en las últimas décadas y el derretimiento de los glaciares.",
         "explanation": "La evidencia convierte la afirmación en un argumento basado en hechos."}
    ]

    print("Observa la diferencia y cómo se usa la evidencia:\n")
    print(f"{'TIPO':<15} {'AFIRMACIÓN / EVIDENCIA':<60}")
    print("-" * 75)
    for ex in examples:
        print(f"{ex['type']:<15} {ex['statement']:<60}")
        print(f"  Explicación: {ex['explanation']}")
        if "evidence" in ex:
            print(f"  Evidencia: {ex['evidence']}")
        print("-" * 75)
        time.sleep(2.5) # Pausa para que el estudiante procese

    print("\n¡Las buenas evidencias fortalecen nuestros argumentos!\n")
    input("Presiona ENTER para ir a los ejercicios...")

def run_exercise(question, options, correct_answer_index, feedback_correct, feedback_incorrect):
    """Ejecuta un solo ejercicio de opción múltiple."""
    print("\n" + question)
    for i, option in enumerate(options):
        print(f"  {i+1}. {option}")
    
    while True:
        try:
            choice = int(input("Elige el número de tu respuesta: "))
            if 1 <= choice <= len(options):
                if choice - 1 == correct_answer_index:
                    print(f"¡Correcto! ✅ {feedback_correct}")
                    return True
                else:
                    print(f"¡Incorrecto! ❌ {feedback_incorrect}")
                    return False
            else:
                print("Número no válido. Elige un número de la lista.")
        except ValueError:
            print("Entrada inválida. Por favor, escribe un número.")
    print("-" * 30)
    time.sleep(2) # Pausa para que el usuario lea el feedback

def start_exercises():
    """Inicia la sección de ejercicios de identificación y argumentación."""
    show_header("¡A Practicar! Hechos, Opiniones y Evidencia")
    score = 0
    total_questions = 0

    exercises = [
        # Identificación de Hechos/Opiniones (8 ejercicios)
        {
            "type": "identification",
            "q": "La oración 'El Sol es una estrella' es un...",
            "opt": ["Hecho", "Opinión"],
            "ans": 0, # Index 0 = "Hecho"
            "fb_c": "¡Correcto! Se puede probar científicamente.",
            "fb_i": "No. ¿Se puede verificar objetivamente?"
        },
        {
            "type": "identification",
            "q": "La oración 'Los lunes son el peor día de la semana' es una...",
            "opt": ["Hecho", "Opinión"],
            "ans": 1, # Index 1 = "Opinión"
            "fb_c": "¡Así es! Es un sentimiento personal.",
            "fb_i": "No. ¿Es algo que se pueda probar para todos?"
        },
        {
            "type": "identification",
            "q": "La oración 'El agua es esencial para la vida' es un...",
            "opt": ["Hecho", "Opinión"],
            "ans": 0, # Index 0 = "Hecho"
            "fb_c": "¡Correcto! Es una verdad científica.",
            "fb_i": "Piénsalo bien. ¿Puedes vivir sin agua?"
        },
        {
            "type": "identification",
            "q": "La oración 'La lectura es aburrida' es una...",
            "opt": ["Hecho", "Opinión"],
            "ans": 1, # Index 1 = "Opinión"
            "fb_c": "¡Excelente! Depende del gusto de cada persona.",
            "fb_i": "Intenta de nuevo. ¿Todos piensan igual sobre la lectura?"
        },
        {
            "type": "identification",
            "q": "La oración 'Hay 7 continentes en la Tierra' es un...",
            "opt": ["Hecho", "Opinión"],
            "ans": 0, # Index 0 = "Hecho"
            "fb_c": "¡Genial! Es un dato geográfico verificable.",
            "fb_i": "No. Busca en un atlas, ¿es cierto o no?"
        },
        {
            "type": "identification",
            "q": "La oración 'El chocolate es mejor que la vainilla' es una...",
            "opt": ["Hecho", "Opinión"],
            "ans": 1, # Index 1 = "Opinión"
            "fb_c": "¡Correcto! Es una preferencia personal.",
            "fb_i": "¿Todos tienen el mismo sabor favorito?"
        },
        {
            "type": "identification",
            "q": "La oración 'Las plantas realizan fotosíntesis' es un...",
            "opt": ["Hecho", "Opinión"],
            "ans": 0, # Index 0 = "Hecho"
            "fb_c": "¡Así es! Es un proceso biológico demostrado.",
            "fb_i": "No. ¿Es algo que aprendes en ciencias?"
        },
        {
            "type": "identification",
            "q": "La oración 'Los perros son más lindos que los gatos' es una...",
            "opt": ["Hecho", "Opinión"],
            "ans": 1, # Index 1 = "Opinión"
            "fb_c": "¡Excelente! La belleza es subjetiva.",
            "fb_i": "No. ¿Es algo que se pueda medir o probar?"
        },

        # Añadir Evidencia a una afirmación (12 ejercicios)
        # Aquí pediremos al estudiante que escriba su propia evidencia
        # y luego se mostrará una respuesta modelo para comparación.
    ]

    random.shuffle(exercises) 

    good_answers_count = 0
    
    # Primero los ejercicios de identificación
    print("\n--- Parte 1: Identifica Hechos u Opiniones ---")
    for i, ex in enumerate([e for e in exercises if e["type"] == "identification"]):
        total_questions += 1
        print(f"\n--- Pregunta {i+1} de 8 ---")
        if run_exercise(ex["q"], ex["opt"], ex["ans"], ex["fb_c"], ex["fb_i"]):
            good_answers_count += 1
    
    print("\n" * 2)
    print("-" * 60)
    print(f"Parte 1 Terminada. Puntuación: {good_answers_count} de 8.")
    print("-" * 60)
    input("Presiona ENTER para la Parte 2: Añadir Evidencia...")

    # Luego los ejercicios de añadir evidencia
    evidence_exercises = [
        {"statement": "El ejercicio físico mejora la salud.",
         "evidence_model": "Un estudio de la OMS (Organización Mundial de la Salud) indica que 30 minutos de actividad moderada al día reducen el riesgo de enfermedades crónicas en un 20%."},
        {"statement": "La lectura fomenta el desarrollo cognitivo en los niños.",
         "evidence_model": "Investigaciones de la Universidad de Oxford han demostrado que los niños que leen regularmente tienen un vocabulario más amplio y una mejor capacidad de comprensión."},
        {"statement": "El consumo excesivo de azúcar es perjudicial.",
         "evidence_model": "La Asociación Americana del Corazón advierte que una dieta alta en azúcares añadidos aumenta el riesgo de obesidad, diabetes tipo 2 y enfermedades cardíacas."},
        {"statement": "Aprender un nuevo idioma estimula el cerebro.",
         "evidence_model": "Neurocientíficos del MIT han encontrado que las personas bilingües muestran una mayor densidad de materia gris en ciertas áreas del cerebro, lo que indica un mayor desarrollo cognitivo."},
        {"statement": "El uso de pantallas antes de dormir afecta la calidad del sueño.",
         "evidence_model": "Estudios publicados en la revista 'Nature and Science of Sleep' revelan que la luz azul emitida por dispositivos electrónicos suprime la producción de melatonina, hormona reguladora del sueño."},
        {"statement": "La biodiversidad es crucial para la estabilidad de los ecosistemas.",
         "evidence_model": "Científicos del Programa de las Naciones Unidas para el Medio Ambiente han demostrado que los ecosistemas con mayor diversidad de especies son más resistentes a las perturbaciones y enfermedades."},
        {"statement": "El reciclaje reduce la contaminación ambiental.",
         "evidence_model": "Datos de la EPA (Agencia de Protección Ambiental de EE. UU.) muestran que el reciclaje de materiales como papel y plástico disminuye las emisiones de gases de efecto invernadero y el uso de recursos naturales."},
        {"statement": "El voluntariado mejora el bienestar emocional de las personas.",
         "evidence_model": "Investigaciones psicológicas de la Universidad de Harvard sugieren que las personas que realizan voluntariado experimentan niveles más bajos de estrés y una mayor satisfacción con la vida."},
        {"statement": "La educación de calidad es clave para el desarrollo económico de un país.",
         "evidence_model": "El Banco Mundial ha publicado informes que correlacionan directamente el nivel educativo de la población con el crecimiento del Producto Interno Bruto (PIB) y la reducción de la pobreza."},
        {"statement": "La inteligencia artificial está transformando la industria laboral.",
         "evidence_model": "Un informe de McKinsey & Company estima que la automatización y la IA podrían desplazar millones de empleos, pero también crear nuevas oportunidades en sectores emergentes."},
        {"statement": "El uso de transporte público reduce la huella de carbono.",
         "evidence_model": "Según la Agencia Europea del Medio Ambiente, optar por el transporte público en lugar del coche privado puede reducir las emisiones de CO2 en un 45% por pasajero-kilómetro."},
        {"statement": "La meditación puede disminuir los niveles de estrés.",
         "evidence_model": "Estudios científicos en la revista 'JAMA Internal Medicine' han demostrado que la práctica regular de la meditación de atención plena reduce significativamente los síntomas de ansiedad y depresión."}
    ]
    random.shuffle(evidence_exercises)

    good_evidence_count = 0
    print("\n--- Parte 2: Añade Evidencia a estas afirmaciones ---")
    print("Para cada afirmación, escribe una frase de evidencia que la respalde.")
    print("Piensa en datos, estudios, expertos, ejemplos concretos. ¡Sé creativo y lógico!\n")

    for i, ex in enumerate(evidence_exercises):
        total_questions += 1 # Contamos estas también para el total general
        print(f"\n--- Ejercicio {i+1} de 12 ---")
        print(f"Afirmación: '{ex['statement']}'")
        user_evidence = input("Tu evidencia: ").strip()

        print("\n--- Evidencia Modelo ---")
        print(f"Una posible evidencia sería: '{ex['evidence_model']}'")
        
        while True:
            evaluation = input("\n¿Consideras que tu evidencia es fuerte y lógica? (s/n): ").lower().strip()
            if evaluation == 's':
                good_evidence_count += 1
                print("¡Excelente! Estás aprendiendo a argumentar con solidez.")
                break
            elif evaluation == 'n':
                print("Está bien, sigue practicando. Pensar en fuentes y datos te ayudará.")
                break
            else:
                print("Respuesta no válida. Por favor, escribe 's' para sí o 'n' para no.")
        time.sleep(2.5) 

    print("\n" * 2)
    print("-" * 60)
    print("¡EJERCICIOS TERMINADOS!")
    print(f"En la Parte 1 (Hechos/Opiniones) obtuviste: {good_answers_count} de 8 correctas.")
    print(f"En la Parte 2 (Añadir Evidencia) consideras que diste {good_evidence_count} evidencias fuertes de {len(evidence_exercises)}.")
    print("-" * 60)
    print("¡Sigue fortaleciendo tus argumentos!\n")
    input("Presiona ENTER para volver al menú principal...")

def write_full_argument():
    """Permite al usuario construir un argumento completo con tesis, razón y evidencia."""
    show_header("✍️ ¡Construye un Argumento Completo! ✍️")
    print("Ahora es tu turno de crear un argumento completo sobre un tema que te interese.\n")
    print("Escribe una TESIS (tu afirmación), luego una RAZÓN que la apoye,")
    print("y finalmente una EVIDENCIA (un dato, ejemplo, estudio) que refuerce tu razón.\n")
    print("Si quieres terminar antes, escribe 'listo' en cualquier momento.\n")

    print("\n--- Tu Argumento ---")
    thesis = input("1. Tu Tesis (tu afirmación principal): ").strip()
    if thesis.lower() == 'listo': return
    if not thesis: print("Tesis vacía. Intenta de nuevo."); return

    reason = input(f"2. Una Razón para tu tesis ('porque...'): ").strip()
    if reason.lower() == 'listo': return
    if not reason: print("Razón vacía. Intenta de nuevo."); return

    evidence = input(f"3. Una Evidencia (dato, estudio, ejemplo) que apoya tu razón: ").strip()
    if evidence.lower() == 'listo': return
    if not evidence: print("Evidencia vacía. Intenta de nuevo."); return
    
    print("\n--- Tu Argumento Creado ---")
    print(f"Tesis: '{thesis}'")
    print(f"Razón: '{reason}'")
    print(f"Evidencia: '{evidence}'")
    print("\n¡Excelente! Has construido un argumento completo. ¡La práctica hace al maestro!\n")
    
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: Hechos, Opiniones y Evidencia (10º Grado)")
        print("1. Aprender la Teoría")
        print("2. Ver Ejemplos")
        print("3. Hacer Ejercicios (Identificar y Añadir Evidencia)")
        print("4. Construir Mi Propio Argumento Completo")
        print("5. Salir de la Lección")
        print("-" * 60)

        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            show_theory()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            start_exercises()
        elif choice == '4':
            write_full_argument()
        elif choice == '5':
            print("¡Hasta pronto! Sigue construyendo argumentos sólidos. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
