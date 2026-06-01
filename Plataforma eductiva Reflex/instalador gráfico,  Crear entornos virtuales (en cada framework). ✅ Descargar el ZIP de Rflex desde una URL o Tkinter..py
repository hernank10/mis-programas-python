import os
import sys
import subprocess
import platform
import urllib.request
import zipfile
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# ==============================
#   CONFIGURACIÓN GLOBAL
# ==============================

RREFLEX_URL = "https://example.com/rflex_latest.zip"  # 🔧 URL del ZIP (puedes cambiarla)
PROJECTS_DIR = "projects"
VENV_DIR = "venvs"

# ==============================
#   FUNCIONES DE SISTEMA
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

def ejecutar(cmd):
    """Ejecuta un comando y devuelve su salida completa."""
    try:
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error ejecutando {cmd}: {e}"

# ==============================
#   FUNCIONES DE INSTALACIÓN
# ==============================

def crear_entorno_virtual(framework):
    ruta_venv = os.path.join(VENV_DIR, framework.lower())
    if not os.path.exists(ruta_venv):
        os.makedirs(VENV_DIR, exist_ok=True)
        salida = ejecutar(f"{sys.executable} -m venv {ruta_venv}")
        return f"Entorno virtual creado en {ruta_venv}\n{salida}"
    else:
        return f"El entorno virtual ya existe en {ruta_venv}"

def instalar_dependencias(framework):
    ruta_venv = os.path.join(VENV_DIR, framework.lower())
    requirements = f"requirements/{framework.lower()}.txt"
    if os.path.exists(requirements):
        pip_exec = os.path.join(ruta_venv, "bin", "pip") if detectar_sistema() != "Windows" else os.path.join(ruta_venv, "Scripts", "pip.exe")
        cmd = f"\"{pip_exec}\" install -r {requirements}"
        return ejecutar(cmd)
    return f"No se encontró el archivo {requirements}"

def descargar_rflex():
    """Descarga el ZIP de RFlex si no existe."""
    os.makedirs(PROJECTS_DIR, exist_ok=True)
    zip_path = os.path.join(PROJECTS_DIR, "rflex_latest.zip")

    if os.path.exists(zip_path):
        return "ZIP de RFlex ya existe, omitiendo descarga."
    try:
        urllib.request.urlretrieve(RREFLEX_URL, zip_path)
        return f"Descargado correctamente: {zip_path}"
    except Exception as e:
        return f"Error descargando ZIP: {e}"

def descomprimir_rflex():
    """Descomprime el ZIP descargado."""
    zip_path = os.path.join(PROJECTS_DIR, "rflex_latest.zip")
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(PROJECTS_DIR)
        return f"Archivo descomprimido en {PROJECTS_DIR}"
    else:
        return "No se encontró el archivo ZIP para descomprimir."

def ejecutar_proyecto(framework):
    rutas = {
        "Flask": "projects/reflex_flask",
        "Django": "projects/reflex_django",
        "FastAPI": "projects/reflex_fastapi"
    }
    ruta = rutas.get(framework)
    if not ruta or not os.path.exists(ruta):
        return f"No se encontró el directorio del proyecto {framework}."
    
    ruta_venv = os.path.join(VENV_DIR, framework.lower())
    python_exec = os.path.join(ruta_venv, "bin", "python") if detectar_sistema() != "Windows" else os.path.join(ruta_venv, "Scripts", "python.exe")
    
    if framework == "Flask":
        cmd = f"cd {ruta} && {python_exec} -m flask run"
    elif framework == "Django":
        cmd = f"cd {ruta} && {python_exec} manage.py runserver"
    elif framework == "FastAPI":
        cmd = f"cd {ruta} && {python_exec} -m uvicorn main:app --reload"
    else:
        return "Framework no soportado."
    
    return ejecutar(cmd)

# ==============================
#   INTERFAZ TKINTER
# ==============================

class ReflexInstallerApp:
    def __init__(self, root):
        self.root = root
        root.title("Rflex Installer – Instalador Multiplataforma Educativo")
        root.geometry("880x650")

        ttk.Label(root, text=f"Sistema detectado: {detectar_sistema()}", font=("Arial", 12, "bold")).pack(pady=10)
        ttk.Label(root, text="Selecciona el framework educativo a configurar:", font=("Arial", 11)).pack()

        self.framework = tk.StringVar(value="Flask")
        opciones = ["Flask", "Django", "FastAPI"]
        ttk.Combobox(root, textvariable=self.framework, values=opciones, state="readonly").pack(pady=5)

        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="1️⃣ Crear Entorno Virtual", command=self.crear_venv).grid(row=0, column=0, padx=10)
        ttk.Button(frame_botones, text="2️⃣ Instalar Dependencias", command=self.instalar).grid(row=0, column=1, padx=10)
        ttk.Button(frame_botones, text="3️⃣ Descargar y Descomprimir RFlex", command=self.descargar).grid(row=0, column=2, padx=10)
        ttk.Button(frame_botones, text="4️⃣ Ejecutar Proyecto", command=self.ejecutar).grid(row=0, column=3, padx=10)
        ttk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=4, padx=10)

        ttk.Label(root, text="🪄 Registro de salida:", font=("Arial", 11, "bold")).pack(pady=10)
        self.salida = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=25)
        self.salida.pack(padx=10, pady=5)

    def log(self, text):
        self.salida.insert(tk.END, f"{text}\n")
        self.salida.see(tk.END)

    def crear_venv(self):
        fw = self.framework.get()
        salida = crear_entorno_virtual(fw)
        self.log(salida)
        messagebox.showinfo("Entorno virtual", f"Entorno para {fw} listo.")

    def instalar(self):
        fw = self.framework.get()
        salida = instalar_dependencias(fw)
        self.log(salida)
        messagebox.showinfo("Instalación completa", f"Dependencias de {fw} instaladas.")

    def descargar(self):
        self.log(descargar_rflex())
        self.log(descomprimir_rflex())
        messagebox.showinfo("RFlex", "RFlex descargado y descomprimido correctamente.")

    def ejecutar(self):
        fw = self.framework.get()
        salida = ejecutar_proyecto(fw)
        self.log(salida)
        messagebox.showinfo("Ejecución", f"{fw} ejecutado. Ver consola o navegador.")

# ==============================
#   EJECUCIÓN
# ==============================

if __name__ == "__main__":
    root = tk.Tk()
    app = ReflexInstallerApp(root)
    root.mainloop()
