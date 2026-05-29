import tkinter as tk
from tkinter import messagebox
import random

# Lista de oraciones
adjetivo_absoluto = [
    "Libros, tiene miles.", "Amigos, conserva pocos.", "Ideas, le sobran.",
    "Problemas, ha enfrentado bastantes.", "Sueños, mantiene vivos muchos.",
    "Errores, cometió incontables.", "Recuerdos, le quedan pocos.", "Canciones, canta muchísimas.",
    "Fiestas, ha celebrado incontables.", "Anécdotas, ha contado graciosas."
] * 5  # total 50

pronombre_retoma = [
    "Libros, los guarda con celo.", "Amigos, los valora muchísimo.",
    "Ideas, las organiza con cuidado.", "Problemas, los enfrenta con valentía.",
    "Recuerdos, los guarda en fotos.", "Sueños, los persigue sin cesar.",
    "Errores, los repasa para aprender.", "Fiestas, las organiza con esmero.",
    "Metas, las cumple con disciplina.", "Anécdotas, las cuenta con humor."
] * 5  # total 50

puntos = 0
registro = []

# Función para clasificar la oración
def clasificar_oracion():
    global puntos
    oracion = entrada_oracion.get()
    eleccion = opcion_var.get()
    resultado = ""
    categoria = ""

    if not oracion.strip():
        resultado_var.set("⚠️ Escribe una oración primero.")
        return

    if any(pron in oracion.lower() for pron in [" los ", " las ", " lo ", " la "]):
        categoria = "Pronombre"
        correcta = eleccion == "2"
    elif any(adj in oracion.lower() for adj in ["muchos", "pocos", "varios", "bastantes", "numerosas", "incontables"]):
        categoria = "Adjetivo"
        correcta = eleccion == "1"
    else:
        categoria = "No clara"
        correcta = False

    if correcta:
        resultado = "✔️ ¡Correcto!"
        puntos_label.config(text=f"Puntuación: {puntos + 1}")
        puntos_label.update()
        puntos_suma = 1
    else:
        resultado = "❌ Incorrecto."
        puntos_suma = 0

    registro.append(f"Oración: {oracion}\nClasificación usuario: {eleccion}\nReal: {categoria}\nResultado: {resultado}\n")
    resultado_var.set(f"{resultado} (Categoría: {categoria})")

    global puntos
    puntos += puntos_suma
    entrada_oracion.delete(0, tk.END)

# Función para ver ejemplos
def mostrar_ejemplos():
    ejemplos = "🔹 Adjetivo absoluto:\n"
    ejemplos += "\n".join(random.sample(adjetivo_absoluto, 3)) + "\n\n"
    ejemplos += "🔸 Pronombre:\n"
    ejemplos += "\n".join(random.sample(pronombre_retoma, 3))
    messagebox.showinfo("Ejemplos", ejemplos)

# Función para guardar el registro
def guardar_registro():
    with open("registro_tkinter.txt", "w", encoding="utf-8") as f:
        f.write("Registro de oraciones\n\n")
        for r in registro:
            f.write(r + "\n")
    print("Registro guardado.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio de Anticipación Enfática")
ventana.geometry("500x400")

# Widgets
tk.Label(ventana, text="Escribe tu oración:", font=("Arial", 12)).pack(pady=10)
entrada_oracion = tk.Entry(ventana, width=60, font=("Arial", 11))
entrada_oracion.pack()

tk.Label(ventana, text="Selecciona la categoría:", font=("Arial", 12)).pack(pady=5)
opcion_var = tk.StringVar(value="1")
tk.Radiobutton(ventana, text="Adjetivo absoluto", variable=opcion_var, value="1").pack()
tk.Radiobutton(ventana, text="Pronombre que retoma", variable=opcion_var, value="2").pack()

tk.Button(ventana, text="Clasificar oración", command=clasificar_oracion).pack(pady=10)
tk.Button(ventana, text="Ver ejemplos", command=mostrar_ejemplos).pack()

resultado_var = tk.StringVar()
tk.Label(ventana, textvariable=resultado_var, font=("Arial", 12), fg="blue").pack(pady=10)

puntos_label = tk.Label(ventana, text=f"Puntuación: {puntos}", font=("Arial", 12, "bold"))
puntos_label.pack()

# Cierre con guardado
def al_cerrar():
    guardar_registro()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", al_cerrar)
ventana.mainloop()
