import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de verbos y ejemplos para practicar
verbos_anticausativos = ["romper", "caer", "perder", "quemar", "abrir", "cerrar"]
ejemplos = [
    "A Juan se le rompió el móvil.",
    "A María se le quemó la comida.",
    "A Pedro se le perdió la llave.",
    "A Luisa se le cayó el vaso.",
    "A Carlos se le abrió la puerta.",
    "A Ana se le cerró la ventana."
]

# Función para generar un ejemplo aleatorio
def generar_ejemplo():
    ejemplo = random.choice(ejemplos)
    messagebox.showinfo("Ejemplo Generado", ejemplo)

# Función para completar una oración
def completar_oracion():
    verbo = random.choice(verbos_anticausativos)
    dativo = simpledialog.askstring("Completar Oración", f"Completa la siguiente oración:\nA _____ se le {verbo} _____.\nIngresa el dativo (por ejemplo, 'Juan'):")
    objeto = simpledialog.askstring("Completar Oración", f"Ingresa el objeto (por ejemplo, 'el móvil'):")
    if dativo and objeto:
        oracion_completa = f"A {dativo} se le {verbo} {objeto}."
        messagebox.showinfo("Oración Completa", f"Tu oración completa es:\n{oracion_completa}\n\n¡Buen trabajo! Aquí tienes un ejemplo similar:\n{random.choice(ejemplos)}")
    else:
        messagebox.showwarning("Error", "Debes ingresar un dativo y un objeto.")

# Función para verificar si una construcción es correcta
def verificar_construccion():
    oracion_usuario = simpledialog.askstring("Verificar Construcción", "Escribe una oración con una construcción anticausativa y dativo:\nPor ejemplo, 'A Juan se le rompió el móvil':")
    if oracion_usuario and oracion_usuario.startswith("A ") and " se le " in oracion_usuario:
        messagebox.showinfo("Resultado", "¡Correcto! Tu oración sigue la estructura de una construcción anticausativa con dativo.")
    else:
        messagebox.showwarning("Resultado", "Parece que tu oración no sigue la estructura correcta. Recuerda que debe comenzar con 'A' y contener 'se le'.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Construcciones Anticausativas con Dativo")
ventana.geometry("400x300")

# Botones para las funcionalidades
btn_generar = tk.Button(ventana, text="Generar Ejemplo", command=generar_ejemplo, width=30, height=2)
btn_generar.pack(pady=10)

btn_completar = tk.Button(ventana, text="Completar Oración", command=completar_oracion, width=30, height=2)
btn_completar.pack(pady=10)

btn_verificar = tk.Button(ventana, text="Verificar Construcción", command=verificar_construccion, width=30, height=2)
btn_verificar.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, width=30, height=2)
btn_salir.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
