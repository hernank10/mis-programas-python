import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext

class SintaxisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Sintaxis Española")
        self.root.geometry("800x600")
        
        self.estructuras = self.cargar_datos()
        self.ejemplos_guardados = self.cargar_ejemplos()
        
        self.crear_menu_principal()
    
    def cargar_datos(self):
        return {
            "Adjetivo modificado": {
                "definicion": "Modificado por adverbios, complementos o proposiciones",
                "ejemplos": [
                    {"texto": "muy prudente", "modificador": "muy", "tipo": "adverbio"},
                    {"texto": "abundante de frutos", "modificador": "de frutos", "tipo": "complemento"}
                ]
            },
            # ... (otros datos similares)
        }
    
    def cargar_ejemplos(self):
        if os.path.exists("ejemplos.json"):
            with open("ejemplos.json", "r") as f:
                return json.load(f)
        return {}
    
    def guardar_ejemplos(self):
        with open("ejemplos.json", "w") as f:
            json.dump(self.ejemplos_guardados, f)
    
    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        ttk.Label(main_frame, text="PRÁCTICA DE SINTAXIS", font=("Arial", 16)).pack(pady=10)
        
        botones = [
            ("Ver Diapositivas", self.mostrar_diapositivas),
            ("Practicar Modificaciones", self.practicar_modificaciones),
            ("Identificar Palabras", self.identificar_palabras),
            ("Gestionar Ejemplos", self.gestionar_ejemplos),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones:
            ttk.Button(main_frame, text=texto, command=comando).pack(fill="x", pady=5)

    def mostrar_diapositivas(self):
        self.limpiar_pantalla()
        
        diapositiva_frame = ttk.Frame(self.root)
        diapositiva_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.current_slide = 0
        self.slides = list(self.estructuras.items()) + list(self.ejemplos_guardados.items())
        
        self.slide_label = ttk.Label(diapositiva_frame, font=("Arial", 14, "bold"))
        self.slide_label.pack(pady=10)
        
        self.content_text = scrolledtext.ScrolledText(diapositiva_frame, wrap=tk.WORD, height=15)
        self.content_text.pack(fill="both", expand=True)
        
        nav_frame = ttk.Frame(diapositiva_frame)
        nav_frame.pack(pady=10)
        
        ttk.Button(nav_frame, text="Anterior", command=self.slide_anterior).pack(side="left", padx=5)
        ttk.Button(nav_frame, text="Siguiente", command=self.slide_siguiente).pack(side="left", padx=5)
        ttk.Button(nav_frame, text="Volver", command=self.crear_menu_principal).pack(side="right", padx=5)
        
        self.actualizar_diapositiva()
    
    def actualizar_diapositiva(self):
        if self.slides:
            categoria, datos = self.slides[self.current_slide]
            self.slide_label.config(text=categoria)
            self.content_text.delete(1.0, tk.END)
            contenido = f"Definición: {datos['definicion']}\n\nEjemplos:\n"
            for ejemplo in datos['ejemplos']:
                contenido += f"- {ejemplo['texto']} (Modificador: {ejemplo['modificador']})\n"
            self.content_text.insert(tk.END, contenido)
    
    def slide_siguiente(self):
        if self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self.actualizar_diapositiva()
    
    def slide_anterior(self):
        if self.current_slide > 0:
            self.current_slide -= 1
            self.actualizar_diapositiva()
    
    def practicar_modificaciones(self):
        self.limpiar_pantalla()
        
        practice_frame = ttk.Frame(self.root)
        practice_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.ejemplo_actual = 0
        self.ejemplos = [ej for cat in self.estructuras.values() for ej in cat['ejemplos']]
        
        ttk.Label(practice_frame, text="Reescribe el ejemplo subrayando el modificador (usa **)", 
                 font=("Arial", 12)).pack(pady=10)
        
        self.ejemplo_label = ttk.Label(practice_frame, font=("Arial", 14))
        self.ejemplo_label.pack(pady=10)
        
        self.respuesta_entry = ttk.Entry(practice_frame, width=50)
        self.respuesta_entry.pack(pady=10)
        
        feedback_frame = ttk.Frame(practice_frame)
        feedback_frame.pack(pady=10)
        
        ttk.Button(feedback_frame, text="Verificar", command=self.verificar_respuesta).pack(side="left", padx=5)
        ttk.Button(feedback_frame, text="Volver", command=self.crear_menu_principal).pack(side="right", padx=5)
        
        self.mostrar_siguiente_ejemplo()
    
    def mostrar_siguiente_ejemplo(self):
        if self.ejemplo_actual < len(self.ejemplos):
            ejemplo = self.ejemplos[self.ejemplo_actual]
            self.ejemplo_label.config(text=ejemplo['texto'])
            self.respuesta_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Fin", "¡Has completado todos los ejemplos!")
            self.crear_menu_principal()
    
    def verificar_respuesta(self):
        # ... (similar al código original con Tkinter)
    
    # ... (resto de funciones similares adaptadas a Tkinter)
    
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SintaxisApp(root)
    root.mainloop()
