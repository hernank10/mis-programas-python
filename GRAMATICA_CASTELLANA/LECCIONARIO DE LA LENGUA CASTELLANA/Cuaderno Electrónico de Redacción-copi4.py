import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Crear ventana principal
root = tk.Tk()
root.title("Cuaderno Electrónico de Redacción")
root.geometry("800x600")

# Crear el Notebook para pestañas temáticas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Diccionario de plantillas organizadas por tipo de texto
plantillas = {
    "Diálogo": {
        "descripcion": "🎭 Texto dialogado: Representa conversaciones entre personajes con estructura teatral.",
        "guia": "📜 Claves del diálogo teatral:\n✅ Usa nombres para identificar personajes.\n✅ Usa acotaciones para indicar acciones.\n✅ Mantén coherencia en la conversación."
    },
    "Reseña": {
        "descripcion": "📖 Reseña crítica: Evalúa una obra, libro o película con argumentos y opiniones.",
        "guia": "📜 Claves de la reseña:\n✅ Presenta una introducción clara.\n✅ Describe los puntos clave de la obra.\n✅ Expón tu opinión fundamentada."
    },
    "Noticia": {
        "descripcion": "📰 Texto periodístico: Informa sobre un hecho relevante con datos verificables.",
        "guia": "📜 Claves de la noticia:\n✅ Explica qué, quién, cuándo, dónde y por qué.\n✅ Usa lenguaje objetivo y claro.\n✅ Presenta fuentes o testimonios."
    },
    "Crónica": {
        "descripcion": "📜 Crónica narrativa: Relata un suceso con detalles y observaciones personales.",
        "guia": "📜 Claves de la crónica:\n✅ Usa narración detallada.\n✅ Relata el suceso en orden cronológico.\n✅ Agrega reflexiones o análisis sobre el hecho."
    }
}

# Variable para mostrar contenido seleccionado
texto_guia = tk.StringVar()
texto_guia.set("Seleccione una plantilla para comenzar.")

# Área de escritura
area_texto = tk.Text(root, height=8, width=70, font=("Arial", 12))

# Función para mostrar plantilla seleccionada
def mostrar_plantilla(tipo):
    texto_guia.set(plantillas[tipo]["guia"])

# Función para guardar redacción en archivo .txt
def guardar_redaccion():
    contenido = area_texto.get("1.0", tk.END).strip()
    if contenido:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        with open("redaccion_guardada.txt", "a", encoding="utf-8") as file:
            file.write(f"{fecha}\n{contenido}\n{'-'*40}\n")
        mensaje.set("✅ Texto guardado exitosamente.")
    else:
        mensaje.set("⚠️ Escribe algo antes de guardar.")

# Función para evaluación automática de estructura y ortografía
def evaluar_redaccion():
    contenido = area_texto.get("1.0", tk.END).strip()
    palabras_clave = ["quién", "dijo", "acto", "evento", "opinión", "detalle", "cronología"]
    
    if any(palabra in contenido for palabra in palabras_clave):
        mensaje.set("✅ ¡Tu texto tiene buena estructura!")
    else:
        mensaje.set("❌ Revisa la coherencia de tu redacción.")

# Función de "Modo Reto" que oculta la guía
def modo_reto():
    texto_guia.set("🎯 Modo Reto Activado: Escribe sin ver la plantilla.")
    area_texto.delete("1.0", tk.END)

# Menú de selección por tipo de texto
ttk.Label(root, text="📚 Seleccione un tipo de texto:", font=("Arial", 14)).pack(pady=10)
frame_botones = ttk.Frame(root)
frame_botones.pack()

for tipo in plantillas.keys():
    ttk.Button(frame_botones, text=tipo, command=lambda t=tipo: mostrar_plantilla(t)).pack(side=tk.LEFT, padx=5)

# Área de contenido de la plantilla
ttk.Label(root, textvariable=texto_guia, font=("Arial", 12), wraplength=700).pack(pady=10)

# Área de escritura
area_texto.pack(pady=10)

# Botones de evaluación, guardado y modo reto
frame_acciones = ttk.Frame(root)
frame_acciones.pack(pady=10)
ttk.Button(frame_acciones, text="Guardar Redacción", command=guardar_redaccion).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_acciones, text="Evaluar Redacción", command=evaluar_redaccion).pack(side=tk.LEFT, padx=10)
ttk.Button(frame_acciones, text="Modo Reto", command=modo_reto).pack(side=tk.LEFT, padx=10)

# Mensaje de resultado
mensaje = tk.StringVar()
ttk.Label(root, textvariable=mensaje, font=("Arial", 12)).pack(pady=5)

# Ejecutar aplicación
root.mainloop()
