import tkinter as tk
from tkinter import messagebox, simpledialog

class ModificadoresLocativosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modificadores Locativos")
        self.root.geometry("500x500")

        self.stats = {"oraciones_escritas": 0, "aciertos": 0, "intentos": 0}

        tk.Label(root, text="Modificadores Locativos", font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Button(root, text="Ver teoría", command=self.mostrar_teoria).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Ver ejemplos", command=self.mostrar_ejemplos).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Practicar escritura", command=self.ejercicio_escritura).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Realizar test", command=self.test_interactivo).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Ver estadísticas", command=self.mostrar_estadisticas).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(fill="x", padx=20, pady=10)

    def mostrar_teoria(self):
        teoria = (
            "📖 TEORÍA SOBRE MODIFICADORES LOCATIVOS\n\n"
            "Los modificadores locativos son aquellos que indican un lugar o posición "
            "relacionado con el sustantivo. Suelen introducirse con preposiciones como "
            "'en', 'sobre', 'bajo', 'dentro de', etc.\n\n"
            "Ejemplos correctos:\n"
            "- Tengo un coche en el garaje. ✅\n"
            "- Es catedrático en la Complutense. ✅\n\n"
            "Ejemplo incorrecto:\n"
            "- *Tengo coche en el garaje. ❌\n"
            "(Falta determinante en 'coche')\n\n"
            "🔹 REGLA IMPORTANTE: Un sustantivo contable sin determinación no puede tener un "
            "modificador locativo cuando es objeto directo."
        )
        messagebox.showinfo("Teoría", teoria)

    def mostrar_ejemplos(self):
        ejemplos = (
            "✅ Ejemplos correctos:\n"
            "1. Tengo un coche en el garaje.\n"
            "2. Dejé las llaves sobre la mesa.\n"
            "3. Encontré un libro dentro de la mochila.\n"
            "4. La reunión será en la oficina principal.\n"
            "5. Compró una casa junto al río.\n"
            "6. Mi perro duerme bajo la mesa.\n"
            "7. Hay estudiantes en la biblioteca.\n"
            "8. Pedro trabaja en la universidad.\n"
            "9. Es maestro en la secundaria.\n"
            "10. María está en el parque con sus hijos.\n\n"
            "❌ Ejemplo incorrecto:\n"
            "- *Tengo coche en el garaje.\n"
            "(El sustantivo 'coche' no tiene determinante)"
        )
        messagebox.showinfo("Ejemplos", ejemplos)

    def ejercicio_escritura(self):
        texto = simpledialog.askstring("Práctica", "Escribe una oración con un modificador locativo:")
        if texto:
            self.stats["oraciones_escritas"] += 1
            messagebox.showinfo("Respuesta guardada", f"Tu oración fue:\n{texto}")

    def test_interactivo(self):
        preguntas = [
            ("¿Cuál oración es correcta?", 
             ["*Tengo coche en el garaje", "Tengo un coche en el garaje"], 1),
            ("¿Cuál oración usa un modificador locativo?", 
             ["Es catedrático en la Complutense", "Es catedrático excelente"], 0),
            ("¿Cuál oración está bien formulada?", 
             ["*Hay perro en la casa", "Hay un perro en la casa"], 1),
            ("¿Qué preposición es común en modificadores locativos?", 
             ["en", "de"], 0),
            ("¿Cuál oración es incorrecta?", 
             ["Compré un cuadro para la sala", "*Tengo bicicleta en el garaje"], 1),
            ("¿Qué oración usa correctamente un locativo?", 
             ["La reunión será en la oficina", "Es un gran profesor"], 0),
            ("¿Dónde está el modificador locativo en 'Dejé mi bolso bajo la mesa'?", 
             ["bajo la mesa", "mi bolso"], 0),
            ("¿Qué oración no usa un modificador locativo?", 
             ["Es médico en el hospital", "Es médico excelente"], 1),
            ("En 'Pedro estudia en la biblioteca', ¿cuál es el modificador locativo?", 
             ["en la biblioteca", "Pedro"], 0),
            ("¿Qué oración necesita un determinante para ser correcta?", 
             ["Tengo coche en el garaje", "Tengo un coche en el garaje"], 0)
        ]

        for pregunta, opciones, respuesta_correcta in preguntas:
            respuesta = simpledialog.askstring("Test", f"{pregunta}\n1. {opciones[0]}\n2. {opciones[1]}\n\nEscribe el número de la opción:")
            if respuesta and respuesta.isdigit():
                self.stats["intentos"] += 1
                if int(respuesta) - 1 == respuesta_correcta:
                    self.stats["aciertos"] += 1
                    messagebox.showinfo("Resultado", "¡Correcto!")
                else:
                    messagebox.showwarning("Resultado", "Incorrecto.")

    def mostrar_estadisticas(self):
        messagebox.showinfo("Estadísticas",
            f"📊 ESTADÍSTICAS DE USUARIO\n"
            f"📌 Oraciones escritas: {self.stats['oraciones_escritas']}\n"
            f"📌 Aciertos en test: {self.stats['aciertos']} de {self.stats['intentos']} intentos\n"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = ModificadoresLocativosApp(root)
    root.mainloop()
