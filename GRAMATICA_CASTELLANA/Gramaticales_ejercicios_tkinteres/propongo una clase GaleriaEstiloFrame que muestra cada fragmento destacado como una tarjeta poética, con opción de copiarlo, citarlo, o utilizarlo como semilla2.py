import tkinter as tk
import json, os, random

def lanzar_meditacion():
    # Cargar fragmento
    archivo = "galeria_estilo.json"
    if not os.path.exists(archivo):
        return tk.messagebox.showinfo("Sin galería", "No hay fragmentos aún.")
    with open(archivo, "r", encoding="utf-8") as f:
        fragmentos = json.load(f)
    if not fragmentos:
        return tk.messagebox.showinfo("Vacía", "La galería está vacía.")
    seleccionado = random.choice(fragmentos)

    # Crear ventana de meditación
    medit = tk.Toplevel()
    medit.title("💭 Meditación Lingüística")
    medit.configure(bg="#e0f7fa")
    medit.geometry("700x300")

    # Color evocador (simple ejemplo)
    colores = {"Narrativo": "#e1f5fe", "Argumentativo": "#f3e5f5", "Explicativo": "#fff9c4"}
    color = colores.get(seleccionado["tipo"], "#f5f5f5")
    medit.configure(bg=color)

    # Mostrar texto
    tk.Label(medit, text=f"🌱 Fragmento [{seleccionado['tipo']}]", bg=color,
             font=("Georgia", 14, "bold")).pack(pady=10)
    area = tk.Message(medit, text=seleccionado["contenido"], width=650,
                      font=("Georgia", 13), bg=color, justify="center")
    area.pack(pady=20)

    # Cierre contemplativo
    tk.Button(medit, text="✨ Cerrar y continuar el viaje", command=medit.destroy).pack(pady=10)
