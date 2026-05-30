import tkinter as tk
from tkinter import messagebox

# ---------------- Funciones de ejercicios ------------------

def ejercicio_expresiones_unidas(ventana):
    instrucciones = "Escribe expresiones que deben escribirse juntas.\nEjemplos: asimismo, porque, alrededor."
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_expresiones_cambian_sentido(ventana):
    instrucciones = "Escribe expresiones que cambian de significado si se escriben juntas o separadas.\nEjemplos: porqué / por qué, con que / conqué."
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_tilde_diacritica(ventana):
    instrucciones = "Escribe palabras homónimas con tilde diacrítica.\nEjemplos: tú / tu, él / el, más / mas."
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_palabras_compuestas(ventana):
    instrucciones = "Corrige las siguientes palabras compuestas en mayúsculas sin tilde:\nEJEMPLO: PARARRAYOS, SACAPUNTAS, MEDIODIA"
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_silabas(ventana):
    instrucciones = "Identifica si estas palabras son monosílabas, bisílabas, trisílabas o tetrasílabas.\nEjemplos: sol, casa, teléfono, mariposa."
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_diptongos(ventana):
    instrucciones = "Escribe palabras con diptongos.\nEjemplos: tierra, cielo, aire, fuerte."
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_triptongos(ventana):
    instrucciones = "Escribe palabras con triptongos.\nEjemplos: miau, Uruguay, buey."
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_hiatos(ventana):
    instrucciones = "Escribe palabras con hiatos.\nEjemplos: poesía, aéreo, tía, río."
    mostrar_ejercicio(ventana, instrucciones)

def ejercicio_prefijos(ventana):
    instrucciones = "Escribe palabras con prefijos.\nEjemplos: anteayer, antihéroe, replantear."
    mostrar_ejercicio(ventana, instrucciones)

def mostrar_ejercicio(ventana, instrucciones):
    label = tk.Label(ventana, text=instrucciones, wraplength=500, justify="left")
    label.pack(pady=10)
    entrada = tk.Text(ventana, height=6, width=60)
    entrada.pack(pady=5)
    tk.Button(ventana, text="Enviar", command=lambda: guardar_respuesta(instrucciones, entrada.get("1.0", tk.END))).pack(pady=5)

def guardar_respuesta(instrucciones, respuesta):
    with open("respuestas_usuario.txt", "a", encoding="utf-8") as archivo:
        archivo.write("--- EJERCICIO ---\n")
        archivo.write(instrucciones + "\n")
        archivo.write("Respuesta del usuario:\n" + respuesta + "\n\n")
    messagebox.showinfo("Guardado", "Respuesta guardada correctamente.")

# ---------------- Interfaz principal ------------------

def abrir_ventana(funcion):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Ejercicio")
    nueva_ventana.geometry("650x400")
    funcion(nueva_ventana)

root = tk.Tk()
root.title("Suite de Ejercicios Lingüísticos")
root.geometry("700x650")

titulo = tk.Label(root, text="Menú de Ejercicios", font=("Helvetica", 16))
titulo.pack(pady=20)

# Lista de botones
botones = [
    ("1. Expresiones que se escriben unidas", ejercicio_expresiones_unidas),
    ("2. Expresiones que cambian de sentido (junto/separado)", ejercicio_expresiones_cambian_sentido),
    ("3. Homónimos con tilde diacrítica", ejercicio_tilde_diacritica),
    ("4. Palabras compuestas en mayúsculas", ejercicio_palabras_compuestas),
    ("5. Clasificación por número de sílabas", ejercicio_silabas),
    ("6. Palabras con diptongos", ejercicio_diptongos),
    ("7. Palabras con triptongos", ejercicio_triptongos),
    ("8. Palabras con hiatos", ejercicio_hiatos),
    ("9. Palabras con prefijos", ejercicio_prefijos),
]

for texto, funcion in botones:
    tk.Button(root, text=texto, command=lambda f=funcion: abrir_ventana(f), width=60).pack(pady=5)

root.mainloop()
