import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import os
import pyttsx3
import random

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
    "Sinónimos": "El día estaba alegre y contento, lleno de cosas hermosas y bellas...",
    "Homónimos": "Fui al banco a sentarme. Luego pasé por el banco a retirar dinero...",
    "Homófonas": "La ola golpeó la orilla. Dije hola al pescador...",
    "Isónimos": "El doctor y el médico llegaron a atender al infante...",
    "Antónimos": "Pasamos de la alegría a la tristeza. Algunos eran fuertes, otros débiles..."
}

puntaje_total = 0

def procesar_ensayo():
    global puntaje_total
    categoria = categoria_var.get()
    palabras = categorias[categoria]
    texto = entrada_ensayo.get("1.0", tk.END).strip().lower()
    texto_palabras = texto.split()
    coincidencias = [p for p in palabras if p in texto_palabras]

    if len(coincidencias) >= 5:
        resultado = "✅ ¡Bien hecho! Has usado al menos 5 palabras aprendidas."
        puntaje_total += 10
    else:
        resultado = "❌ Intenta incluir más palabras aprendidas (mínimo 5)."
        puntaje_total += 2

    messagebox.showinfo("Resultado del análisis", f"{resultado}\nPalabras encontradas: {len(coincidencias)}")

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
    actualizar_puntaje()

def mostrar_ejemplo():
    categoria = categoria_var.get()
    ejemplo = ejemplos.get(categoria, "No hay ejemplo disponible.")
    messagebox.showinfo("Ejemplo de ensayo", ejemplo)

def mostrar_palabras():
    categoria = categoria_var.get()
    lista = categorias.get(categoria, [])
    messagebox.showinfo("Palabras aprendidas", "\n".join(lista))

def leer_ensayo():
    carpeta = "ensayos_guardados"
    archivo = filedialog.askopenfilename(initialdir=carpeta, title="Abrir ensayo guardado")
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            entrada_ensayo.delete("1.0", tk.END)
            entrada_ensayo.insert(tk.END, contenido)

def leer_voz():
    texto = entrada_ensayo.get("1.0", tk.END).strip()
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def actualizar_puntaje():
    lbl_puntaje.config(text=f"🎯 Puntaje total: {puntaje_total}")

def prueba_multiple():
    categoria = categoria_var.get()
    palabras = categorias[categoria]
    palabra = random.choice(palabras)
    opciones = random.sample(palabras, 3)
    if palabra not in opciones:
        opciones[random.randint(0, 2)] = palabra
    respuesta = messagebox.askquestion("Prueba de selección", f"¿Cuál es una palabra de la categoría '{categoria}'?\n\n" + "\n".join(opciones))
    if respuesta == "yes":
        messagebox.showinfo("Resultado", f"La palabra era: {palabra}")
    else:
        messagebox.showinfo("Resultado", "Sigue intentando.")

# Interfaz
ventana = tk.Tk()
ventana.title("🧠 Práctica de Palabras con Tkinter")

categoria_var = tk.StringVar(value="Sinónimos")
menu_categorias = tk.OptionMenu(ventana, categoria_var, *categorias.keys())
menu_categorias.pack(pady=5)

btn_palabras = tk.Button(ventana, text="📋 Ver palabras aprendidas", command=mostrar_palabras)
btn_palabras.pack()

etiqueta = tk.Label(ventana, text="📝 Escribe tu ensayo:")
etiqueta.pack()
entrada_ensayo = scrolledtext.ScrolledText(ventana, width=60, height=10)
entrada_ensayo.pack(padx=10, pady=5)

btn_procesar = tk.Button(ventana, text="✅ Verificar y guardar ensayo", command=procesar_ensayo)
btn_procesar.pack(pady=5)

btn_ejemplo = tk.Button(ventana, text="📌 Ver ejemplo automático", command=mostrar_ejemplo)
btn_ejemplo.pack()

btn_leer_archivo = tk.Button(ventana, text="📂 Leer ensayo guardado", command=leer_ensayo)
btn_leer_archivo.pack()

btn_voz = tk.Button(ventana, text="🔊 Leer ensayo en voz alta", command=leer_voz)
btn_voz.pack()

btn_prueba = tk.Button(ventana, text="🧪 Prueba de selección múltiple", command=prueba_multiple)
btn_prueba.pack()

lbl_puntaje = tk.Label(ventana, text="🎯 Puntaje total: 0")
lbl_puntaje.pack(pady=5)

ventana.mainloop()

