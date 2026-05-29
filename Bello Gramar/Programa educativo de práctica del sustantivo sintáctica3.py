import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Datos base
ejemplos = [
    ("El niño travieso juega en el parque.", "adjetivo"),
    ("La ciudad antigua guarda muchos secretos.", "adjetivo"),
    ("La dama elegante caminaba por el salón.", "adjetivo"),
    ("La sin par Dulcinea", "complemento"),
    ("Las orillas del Maipo estaban cubiertas de flores.", "complemento"),
    ("El cuadro de Goya se exhibe en el museo.", "complemento"),
    ("Aquel gran bulto que allí se ve", "proposición"),
    ("La persona a quien vimos ayer en el paseo", "proposición"),
    ("La campiña por donde transitábamos", "proposición")
]

oraciones_usuario = []

# Ventana principal
root = tk.Tk()
root.title("Juego de Sintaxis")
root.geometry("600x400")

text_area = tk.Text(root, wrap="word", height=10)
text_area.pack(pady=10)

# Funciones

def mostrar_diapositiva():
    text_area.delete(1.0, tk.END)
    resumen = (
        "\n📘 Diapositiva: Tipos de modificación del sustantivo\n\n"
        "1️⃣ Por adjetivos:\n"
        "- El niño travieso juega en el parque.\n"
        "- La ciudad antigua guarda muchos secretos.\n\n"
        "2️⃣ Por complementos:\n"
        "- Las orillas del Maipo estaban cubiertas de flores.\n"
        "- La sin par Dulcinea\n\n"
        "3️⃣ Por proposiciones:\n"
        "- La persona a quien vimos ayer en el paseo.\n"
        "- La campiña por donde transitábamos.\n"
    )
    text_area.insert(tk.END, resumen)

def ver_oraciones():
    text_area.delete(1.0, tk.END)
    if not oraciones_usuario:
        text_area.insert(tk.END, "📂 Aún no has creado oraciones.")
    else:
        text_area.insert(tk.END, "📂 Tus oraciones creadas:\n\n")
        for i, oracion in enumerate(oraciones_usuario, 1):
            text_area.insert(tk.END, f"{i}. {oracion}\n")

def cuestionario_completar():
    base = [
        ("El ______ valiente salvó al niño.", "perro"),
        ("La casa ______ está en venta.", "grande"),
        ("El camino por donde ______ era angosto.", "veníamos")
    ]
    pregunta, respuesta = random.choice(base)
    user = simpledialog.askstring("Completa", f"✏️ Completa la oración: {pregunta}")
    if user:
        if user.strip().lower() == respuesta.lower():
            messagebox.showinfo("Resultado", "✅ ¡Correcto!")
        else:
            messagebox.showerror("Resultado", f"❌ Incorrecto. La respuesta era: {respuesta}")

def cuestionario_opcion_multiple():
    oracion, correcta = random.choice(ejemplos)
    opciones = ["adjetivo", "complemento", "proposición"]
    random.shuffle(opciones)

    seleccion = simpledialog.askinteger(
        "Opción múltiple",
        f"📝 {oracion}\n\n1. {opciones[0]}\n2. {opciones[1]}\n3. {opciones[2]}\n\nElige 1, 2 o 3:"
    )
    if seleccion in [1, 2, 3]:
        if opciones[seleccion - 1] == correcta:
            messagebox.showinfo("Resultado", "✅ ¡Correcto!")
        else:
            messagebox.showerror("Resultado", f"❌ Era: {correcta}")

def practicar():
    oracion, tipo = random.choice(ejemplos)
    clasificacion = simpledialog.askstring("Clasifica", f"🔸 Oración: {oracion}\n👉 Tipo de modificación (adjetivo / complemento / proposición):")
    if clasificacion:
        if clasificacion.strip().lower() == tipo:
            messagebox.showinfo("Resultado", "✅ ¡Correcto!")
        else:
            messagebox.showerror("Resultado", f"❌ La respuesta correcta es: {tipo}")

    nueva = simpledialog.askstring("Reescribe", "✍️ Reescribe esta oración cambiando el modificador:")
    if nueva:
        oraciones_usuario.append(nueva)

    or1 = simpledialog.askstring("Crear", "Crea una oración con adjetivo:")
    or2 = simpledialog.askstring("Crear", "Crea una oración con complemento:")
    or3 = simpledialog.askstring("Crear", "Crea una oración con proposición:")
    for oracion in [or1, or2, or3]:
        if oracion:
            oraciones_usuario.append(oracion)

# Botones
botones = [
    ("1. Practicar", practicar),
    ("2. Ver diapositiva", mostrar_diapositiva),
    ("3. Ver mis oraciones", ver_oraciones),
    ("4. Completar oración", cuestionario_completar),
    ("5. Opción múltiple", cuestionario_opcion_multiple),
    ("6. Salir", root.quit)
]

for texto, comando in botones:
    b = tk.Button(root, text=texto, width=30, command=comando)
    b.pack(pady=2)

root.mainloop()
