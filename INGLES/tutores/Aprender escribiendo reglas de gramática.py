import tkinter as tk
from tkinter import messagebox

# Diccionario de temas con definiciones breves (puedes ampliar cada una)
temas = {
    "Sujeto y Predicado": "El sujeto es quien realiza la acción y el predicado expresa la acción realizada.",
    "Concordancia Verbal": "El verbo debe concordar en persona y número con el sujeto.",
    "Tiempos Verbales": "Los tiempos verbales sitúan la acción en el presente, pasado o futuro.",
    "Oraciones Simples": "Tienen un solo verbo y expresan una idea completa.",
    "Oraciones Compuestas": "Contienen más de un verbo y se forman por coordinación o subordinación.",
    "Uso de Coma": "Se emplea para separar elementos en una serie, aposiciones o incisos.",
    "Uso de Punto y Coma": "Se usa para separar oraciones relacionadas o elementos complejos en una lista.",
    "Uso de Puntos": "El punto marca el final de una oración o párrafo.",
    "Pronombres Personales": "Sustituyen al sustantivo y concuerdan en género y número.",
    "Adjetivos": "Acompañan al sustantivo y expresan cualidades o propiedades."
}

# Función para verificar lo que el usuario escribe
def verificar_respuesta(tema, entrada_usuario):
    respuesta_correcta = temas[tema].lower().strip()
    respuesta_usuario = entrada_usuario.lower().strip()
    if respuesta_usuario == respuesta_correcta:
        messagebox.showinfo("Correcto ✅", "¡Muy bien! Has escrito la definición correctamente.")
    else:
        messagebox.showwarning("Revisa ✍️", f"Tu respuesta no coincide del todo.\n\nCorrecta:\n{respuesta_correcta}")

# Ventana principal
root = tk.Tk()
root.title("Aprender escribiendo reglas de gramática")
root.geometry("600x400")

# Etiqueta
label = tk.Label(root, text="Selecciona un tema y escribe su definición:", font=("Arial", 12))
label.pack(pady=10)

# Menú desplegable con los temas
var_tema = tk.StringVar(root)
var_tema.set(list(temas.keys())[0])  # valor por defecto
menu = tk.OptionMenu(root, var_tema, *temas.keys())
menu.pack(pady=5)

# Caja de texto para que el usuario escriba
texto = tk.Text(root, height=5, width=60)
texto.pack(pady=10)

# Botón para verificar
def evaluar():
    tema = var_tema.get()
    entrada = texto.get("1.0", tk.END)
    verificar_respuesta(tema, entrada)

btn = tk.Button(root, text="Verificar", command=evaluar, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn.pack(pady=10)

# Iniciar loop
root.mainloop()
