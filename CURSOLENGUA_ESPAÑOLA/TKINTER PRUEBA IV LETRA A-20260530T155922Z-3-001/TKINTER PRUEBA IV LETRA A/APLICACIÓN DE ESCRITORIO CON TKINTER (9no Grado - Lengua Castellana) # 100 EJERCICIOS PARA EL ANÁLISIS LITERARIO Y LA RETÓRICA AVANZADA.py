# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (9no Grado - Lengua Castellana)
# 100 EJERCICIOS PARA EL ANÁLISIS LITERARIO Y LA RETÓRICA AVANZADA
# ==============================================================================
# Esta aplicación recrea la funcionalidad del programa anterior de Kivy,
# utilizando la librería estándar de Python, Tkinter. Está diseñada para
# estudiantes de noveno grado, profundizando en temas como el análisis de textos
# complejos, el estudio de figuras retóricas más sofisticadas y la comprensión
# de géneros y movimientos literarios.
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
        self.root.title("Ejercicios de Lengua Castellana (9no Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para noveno grado
        # Esta lista es idéntica a la versión de Kivy para mantener la consistencia
        self.ejercicios = [
            # SECCIÓN 1: GRAMÁTICA Y SINTAXIS AVANZADA
            {"titulo": "1. El uso del modo Subjuntivo", "contenido": "El subjuntivo se usa para expresar deseos, dudas, hipótesis, juicios de valor o acciones no reales. Ej: 'Espero que vengas'."},
            {"titulo": "2. Tiempos verbales perfectos y su uso", "contenido": "El pretérito pluscuamperfecto, el antepresente, el antefuturo. Indican una acción anterior a otra acción o a un momento en el tiempo."},
            {"titulo": "3. Oraciones compuestas subordinadas sustantivas de complemento de régimen", "contenido": "La proposición subordinada complementa a un verbo que exige una preposición. Ej: 'Se acordó de que era tarde'."},
            {"titulo": "4. Subordinadas de complemento del nombre y del adjetivo", "contenido": "La proposición subordinada complementa un sustantivo o adjetivo. Ej: 'Estoy convencido de que volverá'."},
            {"titulo": "5. El uso de la voz pasiva con 'ser' y 'estar'", "contenido": "La pasiva con 'ser' se usa para acciones. La pasiva con 'estar' se usa para estados. Ej: 'El libro fue escrito por ella' vs 'El libro está escrito'."},
            {"titulo": "6. La nominalización en la redacción formal", "contenido": "Transformar verbos o adjetivos en sustantivos para dar más objetividad y formalidad a un texto. Ej: 'Llegó tarde' -> 'La tardía llegada'."},
            {"titulo": "7. El uso de los verbos 'haber' y 'tener'", "contenido": "'Haber' se usa como auxiliar. 'Tener' se usa para posesión. El uso incorrecto es una incorrección. Ej: 'Había muchos libros' vs 'Tenía muchos libros'."},
            {"titulo": "8. Conectores de adición y de consecuencia", "contenido": "Conectores para añadir información (además, asimismo) y para indicar el resultado de una acción (en consecuencia, por ende)."},
            {"titulo": "9. Análisis de la oración compuesta por yuxtaposición", "contenido": "Oraciones sin nexos que se unen por signos de puntuación. Ej: 'Llegó; estaba cansado'."},
            {"titulo": "10. La subordinada sustantiva de aposición", "contenido": "La proposición subordinada funciona como una aposición del sujeto o de otro sustantivo. Ej: 'Dijo una cosa, que no iría'."},
            {"titulo": "11. El uso correcto del gerundio", "contenido": "El gerundio debe expresar una acción simultánea o anterior a la del verbo principal. Su uso para acciones posteriores es un error."},
            {"titulo": "12. La estructura de las oraciones impersonales", "contenido": "Oraciones sin sujeto explícito ni implícito. Verbos como 'haber', 'hacer' (clima), 'ser' (tiempo)."},
            {"titulo": "13. Análisis de las oraciones interrogativas indirectas", "contenido": "Oraciones que formulan una pregunta dentro de otra oración principal. No llevan signos de interrogación. Ej: 'Le pregunté si vendría'."},
            {"titulo": "14. La anacoluto y otros vicios de la sintaxis", "contenido": "Una interrupción en la estructura sintáctica de una oración, que causa incoherencia. Es un error gramatical."},
            {"titulo": "15. La conjunción 'si' condicional vs. 'si' interrogativo", "contenido": "La conjunción 'si' sin tilde introduce una condición. El 'si' con tilde es una nota musical o una afirmación."},
            {"titulo": "16. El uso de las preposiciones en complementos circunstanciales", "contenido": "Uso de preposiciones como 'a', 'con', 'de', 'en' para construir C.C. de modo, lugar, tiempo, etc."},
            {"titulo": "17. Adverbios de cantidad y de grado", "contenido": "Adverbios que modifican al verbo, adjetivo o a otro adverbio, indicando la intensidad de la acción o cualidad. Ej: 'muy', 'bastante'."},
            {"titulo": "18. Los relativos 'cuyo' y 'cuanto'", "contenido": "El relativo 'cuyo' indica posesión. 'Cuanto' tiene valor de cantidad. Su uso incorrecto es un error común."},
            {"titulo": "19. Los verbos de régimen y su relación con la preposición", "contenido": "Verbos que necesitan una preposición específica para funcionar. Ej: 'depender de', 'confiar en'."},
            {"titulo": "20. La correlación de tiempos verbales en la subordinación", "contenido": "La relación que existe entre el tiempo del verbo en la oración principal y el de la proposición subordinada."},
            {"titulo": "21. El verbo 'ir' y su uso en perífrasis de futuro", "contenido": "La perífrasis 'ir a + infinitivo' se usa para expresar un futuro cercano o una intención. Ej: 'Voy a estudiar'."},
            {"titulo": "22. La puntuación en oraciones complejas", "contenido": "Uso correcto de comas, punto y coma y dos puntos para separar y organizar oraciones subordinadas y coordinadas."},
            {"titulo": "23. La sinonimia y la antonimia contextual", "contenido": "El significado de una palabra cambia dependiendo del contexto en el que se use."},
            {"titulo": "24. Los verbos copulativos y predicativos", "contenido": "Los copulativos ('ser', 'estar', 'parecer') unen el sujeto con un atributo. Los predicativos expresan una acción."},
            {"titulo": "25. Verbos impersonales con 'se'", "contenido": "Oraciones que se construyen con 'se' y un verbo en tercera persona para referirse a un sujeto indeterminado. Ej: 'Se vive bien aquí'."},
            
            # SECCIÓN 2: FIGURAS RETÓRICAS Y ESTILÍSTICAS AVANZADAS
            {"titulo": "26. La paradoja", "contenido": "Figura retórica que une dos ideas aparentemente contradictorias pero que encierran una verdad profunda. Ej: 'Al avaro, las riquezas lo hacen más pobre'."},
            {"titulo": "27. La sinestesia", "contenido": "Asociación de sensaciones que provienen de diferentes sentidos. Ej: 'Un sonido amarillo' o 'un olor dulce'."},
            {"titulo": "28. El hipérbaton", "contenido": "Alteración del orden sintáctico habitual de la oración para lograr un efecto estético. Ej: 'Del salón en el ángulo oscuro' (en lugar de 'En el ángulo oscuro del salón')."},
            {"titulo": "29. El eufemismo y el disfemismo", "contenido": "El eufemismo suaviza una idea desagradable. El disfemismo la hace más dura. Ej: 'pasar a mejor vida' vs 'estirar la pata'."},
            {"titulo": "30. La elipsis", "contenido": "Omisión de un elemento de la oración que se sobreentiende por el contexto. Ej: 'Yo llevé los libros; ella, las revistas'."},
            {"titulo": "31. La anáfora y la epífora", "contenido": "La anáfora es la repetición de palabras al inicio del verso. La epífora es la repetición al final del verso."},
            {"titulo": "32. El paralelismo", "contenido": "Repetición de la misma estructura sintáctica en dos o más oraciones o versos. Ej: 'Cómo quisiera yo, cómo quisiera'."},
            {"titulo": "33. La aliteración y la onomatopeya", "contenido": "La aliteración es la repetición de sonidos para lograr un efecto. La onomatopeya imita los sonidos naturales."},
            {"titulo": "34. El pleonasmo", "contenido": "Empleo de palabras superfluas que añaden información ya incluida. Ej: 'Subir arriba'."},
            {"titulo": "35. La ironía y el sarcasmo", "contenido": "La ironía dice lo contrario de lo que se piensa, el sarcasmo es una ironía cruel y ofensiva."},
            {"titulo": "36. La catáfora", "contenido": "Adelanto de un elemento que se explicará más adelante en el texto. Ej: 'Te diré una cosa: que no te preocupes'."},
            {"titulo": "37. La prosopopeya", "contenido": "Atribuir cualidades de seres animados o humanos a objetos o conceptos abstractos. Ej: 'El viento gimió tristemente'."},
            {"titulo": "38. La antonomasia", "contenido": "Sustitución de un nombre propio por un apelativo o una característica. Ej: 'El Rey del Pop' por Michael Jackson."},
            {"titulo": "39. La perífrasis", "contenido": "Decir algo de forma indirecta, usando un rodeo de palabras. Ej: 'La ciudad de la luz' por París."},
            {"titulo": "40. La reticencia y el apóstrofe", "contenido": "La reticencia es dejar una frase inacabada. El apóstrofe es una interrupción para dirigirse a un ser o cosa."},
            {"titulo": "41. La sinécdoque", "contenido": "Designación de una cosa con el nombre de otra, por la relación de la parte por el todo. Ej: 'Tiene veinte primaveras' para decir 'veinte años'."},
            {"titulo": "42. La metonimia", "contenido": "Designación de una cosa con el nombre de otra por una relación de causa-efecto, continente-contenido. Ej: 'Beber una copa'."},
            {"titulo": "43. El asíndeton y el polisíndeton", "contenido": "El asíndeton omite las conjunciones. El polisíndeton las repite para dar un efecto de enumeración. Ej: 'Vino, vio, venció' vs 'Vino y vio y venció'."},
            {"titulo": "44. La gradación", "contenido": "Disposición de palabras en orden ascendente o descendente. Ej: 'En polvo, en humo, en nada'."},
            {"titulo": "45. La interpelación retórica", "contenido": "Una pregunta que no espera respuesta, sino que busca un efecto o una reflexión."},
            {"titulo": "46. La zeugma", "contenido": "Una palabra se usa una sola vez, pero se aplica a varios elementos de la oración. Ej: 'Se quedó sin aliento y sin habla'."},
            {"titulo": "47. La hipálage", "contenido": "Atribuir a un sustantivo una cualidad propia de otro. Ej: 'El ruido de un silencio frío'."},
            {"titulo": "48. La alegoría", "contenido": "Una metáfora continuada, donde cada elemento de la historia tiene un significado simbólico."},
            {"titulo": "49. La hipérbole", "contenido": "Exageración de una idea para magnificarla o restarle importancia. Ej: 'Te lo he dicho un millón de veces'."},
            {"titulo": "50. El clímax y el anticlímax", "contenido": "El clímax es el punto de mayor intensidad. El anticlímax es la culminación de un proceso que resulta decepcionante."},

            # SECCIÓN 3: ANÁLISIS DE TEXTOS Y GÉNEROS LITERARIOS
            {"titulo": "51. Análisis de la trama y el conflicto en una novela", "contenido": "Identificación de la estructura narrativa (planteamiento, nudo, desenlace) y de los tipos de conflicto (interno, externo)."},
            {"titulo": "52. El desarrollo de personajes principales y secundarios", "contenido": "Análisis de la caracterización de los personajes, su evolución a lo largo de la historia y su función en la trama."},
            {"titulo": "53. El narrador y el punto de vista en textos complejos", "contenido": "Identificación de los diferentes tipos de narrador (omnisciente, testigo, protagonista) y su influencia en la percepción del relato."},
            {"titulo": "54. El tema y la idea principal en la poesía", "contenido": "Diferenciación entre el tema general del poema y la idea central que el poeta busca transmitir."},
            {"titulo": "55. El ensayo como herramienta de argumentación", "contenido": "Reconocimiento de la estructura argumentativa del ensayo y la tesis que el autor defiende."},
            {"titulo": "56. El teatro del siglo de oro español", "contenido": "Características principales del teatro de Lope de Vega o Calderón de la Barca: temas de honor, religión y amor."},
            {"titulo": "57. La novela picaresca y el antihéroe", "contenido": "Análisis del género de la novela picaresca, con un protagonista de clase baja que se vale de la astucia para sobrevivir."},
            {"titulo": "58. El Modernismo literario", "contenido": "Características del Modernismo como la búsqueda de la belleza, la exquisitez, el exotismo y la musicalidad en la lengua."},
            {"titulo": "59. El Realismo en la literatura", "contenido": "Movimiento literario que busca retratar la realidad social de forma objetiva y detallada, con un enfoque en la crítica social."},
            {"titulo": "60. El mito y el arquetipo en la literatura", "contenido": "Análisis de personajes y situaciones que representan modelos universales y simbólicos en la literatura."},
            {"titulo": "61. El Romanticismo y su enfoque en la emoción", "contenido": "Movimiento que exalta los sentimientos, el individualismo, la libertad y la naturaleza, oponiéndose al racionalismo."},
            {"titulo": "62. El Soneto renacentista y barroco", "contenido": "Análisis del soneto como forma poética, sus características métricas y temáticas en diferentes épocas literarias."},
            {"titulo": "63. La crítica literaria y el comentario de texto", "contenido": "Reconocimiento de la estructura y los elementos necesarios para hacer un análisis crítico de un texto."},
            {"titulo": "64. El Boom Latinoamericano", "contenido": "Movimiento de la literatura hispanoamericana que introdujo nuevas técnicas narrativas y exploró temas como la identidad y la política."},
            {"titulo": "65. La vanguardia literaria", "contenido": "Movimientos artísticos del siglo XX que rompieron con la tradición y experimentaron con nuevas formas de expresión. Ej: Surrealismo, Futurismo."},
            {"titulo": "66. La Novela Gótica y el suspense", "contenido": "Análisis del género gótico y sus elementos: escenarios tétricos, misterio y terror."},
            {"titulo": "67. La Odisea y los viajes iniciáticos", "contenido": "Análisis del viaje de Ulises como un arquetipo de la aventura, la superación y el regreso al hogar."},
            {"titulo": "68. El Poema épico y la figura del héroe", "contenido": "Características del poema épico como género narrativo y la figura del héroe con cualidades extraordinarias."},
            {"titulo": "69. La Fábula y su función didáctica", "contenido": "Reconocimiento de la estructura de la fábula y su moraleja o enseñanza final."},
            {"titulo": "70. La autobiografía y su valor testimonial", "contenido": "Análisis de la autobiografía como género que narra la vida del autor y su valor como testimonio histórico."},
            {"titulo": "71. El haiku y la poesía breve", "contenido": "Análisis del haiku japonés y otras formas de poesía breve, su estructura y la búsqueda de la síntesis."},
            {"titulo": "72. La sátira y la crítica social", "contenido": "El uso de la sátira en la literatura para criticar y ridiculizar vicios sociales o políticos."},
            {"titulo": "73. La novela histórica", "contenido": "Género que mezcla la ficción con hechos y personajes históricos para recrear una época."},
            {"titulo": "74. El microrrelato y sus características", "contenido": "Análisis de las principales características del microrrelato: brevedad, concisión y final sorprendente."},
            {"titulo": "75. La poesía de la generación del 27", "contenido": "Movimiento poético español que buscaba una síntesis entre la tradición y la vanguardia. Ej: Lorca, Alberti."},
            
            # SECCIÓN 4: PRODUCCIÓN TEXTUAL Y COMUNICACIÓN CRÍTICA
            {"titulo": "76. La estructura de un ensayo argumentativo", "contenido": "Planificación y desarrollo de la estructura de un ensayo argumentativo: introducción (tesis), desarrollo (argumentos) y conclusión."},
            {"titulo": "77. La redacción de una tesis y su defensa", "contenido": "Formulación de una tesis clara y el desarrollo de argumentos sólidos para respaldarla en un texto."},
            {"titulo": "78. La refutación y la contraargumentación en un debate", "contenido": "Técnicas para invalidar o contradecir los argumentos del oponente en un debate."},
            {"titulo": "79. La voz y el tono en la escritura", "contenido": "Elección del tono (formal, informal, objetivo, subjetivo) y la voz del autor para adecuar el texto al público y al propósito."},
            {"titulo": "80. La reseña crítica de una obra literaria o cinematográfica", "contenido": "Análisis de la estructura y los elementos de una reseña crítica: resumen, opinión y valoración."},
            {"titulo": "81. La carta formal y la carta informal", "contenido": "Diferencias en la estructura, el lenguaje y el propósito entre una carta formal y una informal."},
            {"titulo": "82. La coherencia y la cohesión en textos extensos", "contenido": "Uso de conectores lógicos, pronombres y repeticiones para dar fluidez y unidad de sentido a un texto."},
            {"titulo": "83. El discurso expositivo y sus características", "contenido": "Análisis de la estructura del discurso expositivo, su objetivo de informar y su uso de un lenguaje claro y preciso."},
            {"titulo": "84. La inferencia y la lectura entre líneas", "contenido": "Habilidad para deducir información implícita que el autor no menciona de forma explícita en el texto."},
            {"titulo": "85. La importancia del contexto en la interpretación de un texto", "contenido": "Consideración de la época, el autor y la cultura para interpretar correctamente el significado de un texto."},
            {"titulo": "86. La paráfrasis y el resumen", "contenido": "Diferencia entre parafrasear (reformular un texto con palabras propias) y resumir (acortar un texto a sus ideas principales)."},
            {"titulo": "87. La escritura creativa y sus elementos", "contenido": "Práctica de los elementos clave de la escritura creativa: personajes, ambientación, narrador y diálogo."},
            {"titulo": "88. La importancia de la revisión y corrección de textos", "contenido": "Reconocimiento de la importancia de la revisión para detectar errores de ortografía, gramática y coherencia."},
            {"titulo": "89. El informe y el reporte", "contenido": "Análisis de la estructura y el propósito del informe, que presenta datos de forma objetiva y organizada."},
            {"titulo": "90. La publicidad y la persuasión", "contenido": "Análisis de las estrategias retóricas y argumentativas que utiliza la publicidad para persuadir al público."},
            {"titulo": "91. El discurso político y la retórica", "contenido": "Análisis de las figuras retóricas y los recursos de persuasión más comunes en el discurso político."},
            {"titulo": "92. La lectura crítica y sus estrategias", "contenido": "Habilidad para evaluar un texto, cuestionar las ideas del autor y formarse una opinión propia."},
            {"titulo": "93. El discurso oral y sus características", "contenido": "Análisis de los elementos clave del discurso oral: entonación, pausas, gestos y contacto visual."},
            {"titulo": "94. La estructura de un artículo de opinión", "contenido": "Análisis del formato del artículo de opinión, que combina la información con la valoración personal del autor."},
            {"titulo": "95. El uso de la ironía en la redacción", "contenido": "Utilización de la ironía como recurso para dar un toque de humor, crítica o doble sentido a un texto."},
            {"titulo": "96. La argumentación deductiva e inductiva", "contenido": "Diferencias entre la argumentación que va de lo general a lo particular (deductiva) y la que va al revés (inductiva)."},
            {"titulo": "97. La importancia del vocabulario en la expresión", "contenido": "Uso de un vocabulario amplio y preciso para mejorar la claridad y la elegancia de la expresión oral y escrita."},
            {"titulo": "98. La paráfrasis de textos científicos y técnicos", "contenido": "Técnicas para reformular textos de carácter científico, manteniendo la precisión y la exactitud de la información."},
            {"titulo": "99. La comunicación no verbal en la exposición oral", "contenido": "Análisis de los gestos, la postura y las expresiones faciales como elementos clave en la comunicación no verbal."},
            {"titulo": "100. El análisis de un poema de un autor contemporáneo", "contenido": "Aplicación de los conocimientos de métrica, ritmo, figuras retóricas y temas a un poema de un autor actual."},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Lengua Castellana (9no Grado)", font=("Helvetica", 20, "bold"), background="#f0f0f0")
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
        filename = "parafrasis_lengua_castellana_9no_tkinter.txt"
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
