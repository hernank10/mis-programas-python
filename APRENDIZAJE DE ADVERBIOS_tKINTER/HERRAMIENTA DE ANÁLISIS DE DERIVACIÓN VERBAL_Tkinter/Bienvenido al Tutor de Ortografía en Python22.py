import json
import pyttsx3
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText

class OrtografiaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PracticOrtografía GUI")
        self.geometry("1000x600")
        self.ejemplos = []
        self.progreso = {}
        self.categorias = {
            1: "B/V", 2: "C/S/Z", 3: "G/J", 4: "LL/Y",
            5: "H muda", 6: "Dígrafos", 7: "Diptongos/Hiatos",
            8: "Tildes", 9: "Homófonas/Etimológicas"
        }
        self.engine = pyttsx3.init()
        self.cargar_datos()
        self.crear_widgets()
        
    def crear_widgets(self):
        # Panel principal
        self.notebook = ttk.Notebook(self)
        
        # Pestaña de Ejemplos
        self.frame_ejemplos = ttk.Frame(self.notebook)
        self.crear_pestana_ejemplos()
        
        # Pestaña de Progreso
        self.frame_progreso = ttk.Frame(self.notebook)
        self.crear_pestana_progreso()
        
        self.notebook.add(self.frame_ejemplos, text="📝 Ejemplos")
        self.notebook.add(self.frame_progreso, text="📊 Progreso")
        self.notebook.pack(expand=True, fill=tk.BOTH)
        
        # Barra de herramientas
        self.barra_herramientas = ttk.Frame(self)
        self.botones_herramientas()
        self.barra_herramientas.pack(side=tk.TOP, fill=tk.X)
        
    def crear_pestana_ejemplos(self):
        # Listado de ejemplos
        self.tree = ttk.Treeview(self.frame_ejemplos, columns=('Categoría', 'Palabra', 'Oración'), show='headings')
        self.tree.heading('Categoría', text='Categoría')
        self.tree.heading('Palabra', text='Palabra')
        self.tree.heading('Oración', text='Oración')
        self.tree.column('Categoría', width=150)
        self.tree.column('Palabra', width=150)
        self.tree.column('Oración', width=500)
        
        # Scrollbar
        scroll = ttk.Scrollbar(self.frame_ejemplos, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scroll.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def crear_pestana_progreso(self):
        self.tree_progreso = ttk.Treeview(self.frame_progreso, columns=('Categoría', 'Ejemplos'), show='headings')
        self.tree_progreso.heading('Categoría', text='Categoría')
        self.tree_progreso.heading('Ejemplos', text='Ejemplos Registrados')
        self.tree_progreso.pack(expand=True, fill=tk.BOTH)
        
    def botones_herramientas(self):
        btn_agregar = ttk.Button(self.barra_herramientas, text="➕ Agregar", command=self.agregar_ejemplo)
        btn_editar = ttk.Button(self.barra_herramientas, text="✏️ Editar", command=self.editar_ejemplo)
        btn_escuchar = ttk.Button(self.barra_herramientas, text="🔊 Escuchar", command=self.escuchar_ejemplo)
        btn_actualizar = ttk.Button(self.barra_herramientas, text="🔄 Actualizar", command=self.actualizar_vista)
        
        btn_agregar.pack(side=tk.LEFT, padx=5)
        btn_editar.pack(side=tk.LEFT, padx=5)
        btn_escuchar.pack(side=tk.LEFT, padx=5)
        btn_actualizar.pack(side=tk.LEFT, padx=5)
        
    def cargar_datos(self):
        try:
            with open('ejemplos.json') as f:
                data = json.load(f)
                self.ejemplos = data['ejemplos']
                self.progreso = data['progreso']
        except FileNotFoundError:
            self.progreso = {v: 0 for v in self.categorias.values()}
        
    def guardar_datos(self):
        with open('ejemplos.json', 'w') as f:
            json.dump({'ejemplos': self.ejemplos, 'progreso': self.progreso}, f)
            
    def actualizar_vista(self):
        # Actualizar lista de ejemplos
        self.tree.delete(*self.tree.get_children())
        for ej in self.ejemplos:
            self.tree.insert('', tk.END, values=(ej['categoria'], ej['palabra'], ej['oracion']))
            
        # Actualizar progreso
        self.tree_progreso.delete(*self.tree_progreso.get_children())
        for cat, total in self.progreso.items():
            self.tree_progreso.insert('', tk.END, values=(cat, total))
    
    def agregar_ejemplo(self):
        if len(self.ejemplos) >= 100:
            messagebox.showwarning("Límite alcanzado", "¡Se ha llegado al máximo de 100 ejemplos!")
            return
            
        ventana = tk.Toplevel(self)
        ventana.title("Nuevo Ejemplo")
        
        ttk.Label(ventana, text="Categoría:").grid(row=0, column=0, padx=5, pady=5)
        categoria = ttk.Combobox(ventana, values=list(self.categorias.values()), state='readonly')
        categoria.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(ventana, text="Palabra:").grid(row=1, column=0, padx=5, pady=5)
        palabra = ttk.Entry(ventana)
        palabra.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(ventana, text="Oración:").grid(row=2, column=0, padx=5, pady=5)
        oracion = ScrolledText(ventana, width=40, height=4)
        oracion.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(ventana, text="Regla:").grid(row=3, column=0, padx=5, pady=5)
        regla = ScrolledText(ventana, width=40, height=4)
        regla.grid(row=3, column=1, padx=5, pady=5)
        
        def guardar():
            if not all([categoria.get(), palabra.get(), oracion.get("1.0", tk.END).strip()]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
                
            nuevo = {
                'categoria': categoria.get(),
                'palabra': palabra.get(),
                'oracion': oracion.get("1.0", tk.END).strip(),
                'regla': regla.get("1.0", tk.END).strip()
            }
            self.ejemplos.append(nuevo)
            self.progreso[categoria.get()] += 1
            self.guardar_datos()
            self.actualizar_vista()
            ventana.destroy()
            
        ttk.Button(ventana, text="Guardar", command=guardar).grid(row=4, columnspan=2, pady=10)
        
    def editar_ejemplo(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selección requerida", "Seleccione un ejemplo de la lista")
            return
            
        index = self.tree.index(seleccionado[0])
        ejemplo = self.ejemplos[index]
        
        ventana = tk.Toplevel(self)
        ventana.title("Editar Ejemplo")
        
        # Campos de edición (similar a agregar_ejemplo)
        # ... [código similar al de agregar pero con valores precargados]
        
    def escuchar_ejemplo(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selección requerida", "Seleccione un ejemplo de la lista")
            return
            
        index = self.tree.index(seleccionado[0])
        ejemplo = self.ejemplos[index]
        texto = f"Palabra: {ejemplo['palabra']}. Oración: {ejemplo['oracion']}"
        self.engine.say(texto)
        self.engine.runAndWait()
        
if __name__ == "__main__":
    app = OrtografiaApp()
    app.mainloop()
