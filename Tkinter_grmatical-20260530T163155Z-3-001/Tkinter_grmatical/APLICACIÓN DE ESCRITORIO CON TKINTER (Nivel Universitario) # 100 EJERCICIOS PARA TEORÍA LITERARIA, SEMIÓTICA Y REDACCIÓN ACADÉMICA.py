# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (Nivel Universitario)
# 100 EJERCICIOS PARA TEORÍA LITERARIA, SEMIÓTICA Y REDACCIÓN ACADÉMICA
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de nivel superior, con ejercicios
# sobre análisis deconstructivo, narratología avanzada, semiótica y producción de
# textos de investigación y tesis doctorales.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox
import os

class ParaphraseApp:
    """
    Clase principal que maneja la interfaz de usuario y la lógica de la aplicación.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Lengua Castellana (Nivel Universitario)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para nivel universitario
        self.ejercicios = [
            # SECCIÓN 1: TEORÍA LITERARIA Y CRÍTICA AVANZADA (25 EJERCICIOS)
            {"titulo": "1. La deconstrucción de Derrida y la crítica del logocentrismo", "contenido": "Análisis del concepto de deconstrucción y su aplicación para cuestionar la primacía del habla sobre la escritura y los binomios opuestos en un texto literario."},
            {"titulo": "2. La intertextualidad en la obra de Jorge Luis Borges", "contenido": "Análisis de la forma en que Borges construye sus relatos a partir de alusiones, citas y referencias a otros textos, creando un laberinto literario."},
            {"titulo": "3. La teoría de la recepción de H. R. Jauss y la estética del efecto", "contenido": "Análisis del papel del lector en la construcción del significado de una obra, considerando su 'horizonte de expectativas'."},
            {"titulo": "4. El Post-estructuralismo: Foucault y el poder del discurso", "contenido": "Análisis de la obra de Foucault y cómo el discurso no es una simple herramienta de comunicación, sino un mecanismo de poder y control social."},
            {"titulo": "5. La narratología de Gérard Genette: tiempo, modo y voz", "contenido": "Análisis de los conceptos clave de Genette para estudiar la estructura del relato, como la analepsis y la prolepsis, el punto de vista y el narrador."},
            {"titulo": "6. El modernismo en la poesía hispanoamericana: Rubén Darío", "contenido": "Análisis del Modernismo como un movimiento que buscó la renovación estética, la belleza formal y la musicalidad en la poesía hispanoamericana."},
            {"titulo": "7. El teatro del absurdo: Samuel Beckett y 'Esperando a Godot'", "contenido": "Análisis de la obra de Beckett, su crítica a la condición humana, la incomunicación y la ausencia de sentido en la existencia."},
            {"titulo": "8. La literatura del realismo mágico: la narrativa de Gabriel García Márquez", "contenido": "Análisis de la mezcla de elementos fantásticos con la realidad cotidiana en las obras del Realismo Mágico, como 'Cien años de soledad'."},
            {"titulo": "9. La novela del 'Boom' latinoamericano: Julio Cortázar y el juego con el lector", "contenido": "Análisis de la obra de Cortázar, su experimentación narrativa, la fragmentación y la invitación al lector a participar en la construcción del relato."},
            {"titulo": "10. El psicoanálisis en la interpretación de la literatura", "contenido": "Análisis de los mecanismos psicológicos (represión, sublimación, etc.) de los personajes para comprender sus motivaciones y conflictos internos."},
            {"titulo": "11. El concepto de 'Autor Implícito' y 'Lector Implícito' de Wayne Booth", "contenido": "Análisis de la idea de que en cada obra existe una versión del autor y del lector que son construcciones del texto, más allá de la persona real."},
            {"titulo": "12. La semiótica de la cultura: Yuri Lotman y la 'semiosfera'", "contenido": "Análisis de cómo la cultura es un sistema complejo de signos interconectados (la 'semiosfera') que se influyen mutuamente."},
            {"titulo": "13. El neorrealismo italiano y la literatura de posguerra", "contenido": "Análisis de la literatura que retrata la realidad social de forma cruda, sin idealización, con un enfoque en los personajes de las clases bajas."},
            {"titulo": "14. La hermenéutica de Hans-Georg Gadamer: la comprensión y la interpretación", "contenido": "Análisis del concepto de que la comprensión de un texto es un proceso continuo que se da en un 'círculo hermenéutico'."},
            {"titulo": "15. La narrativa de la 'generación de la ruptura' en México", "contenido": "Análisis de la obra de autores como Juan Rulfo y la ruptura con el lenguaje y las estructuras tradicionales para narrar la realidad."},
            {"titulo": "16. El concepto de 'literariedad' en el formalismo ruso", "contenido": "Análisis de la idea de que la literatura tiene sus propias características formales que la diferencian de otros tipos de discurso."},
            {"titulo": "17. El posmodernismo y la fragmentación en la narrativa contemporánea", "contenido": "Análisis de la literatura posmoderna, su crítica a los 'grandes relatos' y su uso de la ironía, la parodia y la intertextualidad."},
            {"titulo": "18. La semiótica del cine: el signo icónico y la narración visual", "contenido": "Análisis de cómo se construyen los significados en el cine a través de los signos visuales, sonoros y narrativos."},
            {"titulo": "19. La poesía experimental y el caligrama", "contenido": "Análisis de la poesía que busca la experimentación con la forma, la tipografía y la disposición de las palabras en la página."},
            {"titulo": "20. La teoría del 'dialogismo' de Mijaíl Bajtín", "contenido": "Análisis del concepto de que todo texto es un diálogo con otros textos, voces y discursos, y que el lenguaje es inherentemente social."},
            {"titulo": "21. El concepto de 'lectura sintomática' de Louis Althusser", "contenido": "Análisis de un texto para descubrir las 'ausencias' o las ideas no dichas, que revelan la ideología subyacente del autor."},
            {"titulo": "22. El teatro épico de Bertolt Brecht y la 'distanciación'", "contenido": "Análisis del teatro de Brecht, su crítica al teatro tradicional y su uso de la 'distanciación' para que el público no se identifique emocionalmente con los personajes."},
            {"titulo": "23. La retórica de la imagen: el análisis de anuncios publicitarios", "contenido": "Análisis de las estrategias retóricas (metáfora, metonimia, etc.) que se utilizan en la publicidad para persuadir al consumidor."},
            {"titulo": "24. El concepto de 'muerte del autor' de Roland Barthes", "contenido": "Análisis de la idea de que el significado de un texto no depende de la intención del autor, sino de la interpretación del lector."},
            {"titulo": "25. La crítica feminista de la literatura: relectura de obras clásicas", "contenido": "Análisis de cómo la perspectiva de género nos permite releer obras clásicas, cuestionando los roles de los personajes femeninos y la representación de la mujer."},

            # SECCIÓN 2: ANÁLISIS TEXTUAL AVANZADO (25 EJERCICIOS)
            {"titulo": "26. Análisis de 'El Aleph' de Jorge Luis Borges", "contenido": "Análisis del cuento de Borges, sus temas del infinito, el tiempo y la intertextualidad, y la estructura de un relato que contiene todos los relatos."},
            {"titulo": "27. Análisis de 'Pedro Páramo' de Juan Rulfo", "contenido": "Análisis de la novela de Rulfo, su narración fragmentada, la mezcla de voces y la representación de un México fantasmagórico y desolado."},
            {"titulo": "28. Análisis de 'Rayuela' de Julio Cortázar", "contenido": "Análisis de la novela de Cortázar, su estructura no lineal, el 'tablero de dirección' y el juego con el lector para que decida el orden de lectura."},
            {"titulo": "29. Análisis de 'La náusea' de Jean-Paul Sartre", "contenido": "Análisis de la novela de Sartre, sus temas del existencialismo, la libertad, la angustia y la contingencia de la existencia humana."},
            {"titulo": "30. Análisis de 'El nombre de la rosa' de Umberto Eco", "contenido": "Análisis de la novela de Eco, su intertextualidad, su complejidad semiótica y su reflexión sobre el lenguaje y la verdad."},
            {"titulo": "31. Análisis de 'Cien años de soledad' de Gabriel García Márquez", "contenido": "Análisis de los temas del tiempo circular, el amor incestuoso, la soledad y la fundación de un mundo a través del lenguaje en la novela."},
            {"titulo": "32. Análisis de 'Don Quijote de la Mancha': la metaliteratura", "contenido": "Análisis de la obra de Cervantes, su crítica a los libros de caballerías y su uso de la metaliteratura (la obra reflexiona sobre sí misma)."},
            {"titulo": "33. Análisis de la poesía de Octavio Paz: 'Piedra de sol'", "contenido": "Análisis de la poesía de Paz, su búsqueda de la identidad mexicana, su reflexión sobre el tiempo y el amor, y su uso de la mitología azteca."},
            {"titulo": "34. Análisis de 'Ulises' de James Joyce: el monólogo interior", "contenido": "Análisis de la novela de Joyce, su uso del monólogo interior para representar la complejidad de la conciencia y la vida interior de los personajes."},
            {"titulo": "35. Análisis de la poesía de César Vallejo: 'Los heraldos negros'", "contenido": "Análisis de la poesía de Vallejo, su tono existencialista, su angustia y su dolor ante la vida y la muerte."},
            {"titulo": "36. Análisis de 'La metamorfosis' de Franz Kafka", "contenido": "Análisis del cuento de Kafka, sus temas de la alienación, la burocracia y la incomunicación, a través de la transformación de un hombre en insecto."},
            {"titulo": "37. Análisis de 'El extranjero' de Albert Camus", "contenido": "Análisis de la novela de Camus, sus temas del existencialismo, el absurdo, la indiferencia y la libertad del individuo ante un mundo sin sentido."},
            {"titulo": "38. Análisis del teatro de Lope de Vega: 'Fuenteovejuna'", "contenido": "Análisis de la obra de Lope de Vega, su crítica social, el poder del pueblo unido contra la tiranía y la defensa del honor."},
            {"titulo": "39. Análisis de 'La casa de Bernarda Alba' de Federico García Lorca", "contenido": "Análisis de la obra de Lorca, sus temas del autoritarismo, la represión, la honra y el destino trágico de las mujeres en una sociedad patriarcal."},
            {"titulo": "40. Análisis de 'El túnel' de Ernesto Sábato", "contenido": "Análisis de la novela de Sábato, sus temas del existencialismo, la soledad, el amor y la incomunicación, a través de la voz de un narrador obsesivo."},
            {"titulo": "41. Análisis de la poesía de Paul Celan: 'Todesfuge'", "contenido": "Análisis de la poesía del Holocausto, su uso del lenguaje fragmentado y su forma de representar el trauma y la memoria del genocidio."},
            {"titulo": "42. Análisis de 'En busca del tiempo perdido' de Marcel Proust", "contenido": "Análisis de la obra de Proust, su exploración de la memoria involuntaria, el tiempo, la conciencia y la vida social de la burguesía francesa."},
            {"titulo": "43. Análisis de la poesía de José Gorostiza: 'Muerte sin fin'", "contenido": "Análisis de la poesía metafísica de Gorostiza, su reflexión sobre la muerte, la existencia y la búsqueda del sentido de la vida."},
            {"titulo": "44. Análisis de la literatura de testimonio: 'Me llamo Rigoberta Menchú'", "contenido": "Análisis de la literatura que busca dar voz a las experiencias de grupos marginados y denunciar las injusticias sociales y políticas."},
            {"titulo": "45. Análisis de 'Poeta en Nueva York' de Federico García Lorca", "contenido": "Análisis de la obra de Lorca, su visión de la alienación urbana, el racismo y la crisis del capitalismo en la ciudad de Nueva York."},
            {"titulo": "46. Análisis de la literatura del exilio: autores y temas", "contenido": "Análisis de la literatura de autores que tuvieron que abandonar su país, y sus temas de la memoria, la identidad y la nostalgia."},
            {"titulo": "47. Análisis de la poesía de José Lezama Lima: 'Paradiso'", "contenido": "Análisis de la novela de Lezama Lima, su complejidad poética, su uso de la metáfora y su búsqueda de la identidad cultural cubana."},
            {"titulo": "48. Análisis de 'La celestina' de Fernando de Rojas", "contenido": "Análisis de la obra de Rojas, su crítica a la moral de la época, sus personajes complejos y su mezcla de tragedia y comedia."},
            {"titulo": "49. Análisis de la literatura colonial: 'Sor Juana Inés de la Cruz'", "contenido": "Análisis de la obra de Sor Juana, su defensa del derecho a la educación de la mujer, su crítica social y su poesía barroca."},
            {"titulo": "50. Análisis de la novela distópica: '1984' de George Orwell", "contenido": "Análisis de la novela de Orwell, su crítica a los totalitarismos, la manipulación del lenguaje y la vigilancia masiva en una sociedad controlada."},

            # SECCIÓN 3: LINGÜÍSTICA Y SEMIÓTICA DEL DISCURSO (25 EJERCICIOS)
            {"titulo": "51. La pragmática avanzada: los actos de habla indirectos", "contenido": "Análisis de los actos de habla que no se expresan de forma literal, sino a través de insinuaciones o inferencias. Ej: '¿Tienes la hora?' para pedir la hora."},
            {"titulo": "52. El análisis del discurso político y la manipulación del lenguaje", "contenido": "Análisis de las estrategias retóricas (eufemismos, falacias, etc.) que se utilizan en el discurso político para persuadir o manipular a la audiencia."},
            {"titulo": "53. La semiótica de la imagen y la construcción del significado", "contenido": "Análisis de cómo se construyen los significados en una imagen a través de los signos icónicos, plásticos y connotativos."},
            {"titulo": "54. El concepto de 'género del discurso' de Mijaíl Bajtín", "contenido": "Análisis de cómo los géneros discursivos (carta, conversación, discurso político) son formas estables de organizar el habla que influyen en cómo nos comunicamos."},
            {"titulo": "55. La teoría de la 'relevancia' de Sperber y Wilson", "contenido": "Análisis del concepto de que la comunicación no solo se basa en el código lingüístico, sino en un proceso de inferencia que busca el máximo de 'relevancia'."},
            {"titulo": "56. El análisis de la conversación: turnos, reparaciones y solapamientos", "contenido": "Análisis de la estructura y las reglas implícitas que rigen una conversación, como el cambio de turno y la reparación de errores."},
            {"titulo": "57. La sociolingüística y la variación dialectal y social", "contenido": "Análisis de las variaciones del lenguaje según el lugar geográfico (dialectos) y la clase social (sociolectos) de los hablantes."},
            {"titulo": "58. La semiótica del vestuario y los códigos de la moda", "contenido": "Análisis de cómo la ropa es un sistema de signos que comunica nuestra identidad, estatus social, gustos, etc."},
            {"titulo": "59. El análisis del discurso publicitario: las falacias lógicas", "contenido": "Análisis de las falacias lógicas (argumentos falsos) que se utilizan en la publicidad para persuadir al consumidor, como la 'falacia ad populum'."},
            {"titulo": "60. La retórica de la imagen: la metáfora y la metonimia visual", "contenido": "Análisis de cómo las figuras retóricas se utilizan en la imagen para crear un significado más profundo y sugerente."},
            {"titulo": "61. El concepto de 'habitus' en la sociología de Pierre Bourdieu", "contenido": "Análisis de cómo las estructuras sociales se interiorizan en el individuo, influyendo en su forma de hablar, pensar y actuar."},
            {"titulo": "62. El análisis del discurso de género: la representación de la mujer", "contenido": "Análisis de cómo el lenguaje y el discurso construyen las identidades de género y cómo se representan a la mujer en los medios de comunicación."},
            {"titulo": "63. La semiótica de la arquitectura: el significado de los espacios", "contenido": "Análisis de cómo los espacios arquitectónicos (una catedral, una cárcel) son un sistema de signos que comunican ideas y valores culturales."},
            {"titulo": "64. El análisis del discurso legal: la ambigüedad y la precisión", "contenido": "Análisis de cómo el lenguaje legal busca la máxima precisión para evitar la ambigüedad, pero a veces falla en su objetivo."},
            {"titulo": "65. La teoría de la 'interpela' de Louis Althusser", "contenido": "Análisis del concepto de cómo la ideología nos 'interpela' o nos llama para que nos identifiquemos con ella y la asumamos como propia."},
            {"titulo": "66. El análisis del discurso de los medios de comunicación", "contenido": "Análisis de las estrategias discursivas (encuadres, selección de noticias, etc.) que utilizan los medios para construir una determinada realidad."},
            {"titulo": "67. La teoría de la 'performatividad' de Judith Butler", "contenido": "Análisis del concepto de que el género no es una esencia, sino una serie de 'actos' o 'performances' que se repiten y construyen la identidad."},
            {"titulo": "68. La semiótica de la música: el significado de los sonidos", "contenido": "Análisis de cómo la música es un sistema de signos que comunica emociones, ideas y valores culturales sin necesidad de palabras."},
            {"titulo": "69. La retórica del humor: la parodia y la ironía en el stand-up", "contenido": "Análisis de cómo el humor utiliza la parodia, la ironía y la sátira para criticar la sociedad y hacer reflexionar al público."},
            {"titulo": "70. El análisis del discurso histórico: la construcción de la verdad", "contenido": "Análisis de cómo los historiadores construyen la 'verdad' a partir de los documentos, las fuentes y su propia interpretación de los hechos."},
            {"titulo": "71. La semiótica de la alimentación: el significado de la comida", "contenido": "Análisis de cómo la comida es un sistema de signos que comunica nuestra cultura, nuestras tradiciones, nuestros gustos y nuestro estatus social."},
            {"titulo": "72. El análisis del discurso científico y su objetividad", "contenido": "Análisis de cómo el lenguaje científico busca la objetividad, la precisión y la universalidad para comunicar sus hallazgos de forma clara."},
            {"titulo": "73. La retórica del liderazgo: la persuasión en el discurso de un líder", "contenido": "Análisis de las estrategias retóricas (metáforas, anáforas, etc.) que se utilizan en el discurso de un líder para inspirar y persuadir a sus seguidores."},
            {"titulo": "74. La semiótica de la danza: el significado del movimiento corporal", "contenido": "Análisis de cómo la danza es un sistema de signos que comunica emociones, ideas y narraciones a través del movimiento y el espacio."},
            {"titulo": "75. El análisis del discurso tecnológico: la jerga y la comunidad", "contenido": "Análisis de cómo la tecnología crea su propio discurso, con una jerga específica y una comunidad de hablantes que comparten un conocimiento."},

            # SECCIÓN 4: PRODUCCIÓN TEXTUAL ACADÉMICA Y PROFESIONAL (25 EJERCICIOS)
            {"titulo": "76. La redacción de una tesis doctoral: estructura y metodología", "contenido": "Planificación y desarrollo de la estructura de una tesis doctoral: la introducción, los capítulos de desarrollo, las conclusiones y la bibliografía."},
            {"titulo": "77. La redacción de un artículo científico o de investigación", "contenido": "Elaboración de un artículo formal que presente una investigación original, con una estructura clara (introducción, metodología, resultados, conclusiones)."},
            {"titulo": "78. La redacción de una propuesta de investigación", "contenido": "Formulación de una propuesta de investigación que incluya un problema de investigación, una pregunta, una hipótesis, una metodología y un cronograma."},
            {"titulo": "79. La elaboración de una reseña de libro para una revista académica", "contenido": "Redacción de una reseña que combine un resumen de la obra con una crítica fundamentada, adecuada para una publicación especializada."},
            {"titulo": "80. La redacción de un ensayo filosófico o teórico", "contenido": "Creación de un ensayo que desarrolle un argumento abstracto, con un lenguaje preciso y una estructura lógica, sobre un tema filosófico o teórico."},
            {"titulo": "81. La paráfrasis de un texto académico complejo", "contenido": "Técnicas para reformular un texto de alta complejidad, manteniendo la exactitud de la información sin alterar su significado."},
            {"titulo": "82. La redacción de un informe técnico para una empresa o una institución", "contenido": "Elaboración de un informe formal que presente datos, análisis y recomendaciones, con un lenguaje claro y preciso."},
            {"titulo": "83. La elaboración de un discurso de presentación de un proyecto", "contenido": "Redacción de un discurso que presente un proyecto de forma clara, concisa y persuasiva, destacando sus objetivos, beneficios y resultados."},
            {"titulo": "84. La redacción de un artículo de opinión para un periódico de prestigio", "contenido": "Creación de un artículo de opinión que combine información relevante con una valoración personal, con un lenguaje formal y una estructura argumentativa."},
            {"titulo": "85. La citación en el formato APA, MLA o Chicago", "contenido": "Uso correcto de las normas de citación para evitar el plagio y dar crédito a las fuentes, en los formatos más comunes en la academia."},
            {"titulo": "86. La redacción de una carta de solicitud para una beca de postgrado", "contenido": "Elaboración de una carta formal que resalte los méritos académicos, la experiencia y la motivación para solicitar una beca de postgrado."},
            {"titulo": "87. La elaboración de un abstract para una ponencia o un congreso", "contenido": "Redacción de un resumen conciso y claro de una investigación, que resuma los objetivos, la metodología y los resultados en un máximo de 250 palabras."},
            {"titulo": "88. La importancia de la revisión por pares en la publicación académica", "contenido": "Análisis del proceso de revisión de un artículo por otros expertos, su importancia para la calidad de la investigación y su función en la comunidad científica."},
            {"titulo": "89. La estructura de un debate formal de nivel universitario", "contenido": "Análisis de las fases de un debate formal: presentación de la tesis, argumentos, refutación, conclusiones y cierre."},
            {"titulo": "90. La elaboración de un 'state of the art' o 'estado del arte'", "contenido": "Redacción de una revisión crítica de la bibliografía existente sobre un tema, para identificar las lagunas y los avances de la investigación."},
            {"titulo": "91. La redacción de un informe de lectura crítica", "contenido": "Elaboración de un informe que resuma y analice críticamente un texto, destacando sus fortalezas, debilidades y contribuciones al campo."},
            {"titulo": "92. El estilo y el tono en la escritura de un ensayo crítico", "contenido": "Elección del tono (formal, analítico, crítico) y el estilo (preciso, claro, argumentativo) adecuados para un ensayo crítico."},
            {"titulo": "93. La redacción de una monografía sobre un tema especializado", "contenido": "Elaboración de una monografía, un trabajo de investigación extenso sobre un tema específico, con rigor y estructura académica."},
            {"titulo": "94. La redacción de un guion para un documental de investigación", "contenido": "Creación de un guion que presente una investigación de forma visual, con un hilo narrativo, entrevistas y datos."},
            {"titulo": "95. La paráfrasis y el plagio en el entorno universitario", "contenido": "Diferenciación entre la paráfrasis (reformular con palabras propias) y el plagio (copiar sin citar) de un texto, y sus consecuencias."},
            {"titulo": "96. La redacción de un 'grant proposal' o propuesta de subvención", "contenido": "Elaboración de una propuesta para solicitar financiación para un proyecto de investigación, con un lenguaje claro y persuasivo."},
            {"titulo": "97. La estructura de un proyecto de investigación para un posgrado", "contenido": "Planificación de un proyecto de investigación para un posgrado, con una justificación, objetivos, metodología y cronograma."},
            {"titulo": "98. La elaboración de un currículum vitae académico", "contenido": "Redacción de un CV que resalte la experiencia en investigación, las publicaciones y las ponencias de un académico."},
            {"titulo": "99. La redacción de un discurso de defensa de tesis o proyecto", "contenido": "Elaboración de un discurso formal, conciso y convincente para defender una tesis o un proyecto ante un tribunal o un público especializado."},
            {"titulo": "100. La ética en la investigación académica: el manejo de datos", "contenido": "Análisis de las normas éticas que rigen la investigación, como el consentimiento informado, la confidencialidad y la honestidad en el manejo de los datos."},
        ]

        self.paraphrases = [None] * len(self.ejercicios)
        self.current_exercise_index = 0
        self.is_editing = False

        # Configuración de los estilos para una apariencia moderna
        style = ttk.Style()
        style.theme_use("clam")

        # --- Creación de los widgets principales ---

        # Frame principal para contener todos los elementos
        main_frame = ttk.Frame(root, padding="15 15 15 15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título principal
        title_label = ttk.Label(main_frame, text="Ejercicios de Lengua Castellana (Nivel Universitario)", font=("Helvetica", 20, "bold"), background="#f0f0f0")
        title_label.pack(pady=(0, 10))

        # Contador de ejercicios
        self.counter_label = ttk.Label(main_frame, text="", font=("Helvetica", 14), background="#f0f0f0")
        self.counter_label.pack(pady=(0, 10))

        # Marco para el contenido del ejercicio
        exercise_frame = ttk.Frame(main_frame, padding="10", relief="groove", borderwidth=2)
        exercise_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Título del ejercicio
        self.exercise_title_label = ttk.Label(exercise_frame, text="", font=("Helvetica", 12, "bold"), wraplength=700, anchor="w", justify="left")
        self.exercise_title_label.pack(fill=tk.X, pady=(0, 5))

        # Contenido del ejercicio (usando un Text widget para scroll)
        self.exercise_text_widget = tk.Text(exercise_frame, wrap=tk.WORD, height=8, font=("Helvetica", 12), padx=5, pady=5)
        self.exercise_text_widget.pack(fill=tk.BOTH, expand=True)

        # Barra de desplazamiento para el contenido
        scrollbar = ttk.Scrollbar(exercise_frame, command=self.exercise_text_widget.yview)
        self.exercise_text_widget['yscrollcommand'] = scrollbar.set
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Etiqueta para el área de paráfrasis
        paraphrase_label = ttk.Label(main_frame, text="Escribe tu paráfrasis aquí:", font=("Helvetica", 12), background="#f0f0f0")
        paraphrase_label.pack(pady=(10, 5), anchor="w")

        # Área de texto para la paráfrasis
        self.paraphrase_text_widget = tk.Text(main_frame, wrap=tk.WORD, height=10, font=("Helvetica", 12), padx=5, pady=5)
        self.paraphrase_text_widget.pack(fill=tk.BOTH, expand=True)

        # Frame para los botones
        button_frame = ttk.Frame(main_frame, padding="10", style="TFrame")
        button_frame.pack(fill=tk.X, pady=(10, 0))

        # Botón para revisar y editar
        self.review_button = ttk.Button(button_frame, text="Revisar y Editar Paráfrasis", command=self.open_edit_window)
        self.review_button.pack(side=tk.LEFT, padx=(0, 5), expand=True, fill=tk.X)

        # Botón principal de acción (Siguiente/Guardar)
        self.action_button = ttk.Button(button_frame, text="Siguiente Ejercicio", command=self.handle_action)
        self.action_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Botón para guardar todas las paráfrasis
        self.save_button = ttk.Button(button_frame, text="Guardar todas las paráfrasis", command=self.save_paraphrases_to_file, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=(5, 0), expand=True, fill=tk.X)
        
        self.load_exercise()

    def load_exercise(self):
        """
        Carga los datos del ejercicio actual en la interfaz.
        """
        self.is_editing = False
        self.action_button.config(text="Siguiente Ejercicio")
        
        if self.current_exercise_index < len(self.ejercicios):
            exercise = self.ejercicios[self.current_exercise_index]
            self.counter_label.config(text=f"Ejercicio {self.current_exercise_index + 1} de {len(self.ejercicios)}")
            self.exercise_title_label.config(text=exercise['titulo'])
            
            # Limpiar y escribir el contenido del ejercicio
            self.exercise_text_widget.config(state=tk.NORMAL)
            self.exercise_text_widget.delete("1.0", tk.END)
            self.exercise_text_widget.insert("1.0", exercise['contenido'])
            self.exercise_text_widget.config(state=tk.DISABLED)
            
            # Cargar la paráfrasis guardada si existe
            self.paraphrase_text_widget.config(state=tk.NORMAL)
            self.paraphrase_text_widget.delete("1.0", tk.END)
            if self.paraphrases[self.current_exercise_index]:
                self.paraphrase_text_widget.insert("1.0", self.paraphrases[self.current_exercise_index])
            
            self.action_button.config(state=tk.NORMAL)
            self.review_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL if any(self.paraphrases) else tk.DISABLED)

        else:
            # Fin de los ejercicios
            self.counter_label.config(text="🎉 ¡Has completado todos los ejercicios! 🎉")
            self.exercise_title_label.config(text="Puedes guardar tus paráfrasis ahora.")
            self.exercise_text_widget.config(state=tk.NORMAL)
            self.exercise_text_widget.delete("1.0", tk.END)
            self.exercise_text_widget.config(state=tk.DISABLED)
            self.paraphrase_text_widget.delete("1.0", tk.END)
            self.paraphrase_text_widget.config(state=tk.DISABLED)
            
            self.action_button.config(state=tk.DISABLED)
            self.review_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.NORMAL if any(self.paraphrases) else tk.DISABLED)

    def handle_action(self):
        """
        Maneja la lógica del botón principal (siguiente o guardar edición).
        """
        if self.is_editing:
            self.save_edited_paraphrase()
        else:
            self.next_exercise()

    def next_exercise(self):
        """
        Guarda la paráfrasis actual y avanza al siguiente ejercicio.
        """
        paraphrase_text = self.paraphrase_text_widget.get("1.0", tk.END).strip()
        self.paraphrases[self.current_exercise_index] = paraphrase_text if paraphrase_text else "OMITIDO"
        
        self.current_exercise_index += 1
        self.load_exercise()

    def open_edit_window(self):
        """
        Abre una nueva ventana (Toplevel) con la lista de ejercicios para editar.
        """
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Revisar y Editar")
        edit_window.geometry("500x400")
        edit_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(edit_window, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        list_label = ttk.Label(frame, text="Selecciona un ejercicio para editar:", font=("Helvetica", 12, "bold"))
        list_label.pack(pady=(0, 10))

        listbox = tk.Listbox(frame, font=("Helvetica", 12), selectmode=tk.SINGLE)
        listbox.pack(fill=tk.BOTH, expand=True)

        # Llenar el listbox con el estado de cada ejercicio
        for i, paraphrase in enumerate(self.paraphrases):
            status = "✅" if paraphrase and paraphrase != "OMITIDO" else "❓"
            listbox.insert(tk.END, f"{status} Ejercicio {i + 1}: {self.ejercicios[i]['titulo']}")

        def select_and_edit():
            """
            Función que se ejecuta al seleccionar un ejercicio del Listbox.
            """
            try:
                selected_index = listbox.curselection()[0]
                edit_window.destroy()  # Cerrar la ventana de edición
                self.load_for_editing(selected_index)
            except IndexError:
                messagebox.showwarning("Selección inválida", "Por favor, selecciona un ejercicio de la lista.")

        edit_button = ttk.Button(frame, text="Editar Ejercicio Seleccionado", command=select_and_edit)
        edit_button.pack(pady=10)

    def load_for_editing(self, index):
        """
        Carga el ejercicio seleccionado desde la ventana de edición.
        """
        self.current_exercise_index = index
        self.is_editing = True
        
        exercise = self.ejercicios[self.current_exercise_index]
        self.counter_label.config(text=f"Editando Ejercicio {self.current_exercise_index + 1} de {len(self.ejercicios)}")
        self.exercise_title_label.config(text=exercise['titulo'])

        self.exercise_text_widget.config(state=tk.NORMAL)
        self.exercise_text_widget.delete("1.0", tk.END)
        self.exercise_text_widget.insert("1.0", exercise['contenido'])
        self.exercise_text_widget.config(state=tk.DISABLED)

        self.paraphrase_text_widget.config(state=tk.NORMAL)
        self.paraphrase_text_widget.delete("1.0", tk.END)
        if self.paraphrases[index]:
            self.paraphrase_text_widget.insert("1.0", self.paraphrases[index])
        
        self.action_button.config(text="Guardar Edición")
        self.review_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)
    
    def save_edited_paraphrase(self):
        """
        Guarda la paráfrasis editada y vuelve al modo normal.
        """
        paraphrase_text = self.paraphrase_text_widget.get("1.0", tk.END).strip()
        self.paraphrases[self.current_exercise_index] = paraphrase_text if paraphrase_text else "OMITIDO"
        
        self.is_editing = False
        self.load_exercise()

    def save_paraphrases_to_file(self):
        """
        Guarda todas las paráfrasis en un archivo de texto.
        """
        filename = "parafrasis_lengua_castellana_universitario_tkinter.txt"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for i, item in enumerate(self.paraphrases):
                    if item and item != "OMITIDO":
                        original_content = self.ejercicios[i]['contenido']
                        title = self.ejercicios[i]['titulo']
                        file.write(f"--- Ejercicio {i + 1} - {title} ---\n")
                        file.write(f"Texto original: {original_content}\n")
                        file.write(f"Tu paráfrasis: {item}\n\n")
            messagebox.showinfo("Guardado Completo", f"¡Guardado Exitoso! ✅\nSe ha creado el archivo '{filename}'.")
        except IOError as e:
            messagebox.showerror("Error de Archivo", f"Error: No se pudo guardar el archivo.\nDetalles: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ParaphraseApp(root)
    root.mainloop()
