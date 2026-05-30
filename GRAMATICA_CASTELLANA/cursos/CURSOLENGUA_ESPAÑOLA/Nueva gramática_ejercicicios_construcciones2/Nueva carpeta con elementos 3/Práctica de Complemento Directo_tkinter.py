import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random
import os

MAX_EJEMPLOS = 100
ARCHIVO_EJEMPLOS = "ejemplos_guardados.json"

ejemplos_correctos = [
    "Leí un libro interesante.",
    "Cocinamos una paella deliciosa.",
    "Ella escribió una carta larga.",
    "Compré un regalo para mi madre.",
    "Pintaron la casa de azul.",
    "Escucharon una canción alegre.",
    "Perdiste las llaves del coche.",
    "Rompimos el vaso sin querer.",
    "Encontré una moneda antigua.",
    "Bebí un jugo de naranja."
]

ejemplos_incorrectos = [
    "Leí un interesante libro.",
    "Cocinamos paella una deliciosa.",
    "Ella carta escribió una.",
    "Compré para mi madre un regalo.",
    "Pintaron azul la casa de."
]

categorias = {
    "Cotidianas": [
        "Limpiamos el salón principal.",
        "Lavaron la ropa sucia.",
        "Perdiste las llaves del coche."
    ],
    "Escolares": [
        "Estudié el capítulo cinco.",
        "Escribí un poema de amor.",
        "Leí un libro interesante."
    ],
    "Emocionales": [
        "Perdonó su error.",
        "Ella contó una historia graciosa.",
        "Celebramos el cumpleaños de Ana."
    ]
}

teoria = """El complemento directo (CD), también llamado objeto directo, 
es la parte de la oración que recibe directamente la acción del verbo.
Ejemplo: "Ha fotografiado las nubes" → CD: "las nubes".
Se detecta preguntando ¿qué...? al verbo."""

# Funciones para cargar/guardar
def cargar_ejemplos():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_ejemplos(ejemplos):
    with open(ARCHIVO_EJEMPLOS, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, ensure_ascii=False, indent=2)

# Funciones prácticas
def mostrar_teoria():
    messagebox.showinfo("Teoría", teoria)

def practicar_correctos():
    oracion = random.choice(ejemplos_correctos)
    respuesta = simpledialog.askstring("Práctica", f"¿Cuál es el CD en la oración?\n\n{oracion}")
    if respuesta and respuesta.lower() in oracion.lower():
        messagebox.showinfo("Resultado", "✅ ¡Correcto!")
    else:
        messagebox.showwarning("Resultado", f"❌ Incorrecto.\nLa oración era:\n{oracion}")

def detectar_errores():
    oracion = random.choice(ejemplos_incorrectos)
    simpledialog.askstring("Detección de error", f"¿Cuál es el error en esta oración?\n\n{oracion}")
    messagebox.showinfo("Sugerencia", "💡 Revisa el orden del complemento directo.")

def practicar_categoria():
    cat = random.choice(list(categorias.keys()))
    oracion = random.choice(categorias[cat])
    respuesta = simpledialog.askstring("Categoría", f"Categoría: {cat}\nOración:\n{oracion}\n\n¿Cuál es el CD?")
    if respuesta and respuesta.lower() in oracion.lower():
        messagebox.showinfo("Resultado", "✅ ¡Correcto!")
    else:
        messagebox.showwarning("Resultado", "❌ Intenta de nuevo.")

def crear_ejemplo():
    ejemplos = cargar_ejemplos()
    if len(ejemplos) >= MAX_EJEMPLOS:
        messagebox.showerror("Límite alcanzado", "Ya tienes 100 ejemplos guardados.")
        return
    oracion = simpledialog.askstring("Nuevo ejemplo", "Escribe una oración con complemento directo:")
    cd = simpledialog.askstring("Complemento directo", "¿Cuál es el CD en la oración?")
    if oracion and cd:
        ejemplos.append({"oracion": oracion, "cd": cd})
        guardar_ejemplos(ejemplos)
        messagebox.showinfo("Guardado", "Ejemplo guardado exitosamente.")

def practicar_guardados():
    ejemplos = cargar_ejemplos()
    if not ejemplos:
        messagebox.showwarning("Sin ejemplos", "No hay ejemplos guardados.")
        return
    ejemplo = random.choice(ejemplos)
    respuesta = simpledialog.askstring("Ejemplo guardado", f"Oración:\n{ejemplo['oracion']}\n\n¿Cuál es el CD?")
    if respuesta and respuesta.lower() in ejemplo['cd'].lower():
        messagebox.showinfo("Resultado", "✅ ¡Correcto!")
    else:
        messagebox.showwarning("Resultado", f"❌ Incorrecto. El CD era: {ejemplo['cd']}")

def pregunta_verbo():
    oracion = random.choice(ejemplos_correctos)
    palabras = oracion.split()
    verbo = next((p for p in palabras if p.endswith("é") or p.endswith("ó") or p.endswith("amos")), None)
    respuesta = simpledialog.askstring("Verbo", f"Oración:\n{oracion}\n\n¿Qué verbo se usa?")
    if verbo and respuesta and verbo.lower() in respuesta.lower():
        messagebox.showinfo("Resultado", "✅ ¡Correcto!")
    else:
        messagebox.showwarning("Resultado", f"❌ El verbo era: {verbo}")

def pregunta_funcion():
    oracion = random.choice(ejemplos_correctos)
    palabras = oracion.split()
    if len(palabras) < 4:
        palabra = palabras[2]
    else:
        palabra = palabras[2] if palabras[2] != "una" else palabras[3]
    resaltada = oracion.replace(palabra, f"[{palabra}]")
    respuesta = simpledialog.askstring("Función", f"Oración:\n{resaltada}\n\n¿Qué función cumple la palabra subrayada?")
    if respuesta and "complemento" in respuesta.lower():
        messagebox.showinfo("Resultado", "✅ Correcto: es complemento directo.")
    else:
        messagebox.showwarning("Resultado", "❌ No es correcto. Es complemento directo.")

# Interfaz Tkinter
root = tk.Tk()
root.title("🧠 Práctica de Complemento Directo")
root.geometry("500x480")

tk.Label(root, text="🧠 Complemento Directo - Práctica", font=("Arial", 16)).pack(pady=10)

botones = [
    ("📖 Ver teoría", mostrar_teoria),
    ("✅ Practicar ejemplos correctos", practicar_correctos),
    ("🛠️ Detectar errores", detectar_errores),
    ("📂 Practicar por categoría", practicar_categoria),
    ("➕ Crear nuevo ejemplo", crear_ejemplo),
    ("🔁 Practicar ejemplos guardados", practicar_guardados),
    ("🧩 ¿Qué verbo se usa?", pregunta_verbo),
    ("🧠 Función de palabra subrayada", pregunta_funcion),
    ("🚪 Salir", root.quit)
]

for texto, comando in botones:
    tk.Button(root, text=texto, command=comando, width=40, height=2).pack(pady=5)

root.mainloop()
