import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

teoria = """LECCIÓN 11 – 5º GRADO
Tema: El sujeto y el predicado

El sujeto es la persona, animal o cosa de quien se dice algo.
El predicado es lo que se dice del sujeto.

Tipos de sujeto:
- Sujeto expreso: aparece en la oración.
- Sujeto implícito: no aparece, pero se sobreentiende.
"""

ejemplos = """EJEMPLOS:

1. El gato duerme en el sofá.
   Sujeto: El gato / Predicado: duerme en el sofá.

2. Comimos pizza ayer.
   Sujeto implícito: Nosotros / Predicado: Comimos pizza ayer.

3. Mi hermana canta una canción.
   Sujeto: Mi hermana / Predicado: canta una canción.
"""

def mostrar_teoria():
    messagebox.showinfo("Teoría", teoria)

def mostrar_ejemplos():
    messagebox.showinfo("Ejemplos", ejemplos)

def crear_cuento():
    cuento = simpledialog.askstring("Crear cuento", "Escribe un cuento corto:")
    if cuento:
        analisis = simpledialog.askstring("Análisis", "Analiza el cuento: ¿Cuál es el sujeto y el predicado?")
        guardar_cuento(cuento, analisis)

def guardar_cuento(cuento, analisis):
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", title="Guardar análisis")
    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("CUENTO:\n" + cuento + "\n\nANÁLISIS:\n" + analisis)
        messagebox.showinfo("Guardado", "El cuento y el análisis han sido guardados.")

def juego_de_rol():
    mensaje = """JUEGO DE ROL:
1. Escribe oraciones con sujeto implícito.
2. Representa con tus compañeros las acciones de las oraciones.
3. El grupo debe adivinar el sujeto implícito.
"""
    messagebox.showinfo("Juego de rol", mensaje)

def lectura_comprensiva():
    texto = """TEXTO:
La niña corre por el parque y salta la cuerda con alegría.

Ejercicio:
Subraya el sujeto y el predicado. 
¿Qué tipo de sujeto tiene esta oración?
"""
    messagebox.showinfo("Lectura comprensiva", texto)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Lección 11 – Lengua Castellana – 5º Grado")
ventana.geometry("600x400")
ventana.config(bg="#f0f0f0")

titulo = tk.Label(ventana, text="Lección 11: El sujeto y el predicado", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)

btn1 = tk.Button(ventana, text="1. Ver teoría", command=mostrar_teoria, width=40)
btn1.pack(pady=5)

btn2 = tk.Button(ventana, text="2. Ver ejemplos", command=mostrar_ejemplos, width=40)
btn2.pack(pady=5)

btn3 = tk.Button(ventana, text="3. Crear cuento y analizar", command=crear_cuento, width=40)
btn3.pack(pady=5)

btn4 = tk.Button(ventana, text="4. Juego de rol (sujeto implícito)", command=juego_de_rol, width=40)
btn4.pack(pady=5)

btn5 = tk.Button(ventana, text="5. Lectura comprensiva", command=lectura_comprensiva, width=40)
btn5.pack(pady=5)

btn6 = tk.Button(ventana, text="Salir", command=ventana.quit, width=40)
btn6.pack(pady=20)

ventana.mainloop()
