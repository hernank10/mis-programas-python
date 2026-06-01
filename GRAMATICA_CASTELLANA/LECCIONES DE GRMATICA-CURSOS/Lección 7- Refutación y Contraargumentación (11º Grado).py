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
    print(f"🛡️ {title.upper()} 🛡️")
    print("-" * 60)
    print()

def show_theory():
    """Muestra la sección de teoría sobre refutación y contraargumentación."""
    show_header("Teoría: Refutación y Contraargumentación")
    print("¡Hola! En grados anteriores, aprendimos a construir tesis y a dar razones con evidencia.")
    print("Hoy subiremos un nivel: vamos a aprender a **dialogar con otros argumentos**, incluso si son contrarios.\n")
    
    print("⭐ 1. CONTRAARGUMENTO:")
    print("   Es un argumento que se presenta para **oponerse o contradecir** una tesis o un argumento previo.")
    print("   Es pensar en '¿Qué diría alguien que no está de acuerdo conmigo?'\n")
    print("   Ejemplo de Tesis: 'La educación en línea es superior a la presencial.'")
    print("   Contraargumento: 'Sin embargo, la educación presencial fomenta una mejor interacción social y oportunidades de networking.'\n")
    
    print("⭐ 2. REFUTACIÓN:")
    print("   Es la acción de **desmentir, invalidar o demostrar la falsedad** de un argumento o contraargumento.")
    print("   No basta con presentar el contraargumento; hay que explicar por qué NO es tan fuerte o por qué tu argumento principal SIGUE SIENDO VÁLIDO a pesar de la objeción.")
    print("   Pregunta clave: '¿Por qué ese contraargumento no invalida mi tesis?'\n")
    print("   Ejemplo (continuando el anterior):")
    print("   Tesis: 'La educación en línea es superior a la presencial.'")
    print("   Contraargumento: 'Sin embargo, la educación presencial fomenta una mejor interacción social y oportunidades de networking.'")
    print("   Refutación: 'Si bien es cierto que la interacción física es valiosa, las plataformas en línea actuales ofrecen herramientas avanzadas de colaboración y foros que, aunque diferentes, permiten construir redes y habilidades de comunicación digital, esenciales en el mundo actual.'\n")
    
    print("La refutación fortalece tu propio argumento porque demuestras que has considerado otras perspectivas y puedes defender tu posición de manera integral.\n")
    input("Presiona ENTER para ver ejemplos...")

def show_examples():
    """Muestra ejemplos de tesis, contraargumentos y refutaciones."""
    show_header("Ejemplos: Construyendo Refutaciones")
    
    examples = [
        {
            "thesis": "Es fundamental prohibir el uso de teléfonos móviles en el aula para mejorar la concentración.",
            "counterargument": "Algunos argumentan que los móviles son herramientas útiles para la investigación y el aprendizaje.",
            "refutation": "Si bien los móviles pueden ser una herramienta, su uso incontrolado genera distracciones constantes, y las escuelas pueden proveer tabletas o computadoras con fines educativos, sin los riesgos de interrupción personal de los móviles."
        },
        {
            "thesis": "La inteligencia artificial traerá más beneficios que perjuicios a la sociedad.",
            "counterargument": "Hay quienes temen que la IA cause una pérdida masiva de empleos y una brecha social.",
            "refutation": "Aunque la IA transformará el mercado laboral, también generará nuevas profesiones y una mayor eficiencia en muchos sectores, permitiendo a los humanos enfocarse en tareas más creativas y de mayor valor si se invierte en reentrenamiento laboral."
        },
        {
            "thesis": "El consumo de carne debería reducirse globalmente por razones ambientales.",
            "counterargument": "Otros señalan que la ganadería es una fuente vital de ingresos para muchas comunidades y una parte integral de la cultura alimentaria.",
            "refutation": "Aunque la ganadería sostiene a muchas familias, existen alternativas económicas y nutricionales sostenibles, como la agricultura orgánica o las proteínas vegetales, que podrían adoptarse gradualmente para mitigar el impacto ambiental sin erradicar las tradiciones."
        }
    ]

    print("Analicemos cómo se construye la refutación:\n")
    for ex in examples:
        print(f"Tesis: '{ex['thesis']}'")
        print(f"  Contraargumento: '{ex['counterargument']}'")
        print(f"  Refutación: '{ex['refutation']}'\n")
        print("-" * 60)
        time.sleep(4) # Pausa para que el estudiante procese

    print("\n¡Ahora es tu turno de practicar la refutación!\n")
    input("Presiona ENTER para ir a los ejercicios...")

def run_refutation_exercise(thesis, counterargument, model_refutation):
    """Ejecuta un solo ejercicio de refutación."""
    print("\n" + "-" * 60)
    print("Tienes la siguiente situación:")
    print(f"Tesis: '{thesis}'")
    print(f"Contraargumento: '{counterargument}'")
    print("\nTu turno: Escribe una **refutación** a este contraargumento.")
    print("Demuestra por qué el contraargumento no invalida la tesis principal.")
    
    user_refutation = input("\nTu Refutación: ").strip()

    print("\n--- Refutación Modelo ---")
    print(f"Una posible refutación sería: '{model_refutation}'")
    
    while True:
        evaluation = input("\n¿Consideras que tu refutación fue fuerte y lógica? (s/n): ").lower().strip()
        if evaluation == 's':
            print("¡Muy bien! Estás desarrollando un pensamiento crítico avanzado.")
            return True
        elif evaluation == 'n':
            print("Está bien, sigue practicando. Comparar con el modelo te ayudará a mejorar.")
            return False
        else:
            print("Respuesta no válida. Elige 's' para sí o 'n' para no.")
    print("-" * 60)
    time.sleep(3) # Pausa para que el usuario lea el feedback

def start_exercises():
    """Inicia la sección de ejercicios de refutación."""
    show_header("¡A Practicar! Refutación y Contraargumentación")
    print("Para cada ejercicio, te daré una Tesis y un Contraargumento.")
    print("Tu tarea es escribir una **REFUTACIÓN**.\n")

    exercises = [
        {
            "thesis": "Las redes sociales han mejorado la comunicación global.",
            "counterargument": "Algunos dicen que las redes sociales aíslan a las personas y reducen la interacción cara a cara.",
            "refutation": "Si bien las interacciones presenciales son importantes, las redes sociales permiten mantener contacto con personas a distancia y facilitan la conexión con comunidades con intereses afines, superando barreras geográficas que antes eran insalvables."
        },
        {
            "thesis": "La energía solar es la mejor alternativa para el futuro energético.",
            "counterargument": "Se argumenta que la energía solar es intermitente y requiere grandes superficies para su producción.",
            "refutation": "Aunque es cierto que la producción solar depende de la luz solar y del espacio, los avances en almacenamiento de energía (baterías) y en la eficiencia de los paneles, junto con la instalación en techos y espacios no cultivables, están resolviendo estas limitaciones, haciéndola cada vez más viable."
        },
        {
            "thesis": "Es esencial que los jóvenes aprendan a programar desde temprana edad.",
            "counterargument": "Hay quienes creen que programar es una habilidad muy específica que no todos necesitan.",
            "refutation": "Si bien no todos serán programadores, aprender a programar desarrolla el pensamiento lógico, la resolución de problemas y la creatividad, habilidades transferibles y fundamentales para cualquier carrera en el siglo XXI, independientemente del campo."
        },
        {
            "thesis": "Las ciudades deberían priorizar el transporte público sobre el uso de vehículos privados.",
            "counterargument": "Algunos usuarios prefieren la comodidad y flexibilidad del coche privado.",
            "refutation": "Aunque la comodidad individual es un factor, priorizar el transporte público reduce la congestión, la contaminación y el estrés vial, beneficiando a la mayoría de los ciudadanos y haciendo las ciudades más habitables para todos."
        },
        {
            "thesis": "La inteligencia artificial no podrá reemplazar la creatividad humana.",
            "counterargument": "Se ha demostrado que la IA puede generar arte, música y textos que parecen creativos.",
            "refutation": "Si bien la IA puede imitar y recombinar patrones existentes para crear 'arte', su creatividad es algorítmica y carece de la intencionalidad, la emoción y la capacidad de experiencia subjetiva que impulsan la verdadera creatividad humana."
        },
        {
            "thesis": "Los videojuegos con fines educativos son una herramienta pedagógica muy eficaz.",
            "counterargument": "Críticos señalan que el tiempo frente a la pantalla es perjudicial para la salud y el desarrollo social.",
            "refutation": "Aunque el tiempo excesivo de pantalla es un riesgo, los videojuegos educativos, usados con moderación, aprovechan el enganche y la interactividad para enseñar de forma lúdica, mejorando la motivación y la retención de conocimientos más allá de lo que un libro de texto tradicional puede lograr."
        },
        {
            "thesis": "La exploración espacial es una inversión valiosa para la humanidad.",
            "counterargument": "Hay quienes argumentan que esos fondos deberían usarse para resolver problemas en la Tierra.",
            "refutation": "Aunque es vital abordar los problemas terrestres, la inversión en exploración espacial genera avances tecnológicos (como materiales o medicina) que benefician directamente a la vida en la Tierra, además de inspirar a futuras generaciones de científicos e ingenieros."
        },
        {
            "thesis": "El aprendizaje autodirigido (sin profesor) es más efectivo para muchos estudiantes.",
            "counterargument": "Se dice que el profesor es esencial para guiar y motivar a los estudiantes.",
            "refutation": "Si bien la guía de un profesor es útil, el aprendizaje autodirigido fomenta la autonomía, la curiosidad intrínseca y la capacidad de buscar información de forma independiente, habilidades clave para el aprendizaje continuo en la vida adulta, que un entorno puramente guiado no siempre desarrolla."
        },
        {
            "thesis": "Las dietas vegetarianas son más saludables que las que incluyen carne.",
            "counterargument": "Algunos nutricionistas advierten que una dieta vegetariana puede carecer de ciertos nutrientes si no está bien planificada.",
            "refutation": "Aunque es cierto que una dieta vegetariana requiere planificación para asegurar todos los nutrientes, una dieta balanceada basada en plantas, rica en legumbres, frutos secos y vegetales, no solo provee todos los nutrientes necesarios sino que también reduce el riesgo de enfermedades cardíacas y obesidad, superando los beneficios de una dieta omnívora promedio."
        },
        {
            "thesis": "La globalización ha beneficiado principalmente a los países desarrollados.",
            "counterargument": "Se argumenta que la globalización ha sacado a millones de personas de la pobreza en países en desarrollo.",
            "refutation": "Si bien la globalización ha impulsado el crecimiento económico en algunas regiones en desarrollo, este crecimiento a menudo ha venido acompañado de una mayor desigualdad interna, explotación laboral y degradación ambiental, con beneficios desproporcionados para las grandes corporaciones y los países más ricos."
        },
        {
            "thesis": "El voto electrónico debería implementarse para modernizar las elecciones.",
            "counterargument": "Expertos en seguridad informática advierten sobre los riesgos de manipulación y falta de transparencia del voto electrónico.",
            "refutation": "Aunque la seguridad es una preocupación legítima, con las tecnologías de encriptación y los sistemas de auditoría adecuados (como el blockchain), el voto electrónico podría ser más seguro y auditable que los sistemas manuales actuales, además de facilitar la participación y reducir costos logísticos."
        },
        {
            "thesis": "Es fundamental que los gobiernos inviertan más en arte y cultura.",
            "counterargument": "Algunos piensan que hay necesidades más urgentes, como la salud o la educación.",
            "refutation": "Si bien la salud y la educación son prioritarias, la inversión en arte y cultura no es un gasto, sino una inversión en el desarrollo integral de la sociedad. Fomenta la identidad, la creatividad, el turismo y la cohesión social, contribuyendo al bienestar tanto como los servicios básicos."
        },
        {
            "thesis": "La pena de muerte no es una medida de justicia efectiva.",
            "counterargument": "Partidarios de la pena de muerte argumentan que disuade a futuros criminales.",
            "refutation": "A pesar de la creencia en su efecto disuasorio, estudios en diversos países no han demostrado una correlación directa entre la existencia de la pena de muerte y una disminución significativa de la criminalidad, lo que sugiere que no es un factor determinante en la prevención de delitos."
        },
        {
            "thesis": "La educación universitaria debería ser gratuita para todos.",
            "counterargument": "Se objeta que la gratuidad podría saturar las universidades y bajar la calidad educativa.",
            "refutation": "Aunque la masificación es un riesgo, un sistema de universidades gratuitas y bien financiadas, con criterios de admisión claros y programas de apoyo, permitiría a más talentos acceder a la educación superior sin barreras económicas, elevando el nivel educativo general y no necesariamente la calidad."
        },
        {
            "thesis": "Las redes sociales son más perjudiciales que beneficiosas para la salud mental.",
            "counterargument": "Algunos defienden que las redes sociales ofrecen apoyo comunitario y reducen la sensación de soledad.",
            "refutation": "Si bien pueden ofrecer apoyo en ciertas situaciones, el uso problemático de las redes sociales está asociado con mayores tasas de ansiedad, depresión y baja autoestima, superando los beneficios potenciales de conexión, especialmente entre los adolescentes, debido a la presión social y la comparación constante."
        },
        {
            "thesis": "Los coches eléctricos son la solución definitiva para la crisis climática.",
            "counterargument": "Se señala que la producción de baterías y la generación de electricidad para cargarlos también tienen un impacto ambiental.",
            "refutation": "Aunque la producción de baterías y la generación de electricidad aún tienen una huella, la tendencia es hacia baterías más sostenibles y una matriz energética basada en renovables. A largo plazo, los coches eléctricos son mucho más eficientes y emiten menos gases de efecto invernadero en su ciclo de vida que los de combustión, representando una mejora neta."
        },
        {
            "thesis": "Es esencial regular estrictamente las grandes empresas tecnológicas para proteger la privacidad de los usuarios.",
            "counterargument": "Las empresas tecnológicas argumentan que la regulación excesiva frena la innovación y el desarrollo.",
            "refutation": "Si bien la innovación es importante, una regulación adecuada de la privacidad no la frena, sino que establece un marco de confianza. Sin regulación, el poder de recolección de datos de estas empresas puede llevar a abusos, discriminación y manipulación, haciendo de la protección de datos un derecho fundamental por encima de la pura 'innovación'."
        },
        {
            "thesis": "La telemedicina debería ser el estándar para la atención médica primaria.",
            "counterargument": "Se objeta que la telemedicina no permite el examen físico completo ni la conexión personal con el médico.",
            "refutation": "Aunque el examen físico y la conexión personal son valiosos, la telemedicina ofrece mayor accesibilidad (especialmente en zonas rurales), reduce tiempos de espera y costos, y es ideal para el seguimiento de enfermedades crónicas o consultas no urgentes, liberando recursos para los casos que sí requieren atención presencial."
        },
        {
            "thesis": "Los plásticos de un solo uso deberían ser prohibidos globalmente.",
            "counterargument": "La industria argumenta que los plásticos son baratos, versátiles y esenciales en muchas aplicaciones, incluyendo la higiene y la medicina.",
            "refutation": "Si bien los plásticos son útiles en ciertos contextos (como la medicina), su uso masivo en productos desechables causa una contaminación ambiental insostenible. Existen alternativas reutilizables y materiales biodegradables para la mayoría de los usos de un solo uso, lo que demuestra que su prohibición es viable y necesaria."
        },
        {
            "thesis": "El consumo de contenido digital (series, películas) es mejor que la lectura de libros.",
            "counterargument": "Los defensores de los libros argumentan que la lectura profunda estimula más la imaginación y el pensamiento crítico.",
            "refutation": "Aunque el contenido digital ofrece estimulación visual y auditiva inmediata, la lectura de libros requiere un procesamiento mental más activo, construye el vocabulario de forma más rica, y desarrolla la capacidad de concentración y el pensamiento crítico de una manera que el consumo pasivo de medios audiovisuales no puede igualar completamente, siendo habilidades complementarias pero no equivalentes."
        },
    ]

    random.shuffle(exercises) # Mezclamos los ejercicios

    good_refutations_count = 0
    total_exercises = len(exercises)

    for i, ex in enumerate(exercises):
        print(f"\n--- Ejercicio {i+1} de {total_exercises} ---")
        if run_refutation_exercise(ex["thesis"], ex["counterargument"], ex["refutation"]):
            good_refutations_count += 1
    
    print("\n" * 2)
    print("-" * 60)
    print("¡EJERCICIOS TERMINADOS!")
    print(f"Consideras que diste {good_refutations_count} refutaciones fuertes de {total_exercises} ejercicios. 🎉")
    print("-" * 60)
    print("¡Has practicado una habilidad clave para la argumentación avanzada!\n")
    input("Presiona ENTER para volver al menú principal...")

def write_full_argument_with_refutation():
    """Permite al usuario construir un argumento completo con tesis, razón, evidencia y refutación."""
    show_header("✍️ ¡Crea un Argumento Completo con Refutación! ✍️")
    print("Ahora es tu turno de crear un argumento complejo sobre un tema que te interese.\n")
    print("1. Escribe tu TESIS (tu afirmación principal).")
    print("2. Da una RAZÓN que la apoye.")
    print("3. Incluye una EVIDENCIA (dato, estudio, ejemplo) que refuerce tu razón.")
    print("4. Piensa en un CONTRAARGUMENTO (una objeción a tu tesis o razón).")
    print("5. Escribe una REFUTACIÓN a ese contraargumento.\n")
    print("Si quieres terminar antes, escribe 'listo' en cualquier momento.\n")

    print("\n--- Tu Argumento ---")
    thesis = input("1. Tu Tesis: ").strip()
    if thesis.lower() == 'listo': return
    if not thesis: print("Tesis vacía. Intenta de nuevo."); return

    reason = input(f"2. Una Razón para '{thesis}': ").strip()
    if reason.lower() == 'listo': return
    if not reason: print("Razón vacía. Intenta de nuevo."); return

    evidence = input(f"3. Una Evidencia para '{reason}': ").strip()
    if evidence.lower() == 'listo': return
    if not evidence: print("Evidencia vacía. Intenta de nuevo."); return

    counterargument = input(f"4. Un Contraargumento a tu tesis/razón: ").strip()
    if counterargument.lower() == 'listo': return
    if not counterargument: print("Contraargumento vacío. Intenta de nuevo."); return

    refutation = input(f"5. Tu Refutación al contraargumento: ").strip()
    if refutation.lower() == 'listo': return
    if not refutation: print("Refutación vacía. Intenta de nuevo."); return
    
    print("\n--- Tu Argumento Construido ---")
    print(f"Tesis: '{thesis}'")
    print(f"Razón: '{reason}'")
    print(f"Evidencia: '{evidence}'")
    print(f"Contraargumento: '{counterargument}'")
    print(f"Refutación: '{refutation}'")
    print("\n¡Felicitaciones! Has construido un argumento completo y sofisticado. ¡Esta es una habilidad preuniversitaria crucial!\n")
    
    input("Presiona ENTER para volver al menú principal...")


def show_main_menu():
    """Muestra el menú principal de la aplicación."""
    while True:
        show_header("Lección 7: Refutación y Contraargumentación (11º Grado)")
        print("1. Aprender la Teoría")
        print("2. Ver Ejemplos")
        print("3. Hacer Ejercicios (Refutación)")
        print("4. Construir Mi Propio Argumento Completo con Refutación")
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
            write_full_argument_with_refutation()
        elif choice == '5':
            print("¡Hasta pronto! Sigue perfeccionando tu argumentación. 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu()
