import tkinter as tk
from tkinter import messagebox

# Listas de oraciones para practicar
oraciones_reducidas = [
    ("Considero eso interesante.", "Correcto"),
    ("Considero que eso es interesante.", "Correcto"),
    ("Juan cree eso importante.", "Correcto"),
    ("Juan cree que eso es importante.", "Correcto"),
    ("Ella supone eso posible.", "Correcto")
]

oraciones_conjetura = [
    ("Conjeturábamos eso perdido.", "Incorrecto"),
    ("Conjeturábamos que eso estaba perdido.", "Correcto"),
    ("Adivinaban a ese su profesor.", "Incorrecto"),
    ("Adivinaban que ese era su profesor.", "Correcto"),
    ("Sospechaban eso imposible.", "Incorrecto")
]

oraciones_mezcladas = [
    ("Considero eso interesante.", "Correcto", "con reducida"),
    ("Conjeturábamos eso perdido.", "Incorrecto", "con conjetura"),
    ("Juan cree que eso es importante.", "Correcto", "con reducida"),
    ("Adivinaban que ese era su profesor.", "Correcto", "con conjetura"),
    ("Sospechaban eso imposible.", "Incorrecto", "con conjetura")
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

        label_oracion.config(text=oracion)
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

        if (respuesta == "sí" and correcto == "Correcto") or (respuesta == "no" and correcto == "Incorrecto"):
            puntaje += 1
            messagebox.showinfo("Correcto", "¡Respuesta correcta! 👍")
        else:
            messagebox.showinfo("Incorrecto", f"Incorrecto. La oración es '{correcto}'. 👎")
        indice += 1
        practicar(oraciones_actuales, tipo_actual)

# Función para mostrar el menú principal
def mostrar_menu():
    label_oracion.config(text="Selecciona una opción para practicar.")
    label_tipo.config(text="")
    entry_respuesta.config(state=tk.DISABLED)
    boton_verificar.config(state=tk.DISABLED)
    boton_reducidas.config(state=tk.NORMAL)
    boton_conjetura.config(state=tk.NORMAL)
    boton_mezclados.config(state=tk.NORMAL)

# Función para iniciar un tipo de práctica
def iniciar_practica(tipo):
    global oraciones_actuales, tipo_actual, indice, puntaje
    indice = 0
    puntaje = 0
    tipo_actual = tipo
    if tipo == "reducidas":
        oraciones_actuales = oraciones_reducidas
    elif tipo == "conjetura":
        oraciones_actuales = oraciones_conjetura
    elif tipo == "mezclados":
        oraciones_actuales = oraciones_mezcladas
    entry_respuesta.config(state=tk.NORMAL)
    boton_verificar.config(state=tk.NORMAL)
    practicar(oraciones_actuales, tipo)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Verbos de Conjetura")
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

boton_reducidas = tk.Button(ventana, text="Practicar con reducidas", command=lambda: iniciar_practica("reducidas"))
boton_reducidas.pack(pady=5)

boton_conjetura = tk.Button(ventana, text="Practicar con conjetura", command=lambda: iniciar_practica("conjetura"))
boton_conjetura.pack(pady=5)

boton_mezclados = tk.Button(ventana, text="Practicar ambos", command=lambda: iniciar_practica("mezclados"))
boton_mezclados.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
