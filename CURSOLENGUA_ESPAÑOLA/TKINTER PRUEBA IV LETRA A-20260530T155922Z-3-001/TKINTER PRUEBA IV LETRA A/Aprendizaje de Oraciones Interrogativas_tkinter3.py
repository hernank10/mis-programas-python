import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

# Ruta para guardar los ejemplos
ARCHIVO_EJEMPLOS = "ejemplos_interrogativas.json"

# Categorías de oraciones interrogativas
categorias = {
    "directa_simple": "Oración interrogativa directa simple",
    "directa_compuesta": "Oración interrogativa directa compuesta",
    "indirecta": "Oración interrogativa indirecta",
    "dubitativa": "Oración dubitativa",
    "enfatica": "Oración interrogativa enfática"
}

# Teoría de oraciones interrogativas
teoria = {
    "directa_simple": "Las oraciones interrogativas directas simples expresan una pregunta de manera directa y con un solo verbo: ¿Vienes? ¿Te gusta?",
    "directa_compuesta": "Contienen más de un verbo o proposición: ¿Qué piensas que ocurrirá si no llega?",
    "indirecta": "No usan signos de interrogación, están subordinadas a otro verbo: Me pregunto si vendrás.",
    "dubitativa": "Expresan duda o posibilidad: No sé si vendrá. Dudamos que diga la verdad.",
    "enfatica": "Tienen carga emocional o énfasis: ¿¡Cómo pudiste hacer eso!?"
}

# Cargar ejemplos desde JSON
if os.path.exists(ARCHIVO_EJEMPLOS):
    with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
        ejemplos_guardados = json.load(f)
else:
    ejemplos_guardados = []

# Guardar ejemplos
def guardar_ejemplos():
    with open(ARCHIVO_EJEMPLOS, "w", encoding="utf-8") as f:
        json.dump(ejemplos_guardados, f, ensure_ascii=False, indent=4)

# Mostrar teoría
def mostrar_teoria():
    ventana = tk.Toplevel(root)
    ventana.title("Teoría de las Oraciones Interrogativas")
    for clave, descripcion in teoria.items():
        ttk.Label(ventana, text=f"{categorias[clave]}:", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=2)
        ttk.Label(ventana, text=descripcion, wraplength=500).pack(anchor="w", padx=20)

# Cuestionario interactivo con retroalimentación
def cuestionario_interactivo():
    ejemplo = random.choice(ejemplos_guardados)
    def verificar():
        seleccion = combo.get()
        correcta = categorias[ejemplo['categoria']]
        if seleccion == correcta:
            messagebox.showinfo("¡Correcto!", f"¡Bien hecho! {correcta}")
        else:
            messagebox.showerror("Incorrecto", f"La categoría correcta es: {correcta}")

    ventana = tk.Toplevel(root)
    ventana.title("Cuestionario Interactivo")
    ttk.Label(ventana, text=ejemplo['oracion'], font=("Arial", 12)).pack(pady=10)
    combo = ttk.Combobox(ventana, values=list(categorias.values()), state="readonly")
    combo.pack()
    ttk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)

# Crear y guardar nuevo ejemplo
def crear_ejemplo():
    def guardar():
        oracion = entrada.get()
        cat = seleccion.get()
        if oracion and cat:
            ejemplos_guardados.append({"oracion": oracion, "categoria": cat})
            guardar_ejemplos()
            top.destroy()
        else:
            messagebox.showerror("Error", "Completa todos los campos")

    top = tk.Toplevel(root)
    top.title("Nuevo ejemplo")
    ttk.Label(top, text="Oración:").pack()
    entrada = ttk.Entry(top, width=50)
    entrada.pack(pady=5)
    seleccion = ttk.Combobox(top, values=list(categorias.keys()), state="readonly")
    seleccion.pack()
    ttk.Button(top, text="Guardar", command=guardar).pack(pady=5)

# Ver ejemplos guardados
def ver_ejemplos():
    ventana = tk.Toplevel(root)
    ventana.title("Ejemplos Guardados")
    for ej in ejemplos_guardados:
        ttk.Label(ventana, text=f"{ej['oracion']} ({categorias[ej['categoria']]})").pack(anchor="w")

# Interfaz principal
root = tk.Tk()
root.title("Práctica de Oraciones Interrogativas")
root.geometry("600x500")

# Botones
ttk.Button(root, text="📘 Ver teoría", command=mostrar_teoria).pack(pady=5)
ttk.Button(root, text="🧠 Cuestionario interactivo", command=cuestionario_interactivo).pack(pady=5)
ttk.Button(root, text="📝 Crear nuevo ejemplo", command=crear_ejemplo).pack(pady=5)
ttk.Button(root, text="📚 Ver ejemplos guardados", command=ver_ejemplos).pack(pady=5)

root.mainloop()
