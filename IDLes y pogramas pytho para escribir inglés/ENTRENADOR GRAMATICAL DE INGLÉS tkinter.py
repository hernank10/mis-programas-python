import tkinter as tk
import random

# ------------------ Datos de práctica ------------------
plurales_regulares = {
    "dog": "dogs",
    "book": "books",
    "car": "cars",
    "table": "tables",
    "cat": "cats"
}

plurales_irregulares = {
    "child": "children",
    "mouse": "mice",
    "man": "men",
    "woman": "women",
    "tooth": "teeth"
}

comparativos_regulares = {
    "big": ["bigger", "biggest"],
    "small": ["smaller", "smallest"],
    "fast": ["faster", "fastest"],
    "tall": ["taller", "tallest"],
    "short": ["shorter", "shortest"]
}

comparativos_irregulares = {
    "good": ["better", "best"],
    "bad": ["worse", "worst"],
    "far": ["farther", "farthest"],
    "little": ["less", "least"],
    "many": ["more", "most"]
}

# ------------------ Ventana principal ------------------
root = tk.Tk()
root.title("Entrenador Gramatical en Inglés")
root.geometry("400x300")

# Variables globales
current_word = ""
current_answer = ""
exercise_type = ""
options = {}

# ------------------ Funciones ------------------
def start_exercise(tipo):
    global exercise_type, options
    exercise_type = tipo

    if tipo == "plurales_regulares":
        options = plurales_regulares
    elif tipo == "plurales_irregulares":
        options = plurales_irregulares
    elif tipo == "comparativos_regulares":
        options = comparativos_regulares
    elif tipo == "comparativos_irregulares":
        options = comparativos_irregulares

    menu_frame.pack_forget()
    practice_frame.pack(fill="both", expand=True)
    new_question()

def new_question():
    global current_word, current_answer
    word = random.choice(list(options.keys()))
    current_word = word

    if exercise_type.startswith("plurales"):
        current_answer = options[word]
        question_label.config(text=f"Escribe el plural de: {word}")
    elif exercise_type == "comparativos_regulares" or exercise_type == "comparativos_irregulares":
        current_answer = options[word]
        question_label.config(text=f"Escribe comparativo y superlativo de: {word}")

    entry.delete(0, tk.END)
    feedback_label.config(text="")

def check_answer():
    user_input = entry.get().strip().lower()

    if exercise_type.startswith("plurales"):
        if user_input == current_answer:
            feedback_label.config(text="✅ ¡Correcto!", fg="green")
        else:
            feedback_label.config(text=f"❌ Incorrecto. Respuesta: {current_answer}", fg="red")
    else:
        parts = user_input.split(",")
        if len(parts) == 2 and [p.strip() for p in parts] == current_answer:
            feedback_label.config(text="✅ ¡Correcto!", fg="green")
        else:
            feedback_label.config(text=f"❌ Incorrecto. Respuesta: {', '.join(current_answer)}", fg="red")

def back_to_menu():
    practice_frame.pack_forget()
    menu_frame.pack(fill="both", expand=True)

# ------------------ Menú principal ------------------
menu_frame = tk.Frame(root)
menu_frame.pack(fill="both", expand=True)

tk.Label(menu_frame, text="Entrenador Gramatical en Inglés", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(menu_frame, text="Plurales Regulares", width=25, command=lambda: start_exercise("plurales_regulares")).pack(pady=5)
tk.Button(menu_frame, text="Plurales Irregulares", width=25, command=lambda: start_exercise("plurales_irregulares")).pack(pady=5)
tk.Button(menu_frame, text="Comparativos y Superlativos Regulares", width=30, command=lambda: start_exercise("comparativos_regulares")).pack(pady=5)
tk.Button(menu_frame, text="Comparativos y Superlativos Irregulares", width=30, command=lambda: start_exercise("comparativos_irregulares")).pack(pady=5)
tk.Button(menu_frame, text="Salir", width=25, command=root.quit).pack(pady=10)

# ------------------ Ventana de práctica ------------------
practice_frame = tk.Frame(root)

question_label = tk.Label(practice_frame, text="", font=("Arial", 12))
question_label.pack(pady=20)

entry = tk.Entry(practice_frame, font=("Arial", 12))
entry.pack(pady=5)

check_btn = tk.Button(practice_frame, text="Comprobar", command=check_answer)
check_btn.pack(pady=5)

feedback_label = tk.Label(practice_frame, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

next_btn = tk.Button(practice_frame, text="Siguiente", command=new_question)
next_btn.pack(pady=5)

back_btn = tk.Button(practice_frame, text="Volver al Menú", command=back_to_menu)
back_btn.pack(pady=10)

# ------------------ Iniciar programa ------------------
root.mainloop()
