import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import time
from PIL import Image, ImageTk, ImageDraw

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
        
    def load_questions(self):
        pass
        
    def display_question(self, parent):
        pass
        
    def check_answer(self, answer):
        pass

# 1. JUEGO: CAZADOR DE SUJETO Y PREDICADO
class SubjectPredicateGame(GrammarGame):
    def __init__(self):
        super().__init__("Cazador de Sujeto y Predicado", "🎯")
        self.load_questions()
        self.user_subject = ""
        self.user_predicate = ""
        
    def load_questions(self):
        self.questions = [
            {
                "sentence": "El niño juega en el parque",
                "subject": "El niño", "predicate": "juega en el parque",
                "bilingual": "The boy plays in the park"
            },
            {
                "sentence": "María estudia matemáticas en la biblioteca",
                "subject": "María", "predicate": "estudia matemáticas en la biblioteca",
                "bilingual": "Maria studies math at the library"
            },
            {
                "sentence": "Los pájaros cantan hermosamente por la mañana",
                "subject": "Los pájaros", "predicate": "cantan hermosamente por la mañana",
                "bilingual": "The birds sing beautifully in the morning"
            }
        ]
    
    def display_question(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.questions):
            self.show_results(parent)
            return
            
        question = self.questions[self.current_question]
        
        title_label = tk.Label(parent, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=20)
        
        sentence_label = tk.Label(parent, text=question["sentence"], 
                                 font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        sentence_label.pack(pady=10)
        
        bilingual_label = tk.Label(parent, text=question["bilingual"], 
                                  font=("Arial", 14), fg="#bdc3c7", bg="#2C3E50")
        bilingual_label.pack(pady=5)
        
        instructions = tk.Label(parent, text="Identifica el sujeto y el predicado / Identify subject and predicate:", 
                               font=("Arial", 12), fg="white", bg="#2C3E50")
        instructions.pack(pady=20)
        
        subject_frame = tk.Frame(parent, bg="#2C3E50")
        subject_frame.pack(pady=10)
        
        subject_label = tk.Label(subject_frame, text="Sujeto / Subject:", 
                                font=("Arial", 12), fg="white", bg="#2C3E50")
        subject_label.pack(side=tk.LEFT, padx=10)
        
        self.subject_entry = tk.Entry(subject_frame, font=("Arial", 12), width=40)
        self.subject_entry.pack(side=tk.LEFT, padx=10)
        self.subject_entry.insert(0, self.user_subject)
        
        predicate_frame = tk.Frame(parent, bg="#2C3E50")
        predicate_frame.pack(pady=10)
        
        predicate_label = tk.Label(predicate_frame, text="Predicado / Predicate:", 
                                  font=("Arial", 12), fg="white", bg="#2C3E50")
        predicate_label.pack(side=tk.LEFT, padx=10)
        
        self.predicate_entry = tk.Entry(predicate_frame, font=("Arial", 12), width=40)
        self.predicate_entry.pack(side=tk.LEFT, padx=10)
        self.predicate_entry.insert(0, self.user_predicate)
        
        verify_button = RainbowButton(parent, text="Verificar / Verify", emoticon="✅", 
                                     command=self.verify_answer, width=200, height=50)
        verify_button.pack(pady=20)
        
        parent.bind("<Return>", lambda e: self.verify_answer())
    
    def verify_answer(self):
        self.user_subject = self.subject_entry.get()
        self.user_predicate = self.predicate_entry.get()
        
        question = self.questions[self.current_question]
        subject_correct = self.user_subject.strip().lower() == question["subject"].lower()
        predicate_correct = self.user_predicate.strip().lower() == question["predicate"].lower()
        
        if subject_correct and predicate_correct:
            self.score += 10
            messagebox.showinfo("✅ Correcto / Correct", 
                              f"¡Ambas respuestas son correctas! / Both answers are correct!\n\n"
                              f"Puntuación / Score: {self.score}")
            self.current_question += 1
            self.user_subject = ""
            self.user_predicate = ""
            self.display_question(self.subject_entry.master)
        else:
            errors = []
            if not subject_correct:
                errors.append("sujeto/subject")
            if not predicate_correct:
                errors.append("predicado/predicate")
                
            messagebox.showerror("❌ Incorrecto / Incorrect", 
                               f"Revisa tu(s): {', '.join(errors)} / Check your: {', '.join(errors)}\n\n"
                               f"Sujeto correcto / Correct subject: {question['subject']}\n"
                               f"Predicado correcto / Correct predicate: {question['predicate']}")
    
    def show_results(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        title_label = tk.Label(parent, text="🎉 ¡Juego Completado! / Game Completed!", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=50)
        
        score_label = tk.Label(parent, text=f"Puntuación / Score: {self.score}/{len(self.questions)*10}", 
                              font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        score_label.pack(pady=20)
        
        menu_button = RainbowButton(parent, text="Volver al Menú / Return to Menu", 
                                   emoticon="🏠", command=self.return_to_menu, width=250, height=60)
        menu_button.pack(pady=30)
    
    def return_to_menu(self):
        pass

# 2. JUEGO: PUZZLE DE LA ORACIÓN
class PuzzleOracionGame(GrammarGame):
    def __init__(self):
        super().__init__("Puzzle de la Oración", "🧩")
        self.load_questions()
        self.user_sentence = ""
        
    def load_questions(self):
        self.questions = [
            {
                "words": ["casa", "la", "blanca", "es"],
                "correct": "La casa es blanca",
                "bilingual": "The house is white"
            },
            {
                "words": ["perro", "el", "corre", "rápidamente"],
                "correct": "El perro corre rápidamente",
                "bilingual": "The dog runs quickly"
            },
            {
                "words": ["libro", "interesante", "es", "un", "este"],
                "correct": "Este es un libro interesante",
                "bilingual": "This is an interesting book"
            }
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
        
        title_label = tk.Label(parent, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=20)
        
        bilingual_label = tk.Label(parent, text=question["bilingual"], 
                                  font=("Arial", 14), fg="#bdc3c7", bg="#2C3E50")
        bilingual_label.pack(pady=5)
        
        instructions = tk.Label(parent, text="Ordena las palabras para formar una oración correcta:", 
                               font=("Arial", 12), fg="white", bg="#2C3E50")
        instructions.pack(pady=10)
        
        # Mostrar palabras desordenadas
        words_frame = tk.Frame(parent, bg="#2C3E50")
        words_frame.pack(pady=10)
        
        words_label = tk.Label(words_frame, text="Palabras disponibles / Available words:", 
                              font=("Arial", 10), fg="white", bg="#2C3E50")
        words_label.pack()
        
        words_text = tk.Label(words_frame, text=" | ".join(shuffled_words), 
                             font=("Arial", 12, "bold"), fg="#f39c12", bg="#2C3E50")
        words_text.pack(pady=5)
        
        # Entrada para la oración
        sentence_frame = tk.Frame(parent, bg="#2C3E50")
        sentence_frame.pack(pady=10)
        
        sentence_label = tk.Label(sentence_frame, text="Tu oración / Your sentence:", 
                                 font=("Arial", 12), fg="white", bg="#2C3E50")
        sentence_label.pack()
        
        self.sentence_entry = tk.Entry(sentence_frame, font=("Arial", 12), width=50)
        self.sentence_entry.pack(pady=10)
        self.sentence_entry.insert(0, self.user_sentence)
        
        verify_button = RainbowButton(parent, text="Verificar / Verify", emoticon="✅", 
                                     command=self.verify_answer, width=200, height=50)
        verify_button.pack(pady=20)
        
        parent.bind("<Return>", lambda e: self.verify_answer())
    
    def verify_answer(self):
        self.user_sentence = self.sentence_entry.get()
        question = self.questions[self.current_question]
        
        if self.user_sentence.strip().lower() == question["correct"].lower():
            self.score += 10
            messagebox.showinfo("✅ Correcto / Correct", 
                              f"¡Oración correcta! / Correct sentence!\n\n"
                              f"Puntuación / Score: {self.score}")
            self.current_question += 1
            self.user_sentence = ""
            self.display_question(self.sentence_entry.master)
        else:
            messagebox.showerror("❌ Incorrecto / Incorrect", 
                               f"La oración no es correcta. / The sentence is not correct.\n\n"
                               f"Correcto: {question['correct']}")
    
    def show_results(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        title_label = tk.Label(parent, text="🎉 ¡Puzzle Completado! / Puzzle Completed!", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=50)
        
        score_label = tk.Label(parent, text=f"Puntuación / Score: {self.score}/{len(self.questions)*10}", 
                              font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        score_label.pack(pady=20)
        
        menu_button = RainbowButton(parent, text="Volver al Menú / Return to Menu", 
                                   emoticon="🏠", command=self.return_to_menu, width=250, height=60)
        menu_button.pack(pady=30)
    
    def return_to_menu(self):
        pass

# 3. JUEGO: CARRERA DE CONECTORES
class CarreraConectoresGame(GrammarGame):
    def __init__(self):
        super().__init__("Carrera de Conectores", "🏎️")
        self.load_questions()
        self.position = 0
        self.goal = 15
        
    def load_questions(self):
        self.questions = [
            {
                "sentence": "No fui a la fiesta ______ estaba enfermo",
                "options": ["porque", "pero", "aunque"],
                "correct": 0,
                "explanation": "'porque' indica causa-efecto",
                "bilingual": "I didn't go to the party ______ I was sick"
            },
            {
                "sentence": "Me gusta el café ______ no tomo mucho",
                "options": ["pero", "porque", "cuando"],
                "correct": 0,
                "explanation": "'pero' indica contraste",
                "bilingual": "I like coffee ______ I don't drink much"
            },
            {
                "sentence": "______ llegues temprano, podremos conversar",
                "options": ["Si", "Aunque", "Pero"],
                "correct": 0,
                "explanation": "'Si' introduce una condición",
                "bilingual": "______ you arrive early, we can talk"
            }
        ]
    
    def display_question(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.questions) or self.position >= self.goal:
            self.show_results(parent)
            return
            
        question = self.questions[self.current_question]
        
        title_label = tk.Label(parent, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=20)
        
        # Mostrar progreso de la carrera
        progress_frame = tk.Frame(parent, bg="#2C3E50")
        progress_frame.pack(pady=10)
        
        progress_text = tk.Label(progress_frame, text=f"Posición: {self.position}/{self.goal}", 
                                font=("Arial", 14), fg="#f39c12", bg="#2C3E50")
        progress_text.pack()
        
        # Barra de progreso simple
        progress_canvas = tk.Canvas(progress_frame, width=400, height=20, bg="#34495e", highlightthickness=0)
        progress_canvas.pack(pady=5)
        progress_width = (self.position / self.goal) * 400
        progress_canvas.create_rectangle(0, 0, progress_width, 20, fill="#2ecc71", outline="")
        
        # Pregunta
        sentence_label = tk.Label(parent, text=question["sentence"], 
                                 font=("Arial", 16), fg="#ecf0f1", bg="#2C3E50")
        sentence_label.pack(pady=10)
        
        bilingual_label = tk.Label(parent, text=question["bilingual"], 
                                  font=("Arial", 12), fg="#bdc3c7", bg="#2C3E50")
        bilingual_label.pack(pady=5)
        
        # Opciones
        options_frame = tk.Frame(parent, bg="#2C3E50")
        options_frame.pack(pady=20)
        
        for i, option in enumerate(question["options"]):
            btn = RainbowButton(options_frame, text=option, emoticon="🔤", 
                              command=lambda idx=i: self.check_answer(idx), 
                              width=150, height=40)
            btn.pack(side=tk.LEFT, padx=10)
    
    def check_answer(self, selected_index):
        question = self.questions[self.current_question]
        
        if selected_index == question["correct"]:
            self.position += 3
            messagebox.showinfo("✅ Correcto / Correct", 
                              f"¡Conector correcto! +3 posiciones\n\n"
                              f"{question['explanation']}")
        else:
            self.position = max(0, self.position - 1)
            messagebox.showerror("❌ Incorrecto / Incorrect", 
                               f"Conector incorrecto. -1 posición\n\n"
                               f"Correcto: {question['options'][question['correct']]}\n"
                               f"Explicación: {question['explanation']}")
        
        self.current_question = (self.current_question + 1) % len(self.questions)
        self.display_question(None)
    
    def show_results(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.position >= self.goal:
            title_text = "🎉 ¡Carrera Ganada! / Race Won!"
            message_text = f"¡Felicidades! Has completado la carrera.\nPosition final: {self.position}"
        else:
            title_text = "🏁 Carrera Terminada / Race Finished"
            message_text = f"Has llegado a la posición {self.position} de {self.goal}"
        
        title_label = tk.Label(parent, text=title_text, 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=50)
        
        message_label = tk.Label(parent, text=message_text, 
                               font=("Arial", 16), fg="#ecf0f1", bg="#2C3E50")
        message_label.pack(pady=20)
        
        score_label = tk.Label(parent, text=f"Puntuación / Score: {self.score}", 
                              font=("Arial", 14), fg="#f39c12", bg="#2C3E50")
        score_label.pack(pady=10)
        
        menu_button = RainbowButton(parent, text="Volver al Menú / Return to Menu", 
                                   emoticon="🏠", command=self.return_to_menu, width=250, height=60)
        menu_button.pack(pady=30)
    
    def return_to_menu(self):
        pass

# 4. JUEGO: CONSTRUCTOR DE ORACIONES
class ConstructorOracionesGame(GrammarGame):
    def __init__(self):
        super().__init__("Constructor de Oraciones", "🧱")
        self.load_words()
        self.user_sentence = ""
        
    def load_words(self):
        self.word_bank = {
            "sustantivos": ["niño", "niña", "libro", "casa", "perro", "gato", "escuela", "parque"],
            "verbos": ["juega", "estudia", "lee", "corre", "escribe", "canta", "dibuja", "salta"],
            "adjetivos": ["grande", "pequeño", "interesante", "divertido", "rápido", "lento", "hermoso"],
            "conectores": ["y", "pero", "porque", "cuando", "donde", "que"]
        }
        
        self.questions = [
            {"requirement": "Usa al menos un sustantivo y un verbo", "min_words": 4},
            {"requirement": "Incluye un adjetivo y un conector", "min_words": 5},
            {"requirement": "Crea una oración compuesta", "min_words": 6}
        ]
    
    def display_question(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.questions):
            self.show_results(parent)
            return
            
        question = self.questions[self.current_question]
        
        title_label = tk.Label(parent, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=20)
        
        requirement_label = tk.Label(parent, text=f"Requisito: {question['requirement']}", 
                                   font=("Arial", 14), fg="#f39c12", bg="#2C3E50")
        requirement_label.pack(pady=10)
        
        # Banco de palabras
        bank_frame = tk.Frame(parent, bg="#2C3E50")
        bank_frame.pack(pady=10)
        
        bank_label = tk.Label(bank_frame, text="Banco de palabras / Word bank:", 
                             font=("Arial", 12), fg="white", bg="#2C3E50")
        bank_label.pack()
        
        for category, words in self.word_bank.items():
            category_frame = tk.Frame(bank_frame, bg="#2C3E50")
            category_frame.pack(pady=5)
            
            category_label = tk.Label(category_frame, text=f"{category.title()}:", 
                                     font=("Arial", 10), fg="#bdc3c7", bg="#2C3E50")
            category_label.pack(side=tk.LEFT)
            
            words_label = tk.Label(category_frame, text=", ".join(words), 
                                  font=("Arial", 10), fg="#ecf0f1", bg="#2C3E50")
            words_label.pack(side=tk.LEFT, padx=10)
        
        # Área de construcción
        construction_frame = tk.Frame(parent, bg="#2C3E50")
        construction_frame.pack(pady=20)
        
        construction_label = tk.Label(construction_frame, text="Construye tu oración / Build your sentence:", 
                                     font=("Arial", 12), fg="white", bg="#2C3E50")
        construction_label.pack()
        
        self.sentence_entry = tk.Text(construction_frame, font=("Arial", 12), width=60, height=4)
        self.sentence_entry.pack(pady=10)
        self.sentence_entry.insert("1.0", self.user_sentence)
        
        verify_button = RainbowButton(parent, text="Verificar / Verify", emoticon="✅", 
                                     command=self.verify_answer, width=200, height=50)
        verify_button.pack(pady=20)
    
    def verify_answer(self):
        self.user_sentence = self.sentence_entry.get("1.0", tk.END).strip()
        question = self.questions[self.current_question]
        
        # Análisis básico de la oración
        words = self.user_sentence.split()
        has_noun = any(word in self.word_bank["sustantivos"] for word in words)
        has_verb = any(word in self.word_bank["verbos"] for word in words)
        has_adj = any(word in self.word_bank["adjetivos"] for word in words)
        has_conn = any(word in self.word_bank["conectores"] for word in words)
        
        # Verificar requisitos según la pregunta
        if self.current_question == 0:
            valid = has_noun and has_verb and len(words) >= question["min_words"]
            feedback = "Debes incluir al menos un sustantivo y un verbo"
        elif self.current_question == 1:
            valid = has_adj and has_conn and len(words) >= question["min_words"]
            feedback = "Debes incluir un adjetivo y un conector"
        else:
            valid = has_conn and len(words) >= question["min_words"]
            feedback = "Debes crear una oración compuesta con un conector"
        
        if valid:
            self.score += 10
            messagebox.showinfo("✅ Oración Válida / Valid Sentence", 
                              f"¡Oración construida correctamente!\n\n"
                              f"Puntuación: {self.score}")
            self.current_question += 1
            self.user_sentence = ""
            self.display_question(self.sentence_entry.master)
        else:
            messagebox.showerror("❌ Oración Inválida / Invalid Sentence", 
                               f"{feedback}\n\n"
                               f"Tu oración: {self.user_sentence}")
    
    def show_results(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()
            
        title_label = tk.Label(parent, text="🎉 ¡Construcción Completada! / Construction Completed!", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=50)
        
        score_label = tk.Label(parent, text=f"Puntuación / Score: {self.score}/{len(self.questions)*10}", 
                              font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        score_label.pack(pady=20)
        
        menu_button = RainbowButton(parent, text="Volver al Menú / Return to Menu", 
                                   emoticon="🏠", command=self.return_to_menu, width=250, height=60)
        menu_button.pack(pady=30)
    
    def return_to_menu(self):
        pass

# APLICACIÓN PRINCIPAL
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
        
        # Crear partículas de fondo
        self.particle_canvas = tk.Canvas(root, bg='#2C3E50', highlightthickness=0)
        self.particle_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.particles = []
        self.start_particle_animation()
        
        # Marco de contenido principal
        self.content_frame = tk.Frame(root, bg='#2C3E50')
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center", width=900, height=600)
        
        self.show_main_menu()
        
        # Animación de fondo
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
        
        games = [
            ("🎯 Cazador de Sujeto y Predicado", SubjectPredicateGame),
            ("🧩 Puzzle de la Oración", PuzzleOracionGame),
            ("🏎️ Carrera de Conectores", CarreraConectoresGame),
            ("🧱 Constructor de Oraciones", ConstructorOracionesGame),
            ("📊 Clasifica la Oración", None),
            ("✏️ Corrector de Oraciones", None),
            ("🛡️ Defiende la Gramática", None)
        ]
        
        for text, game_class in games:
            if game_class:
                btn = RainbowButton(games_frame, text=text, emoticon="", 
                                  command=lambda gc=game_class: self.start_game(gc), 
                                  width=350, height=60, bg="#2C3E50")
            else:
                btn = RainbowButton(games_frame, text=text + " (Próximamente)", emoticon="", 
                                  command=lambda: messagebox.showinfo("Próximamente", "Este juego estará disponible pronto!"), 
                                  width=350, height=60, bg="#2C3E50")
            btn.pack(pady=8)
        
        footer_label = tk.Label(self.content_frame, 
                               text="✨ Aprende gramática español-inglés de forma divertida! ✨", 
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
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
