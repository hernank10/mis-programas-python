import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de verbos de apoyo y sustantivos abstractos
verbos_de_apoyo = ["dar", "echar", "hacer", "tener", "tomar"]
sustantivos_abstractos = ["paseo", "carrera", "alusión", "decisión", "beso", "miedo", "reparos", "atención"]

# Ejemplos de construcciones con verbos de apoyo
ejemplos = [
    "dar un paseo",
    "echar una carrera",
    "hacer alusión",
    "tomar una decisión",
    "dar un beso",
    "perder el miedo",
    "poner reparos",
    "prestar atención"
]

# Función para generar un ejemplo aleatorio
def generar_ejemplo():
    ejemplo = random.choice(ejemplos)
    messagebox.showinfo("Ejemplo Generado", f"Ejemplo de construcción con verbo de apoyo:\n{ejemplo}")

# Función para completar una oración
def completar_oracion():
    verbo = random.choice(verbos_de_apoyo)
    sustantivo = random.choice(sustantivos_abstractos)
    respuesta = simpledialog.askstring("Completar Oración", f"Completa la siguiente construcción:\n{verbo} _____ {sustantivo}.")
    if respuesta:
        construccion_usuario = f"{verbo} {respuesta} {sustantivo}"
        messagebox.showinfo("Construcción Completa", f"Tu construcción es:\n{construccion_usuario}\n\nEjemplo similar: {random.choice(ejemplos)}")
    else:
        messagebox.showwarning("Error", "Debes completar la construcción.")

# Función para verificar si una construcción es correcta
def verificar_construccion():
    construccion_usuario = simpledialog.askstring("Verificar Construcción", "Escribe una construcción con verbo de apoyo:\nPor ejemplo, 'dar un paseo':")
    if construccion_usuario:
        verbo, _, sustantivo = construccion_usuario.partition(" ")
        if verbo in verbos_de_apoyo and sustantivo in sustantivos_abstractos:
            messagebox.showinfo("Resultado", "¡Correcto! Es una construcción válida con verbo de apoyo.")
        else:
            messagebox.showwarning("Resultado", "La construcción no es válida. Asegúrate de usar un verbo de apoyo y un sustantivo abstracto.")
    else:
        messagebox.showwarning("Error", "Debes escribir una construcción.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Verbos de Apoyo")
ventana.geometry("400x300")

# Botones para las funcionalidades
btn_generar = tk.Button(ventana, text="Generar Ejemplo", command=generar_ejemplo, width=30, height=2)
btn_generar.pack(pady=10)

btn_completar = tk.Button(ventana, text="Completar Construcción", command=completar_oracion, width=30, height=2)
btn_completar.pack(pady=10)

btn_verificar = tk.Button(ventana, text="Verificar Construcción", command=verificar_construccion, width=30, height=2)
btn_verificar.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, width=30, height=2)
btn_salir.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
