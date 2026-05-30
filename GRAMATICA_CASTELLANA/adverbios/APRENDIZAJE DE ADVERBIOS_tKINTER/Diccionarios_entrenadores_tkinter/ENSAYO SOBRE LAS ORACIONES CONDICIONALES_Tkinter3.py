import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Archivo donde se guardan los ejemplos
ARCHIVO_EJEMPLOS = "ejemplos_condicionales.json"
MAX_EJEMPLOS = 100

# Ensayo educativo
ENSAYO = """
Las oraciones condicionales son construcciones gramaticales que expresan una relación de causa y efecto entre dos ideas:
una proposición condicional (la condición) y una proposición principal (el resultado).
Estas estructuras permiten hablar de posibilidades reales, irreales o hipotéticas, dependiendo del contexto verbal.
Dominar su uso fortalece la expresión escrita y oral, y mejora la comprensión lectora en textos argumentativos y expositivos.
"""

# Cargar ejemplos existentes o usar algunos por defecto
def cargar_ejemplos():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return [
            {"incompleta": "Si llueve mañana,", "respuesta": "nos quedaremos en casa.", "tipo": "Real"},
            {"incompleta": "Si yo fuera rico,", "respuesta": "viajaría por el mundo.", "tipo": "Irreal"},
        ]

# Guardar los ejemplos
def guardar_ejemplos():
    with open(ARCHIVO_EJEMPLOS, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, ensure_ascii=False, indent=2)

# Mostrar el ensayo
def mostrar_ensayo():
    ensayo_window = tk.Toplevel(root)
    ensayo_window.title("Ensayo educativo")
    tk.Label(ensayo_window, text=ENSAYO, wraplength=500, justify="left").pack(padx=10, pady=10)

# Añadir un nuevo ejemplo
def añadir_ejemplo():
    if len(ejemplos) >= MAX_EJEMPLOS:
        messagebox.showwarning("Límite alcanzado", "Ya tienes 100 ejemplos guardados.")
        return

    inc = simpledialog.askstring("Nueva oración", "Escribe la oración incompleta:")
    if not inc:
        return
    res = simpledialog.askstring("Respuesta", "Escribe la continuación o respuesta:")
    if not res:
        return
    tipo = simpledialog.askstring("Tipo", "¿Qué tipo es? (Real / Irreal / Potencial):")
    if not tipo:
        return

    ejemplos.append({"incompleta": inc, "respuesta": res, "tipo": tipo})
    guardar_ejemplos()
    messagebox.showinfo("Guardado", "Ejemplo guardado con éxito.")

# Ver ejemplos guardados
def ver_ejemplos():
    ver_window = tk.Toplevel(root)
    ver_window.title("Ejemplos guardados")
    texto = tk.Text(ver_window, wrap="word")
    texto.pack(padx=10, pady=10)
    for i, ej in enumerate(ejemplos, 1):
        texto.insert("end", f"{i}. {ej['incompleta']} {ej['respuesta']} ({ej['tipo']})\n\n")
    texto.config(state="disabled")

# Practicar con un ejemplo
def practicar():
    global indice
    if not ejemplos:
        messagebox.showinfo("Sin ejemplos", "No hay ejemplos para practicar.")
        return

    ejemplo = ejemplos[indice]
    oracion_label.config(text=f"{ejemplo['incompleta']} ___________")
    tipo_label.config(text=f"Tipo: {ejemplo['tipo']}")
    entrada.delete(0, tk.END)

def verificar():
    respuesta_usuario = entrada.get().strip().lower()
    respuesta_correcta = ejemplos[indice]["respuesta"].strip().lower()

    if respuesta_usuario == respuesta_correcta:
        messagebox.showinfo("¡Correcto!", "¡Muy bien! Escribiste correctamente la oración.")
    else:
        messagebox.showwarning("Incorrecto", f"La respuesta correcta era:\n{ejemplos[indice]['respuesta']}")

    avanzar()

def avanzar():
    global indice
    indice = (indice + 1) % len(ejemplos)
    practicar()

# Inicializar programa
ejemplos = cargar_ejemplos()
indice = 0

# Interfaz Tkinter
root = tk.Tk()
root.title("Práctica de oraciones condicionales")

oracion_label = tk.Label(root, text="", font=("Arial", 14))
oracion_label.pack(pady=10)

tipo_label = tk.Label(root, text="", font=("Arial", 10))
tipo_label.pack()

entrada = tk.Entry(root, width=60)
entrada.pack(pady=10)

boton_verificar = tk.Button(root, text="Verificar", command=verificar)
boton_verificar.pack()

boton_ensayo = tk.Button(root, text="📘 Leer ensayo", command=mostrar_ensayo)
boton_ensayo.pack(pady=5)

boton_añadir = tk.Button(root, text="➕ Añadir ejemplo", command=añadir_ejemplo)
boton_añadir.pack(pady=5)

boton_ver = tk.Button(root, text="📂 Ver ejemplos guardados", command=ver_ejemplos)
boton_ver.pack(pady=5)

# Iniciar práctica
practicar()

root.mainloop()
