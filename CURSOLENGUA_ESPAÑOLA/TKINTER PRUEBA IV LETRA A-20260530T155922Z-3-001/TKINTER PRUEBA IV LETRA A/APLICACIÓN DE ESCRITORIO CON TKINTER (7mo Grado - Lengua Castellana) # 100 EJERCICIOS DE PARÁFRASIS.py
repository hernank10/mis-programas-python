# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (7mo Grado - Lengua Castellana)
# 100 EJERCICIOS DE PARÁFRASIS
# ==============================================================================
# Esta aplicación recrea la funcionalidad del programa anterior de Kivy,
# utilizando la librería estándar de Python, Tkinter. Permite a los estudiantes
# de séptimo grado practicar la paráfrasis de conceptos de Lengua Castellana
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
        self.root.title("Ejercicios de Lengua Castellana (7mo Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para séptimo grado
        # La lista es idéntica a la versión de Kivy para mantener la consistencia
        self.ejercicios = [
            # SECCIÓN 1: GRAMÁTICA Y SINTAXIS AVANZADA
            {"titulo": "1. Oraciones Compuestas por Coordinación", "contenido": "Son oraciones formadas por dos o más proposiciones independientes unidas por conjunciones coordinantes (y, o, pero)."},
            {"titulo": "2. Oraciones Compuestas por Subordinación", "contenido": "Son oraciones donde una proposición (subordinada) depende de otra (principal) y no puede funcionar sola."},
            {"titulo": "3. Proposiciones Subordinadas Sustantivas", "contenido": "Funcionan como un sustantivo dentro de la oración principal, pudiendo ser sujeto, complemento directo, etc."},
            {"titulo": "4. Proposiciones Subordinadas Adjetivas", "contenido": "Funcionan como un adjetivo, es decir, modifican a un sustantivo de la oración principal. Introducidas por un pronombre relativo (que, quien, cual)."},
            {"titulo": "5. Proposiciones Subordinadas Adverbiales", "contenido": "Funcionan como un adverbio, modificando al verbo de la oración principal. Indican lugar, tiempo, modo, causa, etc."},
            {"titulo": "6. El Complemento Predicativo", "contenido": "Es una palabra que califica al sujeto y al verbo al mismo tiempo. Concuerda en género y número con el sujeto."},
            {"titulo": "7. La Voz Activa y la Voz Pasiva", "contenido": "En la voz activa el sujeto realiza la acción. En la voz pasiva, el sujeto recibe la acción. Ej: 'El niño come la manzana' (activa) vs. 'La manzana es comida por el niño' (pasiva)."},
            {"titulo": "8. El Análisis Sintáctico", "contenido": "Es el proceso de identificar las funciones de las palabras en una oración (sujeto, predicado, complementos, etc.)."},
            {"titulo": "9. Verbos Pronominales y Perífrasis Verbales", "contenido": "Los verbos pronominales necesitan un pronombre (ej: 'arrepentirse'). Las perífrasis verbales combinan dos verbos para expresar una acción (ej: 'ir a cantar')."},
            {"titulo": "10. El Complemento Agente", "contenido": "Aparece en oraciones de voz pasiva e indica quién realiza la acción. Siempre va introducido por la preposición 'por'."},
            {"titulo": "11. El Estilo Directo e Indirecto", "contenido": "El estilo directo reproduce literalmente lo dicho. El indirecto cuenta lo que alguien dijo sin usar sus palabras exactas."},
            {"titulo": "12. La Oración Impersonal", "contenido": "Es aquella que no tiene un sujeto gramatical. Ej: 'Llueve mucho' o 'Hace calor'."},
            {"titulo": "13. El Subjuntivo en Oraciones Subordinadas", "contenido": "Se usa para expresar hipótesis, deseos, dudas o emociones en las proposiciones subordinadas."},
            {"titulo": "14. Los Conectores de Causa y Consecuencia", "contenido": "Son palabras que unen oraciones indicando un motivo (porque, ya que) o un resultado (por lo tanto, en consecuencia)."},
            {"titulo": "15. Los Conectores de Oposición", "contenido": "Unen oraciones que presentan ideas contrarias o contrapuestas (pero, sin embargo, no obstante)."},
            {"titulo": "16. La Dequeísmo y Queísmo", "contenido": "El dequeísmo es el uso incorrecto de 'de que'. El queísmo es la omisión incorrecta de la preposición 'de' antes de 'que'."},
            {"titulo": "17. Oraciones Yuxtapuestas", "contenido": "Son oraciones que están unidas sin nexos, solo por signos de puntuación (coma, punto y coma)."},
            {"titulo": "18. Complemento del Nombre y del Adjetivo", "contenido": "El complemento del nombre es un grupo de palabras que modifica a un sustantivo. El del adjetivo modifica a un adjetivo."},
            {"titulo": "19. El Uso de Preposiciones", "contenido": "Las preposiciones son nexos que indican dirección, lugar, tiempo, causa, etc. Es importante usarlas correctamente."},
            {"titulo": "20. La Función del Pronombre Relativo", "contenido": "Los pronombres relativos (que, quien, cuyo) introducen proposiciones subordinadas adjetivas."},
            {"titulo": "21. El Estilo y Tono en la Escritura", "contenido": "El estilo es la manera particular de escribir. El tono es la actitud del autor hacia el tema (serio, irónico, humorístico)."},
            {"titulo": "22. Adjetivos y Pronombres Indefinidos", "contenido": "Indican una cantidad o identidad no precisa. Ej: 'muchos', 'pocos', 'alguien', 'nadie'."},
            {"titulo": "23. La Morfología de la Palabra", "contenido": "Estudia la estructura interna de las palabras y sus variaciones (morfemas, lexemas, prefijos, sufijos)."},
            {"titulo": "24. El Sintagma Preposicional", "contenido": "Es un grupo de palabras que empieza con una preposición y funciona como complemento de otro elemento."},
            {"titulo": "25. La Oración Subordinada Adverbial de Tiempo", "contenido": "Indica cuándo se realiza la acción de la oración principal. Se introduce con nexos como 'cuando', 'mientras', 'después de que'."},
            
            # SECCIÓN 2: ORTOGRAFÍA Y LÉXICO
            {"titulo": "26. Uso de Puntos Suspensivos", "contenido": "Indican una pausa intencionada, duda, o la omisión de una parte de un texto o enumeración."},
            {"titulo": "27. Uso de las Comillas", "contenido": "Se utilizan para citar palabras de otra persona, destacar una palabra o título, o indicar ironía."},
            {"titulo": "28. Palabras Homónimas y Parónimas", "contenido": "Las homónimas suenan y se escriben igual pero tienen distinto significado. Las parónimas suenan similar pero se escriben y significan distinto."},
            {"titulo": "29. La Tilde Diacrítica en Monosílabos", "contenido": "Se usa para diferenciar monosílabos que se escriben igual pero tienen diferente función gramatical. Ej: 'tú' vs. 'tu'."},
            {"titulo": "30. Acentuación de Palabras Compuestas", "contenido": "Si se unen palabras con guion, cada una mantiene su tilde. Sin guion, la primera la pierde."},
            {"titulo": "31. Uso de la `x` y la `s`", "contenido": "La `x` se usa en palabras que inician con 'ex-' o 'extra-'. La `s` en el sonido de 'z' y 'c' en algunos casos."},
            {"titulo": "32. Palabras con Doble Consonante", "contenido": "En español, solo se admiten `cc`, `ll`, `rr` y `nn`. Otras combinaciones son de origen extranjero."},
            {"titulo": "33. Los Dos Puntos en Cartas y Documentos", "contenido": "Se usan después de un saludo formal para dar paso al cuerpo del texto."},
            {"titulo": "34. Uso de la `b` y la `v` en prefijos", "contenido": "Se usa `b` en los prefijos `bi-`, `bene-` y `biblio-`. Se usa `v` en `vice-` y `vill-`."},
            {"titulo": "35. Uso de las Mayúsculas en Nombres Propios", "contenido": "Se escriben con mayúscula nombres de personas, lugares, instituciones, títulos de obras y de dignidades."},
            {"titulo": "36. La Acentuación de Adverbios terminados en `-mente`", "contenido": "Estos adverbios mantienen la tilde del adjetivo del que derivan. Ej: `fácil` -> `fácilmente`."},
            {"titulo": "37. Uso del Guion Largo (raya)", "contenido": "Se usa para las intervenciones de los personajes en un diálogo y para insertar aclaraciones extensas en un texto."},
            {"titulo": "38. Uso de los Paréntesis", "contenido": "Se usan para introducir aclaraciones, fechas, acrónimos o información adicional en un texto."},
            {"titulo": "39. Uso de la `j` y la `g` en los prefijos", "contenido": "Se usa `geo-`, `legi-` y `gen-` con `g`. Se usa `ej-` y `obj-` con `j`."},
            {"titulo": "40. Palabras con Acentuación Especial", "contenido": "Hay palabras que no siguen las reglas generales, como los adverbios interrogativos (dónde, cuándo, cómo)."},
            {"titulo": "41. La Elipsis", "contenido": "Es la omisión de un elemento de la oración (como un verbo) que se puede inferir del contexto."},
            {"titulo": "42. Los Arcaísmos y Neologismos", "contenido": "Los arcaísmos son palabras en desuso. Los neologismos son palabras nuevas que se han incorporado al idioma."},
            {"titulo": "43. La Tilde en los Demostrativos", "contenido": "Actualmente no se acentúan, pero antes se hacía para diferenciarlos de los pronombres demostrativos."},
            {"titulo": "44. Uso de la `i` y la `y`", "contenido": "La `i` es una vocal. La `y` puede ser vocal (al final de sílaba o palabra) o consonante (al inicio de sílaba)."},
            {"titulo": "45. Los Puntos Cardinales", "contenido": "Los puntos cardinales (norte, sur, este, oeste) se escriben con minúscula, excepto si forman parte de un nombre propio."},
            {"titulo": "46. Uso de los Dos Puntos para la Enumeración", "contenido": "Se usan para introducir una lista de elementos que se relacionan con lo dicho anteriormente."},
            {"titulo": "47. Acentuación en Palabras Interrogativas", "contenido": "Las palabras que introducen preguntas o exclamaciones siempre llevan tilde (qué, cómo, cuándo, dónde)."},
            {"titulo": "48. Los Puntos del Diálogo", "contenido": "Los signos de puntuación van fuera o dentro de las comillas o rayas, dependiendo de si son parte de la cita."},
            {"titulo": "49. Uso de `s` y `z` en los diminutivos", "contenido": "Se usa `c` para el diminutivo `-cito`, `-cita` en palabras que terminan en `z`."},
            {"titulo": "50. Los Extranjerismos", "contenido": "Son palabras de otros idiomas que se han incorporado al español. Es preferible usar una alternativa en español si existe."},

            # SECCIÓN 3: FIGURAS LITERARIAS Y GÉNEROS
            {"titulo": "51. La Hipérbole", "contenido": "Figura retórica de exageración, que aumenta o disminuye las cualidades de algo para crear un efecto. Ej: 'Tengo un hambre que me comería un elefante'."},
            {"titulo": "52. El Hipérbaton", "contenido": "Figura retórica que altera el orden gramatical de las palabras en la oración para darle un efecto estilístico. Ej: 'Volverán las oscuras golondrinas en tu balcón...'"},
            {"titulo": "53. La Antítesis", "contenido": "Figura retórica que opone dos ideas o palabras contrarias. Ej: 'Un pequeño paso para el hombre, un gran salto para la humanidad'."},
            {"titulo": "54. La Ironía", "contenido": "Figura retórica que consiste en decir lo contrario de lo que se piensa, para burlarse o criticar."},
            {"titulo": "55. La Personificación o Prosopopeya", "contenido": "Consiste en dar cualidades o acciones humanas a objetos inanimados o animales. Ej: 'El sol sonreía en la mañana'."},
            {"titulo": "56. La Onomatopeya", "contenido": "Figura retórica que imita sonidos de la naturaleza, animales o ruidos. Ej: 'El tic-tac del reloj'."},
            {"titulo": "57. La Metonimia", "contenido": "Consiste en designar una cosa con el nombre de otra con la que tiene una relación. Ej: 'Beber una copa' (el contenido de la copa)."},
            {"titulo": "58. El Oxímoron", "contenido": "Es la unión de dos palabras con significados opuestos en un mismo sintagma. Ej: 'un silencio ensordecedor'."},
            {"titulo": "59. La Epopeya", "contenido": "Subgénero narrativo en verso, extenso, que relata las hazañas de un héroe o un pueblo."},
            {"titulo": "60. La Tragedia", "contenido": "Subgénero dramático que presenta un conflicto serio y tiene un final fatal para el protagonista."},
            {"titulo": "61. La Comedia", "contenido": "Subgénero dramático que presenta situaciones divertidas y tiene un final feliz. Su objetivo es la risa y la crítica social."},
            {"titulo": "62. El Ensayo", "contenido": "Género literario en prosa que expone, analiza y comenta un tema desde un punto de vista personal y subjetivo."},
            {"titulo": "63. La Reseña", "contenido": "Es un texto que resume y critica una obra (libro, película, etc.), ofreciendo una opinión del autor de la reseña."},
            {"titulo": "64. El Editorial", "contenido": "Artículo periodístico que expresa la opinión del medio de comunicación sobre un tema de actualidad."},
            {"titulo": "65. El Artículo de Opinión", "contenido": "Texto periodístico donde un autor externo al medio expresa su punto de vista personal sobre un tema."},
            {"titulo": "66. La Novela de Aventuras", "contenido": "Género narrativo que se centra en viajes, peligros y hazañas de sus personajes."},
            {"titulo": "67. La Novela Histórica", "contenido": "Género narrativo que recrea un periodo o un acontecimiento histórico, con personajes reales y ficticios."},
            {"titulo": "68. La Lírica y la Épica", "contenido": "La lírica se centra en los sentimientos del autor. La épica relata hazañas heroicas."},
            {"titulo": "69. La Métrica y la Rima", "contenido": "La métrica es la medida de los versos. La rima es la coincidencia de sonidos al final de los versos."},
            {"titulo": "70. La Figura de Anáfora", "contenido": "Repetición de una o varias palabras al comienzo de frases o versos. Ej: 'Temprano levantó la muerte el vuelo, temprano madrugó la madrugada...'"},
            {"titulo": "71. El Paralelismo", "contenido": "Repetición de la misma estructura gramatical en dos o más versos o frases. Ej: 'La niña canta, el niño ríe.'"},
            {"titulo": "72. La Sinestesia", "contenido": "Mezcla de sensaciones de diferentes sentidos. Ej: 'Un olor azul'."},
            {"titulo": "73. La Alegoría", "contenido": "Es una metáfora continuada, una figura retórica que expresa una idea abstracta a través de una historia concreta."},
            {"titulo": "74. El Símbolo", "contenido": "Un objeto o imagen que representa una idea o concepto. Ej: la paloma blanca es símbolo de la paz."},
            {"titulo": "75. El Retrato", "contenido": "Descripción física (prosopografía) y moral (etopeya) de una persona."},

            # SECCIÓN 4: REDACCIÓN Y COMPRENSIÓN LECTORA
            {"titulo": "76. La Estructura de un Texto Argumentativo", "contenido": "Se compone de tres partes: la tesis (postura), los argumentos (razones) y la conclusión."},
            {"titulo": "77. Los Argumentos de Autoridad", "contenido": "Son aquellos que se basan en la opinión de un experto o una institución reconocida para respaldar una tesis."},
            {"titulo": "78. Los Argumentos de Ejemplificación", "contenido": "Son aquellos que se apoyan en ejemplos concretos para ilustrar una idea o reforzar una tesis."},
            {"titulo": "79. Tesis y Argumentos", "contenido": "La tesis es la idea que se defiende. Los argumentos son las razones que se usan para defenderla."},
            {"titulo": "80. El Párrafo de Causa-Efecto", "contenido": "Es aquel que explica las causas de un fenómeno y las consecuencias que provoca."},
            {"titulo": "81. El Párrafo de Comparación y Contraste", "contenido": "Es aquel que expone las semejanzas y diferencias entre dos o más objetos, ideas o personas."},
            {"titulo": "82. La Trama y el Tema", "contenido": "La trama es la sucesión de acontecimientos de una historia. El tema es la idea principal o central."},
            {"titulo": "83. La Moraleja", "contenido": "Es la enseñanza o lección moral que se extrae de una historia, especialmente de una fábula."},
            {"titulo": "84. La Subjetividad y la Objetividad", "contenido": "La subjetividad implica un punto de vista personal. La objetividad se basa en hechos, sin opiniones."},
            {"titulo": "85. La Intención del Autor en un Texto", "contenido": "El objetivo del autor al escribir. Puede ser informar, persuadir, entretener, conmover o criticar."},
            {"titulo": "86. El Subtexto", "contenido": "Es el significado o mensaje oculto que se encuentra debajo del texto literal. A menudo requiere de la inferencia."},
            {"titulo": "87. Estructura de la Noticia", "contenido": "Titular, entradilla, cuerpo y fotografía. La información más importante se presenta al inicio (pirámide invertida)."},
            {"titulo": "88. La Cohesión Textual", "contenido": "Son los mecanismos gramaticales y léxicos que conectan las diferentes partes de un texto. Ej: anáforas, elipsis."},
            {"titulo": "89. La Coherencia Textual", "contenido": "Es la relación lógica entre las ideas de un texto, que debe tener un sentido unitario y claro."},
            {"titulo": "90. La Caracterización de Personajes", "contenido": "Puede ser directa (el narrador lo describe) o indirecta (se revela a través de sus acciones o diálogos)."},
            {"titulo": "91. El Marco de la Historia", "contenido": "Es el lugar (espacio), el momento (tiempo) y las circunstancias en las que se desarrolla la historia."},
            {"titulo": "92. La Argumentación por Analogía", "contenido": "Se basa en la semejanza entre dos situaciones para argumentar. Ej: 'Si X funciona en A, funcionará en B'."},
            {"titulo": "93. El Debate", "contenido": "Es una forma de discusión formal en la que dos o más personas defienden posturas opuestas sobre un tema."},
            {"titulo": "94. Los Tipos de Lectura", "contenido": "Existen la lectura literal, la inferencial y la crítica, cada una con un nivel de profundidad diferente."},
            {"titulo": "95. El Tema y los Subtemas", "contenido": "El tema es la idea general de un texto. Los subtemas son las ideas secundarias que lo amplían y explican."},
            {"titulo": "96. La Reseña Crítica", "contenido": "Es un tipo de reseña que no solo resume, sino que evalúa el contenido, la estructura y el estilo de una obra."},
            {"titulo": "97. El Ensayo Argumentativo", "contenido": "Es un tipo de ensayo que tiene el objetivo de convencer al lector de una tesis a través de argumentos."},
            {"titulo": "98. Los Conectores de Adición", "contenido": "Se usan para agregar ideas en un texto (además, también, asimismo)."},
            {"titulo": "99. Los Conectores de Conclusión", "contenido": "Se usan para resumir o finalizar un texto (en conclusión, por último, en resumen)."},
            {"titulo": "100. El Uso de los Dos Puntos en un Discurso", "contenido": "Se usan para introducir una cita textual o un discurso después de verbos como 'dijo', 'afirmó', 'explicó'."},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Lengua Castellana (7mo Grado)", font=("Helvetica", 20, "bold"), background="#f0f0f0")
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
        filename = "parafrasis_lengua_castellana_7mo_tkinter.txt"
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
