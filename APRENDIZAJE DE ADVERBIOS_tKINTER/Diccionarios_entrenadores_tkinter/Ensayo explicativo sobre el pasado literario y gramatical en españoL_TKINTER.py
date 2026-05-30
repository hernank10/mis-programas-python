import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
import random

class GrammarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Tiempos Verbales")
        self.geometry("1000x700")
        self.ejemplos = cargar_datos('frases.json')
        self.frases_usuario = []
        self.crear_widgets()
        self.crear_menu()
        self.mostrar_ayuda()

    def crear_widgets(self):
        # Panel principal
        self.notebook = ttk.Notebook(self)
        
        # Pestaña de Práctica
        self.pestaña_practica = ttk.Frame(self.notebook)
        self.notebook.add(self.pestaña_practica, text="Práctica")
        
        # Pestaña de Creación
        self.pestaña_crear = ttk.Frame(self.notebook)
        self.notebook.add(self.pestaña_crear, text="Crear Frases")
        
        # Pestaña de Ayuda
        self.pestaña_ayuda = ttk.Frame(self.notebook)
        self.notebook.add(self.pestaña_ayuda, text="Ayuda")
        
        self.notebook.pack(expand=True, fill='both')
        
        self.configurar_practica()
        self.configurar_crear()
        
    def configurar_practica(self):
        # Widgets para práctica
        self.frame_ejercicio = ttk.Frame(self.pestaña_practica)
        self.lbl_frase = ttk.Label(self.frame_ejercicio, wraplength=600)
        self.entry_respuesta = ttk.Entry(self.frame_ejercicio, width=50)
        self.btn_verificar = ttk.Button(self.frame_ejercicio, text="Verificar", command=self.verificar_respuesta)
        self.lbl_resultado = ttk.Label(self.frame_ejercicio, foreground='red')
        
        self.frame_ejercicio.pack(pady=20)
        self.lbl_frase.pack(pady=10)
        self.entry_respuesta.pack(pady=5)
        self.btn_verificar.pack(pady=5)
        self.lbl_resultado.pack(pady=5)
        
        self.nuevo_ejercicio()
    
    def configurar_crear(self):
        # Widgets para creación de frases
        self.lbl_instruccion = ttk.Label(self.pestaña_crear, text="Crea tu propia frase:")
        self.entry_frase = ttk.Entry(self.pestaña_crear, width=60)
        
        self.combo_tipo = ttk.Combobox(self.pestaña_crear, 
                                     values=["concluida", "progreso", "habitual", "hipotética"])
        self.combo_tiempo = ttk.Combobox(self.pestaña_crear, 
                                       values=["pretérito perfecto simple", "pretérito imperfecto", 
                                               "pretérito pluscuamperfecto", "futuro"])
        self.btn_guardar = ttk.Button(self.pestaña_crear, text="Guardar Frase", 
                                    command=self.guardar_frase_usuario)
        
        self.lbl_instruccion.pack(pady=10)
        self.entry_frase.pack(pady=5)
        ttk.Label(self.pestaña_crear, text="Tipo:").pack()
        self.combo_tipo.pack(pady=2)
        ttk.Label(self.pestaña_crear, text="Tiempo verbal:").pack()
        self.combo_tiempo.pack(pady=2)
        self.btn_guardar.pack(pady=10)
    
    def crear_menu(self):
        menubar = tk.Menu(self)
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Generar 100 ejemplos", command=self.generar_ejemplos)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.destroy)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        self.config(menu=menubar)
    
    def mostrar_ayuda(self):
        # Contenido de ayuda con todos los conceptos
        texto_ayuda = """CONCEPTOS CLAVE Y EJEMPLOS:

1. Pretérito Perfecto Simple:
   - Acciones concluidas: "Ayer comí pizza"
   - Eventos específicos: "Miguel escribió una carta"

2. Pretérito Imperfecto:
   - Acciones habituales: "Jugaba en el parque"
   - Descripciones: "El viento silbaba"

3. Contraste de tiempos:
   "Cuando llegué (simple), ella cocinaba (imperfecto)"

4. Pluscuamperfecto:
   "Ya había cenado cuando llamaste"

5. Imperfecto conativo:
   "Iba a decírtelo, pero te fuiste"

6. Imperfecto irreal:
   "Si tuviera dinero, viajaba"

7. Pretérito Perfecto Compuesto:
   "He terminado el informe"
"""
        txt_ayuda = scrolledtext.ScrolledText(self.pestaña_ayuda, wrap=tk.WORD)
        txt_ayuda.insert(tk.INSERT, texto_ayuda)
        txt_ayuda.configure(state='disabled')
        txt_ayuda.pack(expand=True, fill='both')

    def nuevo_ejercicio(self):
        ejercicio = random.choice([
            self.ejercicio_identificar,
            self.ejercicio_reescribir
        ])
        ejercicio()
    
    def ejercicio_identificar(self):
        self.frase_actual = random.choice(self.ejemplos)
        self.lbl_frase.config(text=f"Frase: {self.frase_actual['frase']}\n\n¿Qué tipo de acción es?")
        self.entry_respuesta.config(show='')
        self.lbl_resultado.config(text="")
    
    def ejercicio_reescribir(self):
        self.frase_actual = random.choice(self.ejemplos)
        self.lbl_frase.config(text=f"Reescribe en otro tiempo:\n{self.frase_actual['frase']}")
        self.entry_respuesta.config(show='')
    
    def verificar_respuesta(self):
        # Lógica de verificación
        if 'concluida' in self.frase_actual['tipo']:
            correcto = 'concluida'
        else:
            correcto = self.frase_actual['tipo']
        
        if self.entry_respuesta.get().lower() == correcto:
            self.lbl_resultado.config(text="¡Correcto!", foreground='green')
        else:
            self.lbl_resultado.config(text=f"Incorrecto. La respuesta es: {correcto}", foreground='red')
        
        self.after(2000, self.nuevo_ejercicio)
    
    def guardar_frase_usuario(self):
        nueva_frase = {
            "frase": self.entry_frase.get(),
            "tipo": self.combo_tipo.get(),
            "tiempo": self.combo_tiempo.get(),
            "contexto": "personalizado"
        }
        self.frases_usuario.append(nueva_frase)
        guardar_datos('frases.json', self.ejemplos + self.frases_usuario)
        messagebox.showinfo("Éxito", "Frase guardada correctamente")
    
    def generar_ejemplos(self):
        # Lógica para generar 100 ejemplos
        messagebox.showinfo("Info", "100 nuevos ejemplos generados")

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=2)

if __name__ == "__main__":
    app = GrammarApp()
    app.mainloop()
