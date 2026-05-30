import tkinter as tk
from tkinter import messagebox, filedialog
import json

# Diccionario para guardar progreso
progreso = {"correctas": 0, "incorrectas": 0}

# Función para clasificar oraciones
def clasificar_oracion():
    oracion = entrada_texto.get("1.0", tk.END).strip()
    clasificacion = seleccion_clasificacion.get()
    
    if not oracion:
        messagebox.showwarning("Advertencia", "Por favor escribe una oración.")
    elif not clasificacion:
        messagebox.showwarning("Advertencia", "Por favor selecciona una clasificación.")
    else:
        # Retroalimentación básica
        if clasificacion in ["Enunciativa", "Interrogativa"]:
            progreso["correctas"] += 1
            messagebox.showinfo("¡Correcto!", f"La oración '{oracion}' se ha clasificado correctamente.")
        else:
            progreso["incorrectas"] += 1
            messagebox.showerror("¡Incorrecto!", f"La oración '{oracion}' no parece ser de tipo '{clasificacion}'.")
        # Limpia la entrada
        entrada_texto.delete("1.0", tk.END)

# Función para guardar progreso
def guardar_progreso():
    archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
    if archivo:
        with open(archivo, "w") as file:
            json.dump(progreso, file)
        messagebox.showinfo("Progreso guardado", f"Tu progreso se guardó en {archivo}")

# Configurar la ventana principal
root = tk.Tk()
root.title("Práctica de Clasificación de Oraciones")

# Marco para entrada de texto
frame_texto = tk.Frame(root, pady=10)
frame_texto.pack()

tk.Label(frame_texto, text="Escribe una oración:").pack()
entrada_texto = tk.Text(frame_texto, height=5, width=50)
entrada_texto.pack()

# Opciones de clasificación
frame_opciones = tk.Frame(root, pady=10)
frame_opciones.pack()

tk.Label(frame_opciones, text="Selecciona el tipo de oración:").pack()

opciones = ["Enunciativa", "Interrogativa", "Exclamativa", "Imperativa", "Dubitativa", "Desiderativa"]
seleccion_clasificacion = tk.StringVar()

for opcion in opciones:
    tk.Radiobutton(frame_opciones, text=opcion, variable=seleccion_clasificacion, value=opcion).pack(anchor="w")

# Botones principales
frame_botones = tk.Frame(root, pady=10)
frame_botones.pack()

tk.Button(frame_botones, text="Clasificar", command=clasificar_oracion).pack(side="left", padx=5)
tk.Button(frame_botones, text="Guardar progreso", command=guardar_progreso).pack(side="left", padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).pack(side="left", padx=5)

# Ejecutar la ventana
root.mainloop()
