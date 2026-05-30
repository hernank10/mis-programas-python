import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import os

archivo_resultados = "ejercicios_palabras_claras.txt"

palabras_default = [
    ("rol", "trabajo"),
    ("asueto", "descanso"),
    ("atenaza", "dificulta"),
    ("axiológico", "de los valores"),
    ("bonísimo", "muy bueno"),
    ("boom", "auge"),
    ("burgomaestre", "alcalde"),
    ("cloud computing", "computación en la nube"),
    ("constipación", "resfriado"),
    ("lustro", "cinco años")
]

def guardar_ejemplo(texto):
    with open(archivo_resultados, "a", encoding="utf-8") as f:
        f.write(texto + "\n\n")

def mostrar_teoria():
    mensaje = (
        "🧠 TEORÍA:\n"
        "Usa palabras conocidas en vez de técnicas o complejas.\n"
        "Ejemplo: usa 'trabajo' en vez de 'rol', o 'descanso' en vez de 'asueto'.\n"
        "📌 Ortega y Gasset: «La claridad es la cortesía del filósofo».\n"
        "📌 San Agustín: «La sencillez es la sal de la perfección»."
    )
    messagebox.showinfo("Teoría", mensaje)

def practicar_ejemplo(palabra_rara, palabra_clara):
    sugerida = simpledialog.askstring("Sugerencia", f"Palabra menos conocida: '{palabra_rara}'.\nSugerencia más clara: '{palabra_clara}'\n¿Con qué palabra clara la sustituirías?")
    oracion1 = simpledialog.askstring("Oración 1", f"Escribe una oración con '{palabra_rara}':")
    oracion2 = simpledialog.askstring("Oración 2", f"Escribe una oración con la palabra clara '{sugerida}':")
    reflexion = simpledialog.askstring("Reflexión", "¿Cuál oración se entiende mejor y por qué?")

    resultado = (
        f"Palabra compleja: {palabra_rara}\n"
        f"Alternativa clara: {sugerida}\n"
        f"Oración con palabra rara: {oracion1}\n"
        f"Oración con palabra clara: {oracion2}\n"
        f"Reflexión: {reflexion}\n"
        + "-"*50
    )
    guardar_ejemplo(resultado)
    messagebox.showinfo("Guardado", "✅ Ejercicio guardado correctamente.")

def crear_pares():
    nueva_lista = []
    while True:
        palabra_rara = simpledialog.askstring("Nueva palabra", "Palabra técnica o poco conocida:")
        palabra_clara = simpledialog.askstring("Alternativa", f"¿Cuál sería una alternativa clara para '{palabra_rara}'?")
        nueva_lista.append((palabra_rara, palabra_clara))
        continuar = messagebox.askyesno("Continuar", "¿Deseas agregar otro par?")
        if not continuar:
            break
    for pareja in nueva_lista:
        practicar_ejemplo(*pareja)

def simplificar_oracion():
    original = simpledialog.askstring("Oración técnica", "Escribe una oración técnica o literaria:")
    simplificada = simpledialog.askstring("Oración clara", "Reescribe la oración con lenguaje más claro:")
    reflexion = simpledialog.askstring("Reflexión", "¿Qué cambia al simplificarla?")

    resultado = (
        f"Oración original: {original}\n"
        f"Versión simplificada: {simplificada}\n"
        f"Reflexión: {reflexion}\n"
        + "-"*50
    )
    guardar_ejemplo(resultado)
    messagebox.showinfo("Guardado", "✅ Oración simplificada guardada correctamente.")

def ver_archivo():
    if not os.path.exists(archivo_resultados):
        messagebox.showinfo("Archivo vacío", "Aún no has guardado ejercicios.")
        return

    ventana_archivo = tk.Toplevel(root)
    ventana_archivo.title("Ejercicios guardados")
    texto = scrolledtext.ScrolledText(ventana_archivo, width=80, height=25)
    texto.pack(padx=10, pady=10)

    with open(archivo_resultados, "r", encoding="utf-8") as f:
        contenido = f.read()
        texto.insert(tk.END, contenido)

# Crear ventana principal
root = tk.Tk()
root.title("✍️ Claridad en la Escritura - Usa palabras conocidas")

# Crear botones
tk.Button(root, text="📘 Ver teoría", width=40, command=mostrar_teoria).pack(pady=5)
tk.Button(root, text="🧪 Practicar con ejemplos por defecto", width=40, command=lambda: [practicar_ejemplo(*par) for par in palabras_default]).pack(pady=5)
tk.Button(root, text="✍️ Crear tus propios pares", width=40, command=crear_pares).pack(pady=5)
tk.Button(root, text="🔁 Reescribir una oración compleja", width=40, command=simplificar_oracion).pack(pady=5)
tk.Button(root, text="📂 Ver ejercicios guardados", width=40, command=ver_archivo).pack(pady=5)
tk.Button(root, text="❌ Salir", width=40, command=root.quit).pack(pady=20)

# Ejecutar
root.mainloop()
