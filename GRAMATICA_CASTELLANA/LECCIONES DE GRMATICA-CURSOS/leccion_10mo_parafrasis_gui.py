import tkinter as tk
import random

# Datos
teoria_texto = """
LECCIÓN 6 – PARÁFRASIS ARGUMENTATIVA

Reformular significa decir lo mismo con otras palabras, manteniendo el sentido original.

🔹 Tipos:
- Lexical: cambio de palabras
- Sintáctica: cambio de orden
- Argumentativa: enfoque personal sobre la idea
"""

ejercicios = [
    {"original": "Leer cada día mejora la expresión escrita.", "parafrasis": "La lectura diaria ayuda a escribir mejor."},
    {"original": "Cuidar el medio ambiente es responsabilidad de todos.", "parafrasis": "Todos debemos proteger la naturaleza."},
    {"original": "Dormir bien mejora el rendimiento escolar.", "parafrasis": "El descanso adecuado beneficia el desempeño académico."}
]

# Funciones
def mostrar_teoria():
    salida.config(state="normal")
    salida.delete(1.0, tk.END)
    salida.insert(tk.END, teoria_texto)
    salida.config(state="disabled")

def mostrar_ejemplo():
    ejemplo = random.choice(ejercicios)
    entrada.delete(0, tk.END)
    resultado.config(text="")
    original_label.config(text=f"Frase original:\n{ejemplo['original']}")
    verificar_btn.config(command=lambda: verificar(ejemplo["parafrasis"]))

def verificar(respuesta_correcta):
    respuesta_usuario = entrada.get().lower().strip()
    if respuesta_correcta.lower() in respuesta_usuario:
        resultado.config(text="✅ ¡Paráfrasis correcta!", fg="green")
    else:
        resultado.config(text=f"❌ Ejemplo válido:\n{respuesta_correcta}", fg="red")

# Interfaz
root = tk.Tk()
root.title("Sintaxis Quest EDU – Paráfrasis Argumentativa")
root.geometry("600x500")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="📘 Teoría de la lección", font=("Helvetica", 14)).pack()
btn_teoria = tk.Button(frame, text="Ver teoría", command=mostrar_teoria)
btn_teoria.pack()

salida = tk.Text(frame, height=7, wrap="word", bg="#f0f0f0")
salida.pack()
salida.config(state="disabled")

tk.Label(frame, text="📚 Ejercicio interactivo", font=("Helvetica", 14)).pack(pady=10)
btn_ejemplo = tk.Button(frame, text="Nuevo ejercicio", command=mostrar_ejemplo)
btn_ejemplo.pack()

original_label = tk.Label(frame, text="", font=("Helvetica", 12), wraplength=500)
original_label.pack()

entrada = tk.Entry(frame, width=60)
entrada.pack(pady=5)

verificar_btn = tk.Button(frame, text="Verificar paráfrasis")
verificar_btn.pack()

resultado = tk.Label(frame, text="", font=("Helvetica", 12))
resultado.pack(pady=10)

root.mainloop()
