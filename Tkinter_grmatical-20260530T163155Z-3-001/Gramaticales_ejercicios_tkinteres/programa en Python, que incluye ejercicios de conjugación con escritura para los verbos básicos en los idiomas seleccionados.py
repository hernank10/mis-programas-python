import tkinter as tk
from tkinter import messagebox

# Diccionario de verbos básicos por idioma
verbs = {
    "Inglés": ["to be", "to have", "to go", "to do", "to say"],
    "Portugués": ["ser", "estar", "ir", "ter", "falar"],
    "Hebreo": ["להיות", "ללכת", "לעשות", "לדבר", "לאכול"],
    "Latín": ["esse", "habere", "ire", "facere", "dicere"],
    "Griego": ["είμαι", "έχω", "πηγαίνω", "κάνω", "λέω"]
}

# Ejercicios de conjugación
conjugations = {
    "to be": ["I am", "You are", "He/She/It is", "We are", "They are"],
    "ser": ["Eu sou", "Tu és", "Ele/Ela é", "Nós somos", "Eles são"],
    "להיות": ["אני", "אתה/את", "הוא/היא", "אנחנו", "הם/הן"],
    "esse": ["sum", "es", "est", "sumus", "estis", "sunt"],
    "είμαι": ["είμαι", "είσαι", "είναι", "είμαστε", "είστε", "είναι"]
}

# Función para iniciar el ejercicio de conjugación
def start_exercise(language):
    verb = verbs[language][0]  # Elegir el primer verbo como ejemplo
    conjugation = conjugations.get(verb, ["Conjugación no disponible"])
    
    exercise_window = tk.Toplevel()
    exercise_window.title(f"Ejercicio de {language} - {verb}")
    tk.Label(exercise_window, text=f"Conjuga el verbo: {verb}").pack(pady=10)

    entries = []
    for form in conjugation:
        frame = tk.Frame(exercise_window)
        frame.pack(pady=5)
        tk.Label(frame, text=form).pack(side="left", padx=10)
        entry = tk.Entry(frame)
        entry.pack(side="left")
        entries.append((form, entry))
    
    def check_answers():
        correct = 0
        for form, entry in entries:
            if entry.get().strip().lower() == form.lower():
                correct += 1
        messagebox.showinfo("Resultados", f"Conjugas correctamente {correct}/{len(entries)} formas.")
        exercise_window.destroy()
    
    tk.Button(exercise_window, text="Enviar respuestas", command=check_answers).pack(pady=10)

# Función para mostrar el menú de idiomas
def show_menu():
    language = language_var.get()
    if language in verbs:
        start_exercise(language)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un idioma válido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ejercicios de Caligrafía y Conjugación")
root.geometry("400x300")

tk.Label(root, text="Selecciona un idioma para practicar:", font=("Arial", 14)).pack(pady=10)

language_var = tk.StringVar()
language_var.set("Selecciona un idioma")

language_menu = tk.OptionMenu(root, language_var, *verbs.keys())
language_menu.pack(pady=10)

tk.Button(root, text="Iniciar Ejercicio", command=show_menu).pack(pady=10)

root.mainloop()
