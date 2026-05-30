# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (6to Grado - Lengua Castellana)
# 100 EJERCICIOS DE PARÁFRASIS
# ==============================================================================
# Esta aplicación recrea la funcionalidad del programa anterior de Kivy,
# utilizando la librería estándar de Python, Tkinter. Permite a los estudiantes
# de sexto grado practicar la paráfrasis de conceptos de Lengua Castellana
# y ofrece la funcionalidad de revisión y edición de respuestas.
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
        self.root.title("Ejercicios de Lengua Castellana (6to Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para sexto grado
        # La lista es idéntica a la versión de Kivy para mantener la consistencia
        self.ejercicios = [
            # SECCIÓN 1: GRAMÁTICA (Sintaxis y Morfología)
            {"titulo": "1. El Sujeto y el Predicado", "contenido": "En una oración, el sujeto es la persona, animal o cosa que realiza la acción o de quien se dice algo. El predicado es lo que se dice del sujeto."},
            {"titulo": "2. Sustantivos Propios y Comunes", "contenido": "Los sustantivos comunes nombran a cualquier ser o cosa de una misma clase. Los sustantivos propios nombran a un ser o cosa en particular y se escriben con mayúscula."},
            {"titulo": "3. El Adjetivo Calificativo", "contenido": "El adjetivo es la palabra que describe o califica al sustantivo. Por ejemplo, 'la casa grande' o 'el perro peludo'."},
            {"titulo": "4. Artículos Determinados e Indeterminados", "contenido": "Los artículos determinados (el, la, los, las) especifican un sustantivo. Los artículos indeterminados (un, una, unos, unas) lo presentan de manera general."},
            {"titulo": "5. Tipos de Verbos", "contenido": "Los verbos son palabras que indican acción, estado o proceso. Pueden ser regulares o irregulares, transitivos o intransitivos."},
            {"titulo": "6. Modos Verbales: Indicativo, Subjuntivo e Imperativo", "contenido": "El modo indicativo expresa acciones reales y objetivas. El subjuntivo expresa deseos, dudas o posibilidades. El imperativo expresa órdenes."},
            {"titulo": "7. Pronombres Personales", "contenido": "Son palabras que sustituyen a los sustantivos para evitar la repetición. Por ejemplo: yo, tú, él, nosotros, ustedes, ellos."},
            {"titulo": "8. El Adverbio", "contenido": "El adverbio modifica al verbo, al adjetivo o a otro adverbio, indicando circunstancias de lugar, tiempo, modo o cantidad."},
            {"titulo": "9. Preposiciones y Conjunciones", "contenido": "Las preposiciones (a, ante, bajo...) enlazan palabras. Las conjunciones (y, o, pero...) enlazan oraciones o palabras del mismo tipo."},
            {"titulo": "10. La Oración Simple", "contenido": "Una oración simple es aquella que tiene un solo verbo conjugado y, por lo tanto, un solo predicado."},
            {"titulo": "11. El Complemento Directo (CD)", "contenido": "El complemento directo recibe directamente la acción del verbo. Para encontrarlo, se pregunta '¿Qué?' o '¿A quién?' al verbo."},
            {"titulo": "12. El Complemento Indirecto (CI)", "contenido": "El complemento indirecto se beneficia o perjudica de la acción del verbo. Se identifica con las preguntas '¿A quién?' o '¿Para quién?'."},
            {"titulo": "13. Análisis Morfológico", "contenido": "Consiste en clasificar las palabras de una oración según su categoría gramatical: sustantivo, adjetivo, verbo, etc."},
            {"titulo": "14. Palabras Derivadas y Compuestas", "contenido": "Las palabras derivadas se forman añadiendo prefijos o sufijos a una raíz. Las compuestas se forman uniendo dos o más palabras."},
            {"titulo": "15. La Aposición", "contenido": "Es un sustantivo o grupo de palabras que acompaña a otro sustantivo para explicarlo o especificarlo. Puede ser explicativa o especificativa."},
            {"titulo": "16. Los Determinantes Posesivos", "contenido": "Son palabras que indican a quién pertenece el sustantivo. Por ejemplo: mi, tu, su, nuestro, vuestro."},
            {"titulo": "17. Los Determinantes Demostrativos", "contenido": "Indican la distancia del sustantivo con respecto al hablante. Por ejemplo: este, ese, aquel."},
            {"titulo": "18. Verbos Copulativos", "contenido": "Son verbos (ser, estar, parecer) que no indican una acción, sino que unen el sujeto con una cualidad (atributo)."},
            {"titulo": "19. Los Adverbios de Lugar y de Tiempo", "contenido": "Los de lugar indican dónde ocurre la acción (aquí, allí, cerca). Los de tiempo indican cuándo (ayer, hoy, pronto)."},
            {"titulo": "20. Concordancia Gramatical", "contenido": "Es la relación de coincidencia de género y número que existe entre el sustantivo y el adjetivo, o entre el sujeto y el verbo."},
            {"titulo": "21. El Complemento Circunstancial", "contenido": "Indica las circunstancias en las que ocurre la acción del verbo (lugar, tiempo, modo, cantidad, causa, etc.)."},
            {"titulo": "22. Clases de Sintagmas", "contenido": "Un sintagma es un grupo de palabras que cumple una función. Los principales son nominal, verbal, adjetival y adverbial."},
            {"titulo": "23. Oraciones Coordinadas y Subordinadas", "contenido": "Las oraciones coordinadas son independientes. Las subordinadas dependen de la oración principal para tener sentido."},
            {"titulo": "24. El Verbo y sus Accidentes Gramaticales", "contenido": "El verbo cambia para indicar persona, número, tiempo y modo. Estas variaciones se llaman accidentes gramaticales."},
            {"titulo": "25. Verbos Transitivos e Intransitivos", "contenido": "Los verbos transitivos necesitan un complemento directo. Los intransitivos no lo necesitan."},
            # SECCIÓN 2: ORTOGRAFÍA Y ACENTUACIÓN
            {"titulo": "26. Reglas Generales de Acentuación", "contenido": "Las palabras agudas se acentúan si terminan en n, s o vocal. Las graves si no terminan en n, s o vocal. Las esdrújulas siempre."},
            {"titulo": "27. El Diptongo y el Triptongo", "contenido": "El diptongo es la unión de dos vocales en una misma sílaba. El triptongo es la unión de tres vocales."},
            {"titulo": "28. El Hiato", "contenido": "El hiato es la separación de dos vocales contiguas en sílabas diferentes. Se produce al unir dos vocales fuertes o una fuerte y una débil tónica."},
            {"titulo": "29. Uso de la `b` y la `v`", "contenido": "Se escribe `b` antes de `l` y `r`. Se escribe `v` después de la sílaba `ad`."},
            {"titulo": "30. Uso de la `g` y la `j`", "contenido": "Se usa `g` con los sonidos `ge` y `gi` si no son palabras que terminan en `-jería` o `-jero`. La `j` se usa antes de `a`, `o`, `u` y en palabras con sonido `ge`, `gi`."},
            {"titulo": "31. Uso de la `h`", "contenido": "La `h` es muda en español. Se usa en palabras que inician con `hie-` o `hue-` y en palabras de origen griego como `hidro-`."},
            {"titulo": "32. Signos de Puntuación: la Coma", "contenido": "La coma se usa para separar elementos de una enumeración, vocativos, aclaraciones y oraciones subordinadas cortas."},
            {"titulo": "33. Signos de Puntuación: el Punto", "contenido": "El punto se usa para marcar el final de una oración (punto y seguido), de un párrafo (punto y aparte) o de un texto (punto final)."},
            {"titulo": "34. Puntos Suspensivos", "contenido": "Se usan para indicar una interrupción en el discurso, duda, temor, o para dejar una idea sin terminar."},
            {"titulo": "35. Uso de Mayúsculas", "contenido": "Se usan al inicio de un texto, después de un punto y en nombres propios (personas, lugares, instituciones)."},
            {"titulo": "36. Palabras Homófonas", "contenido": "Son palabras que suenan igual pero se escriben diferente y tienen significados distintos. Ej: 'hay' y 'ay'."},
            {"titulo": "37. Uso de los Paréntesis", "contenido": "Se usan para insertar información adicional, aclaraciones o datos que no son esenciales para la oración."},
            {"titulo": "38. Uso de la `c`, la `s` y la `z`", "contenido": "La `c` suena como `s` o `z`. La `s` tiene un sonido sordo. La `z` suena como `c` antes de `e`, `i`."},
            {"titulo": "39. Uso de la `ll` y la `y`", "contenido": "Ambos fonemas tienen un sonido similar en la mayoría de los países. La `ll` proviene de un dígrafo, la `y` de una vocal o consonante."},
            {"titulo": "40. Palabras con `cc` y `xc`", "contenido": "Se usa `cc` cuando el sonido de la `c` doble es claro. Ej: `acción`. Se usa `xc` en palabras como `excelente`."},
            {"titulo": "41. La Acentuación de Diptongos e Hiatos", "contenido": "Si un diptongo se rompe con una tilde, se convierte en un hiato. Ej: `país`. Si la tilde va en la vocal fuerte del diptongo, se mantiene. Ej: `camión`."},
            {"titulo": "42. Signos de Interrogación y Exclamación", "contenido": "Se usan para formular preguntas y expresar sorpresa, emoción o énfasis. En español, se abren (`¿` y `¡`) y se cierran (`?` y `!`)."},
            {"titulo": "43. El Uso de los Dos Puntos", "contenido": "Se usan para introducir una enumeración, una cita textual o una explicación. Ej: 'Me gusta esto: la música, el cine y los libros'."},
            {"titulo": "44. Uso de la `r` y la `rr`", "contenido": "La `r` tiene un sonido suave al inicio de sílaba y al final de palabra. La `rr` tiene un sonido fuerte y va entre vocales."},
            {"titulo": "45. La Raya o Guion Largo", "contenido": "Se utiliza para introducir las intervenciones de los personajes en un diálogo y para encerrar aclaraciones en un texto."},
            {"titulo": "46. Uso del Punto y Coma", "contenido": "Se usa para separar elementos de una enumeración compleja o para unir oraciones que tienen una estrecha relación entre sí."},
            {"titulo": "47. Acentuación de Palabras Compuestas", "contenido": "Cuando dos palabras se unen, la primera pierde su tilde y la segunda la mantiene si la tiene. Ej: `décimo` + `séptimo` -> `decimoséptimo`."},
            {"titulo": "48. El Guion", "contenido": "Se usa para dividir palabras al final de un renglón o para unir elementos de palabras compuestas. Ej: `franco-español`."},
            {"titulo": "49. El Uso de las Comillas", "contenido": "Se usan para encerrar citas textuales, títulos de obras, ironías o palabras extranjeras."},
            {"titulo": "50. Las Palabras Monosílabas", "contenido": "Generalmente no se acentúan, excepto cuando se usa la tilde diacrítica para diferenciarlas de otras. Ej: `tú` (pronombre) vs. `tu` (posesivo)."},
            # SECCIÓN 3: LECTURA CRÍTICA Y COMPRENSIÓN
            {"titulo": "51. Idea Principal vs. Ideas Secundarias", "contenido": "La idea principal es el mensaje central de un párrafo o texto. Las ideas secundarias amplían, detallan o explican la idea principal."},
            {"titulo": "52. Resumen y Síntesis", "contenido": "Un resumen es una versión corta del texto original que mantiene las ideas principales. Una síntesis relaciona las ideas de varios textos."},
            {"titulo": "53. El Propósito del Autor", "contenido": "El propósito puede ser informar, persuadir, entretener o exponer un punto de vista. Identificarlo es clave para la comprensión."},
            {"titulo": "54. Inferir Información", "contenido": "Es la habilidad de deducir información que no está explícitamente escrita en el texto, basándose en pistas y conocimientos previos."},
            {"titulo": "55. Textos Narrativos", "contenido": "Cuentan una historia con personajes, un narrador, un espacio y un tiempo. Los elementos clave son el inicio, el nudo y el desenlace."},
            {"titulo": "56. Textos Descriptivos", "contenido": "Presentan las características de un ser, objeto, lugar o proceso. Utilizan adjetivos y comparaciones."},
            {"titulo": "57. Textos Expositivos", "contenido": "Tienen como objetivo informar y explicar un tema de forma clara y objetiva. Su estructura es introducción, desarrollo y conclusión."},
            {"titulo": "58. Textos Argumentativos", "contenido": "Buscan convencer al lector de una idea o postura. Presentan una tesis y argumentos para defenderla."},
            {"titulo": "59. El Contexto de una Palabra", "contenido": "El contexto es el entorno de palabras o frases que rodea a una palabra. Es fundamental para entender su significado en un texto."},
            {"titulo": "60. La Intención Comunicativa", "contenido": "Es el objetivo que tiene el emisor al transmitir un mensaje. Puede ser informar, convencer, conmover, etc."},
            {"titulo": "61. Claves Contextuales", "contenido": "Son las palabras o frases que nos ayudan a entender el significado de un término desconocido. Ej: sinónimos o ejemplos."},
            {"titulo": "62. Cohesión y Coherencia", "contenido": "La cohesión es la conexión gramatical y léxica entre las partes de un texto. La coherencia es la conexión lógica de las ideas."},
            {"titulo": "63. Textos Funcionales", "contenido": "Son textos que tienen un propósito práctico y una estructura definida. Ej: un manual de instrucciones o una carta."},
            {"titulo": "64. Hechos y Opiniones", "contenido": "Un hecho es un suceso real y verificable. Una opinión es un juicio o punto de vista personal que no siempre es verificable."},
            {"titulo": "65. La Voz del Narrador", "contenido": "Puede ser en primera persona (protagonista), segunda persona (interpela al lector) o tercera persona (observador externo)."},
            {"titulo": "66. Elementos de la Comunicación", "contenido": "Emisor, receptor, mensaje, canal, código y contexto. Todos son necesarios para que la comunicación sea efectiva."},
            {"titulo": "67. La Estructura de un Ensayo", "contenido": "Se compone de tres partes: introducción (se presenta la tesis), desarrollo (se exponen los argumentos) y conclusión (se reitera la tesis)."},
            {"titulo": "68. Palabras Sinónimas y Antónimas", "contenido": "Los sinónimos son palabras con significado similar. Los antónimos son palabras con significado opuesto."},
            {"titulo": "69. Textos Poéticos", "contenido": "Buscan crear una experiencia estética a través del ritmo, la musicalidad y las figuras retóricas. Se dividen en versos y estrofas."},
            {"titulo": "70. La Biografía y la Autobiografía", "contenido": "Una biografía narra la vida de otra persona. Una autobiografía narra la propia vida del autor."},
            {"titulo": "71. Comprensión Lectora Literal", "contenido": "Es entender lo que el texto dice explícitamente, sin interpretaciones."},
            {"titulo": "72. Comprensión Lectora Inferencial", "contenido": "Es interpretar y deducir la información que no está explícitamente en el texto."},
            {"titulo": "73. Comprensión Lectora Crítica", "contenido": "Es evaluar el texto, el propósito del autor, los argumentos y la calidad de la información."},
            {"titulo": "74. El Tema de un Texto", "contenido": "El tema es el asunto principal del que trata el texto, expresado en una o pocas palabras. Ej: 'el amor', 'la amistad'."},
            {"titulo": "75. La Paráfrasis", "contenido": "Consiste en decir con tus propias palabras lo que un texto dice, sin alterar la idea original."},
            # SECCIÓN 4: REDACCIÓN Y FIGURAS LITERARIAS
            {"titulo": "76. Los Conectores Lógicos", "contenido": "Son palabras o frases que unen oraciones y párrafos, dándole fluidez y coherencia al texto. Ej: `además`, `sin embargo`, `por lo tanto`."},
            {"titulo": "77. Escribir un Párrafo", "contenido": "Un párrafo debe tener una idea principal y varias ideas secundarias que la apoyen, con oraciones conectadas entre sí."},
            {"titulo": "78. La Metáfora", "contenido": "Figura retórica que consiste en nombrar una cosa con el nombre de otra, estableciendo una relación de semejanza. Ej: 'Su cabello es de oro'."},
            {"titulo": "79. El Símil o Comparación", "contenido": "Figura retórica que compara dos elementos usando palabras como `como`, `parece` o `tal como`. Ej: 'Sus ojos brillaban como dos estrellas'."},
            {"titulo": "80. La Personificación", "contenido": "Figura retórica que consiste en atribuir cualidades humanas a seres inanimados o animales. Ej: 'El viento silbaba en la ventana'."},
            {"titulo": "81. El Pleonasmo", "contenido": "Es una redundancia para enfatizar una idea. A veces es considerado un vicio del lenguaje. Ej: 'Subir arriba' o 'entrar adentro'."},
            {"titulo": "82. El Diálogo y el Monólogo", "contenido": "El diálogo es la conversación entre dos o más personajes. El monólogo es el discurso de un solo personaje consigo mismo."},
            {"titulo": "83. La Carta Informal", "contenido": "Se escribe a una persona cercana (amigo o familiar) con un lenguaje coloquial. Su estructura es: encabezamiento, saludo, cuerpo, despedida y firma."},
            {"titulo": "84. La Carta Formal", "contenido": "Se escribe a una institución o persona de autoridad con un lenguaje respetuoso. Su estructura es más estricta que la informal."},
            {"titulo": "85. La Descripción de Personajes", "contenido": "Puede ser prosopografía (físico), etopeya (psicológico) o retrato (combinación de ambos)."},
            {"titulo": "86. Las Figuras Retóricas", "contenido": "Son formas no convencionales de usar las palabras para darles expresividad, belleza o vivacidad. Ej: metáfora, hipérbole, etc."},
            {"titulo": "87. El Resumen", "contenido": "Es la exposición breve de lo esencial de un tema, texto o historia. El objetivo es condensar la información sin perder las ideas principales."},
            {"titulo": "88. Estructura de la Noticia Periodística", "contenido": "Debe responder a las 6 preguntas básicas: qué, quién, cuándo, dónde, por qué y cómo. La información más importante va al inicio (pirámide invertida)."},
            {"titulo": "89. Género Narrativo", "contenido": "Relata sucesos, reales o ficticios. Sus principales subgéneros son el cuento, la novela y la fábula."},
            {"titulo": "90. Género Lírico", "contenido": "Expresa los sentimientos del autor. Su forma más común es la poesía. Se caracteriza por el uso de la métrica y la rima."},
            {"titulo": "91. Género Dramático", "contenido": "Representa acciones a través del diálogo de personajes. Subgéneros: la tragedia, la comedia y el drama."},
            {"titulo": "92. La Fábula y la Moraleja", "contenido": "La fábula es una narración corta con personajes animales que al final deja una enseñanza moral, llamada moraleja."},
            {"titulo": "93. El Cuento y sus Elementos", "contenido": "Narración breve con pocos personajes y un solo conflicto central. Los elementos son: narrador, personajes, acción, espacio y tiempo."},
            {"titulo": "94. La Novela", "contenido": "Es una narración más extensa que el cuento, con una trama más compleja, más personajes y varios conflictos."},
            {"titulo": "95. El Uso de los Dos Puntos en Citas", "contenido": "Se usan para introducir una cita textual. Ej: 'El profesor dijo: \"Estudien para el examen\"'."},
            {"titulo": "96. La Hipérbole", "contenido": "Figura retórica que consiste en exagerar una idea o cualidad. Ej: 'Te he esperado un millón de años'."},
            {"titulo": "97. La Anáfora", "contenido": "Es la repetición de una o varias palabras al inicio de los versos o frases. Ej: '¡Qué triste estás! ¡Qué triste es la vida!'."},
            {"titulo": "98. El Lenguaje Coloquial y Formal", "contenido": "El lenguaje coloquial es el que usamos en la vida diaria. El formal se usa en situaciones que requieren más respeto. Ej: '¿Qué onda?' vs. '¿Cómo está usted?'."},
            {"titulo": "99. El Vocativo", "contenido": "Es la palabra o frase con la que nos dirigimos a alguien. Siempre va separado por comas. Ej: 'María, ven aquí'."},
            {"titulo": "100. Tipos de Textos", "contenido": "Pueden clasificarse según su intención comunicativa en narrativos, descriptivos, expositivos y argumentativos."}
        ]

        self.paraphrases = [None] * len(self.ejercicios)
        self.current_exercise_index = 0
        self.is_editing = False

        # Configuración de los estilos para una apariencia moderna
        style = ttk.Style()
        style.theme_use("clam")  # Usar un tema más moderno

        # --- Creación de los widgets principales ---

        # Frame principal para contener todos los elementos
        main_frame = ttk.Frame(root, padding="15 15 15 15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título principal
        title_label = ttk.Label(main_frame, text="Ejercicios de Lengua Castellana (6to Grado)", font=("Helvetica", 20, "bold"), background="#f0f0f0")
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
            status = "✅" if paraphrase else "❓"
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
        filename = "parafrasis_lengua_castellana_6to_tkinter.txt"
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
