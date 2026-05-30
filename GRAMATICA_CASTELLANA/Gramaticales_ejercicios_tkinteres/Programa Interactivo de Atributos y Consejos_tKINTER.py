import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os

# Archivo donde se guardarán los datos
ARCHIVO_DATOS = "datos_consejos.json"

# Cargar o crear estructura inicial
def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"Autoestima": [], "Relaciones": []}

def guardar_datos():
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(consejos, f, indent=4, ensure_ascii=False)

consejos = cargar_datos()
progreso_total = 0
total_consejos = sum(len(lst) for lst in consejos.values())

# Resto del código anterior para mostrar ensayo, practicar, etc...

# NUEVO: Gestión de ejemplos
def gestionar_ejemplos():
    ventana = tk.Toplevel(root)
    ventana.title("Gestión de Ejemplos por Categoría")
    
    def mostrar_ejemplos():
        lista.delete(0, tk.END)
        categoria = cat_var.get()
        if categoria:
            for idx, item in enumerate(consejos[categoria]):
                lista.insert(tk.END, f"{idx + 1}. {item['consejo'][:50]}...")

    def agregar_ejemplo():
        categoria = cat_var.get()
        if not categoria:
            messagebox.showwarning("Advertencia", "Selecciona una categoría.")
            return
        consejo = simpledialog.askstring("Nuevo consejo", "Escribe el consejo:")
        ejemplo = simpledialog.askstring("Ejemplo", "Escribe el ejemplo:")
        atributo = simpledialog.askstring("Atributo", "Escribe el atributo semántico:")
        if consejo and ejemplo and atributo:
            consejos[categoria].append({
                "consejo": consejo,
                "ejemplo": ejemplo,
                "atributo_correcto": atributo.lower()
            })
            mostrar_ejemplos()

    def editar_ejemplo():
        categoria = cat_var.get()
        idx = lista.curselection()
        if not categoria or not idx:
            return
        i = idx[0]
        item = consejos[categoria][i]
        nuevo_consejo = simpledialog.askstring("Editar Consejo", "Edita el consejo:", initialvalue=item["consejo"])
        nuevo_ejemplo = simpledialog.askstring("Editar Ejemplo", "Edita el ejemplo:", initialvalue=item["ejemplo"])
        nuevo_atributo = simpledialog.askstring("Editar Atributo", "Edita el atributo:", initialvalue=item["atributo_correcto"])
        if nuevo_consejo and nuevo_ejemplo and nuevo_atributo:
            consejos[categoria][i] = {
                "consejo": nuevo_consejo,
                "ejemplo": nuevo_ejemplo,
                "atributo_correcto": nuevo_atributo.lower()
            }
            mostrar_ejemplos()

    def eliminar_ejemplo():
        categoria = cat_var.get()
        idx = lista.curselection()
        if not categoria or not idx:
            return
        i = idx[0]
        if messagebox.askyesno("Eliminar", "¿Deseas eliminar este ejemplo?"):
            consejos[categoria].pop(i)
            mostrar_ejemplos()

    def nueva_categoria():
        nueva = simpledialog.askstring("Nueva Categoría", "Nombre de la nueva categoría:")
        if nueva and nueva not in consejos:
            consejos[nueva] = []
            cat_menu['values'] = list(consejos.keys())
            cat_var.set(nueva)
            mostrar_ejemplos()

    cat_var = tk.StringVar()
    tk.Label(ventana, text="Categoría:").pack()
    cat_menu = ttk.Combobox(ventana, textvariable=cat_var, values=list(consejos.keys()), state="readonly")
    cat_menu.pack()

    tk.Button(ventana, text="Mostrar ejemplos", command=mostrar_ejemplos).pack()
    lista = tk.Listbox(ventana, width=60, height=10)
    lista.pack(pady=10)

    tk.Button(ventana, text="Agregar nuevo ejemplo", command=agregar_ejemplo).pack()
    tk.Button(ventana, text="Editar ejemplo seleccionado", command=editar_ejemplo).pack()
    tk.Button(ventana, text="Eliminar ejemplo seleccionado", command=eliminar_ejemplo).pack()
    tk.Button(ventana, text="Crear nueva categoría", command=nueva_categoria).pack()

# BOTÓN GUARDAR
def guardar_manual():
    guardar_datos()
    messagebox.showinfo("Guardado", "Los datos han sido guardados correctamente.")

# ACTUALIZACIÓN DEL MENÚ PRINCIPAL
root = tk.Tk()
root.title("Programa Interactivo de Atributos y Consejos")
root.geometry("600x500")

tk.Label(root, text="🧠 Programa Interactivo: Atributos y Escritura", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Button(root, text="1. Leer ensayo explicativo", command=mostrar_ensayo, width=40).pack(pady=5)

cat_var = tk.StringVar()
tk.Label(root, text="Selecciona una categoría para practicar:", font=("Arial", 12)).pack()
cat_menu = ttk.Combobox(root, textvariable=cat_var, values=list(consejos.keys()), state="readonly")
cat_menu.pack()

tk.Button(root, text="2. Practicar consejos por categoría", command=practicar_consejos, width=40).pack(pady=5)
tk.Button(root, text="3. Ver progreso", command=ver_progreso, width=40).pack(pady=5)
tk.Button(root, text="4. Gestionar ejemplos (crear, editar...)", command=gestionar_ejemplos, width=40).pack(pady=5)
tk.Button(root, text="5. Guardar datos manualmente", command=guardar_manual, width=40).pack(pady=5)

tk.Button(root, text="Salir", command=lambda: (guardar_datos(), root.quit()), width=40).pack(pady=20)

root.mainloop()
