import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import json

COLORS = {
    'background': '#F5F5F0',
    'primary': '#5AA6D9',
    'secondary': '#ED5454',
    'accent': '#FAD95F',
    'text': '#2D2D2D'
}

class ArtButton(tk.Canvas):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
        self.width = kwargs.get('width', 100)
        self.height = kwargs.get('height', 40)
        self.radius = 20
        
        self.draw_button(text)
    
    def draw_button(self, text):
        self.delete("all")
        # Fondo
        self.create_rounded_rect(0, 0, self.width, self.height, 
                               fill=COLORS['primary'], outline=COLORS['secondary'])
        # Texto
        self.create_text(self.width/2, self.height/2, text=text, 
                        fill=COLORS['text'], font=('Arial', 10, 'bold'))
    
    def create_rounded_rect(self, x1, y1, x2, y2, **kwargs):
        radius = self.radius
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1+radius, y1
        ]
        return self.create_polygon(points, **kwargs, smooth=True)
    
    def on_click(self, event):
        self.itemconfig(1, fill=COLORS['accent'])
        self.after(100, lambda: self.itemconfig(1, fill=COLORS['primary']))
        if self.command:
            self.command()
    
    def on_enter(self, event):
        self.itemconfig(1, fill=COLORS['secondary'])
    
    def on_leave(self, event):
        self.itemconfig(1, fill=COLORS['primary'])

class ExampleItem(ttk.Frame):
    def __init__(self, master, verb, conjugation, example):
        super().__init__(master, style='Example.TFrame')
        self.verb = verb
        self.conjugation = conjugation
        self.example = example
        
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()
    
    def create_widgets(self):
        lbl_verb = ttk.Label(self, text=self.verb, 
                            font=('Arial', 10, 'bold'), 
                            foreground=COLORS['primary'])
        lbl_verb.grid(row=0, column=0, sticky='w', padx=10)
        
        lbl_conj = ttk.Label(self, text=self.conjugation, 
                           font=('Arial', 9), 
                           foreground=COLORS['text'])
        lbl_conj.grid(row=1, column=0, sticky='w', padx=10)
        
        lbl_example = ttk.Label(self, text=self.example, 
                              font=('Arial', 9, 'italic'), 
                              foreground=COLORS['text'])
        lbl_example.grid(row=2, column=0, sticky='w', padx=10, pady=(0,5))

class VerbosArtApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Verbos Artísticos")
        self.geometry("800x600")
        self.configure(bg=COLORS['background'])
        self.create_styles()
        self.create_widgets()
    
    def create_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo del Spinner
        style.configure('TCombobox', 
                       foreground=COLORS['text'],
                       background=COLORS['background'],
                       fieldbackground=COLORS['background'],
                       selectbackground=COLORS['accent'])
        
        # Estilo de los ítems
        style.configure('Example.TFrame', 
                       background=COLORS['background'],
                       bordercolor=COLORS['primary'],
                       relief='solid',
                       borderwidth=1)
    
    def create_widgets(self):
        # Header
        header = ttk.Frame(self, style='Header.TFrame')
        header.pack(fill='x', padx=20, pady=20)
        
        lbl_title = ttk.Label(header, 
                            text="VERBOS ART", 
                            font=('Arial', 24, 'bold'), 
                            foreground=COLORS['primary'])
        lbl_title.pack(side='left')
        
        # Controles
        controls = ttk.Frame(self)
        controls.pack(fill='x', padx=20, pady=10)
        
        self.spinner = ttk.Combobox(controls, 
                                  values=["Epéntesis", "Síncopa", "Alternancias"],
                                  font=('Arial', 12))
        self.spinner.pack(side='left', padx=10)
        self.spinner.set("Epéntesis")
        
        btn_add = ArtButton(controls, text="➕ NUEVO EJEMPLO", 
                          width=150, height=40)
        btn_add.pack(side='left', padx=10)
        
        # Lista scrollable
        container = ttk.Frame(self)
        container.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.canvas = tk.Canvas(container, bg=COLORS['background'], 
                               highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", 
                                 command=self.canvas.yview)
        self.scroll_frame = ttk.Frame(self.canvas)
        
        self.scroll_frame.bind("<Configure>", 
                             lambda e: self.canvas.configure(
                                 scrollregion=self.canvas.bbox("all")))
        
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Cargar ejemplos
        self.load_examples()
    
    def load_examples(self):
        for i in range(15):
            example = ExampleItem(self.scroll_frame, 
                                 verb="Agradecer", 
                                 conjugation="agradezco", 
                                 example="Yo agradezco tu ayuda siempre")
            example.pack(fill='x', pady=5, padx=5)

if __name__ == "__main__":
    app = VerbosArtApp()
    app.mainloop()
