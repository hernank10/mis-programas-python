import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

ARCHIVO_DATOS = "ejemplos_morfologia.json"

class AplicacionMorfologia(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Ejemplos Morfológicos")
        self.geometry("1000x600")
        
        self.datos = self.cargar_datos()
        self.crear_interfaz()
        
    def cargar_datos(self):
        try:
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"prefijos": [], "composiciones": []}
    
    def guardar_datos(self):
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, ensure_ascii=False, indent=2)
    
    def crear_interfaz(self):
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña Prefijos
        self.frame_prefijos = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_prefijos, text="Prefijación")
        self.crear_tabla(self.frame_prefijos, "prefijos", ["Palabra", "Prefijo", "Clasificación", "Significado"])
        
        # Pestaña Composición
        self.frame_composiciones = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_composiciones, text="Composición")
        self.crear_tabla(self.frame_composiciones, "composiciones", ["Palabra", "Tipo", "Clasificación", "Significado"])
        
        # Botones de control
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack(pady=10)
        
        ttk.Button(self.frame_botones, text="Añadir", command=self.aniadir_ejemplo).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Editar", command=self.editar_ejemplo).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar", command=self.eliminar_ejemplo).grid(row=0, column=2, padx=5)
        ttk.Button(self.frame_botones, text="Guardar", command=self.guardar_datos).grid(row=0, column=3, padx=5)
    
    def crear_tabla(self, padre, tipo, columnas):
        # Treeview
        self.tabla = ttk.Treeview(padre, columns=columnas, show="headings", selectmode="browse")
        
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150, anchor=tk.W)
        
        # Scrollbar
        scroll = ttk.Scrollbar(padre, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scroll.set)
        
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Cargar datos
        self.actualizar_tabla(tipo)
    
    def actualizar_tabla(self, tipo):
        tabla = self.get_tabla_actual()
        tabla.delete(*tabla.get_children())
        
        for item in self.datos[tipo]:
            valores = [item[col.lower()] for col in tabla["columns"]]
            tabla.insert("", tk.END, values=valores)
    
    def get_tabla_actual(self):
        tab_id = self.notebook.index(self.notebook.select())
        return [self.tabla_prefijos, self.tabla_composiciones][tab_id]
    
    def aniadir_ejemplo(self):
        tipo = "prefijos" if self.notebook.index(self.notebook.select()) == 0 else "composiciones"
        campos = self.get_campos_por_tipo(tipo)
        
        ventana = tk.Toplevel(self)
        ventana.title("Nuevo Ejemplo")
        
        entries = {}
        for i, campo in enumerate(campos):
            ttk.Label(ventana, text=f"{campo.capitalize()}:").grid(row=i, column=0, padx=5, pady=5)
            entries[campo] = ttk.Entry(ventana, width=30)
            entries[campo].grid(row=i, column=1, padx=5, pady=5)
        
        def guardar():
            nuevo_item = {campo: entries[campo].get() for campo in campos}
            if all(nuevo_item.values()):
                self.datos[tipo].append(nuevo_item)
                self.actualizar_tabla(tipo)
                ventana.destroy()
            else:
                messagebox.showerror("Error", "¡Todos los campos son obligatorios!")
        
        ttk.Button(ventana, text="Guardar", command=guardar).grid(row=len(campos), columnspan=2, pady=10)
    
    def editar_ejemplo(self):
        tabla = self.get_tabla_actual()
        seleccion = tabla.selection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un elemento")
            return
        
        item = tabla.item(seleccion[0])
        valores = item["values"]
        tipo = "prefijos" if self.notebook.index(self.notebook.select()) == 0 else "composiciones"
        campos = self.get_campos_por_tipo(tipo)
        
        ventana = tk.Toplevel(self)
        ventana.title("Editar Ejemplo")
        
        entries = {}
        for i, campo in enumerate(campos):
            ttk.Label(ventana, text=f"{campo.capitalize()}:").grid(row=i, column=0, padx=5, pady=5)
            entries[campo] = ttk.Entry(ventana, width=30)
            entries[campo].insert(0, valores[i])
            entries[campo].grid(row=i, column=1, padx=5, pady=5)
        
        def actualizar():
            nuevos_valores = {campo: entries[campo].get() for campo in campos}
            if all(nuevos_valores.values()):
                index = self.datos[tipo].index(next(item for item in self.datos[tipo] if item[campos[0]] == valores[0]))
                self.datos[tipo][index] = nuevos_valores
                self.actualizar_tabla(tipo)
                ventana.destroy()
            else:
                messagebox.showerror("Error", "¡Todos los campos son obligatorios!")
        
        ttk.Button(ventana, text="Actualizar", command=actualizar).grid(row=len(campos), columnspan=2, pady=10)
    
    def eliminar_ejemplo(self):
        tabla = self.get_tabla_actual()
        seleccion = tabla.selection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un elemento")
            return
        
        if messagebox.askyesno("Confirmar", "¿Eliminar este elemento?"):
            item = tabla.item(seleccion[0])
            valores = item["values"]
            tipo = "prefijos" if self.notebook.index(self.notebook.select()) == 0 else "composiciones"
            
            self.datos[tipo] = [elem for elem in self.datos[tipo] if elem[self.get_campos_por_tipo(tipo)[0]] != valores[0]]
            self.actualizar_tabla(tipo)
    
    def get_campos_por_tipo(self, tipo):
        return ["palabra", "prefijo", "clasificacion", "significado"] if tipo == "prefijos" else ["palabra", "tipo", "clasificacion", "significado"]
    
    def on_closing(self):
        self.guardar_datos()
        self.destroy()

if __name__ == "__main__":
    app = AplicacionMorfologia()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
