# Adaptación a Tkinter
import tkinter as tk
from tkinter import messagebox
import random

# Datos de ejemplo
oraciones_condicionales = {
    "Reales": [
        {"oracion": "Si estudias, aprobarás el examen.", "explicacion": "Condición real. SI + Presente + Futuro."},
        {"oracion": "Si llueve, nos quedamos en casa.", "explicacion": "Condición presente real. SI + Presente + Presente."}
    ],
    "Potenciales": [
        {"oracion": "Si estudiaras más, aprobarías fácilmente.", "explicacion": "Condición hipotética. SI + Pret. Imperfecto Subj. + Condicional simple."},
        {"oracion": "Si vinieras mañana, podrías ayudarme.", "explicacion": "Condición futura dudosa. SI + Pret. Imperfecto Subj. + Condicional simple."}
    ],
    "Irreales": [
        {"oracion": "Si hubieras estudiado, habrías aprobado.", "explicacion": "Condición no cumplida en el pasado. SI + Pret. Pluscuamperfecto Subj. + Condicional compuesto."},
        {"oracion": "Si me lo hubieras dicho, no habría venido.", "explicacion": "Condición pasada no cumplida. SI + Pluscuamperfecto Subj. + Condicional compuesto."}
    ]
}

class JuegoOrdenar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.puntos = 0
        self.palabras = []
        self.respuesta = []
        self.oracion_objetivo = ""
        self.explicacion = ""

        self.label_puntos = tk.Label(self, text=f"\U0001F3AF Puntos: {self.puntos}")
        self.label_puntos.pack()

        self.label_instruccion = tk.Label(self, text="\U0001F524 Haz clic en las palabras en orden:")
        self.label_instruccion.pack()

        self.frame_palabras = tk.Frame(self)
        self.frame_palabras.pack()

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack()

        self.boton_nueva = tk.Button(self, text="Nueva oración", command=self.nueva_oracion)
        self.boton_nueva.pack(pady=5)

        self.nueva_oracion()

    def nueva_oracion(self):
        for widget in self.frame_palabras.winfo_children():
            widget.destroy()

        categoria = random.choice(list(oraciones_condicionales.keys()))
        seleccion = random.choice(oraciones_condicionales[categoria])
        self.oracion_objetivo = seleccion['oracion']
        self.explicacion = seleccion['explicacion']
        self.palabras = self.oracion_objetivo.split()
        random.shuffle(self.palabras)
        self.respuesta = []
        self.label_resultado.config(text="")

        for palabra in self.palabras:
            btn = tk.Button(self.frame_palabras, text=palabra, command=lambda b=palabra: self.agregar_palabra(b))
            btn.pack(side='left')

    def agregar_palabra(self, palabra):
        self.respuesta.append(palabra)
        if len(self.respuesta) == len(self.oracion_objetivo.split()):
            resultado = " ".join(self.respuesta)
            if resultado.strip() == self.oracion_objetivo:
                self.puntos += 1
                self.label_resultado.config(text=f"\u2705 ¡Correcto! \U0001F389\n\U0001F4D8 {self.explicacion}")
                self.label_puntos.config(text=f"\U0001F3AF Puntos: {self.puntos}")
            else:
                self.label_resultado.config(text=f"\u274C Incorrecto.\nEra: {self.oracion_objetivo}\n\U0001F4D8 {self.explicacion}")
            self.respuesta = []

class MenuPrincipal(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        tk.Label(self, text="\U0001F3AE Selecciona un juego condicional:").pack(pady=10)

        juegos = [
            ("Juego 2: Ordenar palabras 🧩", self.ir_juego_ordenar),
            ("Juego 3: Completar espacios ✏️", self.juego_en_construccion),
            ("Juego 4: Memoria 🧠", self.juego_en_construccion),
            ("Juego 5: Construcción de oración 🧱", self.juego_en_construccion),
            ("Juego 6: Selección múltiple ✅", self.juego_en_construccion),
            ("Juego 7: Aventura textual 🗺️", self.juego_en_construccion),
            ("Juego 8: Carrera de condicionales 🚗", self.juego_en_construccion),
            ("Juego 9: Rompecabezas lógico 🧠", self.juego_en_construccion),
            ("Juego 10: Quiz visual 🖼️", self.juego_en_construccion),
        ]

        for texto, funcion in juegos:
            tk.Button(self, text=texto, command=funcion, width=40).pack(pady=2)

    def ir_juego_ordenar(self):
        self.destroy()
        juego = JuegoOrdenar(self.master)
        juego.pack()

    def juego_en_construccion(self):
        messagebox.showinfo("En construcción 🚧", "Este juego estará disponible próximamente.")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Juegos Condicionales (Tkinter)")
    app = MenuPrincipal(root)
    app.pack()
    root.mainloop()
