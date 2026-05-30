# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER (6° Grado)
# 100 EJERCICIOS PARA CIENCIAS NATURALES
# ==============================================================================
# Esta aplicación está diseñada para estudiantes de sexto grado, con ejercicios
# sobre biología (células, ecosistemas), física (energía, fuerzas), química (materia)
# y ciencias de la Tierra (ciclo del agua, sistema solar).
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
        self.root.title("Ejercicios de Ciencias Naturales (6° Grado)")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f0f0")

        # Lista de 100 ejercicios para sexto grado de ciencias naturales
        self.ejercicios = [
            # SECCIÓN 1: BIOLOGÍA - LOS SERES VIVOS (25 EJERCICIOS)
            {"titulo": "1. La célula, unidad básica de la vida", "contenido": "Describe qué es una célula, menciona sus partes principales y explica la diferencia entre una célula animal y una vegetal."},
            {"titulo": "2. Ecosistemas y sus componentes", "contenido": "Define qué es un ecosistema. ¿Cuáles son los dos tipos de componentes que lo forman? Menciona un ejemplo de cada uno."},
            {"titulo": "3. Cadena alimenticia o trófica", "contenido": "Explica qué es una cadena alimenticia y los roles de productor, consumidor y descomponedor. Dibuja un ejemplo simple."},
            {"titulo": "4. Clasificación de los animales", "contenido": "Menciona las principales clasificaciones de los animales (mamíferos, aves, reptiles, anfibios, peces) y da una característica de cada uno."},
            {"titulo": "5. El ciclo de vida de las plantas", "contenido": "Describe el proceso de germinación y crecimiento de una planta, desde la semilla hasta que produce flores y frutos."},
            {"titulo": "6. La fotosíntesis en las plantas", "contenido": "¿Qué es la fotosíntesis y por qué es fundamental para la vida en la Tierra? Explica los elementos que la planta necesita."},
            {"titulo": "7. Reinos de la naturaleza", "contenido": "Menciona los cinco reinos en los que se clasifican los seres vivos (Monera, Protista, Fungi, Plantae, Animalia) y describe brevemente uno de ellos."},
            {"titulo": "8. Biodiversidad y su importancia", "contenido": "Define qué es la biodiversidad. ¿Por qué es importante para el planeta? Menciona una amenaza para la biodiversidad."},
            {"titulo": "9. Adaptación de los seres vivos", "contenido": "Explica qué es la adaptación de los seres vivos a su entorno. Menciona una adaptación de un animal para sobrevivir en el desierto."},
            {"titulo": "10. La reproducción de los animales", "contenido": "Diferencia entre la reproducción sexual y la reproducción asexual en los animales. Menciona un ejemplo de cada tipo."},
            {"titulo": "11. Tipos de células: procariotas y eucariotas", "contenido": "Describe las características principales de las células procariotas y eucariotas. ¿A qué tipo de células pertenecen las plantas y los animales?"},
            {"titulo": "12. La respiración celular", "contenido": "Explica el proceso de la respiración celular, dónde ocurre y por qué es importante para obtener energía."},
            {"titulo": "13. La herencia genética", "contenido": "¿Qué es la herencia genética? Explica cómo los rasgos se transmiten de padres a hijos usando los conceptos de genes y ADN."},
            {"titulo": "14. Los virus y las bacterias", "contenido": "Diferencia entre virus y bacterias. ¿Cuál de los dos se considera un ser vivo? ¿Por qué?"},
            {"titulo": "15. Los hongos y sus funciones", "contenido": "Menciona las características principales de los hongos. ¿Cuál es su papel en un ecosistema? Da un ejemplo."},
            {"titulo": "16. El ciclo del carbono", "contenido": "Describe el ciclo del carbono y cómo la fotosíntesis y la respiración de los seres vivos influyen en este ciclo global."},
            {"titulo": "17. La polinización", "contenido": "Explica el proceso de la polinización y su importancia para las plantas y los ecosistemas. ¿Qué animales ayudan en la polinización?"},
            {"titulo": "18. Relaciones entre los seres vivos", "contenido": "Describe dos tipos de relaciones que se dan entre los seres vivos en un ecosistema (ej. depredación, simbiosis, mutualismo)."},
            {"titulo": "19. Animales vertebrados e invertebrados", "contenido": "Diferencia entre animales vertebrados e invertebrados. Menciona 3 ejemplos de cada uno."},
            {"titulo": "20. La conservación de los ecosistemas", "contenido": "Menciona tres acciones que podemos realizar para conservar los ecosistemas y proteger a los seres vivos que los habitan."},
            {"titulo": "21. Biomas terrestres", "contenido": "Nombra tres biomas terrestres (ej. selva, desierto, tundra) y describe el clima y la vegetación de uno de ellos."},
            {"titulo": "22. Animales de sangre fría y caliente", "contenido": "Explica la diferencia entre animales de sangre fría (poiquilotermos) y de sangre caliente (homeotermos). Da un ejemplo de cada uno."},
            {"titulo": "23. La evolución de las especies", "contenido": "Define la evolución y explica el papel de la selección natural en este proceso, según la teoría de Charles Darwin."},
            {"titulo": "24. Fósiles y evidencias de la evolución", "contenido": "Explica qué es un fósil y cómo su estudio ayuda a comprender la historia de la vida en la Tierra."},
            {"titulo": "25. La biodiversidad en tu región", "contenido": "Nombra tres especies de plantas o animales que sean nativas de tu región y explica por qué es importante protegerlas."},

            # SECCIÓN 2: BIOLOGÍA - EL CUERPO HUMANO Y LA SALUD (25 EJERCICIOS)
            {"titulo": "26. Sistema digestivo humano", "contenido": "Describe el recorrido de los alimentos a través del sistema digestivo, desde la boca hasta su eliminación. Nombra los órganos principales."},
            {"titulo": "27. Sistema respiratorio", "contenido": "Explica el proceso de la respiración. Describe el camino del aire a través del sistema respiratorio, nombrando los órganos principales."},
            {"titulo": "28. Sistema circulatorio", "contenido": "Describe la función del sistema circulatorio. Nombra sus tres componentes principales: el corazón, los vasos sanguíneos y la sangre."},
            {"titulo": "29. Nutrientes esenciales", "contenido": "Nombra los cinco grupos de nutrientes esenciales (carbohidratos, proteínas, grasas, vitaminas, minerales) y menciona una función de cada uno."},
            {"titulo": "30. La pirámide alimenticia", "contenido": "Explica cómo funciona la pirámide alimenticia y qué nos enseña sobre una dieta equilibrada. ¿Qué tipo de alimentos deben consumirse en menor cantidad?"},
            {"titulo": "31. El sistema nervioso", "contenido": "Describe la función principal del sistema nervioso. Explica la diferencia entre el sistema nervioso central y el periférico."},
            {"titulo": "32. El sistema óseo", "contenido": "Menciona tres funciones del sistema óseo. ¿Qué es una articulación? Nombra un ejemplo de articulación en tu cuerpo."},
            {"titulo": "33. El sistema muscular", "contenido": "Describe la función principal del sistema muscular. ¿Qué son los músculos voluntarios e involuntarios? Da un ejemplo de cada uno."},
            {"titulo": "34. Los órganos de los sentidos", "contenido": "Nombra los cinco sentidos y el órgano asociado a cada uno de ellos. Explica cómo funciona el sentido de la vista."},
            {"titulo": "35. La reproducción humana", "contenido": "Describe las principales etapas de la reproducción humana: la fecundación, el embarazo y el nacimiento."},
            {"titulo": "36. Higiene personal", "contenido": "Menciona tres hábitos de higiene personal que son importantes para mantener la salud y prevenir enfermedades."},
            {"titulo": "37. El sistema excretor", "contenido": "Describe la función del sistema excretor. Nombra los órganos principales (riñones, vejiga, etc.) y su papel."},
            {"titulo": "38. La salud mental", "contenido": "¿Por qué es importante cuidar la salud mental? Nombra dos actividades que te ayuden a sentirte bien emocionalmente."},
            {"titulo": "39. Enfermedades y prevención", "contenido": "Diferencia entre una enfermedad infecciosa y una no infecciosa. Da un ejemplo de cada una y una forma de prevenirlas."},
            {"titulo": "40. El sistema inmunitario", "contenido": "Explica qué es el sistema inmunitario y cómo nos protege de las enfermedades. ¿Qué son las vacunas?"},
            {"titulo": "41. La piel, el órgano más grande", "contenido": "Describe las funciones de la piel. ¿Por qué es importante protegerla del sol?"},
            {"titulo": "42. Los hábitos saludables", "contenido": "Menciona tres hábitos saludables (ej. ejercicio, dormir bien, comer sano) y explica por qué son importantes."},
            {"titulo": "43. La importancia del agua", "contenido": "¿Por qué es fundamental beber agua para el buen funcionamiento de tu cuerpo? ¿Cuántos vasos de agua se recomienda beber al día?"},
            {"titulo": "44. La visión y sus cuidados", "contenido": "Menciona tres cuidados que debes tener para proteger tus ojos y mantener una buena visión."},
            {"titulo": "45. La audición y sus cuidados", "contenido": "Explica cómo el sonido llega a nuestro cerebro. ¿Qué precauciones debemos tomar para cuidar nuestros oídos?"},
            {"titulo": "46. La higiene bucal", "contenido": "Menciona las partes de un diente y explica la importancia de cepillarse los dientes y usar hilo dental."},
            {"titulo": "47. Los grupos sanguíneos", "contenido": "Explica qué son los grupos sanguíneos y por qué es importante conocerlos en caso de una transfusión de sangre."},
            {"titulo": "48. La respiración y el deporte", "contenido": "Explica cómo la respiración cambia cuando hacemos deporte y cómo el ejercicio ayuda a fortalecer el sistema respiratorio."},
            {"titulo": "49. El corazón y el ejercicio", "contenido": "Explica cómo el ejercicio físico beneficia al corazón y al sistema circulatorio en general."},
            {"titulo": "50. Primeros auxilios básicos", "contenido": "Describe los pasos a seguir si alguien se hace una herida leve. ¿Cuándo debes buscar ayuda de un adulto o profesional?"},

            # SECCIÓN 3: FÍSICA Y QUÍMICA - MATERIA Y ENERGÍA (25 EJERCICIOS)
            {"titulo": "51. La materia y sus propiedades", "contenido": "Define qué es la materia. Menciona dos propiedades generales (masa, volumen) y dos propiedades específicas (densidad, dureza)."},
            {"titulo": "52. Los tres estados de la materia", "contenido": "Describe las características principales de los tres estados de la materia: sólido, líquido y gaseoso. Da un ejemplo de cada uno."},
            {"titulo": "53. Cambios de estado de la materia", "contenido": "Nombra y explica dos cambios de estado de la materia (ej. fusión, ebullición, solidificación)."},
            {"titulo": "54. Mezclas y soluciones", "contenido": "Diferencia entre una mezcla homogénea (solución) y una heterogénea. Da un ejemplo de cada una y explica por qué son diferentes."},
            {"titulo": "55. Métodos de separación de mezclas", "contenido": "Describe dos métodos para separar los componentes de una mezcla (ej. filtración, decantación, evaporación)."},
            {"titulo": "56. La energía y sus tipos", "contenido": "¿Qué es la energía? Nombra y describe brevemente dos tipos de energía (ej. cinética, potencial, eléctrica, solar)."},
            {"titulo": "57. Fuentes de energía renovable y no renovable", "contenido": "Diferencia entre fuentes de energía renovable y no renovable. Menciona dos ejemplos de cada una."},
            {"titulo": "58. Fuerzas y movimiento", "contenido": "Explica qué es una fuerza y cómo puede afectar el movimiento de un objeto. Da un ejemplo de una fuerza en tu vida diaria."},
            {"titulo": "59. La fuerza de gravedad", "contenido": "Describe la fuerza de gravedad y su efecto en los objetos en la Tierra. ¿Por qué la Luna no cae sobre la Tierra?"},
            {"titulo": "60. El magnetismo y los imanes", "contenido": "Explica qué es el magnetismo. ¿Qué son los polos de un imán y qué ocurre cuando se acercan dos polos iguales?"},
            {"titulo": "61. La electricidad y los circuitos", "contenido": "Define qué es un circuito eléctrico simple y nombra sus componentes principales (fuente de energía, conductor, interruptor, receptor)."},
            {"titulo": "62. Conductores y aislantes", "contenido": "Diferencia entre un material conductor y un aislante de electricidad. Da un ejemplo de cada uno y explica su función."},
            {"titulo": "63. La luz y la visión", "contenido": "Explica qué es la luz y cómo nos permite ver los objetos. ¿Qué diferencia hay entre un objeto transparente y uno opaco?"},
            {"titulo": "64. El sonido y la audición", "contenido": "Describe qué es el sonido y cómo se propaga. ¿Qué son las ondas sonoras?"},
            {"titulo": "65. La temperatura y el calor", "contenido": "Diferencia entre temperatura y calor. ¿Qué instrumento se usa para medir la temperatura?"},
            {"titulo": "66. La dilatación y la contracción térmica", "contenido": "Explica qué es la dilatación térmica. ¿Qué sucede con un metal cuando se calienta? Da un ejemplo en la vida real."},
            {"titulo": "67. La química en la cocina", "contenido": "Menciona un ejemplo de una reacción química que ocurre en la cocina y describe lo que sucede (ej. hornear un pastel)."},
            {"titulo": "68. El átomo, la partícula fundamental", "contenido": "Explica qué es un átomo. Nombra las tres partículas subatómicas principales (protón, neutrón, electrón)."},
            {"titulo": "69. Los elementos y la tabla periódica", "contenido": "Explica qué es un elemento químico. Nombra tres elementos que conozcas (ej. oxígeno, hidrógeno, hierro)."},
            {"titulo": "70. Compuestos químicos", "contenido": "¿Qué es un compuesto químico? Da un ejemplo de un compuesto y explica por qué es diferente a una mezcla."},
            {"titulo": "71. La presión atmosférica", "contenido": "Define la presión atmosférica y explica por qué no sentimos el peso del aire sobre nosotros."},
            {"titulo": "72. Las máquinas simples", "contenido": "Nombra tres máquinas simples (ej. palanca, polea, plano inclinado) y explica la función de una de ellas."},
            {"titulo": "73. La combustión", "contenido": "Describe qué es la combustión. ¿Qué elementos se necesitan para que ocurra una combustión?"},
            {"titulo": "74. La flotabilidad", "contenido": "Explica por qué algunos objetos flotan en el agua y otros se hunden. ¿Qué factor físico influye?"},
            {"titulo": "75. El sistema de poleas", "contenido": "Describe cómo funciona un sistema de poleas para levantar un objeto pesado. ¿Cuál es la ventaja de usar una polea?"},

            # SECCIÓN 4: CIENCIAS DE LA TIERRA Y EL ESPACIO (25 EJERCICIOS)
            {"titulo": "76. La estructura de la Tierra", "contenido": "Nombra las tres capas internas de la Tierra: corteza, manto y núcleo. Describe brevemente una de ellas."},
            {"titulo": "77. Los volcanes y los terremotos", "contenido": "Explica qué es un volcán y un terremoto. ¿Qué causa estos fenómenos naturales?"},
            {"titulo": "78. El ciclo del agua", "contenido": "Describe las etapas principales del ciclo del agua: evaporación, condensación, precipitación y recolección."},
            {"titulo": "79. El clima y el tiempo atmosférico", "contenido": "Diferencia entre clima y tiempo atmosférico. Menciona los factores que influyen en el clima de una región."},
            {"titulo": "80. Los planetas del sistema solar", "contenido": "Nombra los ocho planetas del sistema solar en orden, desde el más cercano al Sol hasta el más lejano."},
            {"titulo": "81. Movimientos de la Tierra", "contenido": "Describe los dos movimientos principales de la Tierra: rotación y traslación. ¿Qué provoca cada uno?"},
            {"titulo": "82. Las fases de la Luna", "contenido": "Explica por qué vemos diferentes fases de la Luna y nombra dos de ellas."},
            {"titulo": "83. La energía solar", "contenido": "Describe la importancia de la energía solar para la Tierra y cómo se puede aprovechar para generar electricidad."},
            {"titulo": "84. Las estaciones del año", "contenido": "Explica por qué existen las estaciones del año y cómo se relacionan con la inclinación del eje de la Tierra."},
            {"titulo": "85. Tipos de rocas", "contenido": "Nombra los tres tipos de rocas (ígneas, sedimentarias, metamórficas) y describe cómo se forma uno de ellos."},
            {"titulo": "86. Los minerales", "contenido": "Define qué es un mineral. Nombra dos minerales comunes y menciona una característica de cada uno."},
            {"titulo": "87. Los recursos naturales", "contenido": "Diferencia entre un recurso natural renovable y uno no renovable. Da un ejemplo de cada uno y explica su importancia."},
            {"titulo": "88. La contaminación del aire", "contenido": "Menciona tres causas de la contaminación del aire y tres efectos que tiene en el medio ambiente y la salud."},
            {"titulo": "89. El efecto invernadero", "contenido": "Explica qué es el efecto invernadero. ¿Por qué es un fenómeno natural y por qué su aumento es preocupante?"},
            {"titulo": "90. La capa de ozono", "contenido": "Describe qué es la capa de ozono y por qué es vital para la vida en la Tierra. ¿Qué productos la dañan?"},
            {"titulo": "91. La energía geotérmica", "contenido": "Explica qué es la energía geotérmica y cómo se aprovecha del calor interno de la Tierra."},
            {"titulo": "92. La atmósfera terrestre", "contenido": "Nombra las capas de la atmósfera terrestre y describe brevemente la función de la troposfera."},
            {"titulo": "93. La marea alta y baja", "contenido": "Explica qué causa las mareas en los océanos y cómo se relacionan con la gravedad de la Luna y el Sol."},
            {"titulo": "94. Eclipses solares y lunares", "contenido": "Diferencia entre un eclipse solar y un eclipse lunar. Dibuja un esquema sencillo de cada uno."},
            {"titulo": "95. La luna, el satélite natural", "contenido": "Menciona tres características de la Luna y explica por qué vemos siempre la misma cara de ella."},
            {"titulo": "96. Las estrellas y las galaxias", "contenido": "Define qué es una estrella y qué es una galaxia. ¿En qué galaxia se encuentra nuestro sistema solar?"},
            {"titulo": "97. El suelo y sus componentes", "contenido": "Describe los diferentes componentes del suelo (minerales, materia orgánica, agua, aire) y su importancia para las plantas."},
            {"titulo": "98. Los fenómenos meteorológicos", "contenido": "Nombra tres fenómenos meteorológicos (ej. lluvia, nieve, viento, huracanes) y explica cómo se forma uno de ellos."},
            {"titulo": "99. La exploración espacial", "contenido": "Menciona tres objetos o misiones que la humanidad ha enviado al espacio y describe qué descubrieron."},
            {"titulo": "100. Los minerales en la vida diaria", "contenido": "Nombra tres minerales que se utilizan en la vida diaria (ej. sal, cuarzo, grafito) y describe su uso."},
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
        title_label = ttk.Label(main_frame, text="Ejercicios de Ciencias Naturales (6° Grado)", font=("Helvetica", 20, "bold"))
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
        filename = "respuestas_ciencias_naturales_sexto_grado_tkinter.txt"
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
