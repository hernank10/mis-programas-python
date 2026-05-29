import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime

# Configuración global
ARCHIVO_DATOS = "frases_teoria.json"
MAX_FRASES = 100
CATEGORIAS = {
    "Simplifica": {
        "regla": "Elimina palabras redundantes, manteniendo el núcleo de la idea",
        "ejemplos": [
            "En lugar de: 'El camino de la vida está lleno de obstáculos que debemos superar'\nUsa: 'La vida es un camino de obstáculos'",
            "En lugar de: 'La lluvia cae suavemente desde el cielo gris'\nUsa: 'La lluvia acaricia el cemento'"
        ]
    },
    "Metáforas": {
        "regla": "Relaciona conceptos abstractos con imágenes concretas y evocadoras",
        "ejemplos": [
            "El tiempo es un ladrón silencioso",
            "La esperanza es la última semilla en invierno"
        ]
    },
    "Contrastes": {
        "regla": "Juega con opuestos para crear profundidad y tensión conceptual",
        "ejemplos": [
            "La luz más brillante nace de la oscuridad más profunda",
            "El silencio grita más fuerte que las palabras"
        ]
    },
    "Verbos Activos": {
        "regla": "Usa verbos dinámicos que impulsen la acción y la visualización",
        "ejemplos": [
            "Construye puentes, no muros",
            "Planta ideas, cosecha revoluciones"
        ]
    },
    "Experiencia Universal": {
        "regla": "Apela a emociones y vivencias compartidas por la mayoría",
        "ejemplos": [
            "El amor madura en los detalles pequeños",
            "Nadie llora con la primera arruga, pero todos con la última"
        ]
    }
}

TEORIA_BASE = """**Regla de construcción filosófica:**
Las grandes frases trascienden cuando:
1. Contienen una verdad universal
2. Usan lenguaje evocador
3. Equilibran profundidad y brevedad
4. Permiten múltiples interpretaciones
5. Generan resonancia emocional

**Consejo clave:** "Lo bueno se explica, lo genial se intuye" """

class FrasesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taller de Frases Filosóficas")
        self.root.geometry("1100x700")
        
        self.datos = self.cargar_datos()
        self.crear_widgets()
        self.centrar_ventana()
    
    def centrar_ventana(self):
        self.root.update_idletasks()
        ancho = self.root.winfo_width()
        alto = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    def cargar_datos(self):
        try:
            with open(ARCHIVO_DATOS, "r") as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {categoria: [] for categoria in CATEGORIAS}
    
    def guardar_datos(self):
        with open(ARCHIVO_DATOS, "w") as archivo:
            json.dump(self.datos, archivo, indent=2)
    
    def crear_widgets(self):
        # Panel principal
        main_panel = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_panel.pack(fill=tk.BOTH, expand=True)
        
        # Panel izquierdo (creación)
        left_frame = ttk.Frame(main_panel, width=600)
        main_panel.add(left_frame)
        
        # Panel derecho (teoría y ejemplos)
        right_frame = ttk.Frame(main_panel, width=400)
        main_panel.add(right_frame)
        
        # Componentes panel izquierdo
        self.crear_panel_creacion(left_frame)
        
        # Componentes panel derecho
        self.crear_panel_teoria(right_frame)
    
    def crear_panel_creacion(self, parent):
        # Selector de categoría
        ttk.Label(parent, text="Categoría:", font=('Arial', 12, 'bold')).pack(pady=10, anchor=tk.W)
        
        self.categoria_var = tk.StringVar()
        for categoria in CATEGORIAS:
            rb = ttk.Radiobutton(
                parent,
                text=categoria,
                variable=self.categoria_var,
                value=categoria,
                command=self.actualizar_teoria
            )
            rb.pack(anchor=tk.W, padx=20, pady=2)
        
        # Entrada de frase
        ttk.Label(parent, text="Escribe tu frase:", font=('Arial', 12, 'bold')).pack(pady=10, anchor=tk.W)
        self.txt_frase = scrolledtext.ScrolledText(parent, width=60, height=6, font=('Arial', 11))
        self.txt_frase.pack(padx=20, pady=5)
        
        # Contador y botones
        bottom_frame = ttk.Frame(parent)
        bottom_frame.pack(fill=tk.X, pady=15)
        
        self.contador_var = tk.StringVar(value="Palabras: 0/12")
        ttk.Label(bottom_frame, textvariable=self.contador_var).pack(side=tk.LEFT, padx=20)
        
        btn_frame = ttk.Frame(bottom_frame)
        btn_frame.pack(side=tk.RIGHT)
        ttk.Button(btn_frame, text="Guardar", command=self.guardar_frase).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Ver Frases", command=self.mostrar_frases).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        # Eventos
        self.txt_frase.bind("<KeyRelease>", self.actualizar_contador)
    
    def crear_panel_teoria(self, parent):
        # Teoría general
        teoria_frame = ttk.LabelFrame(parent, text="Teoría Fundamental", padding=15)
        teoria_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.teoria_text = tk.Text(teoria_frame, wrap=tk.WORD, width=45, height=12, 
                                font=('Arial', 10), bg='#F0F0F0')
        self.teoria_text.insert(tk.END, TEORIA_BASE)
        self.teoria_text.config(state=tk.DISABLED)
        self.teoria_text.pack(fill=tk.BOTH, expand=True)
        
        # Ejemplos específicos
        ejemplo_frame = ttk.LabelFrame(parent, text="Regla y Ejemplos", padding=15)
        ejemplo_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.regla_var = tk.StringVar()
        ttk.Label(ejemplo_frame, textvariable=self.regla_var, wraplength=350, 
                font=('Arial', 10, 'italic')).pack(anchor=tk.W)
        
        self.ejemplo_list = tk.Listbox(ejemplo_frame, width=45, height=6, 
                                    font=('Courier New', 10), selectbackground='#E0E0E0')
        scrollbar = ttk.Scrollbar(ejemplo_frame, orient=tk.VERTICAL, command=self.ejemplo_list.yview)
        self.ejemplo_list.configure(yscrollcommand=scrollbar.set)
        
        self.ejemplo_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Cargar datos iniciales
        self.actualizar_teoria()
    
    def actualizar_teoria(self):
        categoria = self.categoria_var.get()
        if categoria:
            info = CATEGORIAS[categoria]
            self.regla_var.set(f"Regla: {info['regla']}")
            
            self.ejemplo_list.delete(0, tk.END)
            for ejemplo in info['ejemplos']:
                self.ejemplo_list.insert(tk.END, ejemplo)
        else:
            self.regla_var.set("Selecciona una categoría para ver su regla específica")
            self.ejemplo_list.delete(0, tk.END)
    
    # ... (Mantener los métodos restantes iguales que en la versión anterior) ...

if __name__ == "__main__":
    root = tk.Tk()
    app = FrasesApp(root)
    root.mainloop()
