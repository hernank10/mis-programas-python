import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random

# Lista base de ejemplos
ejemplos = [
    {"texto": "Esto me parece injusto.", "categoria": "Demostrativo neutro"},
    {"texto": "Eso no tiene sentido alguno.", "categoria": "Demostrativo neutro"},
    {"texto": "Aquello fue un momento inolvidable.", "categoria": "Demostrativo neutro"},
    {"texto": "Ello no justifica su comportamiento.", "categoria": "Demostrativo neutro"},
    {"texto": "Lo importante es participar.", "categoria": "Demostrativo neutro"},
    {"texto": "Cantar me relaja por las noches.", "categoria": "Infinitivo sustantivado"},
    {"texto": "El comer saludable mejora la salud.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Saber esperar también es sabiduría.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Mucho se dijo, pero poco se hizo.", "categoria": "Cantidad"},
    {"texto": "Nada puede detenernos ahora.", "categoria": "Concepto general"},
    {"texto": "El vivir con miedo no es vivir.", "categoria": "Construcción con artículo"},
    # ... (agrega hasta 50)
]

usuario_ejemplos = []

# Funciones
def mostrar_diapositiva():
    mensaje = (
        "Los sustantivos neutros en español no tienen género.\n\n"
        "Categorías:\n"
        "- Demostrativos neutros\n"
        "- Infinitivos sustantivados\n"
        "- Cantidades\n"
        "- Conceptos generales\n"
        "- Construcciones con artículo"
    )
    messagebox.showinfo("📘 Diapositiva Conceptual", mensaje)

def practicar_ejemplos():
    for ejemplo in ejemplos:
        texto = ejemplo['texto']
        categoria = ejemplo['categoria']
        respuesta = simpledialog.askstring("Ejemplo", f"¿Qué categoría es?:\n\n{texto}")
        if respuesta:
            if respuesta.lower() == categoria.lower():
                messagebox.showinfo("Resultado", "✅ ¡Correcto!")
            else:
                messagebox.showwarning("Resultado", f"❌ Incorrecto. Era: {categoria}")
        oracion = simpledialog.askstring("Oración", "Escribe una oración con este tipo:")
        if oracion:
            messagebox.showinfo("Oración guardada", "📝 ¡Oración escrita!")
        else:
            messagebox.showwarning("Sin oración", "⚠️ No escribiste nada.")

def cuestionario():
    seleccionados = random.sample(ejemplos, min(5, len(ejemplos)))
    puntaje = 0
    for ejemplo in seleccionados:
        resp = simpledialog.askstring("Cuestionario", f"Clasifica este ejemplo:\n{ejemplo['texto']}")
        if resp and resp.lower() == ejemplo['categoria'].lower():
            puntaje += 1
    messagebox.showinfo("Puntaje final", f"Tu puntaje: {puntaje}/5")

def agregar_ejemplo():
    if len(usuario_ejemplos) >= 100:
        messagebox.showerror("Límite alcanzado", "Has llegado al límite de 100 ejemplos.")
        return
    texto = simpledialog.askstring("Nuevo ejemplo", "Escribe un nuevo ejemplo:")
    categoria = simpledialog.askstring("Categoría", "¿Qué categoría tiene?")
    if texto and categoria:
        usuario_ejemplos.append({"texto": texto, "categoria": categoria})
        messagebox.showinfo("Ejemplo agregado", "✅ Ejemplo guardado.")

def ver_ejemplos_usuario():
    if not usuario_ejemplos:
        messagebox.showinfo("Sin ejemplos", "Aún no has agregado ejemplos.")
        return
    lista = "\n".join([f"{i+1}. {e['texto']} ({e['categoria']})" for i, e in enumerate(usuario_ejemplos)])
    messagebox.showinfo("Tus ejemplos", lista)

def guardar_ejemplos_usuario():
    with open("mis_ejemplos_gui.json", "w", encoding="utf-8") as f:
        json.dump(usuario_ejemplos, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("Guardado", "💾 Ejemplos guardados correctamente.")

# Interfaz
ventana = tk.Tk()
ventana.title("📚 Sustantivos Neutros Interactivo")
ventana.geometry("400x400")

tk.Label(ventana, text="MENÚ PRINCIPAL", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(ventana, text="📘 Ver Diapositiva Conceptual", command=mostrar_diapositiva, width=35).pack(pady=5)
tk.Button(ventana, text="🧠 Practicar con ejemplos", command=practicar_ejemplos, width=35).pack(pady=5)
tk.Button(ventana, text="❓ Cuestionario clasificatorio", command=cuestionario, width=35).pack(pady=5)
tk.Button(ventana, text="➕ Agregar nuevo ejemplo", command=agregar_ejemplo, width=35).pack(pady=5)
tk.Button(ventana, text="👀 Ver ejemplos agregados", command=ver_ejemplos_usuario, width=35).pack(pady=5)
tk.Button(ventana, text="💾 Guardar ejemplos", command=guardar_ejemplos_usuario, width=35).pack(pady=5)
tk.Button(ventana, text="🚪 Salir", command=ventana.quit, width=35).pack(pady=20)

ventana.mainloop()
