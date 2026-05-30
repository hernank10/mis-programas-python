import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class AplicacionGramatica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Sintaxis Española")
        self.geometry("800x600")
        
        # Base de datos de ejemplos
        self.ejemplos = [
            {
                "oracion": "El niño curioso preguntó sobre las estrellas.",
                "tipo": "adjetivo",
                "modificador": "curioso",
                "oracion_parcial": "El niño [  ] preguntó sobre las estrellas."
            },
            {
                "oracion": "Las hojas del otoño cubrían el suelo.",
                "tipo": "complemento",
                "modificador": "del otoño",
                "oracion_parcial": "Las hojas [  ] cubrían el suelo."
            }
        ]
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Configurar el notebook (pestañas)
        self.notebook = ttk.Notebook(self)
        
        # Pestañas
        self.tab_clasificar = ttk.Frame(self.notebook)
        self.tab_reescribir = ttk.Frame(self.notebook)
        self.tab_crear = ttk.Frame(self.notebook)
        self.tab_ver = ttk.Frame(self.notebook)
        self.tab_quiz = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_clasificar, text="Clasificar")
        self.notebook.add(self.tab_reescribir, text="Reescribir")
        self.notebook.add(self.tab_crear, text="Crear")
        self.notebook.add(self.tab_ver, text="Ver Ejemplos")
        self.notebook.add(self.tab_quiz, text="Cuestionarios")
        self.notebook.pack(expand=True, fill='both')
        
        # Configurar cada pestaña
        self.crear_tab_clasificar()
        self.crear_tab_reescribir()
        self.crear_tab_crear()
        self.crear_tab_ver()
        self.crear_tab_quiz()
    
    def crear_tab_clasificar(self):
        frame = ttk.Frame(self.tab_clasificar)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        self.lbl_instruccion = ttk.Label(frame, 
            text="Clasifica el tipo de modificación en la oración:")
        self.lbl_instruccion.pack(pady=10)
        
        self.lbl_oracion = ttk.Label(frame, text="", font=('Arial', 12), wraplength=600)
        self.lbl_oracion.pack(pady=10)
        
        self.entrada_respuesta = ttk.Combobox(frame, 
            values=["adjetivo", "complemento", "proposicion"])
        self.entrada_respuesta.pack(pady=10)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Comprobar", 
                 command=self.verificar_clasificacion).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Nueva Oración", 
                 command=self.nueva_oracion_clasificar).pack(side='left', padx=5)
        
        self.lbl_resultado = ttk.Label(frame, text="")
        self.lbl_resultado.pack(pady=10)
        
        self.nueva_oracion_clasificar()
    
    def crear_tab_quiz(self):
        notebook_quiz = ttk.Notebook(self.tab_quiz)
        
        # Subpestañas para tipos de cuestionario
        self.tab_completar = ttk.Frame(notebook_quiz)
        self.tab_opcion_multiple = ttk.Frame(notebook_quiz)
        
        notebook_quiz.add(self.tab_completar, text="Completar")
        notebook_quiz.add(self.tab_opcion_multiple, text="Opción Múltiple")
        notebook_quiz.pack(expand=True, fill='both')
        
        # Configurar cuestionario de completar
        self.crear_tab_completar()
        self.crear_tab_opcion_multiple()
    
    def crear_tab_completar(self):
        frame = ttk.Frame(self.tab_completar)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        self.lbl_instruccion_completar = ttk.Label(frame, 
            text="Completa el espacio en blanco:")
        self.lbl_instruccion_completar.pack(pady=10)
        
        self.lbl_oracion_parcial = ttk.Label(frame, text="", font=('Arial', 12), wraplength=600)
        self.lbl_oracion_parcial.pack(pady=10)
        
        self.entrada_completar = ttk.Entry(frame, width=40)
        self.entrada_completar.pack(pady=10)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Comprobar", 
                 command=self.verificar_completar).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Nueva Pregunta", 
                 command=self.nueva_pregunta_completar).pack(side='left', padx=5)
        
        self.lbl_resultado_completar = ttk.Label(frame, text="")
        self.lbl_resultado_completar.pack(pady=10)
        
        self.nueva_pregunta_completar()
    
    def crear_tab_ver(self):
        # Treeview para mostrar ejemplos
        self.tree = ttk.Treeview(self.tab_ver, columns=('Tipo', 'Oración'), show='headings')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.heading('Oración', text='Oración')
        self.tree.column('Tipo', width=100)
        self.tree.column('Oración', width=600)
        
        vsb = ttk.Scrollbar(self.tab_ver, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')
        
        self.actualizar_treeview()
    
    def actualizar_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for ejemplo in self.ejemplos:
            self.tree.insert('', 'end', values=(ejemplo['tipo'].capitalize(), ejemplo['oracion']))
    
    # Resto de métodos de funcionalidad (verificar_clasificacion, nueva_oracion_clasificar, etc.)
    # ... (Implementar métodos similares a la versión de consola pero adaptados a Tkinter)

if __name__ == "__main__":
    app = AplicacionGramatica()
    app.mainloop()
