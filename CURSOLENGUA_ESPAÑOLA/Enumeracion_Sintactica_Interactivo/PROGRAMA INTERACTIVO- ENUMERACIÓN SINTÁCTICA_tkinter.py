import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# Rutas base
BASE_DIR = "./Enumeracion_Sintactica_Interactivo"
EJEMPLOS = os.path.join(BASE_DIR, "ejemplos_usuario")
os.makedirs(EJEMPLOS, exist_ok=True)

# Diapositivas
DIAPOS = [
    "Enumeración Sintáctica:\n\nEs el uso de comas para separar elementos análogos dentro de una oración.",
    "Ejemplo:\n\nEl Instituto ofrece cursos de inglés, francés, ruso, portugués, italiano y alemán.",
    "Regla fundamental:\n\nNo se debe separar con coma el sujeto, el verbo y el complemento directo o indirecto.",
    "Ejemplo correcto:\n\nLos profesores Jaramillo, Silva y Palencia asesorarán a los alumnos Pérez y Sarmiento.",
    "Uso correcto:\n\nLas comas solo separan elementos dentro del sujeto o del complemento, nunca entre quién, verbo y qué."
]

# Cuestionario
PREGUNTAS = [
    {
        "pregunta": "¿Cuál es el propósito de la coma en una enumeración sintáctica?",
        "opciones": ["Separar sujeto y verbo", "Separar elementos análogos", "Terminar la oración", "Unir oraciones distintas"],
        "respuesta": 1
    },
    {
        "pregunta": "¿Qué no debe separarse con comas en una oración?",
        "opciones": ["Elementos del sujeto", "Verbo de complemento", "Listas de nombres", "Series de adjetivos"],
        "respuesta": 1
    }
]

# Oraciones con errores
ORACIONES_INCORRECTAS = [
    "Los estudiantes, aprobaron matemáticas, ciencias y, literatura.",
    "Los doctores Pérez, Ramírez operaron, a Juan y a, Carlos.",
    "Los músicos, tocaron la guitarra, el violín y el piano, en el festival.",
    "Los pintores, italianos, franceses y, españoles expusieron su obra.",
    "María, Pedro y Sofía, cocinan, pasteles, galletas y flanes."
] * 10

# Guardar ejemplos
def guardar_ejemplo(oracion):
    archivo = os.path.join(EJEMPLOS, "ejemplos.json")
    ejemplos = []
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            ejemplos = json.load(f)
    if len(ejemplos) < 100:
        ejemplos.append(oracion)
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(ejemplos, f, indent=4, ensure_ascii=False)
        messagebox.showinfo("Guardado", "Ejemplo guardado correctamente.")
    else:
        messagebox.showerror("Error", "Límite de 100 ejemplos alcanzado.")

# Interfaz principal
class App:
    def __init__(self, root):
        self.root = root
        root.title("Enumeración Sintáctica Interactiva")

        tk.Button(root, text="📚 Ver Diapositivas", command=self.ver_diapositivas).pack(pady=5)
        tk.Button(root, text="📝 Cuestionario", command=self.cuestionario).pack(pady=5)
        tk.Button(root, text="✍️ Corregir Oraciones", command=self.corregir_oraciones).pack(pady=5)
        tk.Button(root, text="❌ Salir", command=root.quit).pack(pady=5)

    def ver_diapositivas(self):
        for diap in DIAPOS:
            messagebox.showinfo("Diapositiva", diap)

    def cuestionario(self):
        puntuacion = 0
        for p in PREGUNTAS:
            opciones = "\n".join(f"{i}. {o}" for i, o in enumerate(p['opciones']))
            respuesta = simpledialog.askstring("Cuestionario", f"{p['pregunta']}\n\n{opciones}")
            if respuesta and respuesta.isdigit() and int(respuesta) == p['respuesta']:
                puntuacion += 1
                messagebox.showinfo("Correcto", "¡Respuesta correcta!")
            else:
                messagebox.showwarning("Incorrecto", "Respuesta incorrecta.")
        messagebox.showinfo("Resultado", f"Tu puntuación: {puntuacion}/{len(PREGUNTAS)}")

    def corregir_oraciones(self):
        for i, oracion in enumerate(ORACIONES_INCORRECTAS[:10]):
            correccion = simpledialog.askstring("Corregir", f"Corrige la oración {i+1}:\n\n{oracion}")
            if correccion:
                guardar_ejemplo(correccion)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
