import tkinter as tk
from tkinter import messagebox
import random

# Datos de conectores
conectores = {
    "Adición": {
        "ejemplos": ["además", "también", "incluso", "asimismo"],
        "consejos": [
            "Usa 'además' para sumar ideas relacionadas.",
            "Evita repetir 'también' varias veces.",
            "Prefiere 'asimismo' en contextos formales.",
            "Usa 'incluso' para enfatizar lo inesperado."
        ]
    },
    "Contraste": {
        "ejemplos": ["pero", "aunque", "sin embargo", "no obstante"],
        "consejos": [
            "Usa 'pero' para introducir una objeción ligera.",
            "'Sin embargo' indica oposición con más fuerza.",
            "No combines 'pero' con 'sin embargo'.",
            "'Aunque' introduce una idea opuesta dentro de una oración."
        ]
    },
    "Causa": {
        "ejemplos": ["porque", "ya que", "dado que", "debido a que"],
        "consejos": [
            "Usa 'porque' para causas claras.",
            "Prefiere 'dado que' en textos académicos.",
            "'Debido a que' necesita un verbo después.",
            "Evita usar 'por' como si fuera 'porque'."
        ]
    },
    "Consecuencia": {
        "ejemplos": ["por eso", "por lo tanto", "en consecuencia", "así que"],
        "consejos": [
            "Usa 'por eso' en lenguaje informal.",
            "'Por lo tanto' es ideal para argumentar.",
            "'En consecuencia' es perfecto para cerrar ideas.",
            "Evita usar 'entonces' sin lógica clara."
        ]
    }
}

# App principal
class ConectoresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprende Conectores Discursivos")
        self.puntos = 0
        self.pregunta_actual = 0

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)

        self.label = tk.Label(self.main_frame, text="Menú Principal", font=("Arial", 16))
        self.label.pack(pady=10)

        tk.Button(self.main_frame, text="1. Estudiar consejos", width=30, command=self.estudiar).pack(pady=5)
        tk.Button(self.main_frame, text="2. Ver ejemplos", width=30, command=self.ver_ejemplos).pack(pady=5)
        tk.Button(self.main_frame, text="3. Practicar con ejercicios", width=30, command=self.iniciar_practica).pack(pady=5)
        tk.Button(self.main_frame, text="4. Salir", width=30, command=root.quit).pack(pady=5)

    def estudiar(self):
        texto = ""
        for tipo, data in conectores.items():
            texto += f"\n🔹 {tipo}:\n"
            for consejo in data["consejos"]:
                texto += f" - {consejo}\n"
        self.mostrar_mensaje("Consejos por categoría", texto)

    def ver_ejemplos(self):
        texto = ""
        for tipo, data in conectores.items():
            texto += f"🔸 {tipo}: {', '.join(data['ejemplos'])}\n"
        self.mostrar_mensaje("Ejemplos de conectores", texto)

    def mostrar_mensaje(self, titulo, contenido):
        top = tk.Toplevel()
        top.title(titulo)
        text = tk.Text(top, wrap=tk.WORD)
        text.insert(tk.END, contenido)
        text.config(state=tk.DISABLED)
        text.pack(padx=10, pady=10)

    def iniciar_practica(self):
        self.puntos = 0
        self.pregunta_actual = 0
        self.preguntas = list(conectores.items())
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.pregunta_actual >= 5:
            messagebox.showinfo("Resultado", f"Puntaje final: {self.puntos}/5")
            return

        self.tipo_correcto, data = random.choice(list(conectores.items()))
        self.ejemplo = random.choice(data["ejemplos"])

        opciones = random.sample(list(conectores.keys()), 3)
        if self.tipo_correcto not in opciones:
            opciones[random.randint(0, 2)] = self.tipo_correcto
        random.shuffle(opciones)

        self.ventana_pregunta = tk.Toplevel()
        self.ventana_pregunta.title("Ejercicio")

        label = tk.Label(self.ventana_pregunta, text=f"¿A qué tipo de conector pertenece '{self.ejemplo}'?", font=("Arial", 12))
        label.pack(pady=10)

        for op in opciones:
            b = tk.Button(self.ventana_pregunta, text=op, width=30, command=lambda o=op: self.verificar_respuesta(o))
            b.pack(pady=5)

    def verificar_respuesta(self, seleccion):
        if seleccion == self.tipo_correcto:
            self.puntos += 1
            messagebox.showinfo("Correcto", "✅ ¡Muy bien!")
        else:
            messagebox.showerror("Incorrecto", f"❌ Era: {self.tipo_correcto}")
        self.ventana_pregunta.destroy()
        self.pregunta_actual += 1
        self.mostrar_pregunta()

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = ConectoresApp(root)
    root.mainloop()
