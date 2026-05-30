import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font
import json
import os

class GerundioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Gerundios Colorida")
        self.geometry("1000x700")
        self.configure(bg='#2E3440')
        
        # Paleta de colores vivos
        self.colors = {
            'bg': '#2E3440',
            'text': '#D8DEE9',
            'Causal': '#88C0D0',
            'Concesivo': '#81A1C1',
            'Condicional': '#5E81AC',
            'Auxiliares': '#BF616A',
            'button_bg': '#4C566A',
            'button_active': '#3B4252'
        }
        
        # Configuración inicial
        self.categories = {
            'Causal': {'examples': []},
            'Concesivo': {'examples': []},
            'Condicional': {'examples': []},
            'Auxiliares': {'examples': []}
        }
        
        self.load_data()
        self.create_widgets()
        self.create_styles()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure('TFrame', background=self.colors['bg'])
        self.style.configure('TButton', 
                           font=('Helvetica', 12),
                           background=self.colors['button_bg'],
                           foreground=self.colors['text'],
                           borderwidth=0)
        
        self.style.map('TButton',
                      background=[('active', self.colors['button_active'])])
        
        self.style.configure('Title.TLabel', 
                           font=('Helvetica', 18, 'bold'),
                           foreground=self.colors['text'],
                           background=self.colors['bg'])

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Panel izquierdo - Categorías
        left_panel = ttk.Frame(main_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        ttk.Label(left_panel, 
                 text="Categorías", 
                 style='Title.TLabel').pack(pady=10)
        
        for cat in self.categories:
            btn = ttk.Button(left_panel,
                            text=cat,
                            command=lambda c=cat: self.select_category(c),
                            style='Category.TButton')
            btn.configure(style='TButton')
            btn.pack(fill=tk.X, pady=5)
        
        # Panel central - Entrada de texto
        center_panel = ttk.Frame(main_frame)
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.text_input = tk.Text(center_panel,
                                height=5,
                                bg=self.colors['button_active'],
                                fg=self.colors['text'],
                                insertbackground=self.colors['text'],
                                font=('Helvetica', 12))
        self.text_input.pack(fill=tk.X, pady=10)
        
        btn_frame = ttk.Frame(center_panel)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame,
                  text="✨ Añadir Ejemplo",
                  command=self.add_example).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame,
                  text="💾 Guardar Todo",
                  command=self.save_data).pack(side=tk.RIGHT, padx=5)
        
        # Panel derecho - Visualización
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        for cat in self.categories:
            frame = ttk.Frame(self.notebook)
            scroll = scrolledtext.ScrolledText(frame,
                                              wrap=tk.WORD,
                                              bg=self.colors['button_active'],
                                              fg=self.colors['text'],
                                              font=('Helvetica', 12))
            scroll.pack(fill=tk.BOTH, expand=True)
            self.notebook.add(frame, text=cat)

    def select_category(self, category):
        self.notebook.select(list(self.categories.keys()).index(category))

    def add_example(self):
        example = self.text_input.get("1.0", tk.END).strip()
        if not example:
            messagebox.showwarning("Error", "Escribe un ejemplo primero")
            return
            
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        self.categories[current_tab]['examples'].append(example)
        
        # Actualizar vista
        tab_index = list(self.categories.keys()).index(current_tab)
        text_widget = self.notebook.winfo_children()[tab_index].winfo_children()[0]
        text_widget.insert(tk.END, f"- {example}\n")
        
        self.text_input.delete("1.0", tk.END)
        messagebox.showinfo("Éxito", "Ejemplo añadido correctamente!")

    def save_data(self):
        with open('gerundios_data.json', 'w') as f:
            json.dump({k: v['examples'] for k, v in self.categories.items()}, f)
        messagebox.showinfo("Guardado", "Datos guardados exitosamente!")

    def load_data(self):
        if os.path.exists('gerundios_data.json'):
            with open('gerundios_data.json', 'r') as f:
                data = json.load(f)
                for cat, examples in data.items():
                    if cat in self.categories:
                        self.categories[cat]['examples'] = examples
                        tab_index = list(self.categories.keys()).index(cat)
                        text_widget = self.notebook.winfo_children()[tab_index].winfo_children()[0]
                        text_widget.delete("1.0", tk.END)
                        for ex in examples:
                            text_widget.insert(tk.END, f"- {ex}\n")

if __name__ == "__main__":
    app = GerundioApp()
    app.mainloop()
