import json
import random
import tkinter as tk
from tkinter import ttk, messagebox

# Clase principal de la aplicación
class AplicacionSubordinacionAdjetiva(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Subordinación Adjetiva")
        self.geometry("800x600")
        self.ejemplos = self.cargar_ejemplos()
        self.crear_widgets()
    
    def cargar_ejemplos(self):
        try:
            with open('ejemplos.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return [
                {
                    "id": 1,
                    "categoria": "Especificativas",
                    "oracion": "El vestido que compré ayer es azul.",
                    "antecedente": "vestido",
                    "tipo": "especificativa",
                    "funcion_pronombre": "complemento directo",
                    "sustantivizada": "El que compré ayer es azul."
                },
                # ... (Agregar los 100 ejemplos aquí)
            ]
    
    def guardar_ejemplos(self):
        with open('ejemplos.json', 'w') as f:
            json.dump(self.ejemplos, f, indent=4)
    
    def crear_widgets(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Menú de opciones
        self.menu_opciones = ttk.LabelFrame(self.frame_principal, text="Opciones")
        self.menu_opciones.pack(pady=10, padx=10, fill=tk.X)
        
        ttk.Button(self.menu_opciones, text="Ejemplo Aleatorio", command=self.mostrar_ejemplo_aleatorio).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.menu_opciones, text="Por Categoría", command=self.mostrar_selector_categorias).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.menu_opciones, text="Buscar por ID", command=self.mostrar_buscador_id).pack(side=tk.LEFT, padx=5)
        
        # Área de trabajo
        self.area_trabajo = ttk.Frame(self.frame_principal)
        self.area_trabajo.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configurar columnas y filas para expansión
        self.area_trabajo.columnconfigure(0, weight=1)
        self.area_trabajo.rowconfigure(0, weight=1)
    
    def limpiar_area_trabajo(self):
        for widget in self.area_trabajo.winfo_children():
            widget.destroy()
    
    def mostrar_ejemplo_aleatorio(self):
        self.limpiar_area_trabajo()
        ejemplo = random.choice(self.ejemplos)
        self.mostrar_detalles_ejemplo(ejemplo)
    
    def mostrar_selector_categorias(self):
        self.limpiar_area_trabajo()
        categorias = list(set(ej['categoria'] for ej in self.ejemplos))
        
        lbl = ttk.Label(self.area_trabajo, text="Seleccione una categoría:")
        lbl.pack(pady=5)
        
        combo = ttk.Combobox(self.area_trabajo, values=categorias)
        combo.pack(pady=5)
        
        btn = ttk.Button(self.area_trabajo, text="Cargar Ejemplos", 
                        command=lambda: self.mostrar_ejemplos_categoria(combo.get()))
        btn.pack(pady=5)
    
    def mostrar_ejemplos_categoria(self, categoria):
        ejemplos_filtrados = [ej for ej in self.ejemplos if ej['categoria'] == categoria]
        self.limpiar_area_trabajo()
        
        lbl = ttk.Label(self.area_trabajo, text=f"Ejemplos de la categoría '{categoria}':")
        lbl.pack(pady=5)
        
        lista = tk.Listbox(self.area_trabajo)
        for ej in ejemplos_filtrados:
            lista.insert(tk.END, f"ID {ej['id']}: {ej['oracion']}")
        lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        btn = ttk.Button(self.area_trabajo, text="Ver Detalles", 
                        command=lambda: self.mostrar_detalles_ejemplo(self.ejemplos[lista.curselection()[0]]))
        btn.pack(pady=5)
    
    def mostrar_buscador_id(self):
        self.limpiar_area_trabajo()
        
        lbl = ttk.Label(self.area_trabajo, text="Ingrese el ID del ejemplo (1-100):")
        lbl.pack(pady=5)
        
        entry = ttk.Entry(self.area_trabajo)
        entry.pack(pady=5)
        
        btn = ttk.Button(self.area_trabajo, text="Buscar", 
                        command=lambda: self.buscar_por_id(entry.get()))
        btn.pack(pady=5)
    
    def buscar_por_id(self, id_str):
        try:
            id_ej = int(id_str) - 1
            if 0 <= id_ej < len(self.ejemplos):
                self.mostrar_detalles_ejemplo(self.ejemplos[id_ej])
            else:
                messagebox.showerror("Error", "ID fuera de rango.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
    
    def mostrar_detalles_ejemplo(self, ejemplo):
        self.limpiar_area_trabajo()
        
        # Mostrar oración
        lbl_oracion = ttk.Label(self.area_trabajo, text=f"Oración: {ejemplo['oracion']}", wraplength=600)
        lbl_oracion.pack(pady=10)
        
        # Botones de acciones
        frame_botones = ttk.Frame(self.area_trabajo)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Ver Antecedente", 
                  command=lambda: messagebox.showinfo("Antecedente", ejemplo['antecedente'])).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_botones, text="Clasificar", 
                  command=lambda: messagebox.showinfo("Clasificación", ejemplo['tipo'])).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_botones, text="Función del Pronombre", 
                  command=lambda: messagebox.showinfo("Función", ejemplo['funcion_pronombre'])).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_botones, text="Reescribir", 
                  command=lambda: messagebox.showinfo("Reescrita", ejemplo['sustantivizada'])).pack(side=tk.LEFT, padx=5)
    
    def on_closing(self):
        self.guardar_ejemplos()
        self.destroy()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = AplicacionSubordinacionAdjetiva()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
