import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random
import json

# Base de datos de ejemplos
ejemplos = [
    {"oracion": "Desayuno cereal todas las mañanas.", "categoria": "Presente habitual"},
    {"oracion": "Estoy leyendo un libro interesante.", "categoria": "Presente actual"},
    {"oracion": "Mañana compro los boletos del concierto.", "categoria": "Presente por futuro"},
    {"oracion": "El agua hierve a 100 grados Celsius.", "categoria": "Presente nómino"},
]

# Cargar frases personalizadas
def cargar_personales():
    try:
        with open("frases_personales.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guardar frases personalizadas
def guardar_personales(frases):
    with open("frases_personales.json", "w", encoding="utf-8") as file:
        json.dump(frases, file, indent=2, ensure_ascii=False)

# Funciones de las acciones
def mostrar_diapositiva():
    contenido = """\
TIPOS DE PRESENTE EN ESPAÑOL:

1. Presente habitual:
   - Ejemplo: "Desayuno cereal todas las mañanas."
   - Describe acciones que se repiten habitualmente.

2. Presente actual:
   - Ejemplo: "Estoy leyendo un libro interesante."
   - Describe acciones que ocurren en este momento.

3. Presente por futuro:
   - Ejemplo: "Mañana compro los boletos del concierto."
   - Usamos presente para referirnos al futuro cercano.

4. Presente nómino (general):
   - Ejemplo: "El agua hierve a 100 grados Celsius."
   - Enuncia hechos científicos o verdades universales.
"""
    messagebox.showinfo("📖 Diapositiva: El Presente", contenido)

def identificar_categoria():
    ejemplo = random.choice(ejemplos)
    respuesta = simpledialog.askstring("Categoría", f"¿A qué categoría pertenece esta oración?\n\n{ejemplo['oracion']}")
    if respuesta:
        if respuesta.lower() in ejemplo['categoria'].lower():
            messagebox.showinfo("✅ Correcto", "¡Respuesta correcta!")
        else:
            messagebox.showerror("❌ Incorrecto", f"La respuesta correcta era: {ejemplo['categoria']}.")

def reescribir_oracion():
    ejemplo = random.choice(ejemplos)
    nueva_version = simpledialog.askstring("Reescritura", f"Reescribe esta oración en otro tiempo verbal:\n\n{ejemplo['oracion']}")
    if nueva_version:
        messagebox.showinfo("📝 Nueva versión", f"Tu nueva oración:\n{nueva_version}")

def crear_frase(frases_personales):
    if len(frases_personales) >= 100:
        messagebox.showwarning("⚠️ Límite alcanzado", "Ya tienes 100 frases guardadas.")
        return
    oracion = simpledialog.askstring("Crear nueva frase", "Escribe tu nueva oración:")
    if not oracion:
        return
    categoria = simpledialog.askstring("Categoría", "¿Qué categoría tiene? (Presente habitual / actual / por futuro / nómino):")
    if not categoria:
        return
    frases_personales.append({"oracion": oracion, "categoria": categoria})
    guardar_personales(frases_personales)
    messagebox.showinfo("✅ Guardado", "Tu frase fue guardada correctamente.")

def ver_frases(frases_personales):
    ventana = tk.Toplevel(root)
    ventana.title("📚 Tus frases guardadas")
    texto = scrolledtext.ScrolledText(ventana, width=60, height=20)
    texto.pack(padx=10, pady=10)
    if not frases_personales:
        texto.insert(tk.END, "No tienes frases guardadas aún.")
    else:
        for idx, frase in enumerate(frases_personales, 1):
            texto.insert(tk.END, f"{idx}. {frase['oracion']} ({frase['categoria']})\n")
    texto.config(state='disabled')

# Configuración de la ventana principal
root = tk.Tk()
root.title("📖 Estudio del Presente en Español")

# Botones principales
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Button(frame, text="📚 Ver diapositiva del presente", command=mostrar_diapositiva, width=30).grid(row=0, column=0, pady=5)
tk.Button(frame, text="🎯 Identificar categoría", command=identificar_categoria, width=30).grid(row=1, column=0, pady=5)
tk.Button(frame, text="✏️ Reescribir oración", command=reescribir_oracion, width=30).grid(row=2, column=0, pady=5)

frases_personales = cargar_personales()
tk.Button(frame, text="🆕 Crear nueva frase", command=lambda: crear_frase(frases_personales), width=30).grid(row=3, column=0, pady=5)
tk.Button(frame, text="👀 Ver frases guardadas", command=lambda: ver_frases(frases_personales), width=30).grid(row=4, column=0, pady=5)
tk.Button(frame, text="🚪 Salir", command=root.quit, width=30).grid(row=5, column=0, pady=10)

root.mainloop()
