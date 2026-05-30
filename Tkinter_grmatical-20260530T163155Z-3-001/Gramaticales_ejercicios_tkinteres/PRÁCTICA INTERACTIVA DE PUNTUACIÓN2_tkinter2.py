import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import random

class GramaticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica Interactiva de Gramática")
        self.root.geometry("1000x700")
        
        # Configuración inicial
        self.MAX_EJEMPLOS = 100
        self.ARCHIVO_EJEMPLOS = "ejemplos_personalizados.json"
        self.puntuacion = {"aciertos": 0, "errores": 0}
        self.cargar_datos()
        
        # Estilo
        self.estilo = ttk.Style()
        self.estilo.configure('TFrame', background='#F0F0F0')
        self.estilo.configure('TButton', font=('Arial', 10), padding=5)
        self.estilo.configure('TLabel', background='#F0F0F0', font=('Arial', 11))
        
        # Contenedor principal
        self.main_container = ttk.Frame(root)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Barra de navegación
        self.crear_barra_navegacion()
        
        # Frame actual
        self.current_frame = None
        self.mostrar_menu_principal()

    def cargar_datos(self):
        try:
            with open('base_conocimiento.json') as f:
                self.base_conocimiento = json.load(f)
            with open(self.ARCHIVO_EJEMPLOS) as f:
                self.ejemplos_personalizados = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivos de datos no encontrados")
            self.root.destroy()

    def crear_barra_navegacion(self):
        nav_frame = ttk.Frame(self.main_container)
        nav_frame.pack(fill=tk.X, padx=10, pady=5)
        
        btn_menu = ttk.Button(nav_frame, text="Menú Principal", command=self.mostrar_menu_principal)
        btn_menu.pack(side=tk.LEFT, padx=5)
        
        btn_puntaje = ttk.Button(nav_frame, text=f"Aciertos: {self.puntuacion['aciertos']} | Errores: {self.puntuacion['errores']}", 
                               command=self.mostrar_puntaje)
        btn_puntaje.pack(side=tk.RIGHT, padx=5)

    def mostrar_menu_principal(self):
        self.limpiar_frame()
        frame = ttk.Frame(self.main_container)
        frame.pack(pady=50, fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="PRÁCTICA DE GRAMÁTICA", font=('Arial', 16, 'bold')).pack(pady=20)
        
        categorias = [
            ("Punto y coma", self.mostrar_teoria_practica),
            ("Comillas", self.mostrar_teoria_practica),
            ("Signos de Interrogación/Exclamación", self.mostrar_teoria_practica),
            ("Dos puntos", self.mostrar_teoria_practica),
            ("Crear Ejemplos", self.mostrar_crear_ejemplo),
            ("Práctica General", self.iniciar_practica_general)
        ]
        
        for texto, comando in categorias:
            btn = ttk.Button(frame, text=texto, command=lambda c=texto: comando(c))
            btn.pack(pady=5, fill=tk.X, padx=100)

    def mostrar_teoria_practica(self, categoria):
        self.limpiar_frame()
        frame = ttk.Frame(self.main_container)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Teoría
        teoria_frame = ttk.Frame(frame)
        teoria_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        txt_teoria = scrolledtext.ScrolledText(teoria_frame, wrap=tk.WORD, height=8, font=('Arial', 11))
        txt_teoria.pack(fill=tk.BOTH, expand=True)
        
        # Ejemplos
        ejemplos_frame = ttk.Frame(frame)
        ejemplos_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.mostrar_ejemplos(categoria, ejemplos_frame)
        
        # Controles
        controles_frame = ttk.Frame(frame)
        controles_frame.pack(pady=10)
        
        ttk.Button(controles_frame, text="Iniciar Práctica", 
                 command=lambda: self.iniciar_practica(categoria)).pack(side=tk.LEFT, padx=5)
        ttk.Button(controles_frame, text="Volver", command=self.mostrar_menu_principal).pack(side=tk.RIGHT, padx=5)

    def iniciar_practica(self, categoria):
        # Lógica para práctica específica
        pass

    def mostrar_crear_ejemplo(self):
        self.limpiar_frame()
        frame = ttk.Frame(self.main_container)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Formulario
        ttk.Label(frame, text="Crear Nuevo Ejemplo", font=('Arial', 14)).pack(pady=10)
        
        form_frame = ttk.Frame(frame)
        form_frame.pack(fill=tk.X, pady=5)
        
        # Campos del formulario
        ttk.Label(form_frame, text="Categoría:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.categoria_var = tk.StringVar()
        categorias = list(self.base_conocimiento.keys())
        cb_categoria = ttk.Combobox(form_frame, textvariable=self.categoria_var, values=categorias)
        cb_categoria.grid(row=0, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(form_frame, text="Subcategoría:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.subcategoria_var = tk.StringVar()
        self.cb_subcategoria = ttk.Combobox(form_frame, textvariable=self.subcategoria_var)
        self.cb_subcategoria.grid(row=1, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(form_frame, text="Texto del ejemplo:").grid(row=2, column=0, sticky=tk.W, padx=5)
        self.txt_ejemplo = tk.Text(form_frame, height=4, width=50, wrap=tk.WORD)
        self.txt_ejemplo.grid(row=2, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(form_frame, text="Regla aplicada:").grid(row=3, column=0, sticky=tk.W, padx=5)
        self.regla_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.regla_var).grid(row=3, column=1, sticky=tk.EW, padx=5)
        
        # Botones
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Guardar", command=self.guardar_ejemplo).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Volver", command=self.mostrar_menu_principal).pack(side=tk.RIGHT, padx=5)

    def guardar_ejemplo(self):
        # Validación y guardado de ejemplos
        pass

    def iniciar_practica_general(self):
        # Lógica para práctica general
        pass

    def mostrar_puntaje(self):
        messagebox.showinfo("Puntuación", 
                          f"Aciertos: {self.puntuacion['aciertos']}\nErrores: {self.puntuacion['errores']}")

    def limpiar_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
            
    def limpiar_formulario(self):
        self.txt_ejemplo.delete('1.0', tk.END)
        self.regla_var.set('')
        self.categoria_var.set('')
        self.subcategoria_var.set('')

if __name__ == "__main__":
    root = tk.Tk()
    app = GramaticaApp(root)
    root.mainloop()
