# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (11vo Grado - Lengua Castellana)
# 100 EJERCICIOS PARA LA LITERATURA CANÓNICA Y LA PRODUCCIÓN ACADÉMICA
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de undécimo grado, profundizando
# en temas como el Siglo de Oro, el Romanticismo, y la redacción de textos de alta
# complejidad como ensayos filosóficos y críticas literarias.
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
        self.root.title("Ejercicios de Lengua Castellana (11vo Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para undécimo grado
        self.ejercicios = [
            # SECCIÓN 1: GRAMÁTICA Y SINTAXIS DEL DISCURSO (25 EJERCICIOS)
            {"titulo": "1. Sintaxis del discurso: la cohesión referencial", "contenido": "Análisis de los mecanismos que permiten que un texto mantenga la unidad, como la anáfora y la catáfora. Ej: 'Juan y María llegaron. Ellos estaban cansados.'"},
            {"titulo": "2. Sintaxis del discurso: la cohesión léxica", "contenido": "Identificación de los mecanismos que evitan la repetición de palabras, como la sinonimia, la hiponimia y la elipsis."},
            {"titulo": "3. Oraciones subordinadas de infinitivo, gerundio y participio", "contenido": "Análisis de la función sintáctica de las proposiciones no personales. Ej: 'Al llegar, se desmayó'."},
            {"titulo": "4. La perífrasis de infinitivo con valor de futuro", "contenido": "Análisis de las construcciones como 'ir a + infinitivo' y su uso para expresar un futuro cercano. Ej: 'Va a llover'."},
            {"titulo": "5. El uso de la voz pasiva perifrástica en el lenguaje académico", "contenido": "Análisis de la construcción 'ser + participio' y su uso para dar un tono formal y objetivo. Ej: 'La investigación fue realizada por...'"},
            {"titulo": "6. Los conectores lógicos de causa y consecuencia", "contenido": "Análisis del uso de conectores como 'por consiguiente', 'por lo tanto', 'debido a' para estructurar una argumentación."},
            {"titulo": "7. Los conectores lógicos de oposición y concesión", "contenido": "Análisis del uso de conectores como 'no obstante', 'sin embargo', 'a pesar de' para introducir ideas opuestas."},
            {"titulo": "8. Los marcadores de reformulación y ejemplificación", "contenido": "Análisis del uso de marcadores como 'es decir', 'en otras palabras' y 'por ejemplo' para aclarar o ilustrar una idea."},
            {"titulo": "9. Análisis de la oración compleja: la coordinación adversativa", "contenido": "Análisis de las oraciones unidas por nexos como 'pero', 'mas' y 'sino' que expresan una oposición."},
            {"titulo": "10. La subordinación adverbial de condición y su uso en la hipótesis", "contenido": "Análisis de la forma correcta de expresar una condición en un texto formal. Ej: 'En caso de que...'"},
            {"titulo": "11. Los vicios del lenguaje: el dequeísmo y el queísmo", "contenido": "Identificación y corrección de los errores de omisión o adición de la preposición 'de' en la subordinación. Ej: 'Creo de que...'"},
            {"titulo": "12. La ambigüedad léxica y sintáctica en la interpretación de un texto", "contenido": "Identificación de los casos en los que una palabra o una construcción puede tener más de un significado. Ej: 'Se vende un caballo de carreras para un joven'."},
            {"titulo": "13. La estructura sintáctica del párrafo", "contenido": "Análisis de cómo se construyen los párrafos con una idea principal y otras secundarias que la desarrollan o ejemplifican."},
            {"titulo": "14. El uso de la subordinación en la redacción formal", "contenido": "Análisis de cómo el uso de la subordinación ayuda a dar complejidad y precisión a un texto."},
            {"titulo": "15. La corrección sintáctica en el discurso oral y escrito", "contenido": "Identificación de los errores comunes en el habla que deben evitarse en la escritura formal, como la anacoluto."},
            {"titulo": "16. La función del pronombre 'se' en la impersonalidad", "contenido": "Análisis del uso de 'se' con verbos en tercera persona para referirse a un sujeto indefinido. Ej: 'Se vive bien aquí'."},
            {"titulo": "17. El orden de los elementos en la oración: el hipérbaton", "contenido": "Análisis de la alteración del orden natural de las palabras con un fin estilístico. Ej: 'Del salón en el ángulo oscuro...'"},
            {"titulo": "18. El uso de la conjunción 'aunque' para expresar concesión y oposición", "contenido": "Análisis de los diferentes significados de 'aunque' según el contexto y el modo verbal que le sigue. Ej: 'Aunque me lo pida (indicativo), no iré (subjuntivo)'."},
            {"titulo": "19. Los verbos de afección psíquica y su concordancia", "contenido": "Análisis de los verbos como 'gustar' o 'encantar' y la concordancia con el sujeto gramatical. Ej: 'Me gustan los libros'."},
            {"titulo": "20. La correlación de tiempos verbales en la subordinación", "contenido": "Análisis de las reglas de conjugación que rigen las oraciones subordinadas. Ej: 'Pensé que vendría'."},
            {"titulo": "21. La función de los dos puntos en la introducción de una enumeración o una cita", "contenido": "Análisis de la función estilística de los dos puntos para introducir una explicación. Ej: 'Tengo un sueño: la paz mundial'."},
            {"titulo": "22. La puntuación en la oración compleja", "contenido": "Análisis del uso de la coma, el punto y coma y los dos puntos en las oraciones con varias proposiciones."},
            {"titulo": "23. Los conectores de orden y temporalidad", "contenido": "Uso de marcadores como 'en primer lugar', 'a continuación', 'finalmente' para organizar un discurso."},
            {"titulo": "24. El análisis del sintagma verbal en la oración", "contenido": "Reconocimiento del núcleo, los complementos directos, indirectos y circunstanciales en un sintagma verbal."},
            {"titulo": "25. La elipsis como recurso de cohesión", "contenido": "Análisis de la omisión de elementos que se sobreentienden para dar fluidez y evitar la repetición."},

            # SECCIÓN 2: LITERATURA CANÓNICA ESPAÑOLA (25 EJERCICIOS)
            {"titulo": "26. La novela picaresca: 'Lazarillo de Tormes'", "contenido": "Análisis de la figura del pícaro, la crítica social y la estructura autobiográfica en el 'Lazarillo de Tormes'."},
            {"titulo": "27. El Siglo de Oro: la poesía de Garcilaso de la Vega", "contenido": "Análisis de la lírica de Garcilaso, su influencia renacentista y sus temas amorosos y pastoriles."},
            {"titulo": "28. El Barroco: Góngora y el culteranismo", "contenido": "Análisis de la complejidad sintáctica, el uso de metáforas difíciles y la exuberancia verbal en la poesía de Góngora."},
            {"titulo": "29. El Barroco: Quevedo y el conceptismo", "contenido": "Análisis de la poesía de Quevedo, su ingenio, los juegos de palabras y la profundidad de sus ideas."},
            {"titulo": "30. La novela del Siglo de Oro: 'El Quijote' y la sátira de los libros de caballerías", "contenido": "Análisis de la obra de Cervantes, su crítica social y la dicotomía entre realidad y fantasía."},
            {"titulo": "31. El teatro del Siglo de Oro: Lope de Vega y el 'Arte Nuevo de hacer comedias'", "contenido": "Análisis del teatro de Lope de Vega, su ruptura con las reglas clásicas y la creación de un teatro popular."},
            {"titulo": "32. El Romanticismo en España: Espronceda y la rebeldía", "contenido": "Análisis de la poesía de José de Espronceda, sus temas de libertad, el amor ideal y la desilusión."},
            {"titulo": "33. El Realismo y Naturalismo: Clarín y 'La Regenta'", "contenido": "Análisis de la novela realista de Clarín, su crítica a la burguesía y el retrato psicológico de la protagonista."},
            {"titulo": "34. El Realismo: Galdós y la crítica social en 'Fortunata y Jacinta'", "contenido": "Análisis de la obra de Galdós, el retrato de la sociedad madrileña y la crítica a la hipocresía social."},
            {"titulo": "35. La Generación del 98: la angustia existencial de Miguel de Unamuno", "contenido": "Análisis de la obra de Unamuno, su preocupación por la fe, la inmortalidad y la identidad española."},
            {"titulo": "36. La Generación del 98: la visión crítica de Pío Baroja", "contenido": "Análisis de la novela de Baroja, su pesimismo, la búsqueda de la autenticidad y el personaje 'sencillo'."},
            {"titulo": "37. La Generación del 27: la poesía de Federico García Lorca", "contenido": "Análisis de la obra de Lorca, sus temas del amor, la muerte, la injusticia y su fusión de lo popular y lo vanguardista."},
            {"titulo": "38. La Generación del 27: la poesía pura de Jorge Guillén", "contenido": "Análisis de la poesía de Guillén, su búsqueda de la perfección formal y la celebración de la realidad."},
            {"titulo": "39. La novela de posguerra: Camilo José Cela y el tremendismo", "contenido": "Análisis del estilo narrativo que retrata la realidad de forma cruda y violenta, en la obra de Cela."},
            {"titulo": "40. El Realismo Mágico: Gabriel García Márquez y 'Cien años de soledad'", "contenido": "Análisis de la obra cumbre del Realismo Mágico y su mezcla de fantasía y realidad."},
            {"titulo": "41. La narrativa del 'Boom' latinoamericano: Julio Cortázar", "contenido": "Análisis de la obra de Cortázar, su experimentación narrativa, los juegos con la estructura y el lector."},
            {"titulo": "42. La poesía de Pablo Neruda: amor y denuncia social", "contenido": "Análisis de la obra de Neruda, su poesía amorosa ('Veinte poemas') y su compromiso social ('Canto General')."},
            {"titulo": "43. El teatro de Antonio Buero Vallejo y el problema existencial", "contenido": "Análisis del teatro de Buero Vallejo, su crítica a la sociedad y su reflexión sobre la condición humana."},
            {"titulo": "44. La novela de la memoria: autores y temas", "contenido": "Análisis de la novela que busca recuperar la memoria histórica de la Guerra Civil y la dictadura española."},
            {"titulo": "45. El ensayo filosófico: Unamuno y el 'sentimiento trágico de la vida'", "contenido": "Análisis del ensayo de Unamuno y su reflexión sobre la fe, la razón y la existencia humana."},
            {"titulo": "46. La lírica del Renacimiento y el tópico 'Carpe Diem'", "contenido": "Análisis de la poesía de Garcilaso y su invitación a disfrutar del momento presente."},
            {"titulo": "47. La literatura medieval: el 'Poema del Mío Cid'", "contenido": "Análisis del primer cantar de gesta de la literatura española, sus valores y su héroe."},
            {"titulo": "48. La novela picaresca: 'El Buscón' de Quevedo", "contenido": "Análisis de la novela picaresca de Quevedo, su pesimismo y su visión descarnada de la sociedad."},
            {"titulo": "49. La poesía barroca: Lope de Vega y los sonetos", "contenido": "Análisis de la poesía de Lope de Vega, su vitalidad y su ruptura con los tópicos del Renacimiento."},
            {"titulo": "50. El teatro de Calderón de la Barca y la reflexión filosófica", "contenido": "Análisis del teatro de Calderón, sus temas de honor, destino y libre albedrío en obras como 'La vida es sueño'."},

            # SECCIÓN 3: RETÓRICA Y ANÁLISIS CRÍTICO AVANZADO (25 EJERCICIOS)
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

            # SECCIÓN 4: PRODUCCIÓN TEXTUAL AVANZADA (25 EJERCICIOS)
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Lengua Castellana (11vo Grado)", font=("Helvetica", 20, "bold"), background="#f0f0f0")
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
        filename = "parafrasis_lengua_castellana_11vo_tkinter.txt"
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
