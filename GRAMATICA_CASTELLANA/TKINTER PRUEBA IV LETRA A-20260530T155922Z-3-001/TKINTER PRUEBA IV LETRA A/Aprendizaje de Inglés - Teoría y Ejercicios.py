import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Teoría y ejemplos
# -----------------------------
theory_content = {
    "Gerundio": """📘 Gerundio en inglés:
Se forma con el verbo + ing.

Ejemplos:
- I am reading a book. (Estoy leyendo un libro)
- She enjoys swimming. (Ella disfruta nadar)""",

    "Adverbios": """📘 Adverbios en inglés:
Describen cómo, cuándo o dónde ocurre una acción.

Ejemplos:
- He runs quickly. (Él corre rápidamente)
- They arrived late. (Ellos llegaron tarde)""",

    "Interrogativas negativas": """📘 Interrogativas negativas:
Se forman con el auxiliar + not + sujeto.

Ejemplos:
- Don't you like pizza? (¿No te gusta la pizza?)
- Isn't she coming to the party? (¿No viene ella a la fiesta?)"""
}

# -----------------------------
# Ejercicios
# -----------------------------
exercises = [
    {
        "question": "Choose the correct gerund form: She enjoys ____.",
        "options": ["to swim", "swimming", "swim"],
        "answer": "swimming"
    },
    {
        "question": "Choose the correct adverb: He runs ____.",
        "options": ["quick", "quickly", "quicker"],
        "answer": "quickly"
    },
    {
        "question": "Choose the correct negative interrogative: ____ you coming?",
        "options": ["Is not", "Aren't", "Not are"],
        "answer": "Aren't"
    }
]

# -----------------------------
# Aplicación Tkinter
# -----------------------------
class EnglishApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📚 Aprendizaje de Inglés - Teoría y Ejercicios")
        self.geometry("650x550")

        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Pestaña de teoría
        self.theory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.theory_tab, text="Teoría")

        self.theory_list = tk.Listbox(self.theory_tab, height=5)
        for key in theory_content.keys():
            self.theory_list.insert(tk.END, key)
        self.theory_list.pack(side="left", fill="y", padx=10, pady=10)

        self.theory_text = tk.Text(self.theory_tab, wrap="word")
        self.theory_text.pack(expand=True, fill="both", padx=10, pady=10)

        self.theory_list.bind("<<ListboxSelect>>", self.show_theory)

        # Pestaña de ejercicios
        self.exercise_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.exercise_tab, text="Ejercicios")

        self.current_exercise = 0
        self.selected_option = tk.StringVar()

        self.question_label = tk.Label(self.exercise_tab, text="", wraplength=500, font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self.exercise_tab)
        self.options_frame.pack()

        self.check_button = tk.Button(self.exercise_tab, text="Comprobar", command=self.check_answer)
        self.check_button.pack(pady=5)

        # Entrada para reescribir oración
        tk.Label(self.exercise_tab, text="✍️ Escribe la oración completa con tu respuesta:").pack(pady=5)
        self.rewrite_entry = tk.Entry(self.exercise_tab, width=60)
        self.rewrite_entry.pack(pady=5)

        self.feedback_label = tk.Label(self.exercise_tab, text="", font=("Arial", 11))
        self.feedback_label.pack(pady=10)

        self.load_exercise()

    def show_theory(self, event):
        selection = self.theory_list.curselection()
        if selection:
            key = self.theory_list.get(selection[0])
            self.theory_text.delete("1.0", tk.END)
            self.theory_text.insert(tk.END, theory_content[key])

    def load_exercise(self):
        if self.current_exercise < len(exercises):
            ex = exercises[self.current_exercise]
            self.question_label.config(text=ex["question"])

            # Limpiar opciones anteriores
            for widget in self.options_frame.winfo_children():
                widget.destroy()

            # Crear botones de opción
            self.selected_option.set("")
            for opt in ex["options"]:
                tk.Radiobutton(self.options_frame, text=opt, variable=self.selected_option, value=opt).pack(anchor="w")
            
            self.rewrite_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            messagebox.showinfo("Fin", "Has completado todos los ejercicios 🎉")
            self.quit()

    def check_answer(self):
        ex = exercises[self.current_exercise]
        chosen = self.selected_option.get()
        rewrite_text = self.rewrite_entry.get().strip()

        if chosen == ex["answer"]:
            if ex["answer"] in rewrite_text:
                self.feedback_label.config(text="✅ Correcto y bien reescrito", fg="green")
            else:
                self.feedback_label.config(text="⚠️ Correcto, pero la reescritura no contiene la respuesta", fg="orange")
        else:
            self.feedback_label.config(text=f"❌ Incorrecto. La respuesta correcta era: {ex['answer']}", fg="red")

        self.current_exercise += 1
        self.after(2000, self.load_exercise)


# -----------------------------
# Ejecutar aplicación
# -----------------------------
if __name__ == "__main__":
    app = EnglishApp()
    app.mainloop()
