import tkinter as tk
from tkinter import messagebox
import random

# Diccionario de consejos por categoría
consejos = {
    "Diseño pedagógico": [
        "Divide el curso en niveles progresivos según la dificultad.",
        "Establece objetivos de aprendizaje claros para cada lección.",
        "Utiliza una rúbrica común para evaluar ejercicios.",
        "Incluye actividades prácticas en cada tema."
    ],
    "Desarrollo técnico": [
        "Usa Python para prototipos rápidos.",
        "Usa Tkinter o PyQt para interfaces de escritorio.",
        "Usa Kivy para apps móviles.",
        "Aplica POO para escalabilidad del código."
    ],
    "Distribución multiplataforma": [
        "Compila para Android con buildozer o Kotlin.",
        "Usa PyInstaller para apps de escritorio.",
        "Adapta la UI según el sistema operativo.",
        "Documenta dependencias necesarias."
    ],
}

class PracticaConsejosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Práctica de Consejos")
        self.categoria_actual = None
        self.lista_actual = []
        self.consejo_index = 0
        self.aciertos = 0
        self.errores = []

        self.menu_principal()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Selecciona una categoría:", font=("Arial", 16)).pack(pady=10)

        for categoria in consejos:
            tk.Button(self.root, text=categoria, width=30, command=lambda c=categoria: self.mostrar_consejos(c)).pack(pady=5)

        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

    def mostrar_consejos(self, categoria):
        self.limpiar_ventana()
        self.categoria_actual = categoria
        tk.Label(self.root, text=f"📘 Consejos de: {categoria}", font=("Arial", 14)).pack(pady=10)

        for consejo in consejos[categoria]:
            tk.Label(self.root, text=f"- {consejo}", wraplength=500, justify="left").pack(anchor="w", padx=20)

        tk.Button(self.root, text="Practicar esta categoría", command=self.iniciar_practica).pack(pady=10)
        tk.Button(self.root, text="⬅ Volver", command=self.menu_principal).pack()

    def iniciar_practica(self):
        self.lista_actual = consejos[self.categoria_actual][:]
        random.shuffle(self.lista_actual)
        self.consejo_index = 0
        self.aciertos = 0
        self.errores = []
        self.mostrar_practica()

    def mostrar_practica(self):
        self.limpiar_ventana()
        if self.consejo_index >= len(self.lista_actual):
            self.mostrar_resultado()
            return

        self.consejo_actual = self.lista_actual[self.consejo_index]

        tk.Label(self.root, text=f"Escribe el siguiente consejo ({self.consejo_index+1}/{len(self.lista_actual)}):", font=("Arial", 12)).pack(pady=10)
        self.entry_respuesta = tk.Entry(self.root, width=70)
        self.entry_respuesta.pack(pady=10)
        self.entry_respuesta.focus()

        tk.Button(self.root, text="Verificar", command=self.verificar_respuesta).pack(pady=5)

    def verificar_respuesta(self):
        respuesta = self.entry_respuesta.get().strip()
        correcto = self.consejo_actual.strip()

        if respuesta.lower() == correcto.lower():
            self.aciertos += 1
            messagebox.showinfo("✅ Correcto", "¡Muy bien!")
        else:
            self.errores.append((respuesta, correcto))
            messagebox.showwarning("❌ Incorrecto", f"Tu respuesta:\n{respuesta}\n\nCorrecto era:\n{correcto}")

        self.consejo_index += 1
        self.mostrar_practica()

    def mostrar_resultado(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="📊 Resultado final", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"Aciertos: {self.aciertos}/{len(self.lista_actual)}").pack()

        if self.errores:
            tk.Label(self.root, text="❗ Errores:", font=("Arial", 12, "bold")).pack(pady=10)
            for i, (resp, cor) in enumerate(self.errores, 1):
                tk.Label(self.root, text=f"{i}. Tú: {resp}\n   Correcto: {cor}", wraplength=500, justify="left").pack(anchor="w", padx=20)

        tk.Button(self.root, text="Volver al menú principal", command=self.menu_principal).pack(pady=10)


# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    app = PracticaConsejosApp(root)
    root.mainloop()
