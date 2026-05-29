import json
import tkinter as tk
from tkinter import ttk, messagebox

ARCHIVO_DATOS = "ejemplos_morfologia.json"

# Datos iniciales con 10 ejemplos
DATOS_INICIALES = {
    "prefijos": [
        {"palabra": "Antinuclear", "prefijo": "anti-", "clasificacion": "Oposición", "significado": "Contra energía nuclear"},
        {"palabra": "Deshacer", "prefijo": "des-", "clasificacion": "Negación", "significado": "Revertir acción"},
        {"palabra": "Reescribir", "prefijo": "re-", "clasificacion": "Repetición", "significado": "Escribir de nuevo"},
        {"palabra": "Subdirector", "prefijo": "sub-", "clasificacion": "Posición", "significado": "Director secundario"},
        {"palabra": "Superpoblación", "prefijo": "super-", "clasificacion": "Exceso", "significado": "Exceso de población"}
    ],
    "composiciones": [
        {"palabra": "Sacacorchos", "tipo": "Verbo+Sustantivo", "clasificacion": "Objeto-función", "significado": "Herramienta para corchos"},
        {"palabra": "Agridulce", "tipo": "Adjetivo+Adjetivo", "clasificacion": "Característica", "significado": "Mezcla de sabores"},
        {"palabra": "Guardarropa", "tipo": "Verbo+Sustantivo", "clasificacion": "Objeto", "significado": "Mueble para ropa"},
        {"palabra": "Bienvenido", "tipo": "Adverbio+Participio", "clasificacion": "Saludo", "significado": "Recibir con agrado"},
        {"palabra": "Cortocircuito", "tipo": "Adjetivo+Sustantivo", "clasificacion": "Fenómeno", "significado": "Fallo eléctrico"}
    ]
}

class AplicacionMorfologia(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor Morfológico con Ejemplos")
        self.geometry("1000x600")
        
        self.datos = self.cargar_datos()
        self.crear_interfaz()
        self.actualizar_tablas()
        
    def cargar_datos(self):
        try:
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return DATOS_INICIALES
    
    def guardar_datos(self):
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, ensure_ascii=False, indent=2)
    
    def crear_interfaz(self):
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestañas
        self.crear_pestania("Prefijación", "prefijos", ["Palabra", "Prefijo", "Clasificación", "Significado"])
        self.crear_pestania("Composición", "composiciones", ["Palabra", "Tipo", "Clasificación", "Significado"])
        
        # Barra de herramientas
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack(pady=10)
        
        botones = [
            ("Añadir", self.aniadir_ejemplo),
            ("Editar", self.editar_ejemplo),
            ("Eliminar", self.eliminar_ejemplo),
            ("Guardar", self.guardar_datos)
        ]
        
        for texto, comando in botones:
            ttk.Button(self.frame_botones, text=texto, command=comando).pack(side=tk.LEFT, padx=5)
    
    def crear_pestania(self, titulo, tipo, columnas):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=titulo)
        
        # Tabla
        tabla = ttk.Treeview(frame, columns=columnas, show="headings", selectmode="browse")
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=200, anchor=tk.W)
        
        # Scrollbar
        scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
        tabla.configure(yscroll=scroll.set)
        
        tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        setattr(self, f"tabla_{tipo}", tabla)
    
    def actualizar_tablas(self):
        for tipo in ["prefijos", "composiciones"]:
            tabla = getattr(self, f"tabla_{tipo}")
            tabla.delete(*tabla.get_children())
            
            for item in self.datos[tipo]:
                valores = [item[col.lower().replace("ó", "o")] for col in tabla["columns"]]
                tabla.insert("", tk.END, values=valores)
    
    # Resto de funciones (añadir, editar, eliminar) igual que antes...

if __name__ == "__main__":
    app = AplicacionMorfologia()
    app.mainloop()
