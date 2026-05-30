
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import json
import os
import random
import re

ARCHIVO_EJEMPLOS = "ejemplos_modificadores.json"

# Cargar ejemplos guardados o inicializar
def cargar_ejemplos():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_ejemplos(ejemplos):
    with open(ARCHIVO_EJEMPLOS, "w", encoding="utf-8") as f:
        json.dump(ejemplos[:100], f, indent=4, ensure_ascii=False)

def eliminar_clausula(orf):
    return re.sub(r",? que .*?,?", "", orf)

ejemplos_base = [
    {"explicativa": "Mi hermano, que vive en Canadá, vendrá en diciembre.",
     "esencial": "Mi hermano que vive en Canadá vendrá en diciembre."},
    {"explicativa": "La profesora, que escribió el libro, fue premiada.",
     "esencial": "La profesora que escribió el libro fue premiada."},
    {"explicativa": "Juan, que es médico, no pudo venir.",
     "esencial": "Juan que es médico no pudo venir."}
]

ejemplos_guardados = cargar_ejemplos()
todos_ejemplos = ejemplos_base + ejemplos_guardados

# Funciones de interfaz
def mostrar_teoria():
    teoria = """Un modificador explicativo aporta información adicional, pero no es esencial para identificar al sujeto.
Suele ir entre comas y puede eliminarse sin cambiar el sentido central de la oración.

Ejemplo explicativo:
  Los estudiantes, que entran a la Biblioteca con su carnet, pueden pedir hasta tres libros.
  ➤ Todos los estudiantes pueden hacerlo. La cláusula entre comas solo agrega información.

Ejemplo esencial:
  Los estudiantes que entran a la Biblioteca con su carnet pueden pedir hasta tres libros.
  ➤ Solo pueden hacerlo los que entran con su carnet. Sin esa cláusula, el significado cambia.

🔎 ¿Cómo reconocerlo?
- Si puedes quitar la cláusula sin que cambie el sentido → EXPLICATIVO.
- Si al quitarla se pierde precisión → ESENCIAL."""
    ventana = tk.Toplevel(root)
    ventana.title("Teoría")
    text = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=20)
    text.insert(tk.INSERT, teoria)
    text.pack(padx=10, pady=10)

def cuestionario():
    random.shuffle(todos_ejemplos)
    puntaje = 0

    for ejemplo in todos_ejemplos:
        explicativa, esencial = ejemplo["explicativa"], ejemplo["esencial"]
        opciones = [explicativa, esencial]
        random.shuffle(opciones)

        seleccion = simpledialog.askinteger(
            "Cuestionario",
            f"¿Cuál oración tiene modificador explicativo?\n\n1) {opciones[0]}\n2) {opciones[1]}\n\nEscribe 1 o 2:"
        )
        if seleccion not in [1, 2]:
            continue

        seleccionada = opciones[seleccion - 1]
        correcta = explicativa

        resultado = "✅ Correcto!" if seleccionada == correcta else f"❌ Incorrecto. Era:\n{correcta}"
        mensaje = f"{resultado}\n\n🔍 Eliminando cláusula:\n{seleccionada}\n→ {eliminar_clausula(seleccionada)}"

        if seleccionada == explicativa:
            mensaje += "\n📌 Sigue siendo precisa ➜ EXPLICATIVO."
        else:
            mensaje += "\n📌 Pierde especificidad ➜ ESENCIAL."

        reescrita = simpledialog.askstring("Reescritura", "Reescribe la oración correctamente:")
        if reescrita and reescrita.strip() == seleccionada.strip():
            mensaje += "\n✅ Bien reescrita."
            puntaje += 2
        else:
            mensaje += f"\n🔁 Tu versión no coincide.\n👉 Correcta: {seleccionada}"
            puntaje += 1

        messagebox.showinfo("Resultado", mensaje)

    messagebox.showinfo("Puntaje Final", f"🏁 Puntaje total: {puntaje} de {len(todos_ejemplos)*2}")

def crear_ejemplo():
    if len(ejemplos_guardados) >= 100:
        messagebox.showwarning("Límite alcanzado", "Has alcanzado el límite de 100 ejemplos.")
        return

    explicativa = simpledialog.askstring("Nuevo Ejemplo", "Oración con modificador explicativo (usa comas):")
    esencial = simpledialog.askstring("Nuevo Ejemplo", "Oración con modificador esencial (sin comas):")

    if explicativa and esencial:
        ejemplos_guardados.append({"explicativa": explicativa, "esencial": esencial})
        guardar_ejemplos(ejemplos_guardados)
        messagebox.showinfo("Guardado", "✅ Ejemplo guardado correctamente.")

def ver_ejemplos():
    ventana = tk.Toplevel(root)
    ventana.title("Ejemplos Guardados")
    text = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=20)
    for i, ej in enumerate(ejemplos_guardados, 1):
        text.insert(tk.INSERT, f"{i}. Explicativa: {ej['explicativa']}\n   Esencial:   {ej['esencial']}\n\n")
    text.pack(padx=10, pady=10)

# Interfaz principal
root = tk.Tk()
root.title("Modificadores Explicativos y Esenciales")

tk.Label(root, text="📘 Aprende a identificar modificadores explicativos y esenciales", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="📚 Ver teoría del ensayo", width=40, command=mostrar_teoria).pack(pady=5)
tk.Button(root, text="❓ Cuestionario interactivo", width=40, command=cuestionario).pack(pady=5)
tk.Button(root, text="✍️ Crear y guardar nuevos ejemplos", width=40, command=crear_ejemplo).pack(pady=5)
tk.Button(root, text="📂 Ver ejemplos guardados", width=40, command=ver_ejemplos).pack(pady=5)
tk.Button(root, text="❌ Salir", width=40, command=root.quit).pack(pady=20)

root.mainloop()
