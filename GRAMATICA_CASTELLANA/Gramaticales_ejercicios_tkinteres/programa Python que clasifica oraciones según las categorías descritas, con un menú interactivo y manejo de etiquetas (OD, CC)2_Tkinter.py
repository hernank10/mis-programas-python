import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re

class AprendizajeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprendizaje de Estructuras Gramaticales")
        self.geometry("1200x800")
        self.configure(bg='#F0F0F0')
        
        self.categorias = self.inicializar_categorias()
        self.consejos = self.cargar_consejos()
        self.estilos = self.configurar_estilos()
        
        self.crear_interfaz()
    
    def inicializar_categorias(self):
        return {
            1: {"nombre": "Enunciados", "ejemplos": [], "progreso": 0, 
                "teoria": "Unidades mínimas de comunicación con sentido completo..."},
            # ... Agregar todas las categorías
        }
    
    def cargar_consejos(self):
        return ["Consejo 1: Usa OD: para objetos directos...", 
                # ... 100 consejos
               ]
    
    def configurar_estilos(self):
        estilos = ttk.Style()
        estilos.theme_use('clam')
        estilos.configure('TFrame', background='#F0F0F0')
        estilos.configure('TNotebook', background='#FFFFFF')
        estilos.configure('TButton', font=('Arial', 10), padding=6)
        estilos.map('TButton', background=[('active', '#4CAF50')])
        return estilos
    
    def crear_interfaz(self):
        # Panel principal
        main_panel = ttk.Frame(self)
        main_panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Barra lateral
        sidebar = ttk.Frame(main_panel, width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Contenido principal
        content_panel = ttk.Frame(main_panel)
        content_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Componentes de la barra lateral
        ttk.Label(sidebar, text="Categorías", font=('Arial', 12, 'bold')).pack(pady=10)
        self.crear_botones_categorias(sidebar)
        
        # Componentes del panel principal
        self.notebook = ttk.Notebook(content_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        self.crear_pestaña_teoria()
        self.crear_pestaña_practica()
        self.crear_pestaña_progreso()
        self.crear_pestaña_consejos()
    
    def crear_botones_categorias(self, parent):
        for cat_id in self.categorias:
            btn = ttk.Button(parent, text=f"{cat_id}. {self.categorias[cat_id]['nombre']}",
                            command=lambda c=cat_id: self.mostrar_categoria(c))
            btn.pack(fill=tk.X, pady=2)
    
    def crear_pestaña_teoria(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Teoría")
        
        self.teoria_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=('Arial', 11))
        self.teoria_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def crear_pestaña_practica(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Práctica")
        
        # Entrada de ejemplo
        ttk.Label(frame, text="Escribe tu ejemplo (usa OD: y CC:):").pack(pady=5)
        self.entrada_ejemplo = ttk.Entry(frame, width=80)
        self.entrada_ejemplo.pack(pady=5)
        
        # Botones de acción
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Validar", command=self.validar_ejemplo).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_entrada).pack(side=tk.LEFT, padx=5)
        
        # Área de feedback
        self.feedback_text = tk.Text(frame, height=8, wrap=tk.WORD, bg='#FFFFFF')
        self.feedback_text.pack(fill=tk.X, pady=10, padx=10)
    
    def crear_pestaña_progreso(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Progreso")
        
        self.tree = ttk.Treeview(frame, columns=('Categoría', 'Progreso'), show='headings')
        self.tree.heading('Categoría', text='Categoría')
        self.tree.heading('Progreso', text='Progreso')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.actualizar_progreso()
    
    def crear_pestaña_consejos(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Consejos")
        
        self.consejos_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=('Arial', 11))
        self.consejos_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.consejos_text.insert(tk.END, "\n".join(self.consejos))
        self.consejos_text.configure(state='disabled')
    
    def mostrar_categoria(self, categoria_id):
        self.notebook.select(0)
        teoria = f"{self.categorias[categoria_id]['nombre']}\n\n"
        teoria += self.categorias[categoria_id]['teoria'] + "\n\nEjemplos:\n"
        teoria += "\n".join(self.categorias[categoria_id]['ejemplos'][:3])
        
        self.teoria_text.configure(state='normal')
        self.teoria_text.delete(1.0, tk.END)
        self.teoria_text.insert(tk.END, teoria)
        self.teoria_text.configure(state='disabled')
    
    def validar_ejemplo(self):
        ejemplo = self.entrada_ejemplo.get()
        if not ejemplo:
            messagebox.showwarning("Campo vacío", "Por favor escribe un ejemplo")
            return
        
        # Lógica de validación (implementar según categoría)
        es_valido = True
        feedback = "✓ Ejemplo válido! Estructura detectada:\n"
        feedback += f"- OD encontrado\n- CC detectado" if re.search(r"OD:|CC:", ejemplo) else ""
        
        self.feedback_text.configure(state='normal')
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(tk.END, feedback)
        self.feedback_text.configure(state='disabled')
        
        if es_valido:
            self.actualizar_progreso()
            self.limpiar_entrada()
    
    def limpiar_entrada(self):
        self.entrada_ejemplo.delete(0, tk.END)
    
    def actualizar_progreso(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for cat_id, datos in self.categorias.items():
            self.tree.insert('', tk.END, values=(datos['nombre'], f"{datos['progreso']}/10"))
    
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = AprendizajeGUI()
    app.run()
