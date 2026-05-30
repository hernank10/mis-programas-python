import tkinter as tk
from tkinter import messagebox

# Listas de oraciones para practicar
oraciones_estaticas = [
    ("Juan ___ alto.", "es"),
    ("María ___ morena.", "es"),
    ("El libro ___ interesante.", "es"),
    ("La casa ___ grande.", "es"),
    ("El perro ___ juguetón.", "es")
]

oraciones_dinamicas = [
    ("Juan ___ cansado.", "está"),
    ("María ___ contenta.", "está"),
    ("El niño ___ aburrido.", "está"),
    ("La comida ___ fría.", "está"),
    ("El clima ___ nublado.", "está")
]

oraciones_mezcladas = [
    ("Juan ___ alto.", "es", "estático"),
    ("María ___ contenta.", "está", "dinámico"),
    ("El libro ___ interesante.", "es", "estático"),
    ("El niño ___ aburrido.", "está", "dinámico"),
    ("La casa ___ grande.", "es", "estático")
]

# Función para practicar
def practicar(oraciones, tipo):
    global indice, puntaje
    if indice < len(oraciones):
        oracion_actual = oraciones[indice]
        if tipo == "mezclados":
            oracion, correcto, tipo_demo = oracion_actual
            label_tipo.config(text=f"Tipo: {tipo_demo}")
        else:
            oracion, correcto = oracion_actual
            label_tipo.config(text="")

        label_oracion.config(text=oracion.replace("___", "___ (ser/estar)"))
        entry_respuesta.delete(0, tk.END)
    else:
        messagebox.showinfo("Fin del ejercicio", f"Has completado el ejercicio. Puntaje: {puntaje}/{len(oraciones)}")
        indice = 0
        puntaje = 0
        mostrar_menu()

# Función para verificar la respuesta
def verificar_respuesta():
    global indice, puntaje
    respuesta = entry_respuesta.get().strip().lower()
    if indice < len(oraciones_actuales):
        if tipo_actual == "mezclados":
            oracion, correcto, tipo_demo = oraciones_actuales[indice]
        else:
            oracion, correcto = oraciones_actuales[indice]

        if respuesta == correcto:
            puntaje += 1
            messagebox.showinfo("Correcto", "¡Respuesta correcta! 👍")
        else:
            messagebox.showinfo("Incorrecto", f"Incorrecto. La respuesta correcta es '{correcto}'. 👎")
        indice += 1
        practicar(oraciones_actuales, tipo_actual)

# Función para mostrar el menú principal
def mostrar_menu():
    label_oracion.config(text="Selecciona una opción para practicar.")
    label_tipo.config(text="")
    entry_respuesta.config(state=tk.DISABLED)
    boton_verificar.config(state=tk.DISABLED)
    boton_estaticos.config(state=tk.NORMAL)
    boton_dinamicos.config(state=tk.NORMAL)
    boton_mezclados.config(state=tk.NORMAL)

# Función para iniciar un tipo de práctica
def iniciar_practica(tipo):
    global oraciones_actuales, tipo_actual, indice, puntaje
    indice = 0
    puntaje = 0
    tipo_actual = tipo
    if tipo == "estáticos":
        oraciones_actuales = oraciones_estaticas
    elif tipo == "dinámicos":
        oraciones_actuales = oraciones_dinamicas
    elif tipo == "mezclados":
        oraciones_actuales = oraciones_mezcladas
    entry_respuesta.config(state=tk.NORMAL)
    boton_verificar.config(state=tk.NORMAL)
    practicar(oraciones_actuales, tipo)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Oraciones Copulativas")
ventana.geometry("500x300")

# Variables globales
indice = 0
puntaje = 0
oraciones_actuales = []
tipo_actual = ""

# Elementos de la interfaz
label_oracion = tk.Label(ventana, text="Selecciona una opción para practicar.", wraplength=400)
label_oracion.pack(pady=10)

label_tipo = tk.Label(ventana, text="", fg="blue")
label_tipo.pack(pady=5)

entry_respuesta = tk.Entry(ventana, state=tk.DISABLED)
entry_respuesta.pack(pady=10)

boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_respuesta, state=tk.DISABLED)
boton_verificar.pack(pady=5)

boton_estaticos = tk.Button(ventana, text="Practicar atributos estáticos", command=lambda: iniciar_practica("estáticos"))
boton_estaticos.pack(pady=5)

boton_dinamicos = tk.Button(ventana, text="Practicar atributos dinámicos", command=lambda: iniciar_practica("dinámicos"))
boton_dinamicos.pack(pady=5)

boton_mezclados = tk.Button(ventana, text="Practicar ambos", command=lambda: iniciar_practica("mezclados"))
boton_mezclados.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
