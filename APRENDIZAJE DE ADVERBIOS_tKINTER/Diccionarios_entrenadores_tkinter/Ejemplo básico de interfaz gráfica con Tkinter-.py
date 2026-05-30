import tkinter as tk
import random

palabras_con_z = ["cicatriz", "suspicaz", "alabanza", "golpazo", "almirantazgo", "entereza", "analizar", "armazón", "crianza"]

def generar_palabra():
    palabra_aleatoria = random.choice(palabras_con_z)
    label_palabra.config(text=f"Crea una frase con la palabra: {palabra_aleatoria}")

root = tk.Tk()
root.title("Juego de Palabras con Z")

label_palabra = tk.Label(root, text="Presiona el botón para generar una palabra")
label_palabra.pack(pady=20)

boton_generar = tk.Button(root, text="Generar Palabra", command=generar_palabra)
boton_generar.pack(pady=20)

root.mainloop()
