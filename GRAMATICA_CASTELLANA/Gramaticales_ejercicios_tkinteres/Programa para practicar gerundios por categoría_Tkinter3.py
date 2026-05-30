import tkinter as tk
from tkinter import messagebox, simpledialog
import re

# Base de datos de ejemplos organizados
ejemplos = {
    "Gerundio (acción simultánea)": [
        "María paseaba cantando alegremente.",
        "Pedro salió corriendo de su casa.",
        "El gato dormía ronroneando."
    ],
    "Causa (porque)": [
        "Se enfermó comiendo comida en mal estado.",
        "Cayó al suelo resbalando en el hielo.",
        "Llegó tarde perdiendo el autobús."
    ],
    "Condición (si)": [
        "Aprenderás más estudiando todos los días.",
        "Te sentirás mejor descansando adecuadamente.",
        "Lograrás el éxito trabajando duro."
    ],
    "Concesión (aunque)": [
        "Siguió corriendo lloviendo a cántaros.",
        "Continuó trabajando sintiéndose mal.",
        "Salió a caminar haciendo frío."
    ]
}

# Función para mostrar ejemplos de la categoría elegida
def mostrar_ejemplos():
    categoria = categoria_var.get()
    texto.delete('1.0', tk.END)
    if categoria in ejemplos:
        for oracion in ejemplos[categoria]:
            texto.insert(tk.END, subrayar_gerundio(oracion) + "\n\n")

# Función para subrayar gerundios en la oración
def subrayar_gerundio(oracion):
    # Subraya palabras terminadas en -ando, -endo, -iendo
    return re.sub(r'\b(\w+(ando|endo|iendo))\b', r'_\1_', oracion)

# Función para agregar un nuevo ejemplo
def agregar_ejemplo():
    categoria = categoria_var.get()
    if categoria:
        nuevo = simpledialog.askstring("Nuevo ejemplo", "Escribe un nuevo ejemplo:")
        if nuevo:
            ejemplos[categoria].append(nuevo)
            mostrar_ejemplos()
    else:
        messagebox.showwarning("Advertencia", "Selecciona primero una categoría.")

# Función para cambiar sujeto o verbo de un ejemplo
def cambiar_sujeto_verbo():
    categoria = categoria_var.get()
    if categoria and ejemplos[categoria]:
        index = simpledialog.askinteger("Número de ejemplo", f"¿Qué número de ejemplo quieres cambiar? (1 a {len(ejemplos[categoria])})")
        if index and 1 <= index <= len(ejemplos[categoria]):
            nuevo = simpledialog.askstring("Nuevo ejemplo", "Escribe la nueva versión del ejemplo:")
            if nuevo:
                ejemplos[categoria][index-1] = nuevo
                mostrar_ejemplos()
        else:
            messagebox.showerror("Error", "Número inválido.")
    else:
        messagebox.showwarning("Advertencia", "No hay ejemplos para cambiar.")

# --- Interfaz Tkinter ---
root = tk.Tk()
root.title("Practica de Gerundios")

# Menú de categorías
categoria_var = tk.StringVar(root)
categoria_var.set("Selecciona una categoría")
opciones = list(ejemplos.keys())
menu = tk.OptionMenu(root, categoria_var, *opciones)
menu.pack(pady=10)

# Botón para mostrar ejemplos
btn_mostrar = tk.Button(root, text="Mostrar Ejemplos", command=mostrar_ejemplos)
btn_mostrar.pack(pady=5)

# Área de texto
texto = tk.Text(root, height=20, width=70, font=("Arial", 12))
texto.pack(padx=10, pady=10)

# Botones adicionales
frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)

btn_agregar = tk.Button(frame_botones, text="Agregar Ejemplo", command=agregar_ejemplo)
btn_agregar.grid(row=0, column=0, padx=5)

btn_cambiar = tk.Button(frame_botones, text="Cambiar Sujeto o Verbo", command=cambiar_sujeto_verbo)
btn_cambiar.grid(row=0, column=1, padx=5)

# Ejecutar
root.mainloop()
