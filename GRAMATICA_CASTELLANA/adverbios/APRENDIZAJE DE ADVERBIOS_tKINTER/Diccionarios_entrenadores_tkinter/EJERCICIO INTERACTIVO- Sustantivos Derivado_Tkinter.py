import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import random

sufijos = ['dad', 'idad', 'edad', 'tad', 'ez', 'eza', 'icia', 'ura', 'or']
bases = ['amable', 'fiel', 'maduro', 'rico', 'sabio', 'generoso', 'doctor', 'alto', 'dulce', 'frío']
oraciones_sugeridas = [
    "La {palabra} es importante en la vida diaria.",
    "Mostró gran {palabra} en su trabajo.",
    "La {palabra} del ambiente afecta el ánimo.",
    "Es conocido por su {palabra}.",
    "La {palabra} se valora en todas partes."
]

palabras_generadas = {}
oraciones = {}

def generar_palabras():
    palabras_generadas.clear()
    for _ in range(100):
        base = random.choice(bases)
        sufijo = random.choice(sufijos)
        palabra = base + sufijo
        palabras_generadas[palabra] = sufijo
    mostrar_palabras()

def mostrar_palabras():
    salida.delete(1.0, tk.END)
    for palabra in palabras_generadas:
        salida.insert(tk.END, f"{palabra}\n")

def sugerir_oracion():
    salida.delete(1.0, tk.END)
    for palabra in palabras_generadas:
        plantilla = random.choice(oraciones_sugeridas)
        oracion = plantilla.replace("{palabra}", palabra)
        oraciones[palabra] = oracion
        salida.insert(tk.END, f"{palabra}: {oracion}\n")

def editar_oraciones():
    salida.delete(1.0, tk.END)
    for palabra, oracion in oraciones.items():
        salida.insert(tk.END, f"{palabra}: {oracion}\n")
    salida.insert(tk.END, "\nEdita las oraciones directamente aquí y guarda.\n")

def guardar_archivo():
    texto = salida.get(1.0, tk.END)
    archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Texto", "*.txt")])
    if archivo:
        try:
            agrupado = {}
            for linea in texto.strip().split('\n'):
                if ':' in linea:
                    palabra, oracion = linea.split(':', 1)
                    palabra = palabra.strip()
                    oracion = oracion.strip()
                    sufijo = detectar_sufijo(palabra, sufijos)
                    agrupado.setdefault(sufijo, []).append((palabra, oracion))

            with open(archivo, 'w', encoding='utf-8') as f:
                for sufijo, pares in agrupado.items():
                    f.write(f"=== Sufijo: -{sufijo} ===\n")
                    for palabra, oracion in pares:
                        f.write(f"Palabra: {palabra}\nOración: {oracion}\n\n")
            messagebox.showinfo("Guardado", f"Archivo guardado como {archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

def detectar_sufijo(palabra, sufijos):
    for sufijo in sufijos:
        if palabra.endswith(sufijo):
            return sufijo
    return "otro"

def mostrar_teoria():
    teoria = (
        "Sufijos derivados para nombres de cualidad, estado o condición:\n\n"
        "-dad: bondad, lealtad\n"
        "-idad: felicidad, amabilidad\n"
        "-ez: rapidez, honradez\n"
        "-eza: belleza, tristeza\n"
        "-tad: libertad, dificultad\n"
        "-icia: justicia, malicia\n"
        "-ura: altura, hermosura\n"
        "-or: valor, sudor\n"
    )
    salida.delete(1.0, tk.END)
    salida.insert(tk.END, teoria)

# Interfaz tkinter
ventana = tk.Tk()
ventana.title("Derivación nominal: sufijos y escritura")
ventana.geometry("800x600")

boton1 = tk.Button(ventana, text="📘 Ver teoría", command=mostrar_teoria)
boton1.pack()

boton2 = tk.Button(ventana, text="🎲 Generar 100 palabras", command=generar_palabras)
boton2.pack()

boton3 = tk.Button(ventana, text="✍️ Sugerir oraciones", command=sugerir_oracion)
boton3.pack()

boton4 = tk.Button(ventana, text="📝 Editar oraciones", command=editar_oraciones)
boton4.pack()

boton5 = tk.Button(ventana, text="💾 Guardar archivo", command=guardar_archivo)
boton5.pack()

salida = scrolledtext.ScrolledText(ventana, width=90, height=25)
salida.pack(pady=10)

ventana.mainloop()
