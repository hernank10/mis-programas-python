import tkinter as tk
from tkinter import ttk, messagebox
from gestor_datos import cargar_datos, guardar_datos
from tts import leer_texto

datos = cargar_datos()

CATEGORIAS = [
    "1. b/v", "2. c/s/z", "3. g/j", "4. h", "5. dígrafos",
    "6. diptongos/hiatos", "7. tilde", "8. homófonas/etimológicas", "9. yeísmo"
]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercitador Ortográfico con Tkinter")
        self.geometry("600x500")

        self.categoria_var = tk.StringVar(value=CATEGORIAS[0])
        self.ejemplo_var = tk.StringVar()
        self.explicacion_var = tk.StringVar()

        self.create_widgets()
        self.mostrar_ejemplos()

    def create_widgets(self):
        frame_top = ttk.Frame(self)
        frame_top.pack(pady=10)

        ttk.Label(frame_top, text="Categoría:").pack(side="left")
        ttk.OptionMenu(frame_top, self.categoria_var, CATEGORIAS[0], *CATEGORIAS, command=lambda _: self.mostrar_ejemplos()).pack(side="left", padx=10)

        frame_ejemplo = ttk.Frame(self)
        frame_ejemplo.pack(pady=10)

        ttk.Label(frame_ejemplo, text="Palabra o ejemplo:").grid(row=0, column=0)
        ttk.Entry(frame_ejemplo, textvariable=self.ejemplo_var, width=40).grid(row=0, column=1)

        ttk.Label(frame_ejemplo, text="Explicación:").grid(row=1, column=0)
        ttk.Entry(frame_ejemplo, textvariable=self.explicacion_var, width=40).grid(row=1, column=1)

        ttk.Button(self, text="Agregar ejemplo", command=self.agregar_ejemplo).pack(pady=5)

        self.lista = tk.Listbox(self, width=70, height=15)
        self.lista.pack(pady=10)
        self.lista.bind("<Double-1>", self.leer_seleccionado)

        ttk.Button(self, text="Eliminar seleccionado", command=self.eliminar_ejemplo).pack(pady=5)

    def mostrar_ejemplos(self):
        self.lista.delete(0, tk.END)
        categoria = self.categoria_var.get()
        ejemplos = datos.get(categoria, [])
        for ej in ejemplos:
            self.lista.insert(tk.END, f"{ej['palabra']} → {ej['explicacion']}")

    def agregar_ejemplo(self):
        cat = self.categoria_var.get()
        palabra = self.ejemplo_var.get().strip()
        explicacion = self.explicacion_var.get().strip()
        if not palabra or not explicacion:
            messagebox.showwarning("Faltan datos", "Completa ambos campos.")
            return
        datos.setdefault(cat, []).append({"palabra": palabra, "explicacion": explicacion})
        guardar_datos(datos)
        self.ejemplo_var.set("")
        self.explicacion_var.set("")
        self.mostrar_ejemplos()

    def eliminar_ejemplo(self):
        sel = self.lista.curselection()
        if not sel:
            return
        idx = sel[0]
        cat = self.categoria_var.get()
        del datos[cat][idx]
        guardar_datos(datos)
        self.mostrar_ejemplos()

    def leer_seleccionado(self, event):
        sel = self.lista.curselection()
        if not sel:
            return
        cat = self.categoria_var.get()
        idx = sel[0]
        palabra = datos[cat][idx]["palabra"]
        explicacion = datos[cat][idx]["explicacion"]
        leer_texto(f"{palabra}. {explicacion}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
