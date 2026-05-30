import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from collections import deque
from datetime import datetime

class GrammarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Estructuras Gramaticales")
        self.root.geometry("1000x800")
        
        # Configuración inicial
        self.MAX_EXAMPLES = 100
        self.DATA_FILE = "grammar_data.json"
        self.examples = deque(maxlen=self.MAX_EXAMPLES)
        self.load_data()
        self.load_theoretical_examples()
        
        # Configurar interfaz
        self.setup_styles()
        self.create_main_interface()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#F0F8FF')
        self.style.configure('TButton', font=('Arial', 10), padding=6)
        self.style.configure('TLabel', background='#F0F8FF', font=('Arial', 11))
        self.style.configure('Title.TLabel', font=('Arial', 14, 'bold'), foreground='#2F4F4F')
        
    def create_main_interface(self):
        self.notebook = ttk.Notebook(self.root)
        
        # Pestañas principales
        self.create_tab = ttk.Frame(self.notebook)
        self.practice_tab = ttk.Frame(self.notebook)
        self.theory_tab = ttk.Frame(self.notebook)
        self.stats_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.create_tab, text="Crear Ejemplos")
        self.notebook.add(self.practice_tab, text="Practicar")
        self.notebook.add(self.theory_tab, text="Teoría")
        self.notebook.add(self.stats_tab, text="Estadísticas")
        
        self.build_create_tab()
        self.build_practice_tab()
        self.build_theory_tab()
        self.build_stats_tab()
        
        self.notebook.pack(expand=True, fill='both')
        
    def build_create_tab(self):
        frame = ttk.Frame(self.create_tab)
        frame.pack(padx=20, pady=20)
        
        ttk.Label(frame, text="Crear Nuevo Ejemplo", style='Title.TLabel').pack(pady=10)
        
        # Selector de tipo
        self.example_type = tk.StringVar(value='Apex')
        ttk.Radiobutton(frame, text="Aposición Explicativa", variable=self.example_type, 
                       value='Apex').pack(anchor='w', pady=5)
        ttk.Radiobutton(frame, text="Dislocación Derecha", variable=self.example_type, 
                       value='DD').pack(anchor='w', pady=5)
        
        # Plantilla y entrada
        self.template_text = tk.StringVar()
        self.update_template()
        ttk.Label(frame, textvariable=self.template_text, wraplength=600).pack(pady=10)
        
        self.entry = ttk.Entry(frame, width=60)
        self.entry.pack(pady=10)
        
        # Botones
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Nueva Plantilla", command=self.update_template).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Guardar", command=self.save_example).pack(side='left', padx=5)
        
    def build_practice_tab(self):
        frame = ttk.Frame(self.practice_tab)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame, text="Práctica de Estructuras", style='Title.TLabel').pack(pady=10)
        
        self.practice_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=10)
        self.practice_display.pack(fill='both', expand=True, pady=10)
        
        self.practice_input = ttk.Entry(frame)
        self.practice_input.pack(pady=10)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Iniciar Práctica", command=self.start_practice).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Verificar", command=self.check_answer).pack(side='left', padx=5)
        
    def build_theory_tab(self):
        frame = ttk.Frame(self.theory_tab)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        theory_text = """
        TEORÍA DE LAS ESTRUCTURAS GRAMATICALES
        
        Aposición Explicativa:
        - Función: Ampliar información sobre un elemento mencionado
        - Estructura: SN1 + , + SN2
        - Ejemplo: 
          "Miguel de Cervantes, autor del Quijote, es figura clave de la literatura"
        
        Dislocación Derecha:
        - Función: Recuperar/Enfatizar un tópico
        - Estructura: Oración + , + SN
        - Ejemplo:
          "La vi ayer en el parque, a mi prima de Sevilla"
        
        Casos Mixtos:
        - Combinan ambas estructuras
        - Ejemplo analizado:
          "Allí estaba él, el ganador del premio Nobel"
        """
        
        theory_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=20)
        theory_box.insert(tk.END, theory_text)
        theory_box.configure(state='disabled')
        theory_box.pack(fill='both', expand=True)
        
    def build_stats_tab(self):
        frame = ttk.Frame(self.stats_tab)
        frame.pack(padx=20, pady=20)
        
        self.stats_label = ttk.Label(frame, text="", wraplength=600)
        self.stats_label.pack(pady=10)
        self.update_stats()
        
    def update_template(self):
        templates = {
            'Apex': [
                "Gabriel García Márquez, ____________, escribió Cien años de soledad.",
                "El Taj Mahal, ____________, es una maravilla arquitectónica."
            ],
            'DD': [
                "La vi en el concierto, ____________.",
                "Lo encontré en el parque, ____________."
            ]
        }
        self.template_text.set(random.choice(templates[self.example_type.get()]))
        
    def save_example(self):
        user_input = self.entry.get()
        template = self.template_text.get()
        full_example = template.replace("____________", user_input)
        
        if self.validate_example(full_example):
            self.examples.append({
                'type': self.example_type.get(),
                'sentence': full_example,
                'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'attempts': 0,
                'correct': 0
            })
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
            self.entry.delete(0, tk.END)
            self.update_template()
            self.save_data()
            self.update_stats()
        else:
            messagebox.showerror("Error", "Estructura no válida")
            
    def validate_example(self, example):
        if self.example_type.get() == 'Apex':
            return example.count(',') >= 2 and len(example.split(',')) > 1
        elif self.example_type.get() == 'DD':
            return example.startswith(('Lo ', 'La ', 'Los ', 'Las ')) and ', a ' in example
        return False
    
    def start_practice(self):
        if not self.examples:
            messagebox.showwarning("Advertencia", "No hay ejemplos para practicar")
            return
        
        self.current_practice = random.choice(list(self.examples))
        self.practice_display.delete(1.0, tk.END)
        self.practice_display.insert(tk.END, f"Reescribe la siguiente oración:\n\n{self.current_practice['sentence']}")
        self.practice_input.delete(0, tk.END)
        
    def check_answer(self):
        user_answer = self.practice_input.get()
        if user_answer == self.current_practice['sentence']:
            messagebox.showinfo("Correcto", "¡Reconstrucción perfecta!")
            self.current_practice['correct'] += 1
        else:
            messagebox.showinfo("Intenta de nuevo", f"Original:\n{self.current_practice['sentence']}")
        self.current_practice['attempts'] += 1
        self.save_data()
        self.start_practice()
    
    def update_stats(self):
        stats_text = f"Ejemplos almacenados: {len(self.examples)}\n"
        stats_text += f"Aposiciones: {sum(1 for e in self.examples if e['type'] == 'Apex')}\n"
        stats_text += f"Dislocaciones: {sum(1 for e in self.examples if e['type'] == 'DD')}\n"
        self.stats_label.config(text=stats_text)
    
    def load_data(self):
        try:
            with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.examples = deque(data, maxlen=self.MAX_EXAMPLES)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
            
    def load_theoretical_examples(self):
        theoretical = [
            {
                'type': 'Apex',
                'sentence': "Indurain, el cinco veces ganador del Tour, es un mito del ciclismo.",
                'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'attempts': 0,
                'correct': 0
            },
            {
                'type': 'DD',
                'sentence': "Me pareció verlo ayer, a tu hermano.",
                'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'attempts': 0,
                'correct': 0
            },
            {
                'type': 'Mixto',
                'sentence': "Y allí, debajo del peinado, estaba ella, la Señorita del Casco Cartaginés.",
                'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'attempts': 0,
                'correct': 0
            }
        ]
        for example in theoretical:
            if not any(e['sentence'] == example['sentence'] for e in self.examples):
                self.examples.append(example)
    
    def save_data(self):
        with open(self.DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(list(self.examples), f, ensure_ascii=False, indent=2)
            
    def on_closing(self):
        self.save_data()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
