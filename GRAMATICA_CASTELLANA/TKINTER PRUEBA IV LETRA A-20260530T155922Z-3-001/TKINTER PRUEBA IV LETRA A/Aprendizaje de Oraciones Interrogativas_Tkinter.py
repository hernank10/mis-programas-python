import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import random

class InterrogativasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Oraciones Interrogativas")
        self.ejemplos = []
        self.cargar_ejemplos()
        
        self.crear_interfaz()
        self.crear_menu()
    
    def cargar_ejemplos(self):
        try:
            with open("ejemplos.json", "r") as f:
                self.ejemplos = json.load(f)
        except FileNotFoundError:
            self.ejemplos = [
                {"oracion": "¿Vienes a la reunión?", "categoria": 1, "tiempo": "presente"},
                {"oracion": "¿Qué hora es?", "categoria": 2, "tiempo": "presente"}
            ]
    
    def guardar_ejemplos(self):
        with open("ejemplos.json", "w") as f:
            json.dump(self.ejemplos, f, indent=2)

    def crear_interfaz(self):
        self.notebook = ttk.Notebook(self.root)
        
        # Pestaña de práctica
        self.pestana_practica = ttk.Frame(self.notebook)
        self.crear_pestana_practica()
        
        # Pestaña de creación de ejemplos
        self.pestana_crear = ttk.Frame(self.notebook)
        self.crear_pestana_crear()
        
        # Pestaña de visualización
        self.pestana_ver = ttk.Frame(self.notebook)
        self.crear_pestana_ver()
        
        self.notebook.add(self.pestana_practica, text="Práctica")
        self.notebook.add(self.pestana_crear, text="Crear Ejemplos")
        self.notebook.add(self.pestana_ver, text="Ver Ejemplos")
        self.notebook.pack(expand=True, fill="both")

    def crear_pestana_practica(self):
        # Widgets para ejercicios
        self.lbl_ejercicio = ttk.Label(self.pestana_practica, text="", font=('Arial', 14))
        self.lbl_ejercicio.pack(pady=20)
        
        self.frame_opciones = ttk.Frame(self.pestana_practica)
        self.frame_opciones.pack(pady=10)
        
        self.btn_opciones = []
        for i in range(1, 5):
            btn = ttk.Button(self.frame_opciones, text=f"Opción {i}", 
                            command=lambda i=i: self.ejecutar_ejercicio(i))
            btn.pack(side="left", padx=5)
            self.btn_opciones.append(btn)
        
        self.txt_teoria = scrolledtext.ScrolledText(self.pestana_practica, width=60, height=10)
        self.txt_teoria.pack(pady=20)
        
        self.actualizar_ejercicio()

    def crear_pestana_crear(self):
        ttk.Label(self.pestana_crear, text="Crear Nuevo Ejemplo").pack(pady=10)
        
        self.entry_oracion = ttk.Entry(self.pestana_crear, width=50)
        self.entry_oracion.pack(pady=5)
        
        self.combo_categoria = ttk.Combobox(self.pestana_crear, values=list(self.obtener_categorias().values()))
        self.combo_categoria.pack(pady=5)
        
        ttk.Button(self.pestana_crear, text="Guardar Ejemplo", command=self.guardar_ejemplo).pack(pady=10)
    
    def crear_pestana_ver(self):
        self.combo_filtro = ttk.Combobox(self.pestana_ver, values=["Todas"] + list(self.obtener_categorias().values()))
        self.combo_filtro.pack(pady=10)
        self.combo_filtro.bind("<<ComboboxSelected>>", self.filtrar_ejemplos)
        
        self.lista_ejemplos = tk.Listbox(self.pestana_ver, width=80, height=20)
        self.lista_ejemplos.pack(pady=10)
        self.actualizar_lista_ejemplos()

    def obtener_categorias(self):
        return {
            1: "Interrogativa Directa Total",
            2: "Interrogativa Parcial",
            # ... completar con todas las categorías
        }
    
    def actualizar_ejercicio(self):
        ejercicio = random.choice(["identificar", "tiempo", "orden", "enfasis"])
        self.lbl_ejercicio.config(text=self.obtener_enunciado_ejercicio(ejercicio))
    
    def ejecutar_ejercicio(self, opcion):
        # Lógica para cada tipo de ejercicio
        pass
    
    def guardar_ejemplo(self):
        nueva_oracion = {
            "oracion": self.entry_oracion.get(),
            "categoria": list(self.obtener_categorias().keys())[self.combo_categoria.current()],
            "tiempo": "presente"
        }
        self.ejemplos.append(nueva_oracion)
        self.guardar_ejemplos()
        messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
    
    def actualizar_lista_ejemplos(self):
        self.lista_ejemplos.delete(0, tk.END)
        for ejemplo in self.ejemplos:
        self.lista_ejemplos.insert(tk.END, f"{ejemplo['oracion']} - {self.obtener_categorias()[ejemplo['categoria']}"])
    
    def filtrar_ejemplos(self, event):
        categoria = self.combo_filtro.get()
        # Lógica de filtrado
        pass
    
    def crear_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

# Funciones adicionales para ejercicios (implementar según necesidad)
def cambiar_tiempo_verbal(oracion):
    # Lógica para modificar tiempos
    return oracion

def invertir_orden(oracion):
    # Lógica para invertir orden
    return oracion

if __name__ == "__main__":
    root = tk.Tk()
    app = InterrogativasApp(root)
    root.geometry("800x600")
    root.mainloop()
