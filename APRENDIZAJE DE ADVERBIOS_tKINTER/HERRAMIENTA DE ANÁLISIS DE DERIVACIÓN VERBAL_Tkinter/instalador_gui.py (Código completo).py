import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

# Dependencias necesarias
DEPENDENCIAS = ["pyttsx3"]

def instalar_dependencias():
    for paquete in DEPENDENCIAS:
        try:
            __import__(paquete)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])

def verificar_archivos():
    if not os.path.exists("datos.json"):
        with open("datos.json", "w", encoding="utf-8") as f:
            f.write("{}")
    if not os.path.exists("programa.py"):
        with open("programa.py", "w", encoding="utf-8") as f:
            f.write("# Aquí iría el código del programa principal.")

def lanzar_programa():
    try:
        subprocess.Popen([sys.executable, "programa.py"])
    except Exception as e:
        messagebox.showerror("Error al ejecutar", str(e))

def instalar_y_lanzar():
    try:
        instalar_dependencias()
        verificar_archivos()
        messagebox.showinfo("Listo", "Instalación completa. Iniciando el programa...")
        lanzar_programa()
    except Exception as e:
        messagebox.showerror("Error", f"Algo salió mal:\n{e}")

# Interfaz Tkinter
ventana = tk.Tk()
ventana.title("Instalador Ortográfico")
ventana.geometry("400x250")

titulo = tk.Label(ventana, text="🧠 Instalador del Programa Ortográfico", font=("Arial", 14), pady=20)
titulo.pack()

boton_instalar = tk.Button(ventana, text="📥 Instalar y Ejecutar", command=instalar_y_lanzar, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=10)
boton_instalar.pack(pady=20)

ventana.mainloop()
