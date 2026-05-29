import json
import tkinter as tk
from tkinter import messagebox
import random

PROGRESO_FILE = "progreso.json"
EJEMPLOS_FILE = "ejemplos.json"

def cargar_ejemplos():
    try:
        with open(EJEMPLOS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"locativa": "Las lágrimas caían cuello abajo.", "manera": "Lo acostaron boca arriba."}
        ]

def guardar_ejemplos(ejemplos):
    with open(EJEMPLOS_FILE, "w") as file:
        json.dump(ejemplos, file, indent=4)

def cargar_progreso():
    try:
        with open(PROGRESO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_progreso(progreso):
    with open(PROGRESO_FILE, "w") as file:
        json.dump(progreso, file, indent=4)

def mostrar_introduccion():
    messagebox.showinfo("Introducción", "Exploramos construcciones como 'cuello abajo' y 'boca arriba' en español.")

def mostrar_teoria():
    messagebox.showinfo("Teoría", "Las construcciones pueden indicar una ubicación o la manera en que ocurre una acción.")

def mostrar_ejemplos():
    ejemplos = cargar_ejemplos()
    texto = "\n".join([f"Locativa: {ej['locativa']} | Manera: {ej['manera']}" for ej in ejemplos])
    messagebox.showinfo("Ejemplos", texto)

def agregar_ejemplo():
    def guardar():
        ejemplos = cargar_ejemplos()
        ejemplos.append({"locativa": locativa_entry.get(), "manera": manera_entry.get()})
        guardar_ejemplos(ejemplos)
        messagebox.showinfo("Éxito", "Ejemplo agregado correctamente.")
        agregar_win.destroy()
    
    agregar_win = tk.Toplevel(root)
    agregar_win.title("Agregar Ejemplo")
    tk.Label(agregar_win, text="Ejemplo Locativa:").pack()
    locativa_entry = tk.Entry(agregar_win)
    locativa_entry.pack()
    tk.Label(agregar_win, text="Ejemplo Manera:").pack()
    manera_entry = tk.Entry(agregar_win)
    manera_entry.pack()
    tk.Button(agregar_win, text="Guardar", command=guardar).pack()

def ejercicios_escritura():
    ejercicios = [
        "Escribe una oración con una construcción locativa.",
        "Transforma 'Las gotas caían por la cara' en una construcción locativa.",
        "Escribe una oración con 'boca arriba'.",
        "Convierte 'Se deslizaba por la espalda' en una construcción locativa.",
        "Explica la diferencia entre 'cuello abajo' y 'boca arriba'.",
        "Corrige la oración: 'El agua resbalaba abajo la espalda'.",
        "Crea una oración donde 'arriba' indique manera.",
        "Transforma 'Caminaba con pasos pesados' en una oración con construcción de manera.",
        "Completa la oración: 'Las hojas caían ______' (locativa).",
        "Escribe una oración con 'cabeza abajo'.",
        "Reescribe 'Se acostó en la cama con la cara hacia el techo' usando una construcción de manera.",
        "Corrige: 'El perro durmió barriga en el suelo'.",
        "Crea una oración usando 'espalda abajo'.",
        "Transforma 'Lo llevaban de lado' en una construcción más precisa.",
        "Explica cuándo usar 'boca abajo' y cuándo 'de cabeza'."
    ]
    progreso = cargar_progreso()
    
    ejercicio_win = tk.Toplevel(root)
    ejercicio_win.title("Ejercicios de Escritura")
    
    def guardar_respuesta(i):
        progreso[str(i)] = respuestas[i].get()
        guardar_progreso(progreso)
        messagebox.showinfo("Guardado", "Respuesta guardada.")
    
    respuestas = {}
    for i, ej in enumerate(ejercicios):
        tk.Label(ejercicio_win, text=f"{i+1}. {ej}").pack()
        respuestas[i] = tk.Entry(ejercicio_win, width=50)
        respuestas[i].pack()
        if str(i) in progreso:
            respuestas[i].insert(0, progreso[str(i)])
        tk.Button(ejercicio_win, text="Guardar", command=lambda i=i: guardar_respuesta(i)).pack()

def juego():
    niveles = ["Básico", "Intermedio", "Avanzado"]
    nivel = random.choice(niveles)
    if nivel == "Básico":
        messagebox.showinfo("Juego - Nivel Básico", "Distingue si la construcción es locativa o de manera.")
    elif nivel == "Intermedio":
        messagebox.showinfo("Juego - Nivel Intermedio", "Completa la oración con la construcción correcta.")
    else:
        messagebox.showinfo("Juego - Nivel Avanzado", "Reescribe la oración cambiando la estructura.")

def crear_gui():
    global root
    root = tk.Tk()
    root.title("Práctica de Construcciones Castellanas")
    tk.Button(root, text="Introducción", command=mostrar_introduccion).pack(fill='x')
    tk.Button(root, text="Teoría", command=mostrar_teoria).pack(fill='x')
    tk.Button(root, text="Ejemplos", command=mostrar_ejemplos).pack(fill='x')
    tk.Button(root, text="Agregar Ejemplo", command=agregar_ejemplo).pack(fill='x')
    tk.Button(root, text="Ejercicios de Escritura", command=ejercicios_escritura).pack(fill='x')
    tk.Button(root, text="Juego", command=juego).pack(fill='x')
    tk.Button(root, text="Salir", command=root.quit).pack(fill='x')
    root.mainloop()

if __name__ == "__main__":
    crear_gui()
