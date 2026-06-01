import tkinter as tk
from tkinter import messagebox

# -------------------------------
# 🧠 Datos base
# -------------------------------

tesis_lista = [
    "Las tareas escolares deben tener un propósito claro",
    "El reciclaje debe enseñarse desde primaria",
    "La lectura diaria mejora el desempeño escolar",
    "Los teléfonos en clase deben estar regulados",
    "Los videojuegos pueden ser positivos",
    "La puntualidad debe enseñarse como valor escolar",
    "Las excursiones educativas son valiosas",
    "La alimentación saludable debe ser promovida",
    "El arte urbano merece reconocimiento",
    "El descanso entre clases es necesario",
    "Los estudiantes deben respetar a sus compañeros",
    "La historia es una materia clave en la educación",
    "El deporte debe formar parte del horario escolar",
    "La escritura mejora el pensamiento crítico",
    "Los estudiantes deben aprender sobre economía básica",
    "La música estimula la memoria y la concentración",
    "Los profesores deben recibir apoyo emocional",
    "Las actividades en grupo ayudan al aprendizaje",
    "El bullying debe tratarse con firmeza",
    "La tecnología debe usarse con responsabilidad"
]

elogios = [
    "✅ ¡Razón clara y lógica!",
    "🎯 ¡Tu tesis tiene fuerza!",
    "🌟 ¡Excelente justificación!",
    "👏 ¡Buena conexión entre postura y argumento!",
    "🧠 ¡Pensamiento argumentativo sólido!"
]

# -------------------------------
# ⚙️ Evaluación de respuestas
# -------------------------------

def evaluar_respuesta(razon):
    razon = razon.strip().lower()
    puntos = 0
    conectores = ["porque", "ya que", "debido a"]
    if any(c in razon for c in conectores):
        puntos += 1
    if len(razon.split()) >= 5:
        puntos += 1
    if "." in razon or "," in razon:
        puntos += 1
    return puntos

# -------------------------------
# 🎮 Funcionalidades de interfaz
# -------------------------------

def mostrar_teoria():
    texto = (
        "📘 LECCIÓN 7 – ¿CÓMO PRESENTAMOS UNA TESIS Y LA SOSTENEMOS?\n\n"
        "Una tesis es una afirmación clara sobre un tema. Debe ir acompañada de una razón principal que la justifique.\n\n"
        "Estructura recomendada:\nTesis + conector + razón\n\n"
        "Conectores comunes:\n- porque\n- ya que\n- debido a\n\n"
        "Ejemplo:\nToda escuela debería tener biblioteca, porque fomenta la lectura y el pensamiento independiente."
    )
    messagebox.showinfo("Teoría", texto)

def evaluar_y_mostrar():
    idx = selector.get()
    if idx == "":
        messagebox.showwarning("Aviso", "Selecciona un número de ejercicio.")
        return
    idx = int(idx)
    tesis = tesis_lista[idx - 1]
    razon = entrada.get("1.0", tk.END).strip()
    puntos = evaluar_respuesta(razon)

    if puntos == 3:
        comentario = "🏅 ¡Argumento sólido, bien estructurado!"
    elif puntos == 2:
        comentario = "✅ ¡Buena razón, podrías agregar más detalle!"
    elif puntos == 1:
        comentario = "⚠️ Tu razón tiene potencial, pero le falta estructura."
    else:
        comentario = "❌ Falta conexión lógica o desarrollo en la respuesta."

    resultado.set(f"Tesis: {tesis}\nRazón: {razon}\n\n{comentario}\nPuntaje: {puntos}/3")

# -------------------------------
# 🖼️ Interfaz principal
# -------------------------------

root = tk.Tk()
root.title("Sintaxis Quest EDU – 9.º Grado – Lección 7")
root.geometry("750x600")

tk.Label(root, text="🧠 Lección 7: Tesis + Razón Argumentativa", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="📘 Ver teoría", command=mostrar_teoria).pack(pady=5)

frame_selector = tk.Frame(root)
frame_selector.pack()

tk.Label(frame_selector, text="Selecciona ejercicio (1–20):").pack(side=tk.LEFT, padx=5)
selector = tk.StringVar()
opciones = [str(i+1) for i in range(20)]
menu = tk.OptionMenu(frame_selector, selector, *opciones)
menu.pack(side=tk.LEFT)

tk.Label(root, text="✍️ Escribe tu razón aquí:", font=("Arial", 12)).pack(pady=8)
entrada = tk.Text(root, height=4, width=80)
entrada.pack()

tk.Button(root, text="🧠 Evaluar respuesta", command=evaluar_y_mostrar).pack(pady=10)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado, font=("Arial", 11), wraplength=700, justify="left").pack(pady=10)

tk.Label(root, text="✨ ¡No olvides usar conectores como 'porque', 'ya que' o 'debido a' para enriquecer tu argumento!", fg="blue", font=("Arial", 10, "italic")).pack(pady=5)

root.mainloop()
