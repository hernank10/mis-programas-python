# -*- coding: utf-8 -*-
import json
import random
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

class SpanishConstructorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Construcciones Españolas")
        self.root.geometry("800x600")
        self.progress_file = Path("spanish_progress.json")
        self.progress = self.load_progress()
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#F0F0F0')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('Title.TLabel', font=('Arial', 14, 'bold'), background='#F0F0F0')
        self.style.configure('Theory.TLabel', font=('Arial', 11), background='#F0F0F0')
        
        # Crear widgets
        self.create_widgets()
        self.load_progress()
        
        # Cargar datos
        self.constructions = self.load_constructions()
        self.sustantivos = self.load_sustantivos()
        
    def create_widgets(self):
        # Marco principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo (menú)
        self.left_panel = ttk.Frame(self.main_frame, width=200)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Panel derecho (contenido)
        self.right_panel = ttk.Frame(self.main_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Widgets del panel izquierdo
        ttk.Label(self.left_panel, text="Menú", style='Title.TLabel').pack(pady=10)
        self.construccion_var = tk.IntVar(value=1)
        for i in range(1, 4):
            ttk.Radiobutton(
                self.left_panel, 
                text=f"Construcción {i}", 
                variable=self.construccion_var, 
                value=i,
                command=self.update_content
            ).pack(anchor=tk.W, pady=2)
        
        ttk.Button(
            self.left_panel, 
            text="Ver Progreso", 
            command=self.show_progress
        ).pack(pady=10, fill=tk.X)
        
        ttk.Button(
            self.left_panel, 
            text="Salir", 
            command=self.root.destroy
        ).pack(side=tk.BOTTOM, pady=10, fill=tk.X)
        
        # Widgets del panel derecho
        self.content_frame = ttk.Frame(self.right_panel)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Teoría y ejemplos
        self.theory_label = ttk.Label(self.content_frame, style='Title.TLabel')
        self.theory_label.pack(pady=5, anchor=tk.W)
        
        self.examples_text = tk.Text(
            self.content_frame, 
            height=5, 
            width=60,
            font=('Arial', 10),
            wrap=tk.WORD
        )
        self.examples_text.pack(pady=5, fill=tk.X)
        
        # Ejercicio
        self.exercise_frame = ttk.Frame(self.content_frame)
        self.exercise_frame.pack(pady=20, fill=tk.X)
        
        ttk.Label(self.exercise_frame, text="Ejercicio Actual:", style='Theory.TLabel').pack(anchor=tk.W)
        self.current_exercise = ttk.Label(self.exercise_frame, font=('Arial', 12), background='#FFFFFF')
        self.current_exercise.pack(fill=tk.X, pady=5)
        
        self.answer_entry = ttk.Entry(self.content_frame, font=('Arial', 12))
        self.answer_entry.pack(fill=tk.X, pady=5)
        self.answer_entry.bind("<Return>", self.check_answer)
        
        ttk.Button(
            self.content_frame, 
            text="Comprobar Respuesta", 
            command=self.check_answer
        ).pack(pady=10)
        
        # Feedback
        self.feedback_label = ttk.Label(self.content_frame, font=('Arial', 12))
        self.feedback_label.pack(pady=10)
        
        self.update_content()
        
    def load_constructions(self):
        return {
            1: {
                'name': "Artículo indefinido + sustantivo + posesivo",
                'theory': "Estructura: [un/una/unos/unas] + [sustantivo] + [posesivo pospuesto]\n\nEj: 'Un libro tuyo' en lugar de 'uno de tus libros'",
                'examples': [
                    "Un libro tuyo", "Una idea suya", "Unos colegas nuestros",
                    "Unas dudas mías", "Un profesor suyo", "Una amiga mía"
                ]
            },
            # ... (agregar otras construcciones similares)
        }
    
    def load_sustantivos(self):
        return [
            {'palabra': 'amigo', 'genero': 'm', 'plural': 'amigos'},
            {'palabra': 'idea', 'genero': 'f', 'plural': 'ideas'},
            {'palabra': 'libro', 'genero': 'm', 'plural': 'libros'},
        ]
    
    def load_progress(self):
        try:
            if self.progress_file.exists():
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {'intentos': 0, 'aciertos': 0, 'construcciones': {}}
        except Exception as e:
            messagebox.showerror("Error", f"Error cargando progreso: {str(e)}")
            return {'intentos': 0, 'aciertos': 0, 'construcciones': {}}

    def save_progress(self):
        try:
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error", f"Error guardando progreso: {str(e)}")

    def update_content(self):
        construccion_id = self.construccion_var.get()
        construccion = self.constructions[construccion_id]
        
        self.theory_label.config(text=construccion['name'])
        self.examples_text.config(state=tk.NORMAL)
        self.examples_text.delete(1.0, tk.END)
        self.examples_text.insert(tk.END, f"Teoría:\n{construccion['theory']}\n\nEjemplos:\n" + 
                                 "\n".join(f"- {ej}" for ej in construccion['examples']))
        self.examples_text.config(state=tk.DISABLED)
        
        self.generate_new_exercise()

    def generate_new_exercise(self):
        construccion_id = self.construccion_var.get()
        construccion = self.constructions[construccion_id]
        
        # Lógica de generación de ejercicio similar a la versión anterior
        # ... (implementar según la lógica previa)
        
        ejercicio_ejemplo = "Un libro tuyo"  # Ejemplo temporal
        self.current_exercise.config(text=ejercicio_ejemplo)
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self, event=None):
        respuesta = self.answer_entry.get().strip()
        respuesta_correcta = self.current_exercise.cget("text")
        
        # Lógica de corrección
        correcto = respuesta.lower() == respuesta_correcta.lower()
        
        # Actualizar progreso
        self.progress['intentos'] += 1
        if correcto:
            self.progress['aciertos'] += 1
            self.feedback_label.config(text="✅ ¡Respuesta Correcta!", foreground='green')
        else:
            self.feedback_label.config(text=f"❌ Correcto: {respuesta_correcta}", foreground='red')
        
        self.save_progress()
        self.root.after(2000, self.generate_new_exercise)

    def show_progress(self):
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Tu Progreso")
        
        ttk.Label(progress_window, text="Estadísticas de Aprendizaje", style='Title.TLabel').pack(pady=10)
        
        stats = [
            f"Intentos totales: {self.progress['intentos']}",
            f"Aciertos totales: {self.progress['aciertos']}",
            f"Tasa de éxito: {self.progress['aciertos']/self.progress['intentos']*100:.1f}%" 
            if self.progress['intentos'] > 0 else ""
        ]
        
        for stat in stats:
            ttk.Label(progress_window, text=stat).pack(anchor=tk.W, padx=20, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpanishConstructorGUI(root)
    root.mainloop()
