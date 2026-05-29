import tkinter as tk
from tkinter import ttk, messagebox

# Ejemplo de datos: agrega más hasta completar los 100
consejos = [
    {"nro": 1, "consejo": "Usa 'yo' como sujeto de la oración.",
     "ejemplo": "Yo ya llegué, ¿y tú?", "categoría": "gramatical"},
    {"nro": 2, "consejo": "Emplea 'yo' solo cuando sea necesario aclarar el sujeto.",
     "ejemplo": "Yo llamé ayer a tu casa.", "categoría": "sintáctico"},
    {"nro": 3, "consejo": "No repitas innecesariamente 'yo' en una oración.",
     "ejemplo": "Yo ya no lloro por eso.", "categoría": "discursivo"},
]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("100 Consejos del Uso del 'Yo'")

        self.index = 0
        self.total = len(consejos)
        self.ejercicios_completados = 0

        self.titulo = tk.Label(root, text="Consejo sobre el uso de 'yo'", font=("Helvetica", 16, "bold"))
        self.titulo.pack(pady=10)

        self.texto = tk.Label(root, text="", wraplength=500, justify="left", font=("Helvetica", 12))
        self.texto.pack(pady=5)

        self.entry = tk.Entry(root, width=70)
        self.entry.pack(pady=5)

        self.btn_siguiente = tk.Button(root, text="Enviar ejemplo", command=self.verificar)
        self.btn_siguiente.pack(pady=10)

        self.progress = ttk.Progressbar(root, length=400, mode='determinate', maximum=self.total)
        self.progress.pack(pady=5)

        self.estado = tk.Label(root, text=f"0 de {self.total} completados", font=("Helvetica", 10))
        self.estado.pack()

        self.mostrar_consejo()

    def mostrar_consejo(self):
        if self.index < self.total:
            c = consejos[self.index]
            self.texto.config(text=f"Consejo {c['nro']} ({c['categoría']}): {c['consejo']}\nEjemplo: {c['ejemplo']}")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Completado", "¡Has completado los 100 consejos!")
            self.root.quit()

    def verificar(self):
        entrada = self.entry.get().strip()
        if entrada:
            self.ejercicios_completados += 1
            self.progress["value"] = self.ejercicios_completados
            self.estado.config(text=f"{self.ejercicios_completados} de {self.total} completados")
            self.index += 1
            self.mostrar_consejo()
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, escribe un ejemplo similar.")

# Ejecutar interfaz
root = tk.Tk()
app = App(root)
root.mainloop()
