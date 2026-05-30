import tkinter as tk
from tkinter import ttk, messagebox
import random

# Diccionario base con ejemplos por tipo
EJERCICIOS = {
    "Selección múltiple": [
        {
            "pregunta": "¿Cuál palabra está escrita correctamente?",
            "opciones": ["exámen", "examen", "exámenn"],
            "respuesta": "examen"
        }
    ],
    "Completar oraciones": [
        {
            "pregunta": "Completa la frase: El ___ está caliente.",
            "opciones": ["café", "cafe", "cafè"],
            "respuesta": "café"
        }
    ],
    "Detectar errores": [
        {
            "pregunta": "Frase: Los niño juega.\n¿Qué tipo de error contiene?",
            "opciones": ["Concordancia", "Ortografía", "Puntuación"],
            "respuesta": "Concordancia"
        }
    ]
    # Agrega los otros tipos aquí
}

class EntrenadorCastellano(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧠 Entrenador del Castellano")
        self.geometry("600x400")
        self.configure(bg="#f2f2f2")

        self.tipo_ejercicio = tk.StringVar()

        self.crear_menu_principal()

    def crear_menu_principal(self):
        ttk.Label(self, text="📘 Selecciona el tipo de ejercicio", font=("Arial", 14)).pack(pady=10)

        tipos = list(EJERCICIOS.keys())
        self.tipo_combo = ttk.Combobox(self, textvariable=self.tipo_ejercicio, values=tipos)
        self.tipo_combo.pack(pady=10)

        ttk.Button(self, text="🧪 Comenzar práctica", command=self.mostrar_ejercicio).pack(pady=10)

    def mostrar_ejercicio(self):
        tipo = self.tipo_combo.get()
        if not tipo or tipo not in EJERCICIOS:
            messagebox.showwarning("Selecciona un tipo válido", "Debes elegir un tipo de ejercicio.")
            return

        ejercicio = random.choice(EJERCICIOS[tipo])
        self.abrir_ejercicio_ventana(ejercicio)

    def abrir_ejercicio_ventana(self, ejercicio):
        ventana = tk.Toplevel(self)
        ventana.title("Ejercicio")
        ventana.geometry("550x300")

        tk.Label(ventana, text=ejercicio["pregunta"], font=("Arial", 13), wraplength=500).pack(pady=10)

        seleccion = tk.StringVar()
        for opcion in ejercicio["opciones"]:
            ttk.Radiobutton(ventana, text=opcion, variable=seleccion, value=opcion).pack(anchor="w")

        resultado = tk.Label(ventana, text="", font=("Arial", 12))
        resultado.pack(pady=10)

        def verificar():
            if seleccion.get() == ejercicio["respuesta"]:
                resultado.config(text="✅ ¡Correcto!", foreground="green")
            else:
                resultado.config(text=f"❌ Incorrecto. Respuesta: {ejercicio['respuesta']}", foreground="red")

        ttk.Button(ventana, text="Verificar", command=verificar).pack(pady=10)
        ttk.Button(ventana, text="Cerrar", command=ventana.destroy).pack()

if __name__ == "__main__":
    app = EntrenadorCastellano()
    app.mainloop()
