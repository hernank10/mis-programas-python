import os
import sys
import platform
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# ==============================
#   FUNCIONES PRINCIPALES
# ==============================

def detectar_sistema():
    so = platform.system().lower()
    if "darwin" in so:
        return "macOS"
    elif "windows" in so:
        return "Windows"
    elif "linux" in so:
        if "termux" in os.environ.get("PREFIX", ""):
            return "Android (Termux)"
        else:
            return "Linux"
    else:
        return "Desconocido"

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
        return resultado.stdout + resultado.stderr
    except Exception as e:
        return str(e)

def instalar_dependencias(framework):
    archivos = {
        "Flask": "requirements/flask.txt",
        "Django": "requirements/django.txt",
        "FastAPI": "requirements/fastapi.txt",
        "Común": "requirements/common.txt"
    }
    salida = ""
    if os.path.exists(archivos[framework]):
        comando = f"{sys.executable} -m pip install -r {archivos[framework]}"
        salida += ejecutar_comando(comando)
    else:
        salida += f"Archivo de requisitos no encontrado: {archivos[framework]}\n"
    return salida

def ejecutar_proyecto(framework):
    rutas = {
        "Flask": "projects/reflex_flask",
        "Django": "projects/reflex_django",
        "FastAPI": "projects/reflex_fastapi",
        "Kotlin": "projects/reflex_kotlin"
    }
    if os.path.exists(rutas[framework]):
        if framework == "Flask":
            comando = f"cd {rutas[framework]} && flask run"
        elif framework == "Django":
            comando = f"cd {rutas[framework]} && python manage.py runserver"
        elif framework == "FastAPI":
            comando = f"cd {rutas[framework]} && uvicorn main:app --reload"
        elif framework == "Kotlin":
            comando = f"cd {rutas[framework]} && ./gradlew run"
        return ejecutar_comando(comando)
    else:
        return f"No se encontró el directorio del proyecto: {rutas[framework]}"

# ==============================
#   INTERFAZ TKINTER
# ==============================

class ReflexManagerApp:
    def __init__(self, root):
        self.root = root
        root.title("Rflex Manager – Plataforma Educativa Multiplataforma")
        root.geometry("800x600")

        ttk.Label(root, text=f"Sistema detectado: {detectar_sistema()}", font=("Arial", 12, "bold")).pack(pady=10)

        ttk.Label(root, text="Selecciona la plataforma educativa a gestionar:", font=("Arial", 11)).pack()

        self.framework = tk.StringVar(value="Flask")
        opciones = ["Flask", "Django", "FastAPI", "Kotlin"]
        ttk.Combobox(root, textvariable=self.framework, values=opciones, state="readonly").pack(pady=5)

        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Instalar Dependencias", command=self.instalar).grid(row=0, column=0, padx=10)
        ttk.Button(frame_botones, text="Ejecutar Proyecto", command=self.ejecutar).grid(row=0, column=1, padx=10)
        ttk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=10)

        ttk.Label(root, text="Salida del sistema:", font=("Arial", 11, "bold")).pack(pady=10)
        self.salida = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=20)
        self.salida.pack(padx=10, pady=5)

    def instalar(self):
        fw = self.framework.get()
        salida = instalar_dependencias(fw)
        self.salida.insert(tk.END, f"\n=== Instalando {fw} ===\n{salida}\n")
        self.salida.see(tk.END)
        messagebox.showinfo("Instalación completa", f"Dependencias de {fw} instaladas correctamente.")

    def ejecutar(self):
        fw = self.framework.get()
        salida = ejecutar_proyecto(fw)
        self.salida.insert(tk.END, f"\n=== Ejecutando {fw} ===\n{salida}\n")
        self.salida.see(tk.END)
        messagebox.showinfo("Ejecución", f"{fw} ejecutado (ver consola o navegador).")

# ==============================
#   EJECUCIÓN
# ==============================

if __name__ == "__main__":
    root = tk.Tk()
    app = ReflexManagerApp(root)
    root.mainloop()
