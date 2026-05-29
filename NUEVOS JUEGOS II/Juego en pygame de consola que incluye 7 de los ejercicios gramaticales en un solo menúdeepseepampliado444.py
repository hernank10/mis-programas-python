import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import time
from PIL import Image, ImageTk, ImageDraw
import threading

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
        
        # Bind events
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)
        
        # Animation
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
        
        # Create gradient background
        if self.hovered:
            # Rainbow gradient for hover
            for i in range(7):
                hue = (self.rainbow_offset + i * 30) % 360
                color = self.hsv_to_rgb(hue, 1, 1)
                x1 = i * (self.width // 7)
                x2 = (i + 1) * (self.width // 7)
                self.create_rectangle(x1, 0, x2, self.height, fill=color, outline=color)
        else:
            # Solid color with rainbow border
            self.create_rectangle(0, 0, self.width, self.height, fill="#3498db", outline="#3498db")
            for i in range(3):
                hue = (self.rainbow_offset + i * 30) % 360
                color = self.hsv_to_rgb(hue, 1, 1)
                self.create_rectangle(i, i, self.width-i, self.height-i, outline=color, width=2)
        
        # Add text and emoticon
        text_color = "white" if not self.hovered else "black"
        text_content = f"{self.emoticon} {self.text}"
        self.create_text(self.width//2, self.height//2, text=text_content, 
                        fill=text_color, font=("Arial", 12, "bold"))
        
        # Add particle effects on hover
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

class ParticleSystem(tk.Canvas):
    def __init__(self, parent, width, height, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.particles = []
        self.configure(highlightthickness=0, bg='#1a1a2e')
        self.animation_running = False
        
    def start_animation(self):
        self.animation_running = True
        self.animate()
        
    def stop_animation(self):
        self.animation_running = False
        
    def animate(self):
        if not self.animation_running:
            return
            
        # Add new particles randomly
        if random.random() < 0.1:
            self.add_particle()
            
        # Move existing particles
        for particle in self.particles[:]:
            particle_id, x, y, speed, size, emoticon, color, rotation = particle
            new_y = y + speed
            
            if new_y > self.height + 20:
                self.delete(particle_id)
                self.particles.remove(particle)
            else:
                # Update position and rotation
                new_rotation = (rotation + 2) % 360
                self.coords(particle_id, x, new_y)
                
                # For rotation effect, we'd need to delete and recreate with rotation
                # This is simplified for performance
                particle[1] = x
                particle[2] = new_y
                particle[7] = new_rotation
                
        self.after(50, self.animate)
        
    def add_particle(self):
        x = random.randint(0, self.width)
        y = -20
        speed = random.uniform(1, 3)
        size = random.randint(15, 25)
        emoticon = random.choice(["🎯", "🧩", "📊", "✏️", "🧱", "🏎️", "🛡️", "⭐", "🎉", "💫"])
        color = random.choice(["#ff6b6b", "#48dbfb", "#1dd1a1", "#feca57", "#ff9ff3", "#54a0ff"])
        
        particle_id = self.create_text(x, y, text=emoticon, fill=color, 
                                     font=("Arial", size), anchor="center")
        rotation = random.uniform(0, 360)
        
        self.particles.append([particle_id, x, y, speed, size, emoticon, color, rotation])

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

class SubjectPredicateGame(GrammarGame):
    def __init__(self):
        super().__init__("Cazador de Sujeto y Predicado", "🎯")
        self.load_questions()
        self.user_subject = ""
        self.user_predicate = ""
        self.input_active = "subject"
        
    def load_questions(self):
        self.questions = [
            {
                "sentence": "El niño juega en el parque",
                "subject": "El niño",
                "predicate": "juega en el parque",
                "bilingual": "The boy plays in the park"
            },
            {
                "sentence": "María estudia matemáticas en la biblioteca",
                "subject": "María",
                "predicate": "estudia matemáticas en la biblioteca",
                "bilingual": "Maria studies math at the library"
            },
            {
                "sentence": "Los pájaros cantan hermosamente por la mañana",
                "subject": "Los pájaros",
                "predicate": "cantan hermosamente por la mañana",
                "bilingual": "The birds sing beautifully in the morning"
            }
        ]
    
    def display_question(self, parent):
        # Clear previous content
        for widget in parent.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.questions):
            self.show_results(parent)
            return
            
        question = self.questions[self.current_question]
        
        # Title
        title_label = tk.Label(parent, text=f"{self.emoticon} {self.name}", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=20)
        
        # Sentence to analyze
        sentence_label = tk.Label(parent, text=question["sentence"], 
                                 font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        sentence_label.pack(pady=10)
        
        # Bilingual version
        bilingual_label = tk.Label(parent, text=question["bilingual"], 
                                  font=("Arial", 14), fg="#bdc3c7", bg="#2C3E50")
        bilingual_label.pack(pady=5)
        
        # Instructions
        instructions = tk.Label(parent, text="Identifica el sujeto y el predicado / Identify subject and predicate:", 
                               font=("Arial", 12), fg="white", bg="#2C3E50")
        instructions.pack(pady=20)
        
        # Subject input
        subject_frame = tk.Frame(parent, bg="#2C3E50")
        subject_frame.pack(pady=10)
        
        subject_label = tk.Label(subject_frame, text="Sujeto / Subject:", 
                                font=("Arial", 12), fg="white", bg="#2C3E50")
        subject_label.pack(side=tk.LEFT, padx=10)
        
        self.subject_entry = tk.Entry(subject_frame, font=("Arial", 12), width=40)
        self.subject_entry.pack(side=tk.LEFT, padx=10)
        self.subject_entry.insert(0, self.user_subject)
        self.subject_entry.bind("<FocusIn>", lambda e: setattr(self, 'input_active', 'subject'))
        
        # Predicate input
        predicate_frame = tk.Frame(parent, bg="#2C3E50")
        predicate_frame.pack(pady=10)
        
        predicate_label = tk.Label(predicate_frame, text="Predicado / Predicate:", 
                                  font=("Arial", 12), fg="white", bg="#2C3E50")
        predicate_label.pack(side=tk.LEFT, padx=10)
        
        self.predicate_entry = tk.Entry(predicate_frame, font=("Arial", 12), width=40)
        self.predicate_entry.pack(side=tk.LEFT, padx=10)
        self.predicate_entry.insert(0, self.user_predicate)
        self.predicate_entry.bind("<FocusIn>", lambda e: setattr(self, 'input_active', 'predicate'))
        
        # Verify button
        verify_button = RainbowButton(parent, text="Verificar / Verify", emoticon="✅", 
                                     command=self.verify_answer, width=200, height=50)
        verify_button.pack(pady=20)
        
        # Bind Enter key to verify
        parent.bind("<Return>", lambda e: self.verify_answer())
        
        # Set focus to appropriate field
        if self.input_active == "subject":
            self.subject_entry.focus_set()
        else:
            self.predicate_entry.focus_set()
    
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
            
        # Results title
        title_label = tk.Label(parent, text="🎉 ¡Juego Completado! / Game Completed!", 
                              font=("Arial", 24, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=50)
        
        # Score
        score_label = tk.Label(parent, text=f"Puntuación / Score: {self.score}/{len(self.questions)*10}", 
                              font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        score_label.pack(pady=20)
        
        # Return to menu button
        menu_button = RainbowButton(parent, text="Volver al Menú / Return to Menu", 
                                   emoticon="🏠", command=self.return_to_menu, width=250, height=60)
        menu_button.pack(pady=30)
    
    def return_to_menu(self):
        # This will be set by the main application
        pass

class GrammarAdventureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Grammar Adventure - Aventura Gramatical")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(True, True)
        
        # Center the window
        self.center_window()
        
        # Current game state
        self.current_game = None
        self.current_screen = "menu"
        
        # Create particle system for background
        self.particle_system = ParticleSystem(root, 1000, 700)
        self.particle_system.place(x=0, y=0, relwidth=1, relheight=1)
        self.particle_system.start_animation()
        
        # Create main content frame (on top of particles)
        self.content_frame = tk.Frame(root, bg='#2C3E50')
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center", width=900, height=600)
        
        # Show main menu
        self.show_main_menu()
        
        # Animated background gradient
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
        # Animate the gradient background
        self.gradient_offset = (self.gradient_offset + 0.5) % 100
        self.root.after(100, self.animate_background)
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        self.clear_content()
        self.current_screen = "menu"
        
        # Main title
        title_label = tk.Label(self.content_frame, text="🎮 Grammar Adventure", 
                              font=("Arial", 36, "bold"), fg="white", bg="#2C3E50")
        title_label.pack(pady=30)
        
        subtitle_label = tk.Label(self.content_frame, text="Aventura Gramatical Bilingüe", 
                                 font=("Arial", 18), fg="#ecf0f1", bg="#2C3E50")
        subtitle_label.pack(pady=10)
        
        # Game buttons
        games_frame = tk.Frame(self.content_frame, bg="#2C3E50")
        games_frame.pack(pady=40)
        
        games = [
            ("🎯 Cazador de Sujeto y Predicado", "sujeto_predicado"),
            ("🧩 Puzzle de la Oración", "puzzle_oracion"),
            ("📊 Clasifica la Oración", "clasifica_oracion"),
            ("✏️ Corrector de Oraciones", "corrector_oraciones"),
            ("🧱 Construye tu Propia Oración", "construye_oracion"),
            ("🏎️ Carrera de Conectores", "carrera_conectores"),
            ("🛡️ Defiende la Gramática", "defensa_gramatica")
        ]
        
        for text, game_id in games:
            button = RainbowButton(games_frame, text=text, emoticon="", 
                                  command=lambda g=game_id: self.start_game(g), 
                                  width=350, height=60, bg="#2C3E50")
            button.pack(pady=8)
        
        # Footer
        footer_label = tk.Label(self.content_frame, 
                               text="✨ Aprende gramática español-inglés de forma divertida! ✨", 
                               font=("Arial", 12), fg="#bdc3c7", bg="#2C3E50")
        footer_label.pack(side=tk.BOTTOM, pady=20)
    
    def start_game(self, game_id):
        self.clear_content()
        self.current_screen = "game"
        
        if game_id == "sujeto_predicado":
            self.current_game = SubjectPredicateGame()
            self.current_game.return_to_menu = self.show_main_menu
            self.current_game.display_question(self.content_frame)
        else:
            # Placeholder for other games
            placeholder_label = tk.Label(self.content_frame, 
                                       text=f"🎮 {game_id.replace('_', ' ').title()} \n\n(Próximamente / Coming Soon)", 
                                       font=("Arial", 24), fg="white", bg="#2C3E50")
            placeholder_label.pack(expand=True)
            
            back_button = RainbowButton(self.content_frame, text="Volver al Menú / Back to Menu", 
                                       emoticon="🏠", command=self.show_main_menu, width=250, height=50)
            back_button.pack(pady=30)

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
