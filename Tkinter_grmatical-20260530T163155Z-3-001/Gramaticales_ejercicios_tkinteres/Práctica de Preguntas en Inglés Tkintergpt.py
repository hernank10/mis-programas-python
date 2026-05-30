import tkinter as tk
from tkinter import messagebox
import random

# ==========================
# LISTA DE EJERCICIOS
# ==========================
exercises = [
    ("¿Hablas inglés?", "Do you speak English?"),
    ("¿Estás cansado?", "Are you tired?"),
    ("¿Te gusta el café?", "Do you like coffee?"),
    ("¿Vendrás mañana?", "Will you come tomorrow?"),
    ("¿Has terminado tu tarea?", "Have you finished your homework?"),
    ("¿Dónde vives?", "Where do you live?"),
    ("¿Qué estás haciendo?", "What are you doing?"),
    ("¿Cuándo empieza la clase?", "When does the class start?"),
    ("¿Por qué estás triste?", "Why are you sad?"),
    ("¿Quién es tu mejor amigo?", "Who is your best friend?"),
    ("¿Quieres té o café?", "Do you want tea or coffee?"),
    ("¿Prefieres leer o mirar televisión?", "Do you prefer reading or watching TV?"),
    ("¿Estás estudiando inglés o francés?", "Are you studying English or French?"),
    ("¿Vas en bus o en tren?", "Are you going by bus or by train?"),
    ("¿Es azul o verde?", "Is it blue or green?"),
    ("Eres estudiante, ¿verdad?", "You are a student, aren’t you?"),
    ("No es fácil, ¿o sí?", "It’s not easy, is it?"),
    ("Él viene, ¿no?", "He is coming, isn’t he?"),
    ("Tienes un hermano, ¿verdad?", "You have a brother, don’t you?"),
    ("Ella no está aquí, ¿o sí?", "She isn’t here, is she?"),
    ("¿Puedes decirme dónde está la estación?", "Can you tell me where the station is?"),
    ("¿Sabes qué hora es?", "Do you know what time it is?"),
    ("¿Me dices cómo llegar al parque?", "Can you tell me how to get to the park?"),
    ("¿Recuerdas dónde dejamos el coche?", "Do you remember where we left the car?"),
    ("¿Podrías explicarme qué significa esto?", "Could you explain what this means?"),
    ("¿Quién no quiere ser feliz?", "Who doesn’t want to be happy?"),
    ("¿Acaso no es obvio?", "Isn’t it obvious?"),
    ("¿Por qué no intentarlo?", "Why not try?"),
    ("¿Quién no lo sabe?", "Who doesn’t know that?"),
    ("¿Qué más da?", "What does it matter?"),
    ("¿Realmente crees eso?", "Do you really believe that?"),
    ("¿De verdad quieres hacerlo?", "Do you truly want to do it?"),
    ("¿Acaso no viste la película?", "Didn’t you actually see the movie?"),
    ("¿En serio dijiste eso?", "Did you really say that?"),
    ("¿Acaso no entiendes?", "Don’t you understand?"),
    ("¿Te gusta el chocolate?", "Do you like chocolate?"),
    ("¿Voy a tener que esperar?", "Am I going to wait?"),
    ("¿Ella está viajando?", "Is she traveling?"),
    ("¿Él dijo la verdad?", "Did he tell the truth?"),
    ("¿Estás listo?", "Are you ready?")
]

# Ampliamos hasta 100
while len(exercises) < 100:
    exercises.extend(exercises[:100 - len(exercises)])

random.shuffle(exercises)

# ==========================
# VARIABLES DE CONTROL
# ==========================
index = 0
score = 0

# ==========================
# FUNCIONES
# ==========================
def check_answer():
    global index, score
    user_answer = entry.get().strip()
    correct_answer = exercises[index][1]

    if user_answer.lower() == correct_answer.lower():
        feedback_label.config(text="✅ Correcto!", fg="green")
        score += 1
    else:
        feedback_label.config(
            text=f"❌ Incorrecto. Respuesta: {correct_answer}", fg="red"
        )

    score_label.config(text=f"Puntaje: {score}/{index+1}")
    entry.delete(0, tk.END)

    index += 1
    if index < len(exercises):
        spanish_label.config(text=exercises[index][0])
    else:
        messagebox.showinfo("Fin", f"¡Terminaste! Puntaje final: {score}/{len(exercises)}")
        window.quit()


def show_help():
    correct_answer = exercises[index][1]
    first_word = correct_answer.split()[0]
    feedback_label.config(text=f"Pista: {first_word} ...", fg="blue")


def show_answer():
    correct_answer = exercises[index][1]
    feedback_label.config(text=f"Respuesta: {correct_answer}", fg="purple")


# ==========================
# INTERFAZ TKINTER
# ==========================
window = tk.Tk()
window.title("Práctica de Preguntas en Inglés")
window.geometry("600x400")

title = tk.Label(window, text="Construcción de preguntas en inglés", font=("Arial", 16, "bold"))
title.pack(pady=10)

spanish_label = tk.Label(window, text=exercises[index][0], font=("Arial", 14))
spanish_label.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 14), width=40)
entry.pack(pady=10)

check_button = tk.Button(window, text="Verificar", font=("Arial", 12), command=check_answer)
check_button.pack(pady=5)

help_button = tk.Button(window, text="Pista", font=("Arial", 12), command=show_help)
help_button.pack(pady=5)

show_button = tk.Button(window, text="Mostrar respuesta", font=("Arial", 12), command=show_answer)
show_button.pack(pady=5)

feedback_label = tk.Label(window, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

score_label = tk.Label(window, text="Puntaje: 0/0", font=("Arial", 12))
score_label.pack(pady=10)

window.mainloop()
