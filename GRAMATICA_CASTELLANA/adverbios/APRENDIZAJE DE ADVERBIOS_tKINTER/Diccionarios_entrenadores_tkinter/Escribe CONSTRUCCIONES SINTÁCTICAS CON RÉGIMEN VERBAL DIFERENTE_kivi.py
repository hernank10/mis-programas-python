import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

EJEMPLOS_ARCHIVO = "ejemplos.json"
BITACORA_ARCHIVO = "bitacora.txt"
ESTADISTICAS_ARCHIVO = "estadisticas.json"

# Datos base
EJEMPLOS = {
    "correctas": [
        "Ir y venir a Madrid",
        "Tan bueno o mejor que tú",
        "Tengo tanto o más derecho que tú"
    ],
    "incorrectas": [
        "Espero y me alegraré de que todo le salga bien",
        "Deseo y confío en que apruebes",
        "Intentó y logró que todo saliera perfecto"
    ]
}

# Cargar o inicializar ejemplos
if os.path.exists(EJEMPLOS_ARCHIVO):
    with open(EJEMPLOS_ARCHIVO, "r", encoding="utf-8") as f:
        EJEMPLOS = json.load(f)

# Funciones

def guardar_ejemplos():
    with open(EJEMPLOS_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(EJEMPLOS, f, indent=4, ensure_ascii=False)

def registrar_en_bitacora(tipo, correctas, total):
    with open(BITACORA_ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Tipo: {tipo}, Correctas: {correctas}/{total}\n")

def actualizar_estadisticas(tipo, correctas, total):
    if os.path.exists(ESTADISTICAS_ARCHIVO):
        with open(ESTADISTICAS_ARCHIVO, "r", encoding="utf-8") as f:
            stats = json.load(f)
    else:
        stats = {}

    if tipo not in stats:
        stats[tipo] = {"total": 0, "correctas": 0}

    stats[tipo]["total"] += total
    stats[tipo]["correctas"] += correctas

    with open(ESTADISTICAS_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

def mostrar_estadisticas():
    if os.path.exists(ESTADISTICAS_ARCHIVO):
        with open(ESTADISTICAS_ARCHIVO, "r", encoding="utf-8") as f:
            stats = json.load(f)
        resultado = ""
        for tipo, datos in stats.items():
            total = datos['total']
            correctas = datos['correctas']
            porcentaje = (correctas / total * 100) if total > 0 else 0
            resultado += f"{tipo.capitalize()}: {correctas}/{total} correctas ({porcentaje:.1f}%)\n"
        messagebox.showinfo("Estadísticas", resultado)
    else:
        messagebox.showinfo("Estadísticas", "No hay estadísticas disponibles todavía.")

def practicar(tipo):
    correctas = 0
    total = len(EJEMPLOS[tipo])

    for ejemplo in EJEMPLOS[tipo]:
        respuesta = messagebox.askyesno("Pregunta", f"¿Esta construcción es correcta?\n\n'{ejemplo}'")
        es_correcta = tipo == "correctas"
        if respuesta == es_correcta:
            correctas += 1

    messagebox.showinfo("Resultado", f"Respondiste correctamente {correctas} de {total}.")
    registrar_en_bitacora(tipo, correctas, total)
    actualizar_estadisticas(tipo, correctas, total)

def completar_oracion():
    base = "Tengo tanto ___ más paciencia que tú."
    respuesta = simpledialog.askstring("Completa", f"Completa la oración:\n{base}")
    if respuesta and respuesta.strip().lower() == "o":
        messagebox.showinfo("Correcto", "¡Bien hecho!")
        registrar_en_bitacora("completar", 1, 1)
        actualizar_estadisticas("completar", 1, 1)
    else:
        messagebox.showinfo("Incorrecto", "La respuesta correcta era: 'o'")
        registrar_en_bitacora("completar", 0, 1)
        actualizar_estadisticas("completar", 0, 1)

def agregar_ejemplo():
    tipo = simpledialog.askstring("Tipo", "¿El ejemplo es 'correcto' o 'incorrecto'?").lower()
    if tipo not in EJEMPLOS:
        messagebox.showerror("Error", "Tipo no válido.")
        return
    nuevo = simpledialog.askstring("Nuevo ejemplo", "Escribe el nuevo ejemplo:")
    if nuevo:
        if len(EJEMPLOS[tipo]) < 100:
            EJEMPLOS[tipo].append(nuevo)
            guardar_ejemplos()
            messagebox.showinfo("Guardado", "Ejemplo guardado correctamente.")
        else:
            messagebox.showerror("Límite", "Ya hay 100 ejemplos en esta categoría.")

def mostrar_teoria():
    teoria = (
        "Construcción incorrecta: No se debe aplicar a dos palabras un régimen que sólo conviene a una.\n"
        "Ejemplo incorrecto: 'Espero y me alegraré de que todo le salga bien.'\n\n"
        "Construcciones aceptadas: Hay casos elípticos aceptables por el uso.\n"
        "Ejemplo correcto: 'Ir y venir a Madrid', 'Tan bueno o mejor que tú'."
    )
    messagebox.showinfo("Teoría", teoria)

# Interfaz gráfica
root = tk.Tk()
root.title("Práctica de Construcciones Sintácticas")
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

botones = [
    ("📘 Ver Teoría", mostrar_teoria),
    ("✅ Practicar Correctas", lambda: practicar("correctas")),
    ("❌ Practicar Incorrectas", lambda: practicar("incorrectas")),
    ("✍️ Completar Oración", completar_oracion),
    ("➕ Agregar Ejemplo", agregar_ejemplo),
    ("📈 Ver Estadísticas", mostrar_estadisticas),
    ("🚪 Salir", root.quit)
]

for texto, comando in botones:
    tk.Button(frame, text=texto, command=comando, width=40, pady=5).pack(pady=4)

root.mainloop()
