import tkinter as tk
import random

# Diccionario con tipos de oraciones simples en inglés
sentences = {
    "Declarative": [
        "I like apples.",
        "She is my friend.",
        "They play football every Saturday."
    ],
    "Interrogative": [
        "Do you like apples?",
        "Is she your friend?",
        "Where do they play football?"
    ],
    "Imperative": [
        "Open the window.",
        "Please, sit down.",
        "Don’t be late."
    ],
    "Exclamatory": [
        "What a beautiful day!",
        "How fast he runs!",
        "That was amazing!"
    ]
}

# Función para seleccionar un tipo de oración
def start_practice(sentence_type):
    global current_type, current_sentence
    current_type = sentence_type
    current_sentence = random.choice(sentences[sentence_type])
    lbl_instruction.config(text=f"Write this {sentence_type} sentence correctly:")
    lbl_example.config(text=current_sentence)
    entry_answer.delete(0, tk.END)

# Función para verificar respuesta
def check_answer():
    user_input = entry_answer.get().strip()
    if user_input == current_sentence:
        lbl_feedback.config(text="✅ Correct!", fg="green")
    else:
        lbl_feedback.config(text=f"❌ Incorrect.\nCorrect: {current_sentence}", fg="red")

# Crear ventana principal
root = tk.Tk()
root.title("English Grammar Trainer - Simple Sentences")
root.geometry("600x400")

# Widgets
lbl_title = tk.Label(root, text="Choose the type of sentence to practice", font=("Arial", 14, "bold"))
lbl_title.pack(pady=10)

frame_menu = tk.Frame(root)
frame_menu.pack(pady=10)

btn_decl = tk.Button(frame_menu, text="Declarative", command=lambda: start_practice("Declarative"))
btn_inter = tk.Button(frame_menu, text="Interrogative", command=lambda: start_practice("Interrogative"))
btn_imper = tk.Button(frame_menu, text="Imperative", command=lambda: start_practice("Imperative"))
btn_excla = tk.Button(frame_menu, text="Exclamatory", command=lambda: start_practice("Exclamatory"))

btn_decl.grid(row=0, column=0, padx=5)
btn_inter.grid(row=0, column=1, padx=5)
btn_imper.grid(row=0, column=2, padx=5)
btn_excla.grid(row=0, column=3, padx=5)

lbl_instruction = tk.Label(root, text="", font=("Arial", 12))
lbl_instruction.pack(pady=10)

lbl_example = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="blue")
lbl_example.pack(pady=5)

entry_answer = tk.Entry(root, width=50, font=("Arial", 12))
entry_answer.pack(pady=5)

btn_check = tk.Button(root, text="Check Answer", command=check_answer)
btn_check.pack(pady=5)

lbl_feedback = tk.Label(root, text="", font=("Arial", 12))
lbl_feedback.pack(pady=10)

# Iniciar
root.mainloop()
