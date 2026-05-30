import tkinter as tk
from tkinter import messagebox

# Listas de oraciones para practicar
oraciones_prenominales = [
    ("___ libro es muy interesante.", "este"),
    ("___ casa es grande.", "aquella"),
    ("___ coche es rápido.", "ese"),
    ("___ flores son hermosas.", "estas"),
    ("___ perro es juguetón.", "aquel")
]

oraciones_posnominales = [
    ("El libro ___ es muy interesante.", "este"),
    ("La casa ___ es grande.", "aquella"),
    ("El coche ___ es rápido.", "ese"),
    ("Las flores ___ son hermosas.", "estas"),
    ("El perro ___ es juguetón.", "aquel")
]

oraciones_mezcladas = [
    ("___ libro es muy interesante.", "este", "prenominal"),
    ("El libro ___ es muy interesante.", "este", "posnominal"),
    ("___ casa es grande.", "aquella", "prenominal"),
    ("La casa ___ es grande.", "aquella", "posnominal"),
    ("___ coche es rápido.", "ese", "prenominal"),
    ("El coche ___ es rápido.", "ese", "posnominal")
]

# Función para practicar demostrativos
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

        label_oracion.config(text=oracion.replace("___", "___ (este/ese/aquel)"))
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
    boton_prenominal.config(state=tk.NORMAL)
    boton_posnominal.config(state=tk.NORMAL)
    boton_mezclados.config(state=tk.NORMAL)

# Función para iniciar un tipo de práctica
def iniciar_practica(tipo):
    global oraciones_actuales, tipo_actual, indice, puntaje
    indice = 0
    puntaje = 0
    tipo_actual = tipo
    if tipo == "prenominales":
        oraciones_actuales = oraciones_prenominales
    elif tipo == "posnominales":
        oraciones_actuales = oraciones_posnominales
    elif tipo == "mezclados":
        oraciones_actuales = oraciones_mezcladas
    entry_respuesta.config(state=tk.NORMAL)
    boton_verificar.config(state=tk.NORMAL)
    practicar(oraciones_actuales, tipo)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Demostrativos en Español")
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

boton_prenominal = tk.Button(ventana, text="Practicar Prenominales", command=lambda: iniciar_practica("prenominales"))
boton_prenominal.pack(pady=5)

boton_posnominal = tk.Button(ventana, text="Practicar Posnominales", command=lambda: iniciar_practica("posnominales"))
boton_posnominal.pack(pady=5)

boton_mezclados = tk.Button(ventana, text="Practicar Ambos", command=lambda: iniciar_practica("mezclados"))
boton_mezclados.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
