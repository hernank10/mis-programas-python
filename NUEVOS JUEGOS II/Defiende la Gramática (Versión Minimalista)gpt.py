import tkinter as tk
from tkinter import messagebox
import random
import time

# ==== Datos de ejemplo ====
ejercicios = [
    ("Yo fui al mercado porque quería comprar frutas, pero no tenía dinero.", 
     ["Yo fui al mercado porque quería comprar frutas, pero no tenía dinero. (Correcto)",
      "Yo fui al mercado, porque quería comprar frutas pero no tenía dinero. (Correcto)",
      "Yo fui al mercado porque, quería comprar frutas pero no tenía dinero. (Incorrecto)"]),
    
    ("El perro ladra cuando el cartero llega, el gato duerme tranquilamente.", 
     ["El perro ladra cuando el cartero llega, y el gato duerme tranquilamente. (Correcto)",
      "El perro ladra cuando el cartero llega el gato duerme tranquilamente. (Incorrecto)",
      "El perro ladra, cuando el cartero llega, el gato duerme tranquilamente. (Incorrecto)"]),
    
    ("Salí corriendo pues estaba lloviendo fuerte.", 
     ["Salí corriendo, pues estaba lloviendo fuerte. (Correcto)",
      "Salí corriendo pues, estaba lloviendo fuerte. (Incorrecto)",
      "Salí corriendo. Pues estaba lloviendo fuerte. (Incorrecto)"]),
]

# Puedes duplicar hasta tener 20 variaciones
ejercicios = ejercicios * 7  # total 21 aprox.

# ==== Variables de juego ====
puntaje = 0
vidas = 3
nivel = 1
tiempo_limite = 20  # segundos por ejercicio
tiempo_restante = tiempo_limite
ejercicio_actual = None
opciones_botones = []

# ==== Funciones ====
def nuevo_ejercicio():
    global ejercicio_actual, tiempo_restante
    if vidas <= 0:
        messagebox.showinfo("Fin del juego", f"Te quedaste sin vidas. Puntaje final: {puntaje}")
        root.quit()
    else:
        ejercicio_actual = random.choice(ejercicios)
        lbl_oracion.config(text="Corrige la oración:\n" + ejercicio_actual[0])
        
        for i, boton in enumerate(opciones_botones):
            boton.config(text=ejercicio_actual[1][i], command=lambda i=i: verificar(i))
        
        tiempo_restante = tiempo_limite
        actualizar_tiempo()

def verificar(indice):
    global puntaje, vidas
    opcion = ejercicio_actual[1][indice]
    if "(Correcto)" in opcion:
        puntaje += 10
        lbl_estado.config(text="✅ Correcto!", fg="green")
    else:
        vidas -= 1
        lbl_estado.config(text=f"❌ Incorrecto. Vidas restantes: {vidas}", fg="red")
    
    lbl_puntaje.config(text=f"Puntaje: {puntaje} | Vidas: {vidas}")
    root.after(1500, nuevo_ejercicio)

def actualizar_tiempo():
    global tiempo_restante, vidas
    if tiempo_restante > 0:
        lbl_tiempo.config(text=f"Tiempo: {tiempo_restante}s")
        tiempo_restante -= 1
        root.after(1000, actualizar_tiempo)
    else:
        vidas -= 1
        lbl_estado.config(text=f"⏰ Tiempo agotado. Vidas restantes: {vidas}", fg="orange")
        lbl_puntaje.config(text=f"Puntaje: {puntaje} | Vidas: {vidas}")
        root.after(1500, nuevo_ejercicio)

# ==== Interfaz Tkinter ====
root = tk.Tk()
root.title("Juego Sintáctico - Corrector de Oraciones (Minimalista)")
root.geometry("800x500")

lbl_oracion = tk.Label(root, text="", wraplength=700, font=("Arial", 14))
lbl_oracion.pack(pady=20)

frame_botones = tk.Frame(root)
frame_botones.pack()

opciones_botones = [tk.Button(frame_botones, text="", width=80, height=2, font=("Arial", 12)) for _ in range(3)]
for boton in opciones_botones:
    boton.pack(pady=5)

lbl_estado = tk.Label(root, text="", font=("Arial", 14))
lbl_estado.pack(pady=10)

lbl_puntaje = tk.Label(root, text=f"Puntaje: {puntaje} | Vidas: {vidas}", font=("Arial", 12))
lbl_puntaje.pack()

lbl_tiempo = tk.Label(root, text=f"Tiempo: {tiempo_limite}s", font=("Arial", 12))
lbl_tiempo.pack()

nuevo_ejercicio()
root.mainloop()
