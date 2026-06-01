import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import matplotlib.pyplot as plt

# Crear ventana principal
root = tk.Tk()
root.title("Evaluación de Redacción")
root.geometry("800x600")

# Variables para puntajes
puntaje_estructura = tk.IntVar(value=0)
puntaje_ortografia = tk.IntVar(value=0)
puntaje_claridad = tk.IntVar(value=0)
mensaje_resultado = tk.StringVar()

# Área de escritura
area_texto = tk.Text(root, height=8, width=70, font=("Arial", 12))

# Función para evaluar el texto del usuario
def evaluar_redaccion():
    contenido = area_texto.get("1.0", tk.END).strip()
    
    # Evaluación de estructura
    if len(contenido.split()) > 20:
        puntaje_estructura.set(10)
        estructura_msg = "✅ Estructura correcta."
    else:
        puntaje_estructura.set(5)
        estructura_msg = "❌ Falta desarrollo en la estructura."

    # Evaluación de ortografía
    errores_ortograficos = ["ke", "xq", "haiga", "kiero"]
    if any(error in contenido for error in errores_ortograficos):
        puntaje_ortografia.set(5)
        ortografia_msg = "❌ Hay errores ortográficos."
    else:
        puntaje_ortografia.set(10)
        ortografia_msg = "✅ Buena ortografía."

    # Evaluación de claridad
    if len(set(contenido.split())) > 15:
        puntaje_claridad.set(10)
        claridad_msg = "✅ Texto claro y comprensible."
    else:
        puntaje_claridad.set(5)
        claridad_msg = "❌ Puede mejorar la coherencia."

    # Mensaje final
    mensaje_resultado.set(f"{estructura_msg}\n{ortografia_msg}\n{claridad_msg}")

# Función para guardar resultados en historial
def guardar_resultado():
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    contenido = area_texto.get("1.0", tk.END).strip()
    total_puntaje = puntaje_estructura.get() + puntaje_ortografia.get() + puntaje_claridad.get()
    
    with open("historial_resultados.txt", "a", encoding="utf-8") as file:
        file.write(f"{fecha}\nTexto: {contenido}\nPuntaje total: {total_puntaje}/30\n{'-'*40}\n")

    messagebox.showinfo("Historial", "✅ Resultado guardado en el historial.")

# Función para mostrar gráficos de progreso
def mostrar_grafico():
    categorias = ["Estructura", "Ortografía", "Claridad"]
    puntajes = [puntaje_estructura.get(), puntaje_ortografia.get(), puntaje_claridad.get()]
    
    plt.bar(categorias, puntajes, color=["blue", "red", "green"])
    plt.title("Evaluación de Redacción")
    plt.ylim(0, 10)
    plt.show()

# Interfaz de evaluación
ttk.Label(root, text="✍️ Escribe tu texto aquí:", font=("Arial", 12)).pack(pady=10)
area_texto.pack(pady=10)

frame_acciones = ttk.Frame(root)
frame_acciones.pack(pady=10)
ttk.Button(frame_acciones, text="Evaluar Redacción", command=evaluar_redaccion).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_acciones, text="Guardar Resultado", command=guardar_resultado).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_acciones, text="Ver Gráfico de Progreso", command=mostrar_grafico).pack(side=tk.LEFT, padx=10)

# Mensaje de retroalimentación
ttk.Label(root, textvariable=mensaje_resultado, font=("Arial", 12), wraplength=700, foreground="blue").pack(pady=5)

# Ejecutar aplicación
root.mainloop()
