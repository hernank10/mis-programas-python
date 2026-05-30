import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

# Diccionarios de ejemplos fijos y personalizados
ejemplos_fijos = {
    "Nivel semántico categorial": {
        "casa": ("Sustantivo: nombra un objeto.", "house"),
        "grande": ("Adjetivo calificativo: expresa una cualidad.", "big"),
        "correr": ("Verbo: indica acción.", "run"),
        "rápidamente": ("Adverbio: modifica el verbo.", "quickly"),
        "ella": ("Pronombre: sustituye al sustantivo femenino.", "she")
    },
    "Nivel morfológico": {
        "florista": ("Derivación: flor + ista.", "florist"),
        "soleado": ("Derivación: sol + eado.", "sunny"),
        "comíamos": ("Flexión verbal: 1.ª persona plural, pretérito imperfecto.", "we used to eat"),
        "niños": ("Flexión nominal: plural del sustantivo.", "children"),
        "infeliz": ("Derivación con prefijo: in- + feliz.", "unhappy")
    },
    "Nivel sintáctico": {
        "El gato duerme": ("Oración simple. Sujeto: 'El gato'. Predicado: 'duerme'.", "The cat sleeps"),
        "Estudió mucho y aprobó el examen": ("Coordinada copulativa.", "He studied a lot and passed the exam"),
        "Me alegra que hayas venido": ("Subordinada sustantiva.", "I’m glad you came"),
        "Juan comió manzanas": ("Complemento directo: 'manzanas'.", "Juan ate apples"),
        "Pedro aunque estaba cansado siguió caminando": ("Conector concesivo: 'aunque'.", "Pedro, although tired, kept walking")
    },
    "Nivel fonológico y ortográfico": {
        "zapato": ("Fonema /s/ representado con 'z'.", "shoe"),
        "queso": ("Fonema /k/ representado con 'qu'.", "cheese"),
        "gente": ("Fonema /x/ representado con 'g' ante 'e'.", "people"),
        "lluvia": ("Fonema palatal /ʝ/ representado con 'll'.", "rain"),
        "niño": ("Fonema nasal palatal /ɲ/ representado con 'ñ'.", "boy")
    }
}
ejemplos_usuario = {k: [] for k in ejemplos_fijos}

# Funciones para la GUI
def mostrar_diapositiva():
    texto = (
        "📖 DIAPOSITIVA TEÓRICA\n\n"
        "a. Semántico categorial:\n - Significado y función de palabras (sustantivo, adjetivo, verbo).\n\n"
        "b. Morfológico:\n - Formación de palabras, raíz y morfemas.\n\n"
        "c. Sintáctico:\n - Estructura de oraciones, sujeto, predicado, modificadores.\n\n"
        "d. Fonológico y ortográfico:\n - Sonidos y letras. Ortografía y fonemas (z, qu, ll, ñ).\n"
    )
    messagebox.showinfo("Diapositiva Teórica", texto)

def practicar_escritura():
    for nivel, ejemplos in ejemplos_fijos.items():
        palabras = list(ejemplos.items())
        random.shuffle(palabras)
        for palabra, (desc, _) in palabras:
            entrada = simpledialog.askstring("Escritura", f"{nivel}\nEscribe la palabra: {desc}")
            if entrada is None:
                return
            if entrada.lower() == palabra.lower():
                messagebox.showinfo("Correcto", f"✅ ¡Correcto!\nLa palabra es: {palabra}")
            else:
                messagebox.showwarning("Incorrecto", f"❌ Era: {palabra}")

def practicar_traduccion():
    for nivel, ejemplos in ejemplos_fijos.items():
        palabras = list(ejemplos.items())
        random.shuffle(palabras)
        for palabra, (_, traduccion) in palabras:
            entrada = simpledialog.askstring("Traducción", f"{nivel}\nTraduce al inglés: {palabra}")
            if entrada is None:
                return
            if entrada.lower() == traduccion.lower():
                messagebox.showinfo("Correcto", f"✅ ¡Correcto!\nLa traducción es: {traduccion}")
            else:
                messagebox.showwarning("Incorrecto", f"❌ Era: {traduccion}")

def crear_ejemplo():
    nivel = simpledialog.askstring("Crear", "Nivel (semántico, morfológico, sintáctico, fonológico):")
    if not nivel:
        return
    nivel_key = f"Nivel {nivel.strip().lower()} categorial" if nivel.strip().lower() == "semántico" else (
        f"Nivel {nivel.strip().lower()}" if nivel.strip().lower() in ["morfológico", "sintáctico"] else "Nivel fonológico y ortográfico"
    )
    if nivel_key not in ejemplos_usuario:
        messagebox.showerror("Error", "Nivel no válido.")
        return
    if len(ejemplos_usuario[nivel_key]) >= 10:
        messagebox.showwarning("Límite", "Ya tienes 10 ejemplos en esta categoría.")
        return
    palabra = simpledialog.askstring("Ejemplo", "Palabra o oración:")
    descripcion = simpledialog.askstring("Ejemplo", "Descripción:")
    traduccion = simpledialog.askstring("Ejemplo", "Traducción en inglés:")
    if palabra and descripcion and traduccion:
        ejemplos_usuario[nivel_key].append((palabra, descripcion, traduccion))
        messagebox.showinfo("Guardado", "Ejemplo añadido.")

def ver_ejemplos():
    salida = ""
    for nivel, lista in ejemplos_usuario.items():
        salida += f"== {nivel} ==\n"
        for palabra, desc, trad in lista:
            salida += f" - {palabra} | {desc} | EN: {trad}\n"
        salida += "\n"
    mostrar_ventana_texto("Ejemplos del usuario", salida)

def guardar_ejemplos():
    with open("ejemplos_usuario.txt", "w", encoding="utf-8") as f:
        for nivel, lista in ejemplos_usuario.items():
            f.write(f"== {nivel} ==\n")
            for palabra, desc, trad in lista:
                f.write(f"{palabra} - {desc} - {trad}\n")
            f.write("\n")
    messagebox.showinfo("Guardado", "Ejemplos guardados en 'ejemplos_usuario.txt'")

def mostrar_ventana_texto(titulo, contenido):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    text = tk.Text(ventana, wrap="word", width=70, height=30)
    text.insert("1.0", contenido)
    text.config(state="disabled")
    text.pack(padx=10, pady=10)

# GUI principal
ventana = tk.Tk()
ventana.title("Estudio Lingüístico Interactivo")

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill='both')

# Pestañas
tabs = {
    "Diapositiva": mostrar_diapositiva,
    "Escritura": practicar_escritura,
    "Traducción": practicar_traduccion,
    "Crear Ejemplo": crear_ejemplo,
    "Ver Ejemplos": ver_ejemplos,
    "Guardar Ejemplos": guardar_ejemplos
}

for nombre, funcion in tabs.items():
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=nombre)
    boton = tk.Button(frame, text=nombre, command=funcion, font=("Arial", 14), padx=10, pady=5)
    boton.pack(pady=30)

ventana.mainloop()
