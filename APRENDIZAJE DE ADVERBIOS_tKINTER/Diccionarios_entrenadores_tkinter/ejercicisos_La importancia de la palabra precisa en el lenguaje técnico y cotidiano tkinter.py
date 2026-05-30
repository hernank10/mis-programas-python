import tkinter as tk
from tkinter import messagebox
import json
import random

# Cargar ejemplos desde el archivo JSON
with open("ejemplos_vocabulario_50.json", "r", encoding="utf-8") as file:
    ejemplos = json.load(file)

progreso_usuario = []

# Función para mostrar un nuevo ejemplo
def mostrar_nuevo_ejemplo():
    global ejemplo_actual
    ejemplo_actual = random.choice(ejemplos)
    lbl_pregunta.config(text=f"Corrige la palabra subrayada en la oración:\n\n{ejemplo_actual['ejemplo']}")
    entrada.delete(0, tk.END)

# Función para verificar la respuesta del usuario
def verificar_respuesta():
    respuesta = entrada.get().strip().lower()
    correcta = ejemplo_actual["correcto"].lower()

    if respuesta == correcta:
        mensaje = "¡Correcto!"
        estado = "Correcto"
    else:
        mensaje = f"Incorrecto. La forma correcta es: {correcta}"
        estado = "Incorrecto"

    progreso_usuario.append({
        "ejemplo": ejemplo_actual["ejemplo"],
        "respuesta_usuario": respuesta,
        "correcta": correcta,
        "estado": estado
    })

    messagebox.showinfo("Resultado", mensaje)
    mostrar_nuevo_ejemplo()

# Función para guardar el progreso
def guardar_progreso():
    with open("progreso_usuario.json", "w", encoding="utf-8") as f:
        json.dump(progreso_usuario, f, indent=4, ensure_ascii=False)
    messagebox.showinfo("Guardado", "Progreso guardado correctamente.")

# Configuración de la interfaz
ventana = tk.Tk()
ventana.title("Palabra precisa: Ejercicios interactivos")
ventana.geometry("750x500")
ventana.configure(bg="white")

# Widgets
tk.Label(ventana, text="Corrige la palabra mal usada en el siguiente ejemplo:",
         font=("Arial", 14), bg="white").pack(pady=10)

lbl_pregunta = tk.Label(ventana, text="", wraplength=650, font=("Arial", 12), bg="white")
lbl_pregunta.pack(pady=20)

entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
entrada.pack(pady=10)

tk.Button(ventana, text="Verificar", font=("Arial", 12), command=verificar_respuesta).pack(pady=5)
tk.Button(ventana, text="Guardar Progreso", font=("Arial", 12), command=guardar_progreso).pack(pady=5)
tk.Button(ventana, text="Nuevo Ejemplo", font=("Arial", 12), command=mostrar_nuevo_ejemplo).pack(pady=5)

# Mostrar el primer ejemplo
mostrar_nuevo_ejemplo()

ventana.mainloop()
