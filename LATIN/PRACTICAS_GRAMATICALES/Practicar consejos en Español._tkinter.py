import tkinter as tk
import random

# Lista de consejos (ejemplo con pocos; puedes ampliar hasta 200)
consejos = [
    ("Use adjectives before nouns. / Usa los adjetivos antes de los sustantivos.",
     "Use adjectives before nouns.",
     "Usa los adjetivos antes de los sustantivos."),
    ("Pronouns replace nouns. / Los pronombres reemplazan a los sustantivos.",
     "Pronouns replace nouns.",
     "Los pronombres reemplazan a los sustantivos."),
    ("Prepositions show relationships. / Las preposiciones muestran relaciones.",
     "Prepositions show relationships.",
     "Las preposiciones muestran relaciones."),
]

class ConsejoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Consejos Inglés-Español")

        # Texto principal
        self.label = tk.Label(root, text="Elige una opción", font=("Arial", 14))
        self.label.pack(pady=10)

        # Botones
        self.btn_ver = tk.Button(root, text="Ver un consejo aleatorio", command=self.ver_consejo, width=40)
        self.btn_ver.pack(pady=5)

        self.btn_practicar = tk.Button(root, text="Practicar un consejo", command=self.practicar_consejo, width=40)
        self.btn_practicar.pack(pady=5)

        self.btn_salir = tk.Button(root, text="Salir", command=root.quit, width=40)
        self.btn_salir.pack(pady=5)

        # Área de texto dinámico
        self.output = tk.Label(root, text="", font=("Arial", 12), wraplength=500, justify="left")
        self.output.pack(pady=10)

        # Campos para práctica
        self.entry_eng = tk.Entry(root, width=60)
        self.entry_esp = tk.Entry(root, width=60)
        self.btn_check = tk.Button(root, text="Comprobar", command=self.check_respuesta)
        self.feedback = tk.Label(root, text="", font=("Arial", 12), fg="blue")

        # Consejo actual en práctica
        self.current_consejo = None

    def ver_consejo(self):
        consejo = random.choice(consejos)
        self.output.config(text=consejo[0])

        # Ocultar widgets de práctica si están visibles
        self.entry_eng.pack_forget()
        self.entry_esp.pack_forget()
        self.btn_check.pack_forget()
        self.feedback.pack_forget()

    def practicar_consejo(self):
        self.current_consejo = random.choice(consejos)
        self.output.config(text=f"Practica este consejo:\n\n{self.current_consejo[0]}")

        # Mostrar entradas
        self.entry_eng.delete(0, tk.END)
        self.entry_esp.delete(0, tk.END)
        self.entry_eng.pack(pady=5)
        self.entry_eng.insert(0, "Escribe aquí en inglés...")
        self.entry_esp.pack(pady=5)
        self.entry_esp.insert(0, "Escribe aquí en español...")
        self.btn_check.pack(pady=5)
        self.feedback.pack(pady=10)

    def check_respuesta(self):
        eng = self.entry_eng.get().strip()
        esp = self.entry_esp.get().strip()

        eng_correct = eng == self.current_consejo[1]
        esp_correct = esp == self.current_consejo[2]

        if eng_correct and esp_correct:
            self.feedback.config(text="✅ ¡Correcto en ambos idiomas!", fg="green")
        elif eng_correct and not esp_correct:
            self.feedback.config(
                text=f"⚠️ Inglés correcto. Español incorrecto.\nCorrecto: {self.current_consejo[2]}",
                fg="orange"
            )
        elif not eng_correct and esp_correct:
            self.feedback.config(
                text=f"⚠️ Español correcto. Inglés incorrecto.\nCorrecto: {self.current_consejo[1]}",
                fg="orange"
            )
        else:
            self.feedback.config(
                text=f"❌ Ambos incorrectos.\nInglés: {self.current_consejo[1]}\nEspañol: {self.current_consejo[2]}",
                fg="red"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsejoApp(root)
    root.mainloop()
