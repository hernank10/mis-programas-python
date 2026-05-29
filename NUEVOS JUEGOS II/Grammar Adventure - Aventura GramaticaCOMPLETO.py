import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import time

class RainbowButton(tk.Canvas):
    def __init__(self, parent, text, emoticon="", command=None, width=200, height=50, **kwargs):
        super().__init__(parent, width=width, height=height, highlightthickness=0, **kwargs)
        self.text = text
        self.emoticon = emoticon
        self.command = command
        self.width = width
        self.height = height
        self.hovered = False
        self.clicked = False
        self.rainbow_offset = 0
        self.particles = []
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)
        
        self.after_id = None
        self.draw_button()
        
    def on_enter(self, event):
        self.hovered = True
        self.start_animation()
        
    def on_leave(self, event):
        self.hovered = False
        self.stop_animation()
        self.draw_button()
        
    def on_click(self, event):
        self.clicked = True
        self.draw_button()
        if self.command:
            self.command()
            
    def on_release(self, event):
        self.clicked = False
        self.draw_button()
        
    def start_animation(self):
        if self.after_id is None:
            self.animate()
            
    def stop_animation(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
            
    def animate(self):
        self.rainbow_offset = (self.rainbow_offset + 5) % 360
        self.draw_button()
        self.after_id = self.after(50, self.animate)
        
    def draw_button(self):
        self.delete("all")
        
        if self.hovered:
            for i in range(7):
                hue = (self.rainbow_offset + i * 30) % 360
                color = self.hsv_to_rgb(hue, 1, 1)
                x1 = i * (self.width // 7)
                x2 = (i + 1) * (self.width // 7)
                self.create_rectangle(x1, 0, x2, self.height, fill=color, outline=color)
        else:
            self.create_rectangle(0, 0, self.width, self.height, fill="#3498db", outline="#3498db")
            for i in range(3):
                hue = (self.rainbow_offset + i * 30) % 360
                color = self.hsv_to_rgb(hue, 1, 1)
                self.create_rectangle(i, i, self.width-i, self.height-i, outline=color, width=2)
        
        text_color = "white" if not self.hovered else "black"
        text_content = f"{self.emoticon} {self.text}"
        self.create_text(self.width//2, self.height//2, text=text_content, 
                        fill=text_color, font=("Arial", 12, "bold"))
        
        if self.hovered and random.random() < 0.2:
            self.create_particle()
            
    def create_particle(self):
        x = random.randint(10, self.width-10)
        y = self.height
        emoticon = random.choice(["⭐", "🎉", "💫", "✨", "🔥"])
        color = random.choice(["gold", "cyan", "magenta", "yellow", "orange"])
        
        particle = self.create_text(x, y, text=emoticon, fill=color, font=("Arial", 10))
        
        def move_particle():
            current_y = self.coords(particle)[1]
            if current_y > -10:
                self.move(particle, 0, -5)
                self.after(50, move_particle)
            else:
                self.delete(particle)
                
        move_particle()
        
    def hsv_to_rgb(self, h, s, v):
        h = h / 360.0
        if s == 0.0: 
            r = g = b = int(v * 255)
            return f"#{r:02x}{g:02x}{b:02x}"
        
        i = int(h * 6)
        f = (h * 6) - i
        p = v * (1 - s)
        q = v * (1 - s * f)
        t = v * (1 - s * (1 - f))
        i %= 6
        
        if i == 0: r, g, b = v, t, p
        if i == 1: r, g, b = q, v, p
        if i == 2: r, g, b = p, v, t
        if i == 3: r, g, b = p, q, v
        if i == 4: r, g, b = t, p, v
        if i == 5: r, g, b = v, p, q
        
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        return f"#{r:02x}{g:02x}{b:02x}"

class GrammarGame:
    def __init__(self, name, emoticon):
        self.name = name
        self.emoticon = emoticon
        self.score = 0
        self.current_question = 0
        self.questions = []
        self.return_to_menu = None  # Callback para volver al menú
        
    def load_questions(self):
        pass
        
    def display_question(self, parent):
        pass

# 🎯 JUEGO 1: CAZADOR DE SUJETO Y PREDICADO (Mejorado con navegación)
class SubjectPredicateGame(GrammarGame):
    def __init__(self):
        super().__init__("Cazador de Sujeto y Predicado", "🎯")
        self.load_questions()
        self.user_subject = ""
        self.user_predicate = ""
        
    def load_questions(self):
        self.questions = [
            {"sentence": "El niño juega en el parque", "subject": "El niño", "predicate": "juega en el parque", "bilingual": "The boy plays in the park"},
            {"sentence": "María estudia matemáticas en la biblioteca", "subject": "María", "predicate": "estudia matemáticas en la biblioteca", "bilingual": "Maria studies math at the library"},
            {"sentence": "Los pájaros cantan hermosamente por la mañana", "subject": "Los pájaros", "predicate": "cantan hermosamente por la mañana", "bilingual": "The birds sing beautifully in the morning"}
        ]
    
    def display_question(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.questions):
            self.show_results(parent)
            return
            
        question = self.questions[self.current_question]
        
        # Header con botón de volver al menú
        header_frame = tk.Frame(parent, bg="#2C3E50")
        header_frame.pack(fill=tk.X, pady=10)
        
        back_button = RainbowButton(header_frame, text="Volver al Menú", emoticon="🏠", 
                                   command=self.return_to_menu, width=150, height=40)
        back_button.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(header_frame, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(side=tk.LEFT, expand=True)
        
        # Contenido principal del juego
        content_frame = tk.Frame(parent, bg="#2C3E50")
        content_frame.pack(expand=True, fill=tk.BOTH, pady=20)
        
        sentence_label = tk.Label(content_frame, text=question["sentence"], 
                                 font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        sentence_label.pack(pady=10)
        
        bilingual_label = tk.Label(content_frame, text=question["bilingual"], 
                                  font=("Arial", 14), fg="#bdc3c7", bg="#2C3E50")
        bilingual_label.pack(pady=5)
        
        instructions = tk.Label(content_frame, text="Identifica el sujeto y el predicado:", 
                               font=("Arial", 12), fg="white", bg="#2C3E50")
        instructions.pack(pady=20)
        
        subject_frame = tk.Frame(content_frame, bg="#2C3E50")
        subject_frame.pack(pady=10)
        
        subject_label = tk.Label(subject_frame, text="Sujeto / Subject:", 
                                font=("Arial", 12), fg="white", bg="#2C3E50")
        subject_label.pack(side=tk.LEFT, padx=10)
        
        self.subject_entry = tk.Entry(subject_frame, font=("Arial", 12), width=40)
        self.subject_entry.pack(side=tk.LEFT, padx=10)
        self.subject_entry.insert(0, self.user_subject)
        
        predicate_frame = tk.Frame(content_frame, bg="#2C3E50")
        predicate_frame.pack(pady=10)
        
        predicate_label = tk.Label(predicate_frame, text="Predicado / Predicate:", 
                                  font=("Arial", 12), fg="white", bg="#2C3E50")
        predicate_label.pack(side=tk.LEFT, padx=10)
        
        self.predicate_entry = tk.Entry(predicate_frame, font=("Arial", 12), width=40)
        self.predicate_entry.pack(side=tk.LEFT, padx=10)
        self.predicate_entry.insert(0, self.user_predicate)
        
        # Botones de acción
        button_frame = tk.Frame(content_frame, bg="#2C3E50")
        button_frame.pack(pady=20)
        
        verify_button = RainbowButton(button_frame, text="Verificar Respuesta", emoticon="✅", 
                                     command=self.verify_answer, width=200, height=50)
        verify_button.pack(side=tk.LEFT, padx=10)
        
        skip_button = RainbowButton(button_frame, text="Saltar Pregunta", emoticon="⏭️", 
                                   command=self.skip_question, width=150, height=40)
        skip_button.pack(side=tk.LEFT, padx=10)
        
        parent.bind("<Return>", lambda e: self.verify_answer())
    
    def verify_answer(self):
        self.user_subject = self.subject_entry.get()
        self.user_predicate = self.predicate_entry.get()
        question = self.questions[self.current_question]
        
        subject_correct = self.user_subject.strip().lower() == question["subject"].lower()
        predicate_correct = self.user_predicate.strip().lower() == question["predicate"].lower()
        
        if subject_correct and predicate_correct:
            self.score += 10
            messagebox.showinfo("✅ Correcto", f"¡Ambas respuestas son correctas!\nPuntuación: {self.score}")
            self.next_question()
        else:
            errors = []
            if not subject_correct: errors.append("sujeto/subject")
            if not predicate_correct: errors.append("predicado/predicate")
            messagebox.showerror("❌ Incorrecto", 
                               f"Revisa tu(s): {', '.join(errors)}\nSujeto correcto: {question['subject']}\nPredicado correcto: {question['predicate']}")
    
    def skip_question(self):
        self.current_question += 1
        self.user_subject = ""
        self.user_predicate = ""
        self.display_question(self.subject_entry.master)
    
    def next_question(self):
        self.current_question += 1
        self.user_subject = ""
        self.user_predicate = ""
        self.display_question(self.subject_entry.master)
    
    def show_results(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        # Header con botón de volver
        header_frame = tk.Frame(parent, bg="#2C3E50")
        header_frame.pack(fill=tk.X, pady=10)
        
        back_button = RainbowButton(header_frame, text="Volver al Menú", emoticon="🏠", 
                                   command=self.return_to_menu, width=150, height=40)
        back_button.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(header_frame, text="🎉 ¡Juego Completado!", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(side=tk.LEFT, expand=True)
        
        # Contenido de resultados
        content_frame = tk.Frame(parent, bg="#2C3E50")
        content_frame.pack(expand=True, fill=tk.BOTH, pady=50)
        
        score_label = tk.Label(content_frame, text=f"Puntuación Final: {self.score}/{len(self.questions)*10}", 
                              font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        score_label.pack(pady=20)
        
        # Emoticono según puntuación
        if self.score >= len(self.questions)*8:
            emoticon = "🏆"
            message = "¡Excelente trabajo! Eres un experto en gramática."
        elif self.score >= len(self.questions)*6:
            emoticon = "⭐"
            message = "¡Buen trabajo! Sigue practicando."
        else:
            emoticon = "💪"
            message = "¡Sigue intentándolo! La práctica hace al maestro."
        
        result_label = tk.Label(content_frame, text=f"{emoticon} {message}", 
                               font=("Arial", 14), fg="#f39c12", bg="#2C3E50")
        result_label.pack(pady=10)
        
        button_frame = tk.Frame(content_frame, bg="#2C3E50")
        button_frame.pack(pady=30)
        
        menu_button = RainbowButton(button_frame, text="Volver al Menú Principal", emoticon="🏠", 
                                   command=self.return_to_menu, width=250, height=60)
        menu_button.pack(side=tk.LEFT, padx=10)
        
        restart_button = RainbowButton(button_frame, text="Jugar Otra Vez", emoticon "🔄", 
                                   command=self.restart_game, width=200, height=60)
        restart_button.pack(side=tk.LEFT, padx=10)
    
    def restart_game(self):
        self.score = 0
        self.current_question = 0
        self.user_subject = ""
        self.user_predicate = ""
        self.display_question(None)

# 🧩 JUEGO 2: PUZZLE DE LA ORACIÓN (Mejorado con navegación)
class PuzzleOracionGame(GrammarGame):
    def __init__(self):
        super().__init__("Puzzle de la Oración", "🧩")
        self.load_questions()
        self.user_sentence = ""
        
    def load_questions(self):
        self.questions = [
            {"words": ["casa", "la", "blanca", "es"], "correct": "La casa es blanca", "bilingual": "The house is white"},
            {"words": ["perro", "el", "corre", "rápidamente"], "correct": "El perro corre rápidamente", "bilingual": "The dog runs quickly"},
            {"words": ["libro", "interesante", "es", "un", "este"], "correct": "Este es un libro interesante", "bilingual": "This is an interesting book"}
        ]
    
    def display_question(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.questions):
            self.show_results(parent)
            return
            
        question = self.questions[self.current_question]
        shuffled_words = question["words"][:]
        random.shuffle(shuffled_words)
        
        # Header con navegación
        header_frame = tk.Frame(parent, bg="#2C3E50")
        header_frame.pack(fill=tk.X, pady=10)
        
        back_button = RainbowButton(header_frame, text="Volver al Menú", emoticon="🏠", 
                                   command=self.return_to_menu, width=150, height=40)
        back_button.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(header_frame, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(side=tk.LEFT, expand=True)
        
        progress_label = tk.Label(header_frame, text=f"Pregunta {self.current_question + 1}/{len(self.questions)}", 
                                 font=("Arial", 12), fg="#bdc3c7", bg="#2C3E50")
        progress_label.pack(side=tk.RIGHT, padx=10)
        
        # Contenido principal
        content_frame = tk.Frame(parent, bg="#2C3E50")
        content_frame.pack(expand=True, fill=tk.BOTH, pady=20)
        
        bilingual_label = tk.Label(content_frame, text=question["bilingual"], 
                                  font=("Arial", 14), fg="#bdc3c7", bg="#2C3E50")
        bilingual_label.pack(pady=5)
        
        instructions = tk.Label(content_frame, text="Ordena las palabras para formar una oración correcta:", 
                               font=("Arial", 12), fg="white", bg="#2C3E50")
        instructions.pack(pady=10)
        
        words_frame = tk.Frame(content_frame, bg="#2C3E50")
        words_frame.pack(pady=10)
        
        words_label = tk.Label(words_frame, text="Palabras disponibles:", 
                              font=("Arial", 10), fg="white", bg="#2C3E50")
        words_label.pack()
        
        words_text = tk.Label(words_frame, text=" | ".join(shuffled_words), 
                             font=("Arial", 12, "bold"), fg="#f39c12", bg="#2C3E50")
        words_text.pack(pady=5)
        
        sentence_frame = tk.Frame(content_frame, bg="#2C3E50")
        sentence_frame.pack(pady=10)
        
        sentence_label = tk.Label(sentence_frame, text="Tu oración:", 
                                 font=("Arial", 12), fg="white", bg="#2C3E50")
        sentence_label.pack()
        
        self.sentence_entry = tk.Entry(sentence_frame, font=("Arial", 12), width=50)
        self.sentence_entry.pack(pady=10)
        self.sentence_entry.insert(0, self.user_sentence)
        
        # Botones de acción
        button_frame = tk.Frame(content_frame, bg="#2C3E50")
        button_frame.pack(pady=20)
        
        verify_button = RainbowButton(button_frame, text="Verificar", emoticon="✅", 
                                     command=self.verify_answer, width=150, height=50)
        verify_button.pack(side=tk.LEFT, padx=10)
        
        skip_button = RainbowButton(button_frame, text="Saltar", emoticon="⏭️", 
                                   command=self.skip_question, width=120, height=40)
        skip_button.pack(side=tk.LEFT, padx=10)
        
        hint_button = RainbowButton(button_frame, text="Pista", emoticon="💡", 
                                   command=self.show_hint, width=100, height=40)
        hint_button.pack(side=tk.LEFT, padx=10)
        
        parent.bind("<Return>", lambda e: self.verify_answer())
    
    def verify_answer(self):
        self.user_sentence = self.sentence_entry.get()
        question = self.questions[self.current_question]
        
        if self.user_sentence.strip().lower() == question["correct"].lower():
            self.score += 10
            messagebox.showinfo("✅ Correcto", f"¡Oración correcta!\nPuntuación: {self.score}")
            self.next_question()
        else:
            messagebox.showerror("❌ Incorrecto", f"La oración no es correcta.\nCorrecto: {question['correct']}")
    
    def skip_question(self):
        self.current_question += 1
        self.user_sentence = ""
        self.display_question(self.sentence_entry.master)
    
    def show_hint(self):
        question = self.questions[self.current_question]
        # Mostrar la primera palabra como pista
        first_word = question["correct"].split()[0]
        messagebox.showinfo("💡 Pista", f"La oración comienza con: '{first_word}'")
    
    def next_question(self):
        self.current_question += 1
        self.user_sentence = ""
        self.display_question(self.sentence_entry.master)
    
    def show_results(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        # Header con navegación
        header_frame = tk.Frame(parent, bg="#2C3E50")
        header_frame.pack(fill=tk.X, pady=10)
        
        back_button = RainbowButton(header_frame, text="Volver al Menú", emoticon="🏠", 
                                   command=self.return_to_menu, width=150, height=40)
        back_button.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(header_frame, text="🎉 Puzzle Completado!", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(side=tk.LEFT, expand=True)
        
        # Contenido de resultados
        content_frame = tk.Frame(parent, bg="#2C3E50")
        content_frame.pack(expand=True, fill=tk.BOTH, pady=50)
        
        score_label = tk.Label(content_frame, text=f"Puntuación Final: {self.score}/{len(self.questions)*10}", 
                              font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        score_label.pack(pady=20)
        
        button_frame = tk.Frame(content_frame, bg="#2C3E50")
        button_frame.pack(pady=30)
        
        menu_button = RainbowButton(button_frame, text="Volver al Menú Principal", emoticon="🏠", 
                                   command=self.return_to_menu, width=250, height=60)
        menu_button.pack(side=tk.LEFT, padx=10)
        
        restart_button = RainbowButton(button_frame, text="Jugar Otra Vez", emoticon="🔄", 
                                      command=self.restart_game, width=200, height=60)
        restart_button.pack(side=tk.LEFT, padx=10)
    
    def restart_game(self):
        self.score = 0
        self.current_question = 0
        self.user_sentence = ""
        self.display_question(None)

# 📊 JUEGO 3: CLASIFICA LA ORACIÓN (Mejorado con navegación)
class ClasificaOracionGame(GrammarGame):
    def __init__(self):
        super().__init__("Clasifica la Oración", "📊")
        self.load_questions()
        
    def load_questions(self):
        self.questions = [
            {
                "sentence": "El niño juega y la niña canta.",
                "options": ["Simple", "Compuesta coordinada", "Compuesta subordinada", "Yuxtapuesta"],
                "correct": 1,
                "explanation": "Es compuesta coordinada porque tiene dos oraciones unidas por 'y'",
                "bilingual": "The boy plays and the girl sings."
            },
            {
                "sentence": "Cuando llegué, empezó a llover.",
                "options": ["Simple", "Compuesta coordinada", "Compuesta subordinada", "Yuxtapuesta"],
                "correct": 2,
                "explanation": "Es compuesta subordinada porque 'cuando llegué' depende de la principal",
                "bilingual": "When I arrived, it started to rain."
            }
        ]
    
    def display_question(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.questions):
            self.show_results(parent)
            return
            
        question = self.questions[self.current_question]
        
        # Header con navegación
        header_frame = tk.Frame(parent, bg="#2C3E50")
        header_frame.pack(fill=tk.X, pady=10)
        
        back_button = RainbowButton(header_frame, text="Volver al Menú", emoticon="🏠", 
                                   command=self.return_to_menu, width=150, height=40)
        back_button.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(header_frame, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(side=tk.LEFT, expand=True)
        
        progress_label = tk.Label(header_frame, text=f"Pregunta {self.current_question + 1}/{len(self.questions)}", 
                                 font=("Arial", 12), fg="#bdc3c7", bg="#2C3E50")
        progress_label.pack(side=tk.RIGHT, padx=10)
        
        # Contenido principal
        content_frame = tk.Frame(parent, bg="#2C3E50")
        content_frame.pack(expand=True, fill=tk.BOTH, pady=20)
        
        sentence_label = tk.Label(content_frame, text=question["sentence"], 
                                 font=("Arial", 16), fg="#ecf0f1", bg="#2C3E50")
        sentence_label.pack(pady=10)
        
        bilingual_label = tk.Label(content_frame, text=question["bilingual"], 
                                  font=("Arial", 12), fg="#bdc3c7", bg="#2C3E50")
        bilingual_label.pack(pady=5)
        
        instructions = tk.Label(content_frame, text="Selecciona el tipo de oración:", 
                               font=("Arial", 12), fg="white", bg="#2C3E50")
        instructions.pack(pady=20)
        
        options_frame = tk.Frame(content_frame, bg="#2C3E50")
        options_frame.pack(pady=10)
        
        for i, option in enumerate(question["options"]):
            btn = RainbowButton(options_frame, text=option, emoticon="🔤", 
                              command=lambda idx=i: self.check_answer(idx), 
                              width=250, height=40)
            btn.pack(pady=5)
        
        # Botón de saltar
        skip_frame = tk.Frame(content_frame, bg="#2C3E50")
        skip_frame.pack(pady=10)
        
        skip_button = RainbowButton(skip_frame, text="Saltar Pregunta", emoticon="⏭️", 
                                   command=self.skip_question, width=150, height=40)
        skip_button.pack()
    
    def check_answer(self, selected_index):
        question = self.questions[self.current_question]
        
        if selected_index == question["correct"]:
            self.score += 10
            messagebox.showinfo("✅ Correcto", f"¡Clasificación correcta! 🎉\nPuntuación: {self.score}")
        else:
            messagebox.showerror("❌ Incorrecto", 
                               f"Clasificación incorrecta. ❌\nCorrecto: {question['options'][question['correct']]}")
        
        self.current_question += 1
        self.display_question(None)
    
    def skip_question(self):
        self.current_question += 1
        self.display_question(None)
    
    def show_results(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        # Header con navegación
        header_frame = tk.Frame(parent, bg="#2C3E50")
        header_frame.pack(fill=tk.X, pady=10)
        
        back_button = RainbowButton(header_frame, text="Volver al Menú", emoticon="🏠", 
                                   command=self.return_to_menu, width=150, height=40)
        back_button.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(header_frame, text="🎉 Clasificación Completada!", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(side=tk.LEFT, expand=True)
        
        # Contenido de resultados
        content_frame = tk.Frame(parent, bg="#2C3E50")
        content_frame.pack(expand=True, fill=tk.BOTH, pady=50)
        
        score_label = tk.Label(content_frame, text=f"Puntuación Final: {self.score}/{len(self.questions)*10}", 
                              font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        score_label.pack(pady=20)
        
        button_frame = tk.Frame(content_frame, bg="#2C3E50")
        button_frame.pack(pady=30)
        
        menu_button = RainbowButton(button_frame, text="Volver al Menú Principal", emoticon="🏠", 
                                   command=self.return_to_menu, width=250, height=60)
        menu_button.pack(side=tk.LEFT, padx=10)
        
        restart_button = RainbowButton(button_frame, text="Jugar Otra Vez", emoticon="🔄", 
                                      command=self.restart_game, width=200, height=60)
        restart_button.pack(side=tk.LEFT, padx=10)
    
    def restart_game(self):
        self.score = 0
        self.current_question = 0
        self.display_question(None)

# APLICACIÓN PRINCIPAL MEJORADA
class GrammarAdventureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Grammar Adventure - Aventura Gramatical")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(True, True)
        
        self.center_window()
        self.current_game = None
        self.current_screen = "menu"
        
        # Sistema de partículas de fondo
        self.particle_canvas = tk.Canvas(root, bg='#2C3E50', highlightthickness=0)
        self.particle_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.particles = []
        self.start_particle_animation()
        
        self.content_frame = tk.Frame(root, bg='#2C3E50')
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center", width=900, height=600)
        
        self.show_main_menu()
        self.gradient_offset = 0
        self.animate_background()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def animate_background(self):
        self.gradient_offset = (self.gradient_offset + 0.5) % 100
        self.root.after(100, self.animate_background)
    
    def start_particle_animation(self):
        self.create_particle()
        self.move_particles()
    
    def create_particle(self):
        x = random.randint(0, 1000)
        y = -20
        size = random.randint(15, 25)
        emoticon = random.choice(["🎯", "🧩", "📊", "✏️", "🧱", "🏎️", "🛡️", "⭐", "🎉", "💫"])
        color = random.choice(["#ff6b6b", "#48dbfb", "#1dd1a1", "#feca57", "#ff9ff3", "#54a0ff"])
        
        particle = self.particle_canvas.create_text(x, y, text=emoticon, fill=color, 
                                                  font=("Arial", size), anchor="center")
        self.particles.append(particle)
        
        if len(self.particles) < 20:
            self.root.after(200, self.create_particle)
    
    def move_particles(self):
        for particle in self.particles[:]:
            coords = self.particle_canvas.coords(particle)
            if coords:
                x, y = coords
                new_y = y + 2
                if new_y > 700:
                    self.particle_canvas.delete(particle)
                    self.particles.remove(particle)
                    self.create_particle()
                else:
                    self.particle_canvas.move(particle, 0, 2)
        
        self.root.after(50, self.move_particles)
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        self.clear_content()
        self.current_screen = "menu"
        
        title_label = tk.Label(self.content_frame, text="🎮 Grammar Adventure", 
                              font=("Arial", 36, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=30)
        
        subtitle_label = tk.Label(self.content_frame, text="Aventura Gramatical Bilingüe", 
                                 font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        subtitle_label.pack(pady=10)
        
        games_frame = tk.Frame(self.content_frame, bg="#2C3E50")
        games_frame.pack(pady=40)
        
        # Todos los juegos implementados
        games = [
            ("🎯 Cazador de Sujeto y Predicado", SubjectPredicateGame),
            ("🧩 Puzzle de la Oración", PuzzleOracionGame),
            ("📊 Clasifica la Oración", ClasificaOracionGame),
            ("✏️ Corrector de Oraciones", None),
            ("🧱 Constructor de Oraciones", None),
            ("🏎️ Carrera de Conectores", None),
            ("🛡️ Defiende la Gramática", None)
        ]
        
        for text, game_class in games:
            if game_class:
                btn = RainbowButton(games_frame, text=text, emoticon="", 
                                  command=lambda gc=game_class: self.start_game(gc), 
                                  width=350, height=60, bg="#2C3E50")
            else:
                btn = RainbowButton(games_frame, text=text + " (Próximamente)", emoticon="", 
                                  command=lambda: messagebox.showinfo("Próximamente", "¡Este juego estará disponible pronto! 🚀"), 
                                  width=350, height=60, bg="#2C3E50")
            btn.pack(pady=8)
        
        footer_label = tk.Label(self.content_frame, 
                               text="✨ Navegación mejorada - ¡Volver al menú en cualquier momento! ✨", 
                               font=("Arial", 12), fg="#bdc3c7", bg="#2C3E50")
        footer_label.pack(side=tk.BOTTOM, pady=20)
    
    def start_game(self, game_class):
        self.clear_content()
        self.current_screen = "game"
        self.current_game = game_class()
        self.current_game.return_to_menu = self.show_main_menu
        self.current_game.display_question(self.content_frame)

def main():
    try:
        root = tk.Tk()
        app = GrammarAdventureApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
