import tkinter as tk
from tkinter import messagebox

# ============================
# Datos de teoría y ejemplos
# ============================
compound_sentences = {
    "Coordinating Conjunctions": {
        "theory_en": "Two independent clauses joined with a coordinating conjunction (for, and, nor, but, or, yet, so).",
        "theory_es": "Dos oraciones independientes unidas por una conjunción coordinante (for, and, nor, but, or, yet, so).",
        "examples": ["I wanted to go, but it was raining.", "She is smart and she works hard."]
    },
    "Semicolons": {
        "theory_en": "Two independent clauses joined with a semicolon (;).",
        "theory_es": "Dos oraciones independientes unidas por un punto y coma (;).",
        "examples": ["I like coffee; my friend prefers tea.", "It was late; we decided to go home."]
    },
    "Conjunctive Adverbs": {
        "theory_en": "Two independent clauses joined with a semicolon and a conjunctive adverb (however, therefore, moreover, etc.).",
        "theory_es": "Dos oraciones independientes unidas por punto y coma y un adverbio conjuntivo (however, therefore, moreover, etc.).",
        "examples": ["It was raining; however, we went outside.", "She studied a lot; therefore, she passed."]
    }
}

# ============================
# Funciones
# ============================

def show_theory(sentence_type):
    theory_en = compound_sentences[sentence_type]["theory_en"]
    theory_es = compound_sentences[sentence_type]["theory_es"]
    examples = "\n".join(compound_sentences[sentence_type]["examples"])
    messagebox.showinfo(f"Theory: {sentence_type}",
                        f"📘 English:\n{theory_en}\n\n📗 Español:\n{theory_es}\n\n📑 Examples:\n{examples}")

def practice(sentence_type):
    def check_answer():
        user_input = entry.get("1.0", tk.END).strip()
        if len(user_input.split()) >= 5 and any(conj in user_input.lower() for conj in ["and", "but", "or", "so", "yet", ";", "however", "therefore"]):
            messagebox.showinfo("Correct ✅", "Good job! Your sentence looks like a valid compound sentence.")
        else:
            messagebox.showwarning("Try Again ❌", "That doesn’t look like a compound sentence. Try adding a conjunction or semicolon.")
        entry.delete("1.0", tk.END)

    practice_win = tk.Toplevel(root)
    practice_win.title(f"Practice: {sentence_type}")
    tk.Label(practice_win, text=f"Write an example of {sentence_type}:", font=("Arial", 12)).pack(pady=5)
    entry = tk.Text(practice_win, height=4, width=50)
    entry.pack(pady=5)
    tk.Button(practice_win, text="Check", command=check_answer).pack(pady=5)

# ============================
# Interfaz principal
# ============================
root = tk.Tk()
root.title("Compound Sentences Trainer (Inglés - Español)")

menu = tk.Menu(root)
root.config(menu=menu)

sentence_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Compound Sentences", menu=sentence_menu)

for s_type in compound_sentences.keys():
    sentence_menu.add_command(label=f"Theory - {s_type}", command=lambda t=s_type: show_theory(t))
    sentence_menu.add_command(label=f"Practice - {s_type}", command=lambda t=s_type: practice(t))
    sentence_menu.add_separator()

tk.Label(root, text="📚 Compound Sentences Trainer", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Selecciona en el menú el tipo de oración compuesta que quieras estudiar.\n"
                    "Choose from the menu the type of compound sentence to practice.",
         font=("Arial", 12), justify="center").pack(pady=10)

root.mainloop()
