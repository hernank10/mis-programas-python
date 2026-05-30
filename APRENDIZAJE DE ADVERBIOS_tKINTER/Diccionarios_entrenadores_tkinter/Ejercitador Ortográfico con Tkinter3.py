import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import json
import os
import pyttsx3

# Inicializar voz
engine = pyttsx3.init()

# Archivo de almacenamiento
DATA_FILE = "ejemplos_ortografia.json"

# Categorías
categorias = {
    "1": "Palabras con b y v",
    "2": "Palabras con c, s, z",
    "3": "Palabras con g, j",
    "4": "Palabras con ll y y (yeísmo)",
    "5": "Palabras con h (muda)",
    "6": "Palabras con dígrafos (ch, ll, rr, gu, qu)",
    "7": "Palabras con diptongos y hiatos",
    "8": "Palabras con tilde (acentuación)",
    "9": "Palabras homófonas y etimológicas"
}

# Cargar o crear archivo de datos
def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {nombre: [] for nombre in categorias.values()}

# Guardar datos
def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Leer en voz alta
def leer_voz(texto):
    engine.say(texto)
    engine.runAndWait()

# Clase principal de la aplicación
class OrtografiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplos Ortográficos")
        self.datos = cargar_datos()
        
        # Interfaz
        self.crear_widgets()

    def crear_widgets(self):
        self.categoria_var = tk.StringVar()
        self.categoria_menu = ttk.Combobox(self.root, values=list(categorias.values()), textvariable=self.categoria_var, width=50)
        self.categoria_menu.grid(row=0, column=0, columnspan=3, pady=10)
        self.categoria_menu.set("Selecciona una categoría...")

        self.lista = tk.Listbox(self.root, width=60, height=15)
        self.lista.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        ttk.Button(self.root, text="Ver ejemplos", command=self.ver_ejemplos).grid(row=2, column=0)
        ttk.Button(self.root, text="Agregar", command=self.agregar).grid(row=2, column=1)
        ttk.Button(self.root, text="Editar", command=self.editar).grid(row=2, column=2)
        ttk.Button(self.root, text="Escuchar", command=self.escuchar).grid(row=3, column=0)
        ttk.Button(self.root, text="Progreso", command=self.progreso).grid(row=3, column=1)
        ttk.Button(self.root, text="Guardar y salir", command=self.salir).grid(row=3, column=2)

    def obtener_categoria(self):
        cat = self.categoria_var.get()
        if cat not in self.datos:
            messagebox.showwarning("Aviso", "Selecciona una categoría válida.")
            return None
        return cat

    def ver_ejemplos(self):
        cat = self.obtener_categoria()
        if not cat: return
        self.lista.delete(0, tk.END)
        for ejemplo in self.datos[cat]:
            self.lista.insert(tk.END, ejemplo)

    def agregar(self):
        cat = self.obtener_categoria()
        if not cat: return
        nuevo = simpledialog.askstring("Nuevo ejemplo", f"Ingresar ejemplo para '{cat}':")
        if nuevo:
            self.datos[cat].append(nuevo)
            self.ver_ejemplos()

    def editar(self):
        cat = self.obtener_categoria()
        if not cat: return
        sel = self.lista.curselection()
        if not sel:
            messagebox.showinfo("Editar", "Selecciona un ejemplo para editar.")
            return
        idx = sel[0]
        actual = self.datos[cat][idx]
        nuevo = simpledialog.askstring("Editar ejemplo", f"Editar ejemplo:", initialvalue=actual)
        if nuevo:
            self.datos[cat][idx] = nuevo
            self.ver_ejemplos()

    def escuchar(self):
        cat = self.obtener_categoria()
        if not cat: return
        for ejemplo in self.datos[cat]:
            leer_voz(ejemplo)

    def progreso(self):
        progreso_texto = "\n".join(f"{cat}: {len(ejs)} ejemplos" for cat, ejs in self.datos.items())
        messagebox.showinfo("Progreso", progreso_texto)

    def salir(self):
        guardar_datos(self.datos)
        self.root.destroy()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = OrtografiaApp(root)
    root.mainloop()
