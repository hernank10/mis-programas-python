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
    print(f"🎓 {title.upper()} 📊")
    print("=" * 100)
    print()

def show_introduction_l9_12th():
    """Introduce los conceptos de argumentación para contextos profesionales y de investigación superior."""
    show_header("Introducción: ¡Dominando la Argumentación para el Éxito Universitario y Profesional!")
    print("¡Bienvenidos, futuros líderes y pensadores innovadores! 🌟\n")
    print("En 12.º Grado, su dominio de la argumentación culmina en la capacidad de investigar, analizar críticamente y persuadir en los contextos más exigentes.\n")
    
    print("Esta lección es su preparación final para el rigor académico y las demandas del mundo profesional. Aprenderán a:")
    print("   ✅ **Liderar investigaciones originales** y construir argumentos basados en hallazgos propios.")
    print("   ✅ **Deconstruir discursos complejos** e identificar tácticas persuasivas sofisticadas.")
    print("   ✅ **Formular posiciones matizadas** en temas controversiales, considerando implicaciones éticas.")
    print("   ✅ **Presentar sus ideas** con autoridad y claridad en formatos de alto nivel.\n")
    
    print("¡Es hora de refinar sus habilidades para influir, innovar y destacar en cualquier campo!\n")
    input("Presiona ENTER para comenzar nuestra inmersión profunda...")

def show_original_research_concept():
    """Explica la argumentación en la investigación original."""
    show_header("Argumentación en la Investigación Original")
    print("La investigación original es la cumbre de la argumentación académica: generar nuevo conocimiento y defenderlo.\n")
    
    print("--- **1. Formulación de una Pregunta de Investigación Original:** ---")
    print("  * **Delimitación del Problema:** Identificar un vacío o una controversia específica en el conocimiento existente. No se trata solo de describir un tema, sino de buscar una respuesta nueva y no trivial.")
    print("  * **Criterios de Originalidad:** ¿Tu pregunta aporta algo genuinamente nuevo? ¿Resuelve una disputa académica? ¿Aplica una teoría existente a un nuevo contexto o población?")
    print("  * **Factibilidad:** ¿Es posible investigar esta pregunta con los recursos (tiempo, datos, acceso) disponibles?\n")

    print("--- **2. Diseño de Investigación Argumentativa (Metodología):** ---")
    print("  * **Selección y Justificación:** La elección metodológica debe ser la mejor para responder tu pregunta.")
    print("    * **Cuantitativa:** Datos numéricos, estadísticas (encuestas a gran escala, experimentos). Justificación: medir, comparar, generalizar hallazgos.")
    print("    * **Cualitativa:** Datos textuales, interpretativos (entrevistas en profundidad, grupos focales, análisis de contenido). Justificación: comprender perspectivas, experiencias, significados profundos.")
    print("    * **Mixta:** Combinación de ambas. Justificación: visión más completa y robusta al abordar diferentes aspectos del problema.")
    print("  * **Consideraciones Éticas:** Fundamentales. Incluyen: consentimiento informado, privacidad y anonimato de los participantes, imparcialidad del investigador y manejo responsable de los datos.\n")

    print("--- **3. Análisis y Síntesis de Literatura Académica (Estado del Arte):** ---")
    print("  * **Identificación de Debates Centrales:** ¿Qué dicen los principales autores sobre el tema? ¿Dónde hay desacuerdo o consenso?")
    print("  * **Teorías Predominantes y Metodologías Aceptadas:** Entender el 'lenguaje' y las normas del campo de estudio para posicionar tu trabajo.")
    print("  * **Brechas en el Conocimiento:** Es crucial identificar dónde tu investigación puede hacer una contribución original, llenando un vacío existente.\n")

    print("--- **4. Presentación de Hallazgos Originales:** ---")
    print("  * **Integración con la Literatura Existente:** Tus hallazgos deben dialogar con lo que ya se sabe, ya sea confirmando, refutando o extendiendo el conocimiento. No los presentes de forma aislada.")
    print("  * **Argumentación Coherente:** Cada sección de tu investigación (introducción, metodología, resultados, discusión, conclusión) debe construir el argumento central de tu tesis original de forma lógica y secuencial.\n")
    
    input("Presiona ENTER para explorar el análisis crítico de discurso...")

def show_critical_discourse_concept():
    """Explica el análisis crítico de discurso y la argumentación sofisticada."""
    show_header("Análisis Crítico de Discurso y Argumentación Sofisticada")
    print("El pensamiento crítico avanzado es esencial para navegar y desmantelar discursos complejos y potencialmente engañosos.\n")
    
    print("--- **1. Deconstrucción de Discursos Políticos y Científicos Complejos:** ---")
    print("  * **Identificación de Agendas Ocultas:** ¿Hay intereses económicos, políticos o ideológicos no declarados detrás del mensaje? ¿Quién se beneficia del discurso?")
    print("  * **Suposiciones Implícitas:** ¿Qué se da por sentado sin ser explícitamente dicho? ¿Hay premisas no declaradas o sesgos culturales/sociales?")
    print("  * **Uso Estratégico de Estadísticas y Datos:** Analiza si las estadísticas están presentadas de forma engañosa (ej. correlación vs. causalidad, tamaño de la muestra, gráficos manipulados) o si se omiten datos relevantes.")
    print("  * **Apelaciones Retóricas Avanzadas:**")
    print("    * **Kairos:** La oportunidad o el 'momento adecuado' para el discurso. ¿Por qué se dice esto AHORA?")
    print("    * **Decorum:** La adecuación del discurso al público, la situación y el estilo. ¿Es el tono apropiado para el mensaje y la audiencia, o busca manipular?\n")

    print("--- **2. Identificación de Falacias Lógicas Avanzadas y Tácticas Persuasivas Engañosas:** ---")
    print("  * **Ad Populum (Apelación a la Popularidad):** Argumentar que algo es verdad porque muchas personas lo creen o hacen.")
    print("  * **Falsa Dicotomía/Dilema Falso:** Presentar solo dos opciones como si fueran las únicas posibles, cuando en realidad existen más.")
    print("  * **Pendiente Resbaladiza:** Afirmar que una acción inevitablemente conducirá a una serie de consecuencias negativas, a menudo exageradas y sin evidencia suficiente.")
    print("  * **Tu Quoque (Tú También):** Desacreditar un argumento señalando que el oponente también ha hecho lo que critica, en lugar de abordar el argumento en sí.")
    print("  * **Apelación a la Ignorancia:** Argumentar que algo es verdadero porque no se ha probado que sea falso, o falso porque no se ha probado que sea verdadero.")
    print("  * **Hombre de Paja/Falsa Equivalencia:** Distorsionar o exagerar el argumento del oponente para hacerlo más fácil de atacar, o equiparar dos cosas que no son realmente equivalentes.\n")

    print("--- **3. Evaluación de la Validez y Solidez de Argumentos de Expertos:** ---")
    print("  * **No solo el 'qué':** Más allá de lo que dice un experto, analiza la calidad de su evidencia, la coherencia lógica de su razonamiento y si considera y aborda contrapuntos.")
    print("  * **Consenso Científico vs. Opinión Individual:** Distingue entre un hallazgo validado por el consenso de la comunidad académica y la opinión, incluso de un experto individual, que puede no ser representativa del campo.\n")
    
    input("Presiona ENTER para abordar temas controversiales...")

def show_controversial_topics_concept():
    """Explica la argumentación en temas controversiales y delicados."""
    show_header("Argumentación en Temas Controversiales y Delicados")
    print("Abordar la controversia y los dilemas éticos con maestría requiere no solo lógica, sino también empatía y una profunda consideración ética.\n")
    
    print("--- **1. Formulación de Posiciones Matizadas:** ---")
    print("  * **Reconocimiento de la Complejidad:** Entender que muchos problemas no tienen soluciones binarias o 'correctas', sino múltiples perspectivas válidas y complejidades inherentes.")
    print("  * **Integración de Múltiples Perspectivas:** Mostrar que has considerado diferentes puntos de vista, incluso los opuestos. Esto no debilita tu Ethos; lo fortalece al demostrar un pensamiento exhaustivo.")
    print("  * **Lenguaje Preciso:** Evitar generalizaciones excesivas, simplificaciones y lenguaje polarizador que pueda alienar a la audiencia.\n")

    print("--- **2. Construcción de Argumentos Basados en Valores y Principios Éticos:** ---")
    print("  * **Más allá de los Datos:** Reconocer que algunas decisiones se basan fundamentalmente en principios morales, justicia, equidad, derechos humanos, dignidad, etc., no solo en estadísticas.")
    print("  * **Consistencia Ética:** Asegurar que tu argumento no contradiga principios éticos fundamentales que tu audiencia o la sociedad en general valoran.")
    print("  * **Apelación a la Conciencia:** Utilizar Pathos de manera ética para inspirar acciones basadas en valores compartidos, sin manipular emociones.\n")

    print("--- **3. Comunicación Empática y Estratégica:** ---")
    print("  * **Respeto y Escucha Activa:** Abordar a quienes tienen puntos de vista diferentes con respeto genuino, buscando entender sus razones, no solo refutarlas.")
    print("  * **Anticipación de Reacciones Emocionales:** En temas sensibles, saber que el público puede reaccionar emocionalmente. Prepara tu discurso para manejar estas reacciones con calma y tacto.")
    print("  * **Adaptación sin Comprometer la Integridad:** Ajustar el lenguaje y el enfoque al público sin sacrificar la verdad, la evidencia o tus principios fundamentales. La integridad es primordial.\n")
    
    input("Presiona ENTER para dominar la presentación de alto nivel...")

def show_high_level_presentation_concept():
    """Explica la presentación oral y escrita de alto nivel."""
    show_header("Presentación Oral y Escrita de Alto Nivel")
    print("La persuasión profesional y académica exige no solo un gran argumento, sino también una ejecución impecable en la presentación.\n")
    
    print("--- **1. Estrategias para Ponencias y Presentaciones Académicas:** ---")
    print("  * **Organización Lógica Impecable:** Una introducción clara (problema, pregunta, tesis), un desarrollo estructurado (hallazgos, análisis con evidencia), y una conclusión memorable (reafirmación, implicaciones, llamado a la acción).")
    print("  * **Claridad Visual (Diapositivas/Apoyos):** Minimalismo visual, gráficos claros y etiquetados, puntos clave concisos. Las diapositivas deben apoyar, no reemplazar, al orador.")
    print("  * **Manejo de Preguntas y Objeciones:** Escuchar activamente la pregunta, procesarla rápidamente, responder con calma y autoridad. Admite limitaciones si es necesario, demuestra honestidad intelectual. 'Gracias por esa pregunta tan pertinente...'")
    print("  * **Presencia y Credibilidad:** Contacto visual, postura confiada, voz clara y modulada.\n")

    print("--- **2. Redacción de Documentos de Posición y Propuestas de Investigación:** ---")
    print("  * **Estructura Formal:** Resumen ejecutivo, antecedentes, planteamiento del problema, revisión de literatura, metodología propuesta, resultados esperados, presupuesto (si aplica), cronograma, impacto y conclusiones.")
    print("  * **Lenguaje Preciso y Conciso:** Cada palabra cuenta. Evitar la redundancia, la ambigüedad y la jerga innecesaria. La claridad es primordial.")
    print("  * **Argumentación Basada en Evidencia:** Cada afirmación debe ser respaldada rigurosamente por datos, lógica sólida o referencias académicas fiables. No dejar espacio a la especulación infundada.\n")

    print("--- **3. Uso del Lenguaje Persuasivo para Impacto (con Ética):** ---")
    print("  * **Ritmo y Pausas Estratégicas:** Utiliza el ritmo del habla y pausas para enfatizar puntos clave, permitir la asimilación de información compleja y crear tensión o reflexión.")
    print("  * **Repetición Estratégica:** De ideas centrales, frases memorables o eslóganes, para reforzar el mensaje sin ser redundante.")
    print("  * **Analogías Complejas y Metáforas Potentes:** Para explicar conceptos difíciles de forma accesible y relacionarlos con la experiencia de la audiencia.")
    print("  * **Anécdotas Breves y Relevantes:** Para humanizar el mensaje y generar conexión emocional (Pathos bien usado), siempre y cuando apoyen el argumento central.")
    print("  * **Siempre al Servicio de la Claridad y la Verdad:** Las técnicas retóricas deben amplificar la verdad, no distorsionar la realidad ni manipular al público. La integridad es primordial en toda comunicación persuasiva.\n")
    
    input("Presiona ENTER para nuestros ejercicios de alto nivel...")

# --- NUEVOS EJERCICIOS PARA LECCIÓN 9 (12.º Grado) ---

def exercise_research_design():
    """Ejercicio: Diseña tu Investigación Original."""
    show_header("Ejercicio: ¡Diseña tu Investigación Original!")
    print("Para este ejercicio, vas a proponer un diseño de investigación para un problema complejo. Imagina que es para un proyecto universitario.\n")

    problems = [
        {"problem": "Existe una creciente polarización en las redes sociales sobre temas científicos (ej. cambio climático, vacunas). ¿Cómo se podría diseñar una investigación original que proponga estrategias para fomentar el diálogo constructivo y reducir la desinformación en estas plataformas?",
         "guide": """Tu diseño de investigación debe incluir:
    1. Una [b]pregunta de investigación específica y ORIGINAL[/b] (que no haya sido respondida directamente por otros).
    2. La [b]metodología propuesta[/b] (cuantitativa, cualitativa o mixta) y una [b]justificación clara[/b] de por qué es la más adecuada para tu pregunta.
    3. Los [b]tipos de datos[/b] que recopilarías (ej. encuestas, entrevistas, análisis de contenido de publicaciones, experimentos) y [b]cómo los analizarías[/b] para responder a tu pregunta.
    4. Las [b]posibles limitaciones de tu investigación[/b] y [b]desafíos éticos[/b] (ej. privacidad, sesgo del investigador, manipulación de datos)."""},
        {"problem": "A pesar de la disponibilidad de información sobre hábitos de vida saludables, las tasas de obesidad y enfermedades crónicas siguen siendo altas en la población joven. ¿Cómo diseñarías una investigación original que explore la efectividad de intervenciones innovadoras (no solo educativas) para promover estilos de vida saludables en este grupo demográfico?",
         "guide": """Tu diseño de investigación debe incluir:
    1. Una [b]pregunta de investigación específica y ORIGINAL[/b] que aborde el problema.
    2. La [b]metodología propuesta[/b] (cuantitativa, cualitativa o mixta) y una [b]justificación clara[/b] de por qué es la más adecuada.
    3. Los [b]tipos de datos[/b] que recopilarías (ej. datos de salud, diarios de hábitos, grupos focales, resultados de programas piloto) y [b]cómo los analizarías[/b].
    4. [b]Consideraciones éticas clave[/b] al trabajar con una población joven (ej. consentimiento de padres/tutores, protección de datos sensibles, impacto psicológico)."""},
    ]
    
    random.shuffle(problems)
    current_problem = problems[0]

    print(f"[b]Problema de Investigación a Abordar:[/b] {current_problem['problem']}\n")
    print(f"[b]Instrucciones para tu Diseño:[/b] {current_problem['guide']}\n")
    
    print("Escribe tu propuesta de diseño de investigación aquí (sé lo más detallado y específico posible).")
    print("(Presiona ENTER dos veces para terminar tu propuesta):")
    user_design = ""
    while True:
        line = input()
        if not line:
            break
        user_design += line + "\n"
    user_design = user_design.strip()

    print("\n--- ¡Tu Propuesta de Diseño de Investigación! ---")
    print(user_design)

    print("\n--- Guía de Reflexión (Evalúa tu diseño como lo haría un comité académico) ---")
    print("1. **Originalidad y Especificidad:** ¿Tu pregunta es genuinamente original y lo suficientemente específica para ser investigable?")
    input("> Tu autoevaluación: ").strip()

    print("\n2. **Coherencia Metodológica:** ¿La metodología elegida es la más apropiada y justificaste por qué? ¿Los tipos de datos y análisis son coherentes con ella?")
    input("> Tu autoevaluación: ").strip()

    print("\n3. **Factibilidad y Ética:** ¿Es tu diseño factible con recursos limitados? ¿Abordaste las limitaciones y los aspectos éticos de manera exhaustiva y reflexiva?")
    input("> Tu autoevaluación: ").strip()
    
    print("\n¡Un diseño riguroso es el cimiento de una investigación creíble y con impacto! 🔬")
    input("Presiona ENTER para el siguiente ejercicio...")

def exercise_critical_discourse_analysis():
    """Ejercicio: Analiza un Discurso Complejo y Sofisticado."""
    show_header("Ejercicio: ¡Analiza un Discurso Complejo y Sofisticado!")
    print("Lee el siguiente extracto de un discurso y realiza un análisis crítico, identificando elementos retóricos avanzados y posibles tácticas engañosas.\n")

    discourse_examples = [
        {"title": "Extracto de Discurso Político sobre el Crecimiento Económico",
         "text": """"La oposición insiste en que nuestras políticas actuales son perjudiciales, pero ignoran la verdad irrefutable: desde que asumimos el cargo, nuestra nación ha experimentado una tasa de crecimiento del PIB del 3% anual, un logro sin precedentes en la última década. Quienes critican esta 'nueva era de prosperidad' están ciegos a la realidad o, peor aún, buscan socavar la confianza del pueblo para sus propios fines políticos. Es claro que solo hay dos caminos: el nuestro, de progreso y estabilidad, o el de ellos, que nos arrastrará al estancamiento y la miseria. No podemos permitir que su negatividad nos detenga; el pueblo ya ha hablado con su apoyo masivo. Es su deber cívico apoyar la dirección que nos ha traído la bonanza." """,
         "analysis_points": {
             "Agendas/Suposiciones": "El orador busca consolidar poder y desacreditar a la oposición. Asume que el crecimiento del PIB es el único o principal indicador de bienestar y que su gestión es la única causa de dicho crecimiento. Implícitamente sugiere que el apoyo popular valida sus políticas sin necesidad de análisis profundo.",
             "Uso de Datos": "Menciona un 3% de crecimiento del PIB, lo cual es un dato concreto. Sin embargo, no ofrece contexto (ej. inflación, distribución de riqueza, comparación con otras economías similares). Lo presenta como 'irrefutable' y 'sin precedentes' sin detallar el periodo exacto ni la metodología.",
             "Falacias Avanzadas": "1. **Falsa Dicotomía:** 'solo hay dos caminos... el nuestro... o el de ellos' – simplifica excesivamente las opciones políticas. 2. **Ad Hominem (circunstancial/motivacional):** 'buscan socavar la confianza del pueblo para sus propios fines políticos' – ataca los motivos de la oposición en lugar de sus argumentos. 3. **Ad Populum:** 'el pueblo ya ha hablado con su apoyo masivo' y 'Es su deber cívico apoyar' – apela a la popularidad o el deber colectivo para validar la política, no a su mérito intrínseco. 4. **Pendiente Resbaladiza (implícita):** Sugiere que la opción de la oposición 'nos arrastrará al estancamiento y la miseria' sin pasos intermedios o evidencia.",
             "Retórica Avanzada (Kairos/Decorum)": "Kairos: El discurso se da quizás en un momento de reporte de indicadores económicos positivos, aprovechando la oportunidad. Decorum: El tono es de autoridad y confrontación, buscando movilizar a los partidarios y desmoralizar a los oponentes, lo que puede ser efectivo en un contexto político polarizado, pero no promueve un diálogo racional."
         }},
        {"title": "Extracto de Artículo Científico sobre el Nuevo Tratamiento",
         "text": """ "Nuestro innovador tratamiento, 'Alpha-Cure', ha demostrado una remisión completa en el 75% de los casos en nuestra fase 2a de ensayos clínicos. Esto supera con creces las terapias convencionales, que apenas alcanzan un 40%. Aquellos que dudan de estos resultados, alegando la pequeña muestra (n=50), ignoran la magnitud del efecto observado. Siempre ha sido la tendencia de la 'vieja guardia' de la comunidad médica aferrarse a lo conocido en lugar de abrazar el progreso. Es el momento de la verdad para la medicina: o avanzamos con soluciones audaces como Alpha-Cure, o nos quedamos estancados en el pasado, viendo sufrir a más pacientes. La decisión es obvia para cualquiera con visión de futuro." """,
         "analysis_points": {
             "Agendas/Suposiciones": "El autor tiene un claro interés en promover 'Alpha-Cure'. Asume que una pequeña muestra con un gran efecto es suficiente para generalizar y que la crítica a la metodología equivale a 'dudar del progreso'.",
             "Uso de Datos": "Presenta porcentajes de remisión (75% vs 40%). Críticamente, menciona la 'pequeña muestra (n=50)' pero minimiza su importancia. Un tamaño de muestra pequeño limita significativamente la generalizabilidad y la validez estadística, un punto crucial que el autor 'ignora'.",
             "Falacias Avanzadas": "1. **Ad Hominem (circunstancial/motivacional):** Ataca a los críticos como la 'vieja guardia' que 'se aferra a lo conocido' en lugar de abordar sus preocupaciones metodológicas válidas. 2. **Falsa Dicotomía:** 'o avanzamos con soluciones audaces como Alpha-Cure, o nos quedamos estancados en el pasado' – presenta solo dos opciones extremas. 3. **Apelación a la Novedad:** Implícitamente sugiere que 'innovador' y 'audaz' son inherentemente mejores.",
             "Retórica Avanzada (Kairos/Decorum)": "Kairos: El discurso busca capitalizar el entusiasmo por nuevas soluciones médicas. Decorum: Aunque es un artículo científico (que debería ser objetivo), el tono es marcadamente promocional y confrontativo ('vieja guardia'), lo cual es inusual y sospechoso para un reporte puramente científico. Busca generar emoción (Pathos) y descreditar la crítica (Ethos negativo al oponente)."
         }}
    ]

    random.shuffle(discourse_examples)
    current_discourse = discourse_examples[0]

    print(f"[b]Título del Discurso:[/b] {current_discourse['title']}\n")
    print("[b]Extracto del Discurso:[/b]")
    print(current_discourse['text'])
    print("\n---")
    print("[b]Tu tarea:[/b] Realiza un análisis crítico detallado. Identifica y explica:")
    print("  1.  [b]Posibles agendas ocultas o suposiciones implícitas[/b] del orador/autor.")
    print("  2.  [b]Cómo se utilizan (o manipulan) las estadísticas o datos[/b].")
    print("  3.  Al menos [b]dos falacias lógicas avanzadas[/b] o tácticas persuasivas engañosas (ej. falsa dicotomía, pendiente resbaladiza, ad populum, tu quoque). Explica por qué son falacias.")
    print("  4.  [b]Elementos retóricos avanzados[/b] como Kairos o Decorum, y su efecto.\n")
    
    print("Escribe tu análisis aquí:")
    user_analysis = ""
    print("(Presiona ENTER dos veces para terminar tu análisis):")
    while True:
        line = input()
        if not line:
            break
        user_analysis += line + "\n"
    user_analysis = user_analysis.strip()

    print("\n--- ¡Tu Análisis Crítico! ---")
    print(user_analysis)

    print("\n--- Análisis Experto (Compara tu análisis con este) ---")
    for point, explanation in current_discourse['analysis_points'].items():
        print(f"[b]{point}:[/b] {explanation}\n")
    
    print("El dominio de la deconstrucción de discursos es una habilidad vital en el mundo moderno. ¡Excelente trabajo! 🧐")
    input("Presiona ENTER para el último ejercicio...")

def exercise_ethical_dilemma_argument():
    """Ejercicio: Argumenta un Dilema Ético/Social."""
    show_header("Ejercicio: ¡Argumenta un Dilema Ético/Social!")
    print("Se te presentará un dilema ético/social complejo. Tu tarea es formular una posición matizada y argumentarla, considerando tanto los datos como los valores éticos.\n")

    dilemmas = [
        {"title": "Dilema de la Vigilancia Masiva vs. Seguridad Nacional",
         "scenario": """En un país democrático, el gobierno propone implementar un sistema de vigilancia masiva de las comunicaciones digitales de todos los ciudadanos para prevenir el terrorismo y el crimen organizado. Argumentan que la seguridad nacional es prioritaria y que "quienes no tienen nada que ocultar, no tienen nada que temer". Los defensores de la privacidad y los derechos civiles alertan sobre el riesgo de abuso de poder, la erosión de libertades fundamentales y la ineficacia probada de tales medidas en algunas naciones.

Tu tarea es formular un argumento matizado (un párrafo de 10-15 oraciones) que proponga una postura equilibrada o la mejor vía a seguir. Considera:
    1.  [b]Reconocer la complejidad[/b] del problema y la validez de ambas preocupaciones (seguridad y privacidad).
    2.  Argumentar tu posición [b]basada en principios éticos[/b] (ej. proporcionalidad, dignidad humana, bien común, derechos fundamentales).
    3.  Ofrecer una [b]solución o enfoque que intente mitigar los riesgos[/b] de tu postura o maximizar los beneficios, reconociendo posibles contrapuntos.
    4.  Mantener un [b]tono empático y estratégico[/b], evitando la polarización."""},
        {"title": "Dilema de la Inteligencia Artificial en la Educación",
         "scenario": """Una universidad líder considera implementar un sistema de IA para evaluar automáticamente los ensayos de los estudiantes y proporcionar retroalimentación. Los proponentes argumentan que esto permitirá una retroalimentación instantánea y personalizada a gran escala, liberando tiempo a los profesores para interacciones más significativas. Los críticos, sin embargo, expresan preocupaciones sobre la pérdida de la "voz" humana en la evaluación, la potencial perpetuación de sesgos algorítmicos presentes en los datos de entrenamiento, y la devaluación de habilidades de escritura y pensamiento crítico si los estudiantes solo aprenden a "complacer" a la IA.

Tu tarea es formular un argumento matizado (un párrafo de 10-15 oraciones) que proponga una postura equilibrada o la mejor vía a seguir. Considera:
    1.  [b]Reconocer la complejidad[/b] del problema y los pros y contras de la IA en educación.
    2.  Argumentar tu posición [b]basada en principios éticos[/b] (ej. equidad, desarrollo integral del estudiante, rol del educador, propósito de la evaluación).
    3.  Proponer [b]directrices o un modelo de implementación[/b] que maximice los beneficios y minimice los riesgos, reconociendo contrapuntos.
    4.  Mantener un [b]tono empático y estratégico[/b], enfocado en el bienestar educativo."""},
    ]

    random.shuffle(dilemmas)
    current_dilemma = dilemmas[0]

    print(f"[b]Dilema Ético/Social:[/b] {current_dilemma['title']}\n")
    print(current_dilemma['scenario'])
    print("\n---")
    print("Escribe tu argumento matizado aquí:")
    user_argument = ""
    print("(Presiona ENTER dos veces para terminar tu argumento):")
    while True:
        line = input()
        if not line:
            break
        user_argument += line + "\n"
    user_argument = user_argument.strip()

    print("\n--- ¡Tu Argumento Matizado! ---")
    print(user_argument)

    print("\n--- Reflexión Guiada ---")
    print("Evalúa tu argumento con estas preguntas cruciales:")
    print("1. **Matización:** ¿Reconociste adecuadamente la complejidad del dilema y la validez de múltiples perspectivas, o tomaste una postura demasiado simplista?")
    input("> Tu autoevaluación: ").strip()

    print("\n2. **Fundamentación Ética:** ¿Basaste tu argumento en principios éticos claros (justicia, equidad, derechos, bien común) y no solo en conveniencia o eficiencia?")
    input("> Tu autoevaluación: ").strip()

    print("\n3. **Viabilidad y Contrapuntos:** ¿Ofreciste una solución o enfoque práctico? ¿Anticipaste y respondiste (implícita o explícitamente) a posibles objeciones a tu propia postura?")
    input("> Tu autoevaluación: ").strip()
    
    print("\n¡Dominar la argumentación en dilemas éticos es fundamental para ser un ciudadano global responsable! 🌍⚖️")
    input("Presiona ENTER para terminar la lección...")


def show_main_menu_l9_12th():
    """Muestra el menú principal de la aplicación para 12º Grado."""
    while True:
        show_header("Lección 9: Argumentación para Contextos Profesionales y de Investigación Superior (12º Grado)")
        print("1. Introducción: ¡Dominando la Argumentación para el Éxito!")
        print("2. Argumentación en la Investigación Original")
        print("3. Análisis Crítico de Discurso y Argumentación Sofisticada")
        print("4. Argumentación en Temas Controversiales y Delicados")
        print("5. Presentación Oral y Escrita de Alto Nivel")
        print("6. Ejercicio: ¡Diseña tu Investigación Original!")
        print("7. Ejercicio: ¡Analiza un Discurso Complejo y Sofisticado!")
        print("8. Ejercicio: ¡Argumenta un Dilema Ético/Social!")
        print("9. Salir de la Lección")
        print("=" * 100)

        choice = input("Elige un número (1-9): ")

        if choice == '1':
            show_introduction_l9_12th()
        elif choice == '2':
            show_original_research_concept()
        elif choice == '3':
            show_critical_discourse_concept()
        elif choice == '4':
            show_controversial_topics_concept()
        elif choice == '5':
            show_high_level_presentation_concept()
        elif choice == '6':
            exercise_research_design()
        elif choice == '7':
            exercise_critical_discourse_analysis()
        elif choice == '8':
            exercise_ethical_dilemma_argument()
        elif choice == '9':
            print("¡Adiós, futuros líderes y pensadores! ¡Que sus argumentos sean siempre rigurosos y éticos! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 9.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu_l9_12th()
