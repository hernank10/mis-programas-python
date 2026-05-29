import tkinter as tk
from tkinter import messagebox
import random

# ==== Datos de ejemplo: 20 ejercicios ====
ejercicios = [
    # Simples
    ("El perro duerme en el sofá.", 
     ["El perro duerme en el sofá. (Correcto)",
      "El perro duerme, en el sofá. (Incorrecto)",
      "El perro, duerme en el sofá. (Incorrecto)"]),

    ("María estudia todas las noches.", 
     ["María estudia todas las noches. (Correcto)",
      "María estudia, todas las noches. (Incorrecto)",
      "María, estudia todas las noches. (Incorrecto)"]),

    # Coordinadas
    ("Fui al cine y luego cené con mis amigos.", 
     ["Fui al cine y luego cené con mis amigos. (Correcto)",
      "Fui al cine, y luego cené con mis amigos. (Incorrecto)",
      "Fui al cine luego cené con mis amigos. (Incorrecto)"]),

    ("El sol brillaba pero hacía frío.", 
     ["El sol brillaba, pero hacía frío. (Correcto)",
      "El sol brillaba pero, hacía frío. (Incorrecto)",
      "El sol brillaba pero hacía, frío. (Incorrecto)"]),

    ("Juan quería salir sin embargo estaba lloviendo.", 
     ["Juan quería salir; sin embargo, estaba lloviendo. (Correcto)",
      "Juan quería salir sin embargo, estaba lloviendo. (Incorrecto)",
      "Juan quería salir, sin embargo estaba lloviendo. (Incorrecto)"]),

    # Subordinadas
    ("Me alegra que hayas venido.", 
     ["Me alegra que hayas venido. (Correcto)",
      "Me alegra, que hayas venido. (Incorrecto)",
      "Me alegra que, hayas venido. (Incorrecto)"]),

    ("Si estudias aprobarás el examen.", 
     ["Si estudias, aprobarás el examen. (Correcto)",
      "Si estudias aprobarás, el examen. (Incorrecto)",
      "Si estudias aprobarás el examen. (Incorrecto)"]),

    ("Aunque estaba cansado siguió trabajando.", 
     ["Aunque estaba cansado, siguió trabajando. (Correcto)",
      "Aunque estaba cansado siguió, trabajando. (Incorrecto)",
      "Aunque estaba, cansado siguió trabajando. (Incorrecto)"]),

    ("El libro que compré ayer es interesante.", 
     ["El libro que compré ayer es interesante. (Correcto)",
      "El libro, que compré ayer, es interesante. (Correcto)",
      "El libro que compré, ayer es interesante. (Incorrecto)"]),

    ("Cuando llegues avísame.", 
     ["Cuando llegues, avísame. (Correcto)",
      "Cuando llegues avísame. (Incorrecto)",
      "Cuando, llegues avísame. (Incorrecto)"]),

    # Con conectores
    ("No vino a clase porque estaba enfermo.", 
     ["No vino a clase porque estaba enfermo. (Correcto)",
      "No vino a clase, porque estaba enfermo. (Correcto)",
      "No vino a clase porque, estaba enfermo. (Incorrecto)"]),

    ("Llegaré tarde ya que hay mucho tráfico.", 
     ["Llegaré tarde, ya que hay mucho tráfico. (Correcto)",
      "Llegaré tarde ya que, hay mucho tráfico. (Incorrecto)",
      "Llegaré tarde ya que hay, mucho tráfico. (Incorrecto)"]),

    ("No estudió así que reprobó.", 
     ["No estudió, así que reprobó. (Correcto)",
      "No estudió así que, reprobó. (Incorrecto)",
      "No estudió así, que reprobó. (Incorrecto)"]),

    ("Lo hizo como le habían dicho.", 
     ["Lo hizo como le habían dicho. (Correcto)",
      "Lo hizo, como le habían dicho. (Correcto)",
      "Lo hizo como, le habían dicho. (Incorrecto)"]),

    ("No solo cantó sino que también bailó.", 
     ["No solo cantó, sino que también bailó. (Correcto)",
      "No solo cantó sino que, también bailó. (Incorrecto)",
      "No solo cantó sino, que también bailó. (Incorrecto)"]),

    # Más variados
    ("Apenas salió de casa empezó a llover.", 
     ["Apenas salió de casa, empezó a llover. (Correcto)",
      "Apenas salió de casa empezó, a llover. (Incorrecto)",
      "Apenas, salió de casa empezó a llover. (Incorrecto)"]),

    ("Te llamaré en cuanto termine la reunión.", 
     ["Te llamaré en cuanto termine la reunión. (Correcto)",
      "Te llamaré, en cuanto termine la reunión. (Incorrecto)",
      "Te llamaré en cuanto, termine la reunión. (Incorrecto)"]),

    ("Salieron temprano para que pudieran descansar.", 
     ["Salieron temprano para que pudieran descansar. (Correcto)",
      "Salieron temprano, para que pudieran descansar. (Correcto)",
      "Salieron temprano para que, pudieran descansar. (Incorrecto)"]),

    ("Aunque no estaba invitado, asistió a la fiesta.", 
     ["Aunque no estaba invitado, asistió a la fiesta. (Correcto)",
      "Aunque no estaba invitado asistió a la fiesta. (Incorrecto)",
      "Aunque, no estaba invitado asistió a la fiesta. (Incorrecto)"]),
]

# ==== Variables de juego ====
puntaje = 0
vidas = 3
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
root.geometry("900x600")

lbl_oracion = tk.Label(root, text="", wraplength=800, font=("Arial", 14))
lbl_oracion.pack(pady=20)

frame_botones = tk.Frame(root)
frame_botones.pack()

opciones_botones = [tk.Button(frame_botones, text="", width=90, height=2, font=("Arial", 12)) for _ in range(3)]
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
