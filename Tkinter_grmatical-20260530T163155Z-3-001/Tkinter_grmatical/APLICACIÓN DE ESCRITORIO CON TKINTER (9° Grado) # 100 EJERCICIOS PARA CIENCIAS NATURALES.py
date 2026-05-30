# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (9° Grado)
# 100 EJERCICIOS PARA CIENCIAS NATURALES
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de noveno grado, cubriendo temas
# de biología celular, química avanzada, física newtoniana y geología.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, Text, Scrollbar
import os

class NaturalSciencesApp:
    """
    Clase principal que maneja la interfaz de usuario y la lógica de la aplicación
    para 100 ejercicios de Ciencias Naturales de noveno grado.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Ciencias Naturales (9° Grado)")
        self.root.geometry("800x700")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para noveno grado de ciencias naturales
        # Esta lista es la misma que se proporcionó para la versión de Kivy.
        self.ejercicios = [
            # SECCIÓN 1: BIOLOGÍA - BIOLOGÍA CELULAR Y SISTEMAS (25 EJERCICIOS)
            {"titulo": "1. La célula eucariota y procariota", "contenido": "Diferencia entre la célula eucariota y procariota, mencionando la presencia o ausencia de organelos y el material genético."},
            {"titulo": "2. Organelos celulares y sus funciones", "contenido": "Describe la función de la mitocondria, el retículo endoplasmático y el aparato de Golgi."},
            {"titulo": "3. Fotosíntesis y respiración celular", "contenido": "Explica la diferencia entre los procesos de fotosíntesis y respiración celular, mencionando los reactivos y productos principales."},
            {"titulo": "4. El ciclo celular: mitosis", "contenido": "Describe las fases de la mitosis (profase, metafase, anafase, telofase) y la importancia de este proceso."},
            {"titulo": "5. El ciclo celular: meiosis", "contenido": "Explica la importancia de la meiosis en la reproducción sexual. ¿Cuál es la diferencia en el número de cromosomas entre las células madre y las hijas?"},
            {"titulo": "6. La estructura del ADN y el ARN", "contenido": "Describe la estructura de una molécula de ADN (nucleótidos, bases nitrogenadas) y la diferencia clave con la molécula de ARN."},
            {"titulo": "7. El sistema circulatorio", "contenido": "Describe el recorrido de la sangre en la circulación mayor y menor, explicando la función del corazón y los vasos sanguíneos."},
            {"titulo": "8. El sistema respiratorio", "contenido": "Explica el proceso de intercambio gaseoso en los alvéolos. ¿Qué gases se intercambian y en qué dirección?"},
            {"titulo": "9. El sistema digestivo", "contenido": "Describe las funciones del estómago, el intestino delgado y el intestino grueso en el proceso de la digestión y la absorción de nutrientes."},
            {"titulo": "10. El sistema excretor", "contenido": "Explica la función principal de los riñones y cómo producen la orina para eliminar los desechos metabólicos."},
            {"titulo": "11. Teoría de la evolución de Darwin", "contenido": "Enuncia los principios de la teoría de la selección natural y cómo se relaciona con la adaptación de las especies."},
            {"titulo": "12. La evidencia de la evolución", "contenido": "Menciona tres evidencias que respaldan la teoría de la evolución (ej. registro fósil, anatomía comparada, embriología)."},
            {"titulo": "13. Órganos homólogos y análogos", "contenido": "Diferencia entre órganos homólogos y análogos, dando un ejemplo de cada uno."},
            {"titulo": "14. La evolución humana", "contenido": "Describe las principales etapas del proceso de hominización, mencionando características clave de los homínidos más antiguos y modernos."},
            {"titulo": "15. La biotecnología", "contenido": "Define biotecnología y menciona una aplicación moderna en la medicina o la agricultura."},
            {"titulo": "16. Los virus y las bacterias", "contenido": "Diferencia entre un virus y una bacteria en términos de estructura, reproducción y capacidad de causar enfermedades."},
            {"titulo": "17. El sistema inmune", "contenido": "Explica el concepto de anticuerpos y cómo funcionan para combatir patógenos."},
            {"titulo": "18. Enfermedades infecciosas y no infecciosas", "contenido": "Diferencia entre una enfermedad infecciosa y una no infecciosa. Da un ejemplo de cada una."},
            {"titulo": "19. La herencia ligada al sexo", "contenido": "Explica por qué ciertas enfermedades (ej. hemofilia, daltonismo) son más comunes en los hombres."},
            {"titulo": "20. La ecología de poblaciones", "contenido": "Describe los factores que regulan el tamaño de una población (ej. tasa de natalidad, tasa de mortalidad, migración)."},
            {"titulo": "21. El impacto de la deforestación", "contenido": "Menciona tres consecuencias a nivel global y local de la deforestación masiva."},
            {"titulo": "22. La genética y la herencia de los grupos sanguíneos", "contenido": "Describe cómo se heredan los grupos sanguíneos del sistema ABO y los posibles genotipos para cada tipo de sangre."},
            {"titulo": "23. La reproducción asexual", "contenido": "Explica la reproducción por bipartición y gemación. ¿Qué organismos la realizan?"},
            {"titulo": "24. La polinización", "contenido": "Define polinización y describe la diferencia entre polinización cruzada y autopolinización."},
            {"titulo": "25. El cerebro humano", "contenido": "Nombra las principales partes del cerebro (ej. cerebelo, tronco encefálico) y describe la función del lóbulo frontal."},

            # SECCIÓN 2: FÍSICA - DINÁMICA Y ENERGÍA (25 EJERCICIOS)
            {"titulo": "26. Leyes de Newton en detalle", "contenido": "Explica la segunda ley de Newton ($F=ma$) y da un ejemplo práctico. ¿Qué representa la masa en esta fórmula?"},
            {"titulo": "27. Fuerza de gravedad", "contenido": "Explica la ley de la gravitación universal de Newton. ¿Cómo se calcula la fuerza de atracción entre dos objetos?"},
            {"titulo": "28. Movimiento parabólico", "contenido": "Describe las características de un movimiento parabólico. ¿Qué fuerzas actúan sobre un proyectil en el aire?"},
            {"titulo": "29. Fuerzas y equilibrio", "contenido": "Explica el concepto de fuerzas en equilibrio. ¿Qué condición se debe cumplir para que un objeto esté en equilibrio traslacional?"},
            {"titulo": "30. Trabajo, potencia y energía", "contenido": "Calcula el trabajo realizado por una fuerza de 50 N que mueve un objeto 10 metros en su misma dirección. Escribe la fórmula."},
            {"titulo": "31. Principio de conservación de la energía", "contenido": "Enuncia el principio de conservación de la energía. Da un ejemplo de la transformación de energía en un objeto que cae."},
            {"titulo": "32. Impulso y momento", "contenido": "Define impulso y momento lineal. ¿Cómo se relacionan y en qué situaciones se aplican?"},
            {"titulo": "33. Ondas mecánicas y electromagnéticas", "contenido": "Diferencia entre una onda mecánica y una electromagnética. Da un ejemplo de cada una."},
            {"titulo": "34. Propiedades de las ondas", "contenido": "Define amplitud, frecuencia y longitud de onda. ¿Cómo se relacionan con la velocidad de una onda?"},
            {"titulo": "35. Electrostática: ley de Coulomb", "contenido": "Explica la ley de Coulomb. ¿Cómo se modifica la fuerza eléctrica si la distancia entre dos cargas se duplica?"},
            {"titulo": "36. Circuitos en serie y en paralelo", "contenido": "Describe las características de un circuito en serie y uno en paralelo. ¿Cómo se calcula la resistencia total en cada caso?"},
            {"titulo": "37. Potencia eléctrica y consumo", "contenido": "Calcula la potencia de una bombilla que consume 2 A a 110 V. Escribe la fórmula. ¿Cómo se calcula el costo de la electricidad?"},
            {"titulo": "38. Fenómenos de la luz", "contenido": "Explica el fenómeno de la dispersión de la luz, como en un prisma. ¿Qué es el espectro visible?"},
            {"titulo": "39. El sonido como onda", "contenido": "Describe las ondas sonoras en términos de compresiones y rarefacciones. ¿Qué es el efecto Doppler?"},
            {"titulo": "40. Presión y fluidos", "contenido": "Explica el principio de Pascal y el principio de Arquímedes con un ejemplo para cada uno."},
            {"titulo": "41. Temperatura y calor", "contenido": "Diferencia entre la temperatura y el calor. ¿Cuáles son las tres escalas de temperatura más comunes y cómo se relacionan?"},
            {"titulo": "42. Termodinámica: leyes básicas", "contenido": "Enuncia la primera y segunda ley de la termodinámica de forma conceptual. ¿Qué es la entropía?"},
            {"titulo": "43. La energía nuclear", "contenido": "Diferencia entre la fisión y la fusión nuclear. ¿Qué proceso se usa en las centrales nucleares?"},
            {"titulo": "44. Lentes y espejos", "contenido": "Describe la diferencia entre una lente convergente y una divergente. Da un ejemplo de aplicación para cada una."},
            {"titulo": "45. Campos eléctricos y magnéticos", "contenido": "Explica qué es un campo eléctrico y cómo se representa. ¿Qué sucede si una carga se mueve en un campo magnético?"},
            {"titulo": "46. Inducción electromagnética", "contenido": "Describe el fenómeno de la inducción electromagnética. ¿Cómo se relaciona con la generación de corriente alterna?"},
            {"titulo": "47. Corriente alterna y corriente continua", "contenido": "Diferencia entre la corriente alterna (AC) y la corriente continua (DC). ¿Dónde se usa cada una?"},
            {"titulo": "48. Motores y generadores eléctricos", "contenido": "Explica la función de un motor eléctrico y un generador eléctrico. ¿Qué transformación de energía realizan?"},
            {"titulo": "49. Frecuencia y resonancia", "contenido": "Define el concepto de frecuencia natural y resonancia en sistemas oscilantes. Da un ejemplo."},
            {"titulo": "50. Tecnología láser", "contenido": "Explica el principio básico del funcionamiento de un láser. ¿Qué significa la sigla LASER?"},

            # SECCIÓN 3: QUÍMICA - ENLACES Y REACCIONES (25 EJERCICIOS)
            {"titulo": "51. Enlaces iónicos y covalentes", "contenido": "Diferencia entre un enlace iónico y un enlace covalente, mencionando la transferencia o compartición de electrones."},
            {"titulo": "52. Estructura de Lewis", "contenido": "Dibuja la estructura de Lewis para el metano ($CH_4$) y el agua ($H_2O$), indicando los electrones de valencia."},
            {"titulo": "53. Geometría molecular", "contenido": "Explica la geometría molecular de la molécula de amoníaco ($NH_3$). ¿Cómo influyen los pares de electrones no enlazantes?"},
            {"titulo": "54. Hibridación de orbitales", "contenido": "Describe el concepto de hibridación de orbitales ($sp, sp^2, sp^3$) y da un ejemplo de una molécula con hibridación $sp^3$."},
            {"titulo": "55. Polaridad de las moléculas", "contenido": "Explica la diferencia entre una molécula polar y una no polar. ¿Cómo influyen los momentos dipolares?"},
            {"titulo": "56. Fuerzas intermoleculares", "contenido": "Describe las fuerzas de Van der Waals y los puentes de hidrógeno. ¿Cuál es su importancia?"},
            {"titulo": "57. Gases ideales: ley de los gases", "contenido": "Explica la ley de Boyle-Mariotte. ¿Qué sucede con el volumen de un gas si la presión se duplica a temperatura constante?"},
            {"titulo": "58. Ecuación de los gases ideales", "contenido": "Enuncia la ecuación de los gases ideales ($PV=nRT$) y explica el significado de cada una de sus variables."},
            {"titulo": "59. Reacciones de combustión", "contenido": "Escribe y balancea la reacción de combustión completa del etano ($C_2H_6$)."},
            {"titulo": "60. Ácidos y bases (teoría de Brönsted-Lowry)", "contenido": "Explica la teoría de ácidos y bases de Brönsted-Lowry. Da un ejemplo de un par ácido-base conjugado."},
            {"titulo": "61. El pH y pOH", "contenido": "Define pH y pOH. ¿Cuál es la relación entre ambos y cómo se calcula el pH de una solución ácida?"},
            {"titulo": "62. Soluciones y solubilidad", "contenido": "Diferencia entre soluto y solvente. Explica el concepto de solubilidad y los factores que la afectan."},
            {"titulo": "63. Concentración de las soluciones", "contenido": "Describe las unidades de concentración molaridad y normalidad. Da un ejemplo para cada una."},
            {"titulo": "64. Propiedades coligativas", "contenido": "Menciona dos propiedades coligativas de las soluciones (ej. descenso crioscópico, aumento ebulloscópico) y explica brevemente una."},
            {"titulo": "65. Reacciones químicas reversibles", "contenido": "Explica qué es una reacción reversible. ¿Qué representa el concepto de equilibrio químico?"},
            {"titulo": "66. Catalizadores", "contenido": "Define un catalizador. ¿Qué efecto tiene sobre la velocidad de una reacción química y cómo lo logra?"},
            {"titulo": "67. Electroquímica", "contenido": "Diferencia entre una celda galvánica (pilas) y una celda electrolítica. ¿Qué procesos ocurren en cada una?"},
            {"titulo": "68. Corrosión", "contenido": "Explica el proceso de corrosión de los metales. ¿Cómo se puede prevenir?"},
            {"titulo": "69. Polímeros de adición y condensación", "contenido": "Diferencia entre un polímero de adición y uno de condensación. Da un ejemplo de cada uno."},
            {"titulo": "70. La química del carbono", "contenido": "Describe la estructura del grafito y el diamante. ¿Por qué el carbono es un elemento fundamental en la química orgánica?"},
            {"titulo": "71. Isomería estructural", "contenido": "Define la isomería estructural. Da un ejemplo de dos isómeros de cadena o de posición."},
            {"titulo": "72. Fórmulas empíricas y moleculares", "contenido": "Explica la diferencia entre una fórmula empírica y una fórmula molecular. Da un ejemplo."},
            {"titulo": "73. Leyes de los gases de Charles y Gay-Lussac", "contenido": "Enuncia las leyes de Charles y Gay-Lussac. ¿Cómo se relacionan con la temperatura, el volumen y la presión de un gas?"},
            {"titulo": "74. Termoquímica: entalpía y energía", "contenido": "Define entalpía ($\Delta H$) y diferencia entre una reacción exotérmica y una endotérmica."},
            {"titulo": "75. Métodos de separación de mezclas", "contenido": "Describe el proceso de destilación y decantación para separar mezclas. ¿Qué tipo de mezclas se separan con cada método?"},

            # SECCIÓN 4: CIENCIAS DE LA TIERRA Y ASTRONOMÍA (25 EJERCICIOS)
            {"titulo": "76. La estructura interna de la Tierra", "contenido": "Nombra las capas internas de la Tierra (núcleo, manto, corteza) y describe brevemente las características de cada una."},
            {"titulo": "77. Geología y tectónica de placas", "contenido": "Explica los diferentes tipos de límites de placas tectónicas (convergente, divergente, transformante) y los fenómenos geológicos que causan."},
            {"titulo": "78. La formación de las rocas", "contenido": "Describe el ciclo de las rocas, explicando cómo una roca ígnea puede convertirse en sedimentaria o metamórfica."},
            {"titulo": "79. Erosión y meteorización", "contenido": "Diferencia entre los procesos de erosión y meteorización. ¿Qué agentes externos (ej. agua, viento, hielo) los causan?"},
            {"titulo": "80. La atmósfera y el clima", "contenido": "Explica el fenómeno de la inversión térmica y su impacto en la calidad del aire. ¿Qué gases son responsables?"},
            {"titulo": "81. El cambio climático", "contenido": "Describe el papel de los gases de efecto invernadero en el cambio climático. ¿Cuál es el gas más abundante y el más potente?"},
            {"titulo": "82. Recursos naturales renovables y no renovables", "contenido": "Diferencia entre un recurso natural renovable y no renovable. Da dos ejemplos de cada uno."},
            {"titulo": "83. Los océanos y las corrientes marinas", "contenido": "Explica cómo se forman las corrientes marinas superficiales y profundas. ¿Cuál es su importancia climática?"},
            {"titulo": "84. La contaminación del agua", "contenido": "Menciona tres tipos de contaminantes del agua (ej. orgánicos, inorgánicos, biológicos) y sus fuentes."},
            {"titulo": "85. La formación de las estrellas", "contenido": "Describe el proceso de formación de una estrella a partir de una nebulosa. ¿Qué fuerza es clave en este proceso?"},
            {"titulo": "86. El ciclo de vida de una estrella", "contenido": "Explica las etapas del ciclo de vida de una estrella de gran masa, desde la nebulosa hasta el agujero negro o la estrella de neutrones."},
            {"titulo": "87. Las galaxias y sus tipos", "contenido": "Nombra y describe los tres tipos principales de galaxias (espirales, elípticas, irregulares). ¿A qué tipo pertenece la Vía Láctea?"},
            {"titulo": "88. La teoría del Big Bang", "contenido": "Describe las dos evidencias clave que respaldan la teoría del Big Bang: la expansión del universo y la radiación cósmica de fondo."},
            {"titulo": "89. El sistema solar y la ley de Kepler", "contenido": "Enuncia la primera y segunda ley de Kepler sobre el movimiento de los planetas."},
            {"titulo": "90. La Luna y las mareas", "contenido": "Explica el fenómeno de las mareas vivas y mareas muertas, y cómo se relaciona con las posiciones de la Luna y el Sol."},
            {"titulo": "91. Eclipses solares y lunares", "contenido": "Diferencia entre un eclipse solar y un eclipse lunar, explicando la posición de la Tierra, la Luna y el Sol en cada caso."},
            {"titulo": "92. La exploración espacial", "contenido": "Menciona dos logros importantes de la exploración espacial humana (ej. misión Apolo, Estación Espacial Internacional) y su importancia."},
            {"titulo": "93. Asteroides, cometas y meteoros", "contenido": "Diferencia entre un asteroide, un cometa y un meteoroide. ¿De qué material están compuestos principalmente?"},
            {"titulo": "94. La contaminación lumínica", "contenido": "Explica los efectos negativos de la contaminación lumínica en la observación astronómica y en la ecología."},
            {"titulo": "95. El universo observable", "contenido": "Define el concepto de universo observable. ¿Por qué no podemos ver más allá de este límite?"},
            {"titulo": "96. Las eras geológicas", "contenido": "Nombra las tres eras geológicas (Paleozoica, Mesozoica, Cenozoica) y menciona un evento o forma de vida característica de cada una."},
            {"titulo": "97. Fósiles", "contenido": "Describe el proceso de fosilización. ¿Qué información se puede obtener del estudio de los fósiles?"},
            {"titulo": "98. La escala de tiempo geológico", "contenido": "Explica la diferencia entre un Eón, una Era y un Periodo en la escala de tiempo geológico."},
            {"titulo": "99. Riesgos geológicos", "contenido": "Menciona dos tipos de riesgos geológicos (ej. sismos, volcanes, tsunamis) y cómo se monitorean."},
            {"titulo": "100. El efecto Coriolis", "contenido": "Explica el efecto Coriolis y cómo afecta a los vientos y a las corrientes oceánicas en los diferentes hemisferios."},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales (9° Grado)", font=("Helvetica", 20, "bold"))
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
            self.counter_label.config(text="🎉 ¡Has completado todos los ejercicios! 🎉")
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
        filename = "respuestas_ciencias_naturales_noveno_grado_tkinter.txt"
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
