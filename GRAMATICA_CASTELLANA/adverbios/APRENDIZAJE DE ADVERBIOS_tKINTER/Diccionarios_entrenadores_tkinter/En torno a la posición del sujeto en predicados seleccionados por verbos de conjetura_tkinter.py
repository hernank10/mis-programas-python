import tkinter as tk
from tkinter import messagebox

def mostrar_teoria():
    teoria_texto = (
        "En torno a la posición del sujeto en predicados seleccionados por verbos de conjetura...\n\n"
        "Ejemplo 1: Considero eso interesante.\n"
        "Ejemplo 2: Considero que eso es interesante.\n\n"
        "Los verbos de conjetura como conjeturar, adivinar, intuir, aventurar, sospechar y esperar,"
        " parecen seguir el mismo comportamiento que considerar, pero presentan restricciones..."
    )
    messagebox.showinfo("Teoría", teoria_texto)

def mostrar_ejemplos():
    ejemplos_texto = (
        "Ejemplo correcto: El libro que Juan considera interesante.\n"
        "Ejemplo incorrecto: *Conjeturábamos eso perdido.\n"
        "Ejemplo incorrecto: *Adivinaban a ese su profesor."
    )
    messagebox.showinfo("Ejemplos", ejemplos_texto)

def evaluar_respuesta():
    respuesta = entrada_texto.get("1.0", tk.END).strip()
    if respuesta:
        messagebox.showinfo("Evaluación", "Tu respuesta ha sido registrada. Analízala y compárala con los ejemplos.")
    else:
        messagebox.showwarning("Atención", "Por favor, escribe una oración antes de evaluar.")

def salir():
    ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Práctica de verbos de conjetura")
ventana.geometry("500x400")

# Crear botones y etiquetas
etiqueta = tk.Label(ventana, text="Menú de Práctica", font=("Arial", 14, "bold"))
etiqueta.pack(pady=10)

btn_teoria = tk.Button(ventana, text="Mostrar Teoría", command=mostrar_teoria)
btn_teoria.pack(pady=5)

btn_ejemplos = tk.Button(ventana, text="Mostrar Ejemplos", command=mostrar_ejemplos)
btn_ejemplos.pack(pady=5)

etiqueta_entrada = tk.Label(ventana, text="Escribe tu propia oración:")
etiqueta_entrada.pack(pady=5)

entrada_texto = tk.Text(ventana, height=5, width=50)
entrada_texto.pack(pady=5)

btn_evaluar = tk.Button(ventana, text="Evaluar Respuesta", command=evaluar_respuesta)
btn_evaluar.pack(pady=5)

btn_salir = tk.Button(ventana, text="Salir", command=salir)
btn_salir.pack(pady=5)

ventana.mainloop()
