import tkinter as tk
from tkinter import messagebox
import random

# Definiciones y ejemplos
sustantivos = {
    "Comunes": "Nombran en forma general a personas, animales o cosas. Ej: perro, ciudad, mesa.",
    "Propios": "Nombran en forma particular a personas, animales o lugares. Se escriben con mayúscula. Ej: Pedro, Bogotá, Amazonas.",
    "Concretos": "Se perciben con los sentidos. Ej: flor, guitarra, río.",
    "Abstractos": "Nombran ideas, sentimientos o cualidades. Ej: amor, libertad, belleza.",
    "Individuales": "Nombran en singular a un ser u objeto. Ej: abeja, soldado, árbol.",
    "Colectivos": "Nombran en singular a un conjunto de seres de la misma especie. Ej: enjambre, ejército, arboleda.",
    "Contables": "Se pueden contar. Ej: libro, manzana, auto.",
    "Incontables": "No se pueden contar de forma individual. Ej: agua, arena, aire."
}

# Lista de ejercicios
ejemplos = [
    ("Pedro", "Propios"),
    ("ciudad", "Comunes"),
    ("amor", "Abstractos"),
    ("soldado", "Individuales"),
    ("enjambre", "Colectivos"),
    ("arena", "Incontables"),
    ("guitarra", "Concretos"),
    ("libro", "Contables"),
    ("María", "Propios"),
    ("arboleda", "Colectivos"),
]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprender Sustantivos")
        
        self.score = 0
        self.question_index = 0
        self.questions = random.sample(ejemplos, len(ejemplos))

        # Texto de teoría
        self.text = tk.Text(root, wrap="word", height=12, width=60)
        self.text.pack(pady=10)
        self.mostrar_teoria()

        # Ejercicio
        self.label = tk.Label(root, text="Escribe el tipo de sustantivo:", font=("Arial", 14))
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Responder", command=self.verificar_respuesta)
        self.button.pack(pady=10)
        
        self.feedback = tk.Label(root, text="", font=("Arial", 12))
        self.feedback.pack(pady=5)
        
        self.siguiente_pregunta()

    def mostrar_teoria(self):
        self.text.insert("1.0", "📘 Teoría de los Sustantivos\n\n")
        for tipo, definicion in sustantivos.items():
            self.text.insert("end", f"👉 {tipo}: {definicion}\n\n")

    def siguiente_pregunta(self):
        if self.question_index < len(self.questions):
            palabra, _ = self.questions[self.question_index]
            self.label.config(text=f"¿Qué tipo de sustantivo es: '{palabra}'?")
            self.entry.delete(0, tk.END)
            self.feedback.config(text="")
        else:
            messagebox.showinfo("Fin del Juego", f"¡Terminaste! Tu puntaje fue {self.score}/{len(self.questions)}.")
            self.root.quit()

    def verificar_respuesta(self):
        respuesta = self.entry.get().capitalize()
        palabra, correcto = self.questions[self.question_index]
        
        if respuesta == correcto:
            self.feedback.config(text="✅ Correcto", fg="green")
            self.score += 1
        else:
            self.feedback.config(text=f"❌ Incorrecto. Era: {correcto}", fg="red")
        
        self.question_index += 1
        self.root.after(1500, self.siguiente_pregunta)

# Ejecutar
root = tk.Tk()
app = App(root)
root.mainloop()
