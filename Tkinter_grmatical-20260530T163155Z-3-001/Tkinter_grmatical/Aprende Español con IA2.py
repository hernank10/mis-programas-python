import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import time
import os

# --- Simulación de la API de Google Gemini ---
# IMPORTANTE: En una aplicación real, NO HARÍAS ESTO.
# Tu API_KEY debería cargarse de forma segura (e.g., desde un archivo .env,
# un servicio de gestión de secretos, o una variable de entorno REAL)
# Por ahora, simplemente simulamos que se carga una clave.
# Si tuvieras una API Key REAL, la establecerías así:
# os.environ["GEMINI_API_KEY"] = "TU_VERDADERA_API_KEY_AQUI"
# import google.generativeai as genai
# genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

class SpanishLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprende Español con IA 🇪🇸🤖")
        self.root.geometry("1000x700")
        self.root.configure(bg="#ecf0f1")

        # --- Frames principales ---
        self.header_frame = tk.Frame(root, bg="#2c3e50", height=80)
        self.header_frame.pack(fill="x", side="top")

        self.main_content_frame = tk.Frame(root, bg="#ecf0f1")
        self.main_content_frame.pack(fill="both", expand=True, side="left")

        self.sidebar_frame = tk.Frame(root, bg="#bdc3c7", width=200)
        self.sidebar_frame.pack(fill="y", side="right")

        # --- Contenido del Header ---
        self.title_label = tk.Label(self.header_frame, text="✨ Tu Maestro de Español con Gemini ✨",
                                     font=("Arial", 24, "bold"), fg="white", bg="#2c3e50")
        self.title_label.pack(pady=15)

        # --- Contenido del Sidebar (Menú de Lecciones) ---
        self.create_lesson_menu()

        # --- Área de Contenido Principal (inicialmente vacía o con bienvenida) ---
        self.current_content_frame = tk.Frame(self.main_content_frame, bg="white", padx=20, pady=20)
        self.current_content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.show_welcome_screen()

        # --- Variables de estado de las Lecciones 4 y 5 ---
        self.lesson4_questions = []
        self.current_lesson4_question_index = 0
        self.lesson4_score = 0

        self.lesson5_questions = []
        self.current_lesson5_question_index = 0
        self.lesson5_score = 0

        # --- Simulación del modelo Gemini ---
        self.gemini_model_sim = self.SimulatedGeminiModel()

    def clear_content_frame(self):
        """Limpia el contenido del frame principal para cargar nueva lección/ejercicio."""
        for widget in self.current_content_frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_content_frame()
        welcome_text = tk.Label(self.current_content_frame, text="¡Hola! Selecciona una lección del menú o interactúa con Gemini.",
                                font=("Arial", 16), fg="#34495e", wraplength=500, justify="center", bg="white")
        welcome_text.pack(pady=50)

    def create_lesson_menu(self):
        """Crea los botones para las lecciones en el sidebar."""
        menu_title = tk.Label(self.sidebar_frame, text="Lecciones y IA", font=("Arial", 14, "bold"), bg="#bdc3c7", fg="#34495e")
        menu_title.pack(pady=10)

        lessons = [
            ("Introducción a la Ortografía 📚", self.load_lesson1),
            ("Acentuación ✨", self.load_lesson2),
            ("Transformación de Oraciones 🔄", self.load_lesson3),
            ("Redacción de Reglas (Huecos) ✍️", self.load_lesson4), # Lección 4
            ("Redacción de Reglas (Ejemplo) 🧠", self.load_lesson5), # Lección 5
            ("Tutorías con IA Gemini 🤖", self.load_ai_tutoring),
            ("Solicitar Nueva Lección IA 💡", self.load_ai_new_lesson),
            ("Asistencia para Crear Lecciones con IA 📝✨", self.load_ai_lesson_creation_assistant)
        ]

        for text, command in lessons:
            button = tk.Button(self.sidebar_frame, text=text, command=command,
                               font=("Arial", 12), bg="#3498db", fg="white",
                               relief="raised", bd=2, width=25, height=2)
            button.pack(pady=5, padx=10)
        
        # Botón de salir
        exit_button = tk.Button(self.sidebar_frame, text="Salir 🚶‍♂️", command=self.root.quit,
                                font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
                                relief="raised", bd=2, width=25, height=2)
        exit_button.pack(pady=20, padx=10)

    # --- Métodos para Cargar Lecciones (PLACEHOLDER) ---
    def load_lesson1(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Lección 1: Ortografía Básica ---", font=("Arial", 18, "bold"), bg="white").pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí iría la teoría y los ejercicios de la Lección 1.", wraplength=600, bg="white").pack()

    def load_lesson2(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Lección 2: Acentuación ---", font=("Arial", 18, "bold"), bg="white").pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí iría la teoría y los ejercicios de la Lección 2.", wraplength=600, bg="white").pack()

    def load_lesson3(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Lección 3: Transformación de Oraciones ---", font=("Arial", 18, "bold"), bg="white").pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí iría la teoría y los ejercicios de la Lección 3.", wraplength=600, bg="white").pack()

    # --- Implementación de la Lección 4 para Tkinter ---
    def load_lesson4(self):
        self.clear_content_frame()
        self.current_lesson4_question_index = 0
        self.lesson4_score = 0
        
        tk.Label(self.current_content_frame, text="--- Lección 4: Redacción de Reglas (Completar Huecos) ✍️ ---", 
                 font=("Arial", 18, "bold"), fg="#34495e", bg="white").pack(pady=10)
        
        theory_text = (
            "En esta lección, te enfocarás en la estructura de las reglas gramaticales.\n"
            "Se te presentarán frases incompletas que describen reglas y deberás completarlas con la palabra o frase correcta.\n\n"
            "¡Demuestra tu conocimiento y mejora tu puntuación!"
        )
        tk.Label(self.current_content_frame, text=theory_text, font=("Arial", 11), 
                 wraplength=600, justify="left", bg="white").pack(pady=10)

        start_button = tk.Button(self.current_content_frame, text="Iniciar Ejercicios de Lección 4 📝", 
                                 command=self.start_lesson4_exercises,
                                 font=("Arial", 14, "bold"), bg="#28a745", fg="white", relief="raised")
        start_button.pack(pady=20)

    def start_lesson4_exercises(self):
        self.clear_content_frame()
        
        self.lesson4_questions = [
            {"pregunta": "Las palabras agudas llevan tilde cuando terminan en vocal, en 'n' o en '___'.", "respuesta": "s"},
            {"pregunta": "Las palabras graves NO llevan tilde cuando terminan en vocal, en 'n' o en '___'.", "respuesta": "s"},
            {"pregunta": "Todas las palabras esdrújulas y sobresdrújulas llevan siempre ___.", "respuesta": "tilde"},
            {"pregunta": "Se usa tilde diacrítica para diferenciar palabras que se escriben igual pero tienen diferente ___ o función.", "respuesta": "significado"},
            {"pregunta": "En un hiato, si la vocal cerrada ('i', 'u') es tónica y está junto a una vocal abierta ('a', 'e', 'o'), la vocal cerrada siempre lleva ___.", "respuesta": "tilde"},
            {"pregunta": "Los monosílabos generalmente no llevan ___.", "respuesta": "tilde"}
        ]
        random.shuffle(self.lesson4_questions)
        self.current_lesson4_question_index = 0
        self.lesson4_score = 0
        self.display_lesson4_question()

    def display_lesson4_question(self):
        self.clear_content_frame()
        if self.current_lesson4_question_index < len(self.lesson4_questions):
            q = self.lesson4_questions[self.current_lesson4_question_index]

            tk.Label(self.current_content_frame, text=f"--- Pregunta {self.current_lesson4_question_index + 1} de {len(self.lesson4_questions)} ---",
                     font=("Arial", 16, "bold"), fg="#34495e", bg="white").pack(pady=10)
            
            tk.Label(self.current_content_frame, text=f"Completa la regla: {q['pregunta']}",
                     font=("Arial", 13, "italic"), fg="#555", wraplength=600, bg="white").pack(pady=5, anchor="w")
            
            tk.Label(self.current_content_frame, text="Tu respuesta:",
                     font=("Arial", 12, "bold"), bg="white").pack(pady=10, anchor="w")
            
            self.lesson4_answer_entry = tk.Entry(self.current_content_frame, width=50, font=("Arial", 12), bd=2, relief="groove")
            self.lesson4_answer_entry.pack(pady=5)

            # Frame para los botones de acción
            action_buttons_frame = tk.Frame(self.current_content_frame, bg="white")
            action_buttons_frame.pack(pady=10)

            check_button = tk.Button(action_buttons_frame, text="Verificar Respuesta ✅", 
                                     command=self.check_lesson4_answer,
                                     font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised")
            check_button.pack(side="left", padx=5)

            self.lesson4_feedback_label = tk.Label(self.current_content_frame, text="", font=("Arial", 12), wraplength=600, bg="white")
            self.lesson4_feedback_label.pack(pady=10)

            self.lesson4_score_label = tk.Label(self.current_content_frame, text=f"Puntuación: {self.lesson4_score} / {self.current_lesson4_question_index * 10}",
                                                 font=("Arial", 12, "bold"), fg="#3498db", bg="white")
            self.lesson4_score_label.pack(pady=5)

        else:
            self.show_lesson4_results()

    def check_lesson4_answer(self):
        q = self.lesson4_questions[self.current_lesson4_question_index]
        user_answer = self.lesson4_answer_entry.get().strip().lower()
        correct_answer = q['respuesta'].lower()

        if user_answer == correct_answer:
            self.lesson4_score += 10 # Se ganan 10 puntos por cada acierto
            self.lesson4_feedback_label.config(text=f"¡Correcto! ✅ '{q['respuesta']}' es la palabra clave. ¡Bien hecho!", fg="green")
        else:
            self.lesson4_feedback_label.config(text=f"Incorrecto. ❌ La respuesta correcta era '{q['respuesta']}'.", fg="red")
        
        self.lesson4_score_label.config(text=f"Puntuación: {self.lesson4_score} / {(self.current_lesson4_question_index + 1) * 10}")

        # Bloquear la entrada y el botón de verificar después de la respuesta
        self.lesson4_answer_entry.config(state=tk.DISABLED)
        
        # Reemplazar el botón de verificar con uno de siguiente
        for widget in self.current_content_frame.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_children(): # Buscar el frame de botones
                for btn in widget.winfo_children():
                    if btn.cget("text") == "Verificar Respuesta ✅":
                        btn.destroy()
                next_button = tk.Button(widget, text="Siguiente Pregunta ➡️", 
                                        command=self.next_lesson4_question,
                                        font=("Arial", 12, "bold"), bg="#1a73e8", fg="white", relief="raised")
                next_button.pack(side="left", padx=5)

    def next_lesson4_question(self):
        self.current_lesson4_question_index += 1
        self.display_lesson4_question()

    def show_lesson4_results(self):
        self.clear_content_frame()
        total_possible_score = len(self.lesson4_questions) * 10
        
        tk.Label(self.current_content_frame, text="--- ¡Lección 4 Completada! ---", 
                 font=("Arial", 20, "bold"), fg="#2980b9", bg="white").pack(pady=20)
        
        final_message = f"Tu puntuación final es: {self.lesson4_score} de {total_possible_score} puntos."
        tk.Label(self.current_content_frame, text=final_message, 
                 font=("Arial", 16, "bold"), fg="#2c3e50", bg="white").pack(pady=10)
        
        if self.lesson4_score == total_possible_score:
            tk.Label(self.current_content_frame, text="¡Perfecto! ¡Dominas las reglas gramaticales! ⭐⭐⭐", 
                     font=("Arial", 14, "italic"), fg="green", bg="white").pack(pady=5)
        elif self.lesson4_score >= total_possible_score * 0.7:
            tk.Label(self.current_content_frame, text="¡Muy bien! Estás cerca de dominar estas reglas. ¡Sigue practicando! 👍", 
                     font=("Arial", 14, "italic"), fg="#28a745", bg="white").pack(pady=5)
        else:
            tk.Label(self.current_content_frame, text="¡Buen intento! Repasa las reglas clave y vuelve a intentarlo para mejorar. 💪", 
                     font=("Arial", 14, "italic"), fg="#e67e22", bg="white").pack(pady=5)

        return_button = tk.Button(self.current_content_frame, text="Volver al Menú Principal ↩️", 
                                  command=self.show_welcome_screen,
                                  font=("Arial", 14, "bold"), bg="#3498db", fg="white", relief="raised")
        return_button.pack(pady=30)


    # --- Implementación de la Lección 5 para Tkinter (sin cambios con IA) ---
    def load_lesson5(self):
        self.clear_content_frame()
        self.current_lesson5_question_index = 0
        self.lesson5_score = 0
        
        tk.Label(self.current_content_frame, text="--- Lección 5: Redacción de Reglas (Desde Ejemplo) 🧠 ---", 
                 font=("Arial", 18, "bold"), fg="#34495e", bg="white").pack(pady=10)
        
        theory_text = (
            "En esta lección, desarrollarás tu capacidad de análisis gramatical.\n"
            "Se te presentará un ejemplo de aplicación de una regla y deberás redactar la regla que lo explica.\n\n"
            "**Ejemplo:**\n"
            "Palabra: 'café'\n"
            "Instrucción: Explica por qué 'café' lleva tilde.\n"
            "Respuesta esperada: 'La palabra 'café' es aguda y lleva tilde porque termina en vocal.'\n\n"
            "Intenta ser lo más preciso posible en tu redacción."
        )
        tk.Label(self.current_content_frame, text=theory_text, font=("Arial", 11), 
                 wraplength=600, justify="left", bg="white").pack(pady=10)

        start_button = tk.Button(self.current_content_frame, text="Iniciar Ejercicios de Lección 5 📝", 
                                 command=self.start_lesson5_exercises,
                                 font=("Arial", 14, "bold"), bg="#28a745", fg="white", relief="raised")
        start_button.pack(pady=20)

    def start_lesson5_exercises(self):
        self.clear_content_frame()
        
        self.lesson5_questions = [
            {
                "ejemplo": "Palabra: 'árbol'",
                "pregunta": "Explica por qué 'árbol' lleva tilde.",
                "palabras_clave": ["grave", "tilde", "no", "vocal", "n", "s"],
                "respuesta_ideal": "La palabra 'árbol' es grave y lleva tilde porque no termina en vocal, 'n' ni 's'."
            },
            {
                "ejemplo": "Oración: 'Mi mamá compró pan.'",
                "pregunta": "Explica por qué 'mamá' lleva tilde.",
                "palabras_clave": ["mamá", "aguda", "tilde", "termina", "vocal"],
                "respuesta_ideal": "La palabra 'mamá' es aguda y lleva tilde porque termina en vocal."
            },
            {
                "ejemplo": "Palabra: 'página'",
                "pregunta": "Explica por qué 'página' lleva tilde.",
                "palabras_clave": ["página", "esdrújula", "siempre", "tilde"],
                "respuesta_ideal": "La palabra 'página' es esdrújula y las esdrújulas siempre llevan tilde."
            },
            {
                "ejemplo": "Palabra: 'país'",
                "pregunta": "Explica por qué 'país' lleva tilde.",
                "palabras_clave": ["país", "hiato", "vocal cerrada", "tónica", "tilde"],
                "respuesta_ideal": "La palabra 'país' lleva tilde porque se forma un hiato entre una vocal abierta ('a') y una vocal cerrada tónica ('í'). La vocal cerrada tónica siempre lleva tilde en un hiato."
            },
            {
                "ejemplo": "Oración: 'Él tiene un libro.'",
                "pregunta": "Explica por qué 'Él' lleva tilde en esta oración.",
                "palabras_clave": ["él", "tilde diacrítica", "pronombre personal", "diferenciar", "artículo"],
                "respuesta_ideal": "'Él' lleva tilde diacrítica porque es un pronombre personal, para diferenciarlo del artículo 'el' que no lleva tilde."
            }
        ]
        random.shuffle(self.lesson5_questions)
        self.current_lesson5_question_index = 0
        self.lesson5_score = 0
        self.display_lesson5_question()

    def display_lesson5_question(self):
        self.clear_content_frame()
        if self.current_lesson5_question_index < len(self.lesson5_questions):
            q = self.lesson5_questions[self.current_lesson5_question_index]

            tk.Label(self.current_content_frame, text=f"--- Pregunta {self.current_lesson5_question_index + 1} de {len(self.lesson5_questions)} ---",
                     font=("Arial", 16, "bold"), fg="#34495e", bg="white").pack(pady=10)
            
            tk.Label(self.current_content_frame, text=f"Ejemplo: {q['ejemplo']}",
                     font=("Arial", 13), fg="#555", bg="white").pack(pady=5, anchor="w")
            
            tk.Label(self.current_content_frame, text=f"Pregunta: {q['pregunta']}",
                     font=("Arial", 13, "italic"), fg="#555", bg="white").pack(pady=5, anchor="w")
            
            tk.Label(self.current_content_frame, text="Tu redacción de la regla:",
                     font=("Arial", 12, "bold"), bg="white").pack(pady=10, anchor="w")
            
            self.lesson5_answer_entry = scrolledtext.ScrolledText(self.current_content_frame, wrap=tk.WORD, width=70, height=5, font=("Arial", 11), bd=2, relief="groove")
            self.lesson5_answer_entry.pack(pady=5)

            # Frame para los botones de acción
            action_buttons_frame = tk.Frame(self.current_content_frame, bg="white")
            action_buttons_frame.pack(pady=10)

            check_button = tk.Button(action_buttons_frame, text="Verificar Respuesta ✅", 
                                     command=self.check_lesson5_answer,
                                     font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised")
            check_button.pack(side="left", padx=5)

            self.lesson5_feedback_label = tk.Label(self.current_content_frame, text="", font=("Arial", 12), wraplength=600, bg="white")
            self.lesson5_feedback_label.pack(pady=10)

            self.lesson5_score_label = tk.Label(self.current_content_frame, text=f"Puntuación: {self.lesson5_score} / {self.current_lesson5_question_index * 10}",
                                                 font=("Arial", 12, "bold"), fg="#3498db", bg="white")
            self.lesson5_score_label.pack(pady=5)

        else:
            self.show_lesson5_results()

    def check_lesson5_answer(self):
        q = self.lesson5_questions[self.current_lesson5_question_index]
        user_answer = self.lesson5_answer_entry.get("1.0", tk.END).strip().lower()

        correct_by_keywords = all(keyword in user_answer for keyword in q['palabras_clave'])

        if correct_by_keywords:
            self.lesson5_score += 10
            self.lesson5_feedback_label.config(text=f"¡Correcto! ✅ Has capturado los puntos clave.\nLa regla ideal es: '{q['respuesta_ideal']}'", fg="green")
        else:
            self.lesson5_feedback_label.config(text=f"Incorrecto. ❌ Tu respuesta no contiene los elementos clave.\nLa regla correcta es: '{q['respuesta_ideal']}'.\nConsejo: Asegúrate de incluir conceptos como: {', '.join(q['palabras_clave'])}", fg="red")
        
        self.lesson5_score_label.config(text=f"Puntuación: {self.lesson5_score} / {(self.current_lesson5_question_index + 1) * 10}")

        self.lesson5_answer_entry.config(state=tk.DISABLED)
        
        for widget in self.current_content_frame.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_children():
                for btn in widget.winfo_children():
                    if btn.cget("text") == "Verificar Respuesta ✅":
                        btn.destroy()
                next_button = tk.Button(widget, text="Siguiente Pregunta ➡️", 
                                        command=self.next_lesson5_question,
                                        font=("Arial", 12, "bold"), bg="#1a73e8", fg="white", relief="raised")
                next_button.pack(side="left", padx=5)

    def next_lesson5_question(self):
        self.current_lesson5_question_index += 1
        self.display_lesson5_question()

    def show_lesson5_results(self):
        self.clear_content_frame()
        total_possible_score = len(self.lesson5_questions) * 10
        
        tk.Label(self.current_content_frame, text="--- ¡Lección 5 Completada! ---", 
                 font=("Arial", 20, "bold"), fg="#2980b9", bg="white").pack(pady=20)
        
        final_message = f"Tu puntuación final es: {self.lesson5_score} de {total_possible_score} puntos."
        tk.Label(self.current_content_frame, text=final_message, 
                 font=("Arial", 16, "bold"), fg="#2c3e50", bg="white").pack(pady=10)
        
        if self.lesson5_score == total_possible_score:
            tk.Label(self.current_content_frame, text="¡Eres un maestro en la redacción de reglas! ¡Impresionante! ⭐⭐⭐", 
                     font=("Arial", 14, "italic"), fg="green", bg="white").pack(pady=5)
        elif self.lesson5_score >= total_possible_score * 0.7:
            tk.Label(self.current_content_frame, text="¡Muy bien! Estás dominando la redacción de reglas. ¡Sigue así! 👍", 
                     font=("Arial", 14, "italic"), fg="#28a745", bg="white").pack(pady=5)
        else:
            tk.Label(self.current_content_frame, text="¡Buen intento! Repasa las reglas y vuelve a intentarlo para mejorar tu puntuación. 💪", 
                     font=("Arial", 14, "italic"), fg="#e67e22", bg="white").pack(pady=5)

        return_button = tk.Button(self.current_content_frame, text="Volver al Menú Principal ↩️", 
                                  command=self.show_welcome_screen,
                                  font=("Arial", 14, "bold"), bg="#3498db", fg="white", relief="raised")
        return_button.pack(pady=30)

    # --- Nueva Clase para Simular el Modelo Gemini ---
    class SimulatedGeminiModel:
        def __init__(self):
            self.tutoring_responses = {
                "tilde": "¡Claro! La tilde en español se usa para marcar la sílaba tónica. Hay reglas para agudas, graves y esdrújulas, además de la tilde diacrítica. Por ejemplo, 'árbol' lleva tilde porque es una palabra grave que no termina en vocal, 'n' ni 's'.",
                "acentuacion": "La acentuación es clave para la pronunciación y el significado. Las reglas de acentuación indican dónde va el golpe de voz y cuándo debe marcarse con tilde. Recuerda las palabras agudas, graves, esdrújulas y sobresdrújulas. ¡Practicar con ejemplos ayuda mucho!",
                "verbo": "Los verbos son el corazón de la oración. Indican acción, estado o proceso y se conjugan en diferentes tiempos (pasado, presente, futuro) y modos (indicativo, subjuntivo, imperativo). ¿Qué aspecto de los verbos te interesa más?",
                "conjugacion": "La conjugación verbal en español es compleja pero fascinante. Cada verbo cambia su forma según la persona, número, tiempo y modo. Empieza con los verbos regulares y luego avanza a los irregulares. ¡Es un camino divertido!",
                "coma": "La coma es un signo de puntuación que indica una pausa breve. Se usa para separar elementos de una enumeración, aclarar información (incisos), después de vocativos, y antes de algunas conjunciones. Su correcto uso mejora mucho la claridad del texto.",
                "puntuacion": "Los signos de puntuación son tus aliados para dar sentido a lo que escribes. El punto, la coma, el punto y coma, los dos puntos, etc., ayudan a organizar las ideas, indicar pausas y expresar la entonación adecuada. ¡Dominarlos te hará un mejor escritor!"
            }
            self.lesson_request_confirmations = [
                "¡Excelente sugerencia! He 'generado' una lección detallada sobre ese tema. La encontrarás pronto en tu biblioteca de lecciones.",
                "¡Gran idea! Acabo de 'crear' una lección personalizada sobre lo que pediste. ¡Espero que la disfrutes!",
                "¡Perfecto! Tu solicitud ha sido 'procesada'. La nueva lección está lista para que la explores.",
                "Me encanta ese tema. La lección sobre '{}' ya está 'disponible'."
            ]
            self.lesson_creation_assistant_responses = [
                "Claro, puedo ayudarte a crear una lección. Para empezar, ¿cuál es el tema principal que te gustaría abordar?",
                "¡Excelente idea! Para diseñar tu lección, dime: ¿cuál es el objetivo de aprendizaje? ¿Qué quieres que los estudiantes logren al final?",
                "Perfecto. Una vez que tengas el tema, podemos pensar en la estructura: introducción, explicación de conceptos, ejemplos, y ejercicios. ¿Hay algún tipo de ejercicio específico que te interese?",
                "La creación de lecciones es un proceso colaborativo. Dime más sobre lo que tienes en mente y te daré ideas, ejemplos o incluso te ayudaré a redactar secciones específicas."
            ]

        def generate_content(self, prompt_text, type="tutoring"):
            # Simula un retraso para parecer que la IA está pensando
            time.sleep(2) 
            
            if type == "tutoring":
                for keyword, response in self.tutoring_responses.items():
                    if keyword in prompt_text.lower():
                        return response
                return "¡Esa es una pregunta muy interesante! Gemini te daría una explicación detallada y ejemplos claros. (Respuesta simulada)."
            
            elif type == "new_lesson":
                confirmation = random.choice(self.lesson_request_confirmations)
                if '{}' in confirmation:
                    return confirmation.format(prompt_text)
                return confirmation
            
            elif type == "lesson_creation_assistant":
                if "ideas" in prompt_text.lower() or "temas" in prompt_text.lower():
                    return "Para ideas de lecciones, considera: el uso de los verbos 'ser' y 'estar', el pretérito imperfecto vs. el pretérito indefinido, los pronombres de objeto directo e indirecto, o las conjunciones. ¿Cuál te llama la atención?"
                elif "ejercicios" in prompt_text.lower() or "actividades" in prompt_text.lower():
                    return "Para ejercicios, podemos crear: completar espacios en blanco, verdadero/falso, transformar oraciones, unir conceptos con definiciones, o escribir ejemplos. ¿Qué tipo de habilidad quieres practicar?"
                elif "explicacion" in prompt_text.lower() or "teoria" in prompt_text.lower():
                    return "Si necesitas una explicación teórica, dame el concepto específico (ej. 'uso del subjuntivo') y te ayudaré a redactarlo de forma clara y con ejemplos."
                
                return random.choice(self.lesson_creation_assistant_responses) + "\n\n(Esta asistencia es simulada. Con la API de Gemini, sería mucho más interactiva y profunda.)"


    # --- Métodos para Funcionalidades de IA (sin cambios) ---
    def load_ai_tutoring(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Tutorías con IA Gemini 🤖 ---", font=("Arial", 18, "bold"), fg="#2980b9", bg="white").pack(pady=10)
        tk.Label(self.current_content_frame, text="Escribe tu pregunta sobre cualquier tema de español (gramática, ortografía, significado de palabras, etc.):", wraplength=600, bg="white").pack(pady=10)

        self.ai_question_entry = tk.Entry(self.current_content_frame, width=80, font=("Arial", 12), bd=2, relief="groove")
        self.ai_question_entry.pack(pady=5)
        
        send_button = tk.Button(self.current_content_frame, text="Enviar a Gemini 🚀", command=self.send_to_gemini_tutoring,
                                font=("Arial", 12, "bold"), bg="#27ae60", fg="white", relief="raised")
        send_button.pack(pady=10)

        tk.Label(self.current_content_frame, text="Respuesta de Gemini:", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
        self.ai_response_text = scrolledtext.ScrolledText(self.current_content_frame, wrap=tk.WORD, width=70, height=15, font=("Arial", 11), bd=2, relief="groove")
        self.ai_response_text.pack(pady=5, padx=10)
        self.ai_response_text.insert(tk.END, "Aquí verás las respuestas generadas por Gemini.")
        self.ai_response_text.config(state=tk.DISABLED)

    def send_to_gemini_tutoring(self):
        question = self.ai_question_entry.get().strip()
        if not question:
            messagebox.showwarning("Atención", "Por favor, escribe tu pregunta para Gemini.")
            return

        self.ai_response_text.config(state=tk.NORMAL)
        self.ai_response_text.delete(1.0, tk.END)
        self.ai_response_text.insert(tk.END, "Gemini está 'pensando'...\n")
        self.ai_response_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

        response_text = self.gemini_model_sim.generate_content(question, type="tutoring")
        
        self.ai_response_text.config(state=tk.NORMAL)
        self.ai_response_text.delete(1.0, tk.END)
        self.ai_response_text.insert(tk.END, response_text)
        self.ai_response_text.config(state=tk.DISABLED)

    def load_ai_new_lesson(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Solicitar Nueva Lección a IA Gemini 💡 ---", font=("Arial", 18, "bold"), fg="#2980b9", bg="white").pack(pady=10)
        tk.Label(self.current_content_frame, text="Describe el tema de la lección que te gustaría que Gemini te preparara:", wraplength=600, bg="white").pack(pady=10)

        self.lesson_request_entry = tk.Entry(self.current_content_frame, width=80, font=("Arial", 12), bd=2, relief="groove")
        self.lesson_request_entry.pack(pady=5)
        
        request_button = tk.Button(self.current_content_frame, text="Solicitar Lección a Gemini 📝", command=self.send_lesson_request_to_gemini,
                                  font=("Arial", 12, "bold"), bg="#27ae60", fg="white", relief="raised")
        request_button.pack(pady=10)

        self.lesson_status_label = tk.Label(self.current_content_frame, text="", font=("Arial", 12), fg="#34495e", bg="white")
        self.lesson_status_label.pack(pady=10)

    def send_lesson_request_to_gemini(self):
        request_topic = self.lesson_request_entry.get().strip()
        if not request_topic:
            messagebox.showwarning("Atención", "Por favor, describe el tema de la lección para Gemini.")
            return
        
        self.lesson_status_label.config(fg="blue", text="Gemini está 'generando' tu lección... por favor, espera un momento.")
        self.root.update_idletasks()

        confirmation_message = self.gemini_model_sim.generate_content(request_topic, type="new_lesson")
        
        self.lesson_status_label.config(fg="green", text=confirmation_message)
        messagebox.showinfo("Solicitud de Lección Completada", confirmation_message + "\n\n(En una app real, la lección completa aparecería aquí.)")

    def load_ai_lesson_creation_assistant(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Asistencia para Crear Lecciones con IA 📝✨ ---", 
                 font=("Arial", 18, "bold"), fg="#2980b9", bg="white").pack(pady=10)
        tk.Label(self.current_content_frame, text="Describe lo que necesitas para tu lección (ideas de tema, tipos de ejercicios, explicaciones para un concepto, etc.):", 
                 wraplength=600, bg="white").pack(pady=10)

        self.assistant_request_entry = tk.Entry(self.current_content_frame, width=80, font=("Arial", 12), bd=2, relief="groove")
        self.assistant_request_entry.pack(pady=5)
        
        send_button = tk.Button(self.current_content_frame, text="Pedir Asistencia a Gemini 🤝", 
                                command=self.send_lesson_creation_request_to_gemini,
                                font=("Arial", 12, "bold"), bg="#6c5ce7", fg="white", relief="raised")
        send_button.pack(pady=10)

        tk.Label(self.current_content_frame, text="Respuesta de Gemini:", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
        self.assistant_response_text = scrolledtext.ScrolledText(self.current_content_frame, wrap=tk.WORD, width=70, height=15, font=("Arial", 11), bd=2, relief="groove")
        self.assistant_response_text.pack(pady=5, padx=10)
        self.assistant_response_text.insert(tk.END, "Aquí verás la asistencia de Gemini para tu lección.")
        self.assistant_response_text.config(state=tk.DISABLED)

    def send_lesson_creation_request_to_gemini(self):
        request_text = self.assistant_request_entry.get().strip()
        if not request_text:
            messagebox.showwarning("Atención", "Por favor, describe qué tipo de asistencia necesitas.")
            return

        self.assistant_response_text.config(state=tk.NORMAL)
        self.assistant_response_text.delete(1.0, tk.END)
        self.assistant_response_text.insert(tk.END, "Gemini está 'colaborando' contigo...\n")
        self.assistant_response_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

        response_text = self.gemini_model_sim.generate_content(request_text, type="lesson_creation_assistant")
        
        self.assistant_response_text.config(state=tk.NORMAL)
        self.assistant_response_text.delete(1.0, tk.END)
        self.assistant_response_text.insert(tk.END, response_text)
        self.assistant_response_text.config(state=tk.DISABLED)


# --- Ejecución de la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SpanishLearningApp(root)
    root.mainloop()
