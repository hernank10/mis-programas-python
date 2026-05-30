import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font
import json
import os
from PIL import Image, ImageTk

class GerundioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Artistic Gerund Practice")
        self.geometry("1000x700")
        self.configure(bg='#2E3440')
        
        # Estilo personalizado
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_styles()
        
        # Datos y configuración
        self.categories = {
            'Causal': {'color': '#88C0D0', 'examples': []},
            'Concesivo': {'color': '#81A1C1', 'examples': []},
            'Condicional': {'color': '#5E81AC', 'examples': []},
            'Auxiliares': {'color': '#BF616A', 'examples': []}
        }
        
        self.load_data()
        self.create_widgets()
        self.create_menu()

    def setup_styles(self):
        self.style.configure('TFrame', background='#2E3440')
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('Title.TLabel', 
                           font=('Helvetica', 18, 'bold'),
                           foreground='#D8DEE9',
                           background='#2E3440')
        self.style.map('Category.TButton',
                      foreground=[('active', '#2E3440')],
                      background=[('active', '#D8DEE9')])

    def create_menu(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Guardar todo", command=self.save_data)
        file_menu.add_command(label="Cargar datos", command=self.load_data)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        self.config(menu=menu_bar)

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Panel izquierdo (Categorías y entrada)
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        self.create_category_buttons(left_frame)
        self.create_input_section(left_frame)
        
        # Panel derecho (Visualización)
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.create_display_section(right_frame)
        self.create_preview_section(right_frame)

    def create_category_buttons(self, parent):
        title = ttk.Label(parent, text="Categorías", style='Title.TLabel')
        title.pack(pady=10)
        
        for i, (cat, data) in enumerate(self.categories.items()):
            btn = ttk.Button(parent,
                            text=cat,
                            style='Category.TButton',
                            command=lambda c=cat: self.select_category(c))
            btn.configure(background=data['color'])
            btn.pack(fill=tk.X, pady=5)
            
        self.selected_category = tk.StringVar()
        lbl = ttk.Label(parent,
                       textvariable=self.selected_category,
                       style='Title.TLabel')
        lbl.pack(pady=10)

    def create_input_section(self, parent):
        input_frame = ttk.Frame(parent)
        input_frame.pack(fill=tk.X, pady=20)
        
        self.input_text = tk.Text(input_frame,
                                height=4,
                                wrap=tk.WORD,
                                font=('Helvetica', 12),
                                bg='#3B4252',
                                fg='#D8DEE9')
        self.input_text.pack(fill=tk.X)
        
        btn_frame = ttk.Frame(input_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame,
                  text="➕ Añadir Ejemplo",
                  command=self.add_example).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame,
                  text="💾 Guardar",
                  command=self.save_data).pack(side=tk.RIGHT, padx=5)

    def create_display_section(self, parent):
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        for cat in self.categories:
            frame = ttk.Frame(self.notebook)
            scroll = scrolledtext.ScrolledText(frame,
                                              wrap=tk.WORD,
                                              font=('Helvetica', 12),
                                              bg='#3B4252',
                                              fg='#D8DEE9')
            scroll.pack(fill=tk.BOTH, expand=True)
            self.notebook.add(frame, text=cat)
            
    def create_preview_section(self, parent):
        preview_frame = ttk.Frame(parent)
        preview_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(preview_frame,
                 text="Vista Previa",
                 style='Title.TLabel').pack(anchor=tk.W)
        
        self.preview_canvas = tk.Canvas(preview_frame,
                                       height=100,
                                       bg='#3B4252')
        self.preview_canvas.pack(fill=tk.X)
        
    def select_category(self, category):
        self.selected_category.set(f"Categoría seleccionada: {category}")
        self.notebook.select(list(self.categories.keys()).index(category))

    def add_example(self):
        example = self.input_text.get("1.0", tk.END).strip()
        if not example:
            messagebox.showwarning("Campo vacío", "Escribe un ejemplo primero")
            return
            
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        self.categories[current_tab]['examples'].append(example)
        
        # Actualizar vista
        tab_frame = self.notebook.nametowidget(self.notebook.select())
        text_widget = tab_frame.winfo_children()[0]
        text_widget.insert(tk.END, f"- {example}\n")
        
        # Actualizar vista previa artística
        self.update_preview(example)
        self.input_text.delete("1.0", tk.END)

    def update_preview(self, text):
        self.preview_canvas.delete("all")
        x, y = 10, 20
        for word in text.split():
            color = self.categories[self.notebook.tab(self.notebook.select(), "text")]['color']
            self.preview_canvas.create_text(x, y,
                                           text=word,
                                           fill=color,
                                           font=('Helvetica', 14, 'bold'),
                                           anchor=tk.NW)
            x += len(word)*15 + 10  # Espaciado dinámico

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
                        # Actualizar vista
                        tab_index = list(self.categories.keys()).index(cat)
                        text_widget = self.notebook.winfo_children()[tab_index].winfo_children()[0]
                        text_widget.delete("1.0", tk.END)
                        for ex in examples:
                            text_widget.insert(tk.END, f"- {ex}\n")
            messagebox.showinfo("Cargado", "Datos cargados exitosamente!")

if __name__ == "__main__":
    app = GerundioApp()
    app.mainloop()
