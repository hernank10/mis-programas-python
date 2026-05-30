import random
import tkinter as tk
from tkinter import messagebox

heteronimos = [
    ("padre", "madre"), ("hombre", "mujer"), ("yerno", "nuera"), ("caballo", "yegua"),
    ("toro", "vaca"), ("carnero", "oveja"), ("conde", "condesa"), ("rey", "reina"),
    ("príncipe", "princesa"), ("monje", "monja"), ("poeta", "poetisa"), ("héroe", "heroína"),
    ("zar", "zarina"), ("duque", "duquesa"), ("marqués", "marquesa"), ("abad", "abadesa"),
    ("emperador", "emperatriz"), ("actor", "actriz"), ("sacerdote", "sacerdotisa"),
    ("dios", "diosa"), ("gobernador", "gobernadora"), ("presidente", "presidenta"),
    ("cónsul", "cónsul"), ("barón", "baronesa"), ("hechicero", "hechicera"),
    ("brujo", "bruja"), ("alcalde", "alcaldesa"), ("testigo", "testigo"),
    ("cliente", "clienta"), ("sirviente", "sirvienta"), ("asistente", "asistenta"),
    ("amo", "ama"), ("juez", "jueza"), ("infante", "infanta"), ("vidente", "vidente"),
    ("soldado", "soldado"), ("mártir", "mártir"), ("cantante", "cantante"),
    ("prófugo", "prófuga"), ("prisionero", "prisionera"), ("huérfano", "huérfana"),
    ("zorro", "zorra"), ("león", "leona"), ("tigre", "tigresa"), ("gallo", "gallina"),
    ("ratón", "rata"), ("ciervo", "cierva")
]

ejemplos_usuario = []

def mostrar_teoria():
    messagebox.showinfo("Teoría", "Los nombres heterónimos tienen formas diferentes para masculino y femenino.\nEjemplo: 'padre' y 'madre'.")

def practicar_completacion():
    def siguiente_ejercicio():
        palabra_masculina, palabra_femenina = random.choice(heteronimos)
        etiqueta.config(text=f"Mi {palabra_masculina} y mi ____ me enseñaron grandes valores.")
        entrada.delete(0, tk.END)
        entrada.focus()
        boton_verificar.config(command=lambda: verificar_respuesta(palabra_femenina))
    
    def verificar_respuesta(respuesta_correcta):
        respuesta = entrada.get().strip().lower()
        if respuesta == respuesta_correcta:
            messagebox.showinfo("Correcto", "✔ Has completado la oración correctamente.")
        else:
            messagebox.showerror("Incorrecto", f"✖ La respuesta correcta era '{respuesta_correcta}'.")
        siguiente_ejercicio()
    
    ventana_completacion = tk.Toplevel(root)
    ventana_completacion.title("Ejercicio de Completación")
    etiqueta = tk.Label(ventana_completacion)
    etiqueta.pack()
    entrada = tk.Entry(ventana_completacion)
    entrada.pack()
    boton_verificar = tk.Button(ventana_completacion, text="Verificar")
    boton_verificar.pack()
    siguiente_ejercicio()

def practicar_redaccion():
    if len(ejemplos_usuario) >= 100:
        messagebox.showwarning("Límite alcanzado", "Has alcanzado el límite de 100 ejemplos guardados.")
        return
    
    palabra_masculina, palabra_femenina = random.choice(heteronimos)
    def guardar_ejemplo():
        ejemplos_usuario.append((entrada1.get(), entrada2.get()))
        messagebox.showinfo("Guardado", "✔ Tus ejemplos han sido guardados.")
        ventana_redaccion.destroy()
    
    ventana_redaccion = tk.Toplevel(root)
    ventana_redaccion.title("Ejercicio de Redacción")
    tk.Label(ventana_redaccion, text=f"Escribe una oración usando la palabra: {palabra_masculina}").pack()
    entrada1 = tk.Entry(ventana_redaccion)
    entrada1.pack()
    tk.Label(ventana_redaccion, text=f"Ahora escribe una oración usando la palabra: {palabra_femenina}").pack()
    entrada2 = tk.Entry(ventana_redaccion)
    entrada2.pack()
    tk.Button(ventana_redaccion, text="Guardar", command=guardar_ejemplo).pack()

def mostrar_ejemplos_guardados():
    ejemplos_texto = "\n".join([f"{i+1}. {o1}\n   {o2}" for i, (o1, o2) in enumerate(ejemplos_usuario)])
    if not ejemplos_usuario:
        ejemplos_texto = "No hay ejemplos guardados aún."
    messagebox.showinfo("Ejemplos Guardados", ejemplos_texto)

root = tk.Tk()
root.title("Práctica de Nombres Heterónimos")

tk.Label(root, text="Práctica de nombres heterónimos", font=("Arial", 14)).pack()
tk.Button(root, text="Ver Teoría", command=mostrar_teoria).pack()
tk.Button(root, text="Ejercicio de Completación", command=practicar_completacion).pack()
tk.Button(root, text="Ejercicio de Redacción", command=practicar_redaccion).pack()
tk.Button(root, text="Ver Ejemplos Guardados", command=mostrar_ejemplos_guardados).pack()
tk.Button(root, text="Salir", command=root.quit).pack()

root.mainloop()
