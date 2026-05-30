# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (8vo Grado - Lengua Castellana)
# 100 EJERCICIOS PARA PROFUNDIZAR EN CONCEPTOS AVANZADOS
# ==============================================================================
# Esta aplicación recrea la funcionalidad del programa anterior de Kivy,
# utilizando la librería estándar de Python, Tkinter. Permite a los estudiantes
# de octavo grado practicar la paráfrasis de conceptos avanzados de Lengua
# Castellana y ofrece la funcionalidad de revisión y edición de respuestas.
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
        self.root.title("Ejercicios de Lengua Castellana (8vo Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para octavo grado
        # Esta lista es idéntica a la versión de Kivy para mantener la consistencia
        self.ejercicios = [
            # SECCIÓN 1: ANÁLISIS DE ORACIÓN COMPUESTA Y SINTAXIS AVANZADA
            {"titulo": "1. Proposiciones Subordinadas Adjetivas de Relativo", "contenido": "Son aquellas que funcionan como un adjetivo y están introducidas por un pronombre o adverbio relativo (que, quien, el cual, donde)."},
            {"titulo": "2. Proposiciones Subordinadas Adverbiales Propias", "contenido": "Funcionan como un adverbio, indicando tiempo, lugar o modo. Por ejemplo, 'cuando', 'donde', 'como'."},
            {"titulo": "3. Proposiciones Subordinadas Adverbiales Impropias", "contenido": "No se pueden sustituir por un adverbio y expresan otras relaciones como causa, consecuencia, concesión, condición, etc."},
            {"titulo": "4. Subordinadas Sustantivas de Sujeto", "contenido": "Toda la proposición subordinada realiza la función de sujeto en la oración principal. Ej: 'Me gusta que me escuches'."},
            {"titulo": "5. Subordinadas Sustantivas de Complemento Directo", "contenido": "La proposición subordinada realiza la función de complemento directo. Ej: 'Dijo que llegaría tarde'."},
            {"titulo": "6. Oraciones Coordinadas Copulativas", "contenido": "Unen proposiciones que suman sus significados (y, e, ni)."},
            {"titulo": "7. Oraciones Coordinadas Adversativas", "contenido": "Unen proposiciones que se contraponen (pero, sino, sin embargo)."},
            {"titulo": "8. Oraciones Coordinadas Disyuntivas", "contenido": "Presentan una opción a elegir entre varias (o, u)."},
            {"titulo": "9. Oraciones Coordinadas Distributivas", "contenido": "Reparten la acción entre las proposiciones (ya...ya, bien...bien)."},
            {"titulo": "10. La Interdependencia de las Proposiciones", "contenido": "En una oración compuesta, la relación de dependencia o independencia que existe entre las proposiciones que la conforman."},
            {"titulo": "11. Complemento Directo vs. Complemento Indirecto", "contenido": "El C.D. recibe la acción del verbo. El C.I. indica a quién o para quién se realiza la acción. Ej: 'Compré flores' (C.D.) vs. 'Le compré flores' (C.I.)."},
            {"titulo": "12. Oraciones con Verbos Pronominales", "contenido": "Verbos que siempre se usan con un pronombre átono (me, te, se). Ej: 'arrepentirse', 'quejarse'."},
            {"titulo": "13. La Pasiva Refleja", "contenido": "Oraciones pasivas que se construyen con el pronombre 'se' y el verbo en voz activa. Ej: 'Se venden casas'."},
            {"titulo": "14. Errores Comunes de Concordancia", "contenido": "Fallos en la concordancia de género, número o persona entre el sujeto y el verbo o entre el sustantivo y el adjetivo."},
            {"titulo": "15. La Perífrasis Verbal de Obligación", "contenido": "Combina un verbo modal con un infinitivo, gerundio o participio para expresar obligación. Ej: 'Tengo que estudiar'."},
            {"titulo": "16. La Proposición Subordinada Concesiva", "contenido": "Expresa una dificultad que no impide la acción de la oración principal. Introducida por 'aunque', 'a pesar de que'."},
            {"titulo": "17. La Proposición Subordinada Condicional", "contenido": "Establece una condición para que se cumpla la acción de la principal. Introducida por 'si', 'siempre que'."},
            {"titulo": "18. Uso de Gerundios y Participios", "contenido": "El gerundio indica una acción en desarrollo. El participio indica una acción terminada. Su uso incorrecto es una incorrección."},
            {"titulo": "19. Complementos Circunstanciales de Causa y Finalidad", "contenido": "Indican el motivo de la acción (C.C. de Causa) o el propósito (C.C. de Finalidad)."},
            {"titulo": "20. Subordinadas de Lugar, Tiempo y Modo", "contenido": "Proposiciones subordinadas que indican las circunstancias de la acción principal. Ej: 'Iré donde me digas'."},
            {"titulo": "21. El Estilo Directo e Indirecto en textos complejos", "contenido": "Uso de comillas y verbos de lengua en el estilo directo. Adaptación de tiempos verbales y pronombres en el indirecto."},
            {"titulo": "22. La oración de relativo con antecedente implícito", "contenido": "La proposición adjetiva no tiene un sustantivo al que se refiera directamente. Ej: 'Quien ríe el último, ríe mejor'."},
            {"titulo": "23. Verbos defectivos e impersonales", "contenido": "Verbos defectivos que no se conjugan en todos los tiempos. Verbos impersonales que carecen de sujeto. Ej: 'haber', 'llover'."},
            {"titulo": "24. Elipsis y Cohesión Textual", "contenido": "Omisión de elementos en el texto que se entienden por el contexto para evitar repeticiones y dar fluidez al texto."},
            {"titulo": "25. Conectores de orden y de contraste", "contenido": "Conectores que organizan el texto (en primer lugar) y los que introducen ideas opuestas (en cambio, por el contrario)."},
            
            # SECCIÓN 2: ORTOGRAFÍA, PUNTUACIÓN Y LÉXICO AVANZADO
            {"titulo": "26. Acentuación de palabras con diptongos y triptongos", "contenido": "Las reglas de acentuación se aplican a la sílaba tónica, teniendo en cuenta la combinación de vocales fuertes y débiles."},
            {"titulo": "27. Uso de los puntos y comas", "contenido": "Indican una pausa mayor que la coma, pero menor que el punto. Se usa para separar oraciones con una relación estrecha."},
            {"titulo": "28. Palabras polisémicas y homófonas", "contenido": "Las polisémicas tienen varios significados. Las homófonas suenan igual pero se escriben diferente."},
            {"titulo": "29. Prefijos y sufijos de origen grecolatino", "contenido": "Prefijos como 'bio-' (vida) y sufijos como '-logía' (ciencia) que ayudan a comprender el significado de las palabras."},
            {"titulo": "30. Uso de mayúsculas en títulos y cargos", "contenido": "Se usa mayúscula en la primera palabra del título. Los cargos se escriben con minúscula, salvo excepciones."},
            {"titulo": "31. Abreviaciones, siglas y acrónimos", "contenido": "Las abreviaciones se cierran con punto. Las siglas se escriben sin puntos. Los acrónimos pueden funcionar como nombres comunes."},
            {"titulo": "32. El Guion y la Raya en la puntuación", "contenido": "El guion se usa para dividir palabras. La raya para introducir diálogos o incisos más largos."},
            {"titulo": "33. Uso de la `b` y la `v` en prefijos y sufijos", "contenido": "Se usa `b` en 'bio-' y 'bien-'. Se usa `v` en 'vice-', 'villa-' y '-vora'."},
            {"titulo": "34. Uso de la `g` y la `j`", "contenido": "El sonido fuerte de 'ge' y 'gi' se escribe con `j` si no lleva 'u' (ge, gi)."},
            {"titulo": "35. Sinónimos y antónimos contextuales", "contenido": "Palabras que son sinónimas o antónimas solo en un contexto específico, no en todos los casos."},
            {"titulo": "36. Palabras de origen extranjero y su adaptación", "contenido": "Palabras de otros idiomas que se han incorporado al español y han adaptado su ortografía y acentuación."},
            {"titulo": "37. El uso correcto de las comillas", "contenido": "Se usan para citas textuales, títulos de obras, ironías y para destacar una palabra."},
            {"titulo": "38. Tilde diacrítica en pronombres interrogativos y exclamativos", "contenido": "Palabras como `qué`, `cuándo`, `dónde`, `quién`, `cómo` se acentúan solo en oraciones interrogativas o exclamativas."},
            {"titulo": "39. El uso del punto y seguido vs. punto y aparte", "contenido": "El punto y seguido separa oraciones de un mismo párrafo. El punto y aparte separa párrafos con ideas diferentes."},
            {"titulo": "40. Campo semántico y campo léxico", "contenido": "Un campo semántico agrupa palabras por su significado. Un campo léxico las agrupa por su relación con un tema."},
            {"titulo": "41. Los verbos de la primera, segunda y tercera conjugación", "contenido": "Verbos que terminan en -ar, -er, e -ir. La conjugación es el conjunto de todas las formas del verbo."},
            {"titulo": "42. Los sufijos y prefijos aumentativos y diminutivos", "contenido": "Sufijos que indican un tamaño grande (-azo) o pequeño (-ito)."},
            {"titulo": "43. El uso de las mayúsculas en sustantivos propios", "contenido": "Se usan para nombres de personas, lugares, festividades, instituciones y siglas."},
            {"titulo": "44. Errores de acentuación frecuentes", "contenido": "Errores al acentuar palabras llanas, esdrújulas o al no acentuar palabras agudas terminadas en -n, -s o vocal."},
            {"titulo": "45. Vocabulario técnico y coloquial", "contenido": "El vocabulario técnico se usa en un ámbito especializado. El coloquial en la comunicación informal."},
            {"titulo": "46. Uso de los paréntesis para aclaraciones", "contenido": "Se usan para incluir información adicional o aclaraciones en un texto, sin que altere su fluidez."},
            {"titulo": "47. Concordancia verbal y nominal", "contenido": "La concordancia verbal se refiere a la relación entre sujeto y verbo. La nominal, entre sustantivo y adjetivo."},
            {"titulo": "48. La tilde en las palabras compuestas", "contenido": "Una palabra compuesta por dos palabras agudas, mantiene la tilde solo en la segunda palabra."},
            {"titulo": "49. El uso de la `cc` y la `c`", "contenido": "La `cc` se utiliza en palabras que contienen el grupo `ct` en su familia, como 'acción' de 'acto'."},
            {"titulo": "50. Dequeísmo y Queísmo en la escritura formal", "contenido": "El uso incorrecto o la omisión de la preposición 'de' antes de 'que' son errores que se deben evitar."},
            
            # SECCIÓN 3: GÉNEROS LITERARIOS Y FIGURAS RETÓRICAS
            {"titulo": "51. La Metáfora y la Comparación (Símil)", "contenido": "La metáfora asocia dos elementos sin nexos. La comparación los une con 'como', 'parece'. Ej: 'Sus ojos eran dos luceros' (metáfora) vs. 'Sus ojos brillaban como luceros' (símil)."},
            {"titulo": "52. La Sinécdoque y la Metonimia", "contenido": "La sinécdoque designa la parte por el todo o viceversa. La metonimia designa una cosa con el nombre de otra con la que tiene una relación. Ej: 'Tener cuatro bocas que alimentar' (sinécdoque) vs. 'Leo a Cernuda' (metonimia)."},
            {"titulo": "53. La Hipérbole y la Lítotes", "contenido": "La hipérbole exagera. La lítotes atenúa, diciendo menos de lo que se quiere expresar. Ej: 'No es fea' (lítotes) para decir que es guapa."},
            {"titulo": "54. La Antítesis y el Oxímoron", "contenido": "La antítesis opone dos ideas. El oxímoron une dos palabras con significados contradictorios. Ej: 'dulce amargura'."},
            {"titulo": "55. La Personificación y el Apóstrofe", "contenido": "La personificación da vida a objetos. El apóstrofe es una interrupción para dirigirse a una persona o cosa personificada."},
            {"titulo": "56. El Narrador en Primera Persona (Protagonista y Testigo)", "contenido": "El narrador protagonista cuenta su propia historia. El narrador testigo narra lo que ve, desde fuera."},
            {"titulo": "57. El Narrador en Tercera Persona (Omnisciente y Observador)", "contenido": "El omnisciente lo sabe todo. El observador solo cuenta lo que ve y oye, como una cámara."},
            {"titulo": "58. El Punto de Vista del Narrador", "contenido": "Es la perspectiva desde la que se cuenta la historia, que puede ser interna (1ª persona) o externa (3ª persona)."},
            {"titulo": "59. El Romance y el Soneto", "contenido": "El romance es un poema narrativo de versos octosílabos. El soneto es un poema de 14 versos endecasílabos."},
            {"titulo": "60. La Oda y la Elegía", "contenido": "La oda exalta a una persona o idea. La elegía es un poema de lamentación por la muerte de alguien."},
            {"titulo": "61. El Ensayo Argumentativo y Expositivo", "contenido": "El argumentativo busca convencer. El expositivo busca informar y explicar."},
            {"titulo": "62. La Crónica y el Reportaje", "contenido": "La crónica mezcla la información periodística con la opinión personal. El reportaje es una investigación más profunda."},
            {"titulo": "63. El Ensayo como género literario", "contenido": "Género en prosa que expone un tema desde una perspectiva personal y argumentativa."},
            {"titulo": "64. La Tragedia y la Comedia en el Teatro Clásico", "contenido": "La tragedia presenta un conflicto con un final fatal. La comedia tiene un final feliz y humorístico."},
            {"titulo": "65. El Mito y la Leyenda", "contenido": "El mito explica el origen del mundo. La leyenda narra hechos extraordinarios con base histórica."},
            {"titulo": "66. La Novela de Ciencia Ficción y Fantástica", "contenido": "La ciencia ficción se basa en la tecnología. La fantástica, en elementos imaginarios y mágicos."},
            {"titulo": "67. La Rima Consonante y Asonante", "contenido": "La rima consonante es la coincidencia de vocales y consonantes. La asonante, solo de vocales."},
            {"titulo": "68. El Ritmo y la Métrica en la Poesía", "contenido": "El ritmo es la cadencia musical. La métrica es la medida de los versos."},
            {"titulo": "69. La Figuras de Repetición (Anáfora, Paralelismo, Aliteración)", "contenido": "La anáfora repite palabras al inicio. El paralelismo, la estructura. La aliteración, los sonidos."},
            {"titulo": "70. La Égloga, la Sátira y el Epigrama", "contenido": "La égloga es un poema pastoril. La sátira, un poema de crítica. El epigrama, un poema breve e ingenioso."},
            {"titulo": "71. El Monólogo y el Diálogo", "contenido": "El monólogo es el discurso de un personaje. El diálogo es la conversación entre varios personajes."},
            {"titulo": "72. La Catarsis en la Tragedia Griega", "contenido": "Es la purificación emocional que experimenta el espectador al ver la obra."},
            {"titulo": "73. El Ensayo como instrumento de crítica", "contenido": "Uso del ensayo para expresar una opinión razonada sobre un tema social, político o cultural."},
            {"titulo": "74. Trama, Tema y Argumento", "contenido": "La trama es la secuencia de hechos. El tema es la idea principal. El argumento es el resumen de la historia."},
            {"titulo": "75. Tipos de Cuentos (Tradicional, Realista, Maravilloso)", "contenido": "El cuento tradicional se basa en la oralidad. El realista refleja la vida. El maravilloso, la magia."},

            # SECCIÓN 4: REDACCIÓN Y COMUNICACIÓN
            {"titulo": "76. La Estructura de un Texto Argumentativo Complejo", "contenido": "Introducción (contexto y tesis), desarrollo (argumentos, contraargumentos) y conclusión (reafirmación de la tesis)."},
            {"titulo": "77. Tipos de Argumentos (Autoridad, Ejemplificación, de Causa-Efecto)", "contenido": "Argumentos que usan expertos, ejemplos o relaciones causales para apoyar una idea."},
            {"titulo": "78. La Contraargumentación y la Refutación", "contenido": "La contraargumentación es la objeción a un argumento. La refutación es la demostración de su falsedad."},
            {"titulo": "79. Las Falacias Lógicas", "contenido": "Son argumentos que parecen válidos, pero no lo son. Ej: Ad hominem (atacar a la persona, no a la idea)."},
            {"titulo": "80. La Tesis y la Hipótesis", "contenido": "La tesis es la postura que se defiende. La hipótesis es la suposición inicial que se busca probar o refutar."},
            {"titulo": "81. El Liderazgo en el Debate", "contenido": "La capacidad de guiar el debate, escuchar activamente, estructurar los argumentos y persuadir a la audiencia."},
            {"titulo": "82. El Texto Expositivo y su función", "contenido": "Tiene como objetivo informar de manera clara y objetiva. Su estructura es introducción, desarrollo y conclusión."},
            {"titulo": "83. La Cohesión y la Coherencia Textual", "contenido": "La cohesión es la conexión gramatical y léxica. La coherencia es la unidad de sentido global del texto."},
            {"titulo": "84. Elementos de la Comunicación (Emisor, Receptor, Canal, Código, Contexto)", "contenido": "Los componentes clave de cualquier proceso comunicativo."},
            {"titulo": "85. La Entrevista (tipos y estructura)", "contenido": "Puede ser informativa o de personalidad. Tiene preguntas de apertura, desarrollo y cierre."},
            {"titulo": "86. La Opinión y la Argumentación", "contenido": "La opinión es una idea personal. La argumentación es el proceso de razonar para defender una opinión."},
            {"titulo": "87. Las Características de la Crónica Periodística", "contenido": "Combina la narración de hechos con la interpretación y la subjetividad del autor."},
            {"titulo": "88. La Estructura de una Exposición Oral", "contenido": "Introducción, desarrollo de las ideas y un cierre o conclusión."},
            {"titulo": "89. La Persuasión y la Manipulación", "contenido": "La persuasión es convencer con argumentos. La manipulación es influir de forma engañosa."},
            {"titulo": "90. La Ironía y el Sarcasmo", "contenido": "La ironía dice lo contrario. El sarcasmo es una ironía mordaz y cruel."},
            {"titulo": "91. El Marco Narrativo y el Subtexto", "contenido": "El marco es el contexto físico y temporal. El subtexto es el significado oculto de un texto."},
            {"titulo": "92. Estructura de la Noticia (titular, entradilla, cuerpo)", "contenido": "Los componentes de una noticia, con la información más importante al principio (pirámide invertida)."},
            {"titulo": "93. Elementos de la Comunicación No Verbal", "contenido": "Gestos, posturas, expresiones faciales, tono de voz que acompañan al lenguaje verbal."},
            {"titulo": "94. Conectores de Conclusión y Síntesis", "contenido": "Palabras que introducen un resumen o la parte final de un texto (en definitiva, para concluir)."},
            {"titulo": "95. Conectores de Causalidad y Consecuencia", "contenido": "Palabras que indican la causa de algo (porque) y su efecto (por lo tanto)."},
            {"titulo": "96. La Planificación de la Escritura", "contenido": "Las etapas de preescritura, borrador, revisión y corrección para producir un texto de calidad."},
            {"titulo": "97. El Resumen y la Síntesis", "contenido": "El resumen acorta un texto manteniendo sus ideas principales. La síntesis reestructura un texto y lo reformula."},
            {"titulo": "98. El Tema y la Idea Principal", "contenido": "El tema es la idea general y abstracta. La idea principal es la frase que resume el contenido más importante."},
            {"titulo": "99. La Voz Activa y la Voz Pasiva en la Redacción", "contenido": "La voz activa es más directa. La voz pasiva se usa para dar más importancia al objeto de la acción."},
            {"titulo": "100. Tipos de Textos (Narrativo, Descriptivo, Expositivo, Argumentativo)", "contenido": "Clasificación de los textos según su finalidad y estructura. Cada uno tiene sus propias características."},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Lengua Castellana (8vo Grado)", font=("Helvetica", 20, "bold"), background="#f0f0f0")
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
        filename = "parafrasis_lengua_castellana_8vo_tkinter.txt"
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
