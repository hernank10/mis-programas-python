#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plantas_vocabulario_tkinter.py
Versión con Tkinter del entrenador de vocabulario botánico
(Español / Inglés / Latín).
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

# --- Datos base ---
PLANTAS = [
    ("Caléndula", "Calendula", "Calendula officinalis"),
    ("Manzanilla", "Chamomile", "Matricaria chamomilla"),
    ("Romero", "Rosemary", "Rosmarinus officinalis / Salvia rosmarinus"),
    ("Yerbabuena", "Spearmint", "Mentha spicata"),
    ("Orégano", "Oregano", "Origanum vulgare"),
    ("Moringa", "Moringa", "Moringa oleifera"),
    ("Cidrón", "Lemon verbena", "Aloysia citrodora"),
    ("Canela", "Cinnamon", "Cinnamomum verum"),
    ("Jengibre", "Ginger", "Zingiber officinale"),
    ("Limón", "Lemon", "Citrus limon"),
    ("Laurel", "Bay laurel", "Laurus nobilis"),
    ("Flor de Jamaica", "Hibiscus", "Hibiscus sabdariffa"),
    ("Tomillo", "Thyme", "Thymus vulgaris"),
    ("Menta", "Peppermint", "Mentha × piperita"),
    ("Té verde", "Green tea", "Camellia sinensis"),
    ("Verbena", "Vervain", "Verbena officinalis"),
]

# --- Clase principal ---
class PlantasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌱 Vocabulario de Plantas")
        self.geometry("500x400")
        self.resizable(False, False)

        self.current_index = 0
        self.current_question = None
        self.correct_answer = None

        self.show_menu()

    # --- Menú principal ---
    def show_menu(self):
        self.clear_frame()
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="🌱 Vocabulario de Plantas", font=("Arial", 18)).pack(pady=15)

        ttk.Button(frame, text="Ver lista completa", command=self.show_list).pack(pady=10, fill="x")
        ttk.Button(frame, text="Modo estudio", command=self.show_study).pack(pady=10, fill="x")
        ttk.Button(frame, text="Quiz (preguntas aleatorias)", command=self.show_quiz).pack(pady=10, fill="x")

    # --- Ver lista ---
    def show_list(self):
        self.clear_frame()
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for esp, ing, lat in PLANTAS:
            text = f"{esp}\n   Inglés: {ing}\n   Latín: {lat}\n"
            ttk.Label(scroll_frame, text=text, justify="left", font=("Arial", 12)).pack(anchor="w", pady=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ttk.Button(frame, text="Volver al menú", command=self.show_menu).pack(pady=10)

    # --- Modo estudio ---
    def show_study(self):
        self.clear_frame()
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        self.study_label = ttk.Label(frame, text="", font=("Arial", 14), justify="center")
        self.study_label.pack(pady=20)

        ttk.Button(frame, text="Siguiente", command=self.next_study).pack(pady=10)
        ttk.Button(frame, text="Volver al menú", command=self.show_menu).pack(pady=10)

        self.current_index = 0
        self.show_study_card()

    def show_study_card(self):
        esp, ing, lat = PLANTAS[self.current_index]
        self.study_label.config(text=f"{esp}\nInglés: {ing}\nLatín: {lat}")

    def next_study(self):
        self.current_index = (self.current_index + 1) % len(PLANTAS)
        self.show_study_card()

    # --- Quiz ---
    def show_quiz(self):
        self.clear_frame()
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        self.quiz_label = ttk.Label(frame, text="", font=("Arial", 14))
        self.quiz_label.pack(pady=20)

        self.quiz_buttons = []
        for i in range(4):
            btn = ttk.Button(frame, text="", command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5, fill="x")
            self.quiz_buttons.append(btn)

        ttk.Button(frame, text="Volver al menú", command=self.show_menu).pack(pady=20)

        self.new_question()

    def new_question(self):
        self.current_question = random.choice(PLANTAS)
        esp, ing, lat = self.current_question
        modo = random.choice(["inglés", "latín"])

        if modo == "inglés":
            self.quiz_label.config(text=f"¿Cuál es el nombre INGLÉS de '{esp}'?")
            self.correct_answer = ing
            opciones = [p[1] for p in PLANTAS]
        else:
            self.quiz_label.config(text=f"¿Cuál es el nombre LATÍN de '{esp}'?")
            self.correct_answer = lat
            opciones = [p[2] for p in PLANTAS]

        opciones = random.sample(opciones, 3) + [self.correct_answer]
        random.shuffle(opciones)

        for btn, op in zip(self.quiz_buttons, opciones):
            btn.config(text=op)

    def check_answer(self, i):
        if self.quiz_buttons[i].cget("text") == self.correct_answer:
            messagebox.showinfo("Resultado", "✔️ ¡Correcto!")
        else:
            messagebox.showerror("Resultado", f"✖️ Incorrecto.\nRespuesta: {self.correct_answer}")
        self.new_question()

    # --- Utilidad ---
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()


# --- Ejecutar ---
if __name__ == "__main__":
    app = PlantasApp()
    app.mainloop()
