import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json

# Diccionarios base
concepto_texto = """\nLlámanse numerales los nombres que significan número determinado.\n- Cardinales: uno, dos, tres...\n- Ambos, ambas: señalan conjuntamente dos elementos.\n- Ciento (y su apócope): cien pesos, ciento veinte...\n- Mil, millón, billón: como colectivos.\n"""
ejemplos = [
    "Tengo 2 hermanos.", "Vi 100 pájaros volando.", "Amboz alumnos aprobaron.",
    "Compramos 120 libros.", "La empresa perdió varios 1.000.000."
]

user_ejemplos = []  # Hasta 100 ejemplos nuevos
contextos = {}  # Para memorización

# Guardar/Leer ejemplos personalizados
FILE_NAME = "user_ejemplos.json"

def guardar_ejemplos():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(user_ejemplos, f)

def cargar_ejemplos():
    global user_ejemplos
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            user_ejemplos = json.load(f)
    except FileNotFoundError:
        user_ejemplos = []

# Funciones

def mostrar_concepto():
    messagebox.showinfo("Concepto de Numerales", concepto_texto)

def ejercicio_escritura():
    for i, ej in enumerate(ejemplos[:5]):
        entrada = simpledialog.askstring("Ejercicio de Escritura", f"Corrige o reescribe el ejemplo #{i+1}:\n{ej}")
        if entrada:
            print(f"Respuesta del usuario: {entrada}")

def cuestionario():
    aciertos = 0
    for ejemplo in ejemplos[:5]:
        tipo = simpledialog.askstring("Cuestionario", f"¿Qué tipo de numeral aparece en esta oración?\n'{ejemplo}'\n(Tipos: cardinal, ambos, cien, mil)")
        if tipo and tipo.lower() in ejemplo.lower():
            aciertos += 1
    messagebox.showinfo("Resultado", f"Acertaste {aciertos} de 5")

def gestionar_ejemplos():
    cargar_ejemplos()
    while True:
        if len(user_ejemplos) >= 100:
            messagebox.showwarning("Límite alcanzado", "Ya tienes 100 ejemplos guardados.")
            break
        nuevo = simpledialog.askstring("Nuevo ejemplo", "Escribe un nuevo ejemplo o deja vacío para terminar:")
        if not nuevo:
            break
        user_ejemplos.append(nuevo)
    guardar_ejemplos()

def ver_ejemplos():
    cargar_ejemplos()
    texto = "\n".join(user_ejemplos[:20]) if user_ejemplos else "No hay ejemplos aún."
    messagebox.showinfo("Ejemplos personalizados", texto)

def memorizacion_contexto():
    for i in range(3):
        numero = simpledialog.askstring("Memorización", f"Número #{i+1} para usar en contexto:")
        if numero:
            contexto = simpledialog.askstring("Escribe el contexto", f"Usa el número '{numero}' en una oración:")
            if contexto:
                contextos[numero] = contexto
    resumen = "\n".join([f"{n}: {c}" for n, c in contextos.items()])
    messagebox.showinfo("Contextos creados", resumen)

# Interfaz principal
root = tk.Tk()
root.title("Aprendizaje de Numerales")
root.geometry("400x400")

titulo = tk.Label(root, text="APRENDIZAJE DE NUMERALES", font=("Helvetica", 14, "bold"))
titulo.pack(pady=10)

btn1 = tk.Button(root, text="1. Diapositiva conceptual", command=mostrar_concepto)
btn2 = tk.Button(root, text="2. Ejercicio de escritura", command=ejercicio_escritura)
btn3 = tk.Button(root, text="3. Cuestionario clasificatorio", command=cuestionario)
btn4 = tk.Button(root, text="4. Añadir nuevos ejemplos", command=gestionar_ejemplos)
btn5 = tk.Button(root, text="5. Ver ejemplos personalizados", command=ver_ejemplos)
btn6 = tk.Button(root, text="6. Memorización por contexto", command=memorizacion_contexto)
btnSalir = tk.Button(root, text="Salir", command=root.quit)

for btn in (btn1, btn2, btn3, btn4, btn5, btn6, btnSalir):
    btn.pack(pady=5, fill='x', padx=40)

root.mainloop()
