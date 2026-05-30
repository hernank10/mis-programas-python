# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (7° Grado)
# 100 EJERCICIOS PARA CIENCIAS NATURALES
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de séptimo grado, con ejercicios
# sobre biología (genética, tejidos), química (átomos, reacciones), física (fuerzas,
# energía) y ciencias de la Tierra (geología, tectónica).
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
        self.root.title("Ejercicios de Ciencias Naturales (7° Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para séptimo grado de ciencias naturales
        self.ejercicios = [
            # SECCIÓN 1: BIOLOGÍA - GENÉTICA Y TEJIDOS (25 EJERCICIOS)
            {"titulo": "1. Estructura de la célula eucariota", "contenido": "Describe las funciones del núcleo, el citoplasma y los organelos principales (mitocondria, cloroplasto, ribosomas)."},
            {"titulo": "2. Mitosis y el ciclo celular", "contenido": "Explica el proceso de la mitosis y su importancia para el crecimiento y la reparación de tejidos en los organismos. Nombra las fases principales."},
            {"titulo": "3. Meiosis y la reproducción sexual", "contenido": "Describe el proceso de la meiosis. ¿Qué diferencia principal tiene con la mitosis y por qué es crucial para la diversidad genética?"},
            {"titulo": "4. ADN, genes y cromosomas", "contenido": "Explica la relación entre ADN, genes y cromosomas. ¿Cuál es la función del ADN en los seres vivos?"},
            {"titulo": "5. Genética mendeliana", "contenido": "Define los conceptos de alelo dominante y recesivo. Explica con un ejemplo cómo se transmiten los rasgos según las leyes de Mendel."},
            {"titulo": "6. Genotipo y fenotipo", "contenido": "Diferencia entre genotipo y fenotipo. Proporciona un ejemplo para ilustrar ambos conceptos."},
            {"titulo": "7. Biotecnología y sus aplicaciones", "contenido": "Menciona dos aplicaciones de la biotecnología moderna (ej. ingeniería genética, clonación) y describe una de ellas."},
            {"titulo": "8. Los cinco reinos de los seres vivos", "contenido": "Nombra los cinco reinos (Monera, Protista, Fungi, Plantae, Animalia) y da un ejemplo de un organismo de cada reino."},
            {"titulo": "9. Células procariotas", "contenido": "¿Cuáles son las características distintivas de una célula procariota? ¿Qué tipo de organismos las tienen?"},
            {"titulo": "10. Tejidos animales", "contenido": "Nombra los cuatro tipos principales de tejidos animales (epitelial, conectivo, muscular, nervioso) y describe la función de uno de ellos."},
            {"titulo": "11. Tejidos vegetales", "contenido": "Nombra los tejidos vegetales principales (meristemático, dérmico, fundamental, vascular) y explica el papel del xilema y el floema."},
            {"titulo": "12. Los sistemas del cuerpo humano", "contenido": "Menciona tres sistemas del cuerpo humano (ej. circulatorio, respiratorio, digestivo) y describe el papel de cada uno."},
            {"titulo": "13. La nutrición en los seres vivos", "contenido": "Diferencia entre nutrición autótrofa y heterótrofa. Da un ejemplo de un organismo autótrofo y uno heterótrofo."},
            {"titulo": "14. La evolución de los organismos", "contenido": "Explica la teoría de la selección natural de Charles Darwin y su papel en la evolución de las especies."},
            {"titulo": "15. Evidencias de la evolución", "contenido": "Menciona tres tipos de evidencia que apoyan la teoría de la evolución (ej. fósiles, anatomía comparada, bioquímica)."},
            {"titulo": "16. La reproducción sexual en plantas", "contenido": "Describe el proceso de la polinización y la fecundación en una planta con flores. ¿Qué es la semilla?"},
            {"titulo": "17. Clasificación de los animales (vertebrados)", "contenido": "Menciona las cinco clases de vertebrados (mamíferos, aves, reptiles, anfibios, peces) y da un ejemplo de una especie en peligro de extinción en cada clase."},
            {"titulo": "18. Relaciones intraespecíficas e interespecíficas", "contenido": "Diferencia entre una relación intraespecífica y una interespecífica en un ecosistema. Da un ejemplo de cada una."},
            {"titulo": "19. Los ciclos biogeoquímicos", "contenido": "Explica brevemente el ciclo del agua o el ciclo del carbono, detallando las etapas y su importancia."},
            {"titulo": "20. Virus y su mecanismo de acción", "contenido": "¿Qué es un virus y cómo se replica en una célula huésped? ¿Por qué son tan difíciles de tratar?"},
            {"titulo": "21. El sistema endocrino humano", "contenido": "Describe la función del sistema endocrino. Nombra dos glándulas y las hormonas que producen (ej. páncreas-insulina, tiroides-tiroxina)."},
            {"titulo": "22. El sistema circulatorio doble y completo", "contenido": "Explica la diferencia entre circulación mayor y menor en el sistema circulatorio humano."},
            {"titulo": "23. La genética y la medicina", "contenido": "Menciona una enfermedad genética (ej. fibrosis quística, síndrome de Down) y explica cómo la genética ayuda a entenderla."},
            {"titulo": "24. El cerebro humano", "contenido": "Nombra las principales partes del cerebro (ej. cerebelo, cerebro, bulbo raquídeo) y describe la función del cerebelo."},
            {"titulo": "25. Homeostasis", "contenido": "Define homeostasis y da un ejemplo de cómo el cuerpo humano mantiene su equilibrio interno (ej. regulación de la temperatura)."},

            # SECCIÓN 2: QUÍMICA - LA MATERIA Y SUS TRANSFORMACIONES (25 EJERCICIOS)
            {"titulo": "26. Los modelos atómicos", "contenido": "Describe el modelo atómico de Bohr y cómo representa un átomo con sus electrones, protones y neutrones."},
            {"titulo": "27. Partículas subatómicas", "contenido": "Nombra las tres partículas subatómicas fundamentales y describe sus cargas eléctricas y sus ubicaciones en el átomo."},
            {"titulo": "28. Elementos, compuestos y mezclas", "contenido": "Diferencia entre un elemento, un compuesto y una mezcla. Da un ejemplo de cada uno."},
            {"titulo": "29. La tabla periódica de los elementos", "contenido": "¿Cómo está organizada la tabla periódica? ¿Qué información se puede obtener de la posición de un elemento?"},
            {"titulo": "30. Los iones y los isotopos", "contenido": "Diferencia entre un ion y un isótopo. Da un ejemplo de cada uno."},
            {"titulo": "31. Enlaces químicos", "contenido": "Describe brevemente el enlace iónico y el enlace covalente, y menciona un ejemplo de un compuesto con cada tipo de enlace."},
            {"titulo": "32. Reacciones químicas", "contenido": "Explica qué es una reacción química. ¿Cuáles son los reactivos y los productos en una reacción?"},
            {"titulo": "33. Ecuaciones químicas", "contenido": "Balancea la siguiente ecuación química: $CH_4 + O_2 -> CO_2 + H_2O$."},
            {"titulo": "34. Mezclas homogéneas y heterogéneas", "contenido": "Proporciona dos ejemplos de la vida diaria de una mezcla homogénea y una heterogénea."},
            {"titulo": "35. Soluciones: soluto y solvente", "contenido": "Define qué es un soluto y un solvente. Da un ejemplo de una solución y nombra su soluto y solvente."},
            {"titulo": "36. Cambios físicos y químicos", "contenido": "Diferencia entre un cambio físico y un cambio químico de la materia. Da un ejemplo de cada uno."},
            {"titulo": "37. La ley de conservación de la masa", "contenido": "Explica en qué consiste la ley de conservación de la masa de Lavoisier. ¿Qué implica para las reacciones químicas?"},
            {"titulo": "38. Estados de la materia y la teoría cinético-molecular", "contenido": "Usa la teoría cinético-molecular para explicar por qué los gases son fácilmente comprimibles."},
            {"titulo": "39. Oxidación y reducción", "contenido": "Define los procesos de oxidación y reducción. ¿Qué es un agente oxidante y un agente reductor?"},
            {"titulo": "40. Ácidos y bases", "contenido": "Diferencia entre un ácido y una base en términos de su pH. ¿Qué valor de pH es neutro?"},
            {"titulo": "41. La combustión", "contenido": "Describe las condiciones necesarias para que ocurra una reacción de combustión. ¿Qué productos se forman comúnmente?"},
            {"titulo": "42. Reacciones de síntesis y descomposición", "contenido": "Diferencia entre una reacción de síntesis y una de descomposición. Da un ejemplo de cada una."},
            {"titulo": "43. La radioactividad", "contenido": "Explica qué es la radioactividad y menciona dos aplicaciones de las sustancias radioactivas."},
            {"titulo": "44. La química en la industria", "contenido": "Menciona un producto industrial que se obtenga a través de una reacción química y describe su proceso de fabricación."},
            {"titulo": "45. La solubilidad", "contenido": "Define la solubilidad de una sustancia. ¿Qué factores afectan la solubilidad de un soluto en un solvente?"},
            {"titulo": "46. La teoría del octeto", "contenido": "Explica la teoría del octeto. ¿Por qué es importante para la formación de enlaces químicos?"},
            {"titulo": "47. La electrólisis", "contenido": "Describe el proceso de electrólisis y menciona una de sus aplicaciones prácticas."},
            {"titulo": "48. Reacciones endotérmicas y exotérmicas", "contenido": "Diferencia entre una reacción endotérmica y una exotérmica. Da un ejemplo de cada una."},
            {"titulo": "49. Los gases nobles", "contenido": "Menciona las características de los gases nobles y explica por qué son tan poco reactivos."},
            {"titulo": "50. Química orgánica e inorgánica", "contenido": "Diferencia entre la química orgánica e inorgánica. Da un ejemplo de una sustancia orgánica y una inorgánica."},

            # SECCIÓN 3: FÍSICA - FUERZAS Y ENERGÍA (25 EJERCICIOS)
            {"titulo": "51. Leyes de Newton del movimiento", "contenido": "Explica la primera y la tercera ley de Newton. Da un ejemplo de cada una."},
            {"titulo": "52. Fuerza y masa", "contenido": "¿Cuál es la relación entre la fuerza, la masa y la aceleración? Escribe la fórmula de la segunda ley de Newton."},
            {"titulo": "53. Tipos de energía", "contenido": "Diferencia entre energía cinética y energía potencial. Da un ejemplo de un objeto con cada tipo de energía."},
            {"titulo": "54. Conservación de la energía", "contenido": "Explica la ley de la conservación de la energía. ¿Qué significa que la energía no se crea ni se destruye?"},
            {"titulo": "55. Trabajo, potencia y energía", "contenido": "Define trabajo, potencia y energía. ¿Cuál es la unidad de medida del trabajo en el Sistema Internacional?"},
            {"titulo": "56. El sonido como onda", "contenido": "Describe qué es el sonido y cómo se propaga. ¿Qué características del sonido definen su tono y su volumen?"},
            {"titulo": "57. La luz y sus propiedades", "contenido": "Explica la reflexión y la refracción de la luz. ¿Cuál es la diferencia entre un espejo y un lente?"},
            {"titulo": "58. El espectro electromagnético", "contenido": "Nombra al menos tres tipos de ondas electromagnéticas además de la luz visible (ej. radio, microondas, rayos X)."},
            {"titulo": "59. Corriente eléctrica", "contenido": "Define qué es la corriente eléctrica y cómo se mide. ¿Cuál es la diferencia entre corriente continua y alterna?"},
            {"titulo": "60. Circuitos en serie y en paralelo", "contenido": "Diferencia entre un circuito en serie y un circuito en paralelo. ¿Qué sucede si se rompe un componente en cada tipo de circuito?"},
            {"titulo": "61. El magnetismo y el electromagnetismo", "contenido": "Explica la relación entre la electricidad y el magnetismo. ¿Qué es un electroimán?"},
            {"titulo": "62. Máquinas simples", "contenido": "Nombra cinco máquinas simples (palanca, polea, plano inclinado, rueda y eje, tornillo) y explica cómo funciona una de ellas."},
            {"titulo": "63. El principio de Pascal", "contenido": "Describe el principio de Pascal. ¿Cómo se aplica en un sistema hidráulico, como los frenos de un auto?"},
            {"titulo": "64. Presión atmosférica", "contenido": "Define la presión atmosférica y explica por qué un barómetro se usa para medirla."},
            {"titulo": "65. Calor y temperatura", "contenido": "Explica el concepto de calor latente de fusión y de vaporización. ¿Qué es el calor específico?"},
            {"titulo": "66. Transmisión del calor", "contenido": "Diferencia entre los tres mecanismos de transmisión de calor: conducción, convección y radiación. Da un ejemplo de cada uno."},
            {"titulo": "67. Ondas sísmicas", "contenido": "Describe los tipos de ondas sísmicas (ondas P, ondas S, ondas superficiales) y cómo se usan para estudiar el interior de la Tierra."},
            {"titulo": "68. Energía nuclear", "contenido": "Explica qué es la fisión y la fusión nuclear. ¿Cuál de ellas se utiliza en las centrales nucleares actuales?"},
            {"titulo": "69. El movimiento rectilíneo uniforme", "contenido": "Describe el movimiento rectilíneo uniforme (MRU). ¿Cuál es la fórmula para calcular la distancia en este tipo de movimiento?"},
            {"titulo": "70. La energía renovable", "contenido": "Menciona tres tipos de energía renovable (solar, eólica, geotérmica) y los beneficios de usarlas."},
            {"titulo": "71. Densidad y flotabilidad", "contenido": "Explica la densidad de un objeto. ¿Cómo se relaciona la densidad con el principio de Arquímedes y la flotabilidad?"},
            {"titulo": "72. La velocidad del sonido y de la luz", "contenido": "Compara la velocidad del sonido y de la luz. ¿Por qué vemos un relámpago antes de oír el trueno?"},
            {"titulo": "73. Frecuencia y longitud de onda", "contenido": "Define frecuencia y longitud de onda en el contexto de una onda. ¿Cómo se relacionan?"},
            {"titulo": "74. Efecto Doppler", "contenido": "Explica el efecto Doppler y da un ejemplo de cómo lo experimentamos en la vida diaria."},
            {"titulo": "75. La óptica y los instrumentos ópticos", "contenido": "Nombra dos instrumentos ópticos (ej. microscopio, telescopio, lupa) y explica su función."},

            # SECCIÓN 4: CIENCIAS DE LA TIERRA Y EL UNIVERSO (25 EJERCICIOS)
            {"titulo": "76. La teoría de la tectónica de placas", "contenido": "Explica la teoría de la tectónica de placas. ¿Qué fenómenos geológicos se explican con esta teoría?"},
            {"titulo": "77. Los tipos de límites de placas", "contenido": "Diferencia entre los límites de placas convergentes, divergentes y transformantes. Da un ejemplo de cada uno."},
            {"titulo": "78. La geología y los minerales", "contenido": "Define qué es un mineral y una roca. Nombra los tres tipos de rocas (ígneas, sedimentarias, metamórficas) y su proceso de formación."},
            {"titulo": "79. La hidrosfera", "contenido": "Describe las principales características de la hidrosfera. ¿Qué porcentaje del agua de la Tierra es dulce y disponible para consumo?"},
            {"titulo": "80. Las capas de la atmósfera", "contenido": "Nombra las capas de la atmósfera terrestre (troposfera, estratosfera, etc.). ¿En cuál de ellas se encuentra la capa de ozono?"},
            {"titulo": "81. El efecto invernadero y el cambio climático", "contenido": "Explica la diferencia entre el efecto invernadero natural y el provocado por el ser humano. ¿Cómo se relaciona con el cambio climático?"},
            {"titulo": "82. Contaminación del suelo", "contenido": "Menciona tres causas de la contaminación del suelo y tres efectos negativos que tiene en los ecosistemas."},
            {"titulo": "83. Los recursos naturales renovables y no renovables", "contenido": "Explica con ejemplos la diferencia entre un recurso natural renovable y uno no renovable."},
            {"titulo": "84. El sistema solar y sus planetas", "contenido": "Nombra los ocho planetas del sistema solar en orden y clasifícalos en planetas interiores y exteriores."},
            {"titulo": "85. La formación del Universo: la teoría del Big Bang", "contenido": "Explica brevemente la teoría del Big Bang y las evidencias que la apoyan (ej. expansión del universo, radiación de fondo)."},
            {"titulo": "86. Las galaxias", "contenido": "Define qué es una galaxia. Nombra los tres tipos de galaxias y la galaxia en la que se encuentra la Tierra."},
            {"titulo": "87. Estrellas, nebulosas y agujeros negros", "contenido": "Diferencia entre una estrella, una nebulosa y un agujero negro. Explica cómo se forma una estrella."},
            {"titulo": "88. La escala de magnitud sísmica", "contenido": "¿Cómo se mide la intensidad de un terremoto? Explica la escala de Richter o la de magnitud de momento."},
            {"titulo": "89. Las estaciones del año y la inclinación de la Tierra", "contenido": "Explica cómo la inclinación del eje de la Tierra provoca las estaciones del año y las diferencias de temperatura."},
            {"titulo": "90. El ciclo de las rocas", "contenido": "Describe el ciclo de las rocas. ¿Cómo se forma una roca sedimentaria a partir de una ígnea?"},
            {"titulo": "91. La meteorología", "contenido": "Nombra tres instrumentos que usan los meteorólogos para medir las condiciones atmosféricas (ej. termómetro, anemómetro, pluviómetro)."},
            {"titulo": "92. Las corrientes oceánicas", "contenido": "Explica qué son las corrientes oceánicas y su importancia en la regulación del clima global."},
            {"titulo": "93. El ciclo del fósforo", "contenido": "Describe los pasos del ciclo del fósforo. ¿Por qué no tiene una fase atmosférica importante como el ciclo del carbono?"},
            {"titulo": "94. La vida extraterrestre", "contenido": "Discute los argumentos científicos a favor y en contra de la existencia de vida extraterrestre. ¿Qué es la zona habitable?"},
            {"titulo": "95. El Cinturón de Asteroides y el Cinturón de Kuiper", "contenido": "Diferencia entre el Cinturón de Asteroides y el Cinturón de Kuiper en nuestro sistema solar."},
            {"titulo": "96. La exploración espacial: sondas y satélites", "contenido": "Menciona una sonda espacial famosa (ej. Voyager, Cassini) y describe los descubrimientos que realizó."},
            {"titulo": "97. El magnetismo terrestre", "contenido": "Explica por qué la Tierra tiene un campo magnético y su importancia para protegernos de las partículas solares."},
            {"titulo": "98. La erosión y la sedimentación", "contenido": "Define los procesos de erosión y sedimentación. ¿Qué agentes naturales causan la erosión?"},
            {"titulo": "99. El uso de recursos energéticos", "contenido": "Compara las ventajas y desventajas de la energía hidroeléctrica y la energía térmica."},
            {"titulo": "100. El efecto de los fenómenos astronómicos en la Tierra", "contenido": "Explica la relación entre la Luna y las mareas. ¿Qué es un eclipse?"},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales (7° Grado)", font=("Helvetica", 20, "bold"))
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
        filename = "respuestas_ciencias_naturales_septimo_grado_tkinter.txt"
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
