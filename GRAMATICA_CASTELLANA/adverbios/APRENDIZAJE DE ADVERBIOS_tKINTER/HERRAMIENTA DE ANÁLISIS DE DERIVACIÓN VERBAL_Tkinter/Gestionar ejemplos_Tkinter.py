import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

DATA_FILE = "verbos_tkinter.json"
CATEGORIAS = {
    '1': "Epéntesis (Inserción consonántica)",
    '2': "Síncopa y Epéntesis en Futuro/Condicional",
    '3': "Alternancias Consonánticas/Vocálicas",
    '4': "Pretéritos Fuertes",
    '5': "Participios Irregulares",
    '6': "Verbos de Conjugación Especial",
    '7': "Verbos Defectivos"
}

class VerbosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Verbos Conjugados")
        self.root.geometry("800x600")
        
        self.datos = self.cargar_datos()
        self.categoria_actual = tk.StringVar(value='1')
        self.crear_interfaz()
    
    def cargar_datos(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {k: [] for k in CATEGORIAS}
    
    def guardar_datos(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.datos, f, indent=2)
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo (Categorías y Progreso)
        left_panel = ttk.Frame(main_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(left_panel, text="Categorías:").pack(pady=5)
        self.categoria_combobox = ttk.Combobox(
            left_panel, 
            values=list(CATEGORIAS.values()),
            textvariable=self.categoria_actual,
            state="readonly"
        )
        self.categoria_combobox.pack(pady=5)
        self.categoria_combobox.bind("<<ComboboxSelected>>", self.actualizar_lista)
        
        ttk.Button(left_panel, text="Agregar Ejemplo", command=self.agregar_ejemplo).pack(pady=5)
        ttk.Button(left_panel, text="Editar Ejemplo", command=self.editar_ejemplo).pack(pady=5)
        ttk.Button(left_panel, text="Eliminar Ejemplo", command=self.eliminar_ejemplo).pack(pady=5)
        ttk.Button(left_panel, text="Ver Progreso", command=self.mostrar_progreso).pack(pady=5)
        
        # Panel derecho (Lista de ejemplos)
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.lista = tk.Listbox(right_panel, width=60, height=20)
        self.lista.pack(fill=tk.BOTH, expand=True, pady=5)
        scrollbar = ttk.Scrollbar(right_panel, orient=tk.VERTICAL, command=self.lista.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista.config(yscrollcommand=scrollbar.set)
        
        self.actualizar_lista()
    
    def actualizar_lista(self, event=None):
        self.lista.delete(0, tk.END)
        cat = self.get_categoria_actual()
        for ejemplo in self.datos[cat]:
            texto = f"{ejemplo['verbo']}: {ejemplo['ejemplo']}"
            self.lista.insert(tk.END, texto)
    
    def get_categoria_actual(self):
        return str(list(CATEGORIAS.keys())[
            list(CATEGORIAS.values()).index(self.categoria_actual.get())
        ])
    
    def agregar_ejemplo(self):
        cat = self.get_categoria_actual()
        if len(self.datos[cat]) >= 100:
            messagebox.showwarning("Límite alcanzado", "¡Ya hay 100 ejemplos en esta categoría!")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Nuevo Ejemplo")
        
        ttk.Label(dialog, text="Verbo en infinitivo:").grid(row=0, column=0, padx=5, pady=5)
        verbo_entry = ttk.Entry(dialog, width=30)
        verbo_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(dialog, text="Conjugación:").grid(row=1, column=0, padx=5, pady=5)
        conjugacion_entry = ttk.Entry(dialog, width=30)
        conjugacion_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(dialog, text="Oración de ejemplo:").grid(row=2, column=0, padx=5, pady=5)
        ejemplo_entry = ttk.Entry(dialog, width=30)
        ejemplo_entry.grid(row=2, column=1, padx=5, pady=5)
        
        def guardar():
            nuevo = {
                "id": len(self.datos[cat]) + 1,
                "verbo": verbo_entry.get(),
                "conjugacion": conjugacion_entry.get(),
                "ejemplo": ejemplo_entry.get()
            }
            self.datos[cat].append(nuevo)
            self.guardar_datos()
            self.actualizar_lista()
            dialog.destroy()
            messagebox.showinfo("Éxito", "Ejemplo agregado correctamente")
        
        ttk.Button(dialog, text="Guardar", command=guardar).grid(row=3, column=1, pady=10)
    
    def editar_ejemplo(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor seleccione un ejemplo")
            return
        
        index = seleccion[0]
        cat = self.get_categoria_actual()
        ejemplo = self.datos[cat][index]
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Editar Ejemplo")
        
        ttk.Label(dialog, text="Verbo en infinitivo:").grid(row=0, column=0, padx=5, pady=5)
        verbo_entry = ttk.Entry(dialog, width=30)
        verbo_entry.insert(0, ejemplo['verbo'])
        verbo_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(dialog, text="Conjugación:").grid(row=1, column=0, padx=5, pady=5)
        conjugacion_entry = ttk.Entry(dialog, width=30)
        conjugacion_entry.insert(0, ejemplo['conjugacion'])
        conjugacion_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(dialog, text="Oración de ejemplo:").grid(row=2, column=0, padx=5, pady=5)
        ejemplo_entry = ttk.Entry(dialog, width=30)
        ejemplo_entry.insert(0, ejemplo['ejemplo'])
        ejemplo_entry.grid(row=2, column=1, padx=5, pady=5)
        
        def actualizar():
            ejemplo['verbo'] = verbo_entry.get()
            ejemplo['conjugacion'] = conjugacion_entry.get()
            ejemplo['ejemplo'] = ejemplo_entry.get()
            self.guardar_datos()
            self.actualizar_lista()
            dialog.destroy()
            messagebox.showinfo("Éxito", "Ejemplo actualizado correctamente")
        
        ttk.Button(dialog, text="Actualizar", command=actualizar).grid(row=3, column=1, pady=10)
    
    def eliminar_ejemplo(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor seleccione un ejemplo")
            return
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este ejemplo?"):
            index = seleccion[0]
            cat = self.get_categoria_actual()
            del self.datos[cat][index]
            self.guardar_datos()
            self.actualizar_lista()
    
    def mostrar_progreso(self):
        progress = tk.Toplevel(self.root)
        progress.title("Progreso")
        
        total = 0
        for cat in CATEGORIAS:
            total += len(self.datos[cat])
        
        ttk.Label(progress, text="Progreso General", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=10)
        ttk.Label(progress, text=f"Total: {total}/700 ({total/700:.0%})").grid(row=1, column=0, pady=5)
        
        for i, (key, cat) in enumerate(CATEGORIAS.items()):
            ttk.Label(progress, text=f"{cat}:").grid(row=i+2, column=0, sticky=tk.W, padx=10)
            ttk.Label(progress, text=f"{len(self.datos[key])}/100").grid(row=i+2, column=1, padx=10)
        
        ttk.Button(progress, text="Cerrar", command=progress.destroy).grid(row=9, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = VerbosApp(root)
    root.mainloop()
