import tkinter as tk
from tkinter import messagebox

# Listas de oraciones para practicar
oraciones_lo = [
    ("___ bueno de Juan es su generosidad.", "lo"),
    ("___ interesante de la película es su trama.", "lo"),
    ("___ malo de la situación es que no tiene solución.", "lo"),
    ("___ importante de este proyecto es su impacto social.", "lo"),
    ("___ curioso de este fenómeno es su frecuencia.", "lo")
]

oraciones_sustantivos = [
    ("La ___ de Juan es admirable.", "bondad"),
    ("La ___ de los políticos es cuestionable.", "honestidad"),
    ("La ___ de la película es impresionante.", "complejidad"),
    ("La ___ de la situación es preocupante.", "gravedad"),
    ("La ___ de este proyecto es notable.", "importancia")
]

oraciones_mezcladas = [
    ("___ bueno de Juan es su generosidad.", "lo", "con 'lo'"),
    ("La ___ de Juan es admirable.", "bondad", "sustantivo abstracto"),
    ("___ interesante de la película es su trama.", "lo", "con 'lo'"),
    ("La ___ de los políticos es cuestionable.", "honestidad", "sustantivo abstracto"),
    ("___ malo de la situación es que no tiene solución.", "lo", "con 'lo'")
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

        label_oracion.config(text=oracion.replace("___", "___ (lo/la)" if tipo == "con 'lo'" else "___ (bondad/honestidad/complejidad/gravedad/importancia)"))
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
    boton_lo.config(state=tk.NORMAL)
    boton_sustantivos.config(state=tk.NORMAL)
    boton_mezclados.config(state=tk.NORMAL)

# Función para iniciar un tipo de práctica
def iniciar_practica(tipo):
    global oraciones_actuales, tipo_actual, indice, puntaje
    indice = 0
    puntaje = 0
    tipo_actual = tipo
    if tipo == "con 'lo'":
        oraciones_actuales = oraciones_lo
    elif tipo == "sustantivos abstractos":
        oraciones_actuales = oraciones_sustantivos
    elif tipo == "mezclados":
        oraciones_actuales = oraciones_mezcladas
    entry_respuesta.config(state=tk.NORMAL)
    boton_verificar.config(state=tk.NORMAL)
    practicar(oraciones_actuales, tipo)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Nominalizaciones Deadjetivales")
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

boton_lo = tk.Button(ventana, text="Practicar con 'lo'", command=lambda: iniciar_practica("con 'lo'"))
boton_lo.pack(pady=5)

boton_sustantivos = tk.Button(ventana, text="Practicar sustantivos abstractos", command=lambda: iniciar_practica("sustantivos abstractos"))
boton_sustantivos.pack(pady=5)

boton_mezclados = tk.Button(ventana, text="Practicar ambos", command=lambda: iniciar_practica("mezclados"))
boton_mezclados.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
