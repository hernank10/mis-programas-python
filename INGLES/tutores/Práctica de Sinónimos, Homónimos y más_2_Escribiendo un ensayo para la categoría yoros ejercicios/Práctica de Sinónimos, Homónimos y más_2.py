import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

# Diccionario de palabras por categoría
categorias = {
    "Sinónimos": ["alegre", "contento", "hermoso", "bello", "rápido", "veloz", "difícil", "complicado", "enseñar", "instruir"],
    "Homónimos": ["banco", "cura", "banda", "capital", "vela", "cola", "ratón", "vino", "sal", "gato"],
    "Homófonas": ["hola", "ola", "vaca", "baca", "casa", "caza", "bello", "vello", "haya", "halla"],
    "Isónimos": ["doctor", "médico", "niño", "infante", "madre", "progenitora", "padre", "progenitor", "estudiante", "alumno"],
    "Antónimos": ["alegría", "tristeza", "fuerte", "débil", "largo", "corto", "falso", "verdadero", "bueno", "malo"]
}

# Ensayos de ejemplo
ejemplos = {
    "Sinónimos": "El día estaba alegre y contento, lleno de cosas hermosas y bellas. El niño corría rápido y veloz...",
    "Homónimos": "Fui al banco a sentarme. Luego pasé por el banco a retirar dinero. La cura fue milagrosa, o quizás era el cura del pueblo...",
    "Homófonas": "La ola golpeó la orilla. Dije hola al pescador. Vi una vaca y escuché ruidos en la baca del auto...",
    "Isónimos": "El doctor y el médico llegaron a atender al infante. Su madre o progenitora estaba preocupada...",
    "Antónimos": "Pasamos de la alegría a la tristeza. Algunos eran fuertes, otros débiles. El camino largo fue mejor que el corto..."
}

# Función principal para procesar el ensayo
def procesar_ensayo():
    categoria = categoria_var.get()
    palabras = categorias[categoria]
    texto = entrada_ensayo.get("1.0", tk.END).strip().lower()
    texto_palabras = texto.split()
    coincidencias = [p for p in palabras if p in texto_palabras]

    if len(coincidencias) >= 5:
        resultado = "✅ ¡Bien hecho! Has usado al menos 5 palabras aprendidas."
    else:
        resultado = "❌ Intenta incluir más palabras aprendidas (mínimo 5)."

    # Mostrar resultado
    messagebox.showinfo("Resultado del análisis", f"{resultado}\nPalabras encontradas: {len(coincidencias)}")

    # Guardar archivo
    carpeta = "ensayos_guardados"
    os.makedirs(carpeta, exist_ok=True)
    nombre_archivo = f"{carpeta}/ensayo_{categoria.lower()}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Categoría: {categoria}\n")
        f.write("Palabras aprendidas: " + ", ".join(palabras) + "\n")
        f.write("Ensayo del usuario:\n" + texto + "\n")
        f.write(f"\nPalabras coincididas: {len(coincidencias)}\n")
        f.write("Resultado: " + resultado + "\n")

    messagebox.showinfo("Ensayo guardado", f"El ensayo se guardó en:\n{nombre_archivo}")

# Mostrar ejemplo
def mostrar_ejemplo():
    categoria = categoria_var.get()
    ejemplo = ejemplos.get(categoria, "No hay ejemplo disponible.")
    messagebox.showinfo("Ejemplo de ensayo", ejemplo)

# Mostrar palabras
def mostrar_palabras():
    categoria = categoria_var.get()
    lista = categorias.get(categoria, [])
    messagebox.showinfo("Palabras aprendidas", "\n".join(lista))

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("🧠 Práctica de Sinónimos, Homónimos y más")

# Categoría seleccionada
categoria_var = tk.StringVar(value="Sinónimos")
menu_categorias = tk.OptionMenu(ventana, categoria_var, *categorias.keys())
menu_categorias.pack(pady=5)

# Botón para mostrar palabras
btn_palabras = tk.Button(ventana, text="📋 Ver palabras aprendidas", command=mostrar_palabras)
btn_palabras.pack()

# Entrada de texto para el ensayo
etiqueta = tk.Label(ventana, text="📝 Escribe tu ensayo:")
etiqueta.pack()
entrada_ensayo = scrolledtext.ScrolledText(ventana, width=60, height=10)
entrada_ensayo.pack(padx=10, pady=5)

# Botones de acciones
btn_procesar = tk.Button(ventana, text="✅ Verificar y guardar ensayo", command=procesar_ensayo)
btn_procesar.pack(pady=5)

btn_ejemplo = tk.Button(ventana, text="📌 Ver ejemplo automático", command=mostrar_ejemplo)
btn_ejemplo.pack()

# Ejecutar la interfaz
ventana.mainloop()
