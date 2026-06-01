import tkinter as tk
from tkinter import messagebox

parrafos_guardados = []

def mostrar_teoria():
    texto_teoria = """
📘 LECCIÓN 6 – PÁRRAFO ARGUMENTATIVO COMPLETO

Un párrafo argumentativo bien construido tiene tres partes esenciales:

1. 💡 Idea principal (Tesis): postura clara del autor.
2. 📚 Desarrollo: razones, datos, conectores, explicaciones.
3. 🎯 Cierre: refuerza o proyecta la postura.

Ejemplo:
"La lectura crítica debe enseñarse desde temprana edad, ya que permite que los estudiantes distingan entre hechos y opiniones. A través del análisis textual, aprenden a identificar falacias y sesgos ideológicos. Esta habilidad fortalece el pensamiento autónomo y prepara para la participación social."
"""
    salida_texto.delete(1.0, tk.END)
    salida_texto.insert(tk.END, texto_teoria)

def guardar_parrafo():
    idea = entrada_idea.get().strip()
    desarrollo = entrada_desarrollo.get("1.0", tk.END).strip()
    cierre = entrada_cierre.get().strip()

    if idea and desarrollo and cierre:
        parrafo = f"{idea} {desarrollo} {cierre}"
        parrafos_guardados.append(parrafo)
        messagebox.showinfo("✅ Guardado", "¡Párrafo guardado correctamente!")
        entrada_idea.delete(0, tk.END)
        entrada_desarrollo.delete("1.0", tk.END)
        entrada_cierre.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Campos incompletos", "Por favor completa las tres partes del párrafo.")

def mostrar_parrafos():
    salida_texto.delete(1.0, tk.END)
    if parrafos_guardados:
        for idx, p in enumerate(parrafos_guardados, 1):
            salida_texto.insert(tk.END, f"{idx}. {p}\n\n")
    else:
        salida_texto.insert(tk.END, "📭 Aún no hay párrafos guardados.")

# Ventana principal
root = tk.Tk()
root.title("Sintaxis Quest EDU – Lección 6 Preuniversitario")
root.geometry("750x600")

frame_titulo = tk.Frame(root)
frame_titulo.pack(pady=10)
tk.Label(frame_titulo, text="✍️ Párrafo Argumentativo – Estructura Completa", font=("Helvetica", 16)).pack()

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="💡 Idea principal:", anchor="w").pack(fill="x")
entrada_idea = tk.Entry(frame_inputs, width=80)
entrada_idea.pack()

tk.Label(frame_inputs, text="📚 Desarrollo lógico:", anchor="w").pack(fill="x")
entrada_desarrollo = tk.Text(frame_inputs, height=5, width=80)
entrada_desarrollo.pack()

tk.Label(frame_inputs, text="🎯 Cierre reflexivo:", anchor="w").pack(fill="x")
entrada_cierre = tk.Entry(frame_inputs, width=80)
entrada_cierre.pack()

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="📘 Ver teoría", command=mostrar_teoria).pack(side="left", padx=10)
tk.Button(frame_botones, text="✅ Guardar párrafo", command=guardar_parrafo).pack(side="left", padx=10)
tk.Button(frame_botones, text="📄 Ver párrafos guardados", command=mostrar_parrafos).pack(side="left", padx=10)

tk.Label(root, text="🧾 Área de teoría y párrafos", font=("Helvetica", 12)).pack()
salida_texto = tk.Text(root, wrap="word", height=12, width=90, bg="#f0f0f0")
salida_texto.pack()

root.mainloop()
