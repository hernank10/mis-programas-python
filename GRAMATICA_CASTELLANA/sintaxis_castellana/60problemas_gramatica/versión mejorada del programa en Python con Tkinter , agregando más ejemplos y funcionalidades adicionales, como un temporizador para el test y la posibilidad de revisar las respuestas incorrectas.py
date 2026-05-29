import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class OracionesCausativasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oraciones Causativas")
        self.stats = {"correctas": 0, "incorrectas": 0}
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)
        
        tk.Label(self.frame, text="Selecciona una opción:").pack()
        
        tk.Button(self.frame, text="Ver teoría", command=self.mostrar_teoria).pack()
        tk.Button(self.frame, text="Ver ejemplos", command=self.mostrar_ejemplos).pack()
        tk.Button(self.frame, text="Practicar escritura", command=self.ejercicio_escritura).pack()
        tk.Button(self.frame, text="Completar oraciones", command=self.completar_oraciones).pack()
        tk.Button(self.frame, text="Realizar test", command=self.test_interactivo).pack()
        tk.Button(self.frame, text="Ver estadísticas", command=self.mostrar_estadisticas).pack()
        tk.Button(self.frame, text="Salir", command=root.quit).pack()
    
    def mostrar_teoria(self):
        messagebox.showinfo("Teoría", "Las oraciones causativas utilizan 'hacer' para indicar que una acción es causada por otra. Ejemplo: 'La lluvia hace crecer las plantas'.")
    
    def mostrar_ejemplos(self):
        ejemplos = """
1. La guerra hizo subir los precios.
2. La lluvia hace crecer las plantas.
3. El jefe nos hizo trabajar hasta tarde.
4. La música me hizo recordar viejos tiempos.
5. La noticia hizo llorar a María.
        """
        messagebox.showinfo("Ejemplos", ejemplos)
    
    def ejercicio_escritura(self):
        texto = simpledialog.askstring("Practicar escritura", "Escribe una oración usando el verbo 'hacer' en sentido causativo:")
        if texto:
            if "hacer" in texto or "hizo" in texto:
                messagebox.showinfo("Validación", "¡Bien! Has usado correctamente 'hacer'.")
                self.stats["correctas"] += 1
            else:
                messagebox.showwarning("Validación", "No usaste el verbo 'hacer'. Intenta de nuevo.")
                self.stats["incorrectas"] += 1
    
    def completar_oraciones(self):
        oraciones = [
            ("La noticia ___ llorar a todos.", "hizo"),
            ("El problema ___ perder la paciencia a Juan.", "hizo"),
            ("La película me ___ recordar mi infancia.", "hizo")
        ]
        for oracion, respuesta in oraciones:
            user_respuesta = simpledialog.askstring("Completa la oración", oracion)
            if user_respuesta and user_respuesta.lower() == respuesta:
                messagebox.showinfo("Resultado", "¡Correcto!")
                self.stats["correctas"] += 1
            else:
                messagebox.showwarning("Resultado", f"Incorrecto. La respuesta era '{respuesta}'.")
                self.stats["incorrectas"] += 1
    
    def test_interactivo(self):
        preguntas = [
            ("¿Cuál de estas es una oración causativa?", ["Juan corre rápido.", "La lluvia hace crecer las plantas.", "María está feliz."], 1),
            ("¿Qué verbo se usa en las oraciones causativas?", ["Ser", "Tener", "Hacer"], 2)
        ]
        for pregunta, opciones, correcta in preguntas:
            respuesta = simpledialog.askstring("Test", f"{pregunta}\nOpciones: {', '.join(opciones)}")
            if respuesta and respuesta.lower() == opciones[correcta].lower():
                messagebox.showinfo("Resultado", "¡Correcto!")
                self.stats["correctas"] += 1
            else:
                messagebox.showwarning("Resultado", f"Incorrecto. La respuesta era '{opciones[correcta]}'.")
                self.stats["incorrectas"] += 1
    
    def mostrar_estadisticas(self):
        messagebox.showinfo("Estadísticas", f"Respuestas correctas: {self.stats['correctas']}\nRespuestas incorrectas: {self.stats['incorrectas']}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = OracionesCausativasApp(root)
    root.mainloop()
