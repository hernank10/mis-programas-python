import tkinter as tk
from tkinter import messagebox, simpledialog

class Leccion11App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lección 11 – Lengua Castellana – 7º Grado")
        self.root.geometry("600x500")

        self.ejemplos = [
            "El perro ladra. → Sujeto: El perro | Predicado: ladra",
            "Llueve mucho. → Sujeto: (implícito) | Predicado: Llueve mucho",
        ]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="LECCIÓN 11: Tipos de sujeto y predicado", font=("Helvetica", 14, "bold")).pack(pady=10)

        btn_teoria = tk.Button(self.root, text="1. Ver teoría", command=self.mostrar_teoria)
        btn_ejemplos = tk.Button(self.root, text="2. Ver ejemplos", command=self.mostrar_ejemplos)
        btn_actividad = tk.Button(self.root, text="3. Actividades sugeridas", command=self.actividades_sugeridas)
        btn_crear = tk.Button(self.root, text="4. Escribir cuento corto", command=self.escribir_cuento)
        btn_salir = tk.Button(self.root, text="Salir", command=self.root.quit)

        for btn in [btn_teoria, btn_ejemplos, btn_actividad, btn_crear, btn_salir]:
            btn.pack(pady=5, ipadx=10)

    def mostrar_teoria(self):
        teoria = (
            "El sujeto es la persona, animal o cosa de quien se dice algo.\n"
            "El predicado es lo que se dice del sujeto.\n\n"
            "TIPOS DE SUJETO:\n"
            "- Sujeto explícito: está presente en la oración.\n"
            "- Sujeto implícito: no aparece pero se sobreentiende.\n\n"
            "TIPOS DE PREDICADO:\n"
            "- Verbal: contiene un verbo.\n"
            "- Nominal: describe estados o cualidades."
        )
        messagebox.showinfo("Teoría", teoria)

    def mostrar_ejemplos(self):
        ejemplos_texto = "\n\n".join(self.ejemplos)
        opcion = messagebox.askquestion("Ejemplos", f"{ejemplos_texto}\n\n¿Quieres añadir un nuevo ejemplo?")
        if opcion == "yes":
            nuevo = simpledialog.askstring("Nuevo ejemplo", "Escribe un nuevo ejemplo con sujeto y predicado:")
            if nuevo:
                self.ejemplos.append(nuevo)
                messagebox.showinfo("Ejemplo agregado", "El nuevo ejemplo ha sido guardado.")

    def actividades_sugeridas(self):
        actividad = (
            "✅ Actividades sugeridas:\n\n"
            "1. Escribe un cuento corto y subraya el sujeto y predicado en cada oración.\n"
            "2. Participa en juegos de rol donde representes oraciones con sujeto implícito.\n"
            "3. Lee un texto breve y subraya en diferentes colores los sujetos y predicados.\n\n"
            "📌 EJEMPLO:\n"
            "Texto: 'Pedro corre en el parque. Juega con su perro.'\n"
            "Identificación: Sujeto: Pedro | Predicado: corre en el parque\n"
            "Sujeto: (implícito) | Predicado: Juega con su perro"
        )
        messagebox.showinfo("Actividades sugeridas", actividad)

    def escribir_cuento(self):
        cuento = simpledialog.askstring("Escribir cuento", "Escribe tu cuento corto:")
        if cuento:
            with open("cuento_7grado.txt", "a") as f:
                f.write(f"\n\nCUENTO NUEVO:\n{cuento}")
            messagebox.showinfo("Guardado", "Tu cuento ha sido guardado en 'cuento_7grado.txt'.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Leccion11App(root)
    root.mainloop()
