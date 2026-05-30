import tkinter as tk
from tkinter import ttk, messagebox
import json
import random
import os

ARCHIVO = "ejemplos.json"

categorias = {
    "directa": "¿Vendrás mañana?",
    "indirecta": "Quisiera saber si vendrás mañana.",
    "total": "¿Estás listo?",
    "parcial": "¿Dónde estudias?",
    "afirmativa": "¿Tú realmente crees eso?",
    "negativa": "¿No te gusta el cine?",
    "retórica": "¿Acaso no es evidente?",
    "ecoica": "¿Dijo 'vendré'?",
    "exclamativa": "¿Cómo te atreves?",
    "confirmación": "¿No es cierto que lo viste?"
}

# Cargar o crear archivo JSON
def cargar_ejemplos():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            json.dump([], f)
    with open(ARCHIVO, "r") as f:
        return json.load(f)

def guardar_ejemplos(lista):
    with open(ARCHIVO, "w") as f:
        json.dump(lista, f, indent=4)

ejemplos = cargar_ejemplos()

# Función para mostrar teoría
def mostrar_teoria():
    texto = "\n".join([f"{cat.title()}: {ej}" for cat, ej in categorias.items()])
    messagebox.showinfo("Teoría de preguntas", texto)

# Función para práctica aleatoria
def practicar():
    if not ejemplos:
        messagebox.showwarning("Sin datos", "No hay ejemplos para practicar.")
        return

    ejemplo = random.choice(ejemplos)
    pregunta = ejemplo["original"]

    def verificar():
        respuesta = entrada.get().strip().lower()
        if respuesta == ejemplo["categoria"].lower():
            resultado.set("¡Correcto!")
        else:
            resultado.set(f"Incorrecto. La categoría correcta es: {categorias[ejemplo['categoria']]}")
        entrada.delete(0, tk.END)

    ventana = tk.Toplevel(root)
    ventana.title("Práctica")
    ttk.Label(ventana, text="¿Qué tipo de oración es esta?", font=("Arial", 12)).pack(pady=5)
    ttk.Label(ventana, text=pregunta, font=("Arial", 14, "italic")).pack(pady=5)

    entrada = ttk.Entry(ventana, width=40)
    entrada.pack()
    ttk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)

    resultado = tk.StringVar()
    ttk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack(pady=5)

# Función para agregar ejemplo nuevo
def agregar_ejemplo():
    cat = categoria.get()
    orig = original.get().strip()
    pasado = pasado_entry.get().strip()
    enfasis = enfatico_entry.get().strip()

    if not cat or not orig or not pasado:
        messagebox.showwarning("Campos vacíos", "Rellena todos los campos.")
        return

    ejemplos.append({
        "categoria": cat,
        "original": orig,
        "modificado": pasado,
        "enfatico": enfasis
    })
    guardar_ejemplos(ejemplos)
    messagebox.showinfo("Guardado", "Ejemplo agregado con éxito.")
    original.delete(0, tk.END)
    pasado_entry.delete(0, tk.END)
    enfatico_entry.delete(0, tk.END)

# Función para ver ejemplos filtrados
def ver_ejemplos():
    cat = filtro.get()
    filtrados = [e for e in ejemplos if e["categoria"] == cat] if cat else ejemplos
    texto = "\n".join([f"{e['categoria'].title()}: {e['original']}" for e in filtrados]) or "Sin ejemplos"
    messagebox.showinfo("Ejemplos", texto)

# Crear ventana principal
root = tk.Tk()
root.title("Práctica de Oraciones Interrogativas")
root.geometry("600x500")

# Menú superior
ttk.Button(root, text="📘 Ver Teoría", command=mostrar_teoria).pack(pady=5)
ttk.Button(root, text="🎲 Práctica Aleatoria", command=practicar).pack(pady=5)

# Marco para agregar ejemplos
frame = ttk.LabelFrame(root, text="➕ Agregar Ejemplo")
frame.pack(fill="x", padx=10, pady=10)

ttk.Label(frame, text="Categoría:").grid(row=0, column=0, sticky="e")
categoria = ttk.Combobox(frame, values=list(categorias.keys()))
categoria.grid(row=0, column=1)

ttk.Label(frame, text="Oración original:").grid(row=1, column=0, sticky="e")
original = ttk.Entry(frame, width=40)
original.grid(row=1, column=1)

ttk.Label(frame, text="Versión en pasado:").grid(row=2, column=0, sticky="e")
pasado_entry = ttk.Entry(frame, width=40)
pasado_entry.grid(row=2, column=1)

ttk.Label(frame, text="Con énfasis:").grid(row=3, column=0, sticky="e")
enfatico_entry = ttk.Entry(frame, width=40)
enfatico_entry.grid(row=3, column=1)

ttk.Button(frame, text="Guardar ejemplo", command=agregar_ejemplo).grid(row=4, column=1, pady=5)

# Marco para visualizar ejemplos
frame2 = ttk.LabelFrame(root, text="🔎 Ver Ejemplos Guardados")
frame2.pack(fill="x", padx=10, pady=10)

ttk.Label(frame2, text="Filtrar por categoría:").grid(row=0, column=0, sticky="e")
filtro = ttk.Combobox(frame2, values=[""] + list(categorias.keys()))
filtro.grid(row=0, column=1)

ttk.Button(frame2, text="Mostrar ejemplos", command=ver_ejemplos).grid(row=1, column=1, pady=5)

# Ejecutar
root.mainloop()
