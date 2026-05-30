import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class AplicacionAtributos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Máster en Atributos Gramaticales")
        self.geometry("1000x700")
        self.config(bg="#F0F0F0")
        
        # Datos de contenido
        self.ensayo = """[Texto completo del ensayo explicativo...]"""
        self.ejercicios = [
            {
                'categoria': 'Concordancia',
                'enunciado': "El mar está [turbulento]. Identifica el atributo:",
                'atributo': "turbulento",
                'tipo': "Atributo del sujeto (adjetivo)",
                'dificultad': 1,
                'completado': False
            },
            # Añadir más ejercicios...
        ]
        self.consejos = {
            'Concordancia': ["Siempre verifica género y número", "Usa 'lo' para elipsis"],
            # Añadir más categorías...
        }
        
        # Variables de progreso
        self.progreso = {
            'ejercicios_completados': 0,
            'puntaje_total': 0,
            'por_categoria': {}
        }
        
        # Configurar interfaz
        self.crear_widgets()
    
    def crear_widgets(self):
        # Notebook principal
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)
        
        # Pestañas
        self.crear_pestana_ensayo()
        self.crear_pestana_ejercicios()
        self.crear_pestana_progreso()
        self.crear_pestana_teoria()
    
    def crear_pestana_ensayo(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📚 Ensayo")
        
        texto = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=('Arial', 32))
        texto.insert(tk.INSERT, self.ensayo)
        texto.config(state=tk.DISABLED)
        texto.pack(fill='both', expand=True, padx=20, pady=20)
    
    def crear_pestana_ejercicios(self):
        self.frame_ejercicios = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_ejercicios, text="✍️ Ejercicios")
        
        # Controles superiores
        self.frame_controles = ttk.Frame(self.frame_ejercicios)
        self.frame_controles.pack(fill='x', padx=20, pady=10)
        
        self.lbl_categoria = ttk.Label(self.frame_controles, text="Categoría:")
        self.lbl_categoria.pack(side='left')
        
        self.combo_categorias = ttk.Combobox(self.frame_controles, values=list(self.consejos.keys()))
        self.combo_categorias.pack(side='left', padx=10)
        self.combo_categorias.bind('<<ComboboxSelected>>', self.cargar_ejercicio)
        
        # Área de ejercicio
        self.frame_ejercicio = ttk.Frame(self.frame_ejercicios)
        self.frame_ejercicio.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.lbl_enunciado = ttk.Label(self.frame_ejercicio, font=('Arial', 14), wraplength=800)
        self.lbl_enunciado.pack(pady=20)
        
        self.entrada_respuesta = ttk.Entry(self.frame_ejercicio, font=('Arial', 12))
        self.entrada_respuesta.pack(pady=10)
        
        self.btn_verificar = ttk.Button(self.frame_ejercicio, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=10)
        
        self.lbl_feedback = ttk.Label(self.frame_ejercicio, font=('Arial', 12), foreground="gray")
        self.lbl_feedback.pack(pady=10)
        
        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(self.frame_ejercicios, orient='horizontal', mode='determinate')
        self.barra_progreso.pack(fill='x', padx=20, pady=10)
    
    def crear_pestana_progreso(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📊 Progreso")
        
        # Estadísticas
        self.lbl_stats = ttk.Label(frame, text="Estadísticas de aprendizaje:", font=('Arial', 14))
        self.lbl_stats.pack(pady=20)
        
        self.canvas_progreso = tk.Canvas(frame, bg="white", height=300, width=800)
        self.canvas_progreso.pack(pady=20)
        
        self.actualizar_progreso()
    
    def crear_pestana_teoria(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📘 Teoría")
        
        tree = ttk.Treeview(frame, columns=('Tipo', 'Semántica'), show='headings')
        tree.heading('Tipo', text='Tipo Gramatical')
        tree.heading('Semántica', text='Categoría Semántica')
        
        # Ejemplo de datos
        tree.insert('', 'end', values=('Atributo del sujeto', 'Característica física'))
        # Añadir más datos...
        
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        
        tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')
    
    def cargar_ejercicio(self, event=None):
        categoria = self.combo_categorias.get()
        ejercicio = next(e for e in self.ejercicios if e['categoria'] == categoria and not e['completado'])
        
        self.lbl_enunciado.config(text=ejercicio['enunciado'])
        self.entrada_respuesta.delete(0, tk.END)
        self.lbl_feedback.config(text="")
    
    def verificar_respuesta(self):
        respuesta = self.entrada_respuesta.get().strip().lower()
        categoria = self.combo_categorias.get()
        ejercicio = next(e for e in self.ejercicios if e['categoria'] == categoria)
        
        if respuesta == ejercicio['atributo'].lower():
            self.progreso['ejercicios_completados'] += 1
            self.progreso['puntaje_total'] += 10
            self.actualizar_progreso()
            self.lbl_feedback.config(text="✅ Correcto! +10 puntos", foreground="green")
            ejercicio['completado'] = True
        else:
            self.lbl_feedback.config(text=f"❌ Incorrecto. El atributo es: {ejercicio['atributo']}", foreground="red")
        
        self.actualizar_barra_progreso()
    
    def actualizar_barra_progreso(self):
        total = len(self.ejercicios)
        completados = self.progreso['ejercicios_completados']
        self.barra_progreso['value'] = (completados / total) * 100 if total > 0 else 0
    
    def actualizar_progreso(self):
        # Actualizar gráfica
        self.canvas_progreso.delete("all")
        categorias = list(self.consejos.keys())
        valores = [self.progreso['por_categoria'].get(cat, 0) for cat in categorias]
        
        # Dibujar gráfica de barras
        bar_width = 40
        x = 50
        for i, (cat, val) in enumerate(zip(categorias, valores)):
            y0 = 250 - val * 2
            self.canvas_progreso.create_rectangle(x, y0, x + bar_width, 250, fill="skyblue")
            self.canvas_progreso.create_text(x + bar_width/2, 260, text=cat, angle=45, anchor='ne')
            x += bar_width + 30
    
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = AplicacionAtributos()
    app.run()
