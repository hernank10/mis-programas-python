import tkinter as tk
from tkinter import ttk, messagebox
import random

# Lista completa de palabras (completa con tus 100 términos)
palabras = [
    {"prefijo": "ante", "base": "brazo", "categoria": "Locativos", "palabra": "antebrazo"},
    {"prefijo": "sub", "base": "terráneo", "categoria": "Locativos", "palabra": "subterráneo"},
    {"prefijo": "pre", "base": "democrático", "categoria": "Temporales", "palabra": "predemocrático"},
    {"prefijo": "pos", "base": "guerra", "categoria": "Temporales", "palabra": "posguerra"},
    {"prefijo": "bi", "base": "lingüe", "categoria": "Cuantificativos", "palabra": "bilingüe"},
    {"prefijo": "multi", "base": "color", "categoria": "Cuantificativos", "palabra": "multicolor"},
    {"prefijo": "hiper", "base": "activo", "categoria": "Gradativos", "palabra": "hiperactivo"},
    {"prefijo": "super", "base": "población", "categoria": "Gradativos", "palabra": "superpoblación"},
    {"prefijo": "in", "base": "útil", "categoria": "Negativos", "palabra": "inútil"},
    {"prefijo": "des", "base": "orden", "categoria": "Negativos", "palabra": "desorden"},
]

class AprendePrefijosApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprende Prefijos Españoles")
        self.geometry("800x600")
        self.configure(padx=20, pady=20)
        
        self.categorias = list(set([p["categoria"] for p in palabras]))
        self.categorias.sort()
        
        self.palabras_filtradas = []
        self.current_question = 0
        self.score = 0
        self.errors = []
        
        self.crear_widgets_iniciales()
        
    def crear_widgets_iniciales(self):
        self.clear_frame()
        
        self.lbl_titulo = ttk.Label(self, text="Selecciona las categorías:", font=('Arial', 14, 'bold'))
        self.lbl_titulo.pack(pady=10)
        
        self.cat_vars = {}
        for cat in self.categorias:
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self, text=cat, variable=var)
            chk.pack(anchor='w', padx=20, pady=5)
            self.cat_vars[cat] = var
            
        self.btn_iniciar = ttk.Button(self, text="Iniciar Práctica", command=self.iniciar_practica)
        self.btn_iniciar.pack(pady=20)
        
    def iniciar_practica(self):
        categorias_seleccionadas = [cat for cat, var in self.cat_vars.items() if var.get()]
        
        if not categorias_seleccionadas:
            messagebox.showwarning("Selección requerida", "Por favor selecciona al menos una categoría")
            return
            
        self.palabras_filtradas = [p for p in palabras if p["categoria"] in categorias_seleccionadas]
        random.shuffle(self.palabras_filtradas)
        
        if not self.palabras_filtradas:
            messagebox.showinfo("Sin palabras", "No hay palabras en las categorías seleccionadas")
            return
            
        self.mostrar_pregunta()
        
    def mostrar_pregunta(self):
        self.clear_frame()
        
        if self.current_question >= len(self.palabras_filtradas):
            self.mostrar_resultados()
            return
            
        pregunta = self.palabras_filtradas[self.current_question]
        
        # Marco principal
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill='both')
        
        # Cabecera
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill='x', pady=10)
        
        ttk.Label(header_frame, text=f"Pregunta {self.current_question + 1}/{len(self.palabras_filtradas)}", 
                 font=('Arial', 12)).pack(side='left')
        
        ttk.Label(header_frame, text=f"Puntuación: {self.score}", 
                 font=('Arial', 12)).pack(side='right')
        
        # Cuerpo de la pregunta
        body_frame = ttk.Frame(main_frame)
        body_frame.pack(expand=True, pady=20)
        
        ttk.Label(body_frame, text="Categoría:", font=('Arial', 12, 'bold')).pack()
        ttk.Label(body_frame, text=pregunta["categoria"], font=('Arial', 14)).pack(pady=5)
        
        ttk.Label(body_frame, text="Palabra base:", font=('Arial', 12, 'bold')).pack()
        ttk.Label(body_frame, text=pregunta["base"].capitalize(), font=('Arial', 16)).pack(pady=10)
        
        self.entrada_prefijo = ttk.Entry(body_frame, font=('Arial', 14))
        self.entrada_prefijo.pack(pady=10)
        self.entrada_prefijo.bind('<Return>', lambda e: self.verificar_respuesta(pregunta))
        
        ttk.Button(body_frame, text="Verificar", 
                  command=lambda: self.verificar_respuesta(pregunta)).pack(pady=10)
        
    def verificar_respuesta(self, pregunta):
        respuesta = self.entrada_prefijo.get().strip().lower()
        correcto = pregunta["prefijo"].lower()
        
        if respuesta == correcto:
            self.score += 1
            msg = "✅ Correcto!"
            color = "green"
        else:
            self.errors.append({
                'palabra': pregunta["palabra"],
                'tu_respuesta': respuesta,
                'correcto': correcto
            })
            msg = f"❌ Incorrecto. Correcto: {correcto}"
            color = "red"
            
        # Mostrar feedback
        feedback = ttk.Label(self, text=msg, font=('Arial', 14, 'bold'), foreground=color)
        feedback.pack(pady=10)
        self.after(1500, feedback.destroy)
        
        self.current_question += 1
        self.mostrar_pregunta()
        
    def mostrar_resultados(self):
        self.clear_frame()
        
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="🏁 Resultados Finales", font=('Arial', 16, 'bold')).pack(pady=10)
        
        ttk.Label(main_frame, 
                 text=f"Puntuación: {self.score}/{len(self.palabras_filtradas)}",
                 font=('Arial', 14)).pack(pady=10)
                 
        if self.errors:
            ttk.Label(main_frame, text="Errores:", font=('Arial', 12, 'bold')).pack(pady=10)
            error_frame = ttk.Frame(main_frame)
            error_frame.pack(fill='both', expand=True)
            
            for i, error in enumerate(self.errors, 1):
                texto = f"{i}. {error['palabra']}: Tú: '{error['tu_respuesta']}' | Correcto: '{error['correcto']}'"
                ttk.Label(error_frame, text=texto, foreground='red').pack(anchor='w')
                
        ttk.Button(main_frame, text="Volver a Jugar", command=self.resetear_juego).pack(pady=20)
        ttk.Button(main_frame, text="Salir", command=self.destroy).pack(pady=10)
        
    def resetear_juego(self):
        self.current_question = 0
        self.score = 0
        self.errors = []
        self.crear_widgets_iniciales()
        
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = AprendePrefijosApp()
    app.mainloop()
