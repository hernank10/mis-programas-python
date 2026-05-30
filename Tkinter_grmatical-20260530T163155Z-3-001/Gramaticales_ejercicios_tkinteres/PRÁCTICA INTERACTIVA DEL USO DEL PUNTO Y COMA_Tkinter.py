import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Base de datos de ejemplos por categoría
ejemplos_base = {
    "Enumeración compleja": [
        "Jorge, Pedro y María Luisa; Andrés, Patricia y Amelia; y los Pérez estudiaron en la UIS."
    ],
    "Explicativa": [
        "Jorge Pérez, de la UCS; Andrés Hurtado, de los Andes; y María Clara, de la Sabana, son los finalistas."
    ],
    "Elíptica": [
        "Luis se encarga del diseño; Marta, de las estadísticas; Pedro, de la edición."
    ]
}

puntuacion = {"aciertos": 0, "errores": 0}

root = tk.Tk()
root.title("Práctica Punto y Coma")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20)

output = tk.Text(root, height=15, wrap=tk.WORD)
output.pack(pady=10)

def mostrar(text):
    output.delete("1.0", tk.END)
    output.insert(tk.END, text)

def teoria_categoria():
    resultado = "\n=== TEORÍA Y EJEMPLOS ==="
    for tipo, lista in ejemplos_base.items():
        resultado += f"\n\nTipo: {tipo}\n"
        if tipo == "Enumeración compleja":
            resultado += "Uso de punto y coma para separar grupos dentro de una lista extensa.\n"
        elif tipo == "Explicativa":
            resultado += "Uso de punto y coma para aislar incisos explicativos largos o que ya contienen comas.\n"
        elif tipo == "Elíptica":
            resultado += "Uso de punto y coma para omitir el verbo que ya se entiende por el contexto.\n"
        resultado += "Ejemplos:\n"
        for ej in lista:
            resultado += f"- {ej}\n"
    mostrar(resultado)

def corregir_errores_comunes(texto):
    texto = texto.replace("Por:", "Por").replace("por:", "por").replace("a:", "a")
    estructuras_invalidas = [
        "explicará:", "informó:", "dijo:", "contó:", "describió:", "resumió:", "presentó:",
        "mostró:", "narró:", "reveló:", "anunció:"
    ]
    for e in estructuras_invalidas:
        texto = texto.replace(e, e.replace(":", ""))
    return texto

def clasificar_oraciones():
    oraciones = []
    for tipo, lista in ejemplos_base.items():
        oraciones += [(ej, tipo) for ej in lista]
    random.shuffle(oraciones)
    resultado = ""
    for texto, tipo in oraciones[:3]:
        respuesta = simpledialog.askstring("Clasifica", f"Oración: {texto}\nTipo:")
        if respuesta and respuesta.lower() == tipo.lower():
            resultado += f"✔ Correcto: {texto}\n"
            puntuacion["aciertos"] += 1
        else:
            resultado += f"✘ Incorrecto. Era: {tipo}\n"
            puntuacion["errores"] += 1
    mostrar(resultado + f"\nAciertos: {puntuacion['aciertos']} | Errores: {puntuacion['errores']}")

def escribir_modelo():
    tipo = simpledialog.askstring("Tipo", "Selecciona tipo (Enumeración compleja, Explicativa, Elíptica):")
    if tipo in ejemplos_base:
        oracion = simpledialog.askstring("Escribe", "Escribe tu oración:")
        if oracion:
            ejemplos_base[tipo].append(oracion)
            messagebox.showinfo("Guardado", "✔ Oración guardada.")
    else:
        messagebox.showerror("Error", "Tipo no válido")

def corregir_puntuacion():
    texto = simpledialog.askstring("Texto", "Escribe un texto para corregir puntuación:")
    if texto:
        corregido = corregir_errores_comunes(texto)
        mostrar(f"Texto corregido:\n{corregido}")

def organizar_orden():
    ejemplos = [
        ("Llegaron los estudiantes, después de una larga caminata.", "Lógico"),
        ("Después de una larga caminata, llegaron los estudiantes.", "Inverso")
    ]
    random.shuffle(ejemplos)
    resultado = ""
    for texto, orden in ejemplos:
        respuesta = simpledialog.askstring("Orden", f"Oración: {texto}\nOrden (Lógico/Inverso):")
        if respuesta and respuesta.lower() == orden.lower():
            resultado += "✔ Correcto!\n"
            puntuacion["aciertos"] += 1
        else:
            resultado += f"✘ Incorrecto. Era: {orden}\n"
            puntuacion["errores"] += 1
    mostrar(resultado + f"\nAciertos: {puntuacion['aciertos']} | Errores: {puntuacion['errores']}")

def agregar_ejemplo():
    tipo = simpledialog.askstring("Tipo", "Tipo (Enumeración compleja, Explicativa, Elíptica):")
    if tipo in ejemplos_base:
        nuevo = simpledialog.askstring("Ejemplo", "Escribe el ejemplo:")
        if nuevo:
            ejemplos_base[tipo].append(nuevo)
            messagebox.showinfo("Éxito", "✔ Ejemplo añadido correctamente.")
    else:
        messagebox.showerror("Error", "Tipo no reconocido.")

def ver_ejemplos():
    resultado = ""
    for tipo, lista in ejemplos_base.items():
        resultado += f"\n{tipo}:\n"
        for i, ej in enumerate(lista, 1):
            resultado += f"{i}. {ej}\n"
    mostrar(resultado)

btns = [
    ("1. Teoría y ejemplos", teoria_categoria),
    ("2. Clasificar oraciones", clasificar_oraciones),
    ("3. Escribir oraciones", escribir_modelo),
    ("4. Corregir puntuación", corregir_puntuacion),
    ("5. Orden lógico vs inverso", organizar_orden),
    ("6. Añadir ejemplos", agregar_ejemplo),
    ("7. Ver ejemplos", ver_ejemplos),
    ("8. Salir", root.quit)
]

for txt, cmd in btns:
    tk.Button(frame, text=txt, command=cmd, width=30).pack(pady=2)

root.mainloop()
