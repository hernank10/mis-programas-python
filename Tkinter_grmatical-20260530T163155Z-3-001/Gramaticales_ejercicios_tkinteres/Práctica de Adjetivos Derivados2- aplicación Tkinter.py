import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import datetime
import random

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Practicador de Adjetivos Derivados")
        self.geometry("800x600")
        
        # Base de datos
        self.adjetivos = [
            {"adjetivo": "aceitoso", "base": "aceite", "sufijo": "-oso", "dificultad": "Fácil"},
            {"adjetivo": "aceitoso", "base": "aceite", "sufijo": "-oso", "dificultad": "Fácil"},
            {"adjetivo": "aceitoso", "base": "aceite", "sufijo": "-oso", "dificultad": "Fácil"},
            {"adjetivo": "aceitoso", "base": "aceite", "sufijo": "-oso", "dificultad": "Fácil"},
            {"adjetivo": "aceitoso", "base": "aceite", "sufijo": "-oso", "dificultad": "Fácil"},
            {"adjetivo": "aceitoso", "base": "aceite", "sufijo": "-oso", "dificultad": "Fácil"},
            {"adjetivo": "aceitoso", "base": "aceite", "sufijo": "-oso", "dificultad": "Fácil"},
            
            # ... (agregar los demás adjetivos)
        ]
        
        # Configurar interfaz
        self.create_widgets()
        
    def create_widgets(self):
        # Notebook para pestañas
        self.notebook = ttk.Notebook(self)
        
        # Pestañas
        self.home_frame = HomeFrame(self.notebook, self)
        self.ejemplos_frame = ExamplesFrame(self.notebook, self)
        self.practica_frame = PracticeFrame(self.notebook, self)
        self.resultados_frame = ResultsFrame(self.notebook, self)
        
        self.notebook.add(self.home_frame, text="🏠 Inicio")
        self.notebook.add(self.ejemplos_frame, text="📚 Ejemplos")
        self.notebook.add(self.practica_frame, text="✍️ Practicar")
        self.notebook.add(self.resultados_frame, text="🏆 Resultados")
        
        self.notebook.pack(expand=True, fill="both")

class HomeFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ttk.Label(self, text="¡Bienvenido al Practicador!", font=("Arial", 16)).pack(pady=20)
        
        ttk.Label(self, text="Características principales:", font=("Arial", 12)).pack(pady=10)
        ttk.Label(self, text="• 3 niveles de dificultad\n• Sistema de puntuación\n• Registro de resultados").pack()

class ExamplesFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        # Filtro de dificultad
        ttk.Label(self, text="Filtrar por dificultad:").grid(row=0, column=0, padx=5, pady=5)
        self.dificultad = ttk.Combobox(self, values=["Todos", "Fácil", "Medio", "Difícil"])
        self.dificultad.current(0)
        self.dificultad.grid(row=0, column=1, padx=5, pady=5)
        self.dificultad.bind("<<ComboboxSelected>>", self.actualizar_tabla)
        
        # Tabla de ejemplos
        self.tree = ttk.Treeview(self, columns=("Adjetivo", "Base", "Sufijo", "Dificultad"), show="headings")
        self.tree.heading("Adjetivo", text="Adjetivo")
        self.tree.heading("Base", text="Base")
        self.tree.heading("Sufijo", text="Sufijo")
        self.tree.heading("Dificultad", text="Dificultad")
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.actualizar_tabla()
    
    def actualizar_tabla(self, event=None):
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        filtro = self.dificultad.get()
        for adj in self.controller.adjetivos:
            if filtro == "Todos" or adj["dificultad"] == filtro:
                self.tree.insert("", "end", values=(
                    adj["adjetivo"].capitalize(),
                    adj["base"].capitalize(),
                    adj["sufijo"],
                    adj["dificultad"]
                ))

class PracticeFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.current_question = 0
        self.score = 0
        self.create_widgets()
    
    def create_widgets(self):
        # Selección de dificultad
        ttk.Label(self, text="Selecciona nivel:").grid(row=0, column=0, padx=5, pady=5)
        self.dificultad = ttk.Combobox(self, values=["Fácil", "Medio", "Difícil"])
        self.dificultad.current(0)
        self.dificultad.grid(row=0, column=1, padx=5, pady=5)
        
        # Botón de inicio
        ttk.Button(self, text="Comenzar prueba", command=self.iniciar_prueba).grid(row=0, column=2, padx=10)
        
        # Area de preguntas
        self.question_frame = ttk.Frame(self)
        self.lbl_pregunta = ttk.Label(self.question_frame, text="", font=("Arial", 12))
        self.lbl_pregunta.pack(pady=10)
        
        self.entrada_respuesta = ttk.Entry(self.question_frame, width=20)
        self.entrada_respuesta.pack(pady=5)
        
        self.btn_verificar = ttk.Button(self.question_frame, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=10)
        
        self.lbl_puntaje = ttk.Label(self, text="Puntaje: 0", font=("Arial", 12))
    
    def iniciar_prueba(self):
        self.questions = self.filtrar_preguntas()
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        self.mostrar_pregunta()
        self.question_frame.grid(row=1, column=0, columnspan=3, pady=20)
        self.lbl_puntaje.grid(row=2, column=0, columnspan=3)
    
    def filtrar_preguntas(self):
        nivel = self.dificultad.get()
        if nivel == "Fácil":
            return [q for q in self.controller.adjetivos if q["dificultad"] in ["Fácil", "Medio"]]
        elif nivel == "Medio":
            return [q for q in self.controller.adjetivos if q["dificultad"] == "Medio"]
        return self.controller.adjetivos
    
    def mostrar_pregunta(self):
        if self.current_question < len(self.questions):
            pregunta = self.questions[self.current_question]
            self.lbl_pregunta.config(
                text=f"Pregunta {self.current_question + 1}:\nBase: {pregunta['base'].capitalize()}\nForma el adjetivo: {pregunta['base']} + ____ = {pregunta['adjetivo']}"
            )
            self.entrada_respuesta.delete(0, tk.END)
        else:
            self.guardar_resultado()
            messagebox.showinfo("Prueba finalizada", f"Puntaje final: {self.score}/{len(self.questions)}")
            self.question_frame.grid_forget()
            self.lbl_puntaje.grid_forget()
    
    def verificar_respuesta(self):
        pregunta = self.questions[self.current_question]
        respuesta = self.entrada_respuesta.get().strip().lower()
        sufijo_correcto = pregunta["sufijo"].replace("-", "")
        
        if respuesta == sufijo_correcto:
            self.score += 1
            messagebox.showinfo("Resultado", "✅ Correcto!")
        else:
            messagebox.showerror("Resultado", f"❌ Incorrecto. La respuesta era: {pregunta['sufijo']}")
        
        self.current_question += 1
        self.lbl_puntaje.config(text=f"Puntaje: {self.score}")
        self.mostrar_pregunta()
    
    def guardar_resultado(self):
        nombre = simpledialog.askstring("Guardar resultado", "Ingresa tu nombre:")
        if nombre:
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("resultados.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([fecha, nombre, self.score, self.dificultad.get()])

class ResultsFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        # Botones
        ttk.Button(self, text="Actualizar", command=self.actualizar_tabla).pack(pady=5)
        ttk.Button(self, text="Exportar", command=self.exportar_resultados).pack(pady=5)
        
        # Tabla de resultados
        self.tree = ttk.Treeview(self, columns=("Fecha", "Nombre", "Puntaje", "Nivel"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Puntaje", text="Puntaje")
        self.tree.heading("Nivel", text="Nivel")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.actualizar_tabla()
    
    def actualizar_tabla(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        try:
            with open("resultados.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    self.tree.insert("", "end", values=row)
        except FileNotFoundError:
            messagebox.showwarning("Error", "No hay resultados registrados aún")
    
    def exportar_resultados(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )
        if file_path:
            try:
                with open("resultados.csv", "r") as source, open(file_path, "w") as target:
                    target.write(source.read())
                messagebox.showinfo("Éxito", "Resultados exportados correctamente")
            except:
                messagebox.showerror("Error", "No se pudo exportar los resultados")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
