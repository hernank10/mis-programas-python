import tkinter as tk
from tkinter import ttk, messagebox

# Base de datos de la misión (simula JSON)
mision = []

# Función para agregar oración
def agregar_oracion():
    texto = entrada_oracion.get("1.0", tk.END).strip()
    tipo = tipo_var.get()
    if texto and tipo:
        mision.append({"oracion": texto, "tipo": tipo})
        actualizar_lista()
        entrada_oracion.delete("1.0", tk.END)
        tipo_var.set("")
    else:
        messagebox.showwarning("Campos incompletos", "Debes ingresar una oración y seleccionar su tipo.")

# Función para actualizar la lista visual
def actualizar_lista():
    lista.delete(0, tk.END)
    for i, item in enumerate(mision, 1):
        lista.insert(tk.END, f"{i}. {item['oracion']} → {item['tipo']}")

# Función para exportar misión
def exportar_mision():
    print("\n📦 Misión exportada:")
    for item in mision:
        print(item)

# Interfaz principal
ventana = tk.Tk()
ventana.title("Editor de Misiones Gramaticales")
ventana.geometry("600x500")

tk.Label(ventana, text="📝 Escribe una oración compuesta:", font=("Arial", 12)).pack(pady=5)
entrada_oracion = tk.Text(ventana, height=3, width=70)
entrada_oracion.pack()

tk.Label(ventana, text="📌 Selecciona el tipo de oración:", font=("Arial", 12)).pack(pady=5)
tipo_var = tk.StringVar()
menu_tipo = ttk.Combobox(ventana, textvariable=tipo_var, state="readonly")
menu_tipo["values"] = ["coordinada", "subordinada", "yuxtapuesta"]
menu_tipo.pack()

tk.Button(ventana, text="➕ Agregar a la misión", command=agregar_oracion).pack(pady=10)

tk.Label(ventana, text="📋 Oraciones en la misión:", font=("Arial", 12)).pack()
lista = tk.Listbox(ventana, width=80, height=10)
lista.pack()

tk.Button(ventana, text="📤 Exportar misión (consola)", command=exportar_mision).pack(pady=10)

ventana.mainloop()
