import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

# ------------------------------
# ESTRUCTURAS DE CONSEJOS Y EJEMPLOS
# ------------------------------
consejos_modelo = {
    "Temporales": ["Cuando llegues, avísame.", "Después que saliste, te llamé."],
    "Locativas": ["Vive donde nacieron sus abuelos.", "Se sentaron en donde había sombra."],
    "Modales": ["Hazlo como te dije.", "Cocinó según la receta."],
    "Combinadas": ["Te llamé cuando llegué donde tú estás.", "Volverá cuando lo decida, como siempre."]
}

ejemplos_100 = {
    "Temporales": ["Cuando amaneció, salimos a correr."],
    "Locativas": ["Estaba donde lo vi ayer."],
    "Modales": ["Actuó como si supiera todo."],
    "Combinadas": ["Cuando llovía, donde vivíamos, se inundaba todo."]
}

# ------------------------------
# PROGRESO
# ------------------------------
def cargar_progreso(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def guardar_progreso(progreso, archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(progreso, f, ensure_ascii=False, indent=4)

# ------------------------------
# APP PRINCIPAL CON TKINTER
# ------------------------------
class PracticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Consejos y Ejemplos")
        self.root.geometry("800x500")

        self.tipo = None
        self.categoria = None
        self.ejemplo_actual = None
        self.inicio_tiempo = None

        self.progreso_modelo = cargar_progreso("progreso_modelo.json")
        self.progreso_100 = cargar_progreso("progreso_100.json")

        self.niveles = {"Fácil": 30, "Medio": 20, "Difícil": 10}
        self.dificultad = tk.StringVar(value="Fácil")

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Selecciona el tipo de práctica:", fg="blue", font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.root, text="Consejos Modelo", command=lambda: self.seleccionar_categoria("modelo"), width=25).pack()
        tk.Button(self.root, text="100 Ejemplos", command=lambda: self.seleccionar_categoria("ejemplo"), width=25).pack(pady=5)

        tk.Label(self.root, text="Nivel de dificultad (cronómetro):").pack()
        for nivel in self.niveles:
            tk.Radiobutton(self.root, text=nivel, variable=self.dificultad, value=nivel).pack(anchor="w")

        self.texto = tk.Text(self.root, height=10, font=("Arial", 12))
        self.texto.pack(pady=10)

        self.respuesta_entry = tk.Entry(self.root, font=("Arial", 12))
        self.respuesta_entry.pack()
        tk.Button(self.root, text="Verificar", command=self.verificar_respuesta).pack(pady=5)

        self.label_cronometro = tk.Label(self.root, text="")
        self.label_cronometro.pack()

    def seleccionar_categoria(self, tipo):
        self.tipo = tipo
        estructura = consejos_modelo if tipo == "modelo" else ejemplos_100
        categorias = list(estructura.keys())
        self.categoria = simpledialog.askstring("Categoría", f"Elige una categoría: {', '.join(categorias)}")
        if self.categoria in estructura:
            self.mostrar_ejemplo()
        else:
            messagebox.showwarning("Categoría no válida", "Elige una categoría válida.")

    def mostrar_ejemplo(self):
        estructura = consejos_modelo if self.tipo == "modelo" else ejemplos_100
        progreso = self.progreso_modelo if self.tipo == "modelo" else self.progreso_100
        ejemplos_disponibles = [e for e in estructura[self.categoria] if e not in progreso.get(self.categoria, [])]

        if not ejemplos_disponibles:
            messagebox.showinfo("Completado", "Ya completaste esta categoría.")
            return

        self.ejemplo_actual = random.choice(ejemplos_disponibles)
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, f"{Fore.GREEN}Escribe esta oración exactamente igual:
➡️ {self.ejemplo_actual}")
        self.inicio_tiempo = time.time()
        self.label_cronometro.config(text="Tiempo restante: {} segundos".format(self.niveles[self.dificultad.get()]))
        self.root.after(1000, self.actualizar_cronometro)

    def actualizar_cronometro(self):
        if not self.inicio_tiempo:
            return
        tiempo_restante = self.niveles[self.dificultad.get()] - int(time.time() - self.inicio_tiempo)
        if tiempo_restante <= 0:
            self.label_cronometro.config(text="⏰ Tiempo agotado!")
            self.inicio_tiempo = None
        else:
            self.label_cronometro.config(text="Tiempo restante: {} segundos".format(tiempo_restante))
            self.root.after(1000, self.actualizar_cronometro)

    def verificar_respuesta(self):
        respuesta = self.respuesta_entry.get().strip()
        if not respuesta:
            messagebox.showwarning("Sin respuesta", "Escribe algo para verificar.")
            return

        if respuesta.lower() == self.ejemplo_actual.lower():
            nuevo = simpledialog.askstring("Nuevo ejemplo", "Escribe una oración similar:")
            if nuevo:
                progreso = self.progreso_modelo if self.tipo == "modelo" else self.progreso_100
                archivo = "progreso_modelo.json" if self.tipo == "modelo" else "progreso_100.json"

                progreso.setdefault(self.categoria, []).append(self.ejemplo_actual)
                progreso[self.categoria].append(nuevo)
                guardar_progreso(progreso, archivo)
                messagebox.showinfo("Correcto", "✅ Bien hecho. Ejemplo guardado.")
                self.mostrar_ejemplo()
        else:
            messagebox.showerror("Incorrecto", "❌ Revisa la ortografía o puntuación.")

# ------------------------------
# INICIAR APP
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PracticaApp(root)
    root.mainloop()
