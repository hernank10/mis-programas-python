import tkinter as tk
from tkinter import messagebox, simpledialog
import json

reglas = []

def guardar_datos():
    verbo = entry_verbo.get()
    base = entry_base.get()
    afijo = entry_afijo.get()
    patron = entry_patron.get()
    descripcion = entry_descripcion.get()
    variacion_tipo = entry_variacion_tipo.get()
    variacion_detalle = entry_variacion_detalle.get()
    caso_tipo = entry_caso_tipo.get()
    caso_ejemplo = entry_caso_ejemplo.get()
    regla_redactada = entry_regla.get()

    if not verbo or not base or not afijo:
        messagebox.showwarning("Faltan datos", "Por favor, completa al menos: verbo, base y afijo.")
        return

    regla = {
        "verbo": verbo,
        "base": base,
        "afijo": afijo,
        "patron": patron,
        "descripcion_patron": descripcion,
        "variacion": {"tipo": variacion_tipo, "detalle": variacion_detalle},
        "caso": {"tipo": caso_tipo, "ejemplo": caso_ejemplo},
        "regla_redactada": regla_redactada
    }

    reglas.append(regla)
    messagebox.showinfo("Guardado", "Regla añadida con éxito.")
    limpiar_campos()

def limpiar_campos():
    entry_verbo.delete(0, tk.END)
    entry_base.delete(0, tk.END)
    entry_afijo.delete(0, tk.END)
    entry_patron.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)
    entry_variacion_tipo.delete(0, tk.END)
    entry_variacion_detalle.delete(0, tk.END)
    entry_caso_tipo.delete(0, tk.END)
    entry_caso_ejemplo.delete(0, tk.END)
    entry_regla.delete(0, tk.END)

def mostrar_reglas():
    texto = ""
    for i, r in enumerate(reglas):
        texto += f"[{i+1}] {r['verbo']} | {r['base']} + {r['afijo']}\n"
        texto += f"   Patrón: {r['patron']} ({r['descripcion_patron']})\n"
        texto += f"   Variación: {r['variacion']['tipo']} - {r['variacion']['detalle']}\n"
        texto += f"   Caso: {r['caso']['tipo']} - {r['caso']['ejemplo']}\n"
        texto += f"   Regla: {r['regla_redactada']}\n\n"
    messagebox.showinfo("Reglas registradas", texto or "No hay reglas todavía.")

def guardar_en_archivo():
    with open("reglas_derivacion.json", "w", encoding="utf-8") as f:
        json.dump(reglas, f, indent=4, ensure_ascii=False)
    messagebox.showinfo("Archivo guardado", "Reglas guardadas en reglas_derivacion.json.")

# --- INTERFAZ TKINTER ---
root = tk.Tk()
root.title("Editor de Reglas de Derivación Verbal")

tk.Label(root, text="Verbo derivado:").grid(row=0, column=0)
entry_verbo = tk.Entry(root, width=30)
entry_verbo.grid(row=0, column=1)

tk.Label(root, text="Base léxica:").grid(row=1, column=0)
entry_base = tk.Entry(root, width=30)
entry_base.grid(row=1, column=1)

tk.Label(root, text="Afijo derivativo:").grid(row=2, column=0)
entry_afijo = tk.Entry(root, width=30)
entry_afijo.grid(row=2, column=1)

tk.Label(root, text="Patrón morfológico:").grid(row=3, column=0)
entry_patron = tk.Entry(root, width=30)
entry_patron.grid(row=3, column=1)

tk.Label(root, text="Descripción del patrón:").grid(row=4, column=0)
entry_descripcion = tk.Entry(root, width=30)
entry_descripcion.grid(row=4, column=1)

tk.Label(root, text="Variación (tipo):").grid(row=5, column=0)
entry_variacion_tipo = tk.Entry(root, width=30)
entry_variacion_tipo.grid(row=5, column=1)

tk.Label(root, text="Detalle de la variación:").grid(row=6, column=0)
entry_variacion_detalle = tk.Entry(root, width=30)
entry_variacion_detalle.grid(row=6, column=1)

tk.Label(root, text="Caso (prototípico/excepción):").grid(row=7, column=0)
entry_caso_tipo = tk.Entry(root, width=30)
entry_caso_tipo.grid(row=7, column=1)

tk.Label(root, text="Ejemplo del caso:").grid(row=8, column=0)
entry_caso_ejemplo = tk.Entry(root, width=30)
entry_caso_ejemplo.grid(row=8, column=1)

tk.Label(root, text="Redacta la regla:").grid(row=9, column=0)
entry_regla = tk.Entry(root, width=50)
entry_regla.grid(row=9, column=1)

tk.Button(root, text="Añadir regla", command=guardar_datos).grid(row=10, column=0, pady=10)
tk.Button(root, text="Ver reglas", command=mostrar_reglas).grid(row=10, column=1)
tk.Button(root, text="Guardar archivo", command=guardar_en_archivo).grid(row=11, column=0, columnspan=2)

root.mainloop()
