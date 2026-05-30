import json
import tkinter as tk
from tkinter import ttk, messagebox

# Estructura de datos con teoría y ejercicios (ampliable)
ejemplos = [
    {
        "categoria": "Prefijos",
        "teoria": "Confusión entre 'ante-' (anterioridad) y 'anti-' (oposición).",
        "ejemplos_buenos": [
            "antediluviano (anterior al diluvio)",
            "antiguerrilla (contra la guerrilla)"
        ],
        "ejercicio": {
            "tipo": "corrección",
            "pregunta": "Corrige la palabra: 'antidiluviano' (si se refiere a algo muy antiguo)",
            "respuesta": "antediluviano"
        }
    },
    {
        "categoria": "Verbología",
        "teoria": "'Debe' (obligación) vs. 'debe de' (probabilidad).",
        "ejemplos_buenos": [
            "Debe estudiar (obligación)",
            "Debe de estar lloviendo (suposición)"
        ],
        "ejercicio": {
            "tipo": "completar",
            "pregunta": "Completa: 'Él ______ haber llegado tarde por el tráfico.'",
            "respuesta": "debe de"
        }
    },
    # Añadir más ejemplos aquí...
]

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Palabra Precisa - Tutor Interactivo")
        self.geometry("800x600")
        
        self.usuario = None
        self.progreso = {"ejemplo_actual": 0, "correctas": 0}
        self.ejemplo_actual = None
        
        self.crear_widgets_login()
    
    def crear_widgets_login(self):
        # Frame de inicio de sesión
        self.frame_login = ttk.Frame(self)
        self.frame_login.pack(pady=100)
        
        ttk.Label(self.frame_login, text="Nombre de usuario:").pack(pady=5)
        self.entry_usuario = ttk.Entry(self.frame_login, width=30)
        self.entry_usuario.pack(pady=5)
        
        ttk.Button(
            self.frame_login, 
            text="Comenzar", 
            command=self.cargar_progreso
        ).pack(pady=10)
    
    def cargar_progreso(self):
        self.usuario = self.entry_usuario.get()
        try:
            with open(f'progreso_{self.usuario}.json', 'r') as f:
                self.progreso = json.load(f)
        except FileNotFoundError:
            self.progreso = {"ejemplo_actual": 0, "correctas": 0}
        
        self.frame_login.destroy()
        self.crear_widgets_principal()
    
    def crear_widgets_principal(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(
            self.frame_principal, 
            orient=tk.HORIZONTAL, 
            length=400,
            mode='determinate'
        )
        self.barra_progreso.pack(pady=10)
        
        # Contenedor de contenido
        self.frame_contenido = ttk.Frame(self.frame_principal)
        self.frame_contenido = self.frame_contenido  # Corregir nombre de variable
        self.frame_contenido.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.mostrar_ejemplo()
    
    def mostrar_ejemplo(self):
        # Limpiar frame anterior
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()
        
        # Actualizar barra de progreso
        total = len(ejemplos)
        self.barra_progreso['value'] = (self.progreso["ejemplo_actual"] / total) * 100
        
        # Obtener ejemplo actual
        self.ejemplo_actual = ejemplos[self.progreso["ejemplo_actual"]]
        
        # Mostrar teoría
        ttk.Label(
            self.frame_contenido, 
            text=f"Categoría: {self.ejemplo_actual['categoria']}",
            font=('Arial', 14, 'bold')
        ).pack(pady=5, anchor=tk.W)
        
        ttk.Label(
            self.frame_contenido,  # Debe ser self.frame_contenido
            text="Teoría:",
            font=('Arial', 12, 'underline')
        ).pack(pady=5, anchor=tk.W)
        
        ttk.Label(
            self.frame_contenido,
            text=self.ejemplo_actual['teoria'],
            wraplength=700
        ).pack(pady=5, anchor=tk.W)
        
        # Mostrar ejemplos buenos
        ttk.Label(
            self.frame_contenido,
            text="Ejemplos correctos:",
            font=('Arial', 12, 'underline')
        ).pack(pady=5, anchor=tk.W)
        
        for ejemplo in self.ejemplo_actual['ejemplos_buenos']:
            ttk.Label(
                self.frame_contenido,
                text=f"- {ejemplo}",
                wraplength=700
            ).pack(pady=2, anchor=tk.W)
        
        # Mostrar ejercicio
        ttk.Label(
            self.frame_contenido,
            text="\nEjercicio:",
            font=('Arial', 12, 'underline')
        ).pack(pady=10, anchor=tk.W)
        
        ttk.Label(
            self.frame_contenido,
            text=self.ejemplo_actual['ejercicio']['pregunta'],
            wraplength=700
        ).pack(pady=5, anchor=tk.W)
        
        # Campo de respuesta
        self.entry_respuesta = ttk.Entry(self.frame_contenido, width=50)
        self.entry_respuesta.pack(pady=10)
        
        # Botón de verificación
        ttk.Button(
            self.frame_contenido,
            text="Verificar respuesta",
            command=self.verificar_respuesta
        ).pack(pady=10)
    
    def verificar_respuesta(self):  # Corregir nombre del método a verificar_respuesta
        respuesta_usuario = self.entry_respuesta.get().strip().lower()
        respuesta_correcta = self.ejemplo_actual['ejercicio']['respuesta'].lower()
        
        if respuesta_usuario == respuesta_correcta:
            self.progreso["correctas"] += 1
            messagebox.showinfo("Resultado", "✅ ¡Respuesta correcta!")
        else:
            messagebox.showerror(
                "Resultado", 
                f"❌ Incorrecto. La respuesta correcta es:\n{respuesta_correcta}"
            )
        
        self.progreso["ejemplo_actual"] += 1
        self.guardar_progreso()
        
        if self.progreso["ejemplo_actual"] < len(ejemplos):
            self.mostrar_ejemplo()
        else:
            self.mostrar_resultado_final()
    
    def guardar_progreso(self):
        with open(f'progreso_{self.usuario}.json', 'w') as f:
            json.dump(self.progreso, f)
    
    def mostrar_resultado_final(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()
        
        ttk.Label(
            self.frame_contenido,
            text="¡Curso completado! 🎉",
            font=('Arial', 16, 'bold')
        ).pack(pady=20)
        
        ttk.Label(
            self.frame_contenido,
            text=f"Puntuación final: {self.progreso['correctas']}/{len(ejemplos)}",
            font=('Arial', 14)
        ).pack(pady=10)
        
        ttk.Button(
            self.frame_contenido,
            text="Salir",
            command=self.destroy
        ).pack(pady=20)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
