import tkinter as tk
from tkinter import messagebox

# Listas de oraciones para practicar
oraciones_sin_dativo = [
    ("Este culebrón se está {haciendo/volviendo} cada vez más aburrido.", "haciendo"),
    ("El clima se está {haciendo/volviendo} más frío.", "volviendo"),
    ("La situación se está {haciendo/volviendo} más complicada.", "haciendo"),
    ("El niño se está {haciendo/volviendo} más travieso.", "volviendo"),
    ("La película se está {haciendo/volviendo} más interesante.", "haciendo")
]

oraciones_con_dativo = [
    ("Este culebrón se me está {haciendo/volviendo} cada vez más aburrido.", "haciendo"),
    ("El clima se nos está {haciendo/volviendo} más frío.", "haciendo"),
    ("La situación se le está {haciendo/volviendo} más complicada.", "haciendo"),
    ("El niño se te está {haciendo/volviendo} más travieso.", "haciendo"),
    ("La película se les está {haciendo/volviendo} más interesante.", "haciendo")
]

oraciones_mezcladas = [
    ("Este culebrón se está {haciendo/volviendo} cada vez más aburrido.", "haciendo", "sin dativo"),
    ("Este culebrón se me está {haciendo/volviendo} cada vez más aburrido.", "haciendo", "con dativo"),
    ("El clima se está {haciendo/volviendo} más frío.", "volviendo", "sin dativo"),
    ("El clima se nos está {haciendo/volviendo} más frío.", "haciendo", "con dativo"),
    ("La situación se está {haciendo/volviendo} más complicada.", "haciendo", "sin dativo")
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

        label_oracion.config(text=oracion.replace("___", "___ (haciendo/volviendo)"))
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
    boton_sin_dativo.config(state=tk.NORMAL)
    boton_con_dativo.config(state=tk.NORMAL)
    boton_mezclados.config(state=tk.NORMAL)

# Función para iniciar un tipo de práctica
def iniciar_practica(tipo):
    global oraciones_actuales, tipo_actual, indice, puntaje
    indice = 0
    puntaje = 0
    tipo_actual = tipo
    if tipo == "sin dativo":
        oraciones_actuales = oraciones_sin_dativo
    elif tipo == "con dativo":
        oraciones_actuales = oraciones_con_dativo
    elif tipo == "mezclados":
        oraciones_actuales = oraciones_mezcladas
    entry_respuesta.config(state=tk.NORMAL)
    boton_verificar.config(state=tk.NORMAL)
    practicar(oraciones_actuales, tipo)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Hacerse y Volverse")
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

boton_sin_dativo = tk.Button(ventana, text="Practicar sin dativo", command=lambda: iniciar_practica("sin dativo"))
boton_sin_dativo.pack(pady=5)

boton_con_dativo = tk.Button(ventana, text="Practicar con dativo", command=lambda: iniciar_practica("con dativo"))
boton_con_dativo.pack(pady=5)

boton_mezclados = tk.Button(ventana, text="Practicar ambos", command=lambda: iniciar_practica("mezclados"))
boton_mezclados.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
