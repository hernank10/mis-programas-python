import tkinter as tk
from tkinter import ttk, messagebox
import random
import json

# --------------------------------------------
# DATOS Y REGLAS GRAMATICALES
# --------------------------------------------
reglas = {
    "acusativo": {
        "pronombres": ["me", "te", "lo", "la", "nos", "os", "los", "las"],
        "ejemplos": [
            ("___ vi en el espejo (a mí)", "me"),
            ("¿___ llamaron a ti?", "te"),
            ("Ellos ___ miraron (a ustedes)", "los"),
        ]
    },
    "dativo": {
        "pronombres": ["me", "te", "le", "nos", "os", "les"],
        "ejemplos": [
            ("El profesor ___ dio el libro (a mí)", "me"),
            ("___ escribí una carta (a ti)", "te"),
            ("___ entregamos los documentos (a ellos)", "les"),
        ]
    }
}

# --------------------------------------------
# CLASE PRINCIPAL DE LA APLICACIÓN
# --------------------------------------------
class AplicacionPractica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Pronombres Acusativo/Dativo")
        self.geometry("800x600")
        self.puntuacion = 0
        self.ejercicio_actual = None
        self.categoria_actual = None
        
        self.configurar_interfaz()
        self.cargar_recursos()
    
    def configurar_interfaz(self):
        # Frame superior para controles
        frame_controles = ttk.Frame(self, padding=10)
        frame_controles.pack(fill=tk.X)
        
        # Selector de categoría
        self.combo_categorias = ttk.Combobox(frame_controles, values=list(reglas.keys()))
        self.combo_categorias.set("Selecciona categoría")
        self.combo_categorias.pack(side=tk.LEFT, padx=5)
        
        # Botones
        ttk.Button(frame_controles, text="Nuevo Ejercicio", command=self.nuevo_ejercicio).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_controles, text="Mostrar Puntuación", command=self.mostrar_puntuacion).pack(side=tk.LEFT)
        
        # Área de ejercicio
        self.frame_ejercicio = ttk.Frame(self, padding=20)
        self.frame_ejercicio.pack(fill=tk.BOTH, expand=True)
        
        self.lbl_instruccion = ttk.Label(self.frame_ejercicio, text="", font=('Arial', 14))
        self.lbl_instruccion.pack(pady=10)
        
        self.lbl_ejercicio = ttk.Label(self.frame_ejercicio, text="", font=('Arial', 16, 'bold'))
        self.lbl_ejercicio.pack(pady=20)
        
        self.entrada_respuesta = ttk.Entry(self.frame_ejercicio, width=30, font=('Arial', 14))
        self.entrada_respuesta.pack(pady=10)
        
        ttk.Button(self.frame_ejercicio, text="Verificar", command=self.verificar_respuesta).pack(pady=10)
        
        self.lbl_feedback = ttk.Label(self.frame_ejercicio, text="", font=('Arial', 12))
        self.lbl_feedback.pack(pady=10)
        
        # Panel de estadísticas
        self.lbl_puntuacion = ttk.Label(self.frame_ejercicio, text="Puntuación: 0", font=('Arial', 12))
        self.lbl_puntuacion.pack(side=tk.BOTTOM, pady=10)
    
    def cargar_recursos(self):
        try:
            with open('reglas.json', 'r') as f:
                self.reglas = json.load(f)
        except FileNotFoundError:
            self.reglas = reglas
    
    def nuevo_ejercicio(self):
        self.categoria_actual = self.combo_categorias.get()
        if self.categoria_actual not in reglas:
            messagebox.showwarning("Error", "¡Selecciona una categoría válida!")
            return
        
        ejercicios = reglas[self.categoria_actual]["ejemplos"]
        self.ejercicio_actual = random.choice(ejercicios)
        
        self.lbl_instruccion.config(text=f"Categoría: {self.categoria_actual.capitalize()}")
        self.lbl_ejercicio.config(text=self.ejercicio_actual[0])
        self.entrada_respuesta.delete(0, tk.END)
        self.lbl_feedback.config(text="")
    
    def verificar_respuesta(self):
        if not self.ejercicio_actual:
            return
        
        respuesta = self.entrada_respuesta.get().strip().lower()
        correcta = self.ejercicio_actual[1]
        
        if respuesta == correcta:
            self.puntuacion += 10
            feedback = f"✅ Correcto! +10 puntos\nRegla: {self.obtener_explicacion()}"
            color = "darkgreen"
        else:
            self.puntuacion = max(0, self.puntuacion - 5)
            feedback = f"❌ Incorrecto. La respuesta correcta es: {correcta}\n{self.obtener_explicacion()}"
            color = "darkred"
        
        self.lbl_feedback.config(text=feedback, foreground=color)
        self.lbl_puntuacion.config(text=f"Puntuación: {self.puntuacion}")
        self.after(2000, self.nuevo_ejercicio)
    
    def obtener_explicacion(self):
        pronombre = self.ejercicio_actual[1]
        for categoria, datos in reglas.items():
            if pronombre in datos["pronombres"]:
                return f"El pronombre '{pronombre}' es {categoria.upper()}"
        return "Regla gramatical aplicada"
    
    def mostrar_puntuacion(self):
        messagebox.showinfo("Puntuación", f"Puntuación actual: {self.puntuacion}\n\nSigue practicando!")

# --------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# --------------------------------------------
if __name__ == "__main__":
    app = AplicacionPractica()
    app.mainloop()
