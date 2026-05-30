# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (NIVEL UNIVERSITARIO)
# 100 EJERCICIOS PARA CIENCIAS NATURALES AVANZADAS
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de preuniversitario o primeros
# semestres universitarios, cubriendo temas de física cuántica, química orgánica
# avanzada, genética molecular y astrofísica.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, Text, Scrollbar, Toplevel
import os

class NaturalSciencesApp:
    """
    Clase principal que gestiona la interfaz de usuario y la lógica de la aplicación
    para 100 ejercicios de Ciencias Naturales a nivel universitario.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Ciencias Naturales (Nivel Universitario)")
        self.root.geometry("900x750")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para nivel universitario de ciencias naturales
        self.ejercicios = [
            # SECCIÓN 1: BIOLOGÍA AVANZADA Y GENÉTICA MOLECULAR (25 EJERCICIOS)
            {"titulo": "1. Mecánica de la transcripción y traducción", "contenido": "Describe el papel de los factores de transcripción, la ARN polimerasa y los ribosomas en la síntesis de proteínas. Explica la diferencia entre el promotor y el sitio de inicio."},
            {"titulo": "2. Regulación génica en eucariotas", "contenido": "Explica la regulación epigenética, el papel de la metilación del ADN y la acetilación de histonas en la expresión génica. ¿Cómo difiere de la regulación en procariotas?"},
            {"titulo": "3. Reparación del ADN", "contenido": "Describe los mecanismos de reparación por escisión de bases y escisión de nucleótidos. ¿Por qué es crucial para prevenir el cáncer?"},
            {"titulo": "4. CRISPR-Cas9 y edición genética", "contenido": "Explica el mecanismo de acción de la tecnología CRISPR-Cas9. ¿Cuáles son sus principales aplicaciones en biotecnología y medicina?"},
            {"titulo": "5. Inmunología: respuesta inmune celular y humoral", "contenido": "Diferencia entre la respuesta inmune mediada por células y la respuesta humoral. ¿Qué células están involucradas en cada una?"},
            {"titulo": "6. Neurobiología: el potencial de acción", "contenido": "Describe las fases del potencial de acción en una neurona (despolarización, repolarización, hiperpolarización) y el papel de los canales iónicos."},
            {"titulo": "7. Biotecnología: secuenciación de nueva generación (NGS)", "contenido": "Explica el principio de funcionamiento de la secuenciación de nueva generación (NGS) y su importancia en la genómica moderna."},
            {"titulo": "8. Células madre y medicina regenerativa", "contenido": "Diferencia entre células madre embrionarias, adultas y pluripotentes inducidas (iPS). ¿Qué potencial tienen en la medicina regenerativa?"},
            {"titulo": "9. Microbiología: biopelículas y resistencia bacteriana", "contenido": "Explica cómo se forman las biopelículas bacterianas y por qué confieren resistencia a los antibióticos."},
            {"titulo": "10. Virología: replicación viral", "contenido": "Describe el ciclo de vida de un retrovirus, como el VIH, con énfasis en la transcripción inversa y la integración del provirus."},
            {"titulo": "11. Biología del desarrollo: genes Hox", "contenido": "Explica la función de los genes Hox en la especificación del plan corporal de los animales. ¿Qué son los 'genes maestros'?"},
            {"titulo": "12. Ecología avanzada: modelos de dinámica de poblaciones", "contenido": "Describe el modelo de crecimiento logístico y el concepto de capacidad de carga ($K$). ¿Qué factores lo limitan en la realidad?"},
            {"titulo": "13. Biología del cáncer: oncogenes y genes supresores de tumores", "contenido": "Diferencia el papel de los oncogenes y los genes supresores de tumores en la carcinogénesis. Da un ejemplo de cada uno."},
            {"titulo": "14. Bioquímica de la fotosíntesis", "contenido": "Describe las fases luminosa y oscura de la fotosíntesis. Explica el papel del ATP y el NADPH."},
            {"titulo": "15. Fisiología renal: regulación del equilibrio ácido-base", "contenido": "Explica cómo los riñones regulan el pH sanguíneo mediante la reabsorción y secreción de iones de bicarbonato y hidrógeno."},
            {"titulo": "16. Transducción de señales celulares", "contenido": "Describe el proceso de transducción de señales mediado por receptores acoplados a proteínas G (GPCR)."},
            {"titulo": "17. Genómica y proteómica", "contenido": "Diferencia entre genómica y proteómica. Explica por qué el estudio del proteoma es más complejo que el del genoma."},
            {"titulo": "18. Evolución molecular: relojes moleculares", "contenido": "Explica el concepto de 'reloj molecular' y cómo se utiliza para estimar el tiempo de divergencia de especies."},
            {"titulo": "19. Mecanismos de la evolución: el papel del azar", "contenido": "Diferencia entre la deriva genética y la selección natural como fuerzas evolutivas. ¿En qué tipo de poblaciones es más influyente la deriva?"},
            {"titulo": "20. Fisiología vegetal: hormonas de crecimiento", "contenido": "Describe la función de las auxinas y las giberelinas en el crecimiento de las plantas. ¿Qué es el fototropismo?"},
            {"titulo": "21. Genética mendeliana avanzada: ligamiento genético", "contenido": "Explica qué es el ligamiento genético y cómo las frecuencias de recombinación se utilizan para construir mapas genéticos."},
            {"titulo": "22. Bioética: debates actuales", "contenido": "Analiza las implicaciones éticas y sociales de la edición de la línea germinal humana y la clonación reproductiva."},
            {"titulo": "23. Los microbiomas", "contenido": "Describe el concepto de microbioma humano. ¿Qué impacto tiene la composición del microbioma intestinal en la salud?"},
            {"titulo": "24. Citoesqueleto y motilidad celular", "contenido": "Explica la estructura y función de los microtúbulos, los filamentos de actina y los filamentos intermedios en la célula."},
            {"titulo": "25. Regulación del ciclo celular", "contenido": "Describe el papel de las ciclinas y las quinasas dependientes de ciclina (Cdks) en el control del ciclo celular. ¿Qué son los puntos de control?"},

            # SECCIÓN 2: QUÍMICA FÍSICA Y ORGÁNICA AVANZADA (25 EJERCICIOS)
            {"titulo": "26. Termodinámica química: energías libres", "contenido": "Calcula la variación de la energía libre de Gibbs de la siguiente reacción a 298 K: $2 H_2(g) + O_2(g) \to 2 H_2O(l)$, si $\Delta H^\circ = -571.6 kJ$ y $\Delta S^\circ = -326.7 J/K$."},
            {"titulo": "27. Equilibrio químico: el principio de Le Châtelier", "contenido": "Describe cómo el principio de Le Châtelier predice el efecto de los cambios de presión, temperatura y concentración en el equilibrio de una reacción."},
            {"titulo": "28. Cinética química: teoría de las colisiones", "contenido": "Explica la teoría de las colisiones. ¿Qué es la energía de activación y cómo afecta la velocidad de una reacción?"},
            {"titulo": "29. Electroquímica: la ecuación de Nernst", "contenido": "Describe la ecuación de Nernst. ¿Cómo se utiliza para calcular el potencial de una celda electroquímica en condiciones no estándar?"},
            {"titulo": "30. Síntesis orgánica: la reacción de Grignard", "contenido": "Describe la preparación de un reactivo de Grignard y su uso en la síntesis de alcoholes. ¿Por qué es una reacción tan versátil?"},
            {"titulo": "31. Espectroscopía: RMN", "contenido": "Explica el principio de la resonancia magnética nuclear (RMN) y cómo se utiliza para determinar la estructura de las moléculas orgánicas."},
            {"titulo": "32. Mecanismos de reacción: eliminación E1 y E2", "contenido": "Diferencia entre los mecanismos de eliminación E1 y E2. ¿Qué factores favorecen cada uno?"},
            {"titulo": "33. Química de coordinación: la teoría del campo cristalino", "contenido": "Explica la teoría del campo cristalino (TCC). ¿Cómo explica la estabilidad y el color de los complejos de metales de transición?"},
            {"titulo": "34. Química de polímeros: polimerización por etapas y en cadena", "contenido": "Diferencia entre los mecanismos de polimerización por etapas y en cadena. Da un ejemplo de cada tipo de polímero."},
            {"titulo": "35. Termodinámica estadística", "contenido": "Explica el significado de la entropía desde un punto de vista estadístico ($S = k_B \ln W$)."},
            {"titulo": "36. Enlaces químicos avanzados: la teoría del orbital molecular", "contenido": "Construye el diagrama de orbitales moleculares del $O_2$ y predice su orden de enlace y sus propiedades magnéticas."},
            {"titulo": "37. Cinética enzimática: inhibición", "contenido": "Describe y diferencia los tipos de inhibición enzimática (competitiva, no competitiva, acompetitiva) con ejemplos."},
            {"titulo": "38. Química de los materiales: superconductores", "contenido": "Explica el fenómeno de la superconductividad. ¿Qué es el efecto Meissner y cuál es la temperatura crítica?"},
            {"titulo": "39. Química ambiental: contaminantes orgánicos persistentes (POPs)", "contenido": "Describe qué son los POPs y por qué representan un riesgo ambiental significativo. Da un ejemplo de un POP."},
            {"titulo": "40. Reacciones orgánicas: la condensación aldólica", "contenido": "Describe el mecanismo de la condensación aldólica y su uso para formar enlaces C-C."},
            {"titulo": "41. Mecanismos de reacción: sustitución nucleofílica aromática", "contenido": "Explica el mecanismo de reacción de una sustitución nucleofílica aromática. ¿Qué sustituyentes favorecen esta reacción?"},
            {"titulo": "42. Espectroscopía de masas", "contenido": "Describe el principio de la espectroscopía de masas. ¿Cómo se interpreta el espectro para determinar la masa molecular de una sustancia?"},
            {"titulo": "43. Fisicoquímica de las superficies: la ecuación de Gibbs", "contenido": "Explica el concepto de tensión superficial y la relación con la ecuación de Gibbs. ¿Cómo se mide?"},
            {"titulo": "44. Química nuclear: decaimiento radiactivo", "contenido": "Describe los tipos de decaimiento radiactivo ($\alpha, \beta, \gamma$) y sus efectos en el núcleo atómico."},
            {"titulo": "45. Termoquímica: calores de formación y enlace", "contenido": "Explica cómo los calores de formación y los calores de enlace se pueden usar para calcular el $\Delta H^\circ$ de una reacción."},
            {"titulo": "46. Propiedades de los disolventes: solvólisis", "contenido": "Explica el concepto de solvólisis. ¿Cómo afecta la polaridad del disolvente a la velocidad de una reacción química?"},
            {"titulo": "47. Química organometálica", "contenido": "Describe la estructura y las aplicaciones de los catalizadores de Ziegler-Natta en la polimerización de olefinas."},
            {"titulo": "48. Química de la atmósfera: el agujero de ozono", "contenido": "Explica el mecanismo de destrucción catalítica del ozono por el cloro. ¿Cuál es la importancia del vórtice polar?"},
            {"titulo": "49. Bioquímica avanzada: la bioenergética celular", "contenido": "Describe la cadena de transporte de electrones y la fosforilación oxidativa. ¿Cuántas moléculas de ATP se producen por glucosa?"},
            {"titulo": "50. Química de los materiales: zeolitas y catalizadores", "contenido": "Explica la estructura y las propiedades de las zeolitas. ¿Qué aplicaciones tienen como catalizadores?"},
            
            # SECCIÓN 3: FÍSICA MODERNA Y ELECTRODINÁMICA (25 EJERCICIOS)
            {"titulo": "51. Ecuaciones de Maxwell", "contenido": "Enuncia las cuatro ecuaciones de Maxwell en su forma diferencial e integral y describe lo que representa cada una."},
            {"titulo": "52. Propagación de ondas electromagnéticas", "contenido": "Describe cómo las ecuaciones de Maxwell predicen la existencia de ondas electromagnéticas. ¿Cuál es su velocidad en el vacío?"},
            {"titulo": "53. La ecuación de Schrödinger", "contenido": "Explica el significado de la ecuación de Schrödinger independiente del tiempo ($\hat{H}\Psi = E\Psi$) y la interpretación de la función de onda $\Psi$."},
            {"titulo": "54. El pozo de potencial infinito", "contenido": "Resuelve la ecuación de Schrödinger para una partícula en un pozo de potencial infinito unidimensional. ¿Cómo se cuantiza la energía?"},
            {"titulo": "55. El efecto túnel", "contenido": "Explica el efecto túnel cuántico. ¿En qué dispositivos electrónicos o fenómenos naturales se manifiesta?"},
            {"titulo": "56. El espín electrónico", "contenido": "Describe el concepto de espín electrónico como una propiedad cuántica intrínseca. ¿Qué implicaciones tiene para el magnetismo?"},
            {"titulo": "57. Álgebra de tensores en relatividad", "contenido": "Explica brevemente el concepto de tensor en el contexto de la relatividad general. ¿Qué es el tensor de curvatura de Riemann?"},
            {"titulo": "58. Relatividad general: el principio de equivalencia", "contenido": "Enuncia el principio de equivalencia de Einstein. ¿Cómo se relaciona la gravedad con la geometría del espacio-tiempo?"},
            {"titulo": "59. Radiación de cuerpo negro", "contenido": "Describe las leyes de Planck, Wien y Stefan-Boltzmann para la radiación de un cuerpo negro. ¿Qué implica para la termodinámica de las estrellas?"},
            {"titulo": "60. Óptica: las ecuaciones de Fresnel", "contenido": "Describe las ecuaciones de Fresnel para la reflexión y refracción de la luz. ¿Qué es el ángulo de Brewster?"},
            {"titulo": "61. Electrodinámica: los potenciales de Liénard-Wiechert", "contenido": "Explica los potenciales de Liénard-Wiechert y por qué son necesarios para describir los campos generados por cargas en movimiento."},
            {"titulo": "62. Circuitos de corriente alterna: impedancia compleja", "contenido": "Describe el uso de la notación compleja (fasores) para analizar circuitos RLC de corriente alterna. ¿Qué es la impedancia?"},
            {"titulo": "63. Física nuclear: el modelo de la gota líquida", "contenido": "Explica el modelo de la gota líquida del núcleo atómico. ¿Cómo predice la energía de enlace de los núcleos?"},
            {"titulo": "64. Aceleradores de partículas", "contenido": "Describe el funcionamiento de un ciclotrón o un sincrotrón. ¿Para qué se utilizan en la física moderna?"},
            {"titulo": "65. La fuerza de Van der Waals", "contenido": "Describe las fuerzas de Van der Waals (dipolo-dipolo, dipolo-inducido, fuerzas de dispersión de London) y su origen molecular."},
            {"titulo": "66. Fenomenología de las partículas elementales", "contenido": "Describe las cuatro interacciones fundamentales de la naturaleza y los bosones mediadores de cada una."},
            {"titulo": "67. Físicomatemáticas: análisis de Fourier", "contenido": "Explica el concepto de la transformada de Fourier y su importancia en el análisis de señales y la mecánica cuántica."},
            {"titulo": "68. Física de la materia condensada: la teoría de bandas", "contenido": "Describe el origen de la estructura de bandas en los sólidos cristalinos. ¿Cómo diferencia a un conductor, un aislante y un semiconductor?"},
            {"titulo": "69. Termodinámica: las relaciones de Maxwell", "contenido": "Enuncia las relaciones de Maxwell para las variables termodinámicas. ¿Cómo se derivan y para qué sirven?"},
            {"titulo": "70. La paradoja de los gemelos", "contenido": "Explica en detalle la paradoja de los gemelos en la relatividad especial y cómo se resuelve."},
            {"titulo": "71. El tensor de energía-momento", "contenido": "Describe el papel del tensor de energía-momento en las ecuaciones de campo de la relatividad general."},
            {"titulo": "72. Astrofísica: el colapso gravitacional", "contenido": "Explica el proceso de colapso gravitacional de una estrella masiva y la formación de una estrella de neutrones o un agujero negro."},
            {"titulo": "73. Física de plasmas", "contenido": "Define qué es un plasma y describe el concepto de apantallamiento de Debye en un plasma."},
            {"titulo": "74. Láseres", "contenido": "Describe los tres procesos fundamentales del funcionamiento de un láser: absorción, emisión espontánea y emisión estimulada."},
            {"titulo": "75. Electrodinámica: la fuerza de radiación", "contenido": "Explica el concepto de fuerza de radiación y cómo se relaciona con la conservación del momento."},
            
            # SECCIÓN 4: ASTROFÍSICA, COSMOLOGÍA Y CIENCIAS DE LA TIERRA AVANZADAS (25 EJERCICIOS)
            {"titulo": "76. La expansión del universo y la Ley de Hubble", "contenido": "Enuncia la Ley de Hubble y explica cómo las mediciones de los corrimientos al rojo de las galaxias confirman la expansión del universo."},
            {"titulo": "77. La materia oscura y la energía oscura", "contenido": "Describe la evidencia observacional de la materia y la energía oscura. ¿Qué porcentaje del universo compone cada una?"},
            {"titulo": "78. Modelos cosmológicos", "contenido": "Diferencia entre los modelos cosmológicos del 'universo abierto', 'cerrado' y 'plano'. ¿Qué modelo actual es el más aceptado y por qué?"},
            {"titulo": "79. La radiación de fondo de microondas (CMB)", "contenido": "Explica qué es el CMB y por qué es considerada una de las pruebas más importantes del Big Bang."},
            {"titulo": "80. La nucleosíntesis estelar", "contenido": "Describe el proceso de fusión nuclear en las estrellas y cómo se forman los elementos más pesados, desde el helio hasta el hierro."},
            {"titulo": "80. La nucleosíntesis estelar", "contenido": "Describe el proceso de fusión nuclear en las estrellas y cómo se forman los elementos más pesados, desde el helio hasta el hierro."},
            {"titulo": "81. La formación del sistema solar", "contenido": "Describe la teoría de la nebulosa solar para la formación del sistema solar. ¿Cómo explica la distribución de planetas rocosos y gaseosos?"},
            {"titulo": "82. Geología: placas tectónicas y su dinámica", "contenido": "Explica los mecanismos que impulsan el movimiento de las placas tectónicas (ej. convección del manto, empuje de dorsal)."},
            {"titulo": "83. Climatología: los forzamientos climáticos", "contenido": "Diferencia entre forzamientos climáticos positivos y negativos. Da un ejemplo de cada uno (ej. gases de efecto invernadero, aerosoles)."},
            {"titulo": "84. Oceanografía: la circulación termohalina", "contenido": "Describe la circulación termohalina o 'cinta transportadora oceánica' y su importancia en la regulación del clima global."},
            {"titulo": "85. Paleoclimatología: registros climáticos", "contenido": "Menciona tres tipos de registros paleoclimáticos (ej. núcleos de hielo, anillos de árboles, sedimentos oceánicos) y qué tipo de información proveen."},
            {"titulo": "86. Bioquímica ambiental: la biodisponibilidad", "contenido": "Explica el concepto de biodisponibilidad de un contaminante. ¿Qué factores lo afectan en el suelo y el agua?"},
            {"titulo": "87. Astrofísica: agujeros negros", "contenido": "Describe la formación de agujeros negros. ¿Qué es el horizonte de sucesos y la singularidad?"},
            {"titulo": "88. La detección de exoplanetas", "contenido": "Describe los métodos de detección de exoplanetas por tránsito y por velocidad radial. ¿Qué información se obtiene de cada uno?"},
            {"titulo": "89. La geología estructural", "contenido": "Diferencia entre fallas normales, inversas y de desgarre. ¿Cómo se forman y qué tipo de esfuerzos están asociados a cada una?"},
            {"titulo": "90. La teoría de la biosfera", "contenido": "Describe el concepto de biosfera como un sistema. ¿Cómo interactúan los ciclos biogeoquímicos con los organismos vivos?"},
            {"titulo": "91. El cambio climático y los ciclos biogeoquímicos", "contenido": "Explica cómo el aumento del $CO_2$ atmosférico afecta la acidificación de los océanos y qué consecuencias tiene para la vida marina."},
            {"titulo": "92. Sismología: ondas sísmicas", "contenido": "Diferencia entre las ondas sísmicas P y S. ¿Cómo se utilizan para determinar la estructura interna de la Tierra?"},
            {"titulo": "93. Hidrología: el ciclo hidrológico avanzado", "contenido": "Describe el concepto de isótopos estables del agua y cómo se utilizan para trazar el movimiento del agua en el ciclo hidrológico."},
            {"titulo": "94. La física de la Tierra sólida: el geodínamo", "contenido": "Explica la teoría del geodínamo y cómo se genera el campo magnético de la Tierra."},
            {"titulo": "95. La habitabilidad planetaria", "contenido": "Define la 'zona de habitabilidad' de una estrella. ¿Qué otros factores son importantes para la habitabilidad de un planeta?"},
            {"titulo": "96. Cosmología: la inflación cósmica", "contenido": "Describe la teoría de la inflación cósmica. ¿Cómo resuelve los problemas del horizonte y la planitud del universo?"},
            {"titulo": "97. Química de los océanos: el ciclo del carbonato", "contenido": "Explica el ciclo del carbonato en los océanos y cómo la disolución de rocas de carbonato actúa como un amortiguador del pH."},
            {"titulo": "98. Vulcanología: tipos de erupciones", "contenido": "Diferencia entre una erupción volcánica efusiva y una explosiva. ¿Qué características del magma determinan el tipo de erupción?"},
            {"titulo": "99. Climatología: teleconexiones climáticas", "contenido": "Explica el fenómeno de El Niño-Oscilación del Sur (ENOS) y cómo afecta los patrones climáticos globales."},
            {"titulo": "100. Astrobiología: el origen de la vida en la Tierra", "contenido": "Describe la teoría de las 'fuentes hidrotermales profundas' como un posible origen de la vida en la Tierra. ¿Qué ventajas tiene sobre la teoría de la sopa primordial?"},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales (Nivel Universitario)", font=("Helvetica", 20, "bold"))
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
        filename = "respuestas_ciencias_naturales_universitario_tkinter.txt"
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
