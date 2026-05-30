import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de ejemplos de oraciones causativas
ejemplos_causativos = [
    "La guerra hizo subir los precios.",
    "La lluvia hace crecer las plantas.",
    "El jefe nos hizo trabajar más.",
    "El profesor hizo estudiar a los alumnos.",
    "El calor hizo derretir el hielo."
]

# Función para generar un ejemplo aleatorio
def generar_ejemplo():
    ejemplo = random.choice(ejemplos_causativos)
    messagebox.showinfo("Ejemplo Generado", f"Ejemplo de oración causativa:\n{ejemplo}")

# Función para completar una oración
def completar_oracion():
    sujetos = ["La guerra", "La lluvia", "El jefe", "El profesor", "El calor"]
    verbos = ["subir", "crecer", "trabajar", "estudiar", "derretir"]
    objetos = ["los precios", "las plantas", "más", "a los alumnos", "el hielo"]

    sujeto = random.choice(sujetos)
    verbo = random.choice(verbos)
    objeto = random.choice(objetos)

    respuesta = simpledialog.askstring("Completar Oración", 
        f"Completa la siguiente oración causativa:\n{sujeto} hizo _____ {objeto}.\nEscribe el verbo en infinitivo:")

    if respuesta:
        oracion_completa = f"{sujeto} hizo {respuesta} {objeto}."
        messagebox.showinfo("Oración Completa", 
            f"Tu oración completa es:\n{oracion_completa}\n\n¡Buen trabajo! Aquí tienes un ejemplo similar:\n{random.choice(ejemplos_causativos)}")
    else:
        messagebox.showwarning("Error", "Debes completar la oración.")

# Función para verificar si una oración es correcta
def verificar_oracion():
    oracion_usuario = simpledialog.askstring("Verificar Oración", 
        "Escribe una oración causativa con 'hacer':\nPor ejemplo, 'La guerra hizo subir los precios':")

    if oracion_usuario:
        if oracion_usuario.lower().startswith(("la", "el")) and "hizo" in oracion_usuario.lower():
            messagebox.showinfo("Resultado", "¡Correcto! Es una oración causativa válida.")
        else:
            messagebox.showwarning("Resultado", "La oración no es válida. Asegúrate de usar 'hacer' como verbo causativo.")
    else:
        messagebox.showwarning("Error", "Debes escribir una oración.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Oraciones Causativas")
ventana.geometry("400x300")

# Botones para las funcionalidades
btn_generar = tk.Button(ventana, text="Generar Ejemplo", command=generar_ejemplo, width=30, height=2)
btn_generar.pack(pady=10)

btn_completar = tk.Button(ventana, text="Completar Oración", command=completar_oracion, width=30, height=2)
btn_completar.pack(pady=10)

btn_verificar = tk.Button(ventana, text="Verificar Oración", command=verificar_oracion, width=30, height=2)
btn_verificar.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, width=30, height=2)
btn_salir.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
