import random
import os
import time

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Muestra un encabezado para la sección."""
    clear_screen()
    print("-" * 70)
    print(f"📚 {title.upper()} 📚")
    print("-" * 70)
    print()

def show_theory():
    """Muestra la sección de teoría sobre la estructura del argumento académico."""
    show_header("Teoría: La Estructura del Argumento Académico")
    print("¡Bienvenidos al nivel preuniversitario de la argumentación! 🎉")
    print("En este grado, perfeccionaremos la construcción de argumentos sólidos, la base de ensayos y trabajos universitarios.\n")
    
    print("Un argumento académico bien estructurado típicamente incluye:")
    print("\n⭐ 1. TESIS (O AFIRMACIÓN CENTRAL):")
    print("   Es la idea principal que quieres defender. Debe ser debatible, clara y específica.")
    print("   Ejemplo: 'La educación superior debería enfocarse más en habilidades blandas que en conocimientos técnicos.'\n")
    
    print("⭐ 2. RAZONES (O PREMISAS):")
    print("   Son las afirmaciones lógicas que apoyan tu tesis. Responden al '¿Por qué?' de tu tesis.")
    print("   Cada razón debe ser una afirmación fuerte y defendible por sí misma.")
    print("   Ejemplo (para la tesis anterior): 'Porque las habilidades blandas, como la comunicación y el trabajo en equipo, son más adaptables a los cambios del mercado laboral.'\n")
    
    print("⭐ 3. EVIDENCIA (O PRUEBAS):")
    print("   Son los datos, hechos, estadísticas, citas de expertos, ejemplos o resultados de investigaciones que **validan tus razones**.")
    print("   La evidencia es lo que hace tu argumento convincente y creíble.")
    print("   Ejemplo (para la razón anterior): 'Un estudio de LinkedIn (2024) reveló que el 85% de los empleadores consideran las habilidades blandas como cruciales para el éxito profesional a largo plazo, independientemente de la especialización técnica.'\n")
    
    print("⭐ 4. CONTRAARGUMENTO Y REFUTACIÓN:")
    print("   Aunque ya lo vimos, es clave en este nivel. Un buen argumento anticipa y responde a objeciones.")
    print("   - Contraargumento: Una objeción a tu tesis o una razón opuesta.")
    print("   - Refutación: Tu respuesta para demostrar por qué el contraargumento no invalida tu posición.\n")
    
    print("Hoy nos enfocaremos en la conexión sólida entre la **Tesis** y las **Razones Lógicas**.")
    print("La coherencia entre estos elementos es la espina dorsal de cualquier ensayo argumentativo.\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de cómo construir tesis y razones."""
    show_header("Ejemplos: Conectando Tesis y Razones")
    
    examples = [
        {
            "thesis": "La inteligencia artificial transformará radicalmente el futuro de la educación.",
            "reason": "Porque la IA puede personalizar el aprendizaje de manera que ningún sistema tradicional puede igualar, adaptándose a las necesidades individuales de cada estudiante.",
            "evidence": "Un informe de UNESCO (2023) destaca que las plataformas de IA pueden ajustar contenidos y ritmos de estudio, mejorando la retención y comprensión en un 30% en pruebas piloto."
        },
        {
            "thesis": "El teletrabajo debería ser la norma en muchas industrias después de la pandemia.",
            "reason": "Porque ofrece mayor flexibilidad y autonomía a los empleados, lo que incrementa su satisfacción y productividad.",
            "evidence": "Según una encuesta de Gartner (2022), el 65% de los trabajadores que implementaron teletrabajo reportaron un aumento en la percepción de autonomía y un 40% en la productividad."
        },
        {
            "thesis": "La inversión en energías renovables es más beneficiosa a largo plazo que la de combustibles fósiles.",
            "reason": "Porque las energías renovables reducen la dependencia de recursos finitos y volátiles, y mitigan el impacto del cambio climático.",
            "evidence": "Datos de la Agencia Internacional de Energía (2024) muestran que el costo nivelado de la energía solar y eólica ya es más bajo que el de las nuevas plantas de carbón y gas en la mayoría de las regiones."
        }
    ]

    print("Observa cómo cada razón responde lógicamente al 'por qué' de la tesis:\n")
    for ex in examples:
        print(f"Tesis: '{ex['thesis']}'")
        print(f"  Razón: '{ex['reason']}'")
        print(f"  (Evidencia para referencia: '{ex['evidence']}')\n")
        print("-" * 70)
        time.sleep(4) # Pausa para que el estudiante procese

    print("\n¡Ahora es tu turno de construir razones sólidas para tesis dadas!\n")
    input("Presiona ENTER para ir a los ejercicios...")

def run_reason_exercise(thesis, model_reason, model_evidence):
    """Ejecuta un solo ejercicio donde el estudiante añade una razón y opcionalmente evidencia."""
    print("\n" + "-" * 70)
    print("Tienes la siguiente Tesis:")
    print(f"Tesis: '{thesis}'")
    print("\nTu turno: Escribe una **razón lógica** que apoye esta tesis.")
    print("(Opcional: puedes intentar pensar también en una evidencia para tu razón)")
    
    user_reason = input("\nTu Razón: ").strip()
    user_evidence = input("Tu Evidencia (opcional): ").strip() # Permite dejar en blanco

    print("\n--- Razones y Evidencia Modelo ---")
    print(f"Razón Modelo: '{model_reason}'")
    if model_evidence:
        print(f"Evidencia Modelo: '{model_evidence}'")
    else:
        print("(No se proporcionó evidencia modelo para este caso, ¡tu creatividad es el límite!)")
    
    while True:
        evaluation = input("\n¿Consideras que tu razón fue lógica y bien conectada con la tesis? (s/n): ").lower().strip()
        if evaluation == 's':
            print("¡Excelente! Estás fortaleciendo tu capacidad argumentativa.")
            return True
        elif evaluation == 'n':
            print("Está bien. Comparar con el modelo te ayudará a afinar tu lógica.")
            return False
        else:
            print("Respuesta no válida. Elige 's' para sí o 'n' para no.")
    print("-" * 70)
    time.sleep(3) # Pausa para que el usuario lea el feedback

def start_exercises():
    """Inicia la sección de ejercicios de construcción de razones."""
    show_header("¡A Practicar! Conectando Tesis y Razones")
    print("Para cada tesis incompleta, añade una razón lógica que la apoye.\n")

    exercises = [
        {"thesis": "La educación a distancia es una modalidad de aprendizaje cada vez más relevante,",
         "reason": "porque ofrece flexibilidad de horarios y acceso a recursos educativos globales.",
         "evidence": "Un informe de Statista (2023) indica que el 70% de los estudiantes valoran la flexibilidad como el principal beneficio de la educación en línea."},
        
        {"thesis": "El fomento del pensamiento crítico desde la escuela primaria es fundamental,",
         "reason": "ya que prepara a los estudiantes para analizar información, resolver problemas complejos y tomar decisiones informadas en un mundo cambiante.",
         "evidence": "Estudios de la OCDE (2022) asocian el desarrollo temprano del pensamiento crítico con mejores resultados académicos y profesionales a largo plazo."},
        
        {"thesis": "La lectura de ficción es crucial para el desarrollo de la empatía,",
         "reason": "porque permite a los lectores sumergirse en diversas perspectivas y experiencias humanas, ampliando su comprensión emocional.",
         "evidence": "Investigaciones en neurociencia (Science, 2013) han demostrado que la lectura de ficción activa áreas cerebrales relacionadas con la empatía y la teoría de la mente."},
        
        {"thesis": "La regulación estricta de las redes sociales es necesaria para proteger la salud mental de los jóvenes,",
         "reason": "dado que la exposición constante a contenido idealizado y la presión social en línea contribuyen a problemas como la ansiedad y la baja autoestima.",
         "evidence": "La Academia Americana de Pediatría (2024) ha emitido alertas sobre el impacto negativo de las redes sociales en el bienestar psicológico adolescente, citando un aumento en tasas de depresión."},
        
        {"thesis": "La inversión en infraestructura ciclista en las ciudades es una medida eficaz para mejorar la calidad de vida urbana,",
         "reason": "pues reduce la congestión vehicular, la contaminación del aire y promueve un estilo de vida más activo entre los ciudadanos.",
         "evidence": "Ciudades como Copenhague y Ámsterdam, con alta inversión en ciclismo, reportan índices de calidad del aire superiores y menores tasas de enfermedades cardiovasculares en sus poblaciones."},
        
        {"thesis": "La energía geotérmica es una fuente de energía renovable subestimada que merece mayor atención,",
         "reason": "ya que ofrece una fuente constante de energía base, no dependiente del clima, y con una huella de carbono muy baja.",
         "evidence": "Un análisis del Laboratorio Nacional de Energía Renovable de EE. UU. (NREL) proyecta que la geotermia podría abastecer una parte significativa de la demanda eléctrica global de forma continua."},
        
        {"thesis": "El voluntariado es una actividad que beneficia tanto a la comunidad como al individuo,",
         "reason": "puesto que fortalece el tejido social y, a su vez, mejora el bienestar psicológico y la autoestima de quienes lo practican.",
         "evidence": "Un estudio de la Universidad de Harvard (2018) encontró que las personas que realizan voluntariado experimentan niveles significativamente más bajos de estrés y una mayor sensación de propósito."},
        
        {"thesis": "La implementación de una semana laboral de cuatro días podría aumentar la productividad de las empresas,",
         "reason": "porque reduce el agotamiento de los empleados y aumenta su motivación, resultando en un mejor rendimiento en menos tiempo.",
         "evidence": "Pilotos en Islandia y el Reino Unido mostraron que la semana de cuatro días mantuvo o incluso mejoró la productividad, con una reducción notable en el estrés y el 'burnout' de los trabajadores."},
        
        {"thesis": "La preservación de los idiomas indígenas es vital para la diversidad cultural global,",
         "reason": "dado que cada idioma encapsula una forma única de ver el mundo, conocimientos ancestrales y tradiciones irremplazables.",
         "evidence": "La UNESCO estima que un idioma muere cada dos semanas, lo que representa una pérdida invaluable de patrimonio cultural y conocimientos sobre biodiversidad y medicina tradicional."},
        
        {"thesis": "La educación financiera debería ser una materia obligatoria en la escuela secundaria,",
         "reason": "ya que capacita a los jóvenes para tomar decisiones económicas responsables, evitando deudas y fomentando el ahorro desde temprana edad.",
         "evidence": "Países con programas obligatorios de educación financiera, como Canadá, muestran tasas más bajas de endeudamiento juvenil y mayor preparación para la inversión."},
        
        {"thesis": "El consumo consciente de moda es una herramienta poderosa contra la explotación laboral y el impacto ambiental,",
         "reason": "porque al elegir marcas éticas y sostenibles, los consumidores presionan a la industria hacia prácticas más justas y ecológicas.",
         "evidence": "Organizaciones como Fashion Revolution demuestran que la demanda creciente de transparencia y sostenibilidad ha llevado a algunas grandes marcas a revisar sus cadenas de suministro y procesos de producción."},
        
        {"thesis": "Los programas de intercambio estudiantil son esenciales para el desarrollo personal y profesional,",
         "reason": "pues exponen a los estudiantes a nuevas culturas, idiomas y formas de pensamiento, fomentando la adaptabilidad y la tolerancia.",
         "evidence": "Un estudio de Erasmus+ (UE) reveló que los participantes en programas de intercambio tienen una mayor tasa de empleabilidad y una mejor comprensión intercultural que sus pares."},
        
        {"thesis": "Es imperativo invertir en la investigación y desarrollo de vacunas para enfermedades raras,",
         "reason": "porque, aunque afecten a pocos, cada vida tiene el mismo valor y la investigación en estas áreas a menudo produce avances aplicables a enfermedades más comunes.",
         "evidence": "El desarrollo de la terapia génica para enfermedades raras, por ejemplo, ha abierto caminos para tratamientos en patologías con mayor incidencia, demostrando el efecto 'cascada' de esta investigación."},
        
        {"thesis": "La agricultura urbana es una solución prometedora para la seguridad alimentaria en las ciudades,",
         "reason": "ya que reduce la distancia entre el productor y el consumidor, disminuye la huella de carbono del transporte y aumenta el acceso a alimentos frescos.",
         "evidence": "Ciudades como Singapur y Detroit han implementado proyectos de agricultura urbana que han demostrado mejorar la disponibilidad de alimentos y fortalecer las economías locales."},
        
        {"thesis": "La protección de los océanos es una prioridad innegociable para la supervivencia del planeta,",
         "reason": "dado que regulan el clima global, producen gran parte del oxígeno que respiramos y albergan una biodiversidad esencial.",
         "evidence": "El IPCC (Panel Intergubernamental del Cambio Climático) advierte que la acidificación y el calentamiento de los océanos ponen en riesgo la vida marina y alteran patrones climáticos fundamentales."},
        
        {"thesis": "El uso de la gamificación en entornos educativos aumenta significativamente la motivación de los estudiantes,",
         "reason": "porque incorpora elementos de juego como recompensas, desafíos y competición, haciendo el aprendizaje más interactivo y atractivo.",
         "evidence": "Estudios en aulas que aplicaron gamificación reportaron un aumento del 25% en la participación de los estudiantes y una mejora del 15% en la retención de conocimientos en comparación con métodos tradicionales."},
        
        {"thesis": "Los programas de reforestación a gran escala son esenciales para combatir el cambio climático y la pérdida de biodiversidad,",
         "reason": "ya que los árboles absorben dióxido de carbono de la atmósfera y restauran hábitats naturales para la fauna y flora.",
         "evidence": "Iniciativas como el Proyecto Trillion Trees estiman que la reforestación masiva podría capturar una cantidad significativa de emisiones de CO2 y recuperar ecosistemas degradados a nivel global."},
        
        {"thesis": "La adopción de dietas basadas en plantas a nivel global es crucial para la sostenibilidad ambiental,",
         "reason": "porque la producción de carne y productos lácteos tiene una huella de carbono y hídrica mucho mayor que la de vegetales y legumbres.",
         "evidence": "Un estudio de la Universidad de Oxford (2018) publicado en Science concluyó que una dieta vegana es la forma más efectiva de reducir el impacto ambiental personal, disminuyendo las emisiones de gases de efecto invernadero en hasta un 73%."},
        
        {"thesis": "La inteligencia emocional es una habilidad tan importante como la inteligencia académica para el éxito profesional,",
         "reason": "ya que permite gestionar mejor las relaciones interpersonales, resolver conflictos y adaptarse a entornos laborales dinámicos y colaborativos.",
         "evidence": "Empresas como Google han encontrado que las habilidades blandas, incluida la inteligencia emocional, son los predictores más fuertes del éxito de sus empleados, por encima de la experiencia técnica."},
        
        {"thesis": "El arte y la música deben ser disciplinas obligatorias en el currículo escolar,",
         "reason": "porque fomentan la creatividad, la expresión personal y el desarrollo cognitivo integral, habilidades que trascienden lo puramente académico.",
         "evidence": "Investigaciones del Centro para el Cerebro, la Mente y la Música de la Universidad de California muestran que la educación musical, por ejemplo, mejora las habilidades de resolución de problemas y el rendimiento en matemáticas."}
    ]

    random.shuffle(exercises) # Mezclamos los ejercicios

    good_reasons_count = 0
    total_exercises = len(exercises)

    for i, ex in enumerate(exercises):
        print(f"\n--- Ejercicio {i+1} de {total_exercises} ---")
        if run_reason_exercise(ex["thesis"], ex["reason"], ex["evidence"]):
            good_reasons_count += 1
    
    print("\n" * 2)
    print("-" * 70)
    print("¡EJERCICIOS TERMINADOS!")
    print(f"Consideras que diste {good_reasons_count} razones lógicas fuertes de {total_exercises} ejercicios. 🎉")
    print("-" * 70)
    print("¡Has practicado una habilidad crucial para la escritura académica!\n")
    input("Presiona ENTER para volver al menú principal...")

def write_full_argument_academic():
    """Permite al usuario construir un argumento académico completo con tesis, razón, evidencia, contraargumento y refutación."""
    show_header("✍️ ¡Construye Tu Argumento Académico Completo! ✍️")
    print("Es hora de aplicar todo lo aprendido. Construye un argumento completo sobre un tema de tu interés.\n")
    print("Deberás incluir: Tesis, Razón, Evidencia, Contraargumento y tu Refutación.")
    print("Si quieres terminar antes, escribe 'listo' en cualquier momento.\n")

    print("\n--- Tu Argumento ---")
    thesis = input("1. Tu Tesis (tu afirmación principal y debatible): ").strip()
    if thesis.lower() == 'listo': return
    if not thesis: print("Tesis vacía. Intenta de nuevo."); return

    reason = input(f"2. Una Razón Lógica que apoye tu Tesis: ").strip()
    if reason.lower() == 'listo': return
    if not reason: print("Razón vacía. Intenta de nuevo."); return

    evidence = input(f"3. Una Evidencia (dato, estudio, ejemplo) para tu Razón: ").strip()
    if evidence.lower() == 'listo': return
    if not evidence: print("Evidencia vacía. Intenta de nuevo."); return

    counterargument = input(f"4. Un Contraargumento (una objeción) a tu Tesis/Razón: ").strip()
    if counterargument.lower() == 'listo': return
    if not counterargument: print("Contraargumento vacío. Intenta de nuevo."); return

    refutation = input(f"5. Tu Refutación a ese Contraargumento: ").strip()
    if refutation.lower() == 'listo': return
    if not refutation: print("Refutación vacía. Intenta de nuevo."); return
    
    print("\n--- Tu Argumento Académico Construido ---")
    print(f"Tesis: '{thesis}'")
    print(f"  Razón: '{reason}'")
    print(f"    Evidencia: '{evidence}'")
    print(f"  Contraargumento: '{counterargument}'")
    print(f"    Refutación: '{refutation}'")
    print("\n¡IMPRESIONANTE! Has dominado la estructura del argumento académico. ¡Estás listo para el nivel universitario! 🎓\n")
    
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: La Estructura del Argumento Académico (12º Grado)")
        print("1. Aprender la Teoría")
        print("2. Ver Ejemplos")
        print("3. Hacer Ejercicios (Tesis y Razones)")
        print("4. Construir Mi Propio Argumento Académico Completo")
        print("5. Salir de la Lección")
        print("-" * 70)

        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            show_theory()
        elif choice == '2':
            show_examples()
        elif choice == '3':
            start_exercises()
        elif choice == '4':
            write_full_argument_academic()
        elif choice == '5':
            print("¡Hasta pronto! Sigue construyendo argumentos sólidos para tu futuro académico. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
