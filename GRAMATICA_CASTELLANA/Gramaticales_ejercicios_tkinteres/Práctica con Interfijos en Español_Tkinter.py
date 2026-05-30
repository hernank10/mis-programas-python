import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Diccionario de interfijos con ejemplos y función
interfijos_info = {
    "-ec-":     {"ejemplo": "panecillo", "base": "pan", "funcion": "diminutivo"},
    "-et-":     {"ejemplo": "florete",   "base": "flor", "funcion": "diminutivo"},
    "-in-":     {"ejemplo": "pececillo", "base": "pez", "funcion": "diminutivo"},
    "-it-":     {"ejemplo": "torito",    "base": "toro", "funcion": "diminutivo"},
    "-ar-":     {"ejemplo": "solarillo", "base": "sol", "funcion": "locativo"},
    "-uz-":     {"ejemplo": "rapazuelo", "base": "rapaz", "funcion": "despectivo"},
    "-ill-":    {"ejemplo": "casilla",   "base": "casa", "funcion": "diminutivo"},
}

# Lista para almacenar nuevas oraciones y palabras
oraciones_creadas = []

# Función para validar y guardar oraciones
def guardar_oracion():
    palabra = palabra_entry.get()
    oracion = oracion_entry.get()
    clasificacion = clasificar_palabra(palabra)

    if clasificacion:
        oraciones_creadas.append((palabra, oracion, clasificacion))
        messagebox.showinfo("Guardado", f"Oración guardada como {clasificacion}.")
    else:
        messagebox.showwarning("No válida", "No se detectó interfijo válido en la palabra.")

# Clasificador automático

def clasificar_palabra(palabra):
    for infijo, datos in interfijos_info.items():
        if infijo in palabra:
            return datos["funcion"]
    return None

# Tabla de referencia
def mostrar_tabla():
    tabla_window = tk.Toplevel(root)
    tabla_window.title("Tabla de Interfijos")
    tree = ttk.Treeview(tabla_window, columns=("Base", "Ejemplo", "Función"), show='headings')
    tree.heading("Base", text="Base")
    tree.heading("Ejemplo", text="Derivada")
    tree.heading("Función", text="Función")
    for infijo, datos in interfijos_info.items():
        tree.insert('', 'end', values=(datos["base"], datos["ejemplo"], datos["funcion"]))
    tree.pack(fill=tk.BOTH, expand=True)

# Guardar oraciones a archivo

def exportar_oraciones():
    with open("oraciones_interfijos.txt", "w", encoding="utf-8") as f:
        for palabra, oracion, clasificacion in oraciones_creadas:
            f.write(f"{palabra} | {clasificacion} | {oracion}\n")
    messagebox.showinfo("Exportado", "Las oraciones fueron guardadas en 'oraciones_interfijos.txt'.")

# Interfaz gráfica
root = tk.Tk()
root.title("Práctica con Interfijos en Español")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Palabra derivada:").grid(row=0, column=0)
palabra_entry = tk.Entry(frame, width=30)
palabra_entry.grid(row=0, column=1)

tk.Label(frame, text="Oración:").grid(row=1, column=0)
oracion_entry = tk.Entry(frame, width=50)
oracion_entry.grid(row=1, column=1)

tk.Button(frame, text="Guardar oración", command=guardar_oracion).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(frame, text="Mostrar tabla de interfijos", command=mostrar_tabla).grid(row=3, column=0, columnspan=2)
tk.Button(frame, text="Exportar oraciones", command=exportar_oraciones).grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
