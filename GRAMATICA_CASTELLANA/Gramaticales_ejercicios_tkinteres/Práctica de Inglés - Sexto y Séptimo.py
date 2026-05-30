import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os

# ===== LISTAS DE FRASES =====
# Aquí pegas las 100 frases de Sexto y Séptimo grado
ejercicios_sexto = [
    # Pega aquí las 100 frases de Sexto grado
]

ejercicios_septimo = [
    # Pega aquí las 100 frases de Séptimo grado
]

# Archivo para guardar frases personalizadas
archivo_personal = "frases_personales.txt"

# ===== FUNCIONES =====
def cargar_frases_personales():
    """Carga frases personalizadas desde archivo"""
    if os.path.exists(archivo_personal):
        with open(archivo_personal, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    return []

def guardar_frase_personal(frase):
    """Guarda una frase personalizada en archivo"""
    with open(archivo_personal, "a", encoding="utf-8") as f:
        f.write(frase + "\n")

def iniciar_practica(frases):
    """Inicia la ventana de práctica"""
    if not frases:
        messagebox.showwarning("Aviso", "No hay frases disponibles para practicar.")
        return

    practica = tk.Toplevel(root)
    practica.title("Práctica de Inglés")
    practica.geometry("500x300")

    frase_actual = tk.StringVar()
    frase_mostrada = random.choice(frases)
    frase_actual.set(frase_mostrada)

    tk.Label(practica, text="Traduce o escribe la frase en inglés:", font=("Arial", 14)).pack(pady=10)
    tk.Label(practica, textvariable=frase_actual, font=("Arial", 12), wraplength=400).pack(pady=5)

    entrada = tk.Entry(practica, font=("Arial", 12))
    entrada.pack(pady=5)

    def siguiente():
        nueva_frase = random.choice(frases)
        frase_actual.set(nueva_frase)
        entrada.delete(0, tk.END)

    tk.Button(practica, text="Siguiente", command=siguiente).pack(pady=10)

def agregar_frase():
    """Permite agregar nuevas frases personalizadas"""
    frase = simpledialog.askstring("Nueva frase", "Escribe la nueva frase:")
    if frase:
        guardar_frase_personal(frase)
        messagebox.showinfo("Guardado", "Frase guardada correctamente.")

def mostrar_menu_grado(grado):
    """Muestra el menú de práctica según el grado"""
    if grado == "Sexto":
        frases = ejercicios_sexto + cargar_frases_personales()
    elif grado == "Séptimo":
        frases = ejercicios_septimo + cargar_frases_personales()
    else:
        frases = cargar_frases_personales()

    iniciar_practica(frases)

# ===== INTERFAZ PRINCIPAL =====
root = tk.Tk()
root.title("Práctica de Inglés - Sexto y Séptimo")
root.geometry("400x300")

tk.Label(root, text="Selecciona el grado para practicar", font=("Arial", 14)).pack(pady=20)

tk.Button(root, text="Práctica Sexto Grado", width=25, command=lambda: mostrar_menu_grado("Sexto")).pack(pady=5)
tk.Button(root, text="Práctica Séptimo Grado", width=25, command=lambda: mostrar_menu_grado("Séptimo")).pack(pady=5)
tk.Button(root, text="Agregar nueva frase", width=25, command=agregar_frase).pack(pady=20)
tk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=5)

root.mainloop()
