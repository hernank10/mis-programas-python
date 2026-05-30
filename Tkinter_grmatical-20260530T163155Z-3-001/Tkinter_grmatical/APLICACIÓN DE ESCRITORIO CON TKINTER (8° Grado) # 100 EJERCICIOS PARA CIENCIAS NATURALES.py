# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (8° Grado)
# 100 EJERCICIOS PARA CIENCIAS NATURALES
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de octavo grado, cubriendo temas
# de ecología, genética avanzada, química inorgánica, física del movimiento
# y geología.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox
import os

class NaturalSciencesApp:
    """
    Clase principal que maneja la interfaz de usuario y la lógica de la aplicación.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Ciencias Naturales (8° Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para octavo grado de ciencias naturales
        self.ejercicios = [
            # SECCIÓN 1: BIOLOGÍA - ECOLOGÍA Y GENÉTICA AVANZADA (25 EJERCICIOS)
            {"titulo": "1. Niveles de organización ecológica", "contenido": "Describe los niveles de organización de la ecología, desde individuo hasta biosfera, y da un ejemplo para cada nivel."},
            {"titulo": "2. Ecosistemas y sus componentes", "contenido": "Diferencia entre los componentes bióticos y abióticos de un ecosistema. ¿Qué papel juegan en la interacción?"},
            {"titulo": "3. Cadenas y redes tróficas", "contenido": "Explica la diferencia entre una cadena y una red trófica. ¿Qué representan los descomponedores en estas interacciones?"},
            {"titulo": "4. Flujo de energía y ciclos de la materia", "contenido": "Describe cómo fluye la energía a través de un ecosistema. Explica el concepto del ciclo de la materia."},
            {"titulo": "5. Biodiversidad", "contenido": "Define biodiversidad y explica por qué es importante para la estabilidad de los ecosistemas."},
            {"titulo": "6. Adaptación de las especies", "contenido": "Explica el concepto de adaptación en los seres vivos. Da un ejemplo de una adaptación física y una de comportamiento."},
            {"titulo": "7. Especies en peligro de extinción", "contenido": "Menciona tres causas principales por las que las especies están en peligro de extinción y sugiere una medida de conservación."},
            {"titulo": "8. Herencia no mendeliana", "contenido": "Explica qué es la herencia codominante y la herencia de dominancia incompleta. Da un ejemplo para cada una."},
            {"titulo": "9. Árboles genealógicos", "contenido": "Describe qué información se puede obtener al analizar un árbol genealógico. ¿Qué símbolos se usan para representar sexos y parentescos?"},
            {"titulo": "10. Mutaciones genéticas", "contenido": "Define qué es una mutación genética. Nombra un tipo de mutación (ej. puntual, cromosómica) y explica su efecto."},
            {"titulo": "11. Biología molecular", "contenido": "Explica el dogma central de la biología: la replicación, transcripción y traducción. ¿Qué rol juega el ARN?"},
            {"titulo": "12. Ecología de poblaciones", "contenido": "Describe los factores que limitan el crecimiento de una población (ej. recursos, depredación, enfermedades)."},
            {"titulo": "13. El sistema nervioso humano", "contenido": "Diferencia entre el sistema nervioso central y el periférico. Nombra las funciones principales de cada uno."},
            {"titulo": "14. Neuronas y sinapsis", "contenido": "Explica la estructura básica de una neurona y cómo se produce la transmisión de un impulso nervioso a través de la sinapsis."},
            {"titulo": "15. El sistema endocrino y las hormonas", "contenido": "Describe cómo funcionan las hormonas para regular los procesos corporales. Nombra dos hormonas y sus funciones (ej. adrenalina, insulina)."},
            {"titulo": "16. Los cinco sentidos", "contenido": "Nombra los cinco sentidos y describe brevemente la estructura del ojo o el oído."},
            {"titulo": "17. Homeostasis en el cuerpo humano", "contenido": "Explica el concepto de homeostasis con un ejemplo más detallado, como la regulación de la glucosa en la sangre."},
            {"titulo": "18. Enfermedades genéticas", "contenido": "Menciona una enfermedad genética recesiva (ej. albinismo, fibrosis quística) y explica cómo se transmite."},
            {"titulo": "19. Impacto ambiental humano", "contenido": "Describe tres formas en las que la actividad humana impacta negativamente los ecosistemas (ej. deforestación, contaminación)."},
            {"titulo": "20. Soluciones sostenibles", "contenido": "Menciona y explica tres acciones que se pueden tomar para promover la sostenibilidad ambiental a nivel local."},
            {"titulo": "21. El sistema inmunológico", "contenido": "Explica la diferencia entre la inmunidad innata y la inmunidad adquirida. ¿Qué papel juegan las vacunas?"},
            {"titulo": "22. El metabolismo celular", "contenido": "Diferencia entre el catabolismo y el anabolismo. ¿Qué proceso es la respiración celular?"},
            {"titulo": "23. La genética y la clonación", "contenido": "Explica el proceso de clonación reproductiva y terapéutica. ¿Cuáles son las diferencias y las implicaciones éticas?"},
            {"titulo": "24. Células madre", "contenido": "¿Qué son las células madre y por qué son importantes en la medicina regenerativa? Nombra dos tipos de células madre."},
            {"titulo": "25. La comunicación en los animales", "contenido": "Describe tres tipos de comunicación animal (química, sonora, visual) y da un ejemplo de cada uno."},

            # SECCIÓN 2: QUÍMICA - ÁTOMOS, MOLÉCULAS Y REACCIONES (25 EJERCICIOS)
            {"titulo": "26. Estructura atómica avanzada", "contenido": "Describe el modelo atómico de la mecánica cuántica y la distribución de electrones en orbitales (niveles, subniveles)."},
            {"titulo": "27. La tabla periódica: grupos y periodos", "contenido": "Explica qué información se puede obtener de la tabla periódica con respecto a los grupos y periodos de los elementos."},
            {"titulo": "28. Propiedades periódicas", "contenido": "Define qué es la electronegatividad, el radio atómico y la energía de ionización. ¿Cómo varían en la tabla periódica?"},
            {"titulo": "29. Nomenclatura de compuestos inorgánicos", "contenido": "Nombra los siguientes compuestos: $H_2SO_4$, $NaOH$, $CO_2$, $FeCl_3$."},
            {"titulo": "30. Formación de óxidos, ácidos e hidróxidos", "contenido": "Escribe la fórmula química de un óxido básico, un óxido ácido, un hidróxido y un ácido oxácido."},
            {"titulo": "31. Reacciones de óxido-reducción", "contenido": "Identifica los agentes oxidantes y reductores en la siguiente reacción: $2Na + Cl_2 -> 2NaCl$."},
            {"titulo": "32. Enlaces químicos (metálicos)", "contenido": "Describe el enlace metálico. ¿Qué propiedades de los metales se explican por este tipo de enlace?"},
            {"titulo": "33. Concentración de soluciones", "contenido": "Diferencia entre soluciones diluidas, concentradas, saturadas y sobresaturadas. Da un ejemplo de cada una."},
            {"titulo": "34. Ácidos y bases (teorías)", "contenido": "Explica la teoría de Arrhenius sobre ácidos y bases. Da un ejemplo de un ácido y una base según esta teoría."},
            {"titulo": "35. Ecuaciones químicas balanceadas", "contenido": "Balancea la siguiente ecuación química: $C_3H_8 + O_2 -> CO_2 + H_2O$."},
            {"titulo": "36. Ley de las proporciones definidas", "contenido": "Explica la ley de las proporciones definidas de Proust. ¿Qué significa para los compuestos químicos?"},
            {"titulo": "37. Estequiometría", "contenido": "En la reacción de formación del agua ($2H_2 + O_2 -> 2H_2O$), si reaccionan 4 moles de hidrógeno, ¿cuántos moles de oxígeno se necesitan?"},
            {"titulo": "38. Polímeros", "contenido": "Define qué es un polímero. Da un ejemplo de un polímero natural y uno sintético y menciona un uso de cada uno."},
            {"titulo": "39. El petróleo", "contenido": "Describe el proceso de destilación fraccionada del petróleo. ¿Qué productos se obtienen?"},
            {"titulo": "40. Reacciones nucleares", "contenido": "Diferencia entre la fusión y la fisión nuclear. ¿Qué ocurre con la masa en estas reacciones?"},
            {"titulo": "41. La química y el medio ambiente", "contenido": "Explica qué es la lluvia ácida, cuáles son sus causas y sus efectos."},
            {"titulo": "42. La capa de ozono", "contenido": "Describe la función de la capa de ozono y cómo se produce su deterioro. ¿Qué son los CFCs?"},
            {"titulo": "43. Isómeros", "contenido": "Define el concepto de isómero. Proporciona un ejemplo sencillo de dos isómeros de una misma fórmula química."},
            {"titulo": "44. La polaridad de las moléculas", "contenido": "Explica qué es una molécula polar y una no polar. ¿Por qué el agua es una molécula polar?"},
            {"titulo": "45. El número de Avogadro", "contenido": "¿Qué es el número de Avogadro y para qué se usa? Explica el concepto de mol."},
            {"titulo": "46. Electrolitos", "contenido": "Define un electrolito. Nombra una sustancia que sea un electrolito fuerte y otra que sea un electrolito débil."},
            {"titulo": "47. Química forense", "contenido": "Menciona dos aplicaciones de la química forense en la investigación criminal."},
            {"titulo": "48. Cromatografía", "contenido": "Describe el proceso de la cromatografía y sus aplicaciones para separar componentes de una mezcla."},
            {"titulo": "49. Reacciones de neutralización", "contenido": "Explica qué es una reacción de neutralización. ¿Qué productos se forman al reaccionar un ácido fuerte con una base fuerte?"},
            {"titulo": "50. La química y la agricultura", "contenido": "Describe el papel de los fertilizantes y los pesticidas en la agricultura moderna. ¿Cuáles son sus ventajas y desventajas?"},

            # SECCIÓN 3: FÍSICA - MOVIMIENTO, FUERZAS Y ENERGÍA (25 EJERCICIOS)
            {"titulo": "51. Cinemática: movimiento rectilíneo", "contenido": "Diferencia entre distancia y desplazamiento. Define velocidad y aceleración."},
            {"titulo": "52. Gráficas de movimiento", "contenido": "Describe qué representa una gráfica de posición vs. tiempo para un objeto en movimiento rectilíneo uniforme."},
            {"titulo": "53. Caída libre", "contenido": "Explica el concepto de caída libre. ¿Cuál es la aceleración de la gravedad y cómo afecta a los objetos que caen?"},
            {"titulo": "54. Las tres leyes de Newton", "contenido": "Enuncia las tres leyes de Newton con un ejemplo para cada una."},
            {"titulo": "55. Rozamiento y fricción", "contenido": "Explica qué es la fuerza de rozamiento. ¿Qué diferencia hay entre fricción estática y cinética?"},
            {"titulo": "56. El concepto de trabajo y potencia", "contenido": "Define trabajo y potencia. ¿Qué unidades de medida se usan para cada una en el SI?"},
            {"titulo": "57. Energía cinética y potencial", "contenido": "Calcula la energía cinética de un coche de 1000 kg que se mueve a 20 m/s. Escribe la fórmula."},
            {"titulo": "58. Conservación del momento lineal", "contenido": "Explica el principio de conservación del momento lineal con un ejemplo, como un choque de billar."},
            {"titulo": "59. Sonido: ondas sonoras", "contenido": "Describe las propiedades del sonido: tono, intensidad y timbre. ¿De qué depende cada una?"},
            {"titulo": "60. Reflexión y refracción del sonido", "contenido": "Diferencia entre el eco y la reverberación. ¿Cómo se relaciona con la reflexión del sonido?"},
            {"titulo": "61. Luz y color", "contenido": "Explica por qué vemos los objetos de un determinado color. ¿Qué es la síntesis aditiva y sustractiva de los colores?"},
            {"titulo": "62. Espejos y lentes", "contenido": "Diferencia entre un espejo cóncavo y uno convexo. ¿Qué tipo de imagen forma cada uno?"},
            {"titulo": "63. Fenómenos ondulatorios", "contenido": "Define difracción e interferencia de ondas. Da un ejemplo de cada uno."},
            {"titulo": "64. Carga eléctrica y ley de Coulomb", "contenido": "Explica la ley de Coulomb. ¿Cómo se relacionan las cargas eléctricas y las fuerzas entre ellas?"},
            {"titulo": "65. Circuito eléctrico: ley de Ohm", "contenido": "Enuncia la ley de Ohm. Si tienes una resistencia de 10 Ω y una tensión de 20 V, ¿cuál es la corriente?"},
            {"titulo": "66. Potencia eléctrica", "contenido": "Define potencia eléctrica. Si un bombillo consume 60 W y está conectado a 120 V, ¿cuánta corriente consume?"},
            {"titulo": "67. Magnetismo y campos magnéticos", "contenido": "Describe qué es un campo magnético. Dibuja las líneas de campo de un imán de barra."},
            {"titulo": "68. Inducción electromagnética", "contenido": "Explica el principio de la inducción electromagnética. ¿Cómo se utiliza para generar electricidad en una central?"},
            {"titulo": "69. Transformadores", "contenido": "Describe la función de un transformador. ¿Por qué son esenciales en la distribución de energía eléctrica?"},
            {"titulo": "70. Energía y sus transformaciones", "contenido": "Describe la transformación de energía en un péndulo. ¿Qué es la energía mecánica?"},
            {"titulo": "71. El calor y la temperatura", "contenido": "Diferencia entre calor y temperatura. ¿Qué escalas de temperatura se usan comúnmente?"},
            {"titulo": "72. Propagación del calor", "contenido": "Describe los mecanismos de propagación del calor: conducción, convección y radiación. Da un ejemplo de cada uno."},
            {"titulo": "73. La presión en los fluidos", "contenido": "Explica el concepto de presión hidrostática. ¿Qué es la densidad de un fluido?"},
            {"titulo": "74. Principio de Arquímedes", "contenido": "Enuncia el principio de Arquímedes. Explica por qué un barco flota."},
            {"titulo": "75. Física en la vida diaria", "contenido": "Menciona tres ejemplos de principios de la física que se aplican en la tecnología moderna (ej. GPS, smartphones, microondas)."},

            # SECCIÓN 4: CIENCIAS DE LA TIERRA Y EL UNIVERSO (25 EJERCICIOS)
            {"titulo": "76. La atmósfera: composición y estructura", "contenido": "Nombra las capas de la atmósfera y describe las funciones de la ionosfera y la exosfera."},
            {"titulo": "77. El clima y el tiempo", "contenido": "Diferencia entre el tiempo meteorológico y el clima. ¿Qué factores influyen en el clima de una región?"},
            {"titulo": "78. El efecto invernadero", "contenido": "Explica en detalle el mecanismo del efecto invernadero. Nombra tres gases de efecto invernadero."},
            {"titulo": "79. Formación de las nubes y las precipitaciones", "contenido": "Describe el proceso de formación de las nubes y los diferentes tipos de precipitación."},
            {"titulo": "80. La hidrosfera: océanos y aguas continentales", "contenido": "Diferencia entre la salinidad y la densidad del agua de mar. Explica la importancia de las corrientes oceánicas."},
            {"titulo": "81. Ciclo hidrológico", "contenido": "Describe las etapas del ciclo del agua: evaporación, condensación, precipitación, infiltración y escorrentía."},
            {"titulo": "82. Geología: tipos de rocas", "contenido": "Describe los tres tipos de rocas: ígneas, sedimentarias y metamórficas. Explica cómo se transforma una roca en otra a través del ciclo."},
            {"titulo": "83. La tectónica de placas", "contenido": "Explica la teoría de la tectónica de placas. ¿Qué son los puntos calientes y los arcos de islas?"},
            {"titulo": "84. Volcanes y terremotos", "contenido": "Diferencia entre un volcán activo, durmiente y extinto. ¿Qué es un sismo y cómo se origina?"},
            {"titulo": "85. La escala de magnitud sísmica", "contenido": "Explica la escala de magnitud de momento y la de Mercalli. ¿Cuál mide la energía liberada y cuál la intensidad de los efectos?"},
            {"titulo": "86. Recursos naturales: no renovables", "contenido": "Nombra tres recursos energéticos no renovables (petróleo, carbón, gas natural) y describe los problemas ambientales de su uso."},
            {"titulo": "87. Recursos naturales: renovables", "contenido": "Nombra tres recursos energéticos renovables (solar, eólica, geotérmica) y sus ventajas comparadas con los no renovables."},
            {"titulo": "88. Contaminación del aire", "contenido": "Menciona los principales contaminantes del aire (ej. monóxido de carbono, óxidos de nitrógeno) y sus efectos en la salud."},
            {"titulo": "89. El universo: el sistema solar", "contenido": "Explica la diferencia entre un planeta, un planeta enano, un satélite y un asteroide. Da un ejemplo de cada uno."},
            {"titulo": "90. Estrellas, galaxias y la Vía Láctea", "contenido": "Describe la estructura de una galaxia espiral como la Vía Láctea. ¿En qué parte de ella se encuentra nuestro sistema solar?"},
            {"titulo": "91. El ciclo de vida de las estrellas", "contenido": "Explica las etapas del ciclo de vida de una estrella de masa similar al Sol. ¿Qué ocurre al final de su vida?"},
            {"titulo": "92. Agujeros negros y cuásares", "contenido": "Define qué es un agujero negro y un cuásar. ¿Cómo se forman?"},
            {"titulo": "93. La teoría del Big Bang", "contenido": "Explica las evidencias principales que respaldan la teoría del Big Bang (expansión, radiación de fondo de microondas)."},
            {"titulo": "94. La Luna y sus fases", "contenido": "Explica las fases de la Luna y por qué las vemos. Describe qué es un eclipse solar y uno lunar."},
            {"titulo": "95. Meteoritos, meteoroides y cometas", "contenido": "Diferencia entre un meteoroide, un meteoro y un meteorito. ¿Qué es un cometa y qué lo diferencia de un asteroide?"},
            {"titulo": "96. Las mareas", "contenido": "Explica la relación entre la gravedad de la Luna y el Sol y la formación de las mareas."},
            {"titulo": "97. Satélites artificiales", "contenido": "Nombra dos tipos de satélites artificiales y explica su función (ej. satélites de comunicación, satélites meteorológicos)."},
            {"titulo": "98. La contaminación lumínica", "contenido": "Define la contaminación lumínica. ¿Cómo afecta a los observatorios astronómicos y a los animales?"},
            {"titulo": "99. El cambio climático", "contenido": "Describe el fenómeno del cambio climático, sus causas y sus consecuencias principales para el planeta."},
            {"titulo": "100. Astronomía y navegación", "contenido": "Explica cómo se usaban las estrellas y otros objetos celestes en la antigüedad para la navegación."},
        ]

        self.answers = [None] * len(self.ejercicios)
        self.current_exercise_index = 0
        self.is_editing = False

        # Configuración de los estilos para una apariencia moderna
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0")

        # --- Creación de los widgets principales ---

        # Frame principal para contener todos los elementos
        main_frame = ttk.Frame(root, padding="15 15 15 15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título principal
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales (8° Grado)", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=(0, 10))

        # Contador de ejercicios
        self.counter_label = ttk.Label(main_frame, text="", font=("Helvetica", 14))
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
        
        self.exercise_text_widget.config(state=tk.DISABLED) # Bloquear edición del texto del ejercicio

        # Etiqueta para el área de respuesta
        answer_label = ttk.Label(main_frame, text="Escribe tu respuesta aquí:", font=("Helvetica", 12))
        answer_label.pack(pady=(10, 5), anchor="w")

        # Área de texto para la respuesta
        self.answer_text_widget = tk.Text(main_frame, wrap=tk.WORD, height=10, font=("Helvetica", 12), padx=5, pady=5)
        self.answer_text_widget.pack(fill=tk.BOTH, expand=True)

        # Frame para los botones
        button_frame = ttk.Frame(main_frame, padding="10")
        button_frame.pack(fill=tk.X, pady=(10, 0))

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

        listbox = tk.Listbox(frame, font=("Helvetica", 12), selectmode=tk.SINGLE)
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
        filename = "respuestas_ciencias_naturales_octavo_grado_tkinter.txt"
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
