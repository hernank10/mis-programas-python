import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

ARCHIVO_DATOS = "derivados.json"

SUFIJOS = {
    "-dad/-tad": {
        "ejemplos": ["maldad", "lealtad", "novedad"],
        "oraciones": [
            "La {derivado} de {base} es esencial para...",
            "Su {derivado} fue reconocida públicamente."
        ]
    },
    "-idad": {
        "ejemplos": ["facilidad", "realidad", "privacidad"],
        "oraciones": [
            "La {derivado} con que resolvió el problema fue sorprendente.",
            "La {derivado} de los datos es prioritaria."
        ]
    },
    "-ez/-eza": {
        "ejemplos": ["sencillez", "timidez", "belleza"],
        "oraciones": [
            "La {derivado} del material sorprendió a todos.",
            "Su {derivado} contrastaba con su personalidad."
        ]
    },
    "-ura": {
        "ejemplos": ["amargura", "dulzura", "blancura"],
        "oraciones": [
            "La {derivado} de sus palabras dejó una huella profunda.",
            "La {derivado} del paisaje era conmovedora."
        ]
    },
    "-or": {
        "ejemplos": ["verdor", "espesor", "dulzor"],
        "oraciones": [
            "El {derivado} del bosque indicaba la llegada de la primavera.",
            "El {derivado} de la tela garantizaba su calidad."
        ]
    },
    "-icia": {
        "ejemplos": ["avaricia", "malicia", "pericia"],
        "oraciones": [
            "Su {derivado} lo llevó a cometer errores graves.",
            "La {derivado} en su mirada era evidente."
        ]
    }
}

class AplicacionDerivados:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Derivados Nominales")
        self.root.geometry("1200x800")
        
        self.cargar_datos()
        self.crear_interfaz()
        self.actualizar_tabla()
    
    def cargar_datos(self):
        try:
            with open(ARCHIVO_DATOS, "r") as f:
                self.datos = json.load(f)
        except FileNotFoundError:
            self.datos = {"ejemplos": self.generar_ejemplos()}
    
    def generar_ejemplos(self):
        ejemplos = []
        id_ejemplo = 1
        
        bases = ["amable", "rápido", "frío", "duro", "limpio", "valiente", 
                "audaz", "puro", "áspero", "suave", "verde", "caliente"]
        
        for sufijo in SUFIJOS:
            for base in bases:
                if len(ejemplos) >= 100:
                    break
                derivado = f"{base}_{sufijo.replace('/', '_')}_{id_ejemplo}"
                oracion = random.choice(SUFIJOS[sufijo]["oraciones"]).format(base=base, derivado=derivado)
                ejemplos.append({
                    "id": id_ejemplo,
                    "base": base,
                    "sufijo": sufijo,
                    "derivado": derivado,
                    "oracion": oracion,
                    "editado": False
                })
                id_ejemplo += 1
        return ejemplos[:100]
    
    def crear_interfaz(self):
        # Marco principal
        marco_principal = ttk.Frame(self.root)
        marco_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Botones superiores
        marco_botones = ttk.Frame(marco_principal)
        marco_botones.pack(fill=tk.X, pady=5)
        
        ttk.Button(marco_botones, text="Mostrar Tabla de Referencia", 
                  command=self.mostrar_tabla_referencia).pack(side=tk.LEFT, padx=5)
        ttk.Button(marco_botones, text="Generar Nuevos Ejemplos", 
                  command=self.generar_nuevos_ejemplos).pack(side=tk.LEFT, padx=5)
        ttk.Button(marco_botones, text="Guardar", 
                  command=self.guardar_datos).pack(side=tk.RIGHT, padx=5)
        
        # Tabla de ejemplos
        self.tabla = ttk.Treeview(marco_principal, columns=("ID", "Base", "Sufijo", "Derivado", "Oración", "Editado"), 
                                show="headings", selectmode="browse")
        
        # Configurar columnas
        columnas = [
            ("ID", 50),
            ("Base", 100),
            ("Sufijo", 120),
            ("Derivado", 200),
            ("Oración", 500),
            ("Editado", 80)
        ]
        
        for col, width in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=width, anchor=tk.W)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(marco_principal, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        
        # Distribución
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botones inferiores
        marco_botones_inferiores = ttk.Frame(marco_principal)
        marco_botones_inferiores.pack(fill=tk.X, pady=5)
        
        ttk.Button(marco_botones_inferiores, text="Editar", 
                  command=self.editar_ejemplo).pack(side=tk.LEFT, padx=5)
        ttk.Button(marco_botones_inferiores, text="Eliminar", 
                  command=self.eliminar_ejemplo).pack(side=tk.LEFT, padx=5)
        ttk.Button(marco_botones_inferiores, text="Salir", 
                  command=self.root.quit).pack(side=tk.RIGHT, padx=5)
    
    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
        for ej in self.datos["ejemplos"]:
            self.tabla.insert("", tk.END, values=(
                ej["id"],
                ej["base"],
                ej["sufijo"],
                ej["derivado"],
                ej["oracion"],
                "✓" if ej["editado"] else ""
            ))
    
    def mostrar_tabla_referencia(self):
        ventana_referencia = tk.Toplevel(self.root)
        ventana_referencia.title("Tabla de Referencia de Sufijos")
        ventana_referencia.geometry("800x600")
        
        tabla = ttk.Treeview(ventana_referencia, columns=("Sufijo", "Ejemplos", "Plantillas"), 
                           show="headings")
        
        tabla.heading("Sufijo", text="Sufijo")
        tabla.heading("Ejemplos", text="Ejemplos")
        tabla.heading("Plantillas", text="Plantillas de Oraciones")
        
        tabla.column("Sufijo", width=100)
        tabla.column("Ejemplos", width=200)
        tabla.column("Plantillas", width=500)
        
        for sufijo, info in SUFIJOS.items():
            ejemplos = ", ".join(info["ejemplos"])
            plantillas = " | ".join(info["oraciones"])
            tabla.insert("", tk.END, values=(sufijo, ejemplos, plantillas))
        
        scrollbar = ttk.Scrollbar(ventana_referencia, orient=tk.VERTICAL, command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)
        
        tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        ventana_referencia.grab_set()
    
    def editar_ejemplo(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un ejemplo de la tabla")
            return
            
        item = self.tabla.item(seleccion[0])
        valores = item["values"]
        ej_id = valores[0]
        
        ejemplo = next(e for e in self.datos["ejemplos"] if e["id"] == ej_id)
        
        ventana_edicion = tk.Toplevel(self.root)
        ventana_edicion.title("Editar Ejemplo")
        
        # Campos de edición
        tk.Label(ventana_edicion, text="Base:").grid(row=0, column=0, padx=5, pady=5)
        entrada_base = ttk.Entry(ventana_edicion)
        entrada_base.grid(row=0, column=1, padx=5, pady=5)
        entrada_base.insert(0, ejemplo["base"])
        
        tk.Label(ventana_edicion, text="Sufijo:").grid(row=1, column=0, padx=5, pady=5)
        entrada_sufijo = ttk.Combobox(ventana_edicion, values=list(SUFIJOS.keys()))
        entrada_sufijo.grid(row=1, column=1, padx=5, pady=5)
        entrada_sufijo.set(ejemplo["sufijo"])
        
        tk.Label(ventana_edicion, text="Derivado:").grid(row=2, column=0, padx=5, pady=5)
        entrada_derivado = ttk.Entry(ventana_edicion)
        entrada_derivado.grid(row=2, column=1, padx=5, pady=5)
        entrada_derivado.insert(0, ejemplo["derivado"])
        
        tk.Label(ventana_edicion, text="Oración:").grid(row=3, column=0, padx=5, pady=5)
        entrada_oracion = tk.Text(ventana_edicion, width=40, height=4)
        entrada_oracion.grid(row=3, column=1, padx=5, pady=5)
        entrada_oracion.insert(tk.END, ejemplo["oracion"])
        
        def guardar_cambios():
            ejemplo["base"] = entrada_base.get()
            ejemplo["sufijo"] = entrada_sufijo.get()
            ejemplo["derivado"] = entrada_derivado.get()
            ejemplo["oracion"] = entrada_oracion.get("1.0", tk.END).strip()
            ejemplo["editado"] = True
            self.actualizar_tabla()
            ventana_edicion.destroy()
            messagebox.showinfo("Éxito", "Ejemplo actualizado correctamente")
        
        ttk.Button(ventana_edicion, text="Guardar Cambios", 
                  command=guardar_cambios).grid(row=4, column=1, pady=10)
    
    def generar_nuevos_ejemplos(self):
        if messagebox.askyesno("Confirmar", "¿Generar nuevos ejemplos? Se perderán los cambios no guardados"):
            self.datos = {"ejemplos": self.generar_ejemplos()}
            self.actualizar_tabla()
    
    def eliminar_ejemplo(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
            
        item = self.tabla.item(seleccion[0])
        ej_id = item["values"][0]
        
        if messagebox.askyesno("Confirmar", "¿Eliminar este ejemplo?"):
            self.datos["ejemplos"] = [e for e in self.datos["ejemplos"] if e["id"] != ej_id]
            self.actualizar_tabla()
    
    def guardar_datos(self):
        try:
            with open(ARCHIVO_DATOS, "w") as f:
                json.dump(self.datos, f, indent=2)
            messagebox.showinfo("Éxito", "Datos guardados correctamente en derivados.json")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionDerivados(root)
    root.mainloop()
