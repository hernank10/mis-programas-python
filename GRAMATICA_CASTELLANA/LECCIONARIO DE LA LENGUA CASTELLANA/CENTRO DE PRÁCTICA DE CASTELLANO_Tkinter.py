import tkinter as tk
from tkinter import messagebox
import random

# Base de datos simplificada (3 por área)
datos = {
    'ortografia': [
        {"tipo": "completar", "pregunta": "Completa: Se escri__e con 'b' después de 'm'.", "respuesta": "be"},
        {"tipo": "opcion", "pregunta": "¿Cuál es la forma correcta?", "opciones": ["invitar", "inbitar"], "respuesta": "invitar"},
        {"tipo": "completar", "pregunta": "Se usa 'h' en: __ombre, __acer, __uevo.", "respuesta": "h"},
    ],
    'morfologia': [
        {"tipo": "clasificar", "pregunta": "¿Qué tipo de palabra es 'corriendo'?", "respuesta": "gerundio"},
        {"tipo": "clasificar", "pregunta": "¿Qué tipo de palabra es 'ellos'?", "respuesta": "pronombre"},
        {"tipo": "clasificar", "pregunta": "'Rápido' en 'tren rápido' es:", "respuesta": "adjetivo"},
    ],
    'sintaxis': [
        {"tipo": "funcion", "pregunta": "¿Qué función cumple 'el perro' en 'El perro duerme'?", "respuesta": "sujeto"},
        {"tipo": "funcion", "pregunta": "¿Qué función cumple 'la pelota' en 'Juan lanzó la pelota'?", "respuesta": "complemento directo"},
        {"tipo": "funcion", "pregunta": "¿Qué tipo de oración es 'Juan estudia porque quiere aprender'?", "respuesta": "subordinada causal"},
    ]
}

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Centro de práctica de castellano")
        self.tema = None
        self.ejercicio_actual = None
        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="📘 Centro de práctica de castellano", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Button(self.root, text="Ortografía", command=lambda: self.seleccionar_tema("ortografia"), width=30).pack(pady=5)
        tk.Button(self.root, text="Morfología", command=lambda: self.seleccionar_tema("morfologia"), width=30).pack(pady=5)
        tk.Button(self.root, text="Sintaxis", command=lambda: self.seleccionar_tema("sintaxis"), width=30).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit, width=30).pack(pady=20)

    def seleccionar_tema(self, tema):
        self.tema = tema
        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        self.limpiar_ventana()
        ejercicios = datos[self.tema]
        self.ejercicio_actual = random.choice(ejercicios)

        tk.Label(self.root, text=f"Área: {self.tema.capitalize()}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=self.ejercicio_actual["pregunta"], wraplength=400, font=("Arial", 12)).pack(pady=10)

        if self.ejercicio_actual["tipo"] == "opcion":
            self.respuesta_var = tk.StringVar()
            for opcion in self.ejercicio_actual["opciones"]:
                tk.Radiobutton(self.root, text=opcion, variable=self.respuesta_var, value=opcion).pack(anchor="w", padx=50)
        else:
            self.entrada_respuesta = tk.Entry(self.root, font=("Arial", 12))
            self.entrada_respuesta.pack(pady=10)

        tk.Button(self.root, text="Enviar respuesta", command=self.verificar_respuesta).pack(pady=10)
        tk.Button(self.root, text="Menú principal", command=self.crear_menu_principal).pack(pady=5)

    def verificar_respuesta(self):
        correcta = self.ejercicio_actual["respuesta"].strip().lower()
        if self.ejercicio_actual["tipo"] == "opcion":
            respuesta = self.respuesta_var.get().strip().lower()
        else:
            respuesta = self.entrada_respuesta.get().strip().lower()

        if respuesta == correcta:
            messagebox.showinfo("Resultado", "✅ ¡Respuesta correcta!")
        else:
            messagebox.showerror("Resultado", f"❌ Incorrecto. La respuesta correcta es: {correcta}")

        self.mostrar_ejercicio()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = Aplicacion(root)
    root.mainloop()
