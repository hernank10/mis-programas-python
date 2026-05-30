import tkinter as tk
from tkinter import messagebox
import random
from num2words import num2words

puntuacion = 0

def actualizar_puntuacion(puntos):
    global puntuacion
    puntuacion += puntos
    lbl_puntos.config(text=f"Puntuación: {puntuacion}")

# ---------- Actividad 1: Ordenar Lista ----------
def ordenar_lista():
    lista = ["subject", "verb", "object", "adjective", "adverb", "preposition", "conjunction"]
    random.shuffle(lista)

    ventana = tk.Toplevel(root)
    ventana.title("Ordenar Lista")
    
    tk.Label(ventana, text="Ordena la lista en orden correcto:").pack()
    tk.Label(ventana, text=", ".join(lista)).pack()

    entradas = []
    for i in range(len(lista)):
        e = tk.Entry(ventana)
        e.pack()
        entradas.append(e)

    def verificar():
        usuario = [e.get().strip().lower() for e in entradas]
        correcto = sorted(lista)
        if usuario == correcto:
            messagebox.showinfo("Resultado", "✅ Correcto")
            actualizar_puntuacion(10)
        else:
            messagebox.showinfo("Resultado", f"❌ Incorrecto\nCorrecto: {', '.join(correcto)}")

    tk.Button(ventana, text="Verificar", command=verificar).pack()

# ---------- Actividad 2: Formar interrogativas ----------
def formar_interrogativas():
    palabras = ["these", "our", "case", "is", "this", "your", "book"]

    ventana = tk.Toplevel(root)
    ventana.title("Formar Interrogativas")

    tk.Label(ventana, text=f"Forma una interrogativa con: {', '.join(palabras)}").pack()
    entrada = tk.Entry(ventana, width=50)
    entrada.pack()

    def verificar():
        oracion = entrada.get().strip()
        if oracion.endswith("?"):
            messagebox.showinfo("Resultado", "✅ Correcto")
            actualizar_puntuacion(10)
        else:
            messagebox.showinfo("Resultado", "❌ Debe terminar con '?'")

    tk.Button(ventana, text="Verificar", command=verificar).pack()

# ---------- Actividad 3: Pasar a plural ----------
def pasar_a_plural():
    oraciones = [
        "The cat is on the roof.",
        "This book is very interesting.",
        "The boy plays in the park.",
        "She has a blue dress.",
        "The apple is red."
    ]

    ventana = tk.Toplevel(root)
    ventana.title("Pasar a Plural")

    i = {"index": 0}

    lbl_oracion = tk.Label(ventana, text=oraciones[0])
    lbl_oracion.pack()

    entrada = tk.Entry(ventana, width=50)
    entrada.pack()

    def siguiente():
        i["index"] += 1
        if i["index"] < len(oraciones):
            lbl_oracion.config(text=oraciones[i["index"]])
            entrada.delete(0, tk.END)
        else:
            messagebox.showinfo("Fin", "Actividad terminada.")

    tk.Button(ventana, text="Siguiente", command=siguiente).pack()

# ---------- Actividad 4: Horas en letras ----------
def horas_en_letras():
    horas = [(3, 15), (7, 45), (12, 0), (9, 5)]
    ventana = tk.Toplevel(root)
    ventana.title("Horas en Letras")

    for h, m in horas:
        tk.Label(ventana, text=f"{h}:{m:02d}").pack()
        e = tk.Entry(ventana, width=40)
        e.pack()

# ---------- Actividad 5: Sumas en letras ----------
def sumas_en_letras():
    ventana = tk.Toplevel(root)
    ventana.title("Sumas en Letras")

    for _ in range(5):
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        resultado = num2words(a+b, lang="en")
        tk.Label(ventana, text=f"{a} + {b} = ?").pack()
        e = tk.Entry(ventana, width=30)
        e.pack()

# ---------- Actividad 6: Horas del día ----------
def horas_del_dia():
    periodos = ["in the morning", "in the afternoon", "in the evening", "at night"]
    horas = [(8, 0), (14, 30), (19, 15), (23, 0)]

    ventana = tk.Toplevel(root)
    ventana.title("Horas del Día")

    for (h, m), periodo in zip(horas, periodos):
        tk.Label(ventana, text=f"{h}:{m:02d} - {periodo}").pack()
        e = tk.Entry(ventana, width=40)
        e.pack()

# ---------- Ventana principal ----------
root = tk.Tk()
root.title("Práctica de Inglés con Tkinter")

tk.Label(root, text="Menú de Actividades", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="1. Ordenar lista", command=ordenar_lista, width=30).pack(pady=2)
tk.Button(root, text="2. Formar interrogativas", command=formar_interrogativas, width=30).pack(pady=2)
tk.Button(root, text="3. Pasar oraciones al plural", command=pasar_a_plural, width=30).pack(pady=2)
tk.Button(root, text="4. Escribir horas en letras", command=horas_en_letras, width=30).pack(pady=2)
tk.Button(root, text="5. Sumas en letras", command=sumas_en_letras, width=30).pack(pady=2)
tk.Button(root, text="6. Horas del día en letras", command=horas_del_dia, width=30).pack(pady=2)
tk.Button(root, text="Salir", command=root.quit, width=30).pack(pady=5)

lbl_puntos = tk.Label(root, text=f"Puntuación: {puntuacion}", font=("Arial", 12))
lbl_puntos.pack(pady=10)

root.mainloop()
