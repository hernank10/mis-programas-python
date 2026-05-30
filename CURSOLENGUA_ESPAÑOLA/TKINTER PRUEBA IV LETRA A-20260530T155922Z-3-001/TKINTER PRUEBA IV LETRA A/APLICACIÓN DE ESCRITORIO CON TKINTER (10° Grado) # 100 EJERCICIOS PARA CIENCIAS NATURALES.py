# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (10° Grado)
# 100 EJERCICIOS PARA CIENCIAS NATURALES
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de décimo grado, cubriendo temas
# de biología molecular, física moderna, termodinámica química y ecología avanzada.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, Text, Scrollbar
import os

class NaturalSciencesApp:
    """
    Clase principal que maneja la interfaz de usuario y la lógica de la aplicación
    para 100 ejercicios de Ciencias Naturales de décimo grado.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Ciencias Naturales (10° Grado)")
        self.root.geometry("800x700")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para décimo grado de ciencias naturales
        # Esta lista es la misma que se proporcionó para la versión de Kivy.
        self.ejercicios = [
            # SECCIÓN 1: BIOLOGÍA - GENÉTICA MOLECULAR Y ECOLOGÍA (25 EJERCICIOS)
            {"titulo": "1. El flujo de información genética", "contenido": "Explica los procesos de replicación, transcripción y traducción del ADN."},
            {"titulo": "2. Código genético y mutaciones", "contenido": "Define el código genético y explica la diferencia entre mutaciones puntuales y cromosómicas. Da un ejemplo de cada una."},
            {"titulo": "3. Herencia no mendeliana", "contenido": "Describe los conceptos de dominancia incompleta y codominancia, dando un ejemplo para cada caso."},
            {"titulo": "4. Ingeniería genética y biotecnología", "contenido": "Explica el proceso de la reacción en cadena de la polimerasa (PCR) y sus aplicaciones en la medicina forense."},
            {"titulo": "5. La tecnología CRISPR-Cas9", "contenido": "Describe el funcionamiento básico de la técnica CRISPR-Cas9 y su potencial en la edición genética."},
            {"titulo": "6. Clones y transgénicos", "contenido": "Diferencia entre un organismo clonado y un organismo transgénico. Menciona las ventajas y desventajas de los alimentos transgénicos."},
            {"titulo": "7. Ecosistemas y biomas", "contenido": "Describe la diferencia entre un ecosistema y un bioma. Menciona las características principales de los biomas de desierto y selva tropical."},
            {"titulo": "8. Cadenas y redes tróficas", "contenido": "Explica la diferencia entre una cadena y una red trófica. ¿Qué consecuencias tiene la desaparición de un depredador tope?"},
            {"titulo": "9. Ciclos biogeoquímicos", "contenido": "Describe los principales pasos del ciclo del carbono y el ciclo del nitrógeno. ¿Cuál es la importancia de las bacterias en el ciclo del nitrógeno?"},
            {"titulo": "10. Sucesión ecológica", "contenido": "Diferencia entre la sucesión ecológica primaria y secundaria. Da un ejemplo de cada tipo."},
            {"titulo": "11. Factores limitantes y capacidad de carga", "contenido": "Define los conceptos de factor limitante y capacidad de carga de un ecosistema."},
            {"titulo": "12. La biodiversidad", "contenido": "Describe los tres niveles de biodiversidad (genética, de especies y de ecosistemas) y por qué es importante conservarla."},
            {"titulo": "13. Especies endémicas e invasoras", "contenido": "Diferencia entre una especie endémica y una especie invasora. ¿Qué problemas causan las especies invasoras?"},
            {"titulo": "14. Conservación y sostenibilidad", "contenido": "Define desarrollo sostenible y menciona tres acciones para promoverlo en una comunidad."},
            {"titulo": "15. El cambio climático y los ecosistemas", "contenido": "Explica el impacto del cambio climático en los ecosistemas polares y de arrecifes de coral."},
            {"titulo": "16. La taxonomía de Linneo", "contenido": "Nombra las principales categorías taxonómicas de la más inclusiva a la menos inclusiva, dando un ejemplo para la especie humana."},
            {"titulo": "17. Los cinco reinos de Whittaker", "contenido": "Describe las características principales de los reinos Monera, Protista y Fungi."},
            {"titulo": "18. El reino Plantae y su clasificación", "contenido": "Diferencia entre plantas vasculares y no vasculares, y entre gimnospermas y angiospermas. Da un ejemplo de cada una."},
            {"titulo": "19. El reino Animalia y los invertebrados", "contenido": "Menciona tres filos de animales invertebrados y sus características distintivas (ej. poríferos, anélidos, artrópodos)."},
            {"titulo": "20. Los vertebrados", "contenido": "Describe las cinco clases de vertebrados y sus características principales."},
            {"titulo": "21. El impacto de la agricultura y la ganadería", "contenido": "Menciona dos impactos ambientales de la agricultura intensiva y la ganadería industrial (ej. erosión del suelo, emisión de metano)."},
            {"titulo": "22. Contaminación del aire", "contenido": "Explica la formación del ozono troposférico y su impacto en la salud humana y las plantas."},
            {"titulo": "23. Los humedales y su importancia", "contenido": "Describe tres funciones ecológicas de los humedales (ej. purificación del agua, control de inundaciones)."},
            {"titulo": "24. Biomas de agua dulce y salada", "contenido": "Diferencia entre los ecosistemas de agua dulce y los ecosistemas marinos. ¿Qué factores los definen?"},
            {"titulo": "25. La bioética", "contenido": "Define bioética y discute un dilema ético relacionado con la biotecnología (ej. clonación humana, organismos modificados genéticamente)."},

            # SECCIÓN 2: FÍSICA - FÍSICA MODERNA Y ÓPTICA (25 EJERCICIOS)
            {"titulo": "26. Espejos planos y esféricos", "contenido": "Diferencia entre una imagen real y una virtual. Explica cómo se forma la imagen en un espejo cóncavo."},
            {"titulo": "27. Refracción y lentes", "contenido": "Explica la ley de Snell de la refracción. Describe la diferencia entre una lente convergente y una divergente y cómo corrigen problemas de visión."},
            {"titulo": "28. La luz y el espectro electromagnético", "contenido": "Nombra al menos cinco tipos de radiación en el espectro electromagnético, ordenándolos por frecuencia o longitud de onda. ¿Cuál es su utilidad?"},
            {"titulo": "29. Dualidad onda-partícula", "contenido": "Explica el concepto de la dualidad onda-partícula de la luz. ¿Qué fenómenos demuestran su naturaleza de onda y cuáles de partícula?"},
            {"titulo": "30. La teoría de la relatividad especial", "contenido": "Enuncia los dos postulados de la relatividad especial de Einstein. ¿Qué consecuencias tienen para el tiempo y el espacio?"},
            {"titulo": "31. La ecuación $E=mc^2$", "contenido": "Explica el significado de la ecuación $E=mc^2$. ¿Cuál es su implicación más importante en la física nuclear?"},
            {"titulo": "32. Física cuántica y el átomo de Bohr", "contenido": "Describe el modelo atómico de Bohr y cómo explica la emisión de luz por parte de los átomos."},
            {"titulo": "33. El efecto fotoeléctrico", "contenido": "Explica el fenómeno del efecto fotoeléctrico. ¿Qué postulado de la física cuántica explica este fenómeno?"},
            {"titulo": "34. Radiactividad y desintegración", "contenido": "Diferencia entre la desintegración alfa, beta y gamma en términos de las partículas emitidas y el cambio en el núcleo."},
            {"titulo": "35. Fisión y fusión nuclear", "contenido": "Explica la diferencia entre la fisión y la fusión nuclear. ¿Qué proceso ocurre en el Sol y cuál en una central nuclear?"},
            {"titulo": "36. Circuitos de corriente alterna", "contenido": "Describe los componentes de un circuito RLC y cómo se comportan la inductancia y la capacitancia en un circuito de CA."},
            {"titulo": "37. El transformador eléctrico", "contenido": "Explica el principio de funcionamiento de un transformador eléctrico. ¿Cuál es su papel en la distribución de energía?"},
            {"titulo": "38. Principio de incertidumbre de Heisenberg", "contenido": "Enuncia el principio de incertidumbre de Heisenberg. ¿Qué implicaciones tiene para la medición de partículas subatómicas?"},
            {"titulo": "39. El modelo estándar de partículas", "contenido": "Nombra las tres familias de partículas elementales (ej. leptones, quarks) y las cuatro fuerzas fundamentales de la naturaleza."},
            {"titulo": "40. Semiconductores y diodos", "contenido": "Explica el funcionamiento de un diodo. ¿Qué lo hace un semiconductor?"},
            {"titulo": "41. Las fuerzas fundamentales", "contenido": "Describe brevemente las cuatro fuerzas fundamentales de la naturaleza: la fuerza gravitatoria, la electromagnética, la nuclear débil y la nuclear fuerte."},
            {"titulo": "42. Lentes convergentes y divergentes", "contenido": "Calcula la potencia de una lente con una distancia focal de 20 cm. ¿Qué tipo de lente es?"},
            {"titulo": "43. Termodinámica: Entropía", "contenido": "Define la entropía y explica su relación con la segunda ley de la termodinámica. ¿Qué significa un aumento de entropía en un sistema?"},
            {"titulo": "44. Transmisión de calor", "contenido": "Diferencia entre la conducción, la convección y la radiación como mecanismos de transferencia de calor. Da un ejemplo de cada uno."},
            {"titulo": "45. La tecnología del láser", "contenido": "Explica los principios físicos que permiten la emisión de luz coherente y monocromática en un láser. ¿Qué significa LASER?"},
            {"titulo": "46. La teoría del color", "contenido": "Diferencia entre los colores primarios aditivos y los colores primarios sustractivos. ¿En qué contexto se usa cada conjunto?"},
            {"titulo": "47. Acústica y ondas de sonido", "contenido": "Explica las características del sonido: intensidad, tono y timbre. ¿Qué magnitud física se asocia a cada una?"},
            {"titulo": "48. Los fluidos y el principio de Bernoulli", "contenido": "Enuncia el principio de Bernoulli y explica cómo se aplica en la sustentación de las alas de un avión."},
            {"titulo": "49. Óptica de fibras", "contenido": "Explica el principio de la reflexión total interna y su aplicación en las fibras ópticas."},
            {"titulo": "50. El CERN y el bosón de Higgs", "contenido": "Explica brevemente la función del Gran Colisionador de Hadrones (CERN) y la importancia del descubrimiento del bosón de Higgs."},

            # SECCIÓN 3: QUÍMICA - TERMODINÁMICA Y CINETICA (25 EJERCICIOS)
            {"titulo": "51. Velocidad de reacción", "contenido": "Define la velocidad de reacción y explica dos factores que pueden acelerarla (ej. temperatura, concentración)."},
            {"titulo": "52. Teoría de colisiones", "contenido": "Explica los tres requisitos de la teoría de colisiones para que una reacción química sea exitosa."},
            {"titulo": "53. Energía de activación", "contenido": "Describe el papel de la energía de activación en una reacción química y cómo un catalizador la afecta."},
            {"titulo": "54. Termodinámica química: Entalpía", "contenido": "Diferencia entre reacciones exotérmicas y endotérmicas en términos de entalpía. ¿Cuál es el signo del $\Delta H$ en cada caso?"},
            {"titulo": "55. Termodinámica química: Entropía y Gibbs", "contenido": "Define la entropía química ($\Delta S$) y la energía libre de Gibbs ($\Delta G$). ¿Qué condición de $\Delta G$ indica una reacción espontánea?"},
            {"titulo": "56. Equilibrio químico", "contenido": "Explica el concepto de equilibrio químico y cómo se expresa matemáticamente a través de la constante de equilibrio ($K_{eq}$). "},
            {"titulo": "57. Principio de Le Châtelier", "contenido": "Enuncia el principio de Le Châtelier. ¿Qué sucede con el equilibrio de una reacción si se aumenta la presión del sistema?"},
            {"titulo": "58. Ácidos y bases fuertes y débiles", "contenido": "Diferencia entre un ácido fuerte y un ácido débil. ¿Qué relación tienen con sus constantes de acidez ($K_a$)?"},
            {"titulo": "59. Nomenclatura de compuestos orgánicos", "contenido": "Nombra los siguientes compuestos orgánicos: $CH_3-CH_2-OH$ y $CH_3-COOH$. ¿A qué grupo funcional pertenece cada uno?"},
            {"titulo": "60. Hidrocarburos saturados e insaturados", "contenido": "Diferencia entre alcanos, alquenos y alquinos. Da un ejemplo de la fórmula estructural de cada uno."},
            {"titulo": "61. Grupos funcionales", "contenido": "Nombra cinco grupos funcionales comunes en química orgánica y da un ejemplo de una molécula para cada uno (ej. alcohol, éter, cetona)."},
            {"titulo": "62. Estereoisomería", "contenido": "Define el concepto de estereoisomería. ¿Cuál es la diferencia entre isómeros geométricos (cis-trans) e isómeros ópticos?"},
            {"titulo": "63. Reacciones de síntesis de polímeros", "contenido": "Describe los procesos de polimerización por adición y polimerización por condensación. Da un ejemplo de un polímero de condensación."},
            {"titulo": "64. Propiedades de los gases reales", "contenido": "Explica por qué la ecuación de los gases ideales no siempre funciona. ¿Qué variables se corrigen en la ecuación de Van der Waals?"},
            {"titulo": "65. Electrólisis", "contenido": "Describe el proceso de la electrólisis y su aplicación en la industria (ej. galvanoplastia, obtención de metales)."},
            {"titulo": "66. Pilas electroquímicas", "contenido": "Explica el funcionamiento de una celda galvánica. ¿Qué es el potencial de reducción estándar y por qué es importante?"},
            {"titulo": "67. La combustión y el poder calorífico", "contenido": "Define poder calorífico. ¿Cuál es la diferencia entre una combustión completa y una incompleta?"},
            {"titulo": "68. Química atmosférica", "contenido": "Describe la formación del ozono en la estratosfera y el problema del agotamiento de la capa de ozono. ¿Qué compuestos lo causan?"},
            {"titulo": "69. Bioquímica: carbohidratos y lípidos", "contenido": "Diferencia entre monosacáridos, disacáridos y polisacáridos. ¿Cuál es la función principal de los lípidos?"},
            {"titulo": "70. Bioquímica: proteínas y ácidos nucleicos", "contenido": "Describe la estructura de una proteína (aminoácidos, enlaces peptídicos). ¿Cuál es la función principal de los ácidos nucleicos?"},
            {"titulo": "71. Química de los polímeros", "contenido": "Diferencia entre termoplásticos y termoestables. Da un ejemplo de cada uno."},
            {"titulo": "72. Solubilidad y producto de solubilidad", "contenido": "Define el producto de solubilidad ($K_{sp}$). ¿Cómo se usa para predecir si un precipitado se formará?"},
            {"titulo": "73. Propiedades coligativas avanzadas", "contenido": "Explica el concepto de presión osmótica. ¿Cómo se aplica en la biología y la medicina?"},
            {"titulo": "74. Catalizadores biológicos: enzimas", "contenido": "Describe el funcionamiento de una enzima y explica el modelo 'llave-cerradura'."},
            {"titulo": "75. Métodos de purificación en química", "contenido": "Explica los procesos de cromatografía y destilación fraccionada y su aplicación."},

            # SECCIÓN 4: CIENCIAS DE LA TIERRA Y ASTRONOMÍA (25 EJERCICIOS)
            {"titulo": "76. La formación del sistema solar", "contenido": "Describe la teoría de la nebulosa solar. ¿Qué fenómenos explican la formación de los planetas terrestres y gaseosos?"},
            {"titulo": "77. Geología y estructura de la Tierra", "contenido": "Describe las principales características de la corteza, el manto y el núcleo. ¿Cómo se conoce esta información?"},
            {"titulo": "78. El vulcanismo", "contenido": "Diferencia entre los volcanes de escudo y los estratovolcanes. ¿Qué tipo de erupciones generan?"},
            {"titulo": "79. Sismos y tectónica", "contenido": "Explica la diferencia entre un sismo y un terremoto. ¿Qué información nos dan las ondas P y S?"},
            {"titulo": "80. La atmósfera: estratos y función", "contenido": "Nombra las capas de la atmósfera y describe la importancia de la estratosfera para la vida en la Tierra."},
            {"titulo": "81. La circulación atmosférica", "contenido": "Describe las células de Hadley, Ferrel y Polar y cómo influyen en el clima global."},
            {"titulo": "82. Océanos: corrientes y termohalina", "contenido": "Explica el funcionamiento de la circulación termohalina y su papel en el clima global. ¿Qué es el Gran Océano Conveyor?"},
            {"titulo": "83. Cambio climático: causas y consecuencias", "contenido": "Explica la diferencia entre el efecto invernadero natural y el potenciado. ¿Qué consecuencias tiene el derretimiento de los polos?"},
            {"titulo": "84. Energías renovables y no renovables", "contenido": "Diferencia entre las energías renovables y no renovables. Menciona dos ejemplos de energías renovables y sus ventajas."},
            {"titulo": "85. La geología de la Luna", "contenido": "Describe las principales características geológicas de la Luna (ej. cráteres, mares, tierras altas) y cómo se formaron."},
            {"titulo": "86. El ciclo de vida de una estrella masiva", "contenido": "Describe las etapas de una estrella masiva desde su nacimiento hasta convertirse en una supernova y, finalmente, un agujero negro o una estrella de neutrones."},
            {"titulo": "87. Las galaxias y la Vía Láctea", "contenido": "Describe la estructura de la Vía Láctea (disco, bulbo, halo) y la ubicación de nuestro sistema solar en ella."},
            {"titulo": "88. Teorías cosmológicas", "contenido": "Explica la teoría del Big Bang. ¿Qué evidencias la respaldan?"},
            {"titulo": "89. Exoplanetas", "contenido": "Define exoplaneta y describe dos métodos para su detección (ej. método de tránsito, velocidad radial)."},
            {"titulo": "90. Astrobiología", "contenido": "Define astrobiología. ¿Qué factores son necesarios para la habitabilidad planetaria?"},
            {"titulo": "91. Contaminación del suelo", "contenido": "Menciona tres fuentes de contaminación del suelo y sus efectos en la agricultura y la salud."},
            {"titulo": "92. Gestión de residuos", "contenido": "Explica la importancia de la regla de las 3R (Reducir, Reutilizar, Reciclar) y da un ejemplo de cada una."},
            {"titulo": "93. Ecosistemas de agua salada", "contenido": "Diferencia entre la zona fótica y afótica en el océano. ¿Qué tipo de organismos viven en cada zona?"},
            {"titulo": "94. La ciencia y la sociedad", "contenido": "Describe cómo la ciencia y la tecnología influyen en la toma de decisiones políticas sobre temas ambientales."},
            {"titulo": "95. El efecto Coriolis", "contenido": "Explica el efecto Coriolis y su impacto en los patrones de vientos y corrientes oceánicas a escala global."},
            {"titulo": "96. Las capas de la hidrosfera", "contenido": "Describe las principales capas de la hidrosfera (criosfera, océanos, aguas dulces)."},
            {"titulo": "97. La glaciología", "contenido": "Explica cómo los glaciares actúan como archivos del clima pasado y por qué su derretimiento es una preocupación actual."},
            {"titulo": "98. Riesgos naturales", "contenido": "Diferencia entre riesgos geológicos (ej. sismos, volcanes) y meteorológicos (ej. huracanes, tornados)."},
            {"titulo": "99. La exploración espacial", "contenido": "Menciona los desafíos tecnológicos y biológicos de los viajes espaciales a largo plazo."},
            {"titulo": "100. El principio de Copérnico", "contenido": "Describe el principio de Copérnico y su implicación en nuestra comprensión del universo. ¿Por qué se considera un cambio de paradigma?"},
        ]

        self.answers = [None] * len(self.ejercicios)
        self.current_exercise_index = 0
        self.is_editing = False

        # Configuración de estilos para una apariencia moderna
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", foreground="#333333")
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.map("TButton", background=[('active', '#e0e0e0')])

        # --- Creación de los widgets principales ---

        # Frame principal para contener todos los elementos
        main_frame = ttk.Frame(root, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título principal
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales (10° Grado)", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=(0, 15))

        # Contador de ejercicios
        self.counter_label = ttk.Label(main_frame, text="", font=("Helvetica", 14))
        self.counter_label.pack(pady=(0, 10))

        # Marco para el contenido del ejercicio
        exercise_frame = ttk.Frame(main_frame, padding="15", relief="solid", borderwidth=1, style="TFrame")
        exercise_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Título del ejercicio
        self.exercise_title_label = ttk.Label(exercise_frame, text="", font=("Helvetica", 16, "bold"), wraplength=700, anchor="w", justify="left")
        self.exercise_title_label.pack(fill=tk.X, pady=(0, 10))

        # Contenido del ejercicio (usando un Text widget para scroll)
        self.exercise_text_widget = Text(exercise_frame, wrap=tk.WORD, height=8, font=("Helvetica", 12), padx=5, pady=5, bd=0, relief=tk.FLAT)
        self.exercise_text_widget.pack(fill=tk.BOTH, expand=True)

        # Barra de desplazamiento para el contenido
        scrollbar = Scrollbar(exercise_frame, command=self.exercise_text_widget.yview)
        self.exercise_text_widget['yscrollcommand'] = scrollbar.set
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.exercise_text_widget.config(state=tk.DISABLED, bg="#f9f9f9") # Bloquear edición del texto del ejercicio

        # Etiqueta para el área de respuesta
        answer_label = ttk.Label(main_frame, text="Escribe tu respuesta aquí:", font=("Helvetica", 14))
        answer_label.pack(pady=(15, 5), anchor="w")

        # Área de texto para la respuesta
        self.answer_text_widget = Text(main_frame, wrap=tk.WORD, height=10, font=("Helvetica", 12), padx=5, pady=5, bd=1, relief=tk.SOLID)
        self.answer_text_widget.pack(fill=tk.BOTH, expand=True)

        # Frame para los botones
        button_frame = ttk.Frame(main_frame, padding="10")
        button_frame.pack(fill=tk.X, pady=(15, 0))

        # Botón para revisar y editar
        self.review_button = ttk.Button(button_frame, text="Revisar y Editar Respuestas", command=self.open_edit_window)
        self.review_button.pack(side=tk.LEFT, padx=(0, 5), expand=True, fill=tk.X)

        # Botón principal de acción (Siguiente/Guardar)
        self.action_button = ttk.Button(button_frame, text="Siguiente Ejercicio", command=self.handle_action)
        self.action_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Botón para guardar todas las respuestas
        self.save_button = ttk.Button(button_frame, text="Guardar todas las respuestas", command=self.save_answers_to_file, state=tk.DISABLED)
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
            
            # Cargar la respuesta guardada si existe
            self.answer_text_widget.config(state=tk.NORMAL)
            self.answer_text_widget.delete("1.0", tk.END)
            if self.answers[self.current_exercise_index]:
                self.answer_text_widget.insert("1.0", self.answers[self.current_exercise_index])
            
            self.action_button.config(state=tk.NORMAL)
            self.review_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL if any(self.answers) else tk.DISABLED)

        else:
            # Fin de los ejercicios
            self.counter_label.config(text="🎉 ¡Has completado todos los ejercicios! �")
            self.exercise_title_label.config(text="Puedes guardar tus respuestas ahora.")
            self.exercise_text_widget.config(state=tk.NORMAL)
            self.exercise_text_widget.delete("1.0", tk.END)
            self.exercise_text_widget.config(state=tk.DISABLED)
            self.answer_text_widget.delete("1.0", tk.END)
            self.answer_text_widget.config(state=tk.DISABLED)
            
            self.action_button.config(state=tk.DISABLED)
            self.review_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.NORMAL if any(self.answers) else tk.DISABLED)

    def handle_action(self):
        """
        Maneja la lógica del botón principal (siguiente o guardar edición).
        """
        if self.is_editing:
            self.save_edited_answer()
        else:
            self.next_exercise()

    def next_exercise(self):
        """
        Guarda la respuesta actual y avanza al siguiente ejercicio.
        """
        answer_text = self.answer_text_widget.get("1.0", tk.END).strip()
        self.answers[self.current_exercise_index] = answer_text if answer_text else "OMITIDO"
        
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

        listbox = tk.Listbox(frame, font=("Helvetica", 12), selectmode=tk.SINGLE, bd=1, relief=tk.SOLID, selectbackground="#c1d5e6")
        listbox.pack(fill=tk.BOTH, expand=True)

        # Llenar el listbox con el estado de cada ejercicio
        for i, answer in enumerate(self.answers):
            status = "✅" if answer and answer != "OMITIDO" else "❓"
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

        self.answer_text_widget.config(state=tk.NORMAL)
        self.answer_text_widget.delete("1.0", tk.END)
        if self.answers[index]:
            self.answer_text_widget.insert("1.0", self.answers[index])
        
        self.action_button.config(text="Guardar Edición")
        self.review_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)
    
    def save_edited_answer(self):
        """
        Guarda la respuesta editada y vuelve al modo normal.
        """
        answer_text = self.answer_text_widget.get("1.0", tk.END).strip()
        self.answers[self.current_exercise_index] = answer_text if answer_text else "OMITIDO"
        
        self.is_editing = False
        self.load_exercise()

    def save_answers_to_file(self):
        """
        Guarda todas las respuestas en un archivo de texto.
        """
        filename = "respuestas_ciencias_naturales_decimo_grado_tkinter.txt"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for i, item in enumerate(self.answers):
                    if item and item != "OMITIDO":
                        original_content = self.ejercicios[i]['contenido']
                        title = self.ejercicios[i]['titulo']
                        file.write(f"--- Ejercicio {i + 1} - {title} ---\n")
                        file.write(f"Texto original: {original_content}\n")
                        file.write(f"Tu respuesta: {item}\n\n")
            messagebox.showinfo("Guardado Completo", f"¡Guardado Exitoso! ✅\nSe ha creado el archivo '{filename}'.")
        except IOError as e:
            messagebox.showerror("Error de Archivo", f"Error: No se pudo guardar el archivo.\nDetalles: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NaturalSciencesApp(root)
    root.mainloop()

