import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import json
import os
import random

ARCHIVO = "oraciones.json"
MAX_ORACIONES = 100

# Funciones de almacenamiento
def cargar_oraciones():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_oraciones(oraciones):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(oraciones, f, ensure_ascii=False, indent=2)

# Clase principal de la app
class PracticaVerbosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📘 Práctica de Verbos con Diptongos")
        self.oraciones = cargar_oraciones()

        self.inicio_ui()

    def inicio_ui(self):
        self.limpiar_pantalla()

        titulo = tk.Label(self.root, text="📘 Práctica Interactiva de Verbos Vocálicos 📘",
                          font=("Helvetica", 16, "bold"), fg="blue")
        titulo.pack(pady=10)

        btn_agregar = tk.Button(self.root, text="➕ Agregar Oración", command=self.agregar_oracion)
        btn_practicar = tk.Button(self.root, text="✅ Practicar", command=self.practicar)
        btn_ver = tk.Button(self.root, text="👁️ Ver Oraciones", command=self.ver_oraciones)
        btn_salir = tk.Button(self.root, text="Salir", command=self.root.quit)

        for btn in (btn_agregar, btn_practicar, btn_ver, btn_salir):
            btn.pack(pady=5, ipadx=10)

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def agregar_oracion(self):
        if len(self.oraciones) >= MAX_ORACIONES:
            messagebox.showwarning("Límite", "⚠️ Ya has agregado 100 oraciones.")
            return

        oracion = simpledialog.askstring("Nueva oración", "Escribe la oración con el verbo entre paréntesis:")
        respuesta = simpledialog.askstring("Respuesta", "Escribe la forma correcta del verbo:")
        regla = simpledialog.askstring("Regla", "Escribe la regla ortográfica:")

        if oracion and respuesta and regla:
            nueva = {"oracion": oracion, "respuesta": respuesta, "regla": regla}
            self.oraciones.append(nueva)
            guardar_oraciones(self.oraciones)
            messagebox.showinfo("Guardado", "✅ Oración guardada correctamente.")

    def ver_oraciones(self):
        self.limpiar_pantalla()

        tk.Label(self.root, text="📚 Lista de Oraciones Guardadas", font=("Helvetica", 14, "bold")).pack(pady=10)
        texto = scrolledtext.ScrolledText(self.root, width=80, height=20)
        texto.pack()

        if not self.oraciones:
            texto.insert(tk.END, "No hay oraciones guardadas.")
        else:
            for i, o in enumerate(self.oraciones, 1):
                texto.insert(tk.END, f"{i}. {o['oracion']} → {o['respuesta']} ({o['regla']})\n")

        tk.Button(self.root, text="🔙 Volver al menú", command=self.inicio_ui).pack(pady=10)

    def practicar(self):
        if not self.oraciones:
            messagebox.showinfo("Sin datos", "No hay oraciones para practicar.")
            return

        self.limpiar_pantalla()
        self.ejercicios = random.sample(self.oraciones, len(self.oraciones))
        self.aciertos = 0
        self.ej_index = 0

        self.label_oracion = tk.Label(self.root, font=("Helvetica", 14), wraplength=500)
        self.label_oracion.pack(pady=10)

        self.entry_respuesta = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_respuesta.pack(pady=5)

        self.btn_verificar = tk.Button(self.root, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=5)

        self.label_resultado = tk.Label(self.root, font=("Helvetica", 12))
        self.label_resultado.pack(pady=5)

        self.mostrar_siguiente()

    def mostrar_siguiente(self):
        if self.ej_index < len(self.ejercicios):
            self.label_resultado.config(text="")
            ejercicio = self.ejercicios[self.ej_index]
            self.label_oracion.config(text=f"Oración: {ejercicio['oracion']}")
            self.entry_respuesta.delete(0, tk.END)
        else:
            self.label_oracion.config(text="🎯 Práctica finalizada")
            self.entry_respuesta.pack_forget()
            self.btn_verificar.pack_forget()
            self.label_resultado.config(text=f"✅ Respuestas correctas: {self.aciertos}/{len(self.ejercicios)}")
            tk.Button(self.root, text="🔙 Volver al menú", command=self.inicio_ui).pack(pady=10)

    def verificar_respuesta(self):
        respuesta_usuario = self.entry_respuesta.get().strip()
        ejercicio = self.ejercicios[self.ej_index]

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            self.label_resultado.config(text="✅ Correcto", fg="green")
            self.aciertos += 1
        else:
            self.label_resultado.config(
                text=f"❌ Incorrecto. Respuesta: {ejercicio['respuesta']} — Regla: {ejercicio['regla']}", fg="red"
            )

        self.ej_index += 1
        self.root.after(1500, self.mostrar_siguiente)


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = PracticaVerbosApp(root)
    root.mainloop()
