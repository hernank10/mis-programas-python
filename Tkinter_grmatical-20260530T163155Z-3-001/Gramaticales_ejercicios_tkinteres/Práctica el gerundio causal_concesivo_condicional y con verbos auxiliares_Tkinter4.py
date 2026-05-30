import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from PIL import Image, ImageTk
import json
import os

class DragonGerundApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dragon's Gerund Practice")
        self.geometry("1200x800")
        
        # Paleta de colores mística
        self.colors = {
            'bg': '#1a1a2e',
            'text': '#e6f5ff',
            'dragon_primary': '#4a90e2',
            'dragon_secondary': '#ff6b6b',
            'button_bg': '#2d3436'
        }
        
        self.categories = {
            'Causal': {'examples': []},
            'Concesivo': {'examples': []},
            'Condicional': {'examples': []},
            'Auxiliares': {'examples': []}
        }
        
        self.load_data()
        self.create_dragon_banner()
        self.create_widgets()
        self.create_styles()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure('TFrame', background=self.colors['bg'])
        self.style.configure('TButton', 
                           font=('Helvetica', 12, 'bold'),
                           background=self.colors['button_bg'],
                           foreground=self.colors['text'],
                           borderwidth=2,
                           relief='ridge')
        
        self.style.map('TButton',
                      background=[('active', '#4a4a4a')],
                      foreground=[('active', self.colors['dragon_secondary'])])

    def create_dragon_banner(self):
        # Canvas para dibujar el dragón
        self.dragon_canvas = tk.Canvas(self, bg=self.colors['bg'], height=150)
        self.dragon_canvas.pack(fill=tk.X)
        
        # Dibujar dragón estilizado
        self.draw_dragon()
        
        # Opcional: Cargar imagen de dragón desde archivo
        try:
            self.dragon_img = ImageTk.PhotoImage(Image.open("dragon.png").resize((200,150)))
            self.dragon_canvas.create_image(50, 25, image=self.dragon_img, anchor=tk.NW)
        except FileNotFoundError:
            pass

    def draw_dragon(self):
        # Cuerpo del dragón
        self.dragon_canvas.create_line(100, 100, 300, 50, 
                                     width=8, fill=self.colors['dragon_primary'], 
                                     smooth=True, splinesteps=20)
        
        # Cabeza
        self.dragon_canvas.create_oval(280, 30, 320, 70, 
                                     outline=self.colors['dragon_secondary'],
                                     width=3)
        
        # Cuernos
        self.dragon_canvas.create_polygon(300, 40, 310, 20, 320, 40, 
                                        fill=self.colors['dragon_secondary'])
        
        # Alas
        self.dragon_canvas.create_line(200, 80, 150, 20, 250, 30, 200, 80,
                                     width=5, fill=self.colors['dragon_primary'],
                                     smooth=True)

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Panel izquierdo - Categorías
        left_panel = ttk.Frame(main_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        ttk.Label(left_panel, 
                 text="🏔️ Categorías", 
                 font=('Helvetica', 16, 'bold'),
                 foreground=self.colors['dragon_secondary'],
                 background=self.colors['bg']).pack(pady=15)
        
        for cat in self.categories:
            btn = ttk.Button(left_panel,
                            text=f"🐉 {cat}",
                            command=lambda c=cat: self.select_category(c))
            btn.pack(fill=tk.X, pady=8)
        
        # Panel central - Entrada y ejemplos
        center_panel = ttk.Frame(main_frame)
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.text_input = tk.Text(center_panel,
                                height=6,
                                bg='#2d3436',
                                fg=self.colors['text'],
                                insertbackground=self.colors['text'],
                                font=('Helvetica', 12),
                                wrap=tk.WORD)
        self.text_input.pack(fill=tk.X, pady=15)
        
        btn_frame = ttk.Frame(center_panel)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame,
                  text="🔥 Añadir Ejemplo",
                  command=self.add_example).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(btn_frame,
                  text="💎 Guardar Todo",
                  command=self.save_data).pack(side=tk.RIGHT, padx=8)
        
        # Panel derecho - Ejemplos
        self.notebook = ttk.Notebook(center_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        for cat in self.categories:
            frame = ttk.Frame(self.notebook)
            scroll = scrolledtext.ScrolledText(frame,
                                              wrap=tk.WORD,
                                              bg='#2d3436',
                                              fg=self.colors['text'],
                                              font=('Helvetica', 12))
            scroll.pack(fill=tk.BOTH, expand=True)
            self.notebook.add(frame, text=cat)

    def select_category(self, category):
        self.notebook.select(list(self.categories.keys()).index(category))

    def add_example(self):
        example = self.text_input.get("1.0", tk.END).strip()
        if not example:
            messagebox.showwarning("¡Fuego débil!", "¡Escribe un ejemplo digno de un dragón!")
            return
            
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        self.categories[current_tab]['examples'].append(example)
        
        # Animación simple
        self.dragon_canvas.itemconfig(1, fill=self.colors['dragon_secondary'])
        self.after(300, lambda: self.dragon_canvas.itemconfig(1, fill=self.colors['dragon_primary']))
        
        tab_index = list(self.categories.keys()).index(current_tab)
        text_widget = self.notebook.winfo_children()[tab_index].winfo_children()[0]
        text_widget.insert(tk.END, f"- 🐲 {example}\n")
        
        self.text_input.delete("1.0", tk.END)

    def save_data(self):
        with open('dragon_gerunds.json', 'w') as f:
            json.dump({k: v['examples'] for k, v in self.categories.items()}, f)
        messagebox.showinfo("Tesoro guardado", "¡Los conocimientos fueron protegidos por el dragón!")

    def load_data(self):
        if os.path.exists('dragon_gerunds.json'):
            with open('dragon_gerunds.json', 'r') as f:
                data = json.load(f)
                for cat, examples in data.items():
                    if cat in self.categories:
                        self.categories[cat]['examples'] = examples
                        tab_index = list(self.categories.keys()).index(cat)
                        text_widget = self.notebook.winfo_children()[tab_index].winfo_children()[0]
                        text_widget.delete("1.0", tk.END)
                        for ex in examples:
                            text_widget.insert(tk.END, f"- 🐲 {ex}\n")

if __name__ == "__main__":
    app = DragonGerundApp()
    app.mainloop()
