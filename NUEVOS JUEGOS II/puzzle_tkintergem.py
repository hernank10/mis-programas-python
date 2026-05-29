import tkinter as tk
import random
from tkinter import messagebox

# --- Datos del Juego: 20 Ejercicios ---
EJERCICIOS = [
    {"es": "El perro persigue al gato.", "en": "The dog chases the cat."},
    {"es": "La profesora enseña a los estudiantes.", "en": "The teacher teaches the students."},
    {"es": "Mi hermano juega con la pelota.", "en": "My brother plays with the ball."},
    {"es": "El sol brilla en el cielo.", "en": "The sun shines in the sky."},
    {"es": "Ella lee un libro interesante.", "en": "She reads an interesting book."},
    {"es": "Nosotros viajamos en un coche.", "en": "We travel in a car."},
    {"es": "Los pájaros cantan por la mañana.", "en": "The birds sing in the morning."},
    {"es": "El chef cocina una deliciosa sopa.", "en": "The chef cooks a delicious soup."},
    {"es": "Tú escribes una historia.", "en": "You write a story."},
    {"es": "Los niños construyen un castillo de arena.", "en": "The children build a sandcastle."},
    {"es": "El tren llega a la estación a tiempo.", "en": "The train arrives at the station on time."},
    {"es": "La luna ilumina la noche.", "en": "The moon illuminates the night."},
    {"es": "Él corre muy rápido en la pista.", "en": "He runs very fast on the track."},
    {"es": "El bebé duerme en su cuna.", "en": "The baby sleeps in his crib."},
    {"es": "Mi madre hornea galletas.", "en": "My mother bakes cookies."},
    {"es": "El gato maúlla en el tejado.", "en": "The cat meows on the roof."},
    {"es": "Ellas bailan en la fiesta.", "en": "They dance at the party."},
    {"es": "El doctor ayuda a la gente.", "en": "The doctor helps people."},
    {"es": "La flor florece en la primavera.", "en": "The flower blooms in the spring."},
    {"es": "El viento sopla fuerte.", "en": "The wind blows hard."}
]

class SentencePuzzleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("El Puzzle de la Oración")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.language = "es"
        self.score = 0
        self.current_exercise_index = 0
        self.correct_sentence = ""
        self.user_sentence = []

        self.create_widgets()
        self.load_exercise()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        self.title_label = tk.Label(main_frame, text="El Puzzle de la Oración 🧩", font=("Arial", 28, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        # Idioma
        self.lang_var = tk.StringVar(value="es")
        self.lang_frame = tk.Frame(main_frame, bg="#f0f0f0")
        self.lang_frame.pack(pady=5)
        self.lang_es = tk.Radiobutton(self.lang_frame, text="Español", variable=self.lang_var, value="es", bg="#f0f0f0", command=self.change_language)
        self.lang_en = tk.Radiobutton(self.lang_frame, text="English", variable=self.lang_var, value="en", bg="#f0f0f0", command=self.change_language)
        self.lang_es.pack(side="left", padx=10)
        self.lang_en.pack(side="left", padx=10)

        # Etiqueta de la oración desordenada
        self.instruction_label = tk.Label(main_frame, text="Haz clic en las palabras en el orden correcto:", font=("Arial", 16), bg="#f0f0f0", fg="#555")
        self.instruction_label.pack(pady=10)

        # Contenedor de palabras desordenadas
        self.word_frame = tk.Frame(main_frame, bg="#fff", bd=2, relief="groove")
        self.word_frame.pack(pady=10, ipadx=10, ipady=10)

        # Contenedor de la oración construida
        self.sentence_label = tk.Label(main_frame, text="", font=("Arial", 18, "bold"), bg="#fff", bd=2, relief="groove", wraplength=700)
        self.sentence_label.pack(pady=20, ipadx=10, ipady=10, fill="x")

        # Botones de control
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=10)

        self.check_button = tk.Button(button_frame, text="Verificar", command=self.check_sentence, font=("Arial", 14), bg="#4CAF50", fg="white", activebackground="#45a049")
        self.check_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(button_frame, text="Reiniciar", command=self.reset_words, font=("Arial", 14), bg="#f44336", fg="white", activebackground="#da190b")
        self.reset_button.pack(side="left", padx=10)

        self.score_label = tk.Label(main_frame, text=f"Puntaje: {self.score}", font=("Arial", 16), bg="#f0f0f0", fg="#333")
        self.score_label.pack(pady=10)

    def change_language(self):
        self.language = self.lang_var.get()
        self.score = 0
        self.current_exercise_index = 0
        self.user_sentence = []
        if self.language == "es":
            self.title_label.config(text="El Puzzle de la Oración 🧩")
            self.instruction_label.config(text="Haz clic en las palabras en el orden correcto:")
            self.check_button.config(text="Verificar")
            self.reset_button.config(text="Reiniciar")
        else:
            self.title_label.config(text="The Sentence Puzzle 🧩")
            self.instruction_label.config(text="Click the words in the correct order:")
            self.check_button.config(text="Check")
            self.reset_button.config(text="Reset")
        self.score_label.config(text=f"Puntaje: {self.score}" if self.language == "es" else f"Score: {self.score}")
        self.load_exercise()

    def load_exercise(self):
        if self.current_exercise_index >= len(EJERCICIOS):
            self.end_game()
            return

        self.user_sentence = []
        self.sentence_label.config(text="")
        
        # Limpiar el frame de palabras
        for widget in self.word_frame.winfo_children():
            widget.destroy()

        exercise = EJERCICIOS[self.current_exercise_index]
        self.correct_sentence = exercise[self.language]
        words = self.correct_sentence.split()
        random.shuffle(words)

        for word in words:
            btn = tk.Button(self.word_frame, text=word, font=("Arial", 14), bg="#e0e0e0", relief="raised", bd=2)
            btn.config(command=lambda w=word, b=btn: self.add_word(w, b))
            btn.pack(side="left", padx=5, pady=5)
    
    def add_word(self, word, button):
        self.user_sentence.append(word)
        self.sentence_label.config(text=" ".join(self.user_sentence))
        button.config(state="disabled") # Deshabilitar el botón

    def check_sentence(self):
        user_sentence_str = " ".join(self.user_sentence)
        if user_sentence_str == self.correct_sentence:
            if self.language == "es":
                messagebox.showinfo("¡Correcto! ✅", "¡Excelente! Has armado la oración correctamente.")
                self.score += 1
            else:
                messagebox.showinfo("Correct! ✅", "Excellent! You've built the sentence correctly.")
                self.score += 1
            self.score_label.config(text=f"Puntaje: {self.score}" if self.language == "es" else f"Score: {self.score}")
            self.current_exercise_index += 1
            self.load_exercise()
        else:
            if self.language == "es":
                messagebox.showerror("Incorrecto ❌", "La oración es incorrecta. Inténtalo de nuevo.")
            else:
                messagebox.showerror("Incorrect ❌", "The sentence is incorrect. Try again.")
            self.reset_words()

    def reset_words(self):
        self.user_sentence = []
        self.sentence_label.config(text="")
        # Habilitar todos los botones de palabras
        for widget in self.word_frame.winfo_children():
            widget.config(state="normal")
            
    def end_game(self):
        if self.language == "es":
            messagebox.showinfo("Fin del Juego 🎉", f"¡Has completado todos los ejercicios!\nTu puntaje final es: {self.score}")
        else:
            messagebox.showinfo("Game Over 🎉", f"You have completed all exercises!\nYour final score is: {self.score}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SentencePuzzleApp(root)
    root.mainloop()
