import json
import random
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Clase principal de la aplicación
class ConditionalSentencesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprendizaje de Oraciones Condicionales")
        self.geometry("600x400")
        
        # Cargar datos
        self.conditional_sentences = self.load_data()
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, font=("Arial", 10))
        self.style.configure("TLabel", font=("Arial", 11))
        
        # Pantalla principal
        self.show_main_menu()

    def load_data(self):
        try:
            with open("progress.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return [
                {
                    "protasis": "Si (llover) mañana",
                    "apodosis": "cancelar el picnic.",
                    "correct_forms": {"protasis": "llueve", "apodosis": "cancelaremos"},
                    "next_review": None
                },
                # Añadir más ejemplos aquí
            ]

    def save_data(self):
        with open("progress.json", "w") as f:
            json.dump(self.conditional_sentences, f)

    def show_main_menu(self):
        self.clear_window()
        ttk.Label(self, text="¡Bienvenido al Tutor de Oraciones Condicionales!", style="TLabel").pack(pady=20)
        
        ttk.Button(self, text="Practicar", command=self.start_practice).pack(pady=10)
        ttk.Button(self, text="Ver Progreso", command=self.show_progress).pack(pady=10)
        ttk.Button(self, text="Salir", command=self.destroy).pack(pady=10)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def start_practice(self):
        self.clear_window()
        now = datetime.now()
        self.to_review = [s for s in self.conditional_sentences if not s["next_review"] or datetime.fromisoformat(s["next_review"]) <= now]
        
        if not self.to_review:
            messagebox.showinfo("¡Perfecto!", "Ya has repasado todo por hoy. 🎉")
            self.show_main_menu()
            return
        
        self.current_sentence = random.choice(self.to_review)
        self.show_question()

    def show_question(self):
        ttk.Label(self, text="Completa la oración condicional:", style="TLabel").pack(pady=10)
        
        # Protasis
        ttk.Label(self, text=f"Si {self.current_sentence['protasis']}", style="TLabel").pack(pady=5)
        self.protasis_entry = ttk.Entry(self, width=30)
        self.protasis_entry.pack(pady=5)
        
        # Apodosis
        ttk.Label(self, text=f"{self.current_sentence['apodosis']}", style="TLabel").pack(pady=5)
        self.apodosis_entry = ttk.Entry(self, width=30)
        self.apodosis_entry.pack(pady=5)
        
        # Botones
        ttk.Button(self, text="Comprobar", command=self.check_answer).pack(pady=20)
        ttk.Button(self, text="Volver al Menú", command=self.show_main_menu).pack(pady=5)

    def check_answer(self):
        user_protasis = self.protasis_entry.get().strip().lower()
        user_apodosis = self.apodosis_entry.get().strip().lower()
        correct = self.current_sentence["correct_forms"]
        
        if user_protasis == correct["protasis"] and user_apodosis == correct["apodosis"]:
            messagebox.showinfo("¡Correcto!", "Has acertado. ✅")
            self.update_review_date()
        else:
            messagebox.showerror("Incorrecto", 
                f"Respuesta correcta:\nProtasis: {correct['protasis']}\nApodosis: {correct['apodosis']}")
        
        self.start_practice()

    def update_review_date(self):
        if not self.current_sentence["next_review"]:
            delta = timedelta(days=1)
        else:
            delta = timedelta(days=2)
        
        self.current_sentence["next_review"] = (datetime.now() + delta).isoformat()
        self.save_data()

    def show_progress(self):
        reviewed = sum(1 for s in self.conditional_sentences if s["next_review"])
        total = len(self.conditional_sentences)
        messagebox.showinfo("Progreso", 
            f"Progreso actual:\nOraciones repasadas: {reviewed}/{total}\nPorcentaje: {reviewed/total:.0%}")

if __name__ == "__main__":
    app = ConditionalSentencesApp()
    app.mainloop()
