import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Diccionario de frases por categoría con errores y correcciones
ejercicios_por_categoria = {
    "1": [("El doctor, llegó tarde.", "El doctor llegó tarde."),
           ("Mi hermano, compró pan.", "Mi hermano compró pan.")],
    "2": [("A los estudiantes del curso, la profesora les explicó el tema.", "A los estudiantes del curso la profesora les explicó el tema.")],
    "3": [("El perro, ladra muy fuerte.", "El perro ladra muy fuerte.")]
}

progreso_usuario = {
    "total_intentos": 0,
    "respuestas_correctas": 0,
    "medallas": 0
}

# Teoría por categoría
def mostrar_diapositiva_teorica(categoria):
    if categoria == "1":
        return ("Categoría 1: Frases con estructura esencial (sin coma)",
                "No se deben separar con coma los elementos esenciales de una oración: sujeto, verbo y complementos.\nEjemplo incorrecto: El doctor, llegó tarde.\nCorrección: El doctor llegó tarde.")
    elif categoria == "2":
        return ("Categoría 2: Cambio de orden (sin coma)",
                "Aunque se cambie el orden, los elementos esenciales no deben separarse con comas.\nEjemplo incorrecto: A los estudiantes del curso, la profesora les explicó el tema.\nCorrección: A los estudiantes del curso la profesora les explicó el tema.")
    elif categoria == "3":
        return ("Categoría 3: Evitar separar sujeto y verbo con coma",
                "Nunca se debe colocar una coma entre el sujeto y el verbo.\nEjemplo incorrecto: El perro, ladra muy fuerte.\nCorrección: El perro ladra muy fuerte.")

# Función para corregir frases
def corregir_frases(categoria):
    ejercicios = ejercicios_por_categoria.get(categoria, [])
    if not ejercicios:
        messagebox.showinfo("Sin ejercicios", "No hay ejercicios disponibles en esta categoría.")
        return

    titulo, teoria = mostrar_diapositiva_teorica(categoria)
    messagebox.showinfo(titulo, teoria)
    random.shuffle(ejercicios)

    for incorrecta, correcta in ejercicios:
        respuesta = simpledialog.askstring("Corrige la frase", f"Frase incorrecta:\n{incorrecta}\n\nEscribe la versión correcta:")
        if respuesta is None:
            break

        progreso_usuario["total_intentos"] += 1

        if respuesta.strip().lower() == correcta.lower():
            messagebox.showinfo("¡Correcto!", "✅ ¡Muy bien!")
            progreso_usuario["respuestas_correctas"] += 1
        else:
            messagebox.showerror("Incorrecto", f"❌ La respuesta correcta era:\n{correcta}")

    actualizar_medallas()

# Sistema de medallas
def actualizar_medallas():
    aciertos = progreso_usuario["respuestas_correctas"]
    progreso_usuario["medallas"] = aciertos // 10

# Añadir nuevos ejemplos
def agregar_ejemplo():
    categoria = simpledialog.askstring("Categoría", "Escribe la categoría (1, 2, 3):")
    if categoria not in ejercicios_por_categoria:
        messagebox.showerror("Error", "Categoría inválida.")
        return

    for _ in range(100):
        incorrecta = simpledialog.askstring("Nueva frase", "Escribe frase incorrecta:")
        if incorrecta is None:
            break
        correcta = simpledialog.askstring("Frase correcta", "Escribe la corrección:")
        if correcta is None:
            break
        ejercicios_por_categoria[categoria].append((incorrecta.strip(), correcta.strip()))
        continuar = messagebox.askyesno("¿Continuar?", "¿Deseas agregar otro ejemplo?")
        if not continuar:
            break

# Mostrar progreso
def mostrar_progreso():
    messagebox.showinfo("Progreso",
                        f"Intentos totales: {progreso_usuario['total_intentos']}\n"
                        f"Respuestas correctas: {progreso_usuario['respuestas_correctas']}\n"
                        f"Medallas 🏅: {progreso_usuario['medallas']}")

# Menú principal con botones
def menu_principal():
    root = tk.Tk()
    root.title("Frases sin coma - Práctica interactiva")
    root.geometry("500x400")

    tk.Label(root, text="📝 MENÚ PRINCIPAL", font=("Helvetica", 16, "bold")).pack(pady=10)

    botones = [
        ("Frases con estructura esencial (sin coma)", lambda: corregir_frases("1")),
        ("Cambio de orden (sin coma)", lambda: corregir_frases("2")),
        ("Evitar separar sujeto y verbo con coma", lambda: corregir_frases("3")),
        ("Agregar nuevos ejemplos (hasta 100)", agregar_ejemplo),
        ("Ver progreso y medallas 🏅", mostrar_progreso),
        ("Salir", root.quit)
    ]

    for texto, comando in botones:
        tk.Button(root, text=texto, command=comando, font=("Helvetica", 12), width=40, pady=5).pack(pady=5)

    root.mainloop()

# Ejecutar la app
menu_principal()
