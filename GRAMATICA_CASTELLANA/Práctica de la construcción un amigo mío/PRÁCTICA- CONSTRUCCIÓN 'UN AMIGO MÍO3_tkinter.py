import tkinter as tk
from tkinter import messagebox
import re

class PracticaConstruccion:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica: 'un amigo mío'")
        self.errores = []

        self.label = tk.Label(root, text="🧠 Práctica de la construcción: un amigo mío", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        self.teoria_btn = tk.Button(root, text="Ver Teoría", command=self.mostrar_teoria)
        self.teoria_btn.pack(pady=5)

        self.ejemplos_btn = tk.Button(root, text="Ver Ejemplos", command=self.mostrar_ejemplos)
        self.ejemplos_btn.pack(pady=5)

        self.entrada_label = tk.Label(root, text="✍️ Escribe 3 oraciones usando la estructura:")
        self.entrada_label.pack(pady=5)

        self.entries = [tk.Entry(root, width=60) for _ in range(3)]
        for entry in self.entries:
            entry.pack(pady=2)

        self.verificar_btn = tk.Button(root, text="Verificar", command=self.verificar_respuestas)
        self.verificar_btn.pack(pady=10)

        self.repaso_btn = tk.Button(root, text="Revisar errores", command=self.revisar_errores)
        self.repaso_btn.pack(pady=5)

    def mostrar_teoria(self):
        teoria = (
            "La construcción 'un amigo mío' es típica del español.\n"
            "Estructura: artículo + sustantivo + posesivo pospuesto.\n"
            "Ejemplo: un amigo mío, una prima suya, unos colegas nuestros.\n"
            "Equivale a: 'one of my friends' en inglés."
        )
        messagebox.showinfo("📘 Teoría", teoria)

    def mostrar_ejemplos(self):
        ejemplos = (
            "• Un amigo mío vive en Barcelona.\n"
            "• Una prima suya trabaja en una embajada.\n"
            "• Un profesor nuestro escribió ese libro.\n"
            "• Un vecino tuyo me saludó ayer.\n"
            "• Una colega mía viaja mucho por trabajo."
        )
        messagebox.showinfo("📚 Ejemplos", ejemplos)

    def verificar_respuestas(self):
        self.errores.clear()
        patron = re.compile(r'\b(un|una|unos|unas)\s+\w+\s+(mío|mía|míos|mías|tuyo|tuya|tuyos|tuyas|suyo|suya|suyos|suyas|nuestro|nuestra|nuestros|nuestras)\b', re.IGNORECASE)
        resultados = []
        for i, entry in enumerate(self.entries, 1):
            texto = entry.get().strip()
            if patron.search(texto):
                resultados.append(f"{i}. ✔️ Correcta: {texto}")
            else:
                resultados.append(f"{i}. ❌ Incorrecta: {texto}")
                self.errores.append(texto)
        messagebox.showinfo("✅ Resultados", "\n".join(resultados))

    def revisar_errores(self):
        if not self.errores:
            messagebox.showinfo("🎉 ¡Bien!", "No hay errores que revisar.")
            return
        repaso = "🔁 REPASO DE ERRORES:\n\n"
        for i, err in enumerate(self.errores, 1):
            repaso += f"{i}. {err}\n"
        messagebox.showinfo("Errores a corregir", repaso)

# Ejecutar interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = PracticaConstruccion(root)
    root.mainloop()

import random

def generar_ejemplos(self):
    articulos = ['Un', 'Una', 'Unos', 'Unas']
    sustantivos = ['amigo', 'prima', 'vecino', 'compañero', 'colega', 'profesor', 'alumno', 'cliente', 'doctor', 'abogado']
    posesivos = ['mío', 'mía', 'tuyo', 'tuya', 'suyo', 'suya', 'nuestro', 'nuestra', 'míos', 'tuyos', 'suyos', 'nuestros']
    verbos = ['vive en Madrid.', 'trabaja aquí.', 'viaja mucho.', 'estudia derecho.', 'enseña francés.',
              'me llamó ayer.', 'saludó en la calle.', 'es muy amable.', 'tiene una casa grande.', 'ayuda a los demás.']

    ejemplos = []
    for _ in range(100):
        art = random.choice(articulos)
        sust = random.choice(sustantivos)
        pose = random.choice(posesivos)
        verbo = random.choice(verbos)
        oracion = f"{art} {sust} {pose} {verbo}"
        ejemplos.append(oracion)

    with open("100_ejemplos.txt", "w", encoding="utf-8") as f:
        for e in ejemplos:
            f.write(e + "\n")

    messagebox.showinfo("📁 Ejemplos Generados", "Se han generado 100 ejemplos.\nGuardados en '100_ejemplos.txt'.")

# Añadir botón en el método __init__ del programa principal:

self.generar_btn = tk.Button(root, text="Generar y guardar 100 ejemplos", command=self.generar_ejemplos)
self.generar_btn.pack(pady=5)

# Asegúrate de añadir este método dentro de la clase PracticaConstruccion:
PracticaConstruccion.generar_ejemplos = generar_ejemplos
