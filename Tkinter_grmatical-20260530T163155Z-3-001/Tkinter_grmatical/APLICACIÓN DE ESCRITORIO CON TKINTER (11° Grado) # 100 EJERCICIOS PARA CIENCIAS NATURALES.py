# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (11° Grado)
# 100 EJERCICIOS PARA CIENCIAS NATURALES
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de undécimo grado, cubriendo temas
# de física avanzada, química orgánica, biología evolutiva y ciencias ambientales.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, Text, Scrollbar, Toplevel
import os

class NaturalSciencesApp:
    """
    Clase principal que maneja la interfaz de usuario y la lógica de la aplicación
    para 100 ejercicios de Ciencias Naturales de undécimo grado.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Ciencias Naturales (11° Grado)")
        self.root.geometry("900x750")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para undécimo grado de ciencias naturales
        self.ejercicios = [
            # SECCIÓN 1: BIOLOGÍA - EVOLUCIÓN, GENÉTICA Y FISIOLOGÍA HUMANA (25 EJERCICIOS)
            {"titulo": "1. Mecanismos de la evolución", "contenido": "Explica la teoría de la selección natural de Darwin y la diferencia entre especiación alopátrica y simpátrica."},
            {"titulo": "2. Evidencias de la evolución", "contenido": "Describe tres evidencias de la evolución (ej. registro fósil, anatomía comparada, bioquímica comparada) y cómo respaldan la teoría."},
            {"titulo": "3. Genética de poblaciones", "contenido": "Enuncia el principio de Hardy-Weinberg y explica su importancia para entender la genética de poblaciones. ¿Qué factores pueden alterar este equilibrio?"},
            {"titulo": "4. Ingeniería genética y terapia génica", "contenido": "Explica cómo se utiliza la tecnología de plásmidos para producir insulina humana. ¿Qué es la terapia génica y cuáles son sus desafíos?"},
            {"titulo": "5. El sistema nervioso central", "contenido": "Describe la función de las principales estructuras del encéfalo humano (corteza cerebral, cerebelo, tronco encefálico) y la importancia de las sinapsis."},
            {"titulo": "6. El sistema endocrino", "contenido": "Nombra tres glándulas endocrinas y las hormonas que producen. Explica cómo la retroalimentación negativa regula la producción de hormonas."},
            {"titulo": "7. Fisiología cardiovascular", "contenido": "Describe el recorrido de la sangre a través del corazón y los pulmones en el ciclo circulatorio doble y completo."},
            {"titulo": "8. Fisiología renal y excreción", "contenido": "Explica las tres etapas principales de la formación de orina en el nefrón (filtración, reabsorción y secreción)."},
            {"titulo": "9. Sistema inmunológico", "contenido": "Diferencia entre la inmunidad innata y la inmunidad adaptativa. ¿Cuál es la función de los linfocitos B y T?"},
            {"titulo": "10. Ciclo celular y cáncer", "contenido": "Explica las fases del ciclo celular. ¿Cómo se relaciona la desregulación de este ciclo con la formación de tumores?"},
            {"titulo": "11. El origen de la vida", "contenido": "Describe la teoría de la panspermia y la hipótesis de la 'sopa primordial' de Oparin y Haldane. ¿Qué experimento la apoya?"},
            {"titulo": "12. La taxonomía de los dominios", "contenido": "Diferencia entre los tres dominios de la vida (Bacteria, Archaea y Eukarya) basándote en la estructura celular."},
            {"titulo": "13. Virología", "contenido": "Explica la diferencia entre el ciclo lítico y el ciclo lisogénico de un virus. ¿Por qué se considera a los virus como seres no vivos?"},
            {"titulo": "14. Mutaciones genéticas", "contenido": "Describe las mutaciones por sustitución de bases, inserción y deleción. ¿Cómo afecta cada una la proteína resultante?"},
            {"titulo": "15. La biotecnología moderna", "contenido": "Menciona dos aplicaciones de la biotecnología en la agricultura (ej. cultivos resistentes a plagas) y dos en la medicina (ej. fármacos biológicos)."},
            {"titulo": "16. Fisiología de las plantas", "contenido": "Explica los procesos de fotosíntesis y respiración celular en las plantas. ¿Cuál es el papel del estoma en estos procesos?"},
            {"titulo": "17. El sistema digestivo humano", "contenido": "Describe el proceso de digestión, absorción y excreción de nutrientes en el sistema digestivo humano."},
            {"titulo": "18. Enfermedades genéticas", "contenido": "Diferencia entre una enfermedad genética autosómica dominante y una recesiva. Da un ejemplo de cada una."},
            {"titulo": "19. Embriología", "contenido": "Describe las etapas iniciales del desarrollo embrionario: segmentación, gastrulación y organogénesis."},
            {"titulo": "20. La teoría endosimbiótica", "contenido": "Explica la teoría endosimbiótica y las evidencias que la respaldan (ej. mitocondrias y cloroplastos)."},
            {"titulo": "21. Genoma humano", "contenido": "Describe brevemente el Proyecto Genoma Humano y las implicaciones de su secuenciación completa."},
            {"titulo": "22. Bioética y manipulación genética", "contenido": "Debate los aspectos éticos de la clonación terapéutica y reproductiva en humanos."},
            {"titulo": "23. Los virus y el control de plagas", "contenido": "Explica el uso de bacteriófagos para controlar infecciones bacterianas. ¿Cuáles son sus ventajas y desventajas?"},
            {"titulo": "24. Fisiología del ejercicio", "contenido": "Describe los cambios fisiológicos que ocurren en el cuerpo humano durante el ejercicio aeróbico y anaeróbico."},
            {"titulo": "25. Regulación de la expresión génica", "contenido": "Explica cómo se regulan los genes en organismos procariotas y eucariotas. ¿Qué es el operón Lac?"},

            # SECCIÓN 2: QUÍMICA - ORGÁNICA, BIOQUÍMICA Y TERMODINÁMICA (25 EJERCICIOS)
            {"titulo": "26. Isómeros estructurales y estereoisómeros", "contenido": "Diferencia entre isómeros de cadena, de posición y de función. ¿Qué es la quiralidad?"},
            {"titulo": "27. Reacciones orgánicas", "contenido": "Describe las reacciones de adición, sustitución y eliminación. Da un ejemplo para cada una con hidrocarburos."},
            {"titulo": "28. Polímeros de condensación", "contenido": "Explica el proceso de polimerización por condensación para formar un poliéster o una poliamida. Da un ejemplo."},
            {"titulo": "29. Grupos funcionales y sus propiedades", "contenido": "Describe la estructura y las propiedades de los alcoholes y las cetonas. ¿Cómo se nombran?"},
            {"titulo": "30. La Ley de Hess", "contenido": "Enuncia la Ley de Hess y explica cómo se utiliza para calcular la entalpía de una reacción. Da un ejemplo."},
            {"titulo": "31. Termodinámica: Entropía y Energía de Gibbs", "contenido": "Explica cómo la ecuación de la energía libre de Gibbs ($\Delta G = \Delta H - T\Delta S$) predice la espontaneidad de una reacción."},
            {"titulo": "32. Electrólisis y celdas galvánicas", "contenido": "Diferencia entre una celda galvánica y una celda electrolítica en términos de la espontaneidad de la reacción y el flujo de electrones."},
            {"titulo": "33. Bioquímica: aminoácidos y proteínas", "contenido": "Describe las cuatro estructuras de una proteína (primaria, secundaria, terciaria, cuaternaria). ¿Qué tipo de enlace las estabiliza?"},
            {"titulo": "34. Bioquímica: lípidos y membranas", "contenido": "Explica la estructura y la función de un fosfolípido en la membrana celular. ¿Qué es una bicapa lipídica?"},
            {"titulo": "35. Reacciones de oxidación y reducción", "contenido": "Balancea la siguiente ecuación por el método de ion-electrón en medio ácido: $MnO_4^{-} + Fe^{2+} \to Mn^{2+} + Fe^{3+}$. "},
            {"titulo": "36. Ácidos y bases de Lewis", "contenido": "Diferencia entre un ácido de Arrhenius, de Brønsted-Lowry y de Lewis. Da un ejemplo de un ácido de Lewis."},
            {"titulo": "37. El efecto buffer", "contenido": "Explica el concepto de una solución amortiguadora (buffer) y su importancia en los sistemas biológicos."},
            {"titulo": "38. Química de la atmósfera", "contenido": "Describe el ciclo del ozono en la estratosfera y el papel de los CFCs en su destrucción. ¿Qué es el ozono troposférico?"},
            {"titulo": "39. Petroquímica", "contenido": "Explica el proceso de craqueo catalítico del petróleo. ¿Qué productos se obtienen y para qué se utilizan?"},
            {"titulo": "40. Cinética enzimática", "contenido": "Describe la cinética de Michaelis-Menten. ¿Qué es la constante $K_M$ y la velocidad máxima $V_{max}$?"},
            {"titulo": "41. Estequiometría avanzada", "contenido": "Calcula la masa de $CO_2$ producida al quemar 100 g de butano ($C_4H_{10}$) en una combustión completa."},
            {"titulo": "42. Reacciones de esterificación", "contenido": "Describe la reacción de esterificación y su importancia en la producción de fragancias y saborizantes."},
            {"titulo": "43. Propiedades coligativas", "contenido": "Explica cómo la adición de sal a la carretera en invierno ayuda a derretir el hielo. ¿Qué propiedad coligativa está involucrada?"},
            {"titulo": "44. Química nuclear", "contenido": "Diferencia entre la fisión y la fusión nuclear. ¿Qué partículas se utilizan para iniciar una reacción de fisión en cadena?"},
            {"titulo": "45. Termoquímica y calor de combustión", "contenido": "Define el calor de combustión. ¿Cómo se mide y por qué es importante para la industria de los combustibles?"},
            {"titulo": "46. Electronegatividad y tipos de enlace", "contenido": "Explica la diferencia entre enlaces covalentes no polares, polares e iónicos, basándote en la electronegatividad."},
            {"titulo": "47. Mecanismos de reacción", "contenido": "Describe el mecanismo de reacción $S_N1$ y $S_N2$. ¿Qué factores determinan qué mecanismo predomina?"},
            {"titulo": "48. Reacciones ácido-base", "contenido": "Define pH y pOH. ¿Cuál es la relación entre el pH y la concentración de iones $H^+$ en una solución acuosa?"},
            {"titulo": "49. Cinética química", "contenido": "Explica la diferencia entre el orden de una reacción y su molecularidad. ¿Qué es una reacción de orden cero?"},
            {"titulo": "50. Carbohidratos y monosacáridos", "contenido": "Diferencia entre una aldohexosa y una cetohexosa. Nombra dos monosacáridos comunes y sus fórmulas."},

            # SECCIÓN 3: FÍSICA - FÍSICA MODERNA, ELECTROMAGNETISMO Y RELATIVIDAD (25 EJERCICIOS)
            {"titulo": "51. Los postulados de la relatividad especial", "contenido": "Enuncia los dos postulados de la relatividad especial de Einstein y explica qué implica el segundo postulado."},
            {"titulo": "52. Contracción de la longitud y dilatación del tiempo", "contenido": "Explica los conceptos de dilatación del tiempo y contracción de la longitud. Da un ejemplo de cada uno."},
            {"titulo": "53. La ecuación $E=mc^2$ y su interpretación", "contenido": "Explica en detalle el significado de la ecuación $E=mc^2$ y cómo se aplica en la física nuclear."},
            {"titulo": "54. Física cuántica y el cuerpo negro", "contenido": "Describe el problema del 'cuerpo negro' en la física clásica y cómo la teoría cuántica de Planck lo resolvió."},
            {"titulo": "55. El efecto fotoeléctrico", "contenido": "Explica el efecto fotoeléctrico y cómo la teoría de los fotones de Einstein lo explica. ¿Qué es el trabajo de extracción?"},
            {"titulo": "56. El modelo atómico de Bohr", "contenido": "Describe los postulados del modelo atómico de Bohr y cómo resolvió el problema del colapso del átomo de Rutherford."},
            {"titulo": "57. Dualidad onda-partícula de De Broglie", "contenido": "Explica el concepto de la dualidad onda-partícula para la materia. ¿Qué es la longitud de onda de De Broglie?"},
            {"titulo": "58. El principio de incertidumbre de Heisenberg", "contenido": "Enuncia el principio de incertidumbre de Heisenberg. ¿Qué implicaciones tiene para la medición de la posición y el momento de una partícula?"},
            {"titulo": "59. Campos eléctricos y potencial eléctrico", "contenido": "Diferencia entre campo eléctrico y potencial eléctrico. ¿Qué es una superficie equipotencial?"},
            {"titulo": "60. La Ley de Ohm y circuitos eléctricos", "contenido": "Enuncia la Ley de Ohm. Explica cómo calcular la resistencia equivalente de un circuito con resistores en serie y en paralelo."},
            {"titulo": "61. Las Leyes de Kirchhoff", "contenido": "Describe las dos Leyes de Kirchhoff (ley de los nodos y ley de las mallas) y cómo se aplican para resolver circuitos complejos."},
            {"titulo": "62. El campo magnético", "contenido": "Explica cómo un conductor con corriente genera un campo magnético. ¿Cómo se determina su dirección (regla de la mano derecha)?"},
            {"titulo": "63. La fuerza de Lorentz", "contenido": "Describe la fuerza de Lorentz. ¿Qué trayectoria sigue una partícula cargada que se mueve en un campo magnético uniforme?"},
            {"titulo": "64. La Ley de Faraday y la inducción electromagnética", "contenido": "Enuncia la Ley de Faraday. Explica cómo un generador eléctrico convierte la energía mecánica en energía eléctrica."},
            {"titulo": "65. Las ecuaciones de Maxwell", "contenido": "Menciona las cuatro ecuaciones de Maxwell y explica su importancia para unificar la electricidad y el magnetismo."},
            {"titulo": "66. Óptica física: interferencia y difracción", "contenido": "Diferencia entre los fenómenos de interferencia y difracción de la luz. ¿Qué demostró el experimento de la doble rendija de Young?"},
            {"titulo": "67. La teoría cuántica de campos", "contenido": "Define la teoría cuántica de campos (QFT) y su papel en el modelo estándar de partículas elementales."},
            {"titulo": "68. Física de semiconductores", "contenido": "Explica cómo un semiconductor intrínseco se convierte en un semiconductor tipo n o tipo p. ¿Qué es una unión p-n?"},
            {"titulo": "69. Reactores nucleares", "contenido": "Describe el funcionamiento de un reactor nuclear de fisión. ¿Qué son los moderadores y las barras de control?"},
            {"titulo": "70. La energía nuclear de fusión", "contenido": "Explica los desafíos tecnológicos y las ventajas de la energía de fusión nuclear sobre la fisión."},
            {"titulo": "71. El bosón de Higgs", "contenido": "Describe la función del bosón de Higgs y del campo de Higgs en el modelo estándar de partículas. ¿Qué le da masa a las partículas?"},
            {"titulo": "72. La Ley de Gauss para la electricidad y el magnetismo", "contenido": "Enuncia la Ley de Gauss para los campos eléctricos y magnéticos. ¿Qué dice sobre los monopolos magnéticos?"},
            {"titulo": "73. La Ley de Lenz", "contenido": "Enuncia la Ley de Lenz. ¿Cómo se relaciona con la conservación de la energía?"},
            {"titulo": "74. Circuitos de corriente alterna", "contenido": "Describe cómo se comporta un circuito RLC en resonancia. ¿Qué es la impedancia?"},
            {"titulo": "75. Los transformadores", "contenido": "Explica el principio de funcionamiento de un transformador. ¿Cuál es su utilidad en la distribución de energía eléctrica?"},

            # SECCIÓN 4: CIENCIAS AMBIENTALES Y ASTROFÍSICA (25 EJERCICIOS)
            {"titulo": "76. Biogeoquímica avanzada", "contenido": "Describe cómo la actividad humana ha alterado el ciclo del nitrógeno y el ciclo del carbono. ¿Qué consecuencias tiene?"},
            {"titulo": "77. Los efectos del cambio climático", "contenido": "Explica tres impactos del cambio climático global (ej. acidificación de los océanos, deshielo de glaciares, eventos climáticos extremos)."},
            {"titulo": "78. El efecto invernadero y sus gases", "contenido": "Diferencia entre el efecto invernadero natural y el potenciado. Nombra tres gases de efecto invernadero y sus fuentes."},
            {"titulo": "79. Biomasa y bioenergía", "contenido": "Explica qué es la biomasa como fuente de energía. ¿Qué ventajas y desventajas tiene su uso?"},
            {"titulo": "80. Gestión de recursos hídricos", "contenido": "Describe el concepto de huella hídrica y por qué es importante para la sostenibilidad de la producción y el consumo."},
            {"titulo": "81. La capa de ozono estratosférico", "contenido": "Explica el mecanismo de destrucción de la capa de ozono por los CFCs y los logros del Protocolo de Montreal."},
            {"titulo": "82. Contaminación del aire en ciudades", "contenido": "Describe la formación del smog fotoquímico. ¿Qué contaminantes lo provocan y qué efectos tiene en la salud?"},
            {"titulo": "83. La energía nuclear y sus residuos", "contenido": "Explica los desafíos de la gestión de residuos radiactivos. ¿Qué opciones se están explorando para su almacenamiento?"},
            {"titulo": "84. La formación de estrellas y planetas", "contenido": "Describe la secuencia de formación de una estrella y un sistema planetario a partir de una nebulosa."},
            {"titulo": "85. La muerte de una estrella", "contenido": "Diferencia entre el final de una estrella de baja masa (como el Sol) y una de alta masa. ¿Qué es una enana blanca y una estrella de neutrones?"},
            {"titulo": "86. Las galaxias y la materia oscura", "contenido": "Explica la evidencia que sugiere la existencia de la materia oscura. ¿Qué es un lente gravitacional?"},
            {"titulo": "87. Expansión del universo y la energía oscura", "contenido": "Describe la evidencia de la expansión acelerada del universo. ¿Qué es la energía oscura y por qué se postula su existencia?"},
            {"titulo": "88. La astrobiología y la vida extraterrestre", "contenido": "Explica la Ecuación de Drake y sus variables. ¿Cómo se relaciona con el estudio de la vida en otros planetas?"},
            {"titulo": "89. El cambio climático y la agricultura", "contenido": "Describe cómo el cambio climático afecta la producción agrícola y las estrategias de adaptación necesarias."},
            {"titulo": "90. La erosión y desertificación", "contenido": "Explica la diferencia entre la erosión del suelo y la desertificación. ¿Qué medidas se pueden tomar para mitigar este problema?"},
            {"titulo": "91. Zonas de subducción y geología", "contenido": "Describe el proceso de subducción de placas tectónicas y los fenómenos geológicos asociados (ej. volcanes, sismos, formación de cadenas montañosas)."},
            {"titulo": "92. Especies indicadoras y bioindicadores", "contenido": "Define especie indicadora o bioindicador. Da un ejemplo de un bioindicador de la calidad del aire o del agua."},
            {"titulo": "93. Contaminación del agua por eutrofización", "contenido": "Explica el proceso de eutrofización. ¿Qué contaminantes lo causan y qué efectos tiene en un ecosistema acuático?"},
            {"titulo": "94. La termodinámica de la Tierra", "contenido": "Describe el balance energético de la Tierra. ¿Cómo afecta la reflectividad (albedo) de la superficie al clima global?"},
            {"titulo": "95. El impacto de la minería", "contenido": "Menciona tres impactos ambientales de la minería a cielo abierto. ¿Qué es la lixiviación ácida?"},
            {"titulo": "96. Las extinciones masivas", "contenido": "Nombra dos extinciones masivas en la historia de la Tierra y describe una de sus posibles causas."},
            {"titulo": "97. Misiones espaciales y exploración de Marte", "contenido": "Describe los objetivos científicos de las misiones recientes a Marte (ej. Perseverance, Curiosity)."},
            {"titulo": "98. La gestión sostenible de los bosques", "contenido": "Explica qué es la silvicultura sostenible y qué beneficios tiene para el medio ambiente y la economía."},
            {"titulo": "99. La contaminación lumínica y acústica", "contenido": "Explica el impacto de la contaminación lumínica en los ecosistemas nocturnos y de la contaminación acústica en la fauna."},
            {"titulo": "100. El principio antrópico", "contenido": "Describe el principio antrópico débil y el principio antrópico fuerte. ¿Qué implicaciones filosóficas tienen para la astrofísica?"},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales (11° Grado)", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=(0, 15))

        # Contador de ejercicios
        self.counter_label = ttk.Label(main_frame, text="", font=("Helvetica", 14))
        self.counter_label.pack(pady=(0, 10))

        # Marco para el contenido del ejercicio
        exercise_frame = ttk.Frame(main_frame, padding="15", relief="solid", borderwidth=1, style="TFrame")
        exercise_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Título del ejercicio
        self.exercise_title_label = ttk.Label(exercise_frame, text="", font=("Helvetica", 16, "bold"), wraplength=800, anchor="w", justify="left")
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
        edit_window = Toplevel(self.root)
        edit_window.title("Revisar y Editar")
        edit_window.geometry("600x500")
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
        filename = "respuestas_ciencias_naturales_undecimo_grado_tkinter.txt"
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
