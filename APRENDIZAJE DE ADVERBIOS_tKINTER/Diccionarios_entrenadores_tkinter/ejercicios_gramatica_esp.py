import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json

# Cargar ejercicios desde archivo JSON
with open("ejercicios_gramatica_esp.json", "r", encoding="utf-8") as f:
    ejercicios_tematicos = json.load(f)

class GramaticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Gramática Española")
        self.aciertos = 0
        self.errores = 0

        # Botones
        tk.Button(root, text="Ejercicio Temático", command=self.ejercicio_tematico, width=30).pack(pady=10)
        tk.Button(root, text="Ver Estadísticas", command=self.mostrar_estadisticas, width=30).pack(pady=10)
        tk.Button(root, text="Salir", command=root.quit, width=30).pack(pady=10)

    def ejercicio_tematico(self):
        categorias_disponibles = "\n- " + "\n- ".join(ejercicios_tematicos.keys())
        tema = simpledialog.askstring("Categorías disponibles", f"Elige una categoría:{categorias_disponibles}")

        if tema in ejercicios_tematicos:
            ejercicio = random.choice(ejercicios_tematicos[tema])
            oracion_mal = ejercicio["incorrecta"]
            oracion_bien = ejercicio["correcta"]
            explicacion = ejercicio["explicacion"]

            respuesta = simpledialog.askstring("Corrige la oración", f"Categoría: {tema}\n\nCorrige esta oración:\n{oracion_mal}")

            if respuesta:
                if respuesta.strip().lower() == oracion_bien.lower():
                    messagebox.showinfo("Corrección", f"✅ ¡Correcto!\n\n📘 Explicación:\n{explicacion}")
                    self.aciertos += 1
                else:
                    self.errores += 1
                    messagebox.showinfo("Corrección", f"❌ Incorrecto.\n✔ Corrección esperada:\n{oracion_bien}\n\n📘 Explicación:\n{explicacion}")
        else:
            messagebox.showwarning("Categoría inválida", "❌ Esa categoría no existe o está mal escrita.")

    def mostrar_estadisticas(self):
        total = self.aciertos + self.errores
        messagebox.showinfo("Estadísticas", f"✅ Aciertos: {self.aciertos}\n❌ Errores: {self.errores}\n📊 Total intentos: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GramaticaApp(root)
    root.mainloop()
