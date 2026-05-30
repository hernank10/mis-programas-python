# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (CON EDICIÓN)
# 100 EJERCICIOS DE CIENCIAS NATURALES (Nivel Preuniversitario / Grado 12)
# ==============================================================================
# Esta versión del programa permite al usuario no solo avanzar por los ejercicios,
# sino también revisar, editar y guardar las paráfrasis de ejercicios que ya ha
# completado previamente.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ParaphraseApp(tk.Tk):
    """
    Clase principal de la aplicación Tkinter.
    Maneja la interfaz de usuario, la lógica de los ejercicios,
    la navegación y la función de revisión/edición.
    """
    def __init__(self):
        super().__init__()
        self.title("Ejercicios de Ciencias Naturales")
        self.geometry("800x700")
        self.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para el grado 12 / preuniversitario
        self.ejercicios = [
            # SECCIÓN 1: QUÍMICA ORGÁNICA Y BIOQUÍMICA
            {"titulo": "1. Estructura de Lewis y Resonancia", "contenido": "La resonancia describe la deslocalización de electrones en moléculas con enlaces dobles o triples conjugados. Ej: el benceno."},
            {"titulo": "2. Nomenclatura IUPAC", "contenido": "La Unión Internacional de Química Pura y Aplicada (IUPAC) establece las reglas para nombrar compuestos orgánicos, basándose en la cadena principal y sus sustituyentes."},
            {"titulo": "3. Grupos Funcionales", "contenido": "Son átomos o grupos de átomos que determinan las propiedades químicas de una molécula orgánica. Ej: el grupo hidroxilo (-OH) en los alcoholes."},
            {"titulo": "4. Isomería Estructural y Geométrica", "contenido": "Dos compuestos con la misma fórmula molecular pero diferente estructura son isómeros. La isomería geométrica (cis-trans) es común en alquenos."},
            {"titulo": "5. Reacciones de Sustitución Nucleofílica", "contenido": "Un nucleófilo (rico en electrones) sustituye a un grupo saliente en la molécula. Mecanismos comunes: $S_N1$ y $S_N2$."},
            {"titulo": "6. Polímeros", "contenido": "Son macromoléculas formadas por la unión de muchas unidades repetitivas (monómeros). Ej: el polietileno y el PVC."},
            {"titulo": "7. Estructura de los Carbohidratos", "contenido": "Glucosa, fructosa y galactosa son monosacáridos. La celulosa y el almidón son polímeros de la glucosa."},
            {"titulo": "8. Lípidos y sus Funciones", "contenido": "Los lípidos, como los fosfolípidos, son componentes clave de las membranas celulares. Otros lípidos almacenan energía."},
            {"titulo": "9. Niveles Estructurales de las Proteínas", "contenido": "La estructura primaria es la secuencia de aminoácidos. Las estructuras secundaria, terciaria y cuaternaria definen la forma tridimensional de la proteína."},
            {"titulo": "10. Enzimas y Catálisis Biológica", "contenido": "Las enzimas, que son proteínas, actúan como catalizadores biológicos, acelerando la velocidad de las reacciones bioquímicas."},
            {"titulo": "11. Ciclo de Krebs", "contenido": "Es una ruta metabólica clave en la respiración celular que produce energía en forma de ATP y otros transportadores de electrones."},
            {"titulo": "12. Fosforilación Oxidativa", "contenido": "Es el paso final de la respiración celular, donde se genera la mayor parte del ATP a través de una cadena de transporte de electrones."},
            {"titulo": "13. Nomenclatura de Ésteres", "contenido": "Un éster se forma a partir de un ácido carboxílico y un alcohol. Se nombra como el 'alcanoato de alquilo'."},
            {"titulo": "14. Reactividad del Benceno", "contenido": "El anillo de benceno es un sistema aromático muy estable. Sus reacciones típicas son de sustitución electrofílica aromática."},
            {"titulo": "15. Reacciones de Saponificación", "contenido": "Es la hidrólisis de un éster, como un triglicérido, en presencia de una base fuerte para producir jabón."},
            {"titulo": "16. Isomería Óptica o Quiralidad", "contenido": "Moléculas con un carbono quiral (unido a cuatro grupos diferentes) tienen isómeros que son imágenes especulares no superponibles (enantiómeros)."},
            {"titulo": "17. Grupos Carbonilo y Carboxilo", "contenido": "El grupo carbonilo (C=O) se encuentra en aldehídos y cetonas. El grupo carboxilo (-COOH) se encuentra en ácidos carboxílicos."},
            {"titulo": "18. Mecanismo de Reacción $S_N1$", "contenido": "La reacción de sustitución nucleofílica $S_N1$ ocurre en dos pasos, con un carbocatión como intermedio."},
            {"titulo": "19. Mecanismo de Reacción $S_N2$", "contenido": "La reacción de sustitución nucleofílica $S_N2$ ocurre en un solo paso concertado, con inversión de la estereoquímica."},
            {"titulo": "20. Aminoácidos Esenciales", "contenido": "Son aquellos que el cuerpo humano no puede sintetizar por sí mismo y debe obtenerlos a través de la dieta."},
            {"titulo": "21. Metabolismo y Anabolismo", "contenido": "El metabolismo es el conjunto de reacciones químicas del cuerpo. El anabolismo construye moléculas grandes a partir de pequeñas."},
            {"titulo": "22. Catabolismo y Glucólisis", "contenido": "El catabolismo descompone moléculas grandes. La glucólisis es el primer paso en la descomposición de la glucosa."},
            {"titulo": "23. Estructura y Función del ATP", "contenido": "El ATP (adenosín trifosfato) es la principal molécula de energía para la mayoría de las actividades celulares."},
            {"titulo": "24. Espectroscopía de RMN", "contenido": "La resonancia magnética nuclear (RMN) es una técnica analítica que permite determinar la estructura de moléculas orgánicas."},
            {"titulo": "25. Hidrólisis de los Ácidos Nucleicos", "contenido": "Es la ruptura de los enlaces fosfodiéster en el ADN o el ARN, liberando nucleótidos."},

            # SECCIÓN 2: FÍSICA MODERNA Y ASTROFÍSICA
            {"titulo": "26. Principio de Incertidumbre de Heisenberg", "contenido": "Afirma que es imposible conocer simultáneamente y con precisión la posición y el momento de una partícula."},
            {"titulo": "27. Dualidad Onda-Partícula", "contenido": "Propuesta por De Broglie, sostiene que las partículas subatómicas como los electrones exhiben propiedades tanto de onda como de partícula."},
            {"titulo": "28. Efecto Fotoeléctrico", "contenido": "Es la emisión de electrones por un material al incidir sobre él una radiación electromagnética (luz)."},
            {"titulo": "29. Postulados de la Relatividad Especial", "contenido": "La velocidad de la luz en el vacío es la misma para todos los observadores, y las leyes de la física son las mismas para todos los sistemas de referencia inerciales."},
            {"titulo": "30. Equivalencia Masa-Energía", "contenido": "La famosa ecuación $E = mc^2$ de Einstein establece que la masa y la energía son dos caras de la misma moneda."},
            {"titulo": "31. Curvatura del Espacio-Tiempo", "contenido": "Según la Relatividad General de Einstein, la gravedad no es una fuerza, sino una manifestación de la curvatura del espacio-tiempo causada por la masa y la energía."},
            {"titulo": "32. Formación Estelar", "contenido": "Las estrellas nacen a partir del colapso gravitacional de nubes moleculares gigantes, ricas en gas y polvo."},
            {"titulo": "33. Ciclo de Vida de una Estrella", "contenido": "El destino de una estrella (enana blanca, estrella de neutrones, agujero negro) depende de su masa inicial."},
            {"titulo": "34. Galaxias", "contenido": "Son sistemas gigantes de estrellas, gas, polvo y materia oscura. La Vía Láctea es nuestra galaxia, de tipo espiral."},
            {"titulo": "35. Teoría del Big Bang", "contenido": "Es el modelo cosmológico que explica el origen del universo como un punto singular que se expandió hace unos 13.800 millones de años."},
            {"titulo": "36. Energía Oscura y Materia Oscura", "contenido": "La materia oscura explica la rotación de las galaxias. La energía oscura es responsable de la expansión acelerada del universo."},
            {"titulo": "37. Búsqueda de Exoplanetas", "contenido": "Los exoplanetas se detectan con métodos como el tránsito (cuando el planeta pasa frente a su estrella) y la velocidad radial."},
            {"titulo": "38. Ley de Hubble", "contenido": "La velocidad a la que se alejan las galaxias es directamente proporcional a su distancia, lo que demuestra la expansión del universo."},
            {"titulo": "39. Inducción Electromagnética", "contenido": "Un campo magnético variable induce una corriente eléctrica en un conductor. Este principio es la base de los generadores eléctricos."},
            {"titulo": "40. Ecuaciones de Maxwell", "contenido": "Son un conjunto de cuatro ecuaciones que describen todos los fenómenos del electromagnetismo, unificando los campos eléctrico y magnético."},
            {"titulo": "41. Circuitos de Corriente Alterna (CA)", "contenido": "En un circuito de CA, la corriente y el voltaje cambian de dirección periódicamente. Se usan en la red eléctrica."},
            {"titulo": "42. Transformadores", "contenido": "Dispositivos que aumentan o disminuyen el voltaje de la corriente alterna mediante inducción electromagnética."},
            {"titulo": "43. Radiación de Cuerpo Negro", "contenido": "Es la radiación térmica emitida por un objeto a una temperatura dada. Su estudio llevó al desarrollo de la mecánica cuántica."},
            {"titulo": "44. Partículas Elementales", "contenido": "Las partículas que componen la materia (quarks y leptones) y las partículas portadoras de fuerzas (bosones)."},
            {"titulo": "45. Aceleradores de Partículas", "contenido": "Se usan para estudiar las partículas subatómicas y sus interacciones. El LHC es el acelerador más grande del mundo."},
            {"titulo": "46. Propiedades de los semiconductores", "contenido": "Su conductividad eléctrica se encuentra entre la de un conductor y la de un aislante, y puede ser alterada por dopaje."},
            {"titulo": "47. Física de partículas", "contenido": "Rama de la física que estudia las partículas elementales que componen la materia y la radiación."},
            {"titulo": "48. Reacciones nucleares", "contenido": "La fisión nuclear es la división de un núcleo pesado en núcleos más ligeros; la fusión es la unión de núcleos ligeros."},
            {"titulo": "49. Relatividad General", "contenido": "Extensión de la relatividad especial que incluye la gravedad. Describe la gravedad como la deformación del espacio-tiempo."},
            {"titulo": "50. Lentes Gravitacionales", "contenido": "La luz de un objeto distante es desviada por la masa de otro objeto intermedio, creando un efecto de lente de aumento."},

            # SECCIÓN 3: BIOLOGÍA MOLECULAR Y GENÉTICA AVANZADA
            {"titulo": "51. Replicación del ADN", "contenido": "Es el proceso por el cual el ADN se duplica. Involucra enzimas como la helicasa, la primasa y la ADN polimerasa."},
            {"titulo": "52. Transcripción", "contenido": "Es la síntesis de una molécula de ARN a partir de una plantilla de ADN, catalizada por la ARN polimerasa."},
            {"titulo": "53. Traducción", "contenido": "Es la síntesis de proteínas a partir de la información del ARNm, llevada a cabo por los ribosomas."},
            {"titulo": "54. Operón lac", "contenido": "Un clásico modelo de regulación génica en bacterias, que controla la expresión de genes para metabolizar la lactosa."},
            {"titulo": "55. Mutaciones Genéticas", "contenido": "Son cambios en la secuencia del ADN. Pueden ser puntuales (cambio de un solo nucleótido) o cromosómicas."},
            {"titulo": "56. Tecnología CRISPR-Cas9", "contenido": "Es una poderosa herramienta de edición genética que permite cortar y pegar secuencias de ADN con gran precisión."},
            {"titulo": "57. Epigenética", "contenido": "Son cambios heredables en la expresión génica que no implican cambios en la secuencia del ADN. Ej: metilación."},
            {"titulo": "58. Apoptosis", "contenido": "Es la muerte celular programada. Es un proceso controlado y crucial para el desarrollo y la homeostasis de los organismos."},
            {"titulo": "59. Bioinformática", "contenido": "Campo que utiliza la computación para analizar datos biológicos, como la secuenciación del genoma o la estructura de proteínas."},
            {"titulo": "60. Diferenciación Celular", "contenido": "Es el proceso por el cual una célula se especializa para realizar una función específica. Es clave en la embriogénesis."},
            {"titulo": "61. Oncogenes y Supresores de Tumores", "contenido": "Los oncogenes promueven la división celular descontrolada. Los supresores de tumores la inhiben. Un desequilibrio causa cáncer."},
            {"titulo": "62. Vías de Señalización Celular", "contenido": "Son redes de comunicación intracelular que controlan procesos como el crecimiento, la diferenciación y la muerte celular."},
            {"titulo": "63. Inmunología", "contenido": "Es el estudio del sistema inmunitario, que defiende al cuerpo de patógenos. Incluye la respuesta inmune innata y adaptativa."},
            {"titulo": "64. Virología Molecular", "contenido": "Estudia los virus a nivel molecular, incluyendo su estructura, replicación y cómo infectan a las células."},
            {"titulo": "65. Regulación Hormonal", "contenido": "Las hormonas son mensajeros químicos que regulan procesos fisiológicos como el metabolismo, el crecimiento y la reproducción."},
            {"titulo": "66. Neurotransmisores y Sinapsis", "contenido": "Los neurotransmisores son moléculas que transmiten señales entre neuronas en la sinapsis."},
            {"titulo": "67. Ciclo de vida del parásito de la malaria", "contenido": "Un parásito complejo que involucra tanto al mosquito Anopheles como al ser humano, con distintas fases de desarrollo."},
            {"titulo": "68. Genómica y Proteómica", "contenido": "La genómica estudia el genoma completo de un organismo. La proteómica estudia el conjunto de proteínas (proteoma)."},
            {"titulo": "69. Bioingeniería", "contenido": "Aplica los principios de ingeniería para resolver problemas biológicos y médicos, creando dispositivos o terapias."},
            {"titulo": "70. Mecanismos de resistencia a antibióticos", "contenido": "Las bacterias desarrollan resistencia a los antibióticos a través de mutaciones o transferencia de genes."},
            {"titulo": "71. Biología evolutiva del desarrollo", "contenido": "Compara los procesos de desarrollo de diferentes organismos para entender las relaciones evolutivas entre ellos."},
            {"titulo": "72. Enzimología avanzada", "contenido": "Estudio de las enzimas, sus mecanismos de acción, inhibidores y cómo son reguladas en el metabolismo."},
            {"titulo": "73. Genética de poblaciones", "contenido": "Estudia la variación en los genes de las poblaciones para entender los mecanismos de la evolución."},
            {"titulo": "74. Transducción de señales", "contenido": "El proceso por el cual una señal química extracelular es convertida en una respuesta celular."},
            {"titulo": "75. Microambiente tumoral", "contenido": "El ecosistema de células y moléculas que rodean un tumor, clave para su crecimiento y metástasis."},

            # SECCIÓN 4: ECOLOGÍA DE SISTEMAS Y SOSTENIBILIDAD AVANZADA
            {"titulo": "76. Modelos de Dinámica de Poblaciones", "contenido": "Ecuaciones que describen cómo cambia el tamaño de una población en el tiempo, considerando natalidad, mortalidad e inmigración."},
            {"titulo": "77. Interacciones Tróficas Avanzadas", "contenido": "Las redes tróficas no son cadenas simples. Incluyen complejas interacciones de depredación, parasitismo, mutualismo y competencia."},
            {"titulo": "78. Ciclos Biogeoquímicos del Nitrógeno y Fósforo", "contenido": "Son esenciales para la vida. El exceso de nitrógeno o fósforo puede causar eutrofización y dañar ecosistemas acuáticos."},
            {"titulo": "79. Ecología del Paisaje", "contenido": "Estudia la relación entre la estructura espacial de los ecosistemas (patrones de hábitat) y los procesos ecológicos."},
            {"titulo": "80. Modelado del Cambio Climático", "contenido": "Se usan modelos matemáticos y computacionales para predecir los efectos del cambio climático en los ecosistemas y la biosfera."},
            {"titulo": "81. Eutrofización", "contenido": "Es el enriquecimiento excesivo de nutrientes en un cuerpo de agua, causando un crecimiento desmedido de algas y reducción de oxígeno."},
            {"titulo": "82. Biomas y Flujos de Energía", "contenido": "Los biomas (selva, desierto) son ecosistemas a gran escala. La energía fluye a través de ellos, perdiéndose en cada nivel trófico."},
            {"titulo": "83. Resiliencia de Ecosistemas", "contenido": "Es la capacidad de un ecosistema para resistir y recuperarse de perturbaciones, como incendios o inundaciones."},
            {"titulo": "84. Contaminantes Emergentes", "contenido": "Son sustancias químicas, como microplásticos o residuos de fármacos, que se están descubriendo en el ambiente y tienen efectos desconocidos."},
            {"titulo": "85. Ecología evolutiva", "contenido": "Combina la ecología y la evolución para entender cómo las interacciones ecológicas influyen en los procesos evolutivos."},
            {"titulo": "86. Sucesión ecológica", "contenido": "Proceso por el cual la estructura de una comunidad biológica cambia a lo largo del tiempo después de una perturbación."},
            {"titulo": "87. Servicios ecosistémicos de regulación", "contenido": "Beneficios que obtenemos de los ecosistemas, como la purificación del aire y del agua, la polinización y la regulación del clima."},
            {"titulo": "88. Biología de la Conservación", "contenido": "Disciplina que busca proteger la biodiversidad, estudiando las causas de su declive y proponiendo soluciones."},
            {"titulo": "89. Mitigación y adaptación al cambio climático", "contenido": "Mitigación: reducir las emisiones de gases de efecto invernadero. Adaptación: prepararse para los efectos inevitables del cambio climático."},
            {"titulo": "90. Ciclos de retroalimentación", "contenido": "Mecanismos que amplifican (retroalimentación positiva) o amortiguan (retroalimentación negativa) un cambio en un sistema ecológico."},
            {"titulo": "91. Ecología de la restauración", "contenido": "Ciencia de ayudar a la recuperación de ecosistemas que han sido dañados o destruidos."},
            {"titulo": "92. Indicadores biológicos", "contenido": "Organismos que nos dan información sobre la salud de un ecosistema, como los líquenes para la calidad del aire."},
            {"titulo": "93. Bioacumulación y biomagnificación", "contenido": "Bioacumulación: un contaminante se acumula en un organismo. Biomagnificación: la concentración aumenta a medida que sube en la cadena trófica."},
            {"titulo": "94. Conectividad del paisaje", "contenido": "Grado en que el paisaje facilita o impide el movimiento de las especies. Es vital para la biodiversidad."},
            {"titulo": "95. Huella hídrica y huella de carbono", "contenido": "Huella hídrica: volumen de agua usado en la producción de bienes. Huella de carbono: gases de efecto invernadero emitidos."},
            {"titulo": "96. Ecología de las enfermedades infecciosas", "contenido": "Estudia cómo las interacciones entre los organismos y el medio ambiente influyen en la propagación de enfermedades."},
            {"titulo": "97. Resiliencia urbana", "contenido": "Capacidad de las ciudades para prepararse, resistir y recuperarse de desastres naturales o shocks sociales."},
            {"titulo": "98. Biodiversidad funcional", "contenido": "Variedad de roles ecológicos en un ecosistema. Es más importante para la estabilidad que el número de especies."},
            {"titulo": "99. Especies clave", "contenido": "Especies que tienen un impacto desproporcionado en su ecosistema. Ej: los lobos en Yellowstone."},
            {"titulo": "100. Contaminación del suelo", "contenido": "El uso excesivo de fertilizantes o pesticidas puede degradar la calidad del suelo, afectando la agricultura y los ecosistemas."}
        ]

        self.current_exercise_index = 0
        self.paraphrases = [None] * len(self.ejercicios)
        self.total_exercises = len(self.ejercicios)
        self.is_editing = False

        self.setup_ui()
        self.load_exercise()

    def setup_ui(self):
        """
        Configura todos los widgets de la interfaz principal de la aplicación.
        """
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill="both", expand=True)

        # Título principal
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales", font=("Helvetica", 20, "bold"), foreground="#333333")
        title_label.pack(pady=(0, 10))

        # Contador de ejercicios
        self.counter_label = ttk.Label(main_frame, text="", font=("Helvetica", 14), foreground="#555555")
        self.counter_label.pack(pady=(0, 10))

        # Contenedor para el ejercicio
        exercise_frame = ttk.Frame(main_frame, padding="15", relief="solid", borderwidth=1, style="Card.TFrame")
        exercise_frame.pack(fill="both", expand=True, pady=10)

        self.exercise_title_label = ttk.Label(exercise_frame, text="", font=("Helvetica", 12, "bold"), wraplength=700)
        self.exercise_title_label.pack(fill="x", pady=(0, 5))
        
        self.exercise_content_text = scrolledtext.ScrolledText(exercise_frame, wrap=tk.WORD, height=8, font=("Helvetica", 12), state='disabled', relief="flat", bg="#fcfcfc")
        self.exercise_content_text.pack(fill="both", expand=True)

        # Área de paráfrasis
        paraphrase_label = ttk.Label(main_frame, text="Escribe tu paráfrasis aquí:", font=("Helvetica", 12), foreground="#333333")
        paraphrase_label.pack(pady=(10, 5), anchor="w")
        
        self.paraphrase_input_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, height=6, font=("Helvetica", 12))
        self.paraphrase_input_text.pack(fill="both", expand=True)

        # Contenedor para los botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Botón para revisar y editar
        review_button = ttk.Button(button_frame, text="Revisar y Editar Paráfrasis", command=self.open_review_window)
        review_button.pack(side="left", padx=5)
        
        # Botón principal de acción
        self.action_button = ttk.Button(button_frame, text="Siguiente Ejercicio", command=self.handle_action)
        self.action_button.pack(side="left", padx=5)
        
        # Botón para guardar en archivo
        save_button = ttk.Button(button_frame, text="Guardar todas las paráfrasis", command=self.save_paraphrases_to_file)
        save_button.pack(side="left", padx=5)
        
        # Estilo para los frames
        self.style = ttk.Style(self)
        self.style.configure("Card.TFrame", background="#e9e9e9", padding=10, relief="flat", borderwidth=1, bordercolor="#cccccc")

    def load_exercise(self, index=None):
        """
        Carga y muestra el ejercicio en el índice especificado (o el actual).
        """
        self.is_editing = False
        self.action_button.config(text="Siguiente Ejercicio")
        
        if index is not None:
            self.current_exercise_index = index
        
        if self.current_exercise_index < self.total_exercises:
            exercise = self.ejercicios[self.current_exercise_index]
            self.counter_label.config(text=f"Ejercicio {self.current_exercise_index + 1} de {self.total_exercises}")
            self.exercise_title_label.config(text=exercise['titulo'])

            # Actualizar el contenido del ejercicio (con manejo de estado)
            self.exercise_content_text.config(state='normal')
            self.exercise_content_text.delete('1.0', tk.END)
            self.exercise_content_text.insert('1.0', exercise['contenido'])
            self.exercise_content_text.config(state='disabled')
            
            # Cargar la paráfrasis si ya existe
            paraphrase_text = self.paraphrases[self.current_exercise_index]
            self.paraphrase_input_text.delete('1.0', tk.END)
            if paraphrase_text:
                self.paraphrase_input_text.insert('1.0', paraphrase_text)
        else:
            self.counter_label.config(text="¡Has completado todos los ejercicios! 🎉")
            self.exercise_title_label.config(text="Puedes guardar tus paráfrasis ahora.")
            self.exercise_content_text.config(state='normal')
            self.exercise_content_text.delete('1.0', tk.END)
            self.exercise_content_text.config(state='disabled')
            self.paraphrase_input_text.config(state='disabled')
            self.action_button.config(state='disabled')

    def handle_action(self):
        """
        Maneja la acción del botón principal ('Siguiente' o 'Guardar').
        """
        if self.is_editing:
            self.save_edited_paraphrase()
        else:
            self.next_exercise()

    def next_exercise(self):
        """
        Guarda la paráfrasis actual y avanza al siguiente ejercicio.
        """
        paraphrase = self.paraphrase_input_text.get('1.0', tk.END).strip()
        self.paraphrases[self.current_exercise_index] = paraphrase if paraphrase else "OMITIDO"
        
        self.current_exercise_index += 1
        self.load_exercise()

    def open_review_window(self):
        """
        Crea y abre una ventana emergente para revisar y editar paráfrasis.
        """
        review_win = tk.Toplevel(self)
        review_win.title("Revisar y Editar Paráfrasis")
        review_win.geometry("500x600")
        review_win.configure(bg="#f0f0f0")
        
        frame = ttk.Frame(review_win, padding="15")
        frame.pack(fill="both", expand=True)

        list_label = ttk.Label(frame, text="Selecciona un ejercicio para editar:", font=("Helvetica", 14, "bold"))
        list_label.pack(pady=(0, 10))

        listbox = tk.Listbox(frame, font=("Helvetica", 12), selectmode=tk.SINGLE, height=20)
        listbox.pack(fill="both", expand=True, pady=(0, 10))
        
        # Llenar el Listbox con los ejercicios y su estado
        for i, exercise in enumerate(self.ejercicios):
            status = "✅" if self.paraphrases[i] else "❓"
            listbox.insert(tk.END, f"{status} Ejercicio {i + 1}: {exercise['titulo']}")
        
        # Vincular el evento de selección del Listbox a una función
        def on_select(event):
            selected_index = listbox.curselection()
            if selected_index:
                index = selected_index[0]
                review_win.destroy()  # Cerrar la ventana emergente
                self.load_for_editing(index)
        
        listbox.bind('<<ListboxSelect>>', on_select)

    def load_for_editing(self, index):
        """
        Carga el ejercicio especificado para su edición.
        """
        self.is_editing = True
        self.current_exercise_index = index
        self.action_button.config(text="Guardar Edición")
        
        exercise = self.ejercicios[self.current_exercise_index]
        self.counter_label.config(text=f"Editando Ejercicio {self.current_exercise_index + 1}")
        self.exercise_title_label.config(text=exercise['titulo'])

        self.exercise_content_text.config(state='normal')
        self.exercise_content_text.delete('1.0', tk.END)
        self.exercise_content_text.insert('1.0', exercise['contenido'])
        self.exercise_content_text.config(state='disabled')
        
        self.paraphrase_input_text.config(state='normal')
        self.paraphrase_input_text.delete('1.0', tk.END)
        self.paraphrase_input_text.insert('1.0', self.paraphrases[self.current_exercise_index])

    def save_edited_paraphrase(self):
        """
        Guarda la paráfrasis editada y revierte la interfaz a la normalidad.
        """
        paraphrase = self.paraphrase_input_text.get('1.0', tk.END).strip()
        self.paraphrases[self.current_exercise_index] = paraphrase if paraphrase else "OMITIDO"
        
        self.is_editing = False
        messagebox.showinfo("Guardado", f"La paráfrasis del Ejercicio {self.current_exercise_index + 1} ha sido guardada.")
        self.load_exercise(self.current_exercise_index)
        
    def save_paraphrases_to_file(self):
        """
        Guarda todas las paráfrasis en un archivo de texto.
        """
        nombre_archivo = "parafrasis_ciencias_12_tkinter.txt"
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                for i, item in enumerate(self.paraphrases):
                    if item and item != "OMITIDO":
                        original_content = self.ejercicios[i]['contenido']
                        titulo = self.ejercicios[i]['titulo']
                        archivo.write(f"--- Ejercicio {i + 1} - {titulo} ---\n")
                        archivo.write(f"Texto original: {original_content}\n")
                        archivo.write(f"Tu paráfrasis: {item}\n\n")
            
            messagebox.showinfo("Guardado Completo", f"¡Guardado Exitoso! ✅\nSe ha creado el archivo '{nombre_archivo}'.")
        except IOError as e:
            messagebox.showerror("Error de Archivo", f"Error: No se pudo guardar el archivo.\n{e}")

if __name__ == '__main__':
    app = ParaphraseApp()
    app.mainloop()

