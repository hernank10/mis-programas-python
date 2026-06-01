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
    print(f"🗣️ {title.upper()} ✍️")
    print("=" * 100)
    print()

def show_introduction_l9_10th():
    """Introduce los conceptos de retórica avanzada para 10º Grado."""
    show_header("Introducción: ¡Maestros de la Persuasión!")
    print("¡Bienvenidos, futuros oradores y pensadores críticos de élite! 🚀")
    print("En 9.º Grado, aprendieron a desentrañar la organización y a construir argumentos sólidos. ¡Ahora, en 10.º, es hora de DOMINAR la persuasión!\n")
    
    print("Nos sumergiremos en las técnicas que los grandes oradores y escritores usan para mover mentes y corazones. Aprenderán a no solo construir argumentos lógicos, sino a imbuirlos de fuerza emocional y credibilidad inquebrantable.\n")
    
    print("En esta lección, ustedes serán capaces de:")
    print("   ✅ **Aplicar conscientemente** Ethos, Pathos y Logos en sus propios discursos.")
    print("   ✅ **Diseñar argumentos complejos** usando modelos avanzados como el de Toulmin.")
    print("   ✅ **Anticipar y neutralizar** objeciones y falacias lógicas de manera proactiva.")
    print("   ✅ **Adaptar su estrategia retórica** a diferentes audiencias y contextos con maestría.\n")
    
    print("¡Prepárense para influir, convencer y liderar con la palabra!\n")
    input("Presiona ENTER para comenzar nuestra inmersión...")

def show_rhetorical_appeals_concept():
    """Explica el dominio de Ethos, Pathos, Logos en la práctica."""
    show_header("Dominio de Apelaciones Retóricas (Ethos, Pathos, Logos)")
    print("En 10.º Grado, no solo identificamos Ethos, Pathos y Logos, ¡los usamos estratégicamente!\n")
    
    print("--- **Ethos (Credibilidad)** ---")
    print("  * **Uso:** Construir confianza y autoridad.")
    print("  * **Estrategias de Organización:**")
    print("    * **Inicio del discurso:** Presentar cualificaciones, experiencia, valores compartidos.")
    print("    * **Integración de fuentes:** Citar expertos respetados al principio de una sección para validar un punto.")
    print("    * **Reconocimiento de limitaciones:** Mostrar humildad o conocimiento de la complejidad de un tema para parecer más objetivo.\n")

    print("--- **Pathos (Emoción)** ---")
    print("  * **Uso:** Conectar con la audiencia a un nivel emocional.")
    print("  * **Estrategias de Organización:**")
    print("    * **Introducción:** Usar anécdotas o historias impactantes para captar la atención emocional.")
    print("    * **Cuerpo del argumento:** Presentar ejemplos vívidos o testimonios personales en momentos clave para reforzar la conexión emocional.")
    print("    * **Conclusión:** Apelar a valores compartidos o un llamado a la acción que resuene emocionalmente.\n")

    print("--- **Logos (Lógica)** ---")
    print("  * **Uso:** Apelar a la razón y la evidencia.")
    print("  * **Estrategias de Organización:**")
    print("    * **Cuerpo del argumento:** Presentar evidencia (estadísticas, hechos, estudios) de forma clara y estructurada (ej. de lo general a lo específico).")
    print("    * **Causa y Efecto:** Organizar la información para mostrar relaciones lógicas claras.")
    print("    * **Problema-Solución:** Presentar el problema con datos y luego la solución lógica.\n")
    
    print("¡Dominar estas apelaciones en la organización te hace un persuasor efectivo!\n")
    input("Presiona ENTER para explorar estructuras argumentativas complejas...")

def show_complex_structures_concept():
    """Explica estructuras argumentativas complejas como Toulmin y Rogerian."""
    show_header("Estructuras Argumentativas Complejas (Toulmin, Rogerian)")
    print("Más allá de lo básico, las estructuras complejas te permiten argumentar con matices y profundidad.\n")
    
    print("--- **Modelo de Toulmin** ---")
    print("  * **Objetivo:** Analizar la lógica de un argumento de forma detallada.")
    print("  * **Componentes:**")
    print("    1.  **Aserción (Claim):** Tu punto principal o conclusión.")
    print("    2.  **Datos (Data):** La evidencia que apoya la aserción.")
    print("    3.  **Garantía (Warrant):** La lógica o principio que conecta los datos con la aserción (¿por qué los datos son relevantes?).")
    print("    4.  **Respaldo (Backing):** Evidencia adicional que apoya la garantía.")
    print("    5.  **Refutación (Rebuttal):** Reconocimiento de las objeciones y una respuesta a ellas.")
    print("    6.  **Cualificador (Qualifier):** El grado de certeza de la aserción (ej. 'probablemente', 'usualmente', 'en la mayoría de los casos').")
    print("  * **Organización:** No es lineal. Puedes presentar tu aserción, luego los datos, la garantía, y entrelazar refutaciones y cualificadores donde sean necesarios para un argumento exhaustivo.\n")

    print("--- **Argumento Rogerian (Orientado al Consenso)** ---")
    print("  * **Objetivo:** Reducir la hostilidad y encontrar un terreno común, especialmente en temas polarizados.")
    print("  * **Organización (Secuencia Típica):**")
    print("    1.  **Introducción:** Presentar el problema de forma neutral y sin juicios.")
    print("    2.  **Entendimiento de la Perspectiva Opuesta:** Explicar el punto de vista del oponente de forma justa y empática, demostrando que lo entiendes.")
    print("    3.  **Identificación de Terreno Común:** Destacar los puntos en los que ambos lados pueden estar de acuerdo o compartir valores.")
    print("    4.  **Presentación de tu Perspectiva:** Exponer tu propio argumento, mostrando cómo es beneficioso para ambas partes o cómo es una solución superior que considera las preocupaciones del otro lado.")
    print("    5.  **Conclusión:** Un llamado a la colaboración o a una solución mutuamente beneficiosa que integra ambos puntos de vista.\n")
    
    print("Estas estructuras te permiten construir argumentos más sofisticados y persuasivos.\n")
    input("Presiona ENTER para aprender a anticipar y neutralizar objeciones...")

def show_fallacies_and_adaptation_concept():
    """Explica la anticipación de falacias y la adaptación retórica."""
    show_header("Anticipación y Neutralización de Contrapuntos y Falacias Lógicas")
    print("Un gran persuasor no solo argumenta, ¡también se defiende y adapta su mensaje!\n")
    
    print("--- **Anticipación y Neutralización de Contrapuntos:** ---")
    print("  * **Proactividad:** No esperes que te presenten objeciones; incorpóralas y desmantélalas *dentro* de tu propio argumento.")
    print("  * **Estrategias de Organización:**")
    print("    * **'Steel-manning':** Presenta el argumento del oponente en su versión más fuerte *antes* de refutarlo. Demuestra comprensión y aumenta tu credibilidad.")
    print("    * **Inclusión Temprana:** Si una objeción es muy fuerte, abórdala al principio para despejar el camino para tu argumento principal.")
    print("    * **Análisis de Consecuencias:** Muestra cómo el contrapunto o la objeción llevaría a resultados negativos o ilógicos.\n")

    print("--- **Identificación y Refutación de Falacias Lógicas:** ---")
    print("  * Las falacias son errores de razonamiento. Identificarlas fortalece tu crítica. Ejemplos:")
    print("    * **Ad Hominem:** Atacar a la persona, no al argumento. (Ej. 'No escuches a X, él es un fracasado.')")
    print("    * **Hombre de Paja:** Caricaturizar o distorsionar el argumento del oponente para que sea más fácil refutarlo. (Ej. 'Ellos quieren que vivamos en cuevas sin tecnología.')")
    print("    * **Apelación a la Autoridad Irrelevante:** Usar la opinión de una autoridad que no es experta en el tema. (Ej. 'Mi actor favorito dice que esta dieta es la mejor.')")
    print("    * **Falsa Causa:** Asumir que porque un evento sigue a otro, el primero causó el segundo. (Ej. 'Desde que usé esta camisa, mi equipo siempre gana.')")
    print("  * **Organización de Refutación:** 1) Identifica la falacia, 2) Explica por qué es una falacia, 3) Re-enfoca el debate en la lógica y evidencia.\n")

    print("--- **Adaptación Retórica a la Audiencia y el Contexto:** ---")
    print("  * **Audiencia Favorable:** Organiza para reforzar creencias y motivar a la acción (más Pathos y Ethos compartido).")
    print("  * **Audiencia Escéptica/Hostil:** Empieza con terreno común (Rogerian), usa más Logos y Ethos, evita confrontaciones directas al inicio.")
    print("  * **Contexto (Oral vs. Escrito):**")
    print("    * **Oral:** Más repetición, frases cortas, pausas, énfasis en Pathos y Ethos inmediatos.")
    print("    * **Escrito:** Más detalle, estructura visual (párrafos, títulos), citas extensas, más énfasis en Logos detallado.")
    print("  * **Organización para el Debate:** Estructura para presentar tu caso, refutar al oponente, y resumir tu posición, todo dentro de límites de tiempo estrictos.\n")
    
    print("¡La adaptabilidad es clave para la persuasión maestra!\n")
    input("Presiona ENTER para nuestros ejercicios avanzados...")

# --- NUEVOS EJERCICIOS PARA LECCIÓN 9 (10.º Grado) ---

def exercise_analyze_rhetorical_discourse():
    """Ejercicio: Analiza un discurso retórico (Ethos, Pathos, Logos y organización)."""
    show_header("Ejercicio: ¡Analiza el Discurso Retórico!")
    print("Lee el siguiente extracto de un discurso. Tu tarea es identificar cómo se utilizan Ethos, Pathos, Logos y cómo la organización de las ideas contribuye (o no) a la persuasión.\n")

    discourses = [
        {"title": "Extracto de un Discurso Político",
         "text": "Compatriotas, les hablo hoy no como un político, sino como un padre que ve el futuro de sus hijos amenazado. Hemos presenciado cómo nuestras industrias languidecen por políticas miopes, dejando a miles sin sustento. Es una verdad innegable que cada cifra de desempleo representa una familia con menos esperanza. Por eso, mi propuesta, basada en rigurosos estudios económicos, es la única vía lógica para revitalizar nuestra nación. ¡Unámonos por un futuro próspero y seguro!",
         "analysis_guide": {
             "ethos": "El orador construye Ethos al inicio: 'no como un político, sino como un padre' (apela a la moralidad y experiencia común), y más adelante con 'basada en rigurosos estudios económicos' (apela a la credibilidad experta).",
             "pathos": "Fuerte uso de Pathos: 'futuro de sus hijos amenazado', 'industrias languidecen', 'miles sin sustento', 'familia con menos esperanza'. Usa un lenguaje emocional para conectar.",
             "logos": "Uso limitado de Logos en el extracto: 'cifra de desempleo' y 'rigurosos estudios económicos' son menciones, pero no se presentan los datos concretos. Se asume que la propuesta es 'la única vía lógica' sin detallar la lógica.",
             "organization": "La organización comienza con Pathos (conexión emocional y personal), pasa a plantear el 'problema' con más Pathos, luego presenta una solución con una ligera apelación a Logos (estudios) y concluye con un llamado a la acción emocional. Prioriza la conexión y el impacto emocional sobre el detalle lógico en este extracto."
         }},
        {"title": "Extracto de un Editorial Científico",
         "text": "La evidencia acumulada durante décadas, proveniente de miles de estudios revisados por pares, demuestra inequívocamente que el cambio climático es un fenómeno acelerado por la actividad humana. Los datos satelitales confirman un aumento sostenido de la temperatura global, correlacionado directamente con los niveles de CO2 atmosférico. Quienes insisten en que 'es un ciclo natural' ignoran la magnitud y velocidad de los cambios actuales, los cuales superan con creces cualquier fluctuación histórica. La inacción actual tendrá repercusiones severas, no solo ecológicas, sino socioeconómicas demostrables.",
         "analysis_guide": {
             "ethos": "Construye Ethos con 'evidencia acumulada durante décadas', 'miles de estudios revisados por pares', 'datos satelitales'. Apela a la autoridad de la ciencia y la comunidad investigadora.",
             "pathos": "Uso muy limitado de Pathos, se enfoca en la objetividad: 'repercusiones severas' es lo más cercano a una apelación emocional, pero se acompaña de 'socioeconómicas demostrables', manteniendo un tono racional.",
             "logos": "Fuerte uso de Logos: 'evidencia acumulada', 'datos sateliales confirman aumento sostenido', 'correlacionado directamente con niveles de CO2'. Refuta directamente un contrapunto ('es un ciclo natural') usando lógica y evidencia ('superan con creces cualquier fluctuación histórica').",
             "organization": "La organización es deductiva, iniciando con la aserción respaldada por Logos (evidencia científica), luego refuta directamente el contrapunto popular con más Logos. Termina con las consecuencias, manteniendo un tono de advertencia basado en la lógica. Prioriza la lógica y la evidencia sobre la emoción."
         }}
    ]
    
    random.shuffle(discourses)

    for i, d in enumerate(discourses):
        print(f"\n--- Extracto {i+1} de {len(discourses)}: {d['title']} ---")
        print(f"'{d['text']}'\n")
        
        print("Tu turno de analizar:")
        print("1. ¿Dónde ves el uso de **Ethos** (credibilidad)?")
        ethos_analysis = input(" > Tu análisis de Ethos: ").strip()
        
        print("\n2. ¿Dónde ves el uso de **Pathos** (emoción)?")
        pathos_analysis = input(" > Tu análisis de Pathos: ").strip()
        
        print("\n3. ¿Dónde ves el uso de **Logos** (lógica/evidencia)?")
        logos_analysis = input(" > Tu análisis de Logos: ").strip()

        print("\n4. ¿Cómo la **organización** de este texto contribuye a su persuasión? (Ej. ¿Qué se dice primero, qué se refuta, cómo se presentan los argumentos?)")
        org_analysis = input(" > Tu análisis de organización: ").strip()
        
        print("\n--- Análisis Experto ---")
        print(f"**Ethos:** {d['analysis_guide']['ethos']}")
        print(f"**Pathos:** {d['analysis_guide']['pathos']}")
        print(f"**Logos:** {d['analysis_guide']['logos']}")
        print(f"**Organización:** {d['analysis_guide']['organization']}")
        print(f"\nTu análisis de Ethos: '{ethos_analysis}'")
        print(f"Tu análisis de Pathos: '{pathos_analysis}'")
        print(f"Tu análisis de Logos: '{logos_analysis}'")
        print(f"Tu análisis de Organización: '{org_analysis}'")
        print("\n¡Compara tu análisis con la guía! Recuerda que estas apelaciones a menudo trabajan juntas.\n")
        input("Presiona ENTER para el siguiente extracto o para terminar este ejercicio...")
    
    print("\nEjercicio terminado. ¡Has practicado el análisis retórico avanzado! 🗣️")
    input("Presiona ENTER para el siguiente paso...")

def exercise_construct_structured_argument():
    """Ejercicio: Construye un argumento estructurado (Modelo de Toulmin o similar)."""
    show_header("Ejercicio: ¡Construye un Argumento Estructurado!")
    print("Vamos a practicar la construcción de un argumento complejo usando una estructura más avanzada (piensa en el Modelo de Toulmin).\n")
    
    print("Tema: **'La implementación de más zonas verdes urbanas'** debería ser una prioridad para las ciudades.")
    
    print("\nConsidera los siguientes elementos que podrías usar:")
    print("  * **Dato/Evidencia:** Estudios demuestran que el acceso a la naturaleza reduce el estrés en residentes urbanos.")
    print("  * **Dato/Evidencia:** Las zonas verdes contribuyen a la calidad del aire y la biodiversidad.")
    print("  * **Contrapunto/Objeción:** Construir zonas verdes es costoso y reduce el espacio para viviendas o negocios.")
    print("  * **Garantía (conexión lógica):** El bienestar mental y físico de los ciudadanos es fundamental para una sociedad productiva.")
    print("  * **Cualificador:** 'Generalmente', 'en la mayoría de los casos'.")
    print("  * **Respaldo para la garantía:** Datos de salud pública sobre el impacto del estrés en la productividad.")
    
    print("\nTu tarea es escribir un párrafo persuasivo (8-10 oraciones) que:\n")
    print("  1. Presente la **aserción** principal (tu punto principal).")
    print("  2. Incorpore **al menos dos datos/evidencias** de la lista.")
    print("  3. Incluya la **garantía** y, si puedes, una mención a su **respaldo**.")
    print("  4. Aborde proactivamente el **contrapunto/objeción** y lo neutralice o refute brevemente.")
    print("  5. Utilice un **cualificador** para su aserción.\n")
    
    print("Escribe tu argumento aquí:")
    user_argument = ""
    print("(Presiona ENTER dos veces para terminar tu párrafo):")
    while True:
        line = input()
        if not line:
            break
        user_argument += line + "\n"
    user_argument = user_argument.strip()

    print("\n--- ¡Tu Argumento Estructurado! ---")
    print(user_argument)

    print("\n--- Reflexión Guiada ---")
    print("Ahora, revisa tu propio trabajo con los ojos de un analista:")
    print("1. **Aserción Clara:** ¿Tu punto principal es inequívoco? ¿Está cualificado?")
    input("> Tu reflexión: ").strip()

    print("\n2. **Conexión Lógica (Garantía):** ¿Queda claro por qué tus datos apoyan tu aserción? ¿Mencionaste el 'respaldo' de esa conexión?")
    input("> Tu reflexión: ").strip()

    print("\n3. **Refutación Proactiva:** ¿Abordaste la objeción del costo de manera efectiva y no reactiva?")
    input("> Tu reflexión: ").strip()

    print("\n4. **Flujo y Cohesión:** ¿El argumento fluye lógicamente o los componentes se sienten desconectados?")
    input("> Tu reflexión: ").strip()

    print("\n¡Dominar esta complejidad te hará un persuasor de alto nivel! 💪")
    input("Presiona ENTER para el último ejercicio...")

def exercise_sophisticated_refutation():
    """Ejercicio: Prepara una refutación sofisticada que identifique una falacia."""
    show_header("Ejercicio: ¡Prepara tu Refutación Sofisticada!")
    print("En este ejercicio, no solo refutarás, sino que también identificarás una falacia común.\n")
    
    print("Imagina este argumento opuesto:")
    print("  **Argumento Opuesto:** 'No debemos invertir en programas de reciclaje más amplios en nuestra ciudad. Mi abuelo siempre decía que el reciclaje es una moda pasajera de la gente 'ecologista' y que las cosas siempre se han tirado a la basura. Además, desde que la ciudad empezó un pequeño programa de reciclaje el año pasado, ha habido un ligero aumento en las quejas de los ciudadanos sobre la recolección de basura. Claramente, el reciclaje causa problemas.'")
    
    print("\nTu tarea es escribir un párrafo de refutación (6-8 oraciones) que:")
    print("  1. **Reconozca** el argumento opuesto.")
    print("  2. **Identifique y explique** al menos UNA **falacia lógica** presente en el argumento opuesto (pista: ¡hay más de una!).")
    print("  3. **Refute el argumento** con tu propia lógica o una breve sugerencia de evidencia, llevando el debate de vuelta a hechos.\n")
    
    print("Escribe tu párrafo de refutación aquí:")
    user_refutation = ""
    print("(Presiona ENTER dos veces para terminar tu párrafo):")
    while True:
        line = input()
        if not line:
            break
        user_refutation += line + "\n"
    user_refutation = user_refutation.strip()

    print("\n--- ¡Tu Refutación Sofisticada! ---")
    print(user_refutation)

    print("\n--- Reflexión Guiada ---")
    print("Revisa tu refutación:")
    print("1. **Identificación de Falacia:** ¿Nombraste la falacia correctamente y explicaste por qué es errónea?")
    input("> Tu reflexión: ").strip()

    print("\n2. **Claridad de la Refutación:** ¿Tu refutación es lógica y se basa en hechos (incluso si son implícitos)?")
    input("> Tu reflexión: ").strip()

    print("\n3. **Tono:** ¿Tu refutación es persuasiva sin ser agresiva o un ataque personal?")
    input("> Tu reflexión: ").strip()

    print("\n¡Felicidades! Has demostrado un nivel avanzado de pensamiento crítico y persuasión. 🧠💡")
    input("Presiona ENTER para terminar la lección...")

def show_main_menu_l9_10th():
    """Muestra el menú principal de la aplicación para 10º Grado."""
    while True:
        show_header("Lección 9: Retórica Avanzada y Argumentación Persuasiva (10º Grado)")
        print("1. Introducción: ¡Maestros de la Persuasión!")
        print("2. Dominio de Apelaciones Retóricas (Ethos, Pathos, Logos)")
        print("3. Estructuras Argumentativas Complejas (Toulmin, Rogerian)")
        print("4. Anticipación de Contrapuntos y Falacias Lógicas")
        print("5. Ejercicio: ¡Analiza el Discurso Retórico!")
        print("6. Ejercicio: ¡Construye un Argumento Estructurado!")
        print("7. Ejercicio: ¡Prepara tu Refutación Sofisticada!")
        print("8. Salir de la Lección")
        print("=" * 100)

        choice = input("Elige un número (1-8): ")

        if choice == '1':
            show_introduction_l9_10th()
        elif choice == '2':
            show_rhetorical_appeals_concept()
        elif choice == '3':
            show_complex_structures_concept()
        elif choice == '4':
            show_fallacies_and_adaptation_concept()
        elif choice == '5':
            exercise_analyze_rhetorical_discourse()
        elif choice == '6':
            exercise_construct_structured_argument()
        elif choice == '7':
            exercise_sophisticated_refutation()
        elif choice == '8':
            print("¡Adiós, maestros de la persuasión! ¡Sigan influyendo con sus palabras y su lógica! 👋")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 8.")
            time.sleep(1)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    show_main_menu_l9_10th()
