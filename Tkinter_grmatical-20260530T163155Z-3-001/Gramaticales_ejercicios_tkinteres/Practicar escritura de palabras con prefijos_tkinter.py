import random
import tkinter as tk
from tkinter import messagebox

# Teoría sobre prefijos categorizadores
teoria = """
En español, se considera que los prefijos no cambian la categoría gramatical de la base. 
Sin embargo, algunos prefijos como 'poli-' y 'multi-' pueden convertir sustantivos en adjetivos. 
Ejemplos:
- 'sílaba' (sustantivo) → 'polisílabo' (adjetivo)
- 'color' (sustantivo) → 'multicolor' (adjetivo)
"""

def ocultar_letras(palabra, num_ocultas=2):
    indices = random.sample(range(len(palabra)), num_ocultas)
    palabra_oculta = list(palabra)
    for i in indices:
        palabra_oculta[i] = '_'
    return ''.join(palabra_oculta)

def verificar_respuesta():
    intento = entrada.get().strip().lower()
    if intento == palabra_actual:
        messagebox.showinfo("Correcto", "¡Has escrito la palabra correctamente!")
        siguiente_palabra()
    else:
        messagebox.showerror("Incorrecto", f"La respuesta correcta era: {palabra_actual}")

def siguiente_palabra():
    global palabra_actual, palabra_oculta
    if palabras:
        palabra_actual = palabras.pop(0)
        palabra_oculta = ocultar_letras(palabra_actual)
        etiqueta_palabra.config(text=f"Palabra: {palabra_oculta}")
        entrada.delete(0, tk.END)
    else:
        messagebox.showinfo("Fin", "Has completado todas las palabras.")

def iniciar_juego():
    global palabras
    palabras = [
        "polisílabo", "policromático", "polifacético", "politécnico", "poligonal", "polimórfico", "polilingüe", "polimétrico", "polifónico", "polivalente",
        "políglota", "polimolecular", "politonal", "polideportivo", "poliestratégico", "politético", "polidimensional", "polineuronal", "polifuncional", "polimaterial",
        "policéfalo", "poligrafía", "polimérico", "multicolor", "multiforme", "multilingüe", "multilateral", "multimodal", "multinacional", "multirracial", "multiorgánico",
        "multigrado", "multipropósito", "multimillonario", "multirregional", "multiescalar", "multifacético", "multiconsciente", "multitemático", "multidimensional", "multivariado",
        "multigeneracional", "multilateralista", "multitarea", "multifunción", "multiangular", "multicausal", "multimotor"
    ]
    siguiente_palabra()

def mostrar_teoria():
    messagebox.showinfo("Teoría", teoria)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Práctica de Prefijos Categorizadores")
ventana.geometry("400x300")

# Botones y etiquetas
etiqueta_palabra = tk.Label(ventana, text="", font=("Arial", 14))
etiqueta_palabra.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=10)

boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_respuesta)
boton_verificar.pack(pady=5)

boton_siguiente = tk.Button(ventana, text="Siguiente", command=siguiente_palabra)
boton_siguiente.pack(pady=5)

boton_teoria = tk.Button(ventana, text="Mostrar Teoría", command=mostrar_teoria)
boton_teoria.pack(pady=5)

boton_iniciar = tk.Button(ventana, text="Iniciar Juego", command=iniciar_juego)
boton_iniciar.pack(pady=5)

ventana.mainloop()
