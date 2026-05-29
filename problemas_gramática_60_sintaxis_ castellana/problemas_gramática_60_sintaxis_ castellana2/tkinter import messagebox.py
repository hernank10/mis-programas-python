import random
import tkinter as tk
from tkinter import messagebox

definir palabras
sustantivos = {
    "niño": {"plural": "niños", "diminutivo": "niñito"},
    "taxi": {"plural": "taxis", "diminutivo": "taxicito"},
    "menú": {"plural": "menús", "diminutivo": "menucito"},
    "piedra": {"plural": "piedras", "diminutivo": "piedrita"},
    "clase": {"plural": "clases", "diminutivo": "clasita"},
    "sofá": {"plural": "sofás", "diminutivo": "sofacito"},
    "rubí": {"plural": "rubíes", "diminutivo": "rubicito"},
    "café": {"plural": "cafés", "diminutivo": "cafecito"},
    "mamá": {"plural": "mamás", "diminutivo": "mamita"},
    "papá": {"plural": "papás", "diminutivo": "papito"},
    "pez": {"plural": "peces", "diminutivo": "pececillo"},
    "lápiz": {"plural": "lápices", "diminutivo": "lapicito"},
    "cruz": {"plural": "cruces", "diminutivo": "crucecita"},
    "juez": {"plural": "jueces", "diminutivo": "juececillo"},
    "nariz": {"plural": "narices", "diminutivo": "naricita"},
    "flor": {"plural": "flores", "diminutivo": "florecita"},
    "amor": {"plural": "amores", "diminutivo": "amorcito"},
    "calor": {"plural": "calores", "diminutivo": "calorcito"},
    "color": {"plural": "colores", "diminutivo": "colorcito"},
    "tambor": {"plural": "tambores", "diminutivo": "tamborcito"},
    "atlas": {"plural": "atlas", "diminutivo": "(sin diminutivo frecuente)"},
    "cosmos": {"plural": "cosmos", "diminutivo": "(sin diminutivo frecuente)"},
    "lunes": {"plural": "lunes", "diminutivo": "lunesito"},
    "tesis": {"plural": "tesis", "diminutivo": "tesecita"},
    "virus": {"plural": "virus", "diminutivo": "virucito"},
    "caos": {"plural": "caos", "diminutivo": "(sin diminutivo frecuente)"},
    "oasis": {"plural": "oasis", "diminutivo": "oasiscito"},
    "crisis": {"plural": "crisis", "diminutivo": "crisecita"},
}

def practicar():
    vidas = 3
    puntaje = 0
    while vidas > 0:
        palabra = random.choice(list(sustantivos.keys()))
        categoria = random.choice(["plural", "diminutivo"])
        respuesta_usuario = input(f"¿Cuál es el {categoria} de '{palabra}'? ").strip()
        respuesta_correcta = sustantivos[palabra][categoria]
        if respuesta_usuario.lower() == respuesta_correcta:
            print("¡Correcto!")
            puntaje += 1
        else:
            vidas -= 1
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}. Te quedan {vidas} vidas.")
    print(f"Tu puntaje final es: {puntaje}")

def iniciar_gui():
    def verificar_respuesta():
        respuesta_usuario = entrada.get().strip().lower()
        respuesta_correcta = sustantivos[palabra_actual][categoria_actual]
        if respuesta_usuario == respuesta_correcta:
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta es: {respuesta_correcta}")
        nueva_pregunta()
    
    def nueva_pregunta():
        global palabra_actual, categoria_actual
        palabra_actual = random.choice(list(sustantivos.keys()))
        categoria_actual = random.choice(["plural", "diminutivo"])
        etiqueta.config(text=f"¿Cuál es el {categoria_actual} de '{palabra_actual}'?")
        entrada.delete(0, tk.END)
    
    root = tk.Tk()
    root.title("Práctica de Flexión Nominal")
    
    etiqueta = tk.Label(root, text="", font=("Arial", 14))
    etiqueta.pack(pady=10)
    
    entrada = tk.Entry(root, font=("Arial", 14))
    entrada.pack(pady=5)
    
    boton_verificar = tk.Button(root, text="Verificar", command=verificar_respuesta)
    boton_verificar.pack(pady=5)
    
    nueva_pregunta()
    root.mainloop()

if __name__ == "__main__":
    iniciar_gui()
