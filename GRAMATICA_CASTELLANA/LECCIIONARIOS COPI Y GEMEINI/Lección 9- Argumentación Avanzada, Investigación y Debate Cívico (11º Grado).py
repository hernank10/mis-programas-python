import os
import time
import random

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado estilizado para la sección."""
    clear_screen()
    print("=" * 100)
    print(f"🎓 {title.upper()} 🔍")
    print("=" * 100)
    print()

def show_introduction_l9_11th():
    """Introduce los conceptos de argumentación avanzada e investigación para 11º Grado."""
    show_header("Introducción: ¡Maestros de la Argumentación Investigada y el Debate!")
    print("¡Bienvenidos, pensadores y comunicadores de élite! 🚀\n")
    print("En 11.º Grado, ya no solo persuadimos; investigamos a fondo, construimos argumentos irrefutables y dominamos el arte del debate académico y cívico.\n")
    
    print("Esta lección es su trampolín hacia el éxito universitario y la participación ciudadana informada. Desarrollaremos habilidades para:")
    print("   ✅ **Diseñar y ejecutar investigaciones** para respaldar argumentos complejos.")
    print("   ✅ **Construir argumentos académicos** sólidos, integrando diversas fuentes éticamente.")
    print("   ✅ **Prepararse y participar** eficazmente en debates estructurados y discursos cívicos.")
    print("   ✅ **Analizar las dimensiones éticas** de la persuasión y la comunicación en la esfera pública.\n")
    
    print("¡Prepárense para ir más allá de la opinión y forjar argumentos con el poder de la investigación y la razón!\n")
    input("Presiona ENTER para comenzar nuestra inmersión...")

def show_research_methodologies_concept():
    """Explica las metodologías de investigación para argumentos."""
    show_header("Metodologías de Investigación para Argumentos")
    print("Una investigación sólida es la base de un argumento inexpugnable.\n")
    
    print("--- **1. Diseño de un Plan de Investigación Argumentativa:** ---")
    print("  * **Definir la Pregunta de Investigación:** Clara, enfocada y que permita una respuesta argumentativa (no solo descriptiva).")
    print("  * **Formular una Tesis Provisional:** Una hipótesis que guiará tu búsqueda, pero que puede evolucionar con la investigación.")
    print("  * **Identificar Palabras Clave y Términos Relacionados:** Crucial para búsquedas efectivas en bases de datos.")
    print("  * **Seleccionar Metodologías de Búsqueda:** Bases de datos académicas (JSTOR, EBSCO, Google Scholar), bibliotecas universitarias, informes gubernamentales, organizaciones de investigación, etc.\n")

    print("--- **2. Evaluación de Fuentes Académicas y Primarias/Secundarias:** ---")
    print("  * **Fuentes Primarias:** Datos originales (estudios de caso, experimentos, entrevistas, documentos históricos). Alta credibilidad si son relevantes y bien conducidas.")
    print("  * **Fuentes Secundarias:** Análisis e interpretación de fuentes primarias (artículos de revisión, libros de texto académicos, críticas). Útiles para obtener una visión general y diferentes perspectivas.")
    print("  * **Criterios de Evaluación (CRAP Test - Currency, Reliability, Authority, Purpose):**")
    print("    * **Autoridad:** ¿Quién es el autor/organización? ¿Es un experto en el campo? ¿Afiliación?")
    print("    * **Objetividad/Sesgo:** ¿La fuente tiene un propósito oculto? ¿Presenta ambos lados de un argumento?")
    print("    * **Actualidad:** ¿La información es reciente y relevante?")
    print("    * **Precisión:** ¿Los datos son verificables? ¿Hay referencias?")
    print("    * **Relevancia:** ¿La fuente es pertinente a tu tesis?\n")

    print("--- **3. Uso Ético de la Información:** ---")
    print("  * **Citación Avanzada (MLA/APA):** Dominar los estilos de citación para dar crédito adecuado a las fuentes.")
    print("  * **Evitación del Plagio:** Comprender la diferencia entre paráfrasis legítima y plagio, incluso accidental.")
    print("  * **Presentación de Datos sin Sesgo:** Reportar hallazgos de manera justa, incluso si contradicen tu tesis. Reconocer limitaciones de tu propia investigación.\n")
    
    input("Presiona ENTER para explorar la construcción de argumentos académicos...")

def show_academic_argument_concept():
    """Explica la construcción de argumentos académicos."""
    show_header("Construcción de Argumentos Académicos")
    print("El argumento académico es una obra de ingeniería, precisa y bien fundamentada.\n")
    
    print("--- **1. Desarrollo de Tesis Argumentativas Complejas:** ---")
    print("  * **Debatible y Específica:** No una declaración de hecho, sino una postura que requiere defensa y permite un contra-argumento. (Ej. NO: 'El cambio climático existe.' SÍ: 'Las políticas de incentivo fiscal son la forma más efectiva de acelerar la transición a energías renovables en países desarrollados.')")
    print("  * **Matizada:** Evita absolutos. Reconoce complejidades. (Ej. 'Aunque X presenta un desafío, Y es más significativo debido a Z.')")
    print("  * **Respaldada por Evidencia:** Debe ser plausible y verificable con investigación rigurosa.\n")

    print("--- **2. Organización de Argumentos Extensos (Ensayos de Investigación):** ---")
    print("  * **Estructura Lógica General:**")
    print("    * **Introducción:** Contexto del tema, relevancia, gancho, y la tesis clara al final.")
    print("    * **Cuerpo (Párrafos Temáticos):** Cada párrafo desarrolla un punto principal que apoya la tesis. Debe tener: Oración temática, evidencia (citas/paráfrasis), análisis/explicación de la evidencia, conexión a la tesis.")
    print("    * **Contra-argumento y Refutación:** Integrar objeciones principales y responder a ellas con evidencia. (Modelo de Toulmin puede guiar aquí).")
    print("    * **Conclusión:** Reafirmar tesis (con nuevas palabras), resumir los argumentos clave, discutir implicaciones futuras o un llamado a la acción.\n")
    print("  * **Estructuras Específicas:**")
    print("    * **Argumento Causal:** Establecer relaciones de causa y efecto. (Ej. 'A causa B, que a su vez impacta C.')")
    print("    * **Argumento de Propuesta:** Presentar un problema y proponer una solución. (Ej. 'Problema X requiere Solución Y debido a Z.')\n")

    print("--- **3. Integración Sofisticada de Fuentes:** ---")
    print("  * **No solo 'soltar' citas:** Introducir, integrar y analizar cada cita para mostrar cómo apoya tu punto.")
    print("  * **Verbos de Señal:** Usar verbos variados (argumenta, sugiere, refuta, analiza, concluye) para introducir las citas.")
    print("  * **Equilibrio:** Mantener tu propia voz predominante; las citas deben apoyar, no reemplazar, tu análisis. Tu interpretación es clave.\n")
    
    input("Presiona ENTER para prepararte para el debate estructurado...")

def show_debate_preparation_concept():
    """Explica la preparación para el debate estructurado y el discurso cívico."""
    show_header("Preparación para el Debate Estructurado y Discurso Cívico")
    print("El debate y el discurso cívico son la culminación de tus habilidades argumentativas, donde la teoría se encuentra con la práctica.\n")
    
    print("--- **1. Estructuración de Argumentos para Debate:** ---")
    print("  * **Construcción de Caso (Primer Discurso):** Presentar tu argumento inicial de forma clara, concisa y convincente (tesis, puntos principales con evidencia, impacto).")
    print("  * **Refutación Específica (Respuestas):** Identificar los puntos clave del oponente y desmantelarlos lógicamente, citando fallas en su evidencia o razonamiento. Sé específico.")
    print("  * **Reconstrucción del Caso (Reafirmación):** Después de la refutación del oponente, reafirmar y fortalecer tus propios argumentos, mostrando cómo resistieron el ataque o corrigiendo malinterpretaciones.")
    print("  * **Conclusión:** Resumir los puntos ganados y el impacto general de tu posición, reforzando tu tesis.\n")

    print("--- **2. Anticipación y Respuesta en Tiempo Real:** ---")
    print("  * **Preparación Exhaustiva:** Anticipar *todas* las posibles objeciones y tener respuestas con evidencia para cada una. Prepara argumentos para ambas partes del tema.")
    print("  * **Escucha Activa:** Comprender completamente el argumento del oponente antes de responder. No asumas; escucha.")
    print("  * **Pensamiento Rápido:** Formular refutaciones lógicas y coherentes bajo presión de tiempo. Practica la improvisación argumentativa.\n")

    print("--- **3. Adaptación del Discurso para Audiencias Académicas y Cívicas:** ---")
    print("  * **Audiencia Académica:** Priorizar **Logos** (lógica, evidencia rigurosa) y **Ethos** (a través de la experticia, la investigación y la citación precisa). Lenguaje formal, preciso, sin jerga innecesaria.")
    print("  * **Audiencia Cívica/Público General:** Simplificar jerga técnica, usar más **Pathos** (ejemplos concretos, anécdotas, apelación a valores compartidos), estructura clara y concisa, llamado a la acción. Adaptar el nivel de detalle.")
    print("  * **Formalidad y Claridad:** Mantener un estándar alto de lenguaje, evitando ambigüedades y jerga excesiva para ambos públicos.\n")

    print("--- **4. Análisis de los Aspectos Éticos de la Persuasión:** ---")
    print("  * **Responsabilidad del Orador:** El uso de la retórica para fines constructivos y la búsqueda de la verdad, no para engañar o manipular.")
    print("  * **Manipulación vs. Persuasión Legítima:** Distinguir entre el uso de falacias, apelaciones emocionales excesivas o deshonestas (manipulación) y la persuasión basada en la razón, la evidencia y un ethos sólido. La ética es el pilar de la argumentación responsable.\n")
    
    input("Presiona ENTER para nuestros ejercicios avanzados...")

# --- NUEVOS EJERCICIOS PARA LECCIÓN 9 (11.º Grado) ---

def exercise_research_plan():
    """Ejercicio: Diseña tu Plan de Investigación Argumentativa."""
    show_header("Ejercicio: ¡Diseña tu Plan de Investigación Argumentativa!")
    print("Un plan de investigación sólido es el primer paso hacia un argumento convincente. Para este ejercicio, te daré un tema y deberás esbozar un plan.\n")

    topics = [
        {"topic": "El impacto de la inteligencia artificial en el mercado laboral del futuro. ¿Deberían los gobiernos implementar una renta básica universal para contrarrestar el desplazamiento de empleos?",
         "guide": """Tu plan debe incluir:
    1. Una posible [b]tesis debatible[/b] sobre el tema.
    2. Al menos 3 [b]tipos de fuentes[/b] relevantes para una investigación académica (ej. estudios económicos, informes tecnológicos, artículos de opinión de expertos).
    3. Al menos 5 [b]palabras clave de búsqueda[/b] específicas que usarías.
    4. [b]Estrategias para evaluar la credibilidad[/b] de fuentes complejas (ej. revisión por pares, afiliación de la organización, fecha de publicación, sesgo ideológico).
    5. Una breve mención de [b]contrapuntos[/b] que esperas encontrar."""},
        {"topic": "La efectividad de las políticas de reciclaje urbano y sus desafíos en ciudades grandes. ¿Deberían las ciudades implementar sistemas de reciclaje de pago por uso?",
         "guide": """Tu plan debe incluir:
    1. Una posible [b]tesis debatible[/b] sobre el tema.
    2. Al menos 3 [b]tipos de fuentes[/b] relevantes (ej. datos municipales, estudios de caso de otras ciudades, reportes de ONGs ambientales, artículos de sociología).
    3. Al menos 5 [b]palabras clave de búsqueda[/b] específicas.
    4. [b]Cómo abordar sesgos[/b] en informes de diferentes grupos de interés (ej. empresas de reciclaje vs. grupos de consumidores).
    5. Una breve mención de [b]contrapuntos[/b] que esperas encontrar."""},
    ]
    
    random.shuffle(topics)
    current_topic = topics[0] # Selecciona un tema al azar

    print(f"[b]Tema de Investigación:[/b] {current_topic['topic']}\n")
    print(f"[b]Instrucciones:[/b] {current_topic['guide']}\n")
    
    print("Escribe tu plan de investigación aquí (sé lo más detallado posible).")
    print("(Presiona ENTER dos veces para terminar tu plan):")
    user_plan = ""
    while True:
        line = input()
        if not line:
            break
        user_plan += line + "\n"
    user_plan = user_plan.strip()

    print("\n--- ¡Tu Plan de Investigación! ---")
    print(user_plan)

    print("\n--- Reflexión Guiada (Compara tu plan con estos puntos clave) ---")
    print("1. **Tesis:** ¿Tu tesis es clara, debatible y enfocada? ¿Podría ser más específica?")
    print("2. **Fuentes:** ¿Consideraste fuentes académicas y autorizadas? ¿Diversificaste los tipos de fuentes?")
    print("3. **Palabras Clave:** ¿Son tus palabras clave variadas y te ayudarían a encontrar información relevante y de calidad?")
    print("4. **Credibilidad:** ¿Pensaste en criterios específicos para evaluar la validez de las fuentes (revisión por pares, afiliación, sesgo)?")
    print("5. **Contrapuntos:** ¿Anticipaste las objeciones obvias o los puntos de vista opuestos?\n")
    
    print("¡Un plan sólido es la hoja de ruta para una investigación y un argumento exitosos! 💪")
    input("Presiona ENTER para el siguiente paso...")

def exercise_academic_argument():
    """Ejercicio: Construye un Argumento Académico Complejo."""
    show_header("Ejercicio: ¡Construye un Argumento Académico Complejo!")
    print("Ahora, vamos a practicar la construcción de un argumento académico. Te daré una aserción y algunas 'fichas de investigación'.\n")
    
    argument_scenario = {
        "claim": "La gamificación en el aula puede mejorar significativamente el compromiso y el rendimiento académico de los estudiantes de secundaria, siempre que se diseñe cuidadosamente.",
        "evidence_pieces": [
            "Estudio (2022, Journal of Educational Psychology): Alumnos en aulas gamificadas mostraron un 15% más de participación en actividades y una mejora del 8% en sus calificaciones promedio.",
            "Crítica (Prof. A. Smith, 2021, libro 'Educación y Distracción'): La gamificación excesiva puede desviar el foco del aprendizaje intrínseco y fomentar la competitividad insana.",
            "Informe de la UNESCO (2023): La personalización del aprendizaje es clave para el compromiso estudiantil, y la gamificación ofrece herramientas para adaptar desafíos a niveles individuales.",
            "Entrevista (Maestra B. García, 2024, High School Today): Implementar gamificación requiere tiempo de preparación adicional del profesor y formación constante.",
            "Teoría del Flujo (Mihaly Csikszentmihalyi): Las actividades que equilibran el desafío con las habilidades del individuo fomentan un estado de inmersión y disfrute óptimo."
        ],
        "task_guide": """Tu tarea es escribir un párrafo de entre 8 y 12 oraciones que:
    1. Reafirme la [b]aserción principal[/b] de manera introductoria.
    2. Integre **al menos tres** de las 'fichas de investigación' como evidencia. Asegúrate de [b]introducir cada fuente[/b] (ej. "Según un estudio de 2022...", "La maestra García señala..."), y [b]analizar cómo la evidencia apoya tu punto[/b].
    3. Aborde el [b]contrapunto[/b] (la crítica del Prof. Smith) y lo [b]refute o matice[/b] brevemente, mostrando que tu aserción considera esta objeción.
    4. Mantenga un [b]tono académico[/b] y una [b]transición fluida[/b] entre ideas."""
    }

    print(f"Tu [b]Aserción Principal[/b]: {argument_scenario['claim']}\n")
    print("[b]Fichas de Investigación Disponibles:[/b]")
    for i, piece in enumerate(argument_scenario['evidence_pieces']):
        print(f"  {i+1}. {piece}")
    print()
    print(argument_scenario['task_guide'])
    print("\nEscribe tu párrafo aquí:")
    user_argument = ""
    print("(Presiona ENTER dos veces para terminar tu párrafo):")
    while True:
        line = input()
        if not line:
            break
        user_argument += line + "\n"
    user_argument = user_argument.strip()

    print("\n--- ¡Tu Argumento Académico! ---")
    print(user_argument)

    print("\n--- Reflexión Guiada ---")
    print("Revisa tu argumento con estas preguntas:")
    print("1. **Integración de Fuentes:** ¿Las citas/paráfrasis están bien introducidas y analizaste su relevancia? ¿No solo las 'soltaste'?")
    input("> Tu reflexión: ").strip()

    print("\n2. **Abordaje del Contrapunto:** ¿Refutaste o matizaste la crítica de manera efectiva, mostrando que tu argumento es robusto?")
    input("> Tu reflexión: ").strip()

    print("\n3. **Claridad y Cohesión:** ¿Las ideas fluyen lógicamente de una a otra? ¿Es fácil seguir tu razonamiento?")
    input("> Tu reflexión: ").strip()

    print("\n¡Dominar la integración de evidencia y la refutación es clave para el éxito académico! 📈")
    input("Presiona ENTER para el último ejercicio...")

def exercise_debate_preparation():
    """Ejercicio: Simula un Segmento de Debate."""
    show_header("Ejercicio: ¡Simula un Segmento de Debate!")
    print("Prepárate para un micro-debate. Se te presentará un argumento inicial y deberás preparar una refutación y una breve reconstrucción de tu propio caso.\n")

    debate_scenario = {
        "your_position": "A favor de la implementación de un sistema de transporte público totalmente eléctrico en tu ciudad.",
        "opponent_argument": """El transporte público totalmente eléctrico es inviable para nuestra ciudad.
        [b]Punto 1 (Costo):[/b] Los costos iniciales de adquisición de la flota y la infraestructura de carga son astronómicos, lo que llevaría a un aumento insostenible de los impuestos municipales.
        [b]Punto 2 (Fiabilidad):[/b] La tecnología de baterías aún es inmadura. Veríamos frecuentes fallas y retrasos, interrumpiendo la vida diaria de los ciudadanos.
        [b]Punto 3 (Impacto en Empleos):[/b] La transición eliminaría los empleos existentes de mecánicos de motores de combustión sin generar suficientes nuevos roles especializados, dejando a muchos sin trabajo.
        Por estas razones, la propuesta es irreal y perjudicial para la economía local."""
    }

    print(f"Tu posición: [b]{debate_scenario['your_position']}[/b]\n")
    print("[b]Argumento del Oponente:[/b]")
    print(debate_scenario['opponent_argument'])
    print("\n---")
    print("[b]Tu tarea:[/b] Escribe un párrafo (10-15 oraciones) que combine una [b]refutación a los puntos del oponente[/b] Y una [b]reconstrucción (reafirmación) de tu propio caso[/b].\n")
    print("Considera:")
    print("  1. **Refutación específica:** Desafía cada punto del oponente con lógica o evidencia contraria (puedes inventar brevemente la evidencia, pero hazla plausible).")
    print("  2. **Reconstrucción:** Vuelve a tus puntos fuertes, mostrando cómo tu posición sigue siendo la mejor opción a pesar de las objeciones.")
    print("  3. **Tono:** Mantén un tono respetuoso pero firme y convincente.\n")
    
    print("Escribe tu refutación y reconstrucción aquí:")
    user_response = ""
    print("(Presiona ENTER dos veces para terminar tu respuesta):")
    while True:
        line = input()
        if not line:
            break
        user_response += line + "\n"
    user_response = user_response.strip()

    print("\n--- ¡Tu Respuesta al Debate! ---")
    print(user_response)

    print("\n--- Reflexión Guiada ---")
    print("Evalúa tu desempeño como debatiente:")
    print("1. **Claridad de Refutación:** ¿Abordaste cada punto del oponente de manera clara y específica? ¿Ofreciste una contra-evidencia o una lógica alternativa?")
    input("> Tu reflexión: ").strip()

    print("\n2. **Fuerza de Reconstrucción:** ¿Reafirmaste tu propia posición eficazmente, mostrando por qué sigue siendo superior?")
    input("> Tu reflexión: ").strip()

    print("\n3. **Persuasión General:** ¿Tu respuesta es coherente, lógica y persuasiva en su conjunto?")
    input("> Tu reflexión: ").strip()

    print("\n¡Felicidades! ¡Has practicado las habilidades críticas para el debate y la argumentación cívica! 🗣️⚖️")
    input("Presiona ENTER para terminar la lección...")


def show_main_menu_l9_11th():
    """Muestra el menú principal de la aplicación para 11º Grado."""
    while True:
        show_header("Lección 9: Argumentación Avanzada, Investigación y Debate Cívico (11º Grado)")
        print("1. Introducción: ¡Maestros de la Argumentación Investigada!")
        print("2. Metodologías de Investigación para Argumentos")
        print("3. Construcción de Argumentos Académicos")
        print("4. Preparación para el Debate Estructurado y Discurso Cívico")
        print("5. Ejercicio: ¡Diseña tu Plan de Investigación Argumentativa!")
        print("6. Ejercicio: ¡Construye un Argumento Académico Complejo!")
        print("7. Ejercicio: ¡Simula un Segmento de Debate!")
        print("8. Salir de la Lección")
        print("=" * 100)

        choice = input("Elige un número (1-8): ")

        if choice == '1':
            show_introduction_l9_11th()
        elif choice == '2':
            show_research_methodologies_concept()
        elif choice == '3':
            show_academic_argument_concept()
        elif choice == '4':
            show_debate_preparation_concept()
        elif choice == '5':
            exercise_research_plan()
        elif choice == '6':
            exercise_academic_argument()
        elif choice == '7':
            exercise_debate_preparation()
        elif choice == '8':
            print("¡Adiós, futuros líderes y pensadores! ¡Sigan investigando y debatiendo con rigor! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 8.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu_l9_11th()
