import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

ARCHIVO = "palabras.json"

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_datos():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tabla, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("Guardar", "Datos guardados correctamente.")

# Datos iniciales
tabla = cargar_datos()

# GUI
root = tk.Tk()
root.title("Gestor de Palabras: Prefijación y Composición")
root.geometry("800x600")

# Frame de categorías
frame_cat = tk.Frame(root)
frame_cat.pack(side="left", fill="y", padx=10, pady=10)

label_cat = tk.Label(frame_cat, text="Categorías")
label_cat.pack()

lista_categorias = tk.Listbox(frame_cat)
lista_categorias.pack(fill="y")

# Frame de palabras
frame_pal = tk.Frame(root)
frame_pal.pack(side="right", expand=True, fill="both", padx=10, pady=10)

label_pal = tk.Label(frame_pal, text="Palabras de la categoría")
label_pal.pack()

lista_palabras = tk.Listbox(frame_pal)
lista_palabras.pack(expand=True, fill="both")

def actualizar_lista_categorias():
    lista_categorias.delete(0, tk.END)
    for cat in sorted(tabla.keys()):
        lista_categorias.insert(tk.END, cat)

def mostrar_palabras(evt):
    lista_palabras.delete(0, tk.END)
    idx = lista_categorias.curselection()
    if not idx:
        return
    cat = lista_categorias.get(idx)
    palabras = tabla.get(cat, [])
    for p in palabras:
        lista_palabras.insert(tk.END, f"{p[0]} ({p[1]}) → {p[2]}")

def agregar_palabra():
    cat = simpledialog.askstring("Categoría", "¿A qué categoría pertenece?")
    if not cat:
        return
    palabra = simpledialog.askstring("Palabra", "Nueva palabra:")
    formacion = simpledialog.askstring("Formación", "Ej: prefijo + base")
    significado = simpledialog.askstring("Significado", "¿Qué significa?")
    if cat not in tabla:
        tabla[cat] = []
    tabla[cat].append((palabra, formacion, significado))
    actualizar_lista_categorias()
    messagebox.showinfo("Agregar", "Palabra agregada con éxito.")

# Botones
botones = tk.Frame(root)
botones.pack(side="bottom", fill="x", pady=10)

tk.Button(botones, text="Agregar palabra", command=agregar_palabra).pack(side="left", padx=5)
tk.Button(botones, text="Guardar datos", command=guardar_datos).pack(side="left", padx=5)
tk.Button(botones, text="Salir", command=root.quit).pack(side="right", padx=5)

# Eventos
lista_categorias.bind("<<ListboxSelect>>", mostrar_palabras)

# Inicial
actualizar_lista_categorias()
root.mainloop()
