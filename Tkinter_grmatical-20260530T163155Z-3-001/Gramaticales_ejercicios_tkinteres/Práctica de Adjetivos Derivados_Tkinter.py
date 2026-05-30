import tkinter as tk
from tkinter import messagebox
import random

# Datos
adjetivos = [
    {"base": "nación", "adjetivo": "nacional", "sufijo": "-al", "tipo": "Relación", "oración": "El himno nacional se canta en los actos cívicos."},
    {"base": "gracia", "adjetivo": "gracioso", "sufijo": "-oso", "tipo": "Cualidad", "oración": "Ese niño es muy gracioso cuando habla."},
    {"base": "historia", "adjetivo": "histórico", "sufijo": "-ico", "tipo": "Relación", "oración": "Fue un momento histórico para el país."},
    {"base": "docilidad", "adjetivo": "dócil", "sufijo": "-il", "tipo": "Cualidad", "oración": "El perro es muy dócil con los niños."},
    {"base": "campo", "adjetivo": "campesino", "sufijo": "-ino", "tipo": "Procedencia", "oración": "El campesino cultiva maíz."},
    {"base": "Canadá", "adjetivo": "canadiense", "sufijo": "-ense", "tipo": "Gentilicio", "oración": "Mi amigo es canadiense."},
    {"base": "salario", "adjetivo": "salarial", "sufijo": "-ario", "tipo": "Relación", "oración": "Hay desigualdad salarial en la empresa."},
    {"base": "iniciativa", "adjetivo": "iniciativo", "sufijo": "-ivo", "tipo": "Cualidad", "oración": "Luis es muy iniciativo en los proyectos."},
    {"base": "tenacidad", "adjetivo": "tenaz", "sufijo": "-az", "tipo": "Cualidad", "oración": "Ella es una estudiante tenaz."},
    {"base": "talento", "adjetivo": "talentoso", "sufijo": "-oso", "tipo": "Cualidad", "oración": "Pedro es un músico talentoso."},
]

# Ventana principal
root = tk.Tk()
root.title("Práctica de Adjetivos Derivados")
root.geometry("500x400")

def ejercicio_asociacion():
    limpiar_pantalla()
    item = random.choice(adjetivos)
    opciones = [item["adjetivo"]]
    while len(opciones) < 3:
        op = random.choice(adjetivos)["adjetivo"]
        if op not in opciones:
            opciones.append(op)
    random.shuffle(opciones)
    
    pregunta = f"¿Cuál es el adjetivo derivado de '{item['base']}'?"
    lbl = tk.Label(root, text=pregunta, font=("Arial", 14))
    lbl.pack(pady=10)
    
    def comprobar(respuesta):
        if respuesta == item["adjetivo"]:
            messagebox.showinfo("¡Correcto!", "Respuesta correcta ✅")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta era: {item['adjetivo']}")
        mostrar_menu()

    for opc in opciones:
        btn = tk.Button(root, text=opc, command=lambda opc=opc: comprobar(opc), width=20)
        btn.pack(pady=5)

def ejercicio_oracion():
    limpiar_pantalla()
    item = random.choice(adjetivos)
    oracion = item["oración"].replace(item["adjetivo"], "__________")
    
    tk.Label(root, text="Completa la oración con el adjetivo correcto:", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=oracion, font=("Arial", 12)).pack()
    entrada = tk.Entry(root)
    entrada.pack(pady=10)
    
    def comprobar():
        respuesta = entrada.get().strip().lower()
        if respuesta == item["adjetivo"]:
            messagebox.showinfo("¡Correcto!", "¡Muy bien! ✅")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era: {item['adjetivo']}")
        mostrar_menu()

    tk.Button(root, text="Comprobar", command=comprobar).pack(pady=10)

def ejercicio_clasificacion():
    limpiar_pantalla()
    item = random.choice(adjetivos)
    opciones = ["Cualidad", "Relación", "Gentilicio", "Procedencia"]
    random.shuffle(opciones)

    tk.Label(root, text=f"¿Qué tipo semántico tiene el adjetivo '{item['adjetivo']}'?", font=("Arial", 14)).pack(pady=10)
    
    def comprobar(tipo):
        if tipo == item["tipo"]:
            messagebox.showinfo("¡Correcto!", "¡Muy bien! ✅")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era: {item['tipo']}")
        mostrar_menu()

    for op in opciones:
        tk.Button(root, text=op, command=lambda op=op: comprobar(op)).pack(pady=5)

def redaccion():
    limpiar_pantalla()
    tk.Label(root, text="Redacción guiada", font=("Arial", 16)).pack(pady=10)
    palabras = random.sample([x["adjetivo"] for x in adjetivos], 4)
    tk.Label(root, text="Incluye al menos tres de estos adjetivos:", font=("Arial", 12)).pack()
    tk.Label(root, text=", ".join(palabras), font=("Arial", 12, "italic")).pack(pady=5)
    
    caja = tk.Text(root, height=8, width=50)
    caja.pack(pady=10)

    def enviar():
        messagebox.showinfo("¡Listo!", "Buen trabajo. Revisa tu redacción con tu profesor.")
        mostrar_menu()

    tk.Button(root, text="Terminé", command=enviar).pack(pady=5)

def mostrar_menu():
    limpiar_pantalla()
    tk.Label(root, text="MENÚ DE EJERCICIOS", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="1. Asociación", command=ejercicio_asociacion, width=30).pack(pady=5)
    tk.Button(root, text="2. Completar oración", command=ejercicio_oracion, width=30).pack(pady=5)
    tk.Button(root, text="3. Clasificación semántica", command=ejercicio_clasificacion, width=30).pack(pady=5)
    tk.Button(root, text="4. Redacción guiada", command=redaccion, width=30).pack(pady=5)
    tk.Button(root, text="Salir", command=root.quit, width=30).pack(pady=10)

def limpiar_pantalla():
    for widget in root.winfo_children():
        widget.destroy()

# Iniciar menú
mostrar_menu()
root.mainloop()
