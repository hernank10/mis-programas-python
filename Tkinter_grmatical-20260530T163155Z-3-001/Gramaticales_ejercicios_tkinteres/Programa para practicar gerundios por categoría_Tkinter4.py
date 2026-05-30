import tkinter as tk
from tkinter import messagebox
import re

# Lista inicial de ejemplos (puedes ampliar aquí luego)
ejemplos = [
    # ① Ejemplos normales
    "María llegó corriendo.",
    "Pedro se fue llorando.",
    "El perro entró ladrando.",
    "El maestro explicó sonriendo.",
    "Mi amigo contestó riendo.",
    # Añade más aquí o sigue cargando las 100 que ya tienes
]

# Función para subrayar gerundios
def subrayar_gerundios(text_widget, texto):
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, texto)

    gerundios = re.finditer(r'\b\w+(ando|iendo|yendo)\b', texto)
    for match in gerundios:
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        text_widget.tag_add("subrayado", start, end)

# Función para mostrar ejemplo seleccionado
def mostrar_ejemplo(event):
    seleccion = lista.curselection()
    if seleccion:
        indice = seleccion[0]
        texto = ejemplos[indice]
        subrayar_gerundios(texto_ejemplo, texto)

# Función para copiar texto
def copiar_texto():
    texto = texto_ejemplo.get("1.0", tk.END).strip()
    if texto:
        root.clipboard_clear()
        root.clipboard_append(texto)
        messagebox.showinfo("Copiado", "¡Ejemplo copiado al portapapeles!")

# Función para agregar nuevo ejemplo
def agregar_ejemplo():
    nuevo = entrada_nuevo.get().strip()
    if nuevo:
        ejemplos.append(nuevo)
        lista.insert(tk.END, nuevo)
        entrada_nuevo.delete(0, tk.END)
        messagebox.showinfo("Agregado", "¡Nuevo ejemplo añadido!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplos de Gerundios Interactivos")

# Estilos
root.geometry("700x500")
root.config(bg="#f0f0f0")

# Lista de ejemplos
lista = tk.Listbox(root, width=50, height=20)
lista.pack(side=tk.LEFT, padx=10, pady=10)

for ejemplo in ejemplos:
    lista.insert(tk.END, ejemplo)

lista.bind('<<ListboxSelect>>', mostrar_ejemplo)

# Área de texto para mostrar el ejemplo
texto_ejemplo = tk.Text(root, width=50, height=5, wrap="word", font=("Arial", 14))
texto_ejemplo.pack(pady=10)

# Subrayado
texto_ejemplo.tag_configure("subrayado", underline=True, foreground="blue")

# Botón de copiar
boton_copiar = tk.Button(root, text="Copiar Ejemplo", command=copiar_texto, bg="#4caf50", fg="white")
boton_copiar.pack(pady=5)

# Entrada para nuevo ejemplo
entrada_nuevo = tk.Entry(root, width=40)
entrada_nuevo.pack(pady=5)

# Botón para agregar nuevo ejemplo
boton_agregar = tk.Button(root, text="Agregar Ejemplo", command=agregar_ejemplo, bg="#2196f3", fg="white")
boton_agregar.pack(pady=5)

root.mainloop()
