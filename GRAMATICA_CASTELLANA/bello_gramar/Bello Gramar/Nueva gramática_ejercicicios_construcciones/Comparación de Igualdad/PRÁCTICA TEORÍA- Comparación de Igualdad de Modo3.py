import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import time
import pyttsx3
import speech_recognition as sr
import threading

engine = pyttsx3.init()
user_sentences = []
score = 0
level = 1
questions = [
    {
        "prompt": "Selecciona la forma correcta de igualdad de modo:",
        "options": [
            "Lo hizo igual como tú.",
            "Lo hizo igual que tú.",
            "Lo hizo lo mismo como tú.",
            "Lo hizo tal tú."
        ],
        "answer": "Lo hizo igual que tú."
    },
    {
        "prompt": "¿Cuál es la forma correcta?",
        "options": [
            "Tengo unas gafas lo mismo como las tuyas.",
            "Tengo unas gafas igual como las tuyas.",
            "Tengo unas gafas idénticas a las tuyas.",
            "Tengo unas gafas como idénticas las tuyas."
        ],
        "answer": "Tengo unas gafas idénticas a las tuyas."
    }
]

class ComparacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Construcción Comparativa")
        self.current_question = 0
        self.timer = 10
        self.create_widgets()

    def create_widgets(self):
        self.text_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.text_label.pack(pady=10)

        self.option_buttons = []
        for _ in range(4):
            btn = tk.Button(self.root, text="", width=50, command=lambda i=_: self.check_answer(i))
            btn.pack(pady=2)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(self.root, text="", fg="green", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        self.timer_label = tk.Label(self.root, text="Tiempo restante: 10", font=("Arial", 12))
        self.timer_label.pack(pady=5)

        self.voice_button = tk.Button(self.root, text="Agregar oración por voz", command=self.voice_input)
        self.voice_button.pack(pady=5)

        self.show_button = tk.Button(self.root, text="Mostrar oraciones guardadas", command=self.show_sentences)
        self.show_button.pack(pady=5)
