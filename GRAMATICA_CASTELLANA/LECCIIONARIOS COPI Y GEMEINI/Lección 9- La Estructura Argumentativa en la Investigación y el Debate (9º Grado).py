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
    print(f"🧠 {title.upper()} 🔬")
    print("=" * 100)
    print()

def show_introduction_l9():
    """Introduce los conceptos de análisis y construcción argumentativa en 9º Grado."""
    show_header("Introducción: ¡Maestros de la Investigación y el Debate!")
    print("¡Bienvenidos, jóvenes pensadores críticos! 🚀")
    print("Ya son expertos en organizar ideas y entender cómo la estructura afecta un mensaje.")
    print("En 9.º Grado, llevaremos esto al siguiente nivel: ¡serán verdaderos detectives de la información y arquitectos de argumentos sólidos!\n")
    
    print("En esta lección, ustedes aprenderán a:")
    print("   ✅ **Evaluar la credibilidad** de fuentes analizando cómo organizan su información.")
    print("   ✅ **Sintetizar y organizar ideas de MÚLTIPLES fuentes** en argumentos complejos.")
    print("   ✅ **Construir refutaciones** efectivas, anticipando y contrarrestando objeciones.\n")
    
    print("¡Prepárense para investigar, analizar y debatir como expertos!\n")
    input("Presiona ENTER para comenzar nuestra inmersión...")

def show_credibility_organization_concept():
    """Explica la evaluación de credibilidad a través de la organización."""
    show_header("Evaluación de Credibilidad: ¿El Orden Dice la Verdad?")
    print("La forma en que se organiza la información puede ser una pista sobre la **credibilidad** de una fuente y si hay **sesgos**.\n")
    print("--- **Preguntas Clave al Analizar la Organización de una Fuente:** ---")
    print("  1. **¿Qué se presenta primero? ¿Qué se deja para el final?**")
    print("     * **Sesgo:** Si un autor presenta primero solo los datos que apoyan su punto y deja las objeciones (o las minimiza) al final, puede estar tratando de influenciarte.")
    print("     * **Credibilidad:** Una fuente equilibrada puede presentar primero el contexto del problema, luego las diferentes perspectivas y finalmente su conclusión, o incluso admitir limitaciones al inicio.")
    
    print("  2. **¿Se omite información clave o se le resta importancia por su posición?**")
    print("     * **Sesgo:** Ignorar contra-argumentos o colocarlos en un lugar secundario (ej. una nota al pie de página) es una señal de que la organización busca favorecer una postura.")
    print("     * **Credibilidad:** Presentar objeciones y luego refutarlas de forma lógica demuestra un argumento más robusto y honesto.")
    
    print("  3. **¿Cómo se organiza la evidencia? ¿Hay un flujo lógico o es una 'lista' de hechos aislados?**")
    print("     * **Credibilidad:** La evidencia bien organizada, que fluye lógicamente para apoyar una tesis, es más persuasiva y creíble que una mera acumulación de datos.")
    
    print("  4. **¿Los datos presentados al principio son conclusiones o puntos de partida para el análisis?**")
    print("     * **Credibilidad:** Un texto que presenta datos como punto de partida para una discusión (inductivo) puede parecer más abierto que uno que comienza con conclusiones fuertes y luego busca apoyar (deductivo) sin considerar otras opciones.\n")
    
    print("¡Ser un lector crítico significa ver más allá de las palabras: hay que ver cómo están presentadas!\n")
    input("Presiona ENTER para un desafío de análisis de credibilidad...")

def game_credibility_analysis():
    """Juego para analizar la credibilidad de fuentes basándose en su organización."""
    show_header("Juego 1: ¡El Detective de la Credibilidad!")
    print("Lee el siguiente extracto. Reflexiona sobre cómo su organización podría influir en tu percepción de la credibilidad o el sesgo.\n")

    scenarios = [
        {"text": "El plan X es la única solución viable para la economía. Mis oponentes presentan argumentos débiles, que ignoro por el momento. Lo importante es que, al implementar el plan X, veremos un crecimiento sin precedentes en solo seis meses.",
         "analysis_points": "El autor posiciona su plan como 'la única solución viable' al inicio, descartando 'débiles' argumentos contrarios sin presentarlos. Esto indica un posible sesgo y falta de equilibrio. La evidencia (crecimiento) se presenta como una promesa sin detalles organizativos sobre cómo se logrará, lo que podría reducir la credibilidad."},
        {"text": "Recientes estudios sugieren una correlación entre el uso prolongado de pantallas y ciertos patrones de sueño alterados en adolescentes. Si bien algunos podrían argumentar que los factores sociales influyen más, la evidencia neurobiológica indica que la exposición a la luz azul antes de dormir es un factor significativo que interrumpe la producción de melatonina.",
         "analysis_points": "El autor presenta una correlación con evidencia ('estudios recientes') y luego aborda una posible objeción ('algunos podrían argumentar...'), para luego refutarla con evidencia científica ('evidencia neurobiológica'). Esta organización de 'reconocer y refutar' aumenta la credibilidad y muestra un argumento más robusto."},
        {"text": "Los nuevos impuestos, que serán aplicados a partir del próximo mes, generarán un ingreso adicional significativo para las arcas públicas. Por supuesto, algunos sectores se verán afectados, pero estos sacrificios menores son necesarios para el bienestar general a largo plazo. Es fundamental entender que cada medida tiene un costo, y este es mínimo en comparación con el beneficio.",
         "analysis_points": "El autor prioriza los beneficios ('ingreso adicional significativo') al inicio. Luego, minimiza los efectos negativos ('sacrificios menores') y los justifica ('necesarios para el bienestar general'). La organización busca persuadir al lector de que los beneficios superan los costos, lo que podría ser una táctica para suavizar la percepción de un impacto negativo. La credibilidad dependerá de si se presentan datos concretos de esos 'sacrificios menores' y cómo se justifica el 'bienestar general'."}
    ]
    
    random.shuffle(scenarios)
    num_scenarios = 1 # Para enfocarse en la profundidad del análisis

    for i in range(num_scenarios):
        s = scenarios[i]
        print(f"\n--- Escenario {i+1} de {num_scenarios} ---")
        print(f"**Extracto:** '{s['text']}'")
        
        print("\n**Tu turno de ser el detective de la credibilidad:**")
        print("¿Cómo crees que la organización de este extracto (qué se pone primero, qué se omite o minimiza, cómo se fluye) influye en su credibilidad o revela un posible sesgo?")
        user_analysis = input("Escribe tu análisis (puedes ser breve): \n> ").strip()
        
        print("\n--- Análisis Experto ---")
        print(s['analysis_points'])
        print(f"\nTu análisis: '{user_analysis}'")
        print("¡Compara tu análisis! La clave es ver más allá de las palabras y entender la estrategia detrás del orden.\n")
        time.sleep(15)
    
    print(f"\nJuego terminado. ¡Sigue entrenando tu ojo crítico! 🕵️‍♀️")
    input("Presiona ENTER para el siguiente paso...")

def show_synthesis_multiple_sources_concept():
    """Explica la organización para la síntesis de múltiples fuentes."""
    show_header("Organización para la Síntesis: ¡Tejiendo Hilos de Información!")
    print("Cuando investigamos, no usamos una sola fuente. ¡Usamos varias! El reto es no solo 'pegar' información, sino **sintetizarla** de forma organizada.\n")
    
    print("--- **Estrategias para Sintetizar con Organización:** ---")
    print("  1. **Organización Temática (por categorías):**")
    print("     * Agrupa la información de todas tus fuentes por **subtemas** o **aspectos** del tema principal.")
    print("     * *Ejemplo:* Si investigas el cambio climático, tendrías secciones para 'Causas', 'Efectos en la vida marina', 'Efectos en la agricultura', 'Posibles soluciones'. Cada sección integra datos de diferentes fuentes.")
    
    print("  2. **Organización por Punto y Contrapunto:**")
    print("     * Presenta un argumento o postura, y luego incorpora evidencia de fuentes que lo apoyan y fuentes que lo contradicen.")
    print("     * Esto muestra un análisis profundo y equilibrado.")
    
    print("  3. **Organización Comparativa (por fuentes o escuelas de pensamiento):**")
    print("     * Compara directamente lo que diferentes fuentes dicen sobre un mismo punto.")
    * *Ejemplo:* 'Mientras que el autor A argumenta X, el autor B, en contraste, sugiere Y, y la fuente C ofrece una tercera perspectiva Z.'\n")
    
    print("La síntesis organizada transforma una lista de hechos en un argumento coherente y persuasivo.\n")
    input("Presiona ENTER para ver cómo construir refutaciones...")

def show_counterarguments_refutations_concept():
    """Explica la construcción de argumentos contrarrestantes y refutaciones."""
    show_header("Argumentos Contrarrestantes y Refutaciones: ¡Fortaleciendo tu Voz!")
    print("Un argumento fuerte no solo presenta su propia postura, ¡también anticipa y responde a las objeciones!\n")
    
    print("--- **Cómo Organizar tus Refutaciones:** ---")
    print("  1. **Presenta la Contrapuesta:** Empieza por enunciar claramente el argumento o la objeción que vas a refutar. (Ej. 'Algunos podrían argumentar que...')")
    print("  2. **Reconoce su Validez (si aplica):** A veces, un contrapunto tiene algo de verdad. Reconocerlo (brevemente) puede aumentar tu credibilidad. (Ej. 'Es cierto que en algunos casos...')")
    print("  3. **Refuta con Evidencia/Lógica:** Aquí es donde presentas tus razones y evidencia para demostrar por qué el contrapunto es incorrecto, incompleto o menos relevante. (Ej. 'Sin embargo, la evidencia demuestra que...', 'Esta perspectiva no considera que...')")
    print("  4. **Conecta de Nuevo con tu Tesis:** Después de refutar, refuerza cómo tu argumento principal sigue siendo el más fuerte. (Ej. 'Por lo tanto, mi argumento sobre X sigue siendo válido porque...').\n")
    
    print("**Organización de un párrafo de refutación:**")
    print("  * **Oración Temática (Tu argumento o el contrapunto que vas a refutar)**")
    print("  * **Contrapunto/Objeción (Introducir la idea opuesta)**")
    print("  * **Refutación (Evidencia y lógica para desmentir o debilitar el contrapunto)**")
    print("  * **Conclusión (Reafirmar tu argumento o la tesis principal)**\n")
    
    print("¡Dominar la refutación te hace un debatiente y escritor imbatible!\n")
    input("Presiona ENTER para nuestros desafíos de escritura avanzados...")

# --- NUEVOS EJERCICIOS PARA LECCIÓN 9 (9.º Grado) ---
def exercise_analyze_organization_for_credibility():
    show_header("Ejercicio: ¡Organización y Credibilidad en la Noticia!")
    print("Imagina que estás leyendo dos titulares y sus primeros párrafos sobre el mismo evento.")
    print("Tu tarea es analizar cómo la organización de la información en cada uno puede influir en tu percepción de su credibilidad o sesgo.\n")

    articles = [
        {"title": "Titular A: 'Crisis Energética: Precios Disparados por Nuevas Regulaciones Gubernamentales'",
         "text": "Los recientes aumentos en el costo de la energía son una consecuencia directa e ineludible de las nuevas regulaciones impuestas por el gobierno, que han estrangulado la producción. Expertos de la industria han advertido repetidamente que estas políticas llevarían a esta situación. La medida busca, según algunos, 'proteger el medio ambiente', pero el costo económico es devastador.",
         "bias_hint": "Este texto empieza culpando directamente al gobierno y a sus 'nuevas regulaciones', presentando esto como la 'consecuencia directa e ineludible'. Cita 'expertos de la industria' (sin especificar quiénes) y minimiza el objetivo ambiental ('según algunos'). La organización es deductiva y selectiva, priorizando la crítica al gobierno y omitiendo posibles otras causas o beneficios, sugiriendo un fuerte sesgo contra las regulaciones."},
        
        {"title": "Titular B: 'Preocupación por Costo Energético: Análisis de Múltiples Factores y Soluciones'",
         "text": "El aumento en los costos de la energía es un fenómeno complejo influenciado por una combinación de factores, incluyendo la fluctuación de los precios internacionales del petróleo, un incremento en la demanda global y, en menor medida, la implementación de nuevas regulaciones ambientales. Un reciente informe económico (Fuente X) detalla cómo la escasez de recursos y los desafíos de la cadena de suministro también contribuyen a la situación. Diversas soluciones, desde la inversión en energías renovables hasta la optimización del consumo, están siendo debatidas por especialistas.",
         "bias_hint": "Este texto inicia con 'un fenómeno complejo influenciado por una combinación de factores', presentando múltiples causas (precios internacionales, demanda, regulaciones, escasez, cadena de suministro) sin culpar a una sola. Menciona una 'fuente X' específica y aborda 'diversas soluciones'. La organización es más inductiva y equilibrada, sugiriendo una mayor objetividad y credibilidad al presentar un panorama más completo y matizado."}
    ]

    random.shuffle(articles)

    for i, article in enumerate(articles):
        print(f"\n--- Artículo {i+1} de {len(articles)} ---")
        print(f"**{article['title']}**")
        print(f"'{article['text']}'")
        
        print("\n**Tu análisis:** ¿Cómo la organización de este texto (el orden de las ideas, el énfasis, las omisiones) influye en su credibilidad o revela un sesgo? ¿Qué pondrías al inicio o al final para cambiar la percepción?")
        user_analysis = input("Escribe tu análisis aquí (puedes ser breve): \n> ").strip()
        
        print("\n--- Análisis Experto de Organización y Credibilidad ---")
        print(article['bias_hint'])
        print(f"\nTu análisis: '{user_analysis}'")
        print("¡La clave es leer la organización entre líneas! 🧐")
        time.sleep(20)
    
    print("\nEjercicio terminado. ¡Has practicado ser un crítico de la información!\n")
    input("Presiona ENTER para el siguiente ejercicio...")

def exercise_construct_argument_with_multiple_sources():
    show_header("Ejercicio: ¡Construye un Argumento Sintetizando Fuentes!")
    print("Imagina que estás escribiendo un ensayo sobre si los videojuegos son beneficiosos o perjudiciales para los adolescentes.")
    print("Has encontrado estas tres 'fuentes' (ideas/evidencias):")
    print("  A) Fuente X dice que mejoran la coordinación mano-ojo y la resolución de problemas (beneficio).")
    print("  B) Fuente Y argumenta que el tiempo excesivo frente a la pantalla puede reducir la actividad física y el rendimiento académico (perjuicio).")
    print("  C) Fuente Z sugiere que los videojuegos multijugador fomentan habilidades de trabajo en equipo y comunicación (beneficio).")

    print("\nTu tarea es escribir un párrafo (5-7 oraciones) que **sintetice estas ideas en un argumento COHESIVO**.")
    print("Tu párrafo debe tener una idea principal clara sobre los videojuegos y luego integrar las fuentes A, B y C para apoyar o desarrollar tu punto, ¡sin que parezca una lista!")
    print("Piensa en la mejor organización para presentar estas ideas de forma lógica y fluida.\n")

    print("Escribe tu párrafo aquí:")
    user_paragraph = ""
    print("(Presiona ENTER dos veces para terminar tu párrafo):")
    while True:
        line = input()
        if not line:
            break
        user_paragraph += line + "\n"
    user_paragraph = user_paragraph.strip()

    print("\n--- ¡Tu Párrafo Sintetizado! ---")
    print(user_paragraph)

    print("\n--- Reflexión Guiada ---")
    print("Ahora, revisa tu propio trabajo:")
    print("1. **Idea Principal Clara:** ¿Tu párrafo tiene una idea principal clara al inicio o al final sobre los videojuegos?")
    user_reflection_main_idea = input("> Tu reflexión: ").strip()

    print("\n2. **Integración Cohesiva:** ¿Lograste integrar las tres fuentes (A, B, C) de manera que se sientan conectadas y no solo 'pegadas'? ¿Qué palabras o frases usaste para unir las ideas?")
    user_reflection_integration = input("> Tu reflexión: ").strip()

    print("\n3. **Flujo Lógico:** ¿El orden en que presentaste las ideas (beneficios, perjuicios, otro beneficio) tiene sentido? ¿Por qué elegiste ese orden?")
    user_reflection_flow = input("> Tu reflexión: ").strip()

    print("\n¡Dominar la síntesis es clave para la investigación y la escritura académica!\n")
    input("Presiona ENTER para el último ejercicio...")

def exercise_construct_counterargument_refutation():
    show_header("Ejercicio: ¡Construye tu Refutación!")
    print("Imagina que estás escribiendo un ensayo a favor de que los colegios deberían ofrecer más opciones de deportes para todos los estudiantes (no solo los equipos competitivos).")
    print("Sabes que una objeción común es:")
    print("  **Objeción:** 'El colegio no tiene suficientes recursos (dinero, espacio, entrenadores) para más deportes, y los programas actuales ya son costosos.'")

    print("\nTu tarea es escribir un párrafo (4-6 oraciones) donde: ")
    print("  1. **Reconozcas** esta objeción.")
    print("  2. Y luego la **refutes** (demuestres por qué no es un problema insuperable o cómo se puede superar), fortaleciendo tu argumento inicial.")
    print("¡Usa transiciones para guiar al lector!\n")
    
    print("Escribe tu párrafo de refutación aquí:")
    user_refutation_paragraph = ""
    print("(Presiona ENTER dos veces para terminar tu párrafo):")
    while True:
        line = input()
        if not line:
            break
        user_refutation_paragraph += line + "\n"
    user_refutation_paragraph = user_refutation_paragraph.strip()

    print("\n--- ¡Tu Párrafo de Refutación! ---")
    print(user_refutation_paragraph)

    print("\n--- Reflexión Guiada ---")
    print("Revisa cómo estructuraste tu refutación:")
    print("1. **Reconocimiento:** ¿Queda claro que mencionaste la objeción al principio del párrafo?")
    user_reflection_recognition = input("> Tu reflexión: ").strip()

    print("\n2. **Refutación Efectiva:** ¿Presentaste razones o soluciones convincentes para desmentir o debilitar la objeción? ¿Tu refutación es lógica?")
    user_reflection_refutation = input("> Tu reflexión: ").strip()

    print("\n3. **Conexión con tu Tesis:** ¿Después de refutar, tu párrafo vuelve a fortalecer tu argumento principal sobre ofrecer más deportes?")
    user_reflection_connection = input("> Tu reflexión: ").strip()

    print("\n¡Felicidades! Dominar la refutación es una habilidad argumentativa de alto nivel. 👏\n")
    input("Presiona ENTER para terminar la lección...")


def show_main_menu_l9():
    """Muestra el menú principal de la aplicación para 9º Grado."""
    while True:
        show_header("Lección 9: La Estructura Argumentativa en la Investigación y el Debate (9º Grado)")
        print("1. Introducción: ¡Maestros de la Investigación y el Debate!")
        print("2. Evaluación de Credibilidad: ¿El Orden Dice la Verdad?")
        print("3. Jugar: ¡El Detective de la Credibilidad!")
        print("4. Organización para la Síntesis: ¡Tejiendo Hilos de Información!")
        print("5. Argumentos Contrarrestantes y Refutaciones: ¡Fortaleciendo tu Voz!")
        print("6. **NUEVO:** Ejercicio: ¡Organización y Credibilidad en la Noticia!")
        print("7. **NUEVO:** Ejercicio: ¡Construye un Argumento Sintetizando Fuentes!")
        print("8. **NUEVO:** Ejercicio: ¡Construye tu Refutación!")
        print("9. Salir de la Lección")
        print("=" * 100)

        choice = input("Elige un número (1-9): ")

        if choice == '1':
            show_introduction_l9()
        elif choice == '2':
            show_credibility_organization_concept()
        elif choice == '3':
            game_credibility_analysis()
        elif choice == '4':
            show_synthesis_multiple_sources_concept()
        elif choice == '5':
            show_counterarguments_refutations_concept()
        elif choice == '6':
            exercise_analyze_organization_for_credibility()
        elif choice == '7':
            exercise_construct_argument_with_multiple_sources()
        elif choice == '8':
            exercise_construct_counterargument_refutation()
        elif choice == '9':
            print("¡Adiós, maestros de la argumentación! ¡Sigan construyendo conocimiento con integridad! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 9.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu_l9()
