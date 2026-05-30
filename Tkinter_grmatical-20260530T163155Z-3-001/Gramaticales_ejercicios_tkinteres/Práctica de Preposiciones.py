import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

archivo_salida = "mis_oraciones_categorizadas.txt"

categorias = {
    "1": ("Lugar", "El libro está ___ la mesa.", "sobre"),
    "2": ("Tiempo", "Nos vemos ___ la tarde.", "por"),
    "3": ("Modo", "Resolví el problema ___ paciencia.", "con"),
    "4": ("Causa", "Suspiraba ___ amor.", "por"),
    "5": ("Finalidad", "Estudia ___ aprender.", "para"),
    "6": ("Compañía", "Fue al cine ___ su hermana.", "con"),
    "7": ("Medio", "Viajamos ___ tren.", "en"),
    "8": ("Dirección", "Salió ___ el mercado.", "hacia"),
    "9": ("Posesión", "El sombrero ___ Pedro es rojo.", "de"),
    "10": ("Tema o materia", "Hablamos ___ política internacional.", "sobre")
}

def practicar_categoria(clave):
    nombre, ejemplo, correcta = categorias[clave]
    respuesta = simpledialog.askstring("Completa la oración", f"🧠 Categoría: {nombre}\n\nEjemplo: {ejemplo}\n\nEscribe la preposición correcta:")

    if respuesta:
        if respuesta.strip().lower() == correcta:
            messagebox.showinfo("¡Correcto!", f"✅ ¡Bien hecho!\nOración completa: {ejemplo.replace('___', correcta)}")
        else:
            messagebox.showwarning("Incorrecto", f"❌ La respuesta correcta era '{correcta}'.\nOración: {ejemplo.replace('___', correcta)}")
        
        oracion_usuario = simpledialog.askstring("Tu oración", f"✍️ Ahora escribe tu propia oración usando la preposición '{correcta}':")
        if oracion_usuario:
            with open(archivo_salida, "a", encoding="utf-8") as archivo:
                archivo.write(f"{nombre.upper()} ({correcta}): {oracion_usuario.strip()}\n")
            messagebox.showinfo("Guardado", "✅ Tu oración fue guardada.")

def mostrar_oraciones_guardadas():
    try:
        with open(archivo_salida, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        contenido = "Aún no has guardado ninguna oración."

    ventana_oraciones = tk.Toplevel()
    ventana_oraciones.title("📘 Oraciones Guardadas")
    texto = scrolledtext.ScrolledText(ventana_oraciones, width=70, height=20, font=("Arial", 12))
    texto.insert(tk.END, contenido)
    texto.config(state=tk.DISABLED)
    texto.pack(padx=10, pady=10)

def crear_menu_principal():
    root = tk.Tk()
    root.title("🧠 Práctica de Preposiciones")

    etiqueta = tk.Label(root, text="Selecciona una categoría para practicar:", font=("Arial", 14))
    etiqueta.pack(pady=10)

    for clave, (nombre, _, _) in categorias.items():
        btn = tk.Button(root, text=f"{clave}. {nombre}", width=40, font=("Arial", 12),
                        command=lambda c=clave: practicar_categoria(c))
        btn.pack(pady=2)

    btn_ver_todo = tk.Button(root, text="📄 Ver oraciones guardadas", font=("Arial", 12), command=mostrar_oraciones_guardadas)
    btn_ver_todo.pack(pady=10)

    btn_salir = tk.Button(root, text="❌ Salir", font=("Arial", 12), command=root.destroy)
    btn_salir.pack(pady=5)

    root.mainloop()

crear_menu_principal()
