import tkinter as tk
from tkinter import ttk, messagebox
import random
# ... (mantener el código anterior de la clase AprendePrefijosApp sin cambios)
# Lista completa de palabras (completa con tus 100 términos)
palabras = [
    {"prefijo": "ante", "base": "brazo", "categoria": "Locativos", "palabra": "antebrazo"},
    {"prefijo": "sub", "base": "terráneo", "categoria": "Locativos", "palabra": "subterráneo"},
    {"prefijo": "pre", "base": "democrático", "categoria": "Temporales", "palabra": "predemocrático"},
    {"prefijo": "pos", "base": "guerra", "categoria": "Temporales", "palabra": "posguerra"},
    {"prefijo": "bi", "base": "lingüe", "categoria": "Cuantificativos", "palabra": "bilingüe"},
    {"prefijo": "multi", "base": "color", "categoria": "Cuantificativos", "palabra": "multicolor"},
    {"prefijo": "hiper", "base": "activo", "categoria": "Gradativos", "palabra": "hiperactivo"},
    {"prefijo": "super", "base": "población", "categoria": "Gradativos", "palabra": "superpoblación"},
    {"prefijo": "in", "base": "útil", "categoria": "Negativos", "palabra": "inútil"},
    {"prefijo": "des", "base": "orden", "categoria": "Negativos", "palabra": "desorden"},
]
class AprendePrefijosApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # ... (código anterior sin cambios)
        
        # Nueva sección de teoría
        self.slides = [
            {
                "categoria": "Locativos",
                "descripcion": "Indican posición o dirección en el espacio",
                "ejemplos": ["antebrazo (posición delantera)", "subterráneo (posición inferior)", "sobrevolar (posición superior)"]
            },
            {
                "categoria": "Temporales",
                "descripcion": "Expresan relaciones de tiempo o secuencia",
                "ejemplos": ["predemocrático (antes de)", "posguerra (después de)", "rehacer (repetición)"]
            },
            # Añadir slides para las demás categorías
        ]
        self.current_slide = 0
        
        self.crear_widgets_iniciales()
        
    def crear_widgets_iniciales(self):
        self.clear_frame()
        
        # Botón nuevo de teoría
        btn_teoria = ttk.Button(self, text="Ver Teoría", command=self.mostrar_teoria)
        btn_teoria.pack(side='top', anchor='ne', padx=10, pady=10)
        
        # ... (resto del código anterior de crear_widgets_iniciales)

    def mostrar_teoria(self):
        teoria_window = tk.Toplevel(self)
        teoria_window.title("Teoría de Prefijos")
        teoria_window.geometry("600x400")
        
        main_frame = ttk.Frame(teoria_window)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.slide_frame = ttk.Frame(main_frame)
        self.slide_frame.pack(expand=True, fill='both')
        
        # Controles de navegación
        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(pady=10)
        
        btn_anterior = ttk.Button(nav_frame, text="← Anterior", 
                                command=lambda: self.cambiar_slide(-1, teoria_window))
        btn_anterior.pack(side='left', padx=10)
        
        btn_siguiente = ttk.Button(nav_frame, text="Siguiente →", 
                                command=lambda: self.cambiar_slide(1, teoria_window))
        btn_siguiente.pack(side='right', padx=10)
        
        self.actualizar_slide(teoria_window)
        
    def cambiar_slide(self, direction, window):
        self.current_slide += direction
        if self.current_slide < 0:
            self.current_slide = 0
        elif self.current_slide >= len(self.slides):
            self.current_slide = len(self.slides) - 1
        self.actualizar_slide(window)
        
    def actualizar_slide(self, window):
        # Limpiar frame anterior
        for widget in self.slide_frame.winfo_children():
            widget.destroy()
            
        slide = self.slides[self.current_slide]
        
        # Título de categoría
        lbl_categoria = ttk.Label(self.slide_frame, 
                                text=slide["categoria"], 
                                font=('Arial', 16, 'bold'),
                                foreground='#2c3e50')
        lbl_categoria.pack(pady=10)
        
        # Descripción
        lbl_desc = ttk.Label(self.slide_frame, 
                           text=slide["descripcion"], 
                           font=('Arial', 12),
                           wraplength=500,
                           justify='center')
        lbl_desc.pack(pady=10)
        
        # Ejemplos
        ejemplos_frame = ttk.Frame(self.slide_frame)
        ejemplos_frame.pack(pady=20)
        
        ttk.Label(ejemplos_frame, 
                text="Ejemplos:", 
                font=('Arial', 12, 'underline')).pack(anchor='w')
        
        for ejemplo in slide["ejemplos"]:
            ttk.Label(ejemplos_frame, 
                    text=f"• {ejemplo}", 
                    font=('Arial', 11),
                    foreground='#27ae60').pack(anchor='w', padx=20)
        
        # Indicador de progreso
        ttk.Label(self.slide_frame, 
                text=f"Slide {self.current_slide + 1}/{len(self.slides)}",
                font=('Arial', 10)).pack(pady=10)

# ... (mantener el resto del código sin cambios)
