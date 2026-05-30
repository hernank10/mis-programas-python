import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random
import json

# Frases de ejemplo
frases = [
    {"texto": "Hernán Cortés llega a Tenochtitlán en 1519.", "categoria": "Presente Histórico"},
    {"texto": "Ayer terminé de leer un libro fascinante.", "categoria": "Pasado"},
    {"texto": "Mañana presentaré mi proyecto en la escuela.", "categoria": "Futuro"},
    {"texto": "Cristóbal Colón zarpa hacia América en 1492.", "categoria": "Presente Histórico"},
    {"texto": "Mis padres celebrarán su aniversario de bodas.", "categoria": "Futuro"},
    {"texto": "El mes pasado visitamos las ruinas de Machu Picchu.", "categoria": "Pasado"},
]

# Función para cambiar tiempo verbal (simplificada)
def cambiar_tiempo(frase, categoria):
    if categoria == "Pasado":
        return frase.replace("ó", "a").replace("ió", "e")
    elif categoria == "Futuro":
        return frase.replace("é", "o")
    elif categoria == "Presente Histórico":
        return frase.replace("a", "ó")
    else:
        return frase

# Mostrar conceptos y ejemplos
def mostrar_conceptos():
    conceptos = """
=== Conceptos: Presente Histórico ===

El presente histórico se usa para narrar hechos pasados como si estuvieran ocurriendo ahora,
dándole más vida y cercanía al relato.

Ejemplos:
- México obtiene su independencia en 1821, aunque la guerra comienza en 1810.
- Hernán Cortés llega a Tenochtitlán en 1519.
- Cristóbal Colón zarpa hacia América en 1492.

Uso:
- En biografías, historias, anécdotas.
- Para hacer más vívidas narraciones del pasado.

=== Recuerda: ===
Pasado = acciones que ya ocurrieron.
Futuro = acciones que ocurrirán después.
Presente Histórico = hechos pasados contados como si sucedieran ahora.
    """
    messagebox.showinfo("Conceptos y Ejemplos", conceptos)

# Función para practicar frases
def practicar_frases():
    frase = random.choice(frases)
    respuesta = simpledialog.askstring("Categoría", f"Frase:\n{frase['texto']}\n\n¿Qué categoría crees que es? (Presente Histórico, Pasado, Futuro)")
    if respuesta:
        if respuesta.lower() == frase["categoria"].lower():
            messagebox.showinfo("Resultado", "✅ ¡Correcto!")
        else:
            messagebox.showerror("Resultado", f"❌ Incorrecto. Era: {frase['categoria']}")

        cambiar = messagebox.askyesno("Cambio de tiempo", "¿Deseas cambiar el tiempo verbal de esta frase?")
        if cambiar:
            nueva = cambiar_tiempo(frase["texto"], frase["categoria"])
            messagebox.showinfo("Frase Modificada", f"Frase con tiempo cambiado:\n{nueva}")

# Función para agregar nueva frase
def agregar_frase():
    if len(frases) >= 100:
        messagebox.showwarning("Límite", "Ya tienes 100 frases registradas.")
        return
    texto = simpledialog.askstring("Nueva Frase", "Escribe tu nueva frase:")
    if texto:
        categoria = simpledialog.askstring("Categoría", "¿Qué categoría es? (Presente Histórico, Pasado, Futuro)")
        if categoria:
            frases.append({"texto": texto, "categoria": categoria})
            messagebox.showinfo("Guardado", "Frase agregada exitosamente.")

# Función para ver todas las frases
def ver_frases():
    ventana = tk.Toplevel(root)
    ventana.title("Todas las Frases")
    text_area = scrolledtext.ScrolledText(ventana, width=70, height=20)
    text_area.pack(padx=10, pady=10)

    for i, frase in enumerate(frases, start=1):
        text_area.insert(tk.END, f"{i}. {frase['texto']} ({frase['categoria']})\n")

# Función para guardar frases
def guardar_frases():
    with open("mis_frases.json", "w", encoding="utf-8") as f:
        json.dump(frases, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("Guardado", "Frases guardadas en 'mis_frases.json'.")

# Crear la ventana principal
root = tk.Tk()
root.title("Práctica de Presente Histórico, Pasado y Futuro")
root.geometry("500x400")

# Crear botones
btn_conceptos = tk.Button(root, text="📚 Ver Conceptos y Ejemplos", command=mostrar_conceptos, width=40, height=2)
btn_practicar = tk.Button(root, text="📝 Practicar Identificación", command=practicar_frases, width=40, height=2)
btn_agregar = tk.Button(root, text="➕ Agregar Nueva Frase", command=agregar_frase, width=40, height=2)
btn_ver = tk.Button(root, text="👀 Ver Todas las Frases", command=ver_frases, width=40, height=2)
btn_guardar = tk.Button(root, text="💾 Guardar Frases", command=guardar_frases, width=40, height=2)
btn_salir = tk.Button(root, text="🚪 Salir", command=root.quit, width=40, height=2)

# Organizar los botones
btn_conceptos.pack(pady=5)
btn_practicar.pack(pady=5)
btn_agregar.pack(pady=5)
btn_ver.pack(pady=5)
btn_guardar.pack(pady=5)
btn_salir.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
