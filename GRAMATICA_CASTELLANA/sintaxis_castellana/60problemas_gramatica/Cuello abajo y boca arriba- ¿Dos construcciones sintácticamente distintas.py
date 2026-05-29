import json
import tkinter as tk
from tkinter import messagebox

PROGRESO_FILE = "progreso_construcciones.json"
EJEMPLOS_FILE = "ejemplos_construcciones.json"

def cargar_ejemplos():
    try:
        with open(EJEMPLOS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"oracion": "Sentí sus lágrimas cayéndome cuello abajo.", "tipo": "Trayecto"},
            {"oracion": "Lo llevaban boca arriba hasta la farmacia.", "tipo": "Manera"}
        ]

def guardar_ejemplos(ejemplos):
    with open(EJEMPLOS_FILE, "w") as file:
        json.dump(ejemplos, file, indent=4)

def mostrar_introduccion():
    messagebox.showinfo("Introducción", "Exploraremos las diferencias entre construcciones como 'cuello abajo' y 'boca arriba'.")

def mostrar_teoria():
    messagebox.showinfo("Teoría", "Las construcciones como 'cuello abajo' expresan trayecto, mientras que 'boca arriba' indica manera.")

def mostrar_ejemplos():
    ejemplos = cargar_ejemplos()
    texto = "\n".join([f"{i+1}. {ej['oracion']} ({ej['tipo']})" for i, ej in enumerate(ejemplos)])
    messagebox.showinfo("Ejemplos", texto)

def agregar_ejemplo():
    def guardar():
        ejemplos = cargar_ejemplos()
        ejemplos.append({"oracion": oracion_entry.get(), "tipo": tipo_var.get()})
        guardar_ejemplos(ejemplos)
        messagebox.showinfo("Éxito", "Ejemplo agregado correctamente.")
        agregar_win.destroy()
    
    agregar_win = tk.Toplevel(root)
    agregar_win.title("Agregar Ejemplo")
    tk.Label(agregar_win, text="Oración:").pack()
    oracion_entry = tk.Entry(agregar_win)
    oracion_entry.pack()
    tk.Label(agregar_win, text="Tipo (Trayecto o Manera):").pack()
    tipo_var = tk.StringVar()
    tipo_entry = tk.Entry(agregar_win, textvariable=tipo_var)
    tipo_entry.pack()
    tk.Button(agregar_win, text="Guardar", command=guardar).pack()

def ejercicios_escritura():
    ejercicios = [
        "Escribe una oración con 'cuello abajo' en sentido de trayecto.",
        "Redacta una oración con 'boca arriba' en sentido de manera.",
        "Convierte 'Lo empujaron hacia abajo' en una estructura con 'cuello abajo'.",
        "Transforma 'Ella estaba tendida de espaldas' en una oración con 'boca arriba'."
    ]
    progreso = {}  # Para futuras mejoras con guardado de progreso
    
    ejercicio_win = tk.Toplevel(root)
    ejercicio_win.title("Ejercicios de Escritura")
    
    respuestas = {}
    for i, ej in enumerate(ejercicios):
        tk.Label(ejercicio_win, text=f"{i+1}. {ej}").pack()
        respuestas[i] = tk.Entry(ejercicio_win, width=50)
        respuestas[i].pack()
    
    tk.Button(ejercicio_win, text="Guardar Respuestas", command=lambda: messagebox.showinfo("Guardado", "Respuestas guardadas.")).pack()

def crear_gui():
    global root
    root = tk.Tk()
    root.title("Práctica de Construcciones Gramaticales")
    tk.Button(root, text="Introducción", command=mostrar_introduccion).pack(fill='x')
    tk.Button(root, text="Teoría", command=mostrar_teoria).pack(fill='x')
    tk.Button(root, text="Ejemplos", command=mostrar_ejemplos).pack(fill='x')
    tk.Button(root, text="Agregar Ejemplo", command=agregar_ejemplo).pack(fill='x')
    tk.Button(root, text="Ejercicios de Escritura", command=ejercicios_escritura).pack(fill='x')
    tk.Button(root, text="Salir", command=root.quit).pack(fill='x')
    root.mainloop()

if __name__ == "__main__":
    crear_gui()
