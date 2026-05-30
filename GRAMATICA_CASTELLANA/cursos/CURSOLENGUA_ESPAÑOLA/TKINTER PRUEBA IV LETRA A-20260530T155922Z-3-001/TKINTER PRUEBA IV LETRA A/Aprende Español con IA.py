import tkinter as tk
from tkinter import messagebox, scrolledtext
# Importar otras funciones de lecciones que ya tenemos
# from your_console_script import (
#    intro_ortografia_teoria_consola, acentuacion_teoria_consola,
#    transformacion_oraciones_teoria_consola, completar_regla_teoria_consola,
#    redactar_regla_desde_ejemplo_teoria_consola
# )

class SpanishLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprende Español con IA 🇪🇸🤖")
        self.root.geometry("1000x700") # Tamaño de la ventana

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

    def clear_content_frame(self):
        """Limpia el contenido del frame principal para cargar nueva lección/ejercicio."""
        for widget in self.current_content_frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_content_frame()
        welcome_text = tk.Label(self.current_content_frame, text="¡Hola! Selecciona una lección del menú o interactúa con Gemini.",
                                font=("Arial", 16), fg="#34495e", wraplength=500, justify="center")
        welcome_text.pack(pady=50)

    def create_lesson_menu(self):
        """Crea los botones para las lecciones en el sidebar."""
        menu_title = tk.Label(self.sidebar_frame, text="Lecciones y IA", font=("Arial", 14, "bold"), bg="#bdc3c7", fg="#34495e")
        menu_title.pack(pady=10)

        lessons = [
            ("Introducción a la Ortografía 📚", self.load_lesson1),
            ("Acentuación ✨", self.load_lesson2),
            ("Transformación de Oraciones 🔄", self.load_lesson3),
            ("Redacción de Reglas (Huecos) ✍️", self.load_lesson4),
            ("Redacción de Reglas (Ejemplo) 🧠", self.load_lesson5),
            ("Tutorías con IA Gemini 🤖", self.load_ai_tutoring),
            ("Solicitar Nueva Lección IA 💡", self.load_ai_new_lesson)
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
        tk.Label(self.current_content_frame, text="--- Lección 1: Ortografía Básica ---", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí iría la teoría y los ejercicios de la Lección 1.", wraplength=600).pack()
        # Aquí llamarías a la lógica de la lección 1, adaptando para Tkinter
        # Por ejemplo: self.show_ortografia_exercises()

    def load_lesson2(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Lección 2: Acentuación ---", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí iría la teoría y los ejercicios de la Lección 2.", wraplength=600).pack()
        # Por ejemplo: self.show_acentuacion_exercises()

    def load_lesson3(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Lección 3: Transformación de Oraciones ---", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí iría la teoría y los ejercicios de la Lección 3.", wraplength=600).pack()

    def load_lesson4(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Lección 4: Redacción de Reglas (Gamificada) ---", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí irían los ejercicios gamificados de completar huecos con puntuación visual.", wraplength=600).pack()
        # Se necesitaría una lógica específica para mostrar el progreso/puntuación en tiempo real en Tkinter.

    def load_lesson5(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Lección 5: Redacción de Reglas (Desde Ejemplo) ---", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.current_content_frame, text="Aquí irían los ejercicios para redactar reglas desde ejemplos.", wraplength=600).pack()

    # --- Métodos para Funcionalidades de IA ---
    def load_ai_tutoring(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Tutorías con IA Gemini 🤖 ---", font=("Arial", 18, "bold"), fg="#2980b9").pack(pady=10)
        tk.Label(self.current_content_frame, text="Escribe tu pregunta sobre cualquier tema de español (gramática, ortografía, significado de palabras, etc.):", wraplength=600).pack(pady=10)

        self.ai_question_entry = tk.Entry(self.current_content_frame, width=80, font=("Arial", 12))
        self.ai_question_entry.pack(pady=5)
        
        send_button = tk.Button(self.current_content_frame, text="Enviar a Gemini 🚀", command=self.simulate_gemini_tutoring,
                                font=("Arial", 12, "bold"), bg="#27ae60", fg="white")
        send_button.pack(pady=10)

        tk.Label(self.current_content_frame, text="Respuesta de Gemini:", font=("Arial", 14, "bold")).pack(pady=10)
        self.ai_response_text = scrolledtext.ScrolledText(self.current_content_frame, wrap=tk.WORD, width=70, height=15, font=("Arial", 11))
        self.ai_response_text.pack(pady=5, padx=10)
        self.ai_response_text.insert(tk.END, "Aquí verás las respuestas generadas por Gemini (simulado).")
        self.ai_response_text.config(state=tk.DISABLED) # Hacerlo de solo lectura

    def simulate_gemini_tutoring(self):
        question = self.ai_question_entry.get().strip()
        if not question:
            messagebox.showwarning("Atención", "Por favor, escribe tu pregunta.")
            return

        self.ai_response_text.config(state=tk.NORMAL)
        self.ai_response_text.delete(1.0, tk.END) # Limpiar contenido anterior

        # --- SIMULACIÓN DE RESPUESTA DE GEMINI ---
        simulated_response = f"¡Excelente pregunta sobre '{question}'!\n\n"
        if "tilde" in question.lower() or "acentuacion" in question.lower():
            simulated_response += "Las tildes en español siguen reglas claras (agudas, graves, esdrújulas, hiatos, diacrítica). Por ejemplo, si preguntas por 'ahí', lleva tilde porque es un hiato que rompe el diptongo 'ai' y la 'í' es la vocal tónica cerrada."
        elif "verbo" in question.lower() or "conjugacion" in question.lower():
            simulated_response += "Los verbos en español son fascinantes. Recuerda que cambian según el tiempo, modo, persona y número. ¿Qué verbo o tiempo verbal te gustaría explorar?"
        elif "coma" in question.lower() or "puntuacion" in question.lower():
            simulated_response += "El uso de la coma es crucial para la claridad. Se usa para separar elementos de una enumeración, en vocativos, antes de ciertas conjunciones, etc. ¿Tienes un ejemplo en mente?"
        else:
            simulated_response += "¡Esa es una pregunta interesante! Gemini podría analizar tu texto y darte una respuesta detallada. Para una interacción real, necesitarías una integración directa con la API de Gemini."
        
        simulated_response += "\n\n(Esta es una respuesta simulada por el momento. Para la funcionalidad completa, necesitarías integrar la API de Gemini.)"
        
        self.ai_response_text.insert(tk.END, simulated_response)
        self.ai_response_text.config(state=tk.DISABLED)
        # --- FIN SIMULACIÓN ---

    def load_ai_new_lesson(self):
        self.clear_content_frame()
        tk.Label(self.current_content_frame, text="--- Solicitar Nueva Lección a IA Gemini 💡 ---", font=("Arial", 18, "bold"), fg="#2980b9").pack(pady=10)
        tk.Label(self.current_content_frame, text="Describe el tema de la lección que te gustaría que Gemini te preparara:", wraplength=600).pack(pady=10)

        self.lesson_request_entry = tk.Entry(self.current_content_frame, width=80, font=("Arial", 12))
        self.lesson_request_entry.pack(pady=5)
        
        request_button = tk.Button(self.current_content_frame, text="Solicitar Lección a Gemini 📝", command=self.simulate_gemini_lesson_request,
                                  font=("Arial", 12, "bold"), bg="#27ae60", fg="white")
        request_button.pack(pady=10)

        self.lesson_status_label = tk.Label(self.current_content_frame, text="", font=("Arial", 12), fg="#34495e")
        self.lesson_status_label.pack(pady=10)

    def simulate_gemini_lesson_request(self):
        request_topic = self.lesson_request_entry.get().strip()
        if not request_topic:
            messagebox.showwarning("Atención", "Por favor, describe el tema de la lección.")
            return
        
        self.lesson_status_label.config(fg="green", text=f"🎉 ¡Solicitud recibida! Gemini está 'generando' una lección sobre '{request_topic}'.")
        messagebox.showinfo("Solicitud de Lección", f"Una lección sobre '{request_topic}' ha sido 'generada' por Gemini (simulado). En una app real, esta lección aparecería aquí.")
        self.lesson_status_label.config(fg="gray", text="Estado: 'Lección generada' (simulado).")


# --- Ejecución de la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SpanishLearningApp(root)
    root.mainloop()
