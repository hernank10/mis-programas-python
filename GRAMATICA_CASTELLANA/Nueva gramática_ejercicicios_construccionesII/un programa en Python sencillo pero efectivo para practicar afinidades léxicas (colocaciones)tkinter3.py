import tkinter as tk
from tkinter import messagebox
import random
import csv
from datetime import datetime

# Combinaciones por verbo
combinaciones = {
    'dar': ["dar una vuelta", "dar la razón", "dar miedo", "dar un consejo"],
    'hacer': ["hacer una pregunta", "hacer ejercicio", "hacer daño"],
    'tener': ["tener razón", "tener éxito", "tener hambre"],
    'ejercer': ["ejercer influencia", "ejercer presión"],
    'ejercitar': ["ejercitar la virtud", "ejercitar la memoria"],
    'cundir': ["cundir el desaliento", "cundir el pánico"],
    'evacuar': ["evacuar la consulta"],
    'reírse': ["reírse de alguien", "reírse con alguien"],
    'contraer': ["contraer matrimonio", "contraer deudas"]
}

niveles = {
    "fácil": ["dar una vuelta", "hacer una pregunta", "tener razón"],
    "medio": ["ejercer influencia", "ejercitar la virtud", "reírse de alguien"],
    "difícil": ["cundir el desaliento", "evacuar la consulta", "contraer matrimonio"]
}

class EntrenadorVerbal:
    def __init__(self, root):
        self.root = root
        self.root.title("Entrenamiento de Combinaciones Verbales")

        self.nivel = tk.StringVar(value="fácil")
        self.vidas = 3
        self.puntos = 0
        self.correctas = 0
        self.incorrectas = 0
        self.frases = []
        self.frase_actual = ""

        self.setup_gui()

    def setup_gui(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Selecciona un nivel:").pack()
        for nivel in niveles:
            tk.Radiobutton(frame, text=nivel.capitalize(), variable=self.nivel, value=nivel).pack(anchor='w')

        self.btn_comenzar = tk.Button(frame, text="Comenzar", command=self.comenzar)
        self.btn_comenzar.pack(pady=10)

        self.lbl_frase = tk.Label(frame, text="")
        self.lbl_frase.pack()

        self.entry_oracion = tk.Entry(frame, width=60)
        self.entry_oracion.pack()

        self.btn_verificar = tk.Button(frame, text="Verificar", command=self.verificar)
        self.btn_verificar.pack(pady=5)

        self.lbl_estado = tk.Label(frame, text="Vidas: 3 | Puntos: 0")
        self.lbl_estado.pack()

    def comenzar(self):
        self.vidas = 3
        self.puntos = 0
        self.correctas = 0
        self.incorrectas = 0
        self.frases = niveles[self.nivel.get()].copy()
        random.shuffle(self.frases)
        self.siguiente_frase()

    def siguiente_frase(self):
        if self.vidas <= 0 or not self.frases:
            self.finalizar()
            return
        self.frase_actual = self.frases.pop()
        self.lbl_frase.config(text=f"Escribe una oración con: '{self.frase_actual}'")
        self.entry_oracion.delete(0, tk.END)

    def verificar(self):
        oracion = self.entry_oracion.get().strip()
        verbo = self.frase_actual.split()[0]
        if verbo in oracion:
            self.puntos += 10
            self.correctas += 1
            messagebox.showinfo("Correcto", "¡Bien hecho! Ganaste 10 puntos.")
        else:
            self.vidas -= 1
            self.incorrectas += 1
            messagebox.showwarning("Incorrecto", f"Debías usar el verbo '{verbo}'. Pierdes una vida.")
        self.lbl_estado.config(text=f"Vidas: {self.vidas} | Puntos: {self.puntos}")
        self.siguiente_frase()

    def finalizar(self):
        messagebox.showinfo("Fin", f"Correctas: {self.correctas}\nIncorrectas: {self.incorrectas}\nPuntos: {self.puntos}")
        self.guardar_estadisticas()

    def guardar_estadisticas(self):
        datos = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nivel": self.nivel.get(),
            "correctas": self.correctas,
            "incorrectas": self.incorrectas,
            "puntos": self.puntos,
            "vidas_restantes": self.vidas
        }
        archivo = "estadisticas_gui.csv"
        archivo_nuevo = not os.path.exists(archivo)
        with open(archivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=datos.keys())
            if archivo_nuevo:
                writer.writeheader()
            writer.writerow(datos)

if __name__ == "__main__":
    root = tk.Tk()
    app = EntrenadorVerbal(root)
    root.mainloop()
