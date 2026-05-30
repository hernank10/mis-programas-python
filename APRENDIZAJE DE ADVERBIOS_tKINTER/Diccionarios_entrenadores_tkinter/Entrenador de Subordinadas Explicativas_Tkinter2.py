import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, Toplevel
import json
import random
from pathlib import Path

class SubordinadasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Entrenador de Subordinadas Explicativas")
        self.geometry("1000x700")
        self.ejemplos_file = "ejemplos_guardados.json"
        self.max_ejemplos = 100
        
        self.ensayo_content = [
            {"titulo": "Introducción", "contenido": "Las frases subordinadas explicativas son elementos clave..."},
            {"titulo": "Características", "contenido": "1. Van entre comas\n2. Se refieren al último sustantivo..."},
            # ... Agregar más diapositivas según el ensayo completo
        ]
        
        self._crear_widgets()
        self._cargar_ejemplos()
    
    def _crear_widgets(self):
        # Barra de herramientas superior
        toolbar = ttk.Frame(self)
        btn_ensayo = ttk.Button(toolbar, text="📄 Ver Ensayo", command=self.mostrar_ensayo)
        btn_ensayo.pack(side=tk.LEFT, padx=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Notebook principal
        self.notebook = ttk.Notebook(self)
        self._crear_pestanas()
        self.notebook.pack(expand=True, fill='both')
    
    def _crear_pestanas(self):
        # Pestañas existentes
        self.teoria_frame = TeoriaFrame(self.notebook, self.ensayo_content[0]['contenido'])
        self.practica_frame = PracticaFrame(self.notebook, self)
        self.crear_frame = CrearFrame(self.notebook, self)
        
        self.notebook.add(self.teoria_frame, text="📚 Teoría")
        self.notebook.add(self.practica_frame, text="✍️ Practicar")
        self.notebook.add(self.crear_frame, text="➕ Crear Ejemplos")
    
    def mostrar_ensayo(self):
        SlideshowWindow(self, self.ensayo_content)
    
    # ... Resto de métodos igual que antes ...

class SlideshowWindow(Toplevel):
    def __init__(self, parent, contenido):
        super().__init__(parent)
        self.title("Ensayo - Diapositivas")
        self.geometry("800x600")
        self.contenido = contenido
        self.slide_actual = 0
        
        self._crear_widgets()
        self.actualizar_slide()
    
    def _crear_widgets(self):
        # Controles de navegación
        self.frame_controles = ttk.Frame(self)
        btn_anterior = ttk.Button(self.frame_controles, text="← Anterior", command=self.slide_anterior)
        btn_siguiente = ttk.Button(self.frame_controles, text="Siguiente →", command=self.slide_siguiente)
        btn_anterior.pack(side=tk.LEFT, padx=10)
        btn_siguiente.pack(side=tk.LEFT)
        self.frame_controles.pack(pady=10)
        
        # Área de contenido
        self.lbl_titulo = ttk.Label(self, font=('Arial', 14, 'bold'))
        self.lbl_titulo.pack(pady=5)
        
        self.txt_contenido = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Arial', 12))
        self.txt_contenido.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Contador
        self.lbl_contador = ttk.Label(self, font=('Arial', 10))
        self.lbl_contador.pack(pady=5)
    
    def actualizar_slide(self):
        slide = self.contenido[self.slide_actual]
        self.lbl_titulo.config(text=slide['titulo'])
        self.txt_contenido.delete('1.0', tk.END)
        self.txt_contenido.insert(tk.INSERT, slide['contenido'])
        self.txt_contenido.configure(state='disabled')
        self.lbl_contador.config(text=f"Diapositiva {self.slide_actual + 1} de {len(self.contenido)}")
    
    def slide_anterior(self):
        if self.slide_actual > 0:
            self.slide_actual -= 1
            self.actualizar_slide()
    
    def slide_siguiente(self):
        if self.slide_actual < len(self.contenido) - 1:
            self.slide_actual += 1
            self.actualizar_slide()

# ... Las clases TeoriaFrame, PracticaFrame y CrearFrame permanecen igual que antes ...

if __name__ == "__main__":
    app = SubordinadasApp()
    app.mainloop()
