import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Lista de oraciones
adjetivo_absoluto = [
    "Libros, tiene miles.", "Amigos, conserva pocos.", "Ideas, le sobran.",
    "Problemas, ha enfrentado bastantes.", "Sueños, mantiene vivos muchos.",
    "Errores, cometió incontables.", "Recuerdos, le quedan pocos.", "Canciones, canta muchísimas.",
    "Fiestas, ha celebrado incontables.", "Anécdotas, ha contado graciosas."
] * 5

pronombre_retoma = [
    "Libros, los guarda con celo.", "Amigos, los valora muchísimo.",
    "Ideas, las organiza con cuidado.", "Problemas, los enfrenta con valentía.",
    "Recuerdos, los guarda en fotos.", "Sueños, los persigue sin cesar.",
    "Errores, los repasa para aprender.", "Fiestas, las organiza con esmero.",
    "Metas, las cumple con disciplina.", "Anécdotas, las cuenta con humor."
] * 5

puntos = 0
registro = []
estadisticas = {"Correctas": 0, "Incorrectas": 0}

# Funciones

def clasificar_oracion():
    global puntos
    oracion = entrada_oracion.get()
    eleccion = opcion_var.get()

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
        puntos += 1
        estadisticas["Correctas"] += 1
    else:
        resultado = "❌ Incorrecto."
        estadisticas["Incorrectas"] += 1

    resultado_var.set(f"{resultado} (Categoría: {categoria})")
    puntos_label.config(text=f"Puntuación: {puntos}")
    registro.append({"oracion": oracion, "usuario": eleccion, "real": categoria, "resultado": resultado})
    entrada_oracion.delete(0, tk.END)


def mostrar_ejemplos():
    ejemplos = "\n🔹 Adjetivo absoluto:\n" + "\n".join(random.sample(adjetivo_absoluto, 3)) + "\n\n"
    ejemplos += "🔸 Pronombre:\n" + "\n".join(random.sample(pronombre_retoma, 3))
    messagebox.showinfo("Ejemplos", ejemplos)


def guardar_registro():
    with open("registro_completo.txt", "w", encoding="utf-8") as f:
        f.write("Registro completo de oraciones\n\n")
        for r in registro:
            f.write(str(r) + "\n")


def mostrar_teoria():
    teoria = (
        "En español, es común anticipar un elemento de la oración para darle énfasis.\n"
        "Esto puede hacerse de dos formas:\n\n"
        "1. Usando un adjetivo absoluto: 'Libros, tiene muchos.'\n"
        "2. Repitiendo el sustantivo mediante un pronombre: 'Libros, los tiene todos.'\n"
    )
    messagebox.showinfo("Teoría", teoria)


def ver_grafico():
    fig = Figure(figsize=(4, 3))
    ax = fig.add_subplot(111)
    ax.bar(estadisticas.keys(), estadisticas.values(), color=["green", "red"])
    ax.set_title("Estadísticas de respuestas")
    ax.set_ylabel("Cantidad")

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()


def editar_respuesta():
    if not registro:
        messagebox.showinfo("Editar", "No hay respuestas que editar.")
        return
    indice = simpledialog.askinteger("Editar", f"Indica el número de la oración (1-{len(registro)}):")
    if indice and 1 <= indice <= len(registro):
        nueva = simpledialog.askstring("Nueva oración", "Escribe la nueva oración:")
        if nueva:
            registro[indice - 1]["oracion"] = nueva
            messagebox.showinfo("Actualizado", "La oración ha sido actualizada.")

# Interfaz
ventana = tk.Tk()
ventana.title("Anticipación Enfática - Ejercicio GUI")
ventana.geometry("550x600")

# Widgets

tk.Label(ventana, text="Escribe tu oración:", font=("Arial", 12)).pack(pady=5)
entrada_oracion = tk.Entry(ventana, width=70, font=("Arial", 11))
entrada_oracion.pack(pady=5)

opcion_var = tk.StringVar(value="1")
tk.Label(ventana, text="Selecciona la categoría:", font=("Arial", 12)).pack(pady=5)
tk.Radiobutton(ventana, text="Adjetivo absoluto", variable=opcion_var, value="1").pack()
tk.Radiobutton(ventana, text="Pronombre que retoma", variable=opcion_var, value="2").pack()

tk.Button(ventana, text="Clasificar oración", command=clasificar_oracion).pack(pady=5)
tk.Button(ventana, text="Mostrar teoría", command=mostrar_teoria).pack(pady=2)
tk.Button(ventana, text="Ver ejemplos", command=mostrar_ejemplos).pack(pady=2)
tk.Button(ventana, text="Ver estadísticas", command=ver_grafico).pack(pady=2)
tk.Button(ventana, text="Editar respuesta", command=editar_respuesta).pack(pady=2)

resultado_var = tk.StringVar()
tk.Label(ventana, textvariable=resultado_var, font=("Arial", 12), fg="blue").pack(pady=10)
puntos_label = tk.Label(ventana, text=f"Puntuación: {puntos}", font=("Arial", 12, "bold"))
puntos_label.pack()

# Al cerrar
ventana.protocol("WM_DELETE_WINDOW", lambda: (guardar_registro(), ventana.destroy()))
ventana.mainloop()
