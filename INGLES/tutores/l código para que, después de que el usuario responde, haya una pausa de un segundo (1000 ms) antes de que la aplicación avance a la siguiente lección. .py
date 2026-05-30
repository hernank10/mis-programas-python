import tkinter as tk
from tkinter import messagebox
import random

# Este es el diccionario principal que contiene TODAS las lecciones.
# Aquí es donde agregarías tus 100 lecciones o más.
GRAMMAR_LESSONS = {
    "Lección 1: El Verbo 'To Be'": {
        "teoría": """El verbo 'to be' (ser/estar) es uno de los más importantes en inglés.
Se conjuga de la siguiente manera:
- I am (Yo soy/estoy)
- You are (Tú eres/estás)
- He/She/It is (Él/Ella/Eso es/está)
- We are (Nosotros somos/estamos)
- They are (Ellos son/están)""",
        "ejemplo": "He is a student. (Él es un estudiante.)",
        "pregunta": "¿Cuál es la forma correcta del verbo 'to be' para 'we'?",
        "opciones": ["is", "am", "are"],
        "respuesta_correcta": "are"
    },
    "Lección 2: Plurales Regulares": {
        "teoría": """Para la mayoría de los sustantivos, se forma el plural agregando una 's' al final.
Ejemplos:
- cat -> cats
- car -> cars
- book -> books""",
        "ejemplo": "I have two books. (Yo tengo dos libros.)",
        "pregunta": "El plural de 'dog' es:",
        "opciones": ["doges", "dog", "dogs"],
        "respuesta_correcta": "dogs"
    },
    "Lección 3: Presente Simple (Afirmativo)": {
        "teoría": """Se usa para hablar de hábitos, verdades generales o hechos.
Para los sujetos 'I, you, we, they', se usa la forma base del verbo.
Para los sujetos 'he, she, it', se agrega una 's' al final del verbo.
Ejemplos:
- I work.
- She works.""",
        "ejemplo": "He reads a lot. (Él lee mucho.)",
        "pregunta": "¿Cuál es la forma correcta de 'to play' para 'we'?",
        "opciones": ["plays", "play", "to playing"],
        "respuesta_correcta": "play"
    },
    # --- AQUÍ EMPEZARÍAS A AGREGAR LAS NUEVAS LECCIONES ---
    "Lección 4: Preposiciones de Tiempo (in, on, at)": {
        "teoría": """Las preposiciones de tiempo se usan para indicar cuándo ocurre algo.
- 'at' se usa para horas y momentos específicos (at 3 PM, at noon).
- 'on' se usa para días y fechas (on Monday, on October 25th).
- 'in' se usa para meses, años, estaciones y períodos de tiempo más largos (in July, in 2024, in the morning).""",
        "ejemplo": "The meeting is at 10 AM on Monday.",
        "pregunta": "¿Qué preposición es correcta para 'the summer'?",
        "opciones": ["on", "at", "in"],
        "respuesta_correcta": "in"
    },
    "Lección 5: Pasado Simple": {
        "teoría": """El pasado simple se usa para acciones que ocurrieron y terminaron en el pasado.
Para verbos regulares, se agrega '-ed' a la forma base.
Ejemplos:
- walk -> walked
- play -> played
- visit -> visited
Para verbos irregulares, la forma cambia completamente.""",
        "ejemplo": "I walked to school yesterday. (Yo caminé a la escuela ayer.)",
        "pregunta": "El pasado simple de 'talk' es:",
        "opciones": ["talks", "talked", "talken"],
        "respuesta_correcta": "talked"
    },
    # --- LECCIÓN AGREGADA PARA ESTA RESPUESTA ---
    "Lección 6: El Verbo Modal 'should'": {
        "teoría": """El verbo modal 'should' se utiliza para dar consejos, sugerencias o para indicar una obligación no muy estricta.
Ejemplos:
- You should study for the test. (Deberías estudiar para el examen.)
- We should leave now. (Deberíamos irnos ahora.)""",
        "ejemplo": "She should eat more vegetables. (Ella debería comer más verduras.)",
        "pregunta": "Selecciona la oración que usa 'should' correctamente:",
        "opciones": ["He should to go.", "They should goes.", "You should go."],
        "respuesta_correcta": "You should go."
    }
}

class GrammarApp:
    def __init__(self, master):
        self.master = master
        master.title("Aprendizaje de Gramática de Inglés")
        master.geometry("600x400")
        master.configure(bg="#f0f0f0")

        self.lecciones = list(GRAMMAR_LESSONS.keys())
        self.leccion_actual_index = 0
        self.puntaje = 0

        # UI Elements
        self.title_label = tk.Label(master, text="", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        self.theory_text = tk.Label(master, text="", font=("Arial", 12), justify="left", wraplength=550, bg="#f0f0f0")
        self.theory_text.pack(pady=5)

        self.example_label = tk.Label(master, text="", font=("Arial", 12, "italic"), bg="#f0f0f0")
        self.example_label.pack(pady=5)

        self.question_label = tk.Label(master, text="", font=("Arial", 14), bg="#f0f0f0")
        self.question_label.pack(pady=10)

        self.buttons_frame = tk.Frame(master, bg="#f0f0f0")
        self.buttons_frame.pack(pady=10)
        
        self.option_buttons = []
        for i in range(3):
            btn = tk.Button(self.buttons_frame, text="", command=lambda i=i: self.check_answer(i),
                            font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=20, pady=5)
            self.option_buttons.append(btn)
            btn.pack(side="left", padx=5)

        self.next_button = tk.Button(master, text="Siguiente Lección", command=self.next_lesson,
                                     font=("Arial", 12), bg="#008CBA", fg="white", bd=0, padx=20, pady=5)
        self.next_button.pack(pady=10)

        self.message_box = tk.Label(master, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.message_box.pack(pady=5)
        
        self.load_lesson()

    def load_lesson(self):
        """Loads the content for the current lesson index."""
        if self.leccion_actual_index < len(self.lecciones):
            leccion_titulo = self.lecciones[self.leccion_actual_index]
            leccion_data = GRAMMAR_LESSONS[leccion_titulo]

            # Update UI with lesson data
            self.title_label.config(text=leccion_titulo)
            self.theory_text.config(text=leccion_data["teoría"])
            self.example_label.config(text=leccion_data["ejemplo"])
            self.question_label.config(text=leccion_data["pregunta"])
            
            # Show options
            opciones = leccion_data["opciones"]
            random.shuffle(opciones)
            for i, btn in enumerate(self.option_buttons):
                btn.config(text=opciones[i], state="normal")
            
            self.next_button.pack_forget()
            self.message_box.config(text="")
        else:
            self.show_end_message()

    def check_answer(self, option_index):
        """Checks if the selected option is correct and provides feedback."""
        leccion_titulo = self.lecciones[self.leccion_actual_index]
        leccion_data = GRAMMAR_LESSONS[leccion_titulo]
        selected_answer = self.option_buttons[option_index]["text"]

        if selected_answer == leccion_data["respuesta_correcta"]:
            self.puntaje += 1
            self.message_box.config(text="¡Correcto! Sigue así.", fg="green")
        else:
            self.message_box.config(text="Incorrecto. La respuesta correcta es '{}'".format(leccion_data["respuesta_correcta"]), fg="red")
        
        # Disable buttons after an answer is selected
        for btn in self.option_buttons:
            btn.config(state="disabled")

        # Agrega un pequeño retraso (1000ms = 1 segundo) antes de pasar a la siguiente lección.
        self.master.after(1000, self.next_lesson)

    def next_lesson(self):
        """Moves to the next lesson."""
        self.leccion_actual_index += 1
        self.load_lesson()

    def show_end_message(self):
        """Displays a message when all lessons are completed."""
        # Clear the current UI elements
        for widget in self.master.winfo_children():
            widget.pack_forget()
        
        # Show end message
        end_label = tk.Label(self.master, text="¡Has completado todas las lecciones!", font=("Arial", 18, "bold"), bg="#f0f0f0")
        end_label.pack(pady=50)
        
        score_label = tk.Label(self.master, text=f"Tu puntuación final es: {self.puntaje}/{len(self.lecciones)}", font=("Arial", 16), bg="#f0f0f0")
        score_label.pack(pady=10)
        
        tk.Button(self.master, text="Reiniciar", command=self.restart_app, font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=5).pack(pady=20)

    def restart_app(self):
        """Restarts the application to the beginning."""
        self.leccion_actual_index = 0
        self.puntaje = 0
        self.master.destroy()
        root = tk.Tk()
        GrammarApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarApp(root)
    root.mainloop()
