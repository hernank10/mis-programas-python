import tkinter as tk
from tkinter import ttk, messagebox
import random

# Diccionario de ejercicios básicos
EJERCICIOS = {
    "Ortografía": {
        "Nivel 1": {
            "Selección múltiple": [
                {"pregunta": "¿Cuál palabra está escrita correctamente?",
                 "opciones": ["exámen", "examen", "exámenn"],
                 "respuesta": "examen"}
            ]
        }
    },
    "Morfología": {
        "Nivel 1": {
            "Clasificación de palabras": [
                {"pregunta": "¿Qué tipo de palabra es ‘rápidamente’?",
                 "opciones": ["Adjetivo", "Verbo", "Adverbio"],
                 "respuesta": "Adverbio"}
            ]
        }
    },
    "Sintaxis": {
        "Nivel 1": {
            "Ordenar oraciones": [
                {"pregunta": "Ordena correctamente: ‘ayer / parque / fuimos / al’",
                 "opciones": ["Fuimos al parque ayer", "Al parque fuimos ayer", "Ayer al parque fuimos"],
                 "respuesta": "Fuimos al parque ayer"}
            ]
        }
    }
}

class PracticaCastellano(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧠 Práctica del Castellano")
        self.geometry("600x400")
        self.configure(bg="#f2f2f2")

        self.area = tk.StringVar()
        self.nivel = tk.StringVar()
        self.tipo = tk.StringVar()

        self.crear_menu()

    def crear_menu(self):
        ttk.Label(self, text="📚 Área del lenguaje:").pack()
        ttk.Combobox(self, textvariable=self.area, values=list(EJERCICIOS.keys())).pack()

        ttk.Label(self, text="🎯 Nivel:").pack()
        ttk.Combobox(self, textvariable=self.nivel, values=["Nivel 1"]).pack()

        ttk.Label(self, text="🧪 Tipo de ejercicio:").pack()
        self.tipo_combo = ttk.Combobox(self)
        self.tipo_combo.pack()

        ttk.Button(self, text="Cargar tipos", command=self.cargar_tipos).pack(pady=5)
        ttk.Button(self, text="Comenzar ejercicio", command=self.mostrar_ejercicio).pack(pady=10)

    def cargar_tipos(self):
        area = self.area.get()
        nivel = self.nivel.get()
        if area and nivel:
            tipos = list(EJERCICIOS[area][nivel].keys())
            self.tipo_combo.config(values=tipos)
            self.tipo.set(tipos[0])
        else:
            messagebox.showwarning("Faltan datos", "Selecciona área y nivel primero.")

    def mostrar_ejercicio(self):
        area = self.area.get()
        nivel = self.nivel.get()
        tipo = self.tipo_combo.get()
        if not (area and nivel and tipo):
            messagebox.showwarning("Faltan datos", "Completa todas las selecciones.")
            return

        ejercicio = random.choice(EJERCICIOS[area][nivel][tipo])
        self.ejercicio_window(ejercicio)

    def ejercicio_window(self, ejercicio):
        win = tk.Toplevel(self)
        win.title("Ejercicio")

        tk.Label(win, text=ejercicio["pregunta"], font=("Arial", 14)).pack(pady=10)
        respuesta_var = tk.StringVar()

        for opcion in ejercicio["opciones"]:
            tk.Radiobutton(win, text=opcion, variable=respuesta_var, value=opcion).pack(anchor="w")

        def verificar():
            seleccion = respuesta_var.get()
            if seleccion == ejercicio["respuesta"]:
                messagebox.showinfo("Resultado", "✅ ¡Correcto!")
            else:
                messagebox.showerror("Resultado", f"❌ Incorrecto. Respuesta: {ejercicio['respuesta']}")

        ttk.Button(win, text="Enviar respuesta", command=verificar).pack(pady=10)

if __name__ == "__main__":
    app = PracticaCastellano()
    app.mainloop()
