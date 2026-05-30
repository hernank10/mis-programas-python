import tkinter as tk
from tkinter import messagebox
import random

# Datos de los temas
temas = {
    "Uso del punto y coma": [
        {
            "regla": "Separa proposiciones relacionadas cuando ya se han usado comas.",
            "ejemplo": "Vino Pedro, el hermano de Luis; María, su prima, también.",
            "pregunta": "Escribe una oración que use el punto y coma según esta regla.",
            "respuesta": ";"
        },
        {
            "regla": "Separa oraciones yuxtapuestas con significados relacionados.",
            "ejemplo": "Estudió toda la noche; aprobó el examen.",
            "pregunta": "Escribe un ejemplo similar al anterior.",
            "respuesta": ";"
        }
    ],
    "Uso de b y v": [
        {
            "regla": "Se escriben con 'b' los verbos terminados en -bir (excepto hervir, servir y vivir).",
            "ejemplo": "Escribió una carta.",
            "pregunta": "Escribe un verbo que termine en -bir y contenga 'b'.",
            "respuesta": "b"
        },
        {
            "regla": "Se escriben con 'v' las formas de los verbos que no tienen 'b' en su infinitivo.",
            "ejemplo": "Vivir en el campo es saludable.",
            "pregunta": "Escribe un verbo que use 'v'.",
            "respuesta": "v"
        }
    ],
    "Tipos de oraciones compuestas": [
        {
            "regla": "Las copulativas unen ideas similares: y, e, ni.",
            "ejemplo": "Juan estudia y María trabaja.",
            "pregunta": "Escribe una oración copulativa.",
            "respuesta": "y"
        },
        {
            "regla": "Las adversativas oponen ideas: pero, sino, aunque.",
            "ejemplo": "Quise ir, pero estaba cansado.",
            "pregunta": "Escribe una oración adversativa.",
            "respuesta": "pero"
        }
    ],
    "Partes de la oración": [
        {
            "regla": "Toda oración tiene sujeto y predicado.",
            "ejemplo": "El perro (sujeto) duerme plácidamente (predicado).",
            "pregunta": "Escribe una oración con sujeto y predicado.",
            "respuesta": "duerme"
        }
    ],
    "Tilde en agudas, llanas y esdrújulas": [
        {
            "regla": "Las palabras agudas llevan tilde si terminan en n, s o vocal.",
            "ejemplo": "Café, sofá.",
            "pregunta": "Escribe una palabra aguda con tilde.",
            "respuesta": "é"
        }
    ],
    "Uso de c, s, z": [
        {
            "regla": "Los sustantivos abstractos terminados en -ez, -eza se escriben con z.",
            "ejemplo": "Riqueza, rapidez.",
            "pregunta": "Escribe una palabra terminada en -ez.",
            "respuesta": "z"
        }
    ],
    "Signos de puntuación": [
        {
            "regla": "Se usa la coma para enumerar elementos.",
            "ejemplo": "Compré pan, leche, queso y frutas.",
            "pregunta": "Escribe una enumeración con comas.",
            "respuesta": ","
        }
    ],
    "Homófonos y parónimos": [
        {
            "regla": "Votar (emitir un voto) y botar (tirar algo) son homófonos.",
            "ejemplo": "Voy a votar en las elecciones.",
            "pregunta": "Escribe una oración usando 'botar'.",
            "respuesta": "botar"
        }
    ]
}

class ProgramaEducativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Programa de Ejercicios Interactivos")
        self.tema_actual = ""
        self.ejercicio_actual = None
        self.modo = tk.StringVar(value="practica")
        self.tema_menu()

    def tema_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Selecciona un tema:").pack(pady=10)
        for tema in temas.keys():
            tk.Button(self.root, text=tema, command=lambda t=tema: self.seleccionar_tema(t)).pack(fill="x", padx=20, pady=2)

    def seleccionar_tema(self, tema):
        self.tema_actual = tema
        self.ejercicio_actual = random.choice(temas[tema])
        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Tema: {self.tema_actual}", font=("Arial", 14, "bold")).pack(pady=5)
        if self.modo.get() == "practica":
            tk.Label(self.root, text="📘 Regla: " + self.ejercicio_actual["regla"]).pack()
            tk.Label(self.root, text="✏️ Ejemplo: " + self.ejercicio_actual["ejemplo"]).pack()
        tk.Label(self.root, text="💬 " + self.ejercicio_actual["pregunta"], font=("Arial", 12)).pack(pady=5)

        self.entrada = tk.Entry(self.root, width=50)
        self.entrada.pack(pady=5)

        tk.Button(self.root, text="Verificar", command=self.verificar_respuesta).pack(pady=5)
        tk.Button(self.root, text="Otro ejercicio", command=self.siguiente_ejercicio).pack(pady=2)
        tk.Button(self.root, text="← Menú principal", command=self.tema_menu).pack(pady=10)

        tk.Label(self.root, text="Modo:").pack()
        tk.Radiobutton(self.root, text="Práctica", variable=self.modo, value="practica", command=self.mostrar_ejercicio).pack()
        tk.Radiobutton(self.root, text="Examen (sin ayuda)", variable=self.modo, value="examen", command=self.mostrar_ejercicio).pack()

    def verificar_respuesta(self):
        respuesta_usuario = self.entrada.get().lower()
        if self.ejercicio_actual["respuesta"] in respuesta_usuario:
            messagebox.showinfo("✅ Correcto", "¡Bien hecho!")
        else:
            messagebox.showwarning("❌ Incorrecto", f"Revisa la regla: {self.ejercicio_actual['regla']}")

    def siguiente_ejercicio(self):
        self.ejercicio_actual = random.choice(temas[self.tema_actual])
        self.mostrar_ejercicio()

# Crear ventana principal
root = tk.Tk()
root.geometry("500x500")
app = ProgramaEducativo(root)
root.mainloop()
