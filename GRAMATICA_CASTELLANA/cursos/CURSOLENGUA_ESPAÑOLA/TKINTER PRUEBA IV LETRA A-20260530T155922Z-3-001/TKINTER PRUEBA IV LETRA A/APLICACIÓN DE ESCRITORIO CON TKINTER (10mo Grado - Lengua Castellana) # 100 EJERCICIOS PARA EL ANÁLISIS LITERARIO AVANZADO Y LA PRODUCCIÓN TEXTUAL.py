# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (10mo Grado - Lengua Castellana)
# 100 EJERCICIOS PARA EL ANÁLISIS LITERARIO AVANZADO Y LA PRODUCCIÓN TEXTUAL
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de décimo grado, profundizando
# en temas como el análisis de movimientos literarios del siglo XX, la crítica
# textual y la redacción de textos argumentativos complejos.
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
        self.root.title("Ejercicios de Lengua Castellana (10mo Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para décimo grado
        # Esta lista es idéntica a la versión de Kivy para mantener la consistencia
        self.ejercicios = [
            # SECCIÓN 1: GRAMÁTICA Y SINTAXIS AVANZADA (25 EJERCICIOS)
            {"titulo": "1. Oraciones subordinadas adverbiales de modo y lugar", "contenido": "Análisis de las proposiciones que indican cómo o dónde se realiza la acción del verbo principal. Ej: 'Lo hizo como le enseñaron'."},
            {"titulo": "2. Subordinadas adverbiales de tiempo y finalidad", "contenido": "Análisis de las proposiciones que indican cuándo o para qué se realiza la acción del verbo principal. Ej: 'Te llamaré cuando llegue'."},
            {"titulo": "3. Oraciones subordinadas concesivas y causales", "contenido": "Proposiciones que expresan una dificultad (concesiva) o la causa de una acción (causal). Ej: 'Aunque llovió, salí' vs 'Salí porque quería'."},
            {"titulo": "4. Subordinadas comparativas y consecutivas", "contenido": "Análisis de las proposiciones que comparan o indican la consecuencia de una acción. Ej: 'Es tan alto como su padre' vs 'Trabajó tanto que se cansó'."},
            {"titulo": "5. El uso de las perífrasis verbales de obligación y reiteración", "contenido": "Análisis de las estructuras 'tener que + infinitivo' y 'volver a + infinitivo' en la prosa. Ej: 'Tenía que estudiar' vs 'Volvió a llover'."},
            {"titulo": "6. El participio como adjetivo y verbo", "contenido": "Diferenciación del participio cuando funciona como modificador de un sustantivo o como parte de un tiempo verbal compuesto. Ej: 'La puerta cerrada' vs 'Ha cerrado la puerta'."},
            {"titulo": "7. Concordancia verbal en oraciones complejas", "contenido": "Análisis de los casos especiales de concordancia entre el sujeto y el verbo cuando están separados o el sujeto es un pronombre. Ej: 'La mayoría de los alumnos salió'."},
            {"titulo": "8. Los pronombres relativos y su función sintáctica", "contenido": "Reconocimiento de los pronombres relativos (que, quien, cual, cuyo) y su función de enlace entre oraciones. Ej: 'El libro que leí'."},
            {"titulo": "9. La oración simple, compuesta y compleja", "contenido": "Diferenciación entre las oraciones según el número de predicados y la forma en que se unen las proposiciones."},
            {"titulo": "10. El uso de la conjunción 'si' y la condicionalidad", "contenido": "Análisis de la forma correcta de expresar una condición en español. Ej: 'Si vienes, iremos'."},
            {"titulo": "11. La voz pasiva refleja con 'se'", "contenido": "Construcciones con 'se' y un verbo en tercera persona para expresar una acción pasiva. Ej: 'Se venden casas'"},
            {"titulo": "12. La función de los signos de puntuación en la prosa formal", "contenido": "Análisis del uso estilístico de la coma, el punto y coma y los dos puntos para dar ritmo y claridad."},
            {"titulo": "13. La nominalización y sus implicaciones estilísticas", "contenido": "Transformación de verbos en sustantivos para lograr un estilo más formal y objetivo. Ej: 'Cuando llegaron' -> 'A la llegada'."},
            {"titulo": "14. Errores de concordancia y vicios de la sintaxis", "contenido": "Identificación de la anacoluto y otros errores que rompen la coherencia sintáctica en una oración."},
            {"titulo": "15. El uso de la aposición en la redacción académica", "contenido": "Uso de la aposición como recurso para aclarar o expandir información sobre un sustantivo. Ej: 'Cervantes, el autor del Quijote...'"},
            {"titulo": "16. Oraciones subordinadas de relativo sin antecedente expreso", "contenido": "Análisis de oraciones de relativo donde el antecedente está implícito. Ej: 'Quien ríe el último...'"},
            {"titulo": "17. El gerundio y la expresión de la simultaneidad", "contenido": "Uso correcto del gerundio para expresar una acción simultánea a la del verbo principal. Ej: 'Salió corriendo'."},
            {"titulo": "18. Los conectores textuales y su función lógica", "contenido": "Uso de conectores (además, sin embargo, por consiguiente) para dar coherencia y cohesión a un texto."},
            {"titulo": "19. Análisis de la estructura del sintagma nominal complejo", "contenido": "Reconocimiento del núcleo, el modificador directo, el indirecto y las aposiciones en un sintagma nominal."},
            {"titulo": "20. La correlación de tiempos verbales en el discurso indirecto", "contenido": "Análisis de cómo cambian los tiempos verbales cuando se reproduce lo que alguien dijo en pasado. Ej: 'Dijo que había ido'."},
            {"titulo": "21. El uso del infinitivo con valor de imperativo", "contenido": "Análisis de la forma en que el infinitivo se utiliza en algunas construcciones con valor de orden. Ej: 'No fumar'."},
            {"titulo": "22. La oración de relativo de valor explicativo y especificativo", "contenido": "Diferenciación entre las oraciones de relativo que aclaran (entre comas) y las que restringen (sin comas)."},
            {"titulo": "23. Los verbos 'ser', 'estar' y 'haber' con valor de existencia", "contenido": "Análisis del uso de estos verbos para indicar la existencia o no de algo. Ej: 'Hay un libro' vs 'El libro está ahí'."},
            {"titulo": "24. La cohesión y la coherencia en un párrafo", "contenido": "Identificación de los mecanismos que dan unidad de sentido y fluidez a un texto: repeticiones, pronombres, sinónimos."},
            {"titulo": "25. La ambigüedad sintáctica y sus causas", "contenido": "Identificación de construcciones que pueden tener más de un significado debido a la sintaxis. Ej: 'Vi un hombre con un telescopio'."},

            # SECCIÓN 2: LITERATURA ESPAÑOLA Y LATINOAMERICANA DEL SIGLO XX (25 EJERCICIOS)
            {"titulo": "26. El Modernismo: Rubén Darío y la búsqueda de la belleza", "contenido": "Análisis del Modernismo como movimiento estético y de la obra de Rubén Darío, su máximo exponente."},
            {"titulo": "27. La Generación del 98: Unamuno y el 'sentimiento trágico'", "contenido": "Análisis de los temas existenciales y de la identidad española en la prosa de Miguel de Unamuno."},
            {"titulo": "28. Antonio Machado y la estética de la soledad y el paisaje", "contenido": "Estudio de la poesía de Antonio Machado, su melancolía y la relación con el paisaje castellano."},
            {"titulo": "29. Las Vanguardias Españolas: el Creacionismo de Huidobro", "contenido": "Análisis de la Vanguardia y la idea de que el poeta debe crear, no imitar, una nueva realidad en el poema."},
            {"titulo": "30. La Generación del 27: Lorca y la poesía neopopular", "contenido": "Estudio de la obra de Federico García Lorca y su fusión de la poesía popular andaluza con las técnicas vanguardistas."},
            {"titulo": "31. La novela de posguerra: el Tremendismo de Cela", "contenido": "Análisis del tremendismo, un estilo narrativo que retrata la realidad de forma cruda y violenta, en la obra de Camilo José Cela."},
            {"titulo": "32. El Existencialismo en la literatura de posguerra", "contenido": "Análisis de temas como la angustia, la libertad y el absurdo de la existencia en la novela de la posguerra española."},
            {"titulo": "33. La novela social de los años 50 y la crítica", "contenido": "Estudio de la novela que retrata las desigualdades sociales y las condiciones de vida de la clase obrera en la España franquista."},
            {"titulo": "34. El Realismo Mágico en Gabriel García Márquez", "contenido": "Análisis del Realismo Mágico, la inclusión de elementos fantásticos en un entorno realista, en 'Cien años de soledad'."},
            {"titulo": "35. La narrativa del 'Boom': Cortázar y la estructura del relato", "contenido": "Análisis de la obra de Julio Cortázar y su experimentación con la narrativa no lineal, los finales abiertos y el lector activo."},
            {"titulo": "36. El cuento latinoamericano moderno", "contenido": "Análisis de los elementos clave del cuento hispanoamericano en autores como Borges y Rulfo."},
            {"titulo": "37. El teatro de Buero Vallejo y el problema existencial", "contenido": "Análisis de la obra de Buero Vallejo, su crítica social y su enfoque en la condición humana."},
            {"titulo": "38. La poesía de la experiencia en Luis García Montero", "contenido": "Análisis del movimiento poético español que busca una conexión con la realidad cotidiana y la experiencia personal."},
            {"titulo": "39. La novela negra en la literatura española", "contenido": "Análisis de las características de la novela negra, como el detective desencantado y la crítica a la corrupción social."},
            {"titulo": "40. El microcuento contemporáneo y sus características", "contenido": "Análisis del género del microcuento, su brevedad, su capacidad de sugerencia y su final inesperado."},
            {"titulo": "41. La poesía de la Generación del 50 en Latinoamérica", "contenido": "Análisis de la poesía de autores como Octavio Paz o Pablo Neruda y sus temas existenciales y sociales."},
            {"titulo": "42. El teatro del absurdo: Ionesco y Beckett", "contenido": "Análisis del teatro que rompe con la lógica y la comunicación para reflejar la falta de sentido de la existencia."},
            {"titulo": "43. La novela de formación ('bildungsroman')", "contenido": "Análisis del género que narra el desarrollo psicológico y moral de un personaje desde la infancia a la madurez."},
            {"titulo": "44. La intertextualidad en la novela moderna", "contenido": "Reconocimiento de las referencias a otras obras literarias, históricas o culturales dentro de un texto."},
            {"titulo": "45. El ensayo literario como género de reflexión", "contenido": "Análisis del ensayo literario, su estructura y su función de reflexión personal sobre temas culturales o filosóficos."},
            {"titulo": "46. La poesía posmoderna y el fragmento", "contenido": "Análisis de la poesía que rompe con las grandes narrativas y utiliza el fragmento y el collage como forma de expresión."},
            {"titulo": "47. La literatura del exilio español", "contenido": "Estudio de la obra de los autores que se vieron obligados a abandonar España tras la Guerra Civil y sus temas de desarraigo."},
            {"titulo": "48. El teatro contemporáneo en Latinoamérica", "contenido": "Análisis de las tendencias del teatro actual, su experimentación con el lenguaje y su crítica social."},
            {"titulo": "49. El surrealismo en la literatura", "contenido": "Análisis de los elementos surrealistas (sueños, irracionalidad, subconsciente) en la poesía y la prosa."},
            {"titulo": "50. La novela del Neorrealismo italiano y su influencia", "contenido": "Análisis de la novela que busca retratar la realidad de la posguerra con un enfoque en los personajes ordinarios."},

            # SECCIÓN 3: RETÓRICA Y ANÁLISIS CRÍTICO (25 EJERCICIOS)
            {"titulo": "51. La Lítotes y la atenuación de una afirmación", "contenido": "Figura retórica que consiste en negar lo contrario de lo que se quiere afirmar. Ej: 'No está nada mal' para decir 'está muy bien'."},
            {"titulo": "52. El Oxímoron y la unión de términos opuestos", "contenido": "Figura retórica que une dos palabras con significados contradictorios. Ej: 'Un silencio atronador'."},
            {"titulo": "53. El Eufemismo y el disfemismo en el lenguaje político", "contenido": "Análisis de cómo se utilizan estos recursos para suavizar o endurecer una idea en el discurso político. Ej: 'Daño colateral' vs 'matanza'."},
            {"titulo": "54. La metáfora compleja y su función poética", "contenido": "Análisis de metáforas que no son directas y que requieren un esfuerzo de interpretación. Ej: 'El sol es una naranja en la mano del ciego'."},
            {"titulo": "55. El paralelismo sintáctico y su efecto rítmico", "contenido": "Repetición de la misma estructura gramatical en varias oraciones para generar un efecto de musicalidad. Ej: 'Por tu amor, por tu dolor'."},
            {"titulo": "56. La interpelación retórica y su uso en la oratoria", "contenido": "Pregunta que no espera respuesta y que se utiliza para persuadir o hacer reflexionar al público. Ej: '¿Acaso no te importa?'"},
            {"titulo": "57. La ironía dramática y la ironía socrática", "contenido": "Diferenciación entre la ironía en el teatro (el público sabe algo que el personaje no) y la ironía para llevar al interlocutor a la contradicción."},
            {"titulo": "58. El 'pathos' y el 'logos' en la argumentación", "contenido": "Análisis de las estrategias para apelar a las emociones (pathos) o a la lógica (logos) en un discurso."},
            {"titulo": "59. La tesis y el argumento en el ensayo", "contenido": "Identificación de la idea principal del ensayo (tesis) y de las razones que la sustentan (argumentos)."},
            {"titulo": "60. El comentario de texto literario: elementos clave", "contenido": "Análisis de la estructura del comentario de texto: contextualización, análisis del contenido y la forma, y conclusión."},
            {"titulo": "61. La reseña crítica y su valoración de una obra", "contenido": "Análisis de la reseña, un texto que combina el resumen de una obra con una opinión personal fundamentada."},
            {"titulo": "62. El editorial periodístico y su función de opinión", "contenido": "Análisis del editorial como texto de opinión que refleja la postura de un medio de comunicación."},
            {"titulo": "63. El aforismo y la sentencia", "contenido": "Análisis del aforismo como una máxima o sentencia breve que condensa una idea o una verdad moral. Ej: 'Lo bueno, si breve, dos veces bueno'."},
            {"titulo": "64. El prólogo y el epílogo en una obra", "contenido": "Análisis de la función del prólogo (presentar la obra) y el epílogo (cerrar la historia o reflexionar)."},
            {"titulo": "65. La parodia y la sátira en la literatura", "contenido": "Diferenciación entre la parodia (imitación burlesca) y la sátira (crítica social con humor)."},
            {"titulo": "66. La Retórica de Aristóteles: los 3 pilares de la persuasión", "contenido": "Análisis de los pilares de la persuasión: el ethos (autoridad), el pathos (emoción) y el logos (lógica)."},
            {"titulo": "67. Análisis de la voz narrativa en la novela de la Generación del 27", "contenido": "Estudio de las diferentes voces narrativas utilizadas en las obras de esta generación."},
            {"titulo": "68. El comentario de un guion de cine o teatro", "contenido": "Análisis de los elementos clave de un guion: diálogos, acotaciones, estructura, personajes."},
            {"titulo": "69. La intertextualidad como recurso estilístico", "contenido": "Reconocimiento de las citas o alusiones a otros textos que enriquecen el significado de una obra."},
            {"titulo": "70. La lectura crítica: cómo cuestionar un texto", "contenido": "Desarrollo de estrategias para no aceptar un texto pasivamente, sino para cuestionar las ideas del autor."},
            {"titulo": "71. El chiasmus y la inversión de elementos", "contenido": "Figura retórica que consiste en la repetición de palabras o estructuras en orden inverso. Ej: 'Ni son todos los que están, ni están todos los que son'."},
            {"titulo": "72. La importancia del contexto en la interpretación de un texto", "contenido": "Consideración del momento histórico, social y cultural para comprender plenamente un texto."},
            {"titulo": "73. El análisis de la trama y el clímax en una obra de teatro", "contenido": "Identificación de los momentos de mayor tensión y del desarrollo del conflicto en una obra teatral."},
            {"titulo": "74. El análisis del ritmo y la métrica en un poema", "contenido": "Estudio de la medida de los versos, las estrofas, la rima y la musicalidad de la poesía."},
            {"titulo": "75. La función del punto de vista en el relato", "contenido": "Análisis de cómo la elección del narrador influye en la información que se da al lector y en la percepción de los hechos."},

            # SECCIÓN 4: PRODUCCIÓN TEXTUAL Y ARGUMENTACIÓN (25 EJERCICIOS)
            {"titulo": "76. La redacción de una tesis argumentativa", "contenido": "Formulación de una tesis clara y debatible para un ensayo o un artículo de opinión. Ej: 'Las redes sociales afectan la salud mental de los jóvenes'."},
            {"titulo": "77. Estructura de un ensayo académico", "contenido": "Planificación y desarrollo de la estructura formal de un ensayo: introducción, desarrollo, conclusión y bibliografía."},
            {"titulo": "78. La redacción de un informe de investigación", "contenido": "Elaboración de un informe formal que presenta datos, metodología y conclusiones de forma objetiva y ordenada."},
            {"titulo": "79. La contraargumentación y la refutación", "contenido": "Técnicas para anticipar y rebatir los argumentos del oponente en un debate o en un texto argumentativo."},
            {"titulo": "80. El discurso persuasivo en la publicidad", "contenido": "Análisis de las estrategias retóricas y emocionales que utiliza la publicidad para convencer a la audiencia."},
            {"titulo": "81. La carta de solicitud formal", "contenido": "Redacción de una carta para solicitar un empleo, una beca o cualquier otro trámite formal, con el lenguaje adecuado."},
            {"titulo": "82. La reseña cinematográfica y su estructura", "contenido": "Análisis de la estructura de una reseña de cine: resumen de la trama, crítica de los aspectos técnicos y valoración personal."},
            {"titulo": "83. La voz y el tono en la escritura de un editorial", "contenido": "Elección del tono (formal, crítico, objetivo) y la voz del autor para expresar la postura de un medio de comunicación."},
            {"titulo": "84. La redacción de un artículo de opinión", "contenido": "Creación de un artículo de opinión que combine información relevante con la valoración personal del autor, de forma clara y coherente."},
            {"titulo": "85. La importancia de la evidencia en la argumentación", "contenido": "Uso de datos, ejemplos y citas de expertos para respaldar y fortalecer los argumentos de un texto."},
            {"titulo": "86. La paráfrasis de un texto científico o técnico", "contenido": "Técnicas para reformular textos complejos, manteniendo la exactitud de la información sin alterar su significado."},
            {"titulo": "87. El discurso expositivo-argumentativo", "contenido": "Análisis de la combinación de la exposición (informar) y la argumentación (convencer) en un mismo texto."},
            {"titulo": "88. La importancia de la revisión y corrección de textos", "contenido": "Reconocimiento de la importancia de la revisión final para asegurar la claridad, la coherencia y la corrección gramatical de un texto."},
            {"titulo": "89. La estructura de un debate formal", "contenido": "Análisis de las fases de un debate: presentación de la tesis, argumentos, refutación, conclusiones y cierre."},
            {"titulo": "90. La elaboración de un resumen ejecutivo", "contenido": "Redacción de un resumen conciso y claro de un informe o documento extenso para los directivos o lectores sin tiempo."},
            {"titulo": "91. La comunicación no verbal en la exposición oral", "contenido": "Análisis del lenguaje corporal, la entonación y la mirada como elementos de persuasión en una exposición."},
            {"titulo": "92. La importancia del registro lingüístico", "contenido": "Elección del registro formal o informal según el público y el propósito comunicativo."},
            {"titulo": "93. El estilo literario en la prosa ensayística", "contenido": "Análisis del uso de recursos literarios (metáforas, hipérboles) en un ensayo para hacerlo más atractivo."},
            {"titulo": "94. La redacción de una monografía", "contenido": "Elaboración de una monografía, un trabajo de investigación extenso sobre un tema específico, con rigor y estructura."},
            {"titulo": "95. La creación de un texto narrativo con múltiples narradores", "contenido": "Práctica de la escritura de un relato donde la historia se cuenta desde el punto de vista de varios personajes."},
            {"titulo": "96. La importancia de la empatía en la comunicación", "contenido": "Análisis de cómo la empatía ayuda a adaptar el mensaje al interlocutor y a generar una mejor conexión."},
            {"titulo": "97. La estructura de una crítica de arte", "contenido": "Redacción de una crítica de arte que combine una descripción de la obra con una interpretación y una valoración personal."},
            {"titulo": "98. La elaboración de un currículum vitae", "contenido": "Redacción de un CV formal que resalte la experiencia, las habilidades y la formación de una persona para un puesto de trabajo."},
            {"titulo": "99. La paráfrasis y el plagio", "contenido": "Diferenciación entre la paráfrasis (reformular con palabras propias) y el plagio (copiar sin citar) de un texto."},
            {"titulo": "100. La redacción de un discurso de graduación", "contenido": "Elaboración de un discurso formal, inspirador y emotivo, adecuado para una ceremonia de graduación."},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Lengua Castellana (10mo Grado)", font=("Helvetica", 20, "bold"), background="#f0f0f0")
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
        filename = "parafrasis_lengua_castellana_10mo_tkinter.txt"
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
