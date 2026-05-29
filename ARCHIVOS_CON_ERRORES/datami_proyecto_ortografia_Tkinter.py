# practica_ortografia_tkinter.py
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

EJEMPLOS_FILE = "ejemplos.json"
PROGRESO_FILE = "progreso.json"

# --------------------------- Datos base ---------------------------
def cargar_ejemplos():
    if os.path.exists(EJEMPLOS_FILE):
        with open(EJEMPLOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_ejemplos(data):
    with open(EJEMPLOS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def cargar_progreso():
    if os.path.exists(PROGRESO_FILE):
        with open(PROGRESO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_progreso(data):
    with open(PROGRESO_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --------------------------- Funciones ---------------------------
def practicar_por_tema(tema):
    ejemplos = [e for e in cargar_ejemplos() if e["tema"] == tema]
    if not ejemplos:
        messagebox.showinfo("Sin ejemplos", f"No hay ejemplos para el tema: {tema}")
        return

    progreso = cargar_progreso()
    correctos = 0

    for ejemplo in ejemplos:
        entrada = simpledialog.askstring(
            "Práctica",
            f"Escribe correctamente esta palabra según la AFI:
{ejemplo['afi']}
(Regla: {ejemplo['regla']})"
        )
        if entrada and entrada.lower().strip() == ejemplo['palabra'].lower():
            messagebox.showinfo("Correcto!", "¡Muy bien!")
            ejemplo_id = ejemplo['palabra']
            progreso[ejemplo_id] = progreso.get(ejemplo_id, {"aciertos": 0, "fallos": 0})
            progreso[ejemplo_id]["aciertos"] += 1
            correctos += 1
        else:
            messagebox.showerror("Incorrecto", f"Respuesta correcta: {ejemplo['palabra']}")
            ejemplo_id = ejemplo['palabra']
            progreso[ejemplo_id] = progreso.get(ejemplo_id, {"aciertos": 0, "fallos": 0})
            progreso[ejemplo_id]["fallos"] += 1

    guardar_progreso(progreso)
    messagebox.showinfo("Resultado", f"Ejercicios correctos: {correctos}/{len(ejemplos)}")

def agregar_ejemplo():
    palabra = simpledialog.askstring("Nueva palabra", "Palabra correcta:")
    if not palabra:
        return
    afi = simpledialog.askstring("AFI", f"Transcripción AFI de '{palabra}':")
    regla = simpledialog.askstring("Regla ortográfica", f"Regla que aplica a '{palabra}':")
    tema = simpledialog.askstring("Tema ortográfico", "Tema general (b/v, qu/c, etc.):")
    ejemplos = cargar_ejemplos()
    ejemplos.append({"palabra": palabra, "afi": afi, "regla": regla, "tema": tema})
    guardar_ejemplos(ejemplos)
    messagebox.showinfo("Guardado", "Ejemplo guardado exitosamente.")

def ver_ejemplos():
    ejemplos = cargar_ejemplos()
    texto = "\n".join([f"{e['palabra']} ({e['afi']}) - {e['regla']} [{e['tema']}]" for e in ejemplos])
    messagebox.showinfo("Ejemplos guardados", texto or "No hay ejemplos aún.")

def ver_progreso():
    progreso = cargar_progreso()
    texto = ""
    for palabra, datos in progreso.items():
        total = datos["aciertos"] + datos["fallos"]
        aciertos = datos["aciertos"]
        porcentaje = (aciertos / total) * 100 if total > 0 else 0
        texto += f"{palabra}: {aciertos}/{total} aciertos ({porcentaje:.0f}%)\n"
    messagebox.showinfo("Progreso", texto or "Sin progreso registrado aún.")

# --------------------------- Interfaz Tkinter ---------------------------
ventana = tk.Tk()
ventana.title("Práctica Ortográfica Interactiva")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Selecciona una opción:", font=("Arial", 14))
etiqueta.pack(pady=10)

btn_bv = tk.Button(ventana, text="Practicar B/V", command=lambda: practicar_por_tema("b/v"))
btn_bv.pack(pady=5)
btn_quc = tk.Button(ventana, text="Practicar QU/C/K", command=lambda: practicar_por_tema("qu/c/k"))
btn_quc.pack(pady=5)
btn_zcs = tk.Button(ventana, text="Practicar Z/C/S", command=lambda: practicar_por_tema("z/c/s"))
btn_zcs.pack(pady=5)
btn_gyj = tk.Button(ventana, text="Practicar G/J", command=lambda: practicar_por_tema("g/j"))
btn_gyj.pack(pady=5)

btn_nuevo = tk.Button(ventana, text="Agregar nuevo ejemplo", command=agregar_ejemplo)
btn_nuevo.pack(pady=5)
btn_ver = tk.Button(ventana, text="Ver ejemplos", command=ver_ejemplos)
btn_ver.pack(pady=5)
btn_progreso = tk.Button(ventana, text="Ver progreso", command=ver_progreso)
btn_progreso.pack(pady=5)

ventana.mainloop()
