import tkinter as tk
from tkinter import ttk, messagebox, Canvas, Frame

# Mapa conceptual del ensayo en formato diccionario
mapa_conceptual = {
    "Gerundios": {
        "Tipos": {
            "Causal": "Indica causa (porque)\nEj: Lloviendo, cancelaron",
            "Concesivo": "Muestra contraste (aunque)\nEj: Siendo rico, vive humilde",
            "Condicional": "Establece condición (si)\nEj: Permitiéndolo Dios, viajaremos",
            "Auxiliares": "Con estar/ir/venir/andar\nEj: Estoy escribiendo"
        },
        "Reglas": {
            "Independencia": "No modifica sujeto/verbo/OD",
            "Puntuación": "Uso obligatorio de comas",
            "Ubicación": "Inicio, medio o final"
        }
    }
}

class AplicacionGerundios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Gerundios con Mapa Conceptual")
        self.geometry("1000x700")
        self.progreso = {"total": 0}
        self.crear_widgets()
        
    def crear_widgets(self):
        # Panel principal
        self.notebook = ttk.Notebook(self)
        
        # Pestaña de práctica
        self.pestana_practica = Frame(self.notebook)
        self.crear_panel_practica()
        
        # Pestaña de mapa conceptual
        self.pestana_mapa = Frame(self.notebook)
        self.dibujar_mapa()
        
        self.notebook.add(self.pestana_practica, text="Práctica")
        self.notebook.add(self.pestana_mapa, text="Mapa Conceptual")
        self.notebook.pack(expand=True, fill="both")

    def crear_panel_practica(self):
        # Controles de categoría
        frame_controles = Frame(self.pestana_practica)
        ttk.Label(frame_controles, text="Categoría:").pack(side=tk.LEFT)
        
        self.categoria = ttk.Combobox(frame_controles, 
                                    values=["Causal", "Concesivo", "Condicional", "Auxiliares"])
        self.categoria.pack(side=tk.LEFT, padx=10)
        self.categoria.bind("<<ComboboxSelected>>", self.mostrar_ejemplos)
        
        ttk.Button(frame_controles, text="Nueva Práctica", 
                 command=self.iniciar_practica).pack(side=tk.LEFT)
        frame_controles.pack(pady=10)
        
        # Área de ejemplos
        self.frame_ejemplos = Frame(self.pestana_practica)
        self.frame_ejemplos.pack(fill=tk.X)
        
        # Entrada de usuario
        self.frame_entrada = Frame(self.pestana_practica)
        ttk.Label(self.frame_entrada, text="Escribe tu oración:").pack()
        self.entrada = ttk.Entry(self.frame_entrada, width=60)
        self.entrada.pack(pady=5)
        ttk.Button(self.frame_entrada, text="Validar", 
                 command=self.validar_gerundio).pack()
        
        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(self.pestana_practica, 
                                            orient="horizontal",
                                            length=300, mode="determinate")
        self.barra_progreso.pack(pady=10)
        
        # Área de retroalimentación
        self.retro = ttk.Label(self.pestana_practica, 
                             foreground="blue",
                             wraplength=400)
        self.retro.pack()

    def dibujar_mapa(self):
        canvas = Canvas(self.pestana_mapa, bg="white")
        canvas.pack(fill="both", expand=True)
        
        # Nodos principales
        self.crear_nodo(canvas, "Gerundios", 500, 50, "#FFE4B5")
        self.crear_nodo(canvas, "Tipos", 300, 200, "#98FB98")
        self.crear_nodo(canvas, "Reglas", 700, 200, "#87CEEB")
        
        # Conexiones
        canvas.create_line(500, 100, 300, 170, arrow=tk.LAST)
        canvas.create_line(500, 100, 700, 170, arrow=tk.LAST)
        
        # Subtipos
        y = 300
        for subtipo in mapa_conceptual["Gerundios"]["Tipos"]:
            self.crear_nodo_sub(canvas, subtipo, 100, y, "#E6E6FA")
            canvas.create_line(300, 230, 150, y+20)
            y += 120
            
        y = 300
        for regla in mapa_conceptual["Gerundios"]["Reglas"]:
            self.crear_nodo_sub(canvas, regla, 800, y, "#FFF0F5")
            canvas.create_line(700, 230, 900, y+20)
            y += 100

    def crear_nodo(self, canvas, texto, x, y, color):
        canvas.create_rectangle(x-100, y-30, x+100, y+30, fill=color)
        canvas.create_text(x, y, text=texto, font=("Arial", 12, "bold"))

    def crear_nodo_sub(self, canvas, texto, x, y, color):
        canvas.create_oval(x-20, y-20, x+200, y+60, fill=color)
        canvas.create_text(x+90, y+20, text=texto, width=150)

    def mostrar_ejemplos(self, event=None):
        for widget in self.frame_ejemplos.winfo_children():
            widget.destroy()
            
        categoria = self.categoria.get().lower()
        ejemplos = {
            "causal": ["Lloviendo tanto, cancelaron...", "Habiendo estudiado, aprobó..."],
            "concesivo": ["Siendo rico, vive...", "Conociendo riesgos, lo intentó..."],
            "condicional": ["Permitiéndolo Dios...", "Consiguiendo boletos..."],
            "auxiliares": ["Estoy escribiendo...", "Vamos mejorando..."]
        }.get(categoria, [])
        
        for ejemplo in ejemplos:
            lbl = ttk.Label(self.frame_ejemplos, 
                          text=self.subrayar_gerundio(ejemplo),
                          foreground="gray")
            lbl.pack()

    def subrayar_gerundio(self, texto):
        palabras = texto.split()
        for i, palabra in enumerate(palabras):
            if palabra.endswith(('ando', 'iendo')):
                palabras[i] = f"[{palabra}]"
        return " ".join(palabras)

    def iniciar_practica(self):
        self.progreso[self.categoria.get().lower()] = 0
        self.actualizar_progreso()
        self.mostrar_ejemplos()

    def validar_gerundio(self):
        oracion = self.entrada.get()
        if any(palabra.endswith(('ando', 'iendo')) for palabra in oracion.split()):
            self.progreso["total"] += 1
            cat = self.categoria.get().lower()
            self.progreso[cat] = self.progreso.get(cat, 0) + 1
            
            self.retro.config(text=f"✓ Correcto: {self.subrayar_gerundio(oracion)}")
            self.entrada.delete(0, tk.END)
            self.actualizar_progreso()
            
            if self.progreso["total"] >= 100:
                messagebox.showinfo("¡Completado!", "Has alcanzado las 100 oraciones")
                self.destroy()
        else:
            self.retro.config(text="✗ Debes incluir un gerundio (-ando/-iendo)", 
                             foreground="red")

    def actualizar_progreso(self):
        total = self.progreso["total"]
        self.barra_progreso["value"] = total
        self.title(f"Práctica de Gerundios - Progreso: {total}/100")

if __name__ == "__main__":
    app = AplicacionGerundios()
    app.mainloop()
