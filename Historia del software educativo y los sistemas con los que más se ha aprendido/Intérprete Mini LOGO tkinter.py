import tkinter as tk
from tkinter import scrolledtext
from turtle import RawTurtle, TurtleScreen

# --- 1. CONFIGURACIÓN DE LA GUI Y LA TORTUGA ---
root = tk.Tk()
root.title("Intérprete Mini LOGO")

# Crear el lienzo (Canvas) para la tortuga
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(side=tk.TOP, padx=10, pady=10)

# Crear el screen y la tortuga
t_screen = TurtleScreen(canvas)
t_screen.bgcolor("lightgray")
t = RawTurtle(t_screen)
t.shape("turtle")

# Área de Entrada y Salida
entry_field = tk.Entry(root, width=70)
entry_field.pack(side=tk.LEFT, padx=10, pady=5)
output_area = scrolledtext.ScrolledText(root, width=30, height=5)
output_area.pack(side=tk.RIGHT, padx=10, pady=5)

# --- 2. FUNCIÓN DE PROCESAMIENTO PRINCIPAL ---
def process_command(comando_bruto):
    try:
        # Simplificación: Divide el comando en tokens
        tokens = comando_bruto.upper().split()
        if not tokens:
            return
        
        cmd = tokens[0]
        args = tokens[1:]

        output_area.insert(tk.END, f"> {comando_bruto}\n")

        if cmd == "FD":
            t.forward(int(args[0]))
        elif cmd == "RT":
            t.right(int(args[0]))
        elif cmd == "PU":
            t.penup()
        elif cmd == "PD":
            t.pendown()
        # Aquí se añadiría la lógica para REPEAT, COLOR, etc.

    except Exception as e:
        output_area.insert(tk.END, f"ERROR: Sintaxis inválida o {e}\n")

# --- 3. BOTÓN DE EJECUCIÓN ---
def execute_input():
    cmd_text = entry_field.get()
    process_command(cmd_text)
    entry_field.delete(0, tk.END)

execute_button = tk.Button(root, text="Ejecutar (RUN)", command=execute_input)
execute_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
