import tkinter as tk
from tkinter import messagebox

# Datos de ejemplo para idiomas
languages_data = {
    "Español": {"intro": "El español es una lengua romance hablada por más de 500 millones de personas.", 
                 "examples": ["amigo", "libro", "agua"]},
    "Japonés": {"intro": "El japonés utiliza los sistemas de escritura Hiragana, Katakana y Kanji.", 
                "examples": ["友達 (amigo)", "本 (libro)", "水 (agua)"]},
    "Chino Mandarín": {"intro": "El chino utiliza caracteres llamados 汉字 (Hanzi).", 
                       "examples": ["朋友 (amigo)", "书 (libro)", "水 (agua)"]},
    "Árabe": {"intro": "El árabe se escribe de derecha a izquierda y tiene un sistema de escritura único.", 
              "examples": ["صديق (amigo)", "كتاب (libro)", "ماء (agua)"]},
    "Ruso": {"intro": "El ruso utiliza el alfabeto cirílico y es la lengua oficial de Rusia.", 
             "examples": ["друг (amigo)", "книга (libro)", "вода (agua)"]}
}

# Guardar progreso en un archivo
def save_progress(language, example):
    with open("progreso.txt", "a") as file:
        file.write(f"Idioma: {language}, Ejemplo practicado: {example}\n")
    messagebox.showinfo("Progreso Guardado", f"Se guardó tu progreso en {language}.")

# Mostrar introducción
def show_intro(language):
    intro_text = languages_data.get(language, {}).get("intro", "No hay datos disponibles.")
    messagebox.showinfo(f"Introducción - {language}", intro_text)

# Practicar caligrafía
def practice_language(language):
    examples = languages_data.get(language, {}).get("examples", [])
    if not examples:
        messagebox.showwarning("Sin ejercicios", f"No hay ejercicios disponibles para {language}.")
        return

    def check_input():
        user_input = entry.get()
        if user_input.strip() == selected_example.strip():
            messagebox.showinfo("¡Correcto!", "Tu caligrafía es correcta.")
            save_progress(language, selected_example)
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era: {selected_example}")

    practice_window = tk.Toplevel(root)
    practice_window.title(f"Práctica - {language}")
    selected_example = examples[0]
    tk.Label(practice_window, text=f"Escribe correctamente: {selected_example}", font=("Arial", 14)).pack(pady=10)
    entry = tk.Entry(practice_window, font=("Arial", 14))
    entry.pack(pady=5)
    tk.Button(practice_window, text="Verificar", command=check_input).pack(pady=10)

# Menú principal
def main_menu():
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Programa Multilingüe de Caligrafía", font=("Arial", 16, "bold")).pack(pady=10)

    for language in languages_data.keys():
        tk.Button(frame, text=language, font=("Arial", 12),
                  command=lambda lang=language: language_menu(lang)).pack(pady=5)

# Menú del idioma seleccionado
def language_menu(language):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text=f"Opciones para {language}", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Button(frame, text="Introducción", font=("Arial", 12),
              command=lambda: show_intro(language)).pack(pady=5)
    tk.Button(frame, text="Practicar Caligrafía", font=("Arial", 12),
              command=lambda: practice_language(language)).pack(pady=5)
    tk.Button(frame, text="Volver al Menú Principal", font=("Arial", 12),
              command=main_menu).pack(pady=10)

# Configuración principal de la ventana
root = tk.Tk()
root.title("Programa Multilingüe de Caligrafía")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

main_menu()

root.mainloop()
