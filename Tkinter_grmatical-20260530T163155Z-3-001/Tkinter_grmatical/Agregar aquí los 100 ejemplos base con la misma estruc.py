import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import json
import random

class LinguMasterPro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LinguMaster Pro")
        self.geometry("1200x800")
        
        # Configuración inicial
        self.idioma = "es"
        self.ejemplos = []
        self.current_question = 0
        self.score = 0
        
        # Cargar datos
        self.cargar_ejemplos()
        self.cargar_glosario()
        
        # Interfaz
        self.crear_interfaz()
        self.actualizar_ui()

    def cargar_ejemplos(self):
        try:
            with open("ejemplos.json", "r", encoding="utf-8") as f:
                self.ejemplos = json.load(f)
                if len(self.ejemplos) < 100:  # Mantener mínimo 100 ejemplos
                    self.ejemplos += self.ejemplos_base()[:100-len(self.ejemplos)]
        except FileNotFoundError:
            self.ejemplos = self.ejemplos_base()[:100]

    def ejemplos_base(self):
        return [
            # (Agregar aquí los 100 ejemplos base con la misma estructura)
            {
                "es": {
                    "texto": "Juraría que hoy es martes",
                    "pregunta": "¿Qué verbo enunciativo implícito sugiere el ejemplo?",
                    "opciones": {"a": "decir", "b": "jurar", "c": "afirmar"},
                    "respuesta": "b",
                    "retro": "✅ Correcto! 'Juraría' implica el verbo performativo JURAR"
                },
                "en": {
                    "texto": "I would swear today is Tuesday",
                    "pregunta": "What implicit speech act verb does the example suggest?",
                    "opciones": {"a": "say", "b": "swear", "c": "claim"},
                    "respuesta": "b",
                    "retro": "✅ Correct! 'Would swear' implies the performative verb SWEAR"
                }
            },
            # ... (99 ejemplos más)
        ]

    def cargar_glosario(self):
        # ... (Mismo glosario anterior)

    def crear_interfaz(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Notebook principal
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de cuestionario
        self.crear_pestana_quiz()
        
        # Pestaña de glosario
        self.crear_pestana_glosario()
        
        # Pestaña para agregar ejemplos
        self.crear_pestana_editor()
        
        # Barra de herramientas
        self.crear_barra_herramientas()

    def crear_pestana_editor(self):
        self.frame_editor = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_editor, text="")
        
        campos = [
            ("Texto en español:", "entry_es", 50),
            ("Texto en inglés:", "entry_en", 50),
            ("Pregunta (ES):", "entry_pregunta_es", 70),
            ("Pregunta (EN):", "entry_pregunta_en", 70),
            ("Opciones (ES) a/b/c:", "entry_opciones_es", 50),
            ("Opciones (EN) a/b/c:", "entry_opciones_en", 50),
            ("Respuesta correcta:", "entry_respuesta", 10)
        ]
        
        for i, (label, var, width) in enumerate(campos):
            frame = ttk.Frame(self.frame_editor)
            frame.pack(fill=tk.X, padx=20, pady=5)
            
            lbl = ttk.Label(frame, text=label)
            lbl.pack(side=tk.LEFT)
            
            entry = ttk.Entry(frame, width=width)
            entry.pack(side=tk.LEFT, expand=True)
            setattr(self, var, entry)
        
        self.btn_guardar = ttk.Button(self.frame_editor, text="Guardar Ejemplo", command=self.guardar_ejemplo)
        self.btn_guardar.pack(pady=20)

    def guardar_ejemplo(self):
        nuevo_ejemplo = {
            "es": {
                "texto": self.entry_es.get(),
                "pregunta": self.entry_pregunta_es.get(),
                "opciones": dict(zip(['a','b','c'], self.entry_opciones_es.get().split("/"))),
                "respuesta": self.entry_respuesta.get(),
                "retro": "Retroalimentación personalizada"
            },
            "en": {
                "texto": self.entry_en.get(),
                "pregunta": self.entry_pregunta_en.get(),
                "opciones": dict(zip(['a','b','c'], self.entry_opciones_en.get().split("/"))),
                "respuesta": self.entry_respuesta.get(),
                "retro": "Custom feedback"
            }
        }
        
        if len(self.ejemplos) < 100:
            self.ejemplos.append(nuevo_ejemplo)
            self.guardar_a_json()
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente!")
        else:
            messagebox.showwarning("Límite", "Se ha alcanzado el máximo de 100 ejemplos")

    def guardar_a_json(self):
        with open("ejemplos.json", "w", encoding="utf-8") as f:
            json.dump(self.ejemplos, f, ensure_ascii=False, indent=2)

    def crear_barra_herramientas(self):
        toolbar = ttk.Frame(self)
        toolbar.pack(fill=tk.X)
        
        ttk.Button(toolbar, text="Exportar Ejemplos", command=self.exportar_ejemplos).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="Importar Ejemplos", command=self.importar_ejemplos).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="Reiniciar Quiz", command=self.iniciar_quiz).pack(side=tk.RIGHT, padx=5)

    def exportar_ejemplos(self):
        archivo = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
        if archivo:
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(self.ejemplos, f, ensure_ascii=False, indent=2)

    def importar_ejemplos(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")]
        )
        if archivo:
            with open(archivo, "r", encoding="utf-8") as f:
                self.ejemplos = json.load(f)[:100]  # Limitar a 100 ejemplos
                self.guardar_a_json()
                self.iniciar_quiz()

    # ... (Mantener las demás funciones anteriores sin cambios)

if __name__ == "__main__":
    app = LinguMasterPro()
    app.mainloop()
