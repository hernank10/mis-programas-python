import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, scrolledtext
import json
import os

# Ruta para guardar ejemplos personalizados
EJEMPLOS_FILE = "ejemplos.json"

# Cargar ejemplos personalizados desde archivo
def cargar_ejemplos():
    if os.path.exists(EJEMPLOS_FILE):
        with open(EJEMPLOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Guardar ejemplos personalizados en archivo
def guardar_ejemplos(ejemplos):
    with open(EJEMPLOS_FILE, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, ensure_ascii=False, indent=4)

# Ensayo explicativo
ENSAYO_TEXTO = """Unidad Didáctica: Adjetivos Derivados

Los adjetivos derivados se forman a partir de otras palabras, generalmente sustantivos o verbos, mediante la adición de sufijos. Por ejemplo:
- montaña → montañoso
- niño → infantil
- flor → floral

Estos adjetivos cumplen funciones descriptivas que enriquecen el lenguaje y permiten una comunicación más precisa. En secundaria, es clave que el estudiante reconozca su origen léxico y su uso en contextos variados.

Sufijos comunes:
- -oso/-osa (montañoso)
- -al (floral)
- -il (infantil)
- -ivo (creativo)

Actividades:
1. Asociación entre sustantivo y adjetivo.
2. Completar oraciones con el adjetivo derivado correcto.
3. Clasificación semántica de los adjetivos (lugar, cualidad, pertenencia).
"""

# Mostrar el ensayo en una nueva ventana
def mostrar_ensayo():
    ensayo_ventana = tk.Toplevel(root)
    ensayo_ventana.title("Ensayo: Adjetivos Derivados")
    ensayo_texto = scrolledtext.ScrolledText(ensayo_ventana, wrap=tk.WORD, width=70, height=20)
    ensayo_texto.insert(tk.END, ENSAYO_TEXTO)
    ensayo_texto.config(state=tk.DISABLED)
    ensayo_texto.pack(padx=10, pady=10)

# Editor de ejemplos personalizados
def editor_de_ejemplos():
    editor = tk.Toplevel(root)
    editor.title("Editor de Ejemplos (máximo 100)")
    editor.geometry("500x400")

    ejemplos = cargar_ejemplos()

    lista = tk.Listbox(editor, width=60, height=10)
    lista.pack(pady=10)

    for ej in ejemplos:
        lista.insert(tk.END, ej)

    entrada = tk.Entry(editor, width=60)
    entrada.pack(pady=5)

    def agregar():
        nuevo = entrada.get().strip()
        if nuevo and len(ejemplos) < 100:
            ejemplos.append(nuevo)
            lista.insert(tk.END, nuevo)
            guardar_ejemplos(ejemplos)
            entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Límite o entrada vacía", "No se puede agregar más de 100 ejemplos o campo vacío.")

    def editar():
        seleccionado = lista.curselection()
        if seleccionado:
            idx = seleccionado[0]
            nuevo_texto = simpledialog.askstring("Editar ejemplo", "Modifica el ejemplo:", initialvalue=ejemplos[idx])
            if nuevo_texto:
                ejemplos[idx] = nuevo_texto
                lista.delete(idx)
                lista.insert(idx, nuevo_texto)
                guardar_ejemplos(ejemplos)

    def eliminar():
        seleccionado = lista.curselection()
        if seleccionado:
            idx = seleccionado[0]
            if messagebox.askyesno("Confirmar", "¿Eliminar este ejemplo?"):
                lista.delete(idx)
                del ejemplos[idx]
                guardar_ejemplos(ejemplos)

    tk.Button(editor, text="Agregar", command=agregar).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(editor, text="Editar", command=editar).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(editor, text="Eliminar", command=eliminar).pack(side=tk.LEFT, padx=5, pady=5)

# Funciones simuladas de ejercicios
def ejercicio_simulado(nombre):
    messagebox.showinfo("Ejercicio", f"Aquí se mostrará el ejercicio de tipo: {nombre}")

# Interfaz principal
root = tk.Tk()
root.title("Adjetivos Derivados - Unidad Didáctica Interactiva")
root.geometry("500x450")

tk.Label(root, text="Seleccione una actividad", font=("Arial", 16)).pack(pady=20)

botones = [
    ("Asociación", lambda: ejercicio_simulado("Asociación")),
    ("Completar oración", lambda: ejercicio_simulado("Completar oración")),
    ("Clasificación semántica", lambda: ejercicio_simulado("Clasificación semántica")),
    ("Redacción guiada", lambda: ejercicio_simulado("Redacción guiada")),
    ("📖 Ver ensayo", mostrar_ensayo),
    ("📝 Editor de ejemplos", editor_de_ejemplos),
    ("Salir", root.quit)
]

for texto, comando in botones:
    tk.Button(root, text=texto, width=30, command=comando).pack(pady=5)

root.mainloop()
