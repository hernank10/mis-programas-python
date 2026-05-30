import tkinter as tk
from tkinter import messagebox

import random

# Lista de oraciones condicionales
oraciones = [
    {"incompleta": "Si estudias, __________ el examen.", "respuesta": "aprobarás", "tipo": "indicativo"},
    {"incompleta": "Si tuviera más tiempo, __________ más libros.", "respuesta": "leería", "tipo": "subjuntivo (hipotética)"},
    {"incompleta": "Si me hubieras llamado, __________ contigo.", "respuesta": "habría ido", "tipo": "subjuntivo (irreal pasado)"},
    {"incompleta": "Si llueve, __________ en casa.", "respuesta": "me quedo", "tipo": "indicativo"},
    {"incompleta": "Si vivieras aquí, __________ más a menudo.", "respuesta": "nos veríamos", "tipo": "subjuntivo (hipotética)"},
    {"incompleta": "Si hubiésemos salido antes, no __________ el tren.", "respuesta": "habríamos perdido", "tipo": "subjuntivo (irreal pasado)"},
]

# Ensayo explicativo
ensayo = """\
ENSAYO SOBRE LAS ORACIONES CONDICIONALES

Las oraciones condicionales son estructuras fundamentales del idioma que permiten expresar hipótesis, consecuencias, advertencias, deseos o hechos reales e irreales. Su núcleo es la conjunción "si", que introduce la condición. Estas oraciones se componen de dos partes: la prótasis (la condición) y la apódosis (la consecuencia).

Existen tres grandes tipos:
1. **Condicionales reales o de indicativo**: expresan hechos posibles y comprobables en el presente o futuro. Ejemplo: "Si estudias, aprobarás".
2. **Condicionales hipotéticas o de subjuntivo**: expresan situaciones poco probables o contrarias a la realidad en presente o futuro. Ejemplo: "Si tuviera tiempo, viajaría más".
3. **Condicionales irreales del pasado**: se refieren a situaciones que no ocurrieron. Ejemplo: "Si me hubieras llamado, habría ido".

Dominar las oraciones condicionales permite mejorar la argumentación, la planificación verbal y la capacidad de comunicar consecuencias de acciones no realizadas. Son herramientas clave para el razonamiento lógico, la cortesía verbal y el análisis crítico del discurso.
"""

# Funciones
def nueva_pregunta(modo):
    global pregunta_actual, modo_actual
    pregunta_actual = random.choice(oraciones)
    modo_actual = modo
    entrada.delete(0, tk.END)

    if modo == "completar":
        enunciado.set("Completa la oración: " + pregunta_actual["incompleta"])
    elif modo == "escribir":
        enunciado.set("Escribe la oración completa:\n" + pregunta_actual["incompleta"])
    elif modo == "tipo":
        completa = pregunta_actual["incompleta"].replace("__________", pregunta_actual["respuesta"])
        enunciado.set("Identifica el tipo de condicional:\n" + completa)

def verificar_respuesta():
    resp = entrada.get().strip().lower()
    correcta = ""

    if modo_actual == "completar":
        correcta = pregunta_actual["respuesta"].lower()
    elif modo_actual == "escribir":
        correcta = pregunta_actual["incompleta"].replace("__________", pregunta_actual["respuesta"]).lower()
    elif modo_actual == "tipo":
        correcta = pregunta_actual["tipo"].lower()

    if resp == correcta:
        messagebox.showinfo("Correcto", "✅ ¡Muy bien!")
    else:
        messagebox.showerror("Incorrecto", f"❌ La respuesta correcta era: {correcta}")

def mostrar_ensayo():
    ventana_ensayo = tk.Toplevel()
    ventana_ensayo.title("Ensayo sobre Oraciones Condicionales")
    texto = tk.Text(ventana_ensayo, wrap="word", font=("Arial", 12))
    texto.insert(tk.END, ensayo)
    texto.pack(expand=True, fill="both", padx=10, pady=10)
    texto.config(state="disabled")

# Interfaz principal
ventana = tk.Tk()
ventana.title("Práctica de Oraciones Condicionales")

enunciado = tk.StringVar()
pregunta_actual = {}
modo_actual = ""

tk.Label(ventana, textvariable=enunciado, wraplength=400, font=("Arial", 14)).pack(pady=10)

entrada = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada.pack(pady=5)

tk.Button(ventana, text="Verificar", command=verificar_respuesta).pack(pady=5)

# Opciones de práctica
tk.Label(ventana, text="Selecciona un modo de práctica:", font=("Arial", 12)).pack(pady=10)

tk.Button(ventana, text="1. Completar oración", command=lambda: nueva_pregunta("completar")).pack()
tk.Button(ventana, text="2. Escribir completa", command=lambda: nueva_pregunta("escribir")).pack()
tk.Button(ventana, text="3. Identificar tipo", command=lambda: nueva_pregunta("tipo")).pack()

# Botón para mostrar el ensayo
tk.Label(ventana, text="¿Deseas repasar la teoría?", font=("Arial", 12)).pack(pady=10)
tk.Button(ventana, text="📖 Leer ensayo explicativo", command=mostrar_ensayo).pack(pady=5)

ventana.mainloop()
