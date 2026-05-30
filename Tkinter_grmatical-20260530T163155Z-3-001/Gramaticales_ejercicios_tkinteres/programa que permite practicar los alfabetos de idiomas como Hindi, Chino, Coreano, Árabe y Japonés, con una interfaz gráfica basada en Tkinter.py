import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Configuración del lector de texto
engine = pyttsx3.init()

# Configuración de voces según el idioma
voices = {
    "Hindi": "com.apple.speech.synthesis.voice.lekha",
    "Chino": "com.apple.speech.synthesis.voice.tingting",
    "Coreano": "com.apple.speech.synthesis.voice.yuna",
    "Árabe": "com.apple.speech.synthesis.voice.maged",
    "Japonés": "com.apple.speech.synthesis.voice.kyoko"
}

# Diccionario de alfabetos
alphabets = {
    "Hindi": [
        ("अ", "a"), ("आ", "aa"), ("इ", "i"), ("ई", "ii"), ("उ", "u")
    ],
    "Chino": [
        ("你", "nǐ"), ("好", "hǎo"), ("是", "shì"), ("我", "wǒ"), ("的", "de")
    ],
    "Coreano": [
        ("ㄱ", "g/k"), ("ㄴ", "n"), ("ㄷ", "d/t"), ("ㄹ", "r/l"), ("ㅁ", "m")
    ],
    "Árabe": [
        ("ا", "alif"), ("ب", "baa"), ("ت", "taa"), ("ث", "thaa"), ("ج", "jeem")
    ],
    "Japonés": [
        ("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o")
    ]
}

# Función para iniciar el ejercicio del alfabeto
def start_exercise(language):
    alphabet = alphabets[language]
    current_index = 0

    def next_character():
        nonlocal current_index
        if current_index < len(alphabet):
            character, pronunciation = alphabet[current_index]
            char_label.config(text=character)
            phonetic_label.config(text=f"Pronunciación: {pronunciation}")
            entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Completado", "¡Has practicado todos los caracteres!")
            exercise_window.destroy()

    def check_answer():
        nonlocal current_index
        correct = alphabet[current_index][0]
        user_input = entry.get().strip()
        if user_input == correct:
            messagebox.showinfo("Correcto", f"¡Respuesta correcta! ({correct})")
            current_index += 1
            next_character()
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era: {correct}")

    def pronounce_character():
        _, pronunciation = alphabet[current_index]
        engine.setProperty('voice', voices[language])
        engine.say(pronunciation)
        engine.runAndWait()

    # Ventana de ejercicio
    exercise_window = tk.Toplevel()
    exercise_window.title(f"Práctica del alfabeto: {language}")
    tk.Label(exercise_window, text=f"Practicando: {language}", font=("Arial", 14)).pack(pady=10)

    char_label = tk.Label(exercise_window, text="", font=("Arial", 48))
    char_label.pack(pady=10)

    phonetic_label = tk.Label(exercise_window, text="", font=("Arial", 14))
    phonetic_label.pack(pady=10)

    entry = tk.Entry(exercise_window, font=("Arial", 14))
    entry.pack(pady=10)

    tk.Button(exercise_window, text="Validar respuesta", command=check_answer).pack(pady=5)
    tk.Button(exercise_window, text="Escuchar pronunciación", command=pronounce_character).pack(pady=5)
    tk.Button(exercise_window, text="Siguiente carácter", command=next_character).pack(pady=5)

    next_character()

# Función para mostrar el menú de idiomas
def show_menu():
    language = language_var.get()
    if language in alphabets:
        start_exercise(language)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un idioma válido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Práctica del Alfabeto")
root.geometry("400x300")

tk.Label(root, text="Selecciona un idioma para practicar el alfabeto:", font=("Arial", 14)).pack(pady=10)

language_var = tk.StringVar()
language_var.set("Selecciona un idioma")

language_menu = tk.OptionMenu(root, language_var, *alphabets.keys())
language_menu.pack(pady=10)

tk.Button(root, text="Iniciar Práctica", command=show_menu).pack(pady=10)

root.mainloop()
