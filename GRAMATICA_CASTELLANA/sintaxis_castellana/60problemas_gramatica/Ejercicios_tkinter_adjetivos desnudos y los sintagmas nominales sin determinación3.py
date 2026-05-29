import json
import tkinter as tk
from tkinter import messagebox

def cargar_ejemplos():
    try:
        with open("ejemplos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"adjetivo": "Julio habla claro.", "nominal": "Julio compra libros."},
            {"adjetivo": "Ana canta fuerte.", "nominal": "Pedro vende frutas."}
        ]

def guardar_ejemplos(ejemplos):
    with open("ejemplos.json", "w") as file:
        json.dump(ejemplos, file, indent=4)

def mostrar_introduccion():
    messagebox.showinfo("Introducción", "Los adjetivos desnudos y los sintagmas nominales sin determinación tienen restricciones en su uso.")

def mostrar_teoria():
    messagebox.showinfo("Teoría", "Los adjetivos desnudos son adjetivos con función adverbial, como en 'Julio escribe claro'.")

def mostrar_ejemplos():
    ejemplos = cargar_ejemplos()
    texto = "\n".join([f"{i+1}. {ej['adjetivo']} | {ej['nominal']}" for i, ej in enumerate(ejemplos)])
    messagebox.showinfo("Ejemplos y Análisis", texto)

def agregar_ejemplo():
    def guardar():
        ejemplos = cargar_ejemplos()
        ejemplos.append({"adjetivo": adjetivo_entry.get(), "nominal": nominal_entry.get()})
        guardar_ejemplos(ejemplos)
        messagebox.showinfo("Éxito", "Ejemplo agregado correctamente.")
        agregar_win.destroy()
    
    agregar_win = tk.Toplevel(root)
    agregar_win.title("Agregar Ejemplo")
    tk.Label(agregar_win, text="Ejemplo con adjetivo desnudo:").pack()
    adjetivo_entry = tk.Entry(agregar_win)
    adjetivo_entry.pack()
    tk.Label(agregar_win, text="Ejemplo con sintagma nominal:").pack()
    nominal_entry = tk.Entry(agregar_win)
    nominal_entry.pack()
    tk.Button(agregar_win, text="Guardar", command=guardar).pack()

def comparar_formas():
    messagebox.showinfo("Comparación", "Ejemplo 1: Julio escribe claramente. vs. Julio escribe claro.\nEjemplo 2: Julio escribe las cartas. vs. Julio escribe cartas.")

def ejercicios_escritura():
    ejercicios = [
        "Escribe una oración con un adjetivo desnudo.",
        "Convierte la siguiente oración en una con un adjetivo desnudo: 'Pedro habla con claridad'.", 
        "Transforma 'Ana canta maravillosamente' en una oración con adjetivo desnudo.",
        "Redacta una oración con un sintagma nominal sin determinación.",
        "Corrige la oración: 'Juan habla buen'.", 
        "Explica la diferencia entre 'Escribe claro' y 'Escribe claramente'.", 
        "Escribe una frase con 'baila hermoso'.", 
        "Transforma 'Corre velozmente' en su forma con adjetivo desnudo.",
        "Crea una oración en la que un adjetivo desnudo modifique un verbo de acción.",
        "Escribe una oración con 'canta fuerte'.", 
        "Transforma 'Lee con atención' en una oración con adjetivo desnudo.",
        "Escribe una oración donde el sustantivo no tenga determinante.",
        "Explica la diferencia entre 'Compra libros' y 'Compra los libros'.", 
        "Redacta una oración que contenga un adjetivo desnudo y un sintagma nominal sin determinante.", 
        "Corrige la frase: 'Carlos escribe claramente las cartas'."
    ]
    texto = "\n".join([f"{i+1}. {ej}" for i, ej in enumerate(ejercicios)])
    messagebox.showinfo("Ejercicios de Escritura", texto)

def juego():
    messagebox.showinfo("Juego", "Adivina si la oración tiene un adjetivo desnudo o un sintagma nominal sin determinante.")

def crear_gui():
    global root
    root = tk.Tk()
    root.title("Práctica de Adjetivos Desnudos y Sintagmas Nominales")
    tk.Button(root, text="Introducción", command=mostrar_introduccion).pack(fill='x')
    tk.Button(root, text="Teoría", command=mostrar_teoria).pack(fill='x')
    tk.Button(root, text="Ejemplos y Análisis", command=mostrar_ejemplos).pack(fill='x')
    tk.Button(root, text="Agregar Ejemplo", command=agregar_ejemplo).pack(fill='x')
    tk.Button(root, text="Comparar Formas", command=comparar_formas).pack(fill='x')
    tk.Button(root, text="Ejercicios de Escritura", command=ejercicios_escritura).pack(fill='x')
    tk.Button(root, text="Juego", command=juego).pack(fill='x')
    tk.Button(root, text="Salir", command=root.quit).pack(fill='x')
    root.mainloop()

if __name__ == "__main__":
    crear_gui()
