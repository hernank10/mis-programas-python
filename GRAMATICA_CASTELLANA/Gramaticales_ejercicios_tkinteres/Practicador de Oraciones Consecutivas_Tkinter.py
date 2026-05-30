import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import random

# Datos de ejemplo (estructura completa en versión final)
CONSEJOS = {
    "Estructura Básica": [
        {"tipo": "consejo", "texto": "Usa 'tan' con adjetivos", 
         "ejemplo": "Es [tan] brillante [que] deslumbra", "elementos": ["tan", "que"]}
    ]
}

EJEMPLOS = {
    "Intensidad": [
        {"tipo": "ejemplo", "texto": "El café estaba [tan] caliente [que] quemó", 
         "elementos": ["tan", "que"]}
    ]
}

class SpanishTutorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Practicador de Oraciones Consecutivas")
        self.geometry("800x600")
        self.progreso = self.cargar_progreso()
        
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.frames = {}
        for F in (MainMenu, CategorySelection, PracticeScreen):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.mostrar_frame(MainMenu)
        
    def mostrar_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.actualizar_interfaz()
    
    def cargar_progreso(self):
        try:
            with open('progreso.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {
                'consejos': set(),
                'ejemplos': set(),
                'puntuacion': 0
            }
    
    def guardar_progreso(self):
        with open('progreso.pkl', 'wb') as f:
            pickle.dump(self.progreso, f)

class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ttk.Label(self, text="Practicador de Oraciones Consecutivas", 
                 font=('Arial', 16)).pack(pady=20)
        
        self.btn_consejos = ttk.Button(self, text="Practicar Consejos",
                                      command=lambda: controller.mostrar_frame(CategorySelection))
        self.btn_consejos.pack(pady=10)
        
        self.btn_ejemplos = ttk.Button(self, text="Practicar Ejemplos",
                                      command=lambda: controller.mostrar_frame(CategorySelection))
        self.btn_ejemplos.pack(pady=10)
        
        ttk.Button(self, text="Reiniciar Progreso", command=self.reiniciar_progreso).pack(pady=10)
        ttk.Button(self, text="Salir", command=self.controller.destroy).pack(pady=10)
        
        self.lbl_progreso = ttk.Label(self, text="")
        self.lbl_progreso.pack(pady=20)
    
    def actualizar_interfaz(self):
        total_consejos = sum(len(v) for v in CONSEJOS.values())
        total_ejemplos = sum(len(v) for v in EJEMPLOS.values())
        texto = (f"Progreso:\nConsejos: {len(self.controller.progreso['consejos'])}/{total_consejos}\n"
                 f"Ejemplos: {len(self.controller.progreso['ejemplos'])}/{total_ejemplos}\n"
                 f"Puntuación: {self.controller.progreso['puntuacion']}")
        self.lbl_progreso.config(text=texto)
    
    def reiniciar_progreso(self):
        if messagebox.askyesno("Confirmar", "¿Borrar todo el progreso?"):
            self.controller.progreso = {'consejos': set(), 'ejemplos': set(), 'puntuacion': 0}
            self.controller.guardar_progreso()
            self.actualizar_interfaz()

class CategorySelection(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.modo_actual = ""
        
        ttk.Label(self, text="Selecciona una categoría", 
                 font=('Arial', 14)).pack(pady=10)
        
        self.category_list = tk.Listbox(self, width=40, height=15)
        self.category_list.pack(pady=20, padx=20)
        
        ttk.Button(self, text="Seleccionar", command=self.seleccionar_categoria).pack(pady=10)
        ttk.Button(self, text="Regresar", command=lambda: controller.mostrar_frame(MainMenu)).pack()
    
    def actualizar_interfaz(self):
        self.category_list.delete(0, tk.END)
        if self.controller.current_mode == "consejos":
            for categoria in CONSEJOS:
                self.category_list.insert(tk.END, categoria)
        else:
            for categoria in EJEMPLOS:
                self.category_list.insert(tk.END, categoria)
    
    def seleccionar_categoria(self):
        seleccion = self.category_list.curselection()
        if seleccion:
            categoria = self.category_list.get(seleccion[0])
            self.controller.mostrar_frame(PracticeScreen)
            self.controller.frames[PracticeScreen].preparar_ejercicio(categoria)

class PracticeScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.categoria_actual = ""
        self.item_actual = None
        
        self.lbl_instruccion = ttk.Label(self, text="", wraplength=700)
        self.lbl_instruccion.pack(pady=20)
        
        self.lbl_ejemplo = ttk.Label(self, text="", wraplength=700)
        self.lbl_ejemplo.pack(pady=10)
        
        self.entrada_respuesta = ttk.Entry(self, width=50)
        self.entrada_respuesta.pack(pady=20)
        
        self.btn_verificar = ttk.Button(self, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=10)
        
        ttk.Button(self, text="Regresar", command=lambda: controller.mostrar_frame(CategorySelection)).pack()
    
    def preparar_ejercicio(self, categoria):
        self.categoria_actual = categoria
        if self.controller.current_mode == "consejos":
            items = [item for item in CONSEJOS[categoria] 
                    if f"{categoria}-{item['texto']}" not in self.controller.progreso['consejos']]
        else:
            items = [item for item in EJEMPLOS[categoria] 
                    if f"{categoria}-{item['texto']}" not in self.controller.progreso['ejemplos']]
        
        if items:
            self.item_actual = random.choice(items)
            self.mostrar_ejercicio()
        else:
            messagebox.showinfo("Info", "¡Ya completaste esta categoría!")
            self.controller.mostrar_frame(CategorySelection)
    
    def mostrar_ejercicio(self):
        if self.controller.current_mode == "consejos":
            self.lbl_instruccion.config(text="Escribe la regla gramatical correspondiente:")
            self.lbl_ejemplo.config(text=self.item_actual['ejemplo'])
        else:
            self.lbl_instruccion.config(text="Completa los espacios faltantes (separados por coma):")
            ejemplo_oculto = self.item_actual['texto'].replace('[', '___').replace(']', '___')
            self.lbl_ejemplo.config(text=ejemplo_oculto)
        
        self.entrada_respuesta.delete(0, tk.END)
    
    def verificar_respuesta(self):
        respuesta = self.entrada_respuesta.get().strip()
        if self.controller.current_mode == "consejos":
            correcto = respuesta.lower() == self.item_actual['texto'].lower()
        else:
            correcto = all(p.lower() in respuesta.lower().split(',') 
                          for p in self.item_actual['elementos'])
        
        if correcto:
            self.controller.progreso['puntuacion'] += 10
            if self.controller.current_mode == "consejos":
                self.controller.progreso['consejos'].add(f"{self.categoria_actual}-{self.item_actual['texto']}")
            else:
                self.controller.progreso['ejemplos'].add(f"{self.categoria_actual}-{self.item_actual['texto']}")
            
            self.controller.guardar_progreso()
            messagebox.showinfo("Correcto", "¡Respuesta correcta! +10 puntos")
            self.preparar_ejercicio(self.categoria_actual)
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era: {', '.join(self.item_actual['elementos']}")

if __name__ == "__main__":
    app = SpanishTutorApp()
    app.mainloop()
