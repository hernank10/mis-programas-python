# Creating rflex_manager_gui.zip with installer, requirements, assets, and including existing rflex_scaffold.zip as rflex_latest.zip
import os, shutil, zipfile, textwrap, pathlib, sys

BASE_DIR = "/mnt/data/rflex_manager_gui"
os.makedirs(BASE_DIR, exist_ok=True)

def write_file(path, content):
    full = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# 1) rflex_installer.py (Tkinter GUI installer that downloads/extracts and creates venvs)
rflex_installer_code = r'''#!/usr/bin/env python3
# Rflex Manager Installer GUI
import os, sys, platform, subprocess, urllib.request, zipfile
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Config
RREFLEX_URL = ""  # leave empty to use local projects/rflex_latest.zip if present
PROJECTS_DIR = "projects"
VENV_DIR = "venvs"
REQUIREMENTS_DIR = "requirements"

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
    return "Desconocido"

def ejecutar(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True, cwd=cwd)
        out = result.stdout or \"\"
        err = result.stderr or \"\"
        return out + err
    except Exception as e:
        return str(e)

def crear_entorno_virtual(framework):
    ruta_venv = os.path.join(VENV_DIR, framework.lower())
    if not os.path.exists(ruta_venv):
        os.makedirs(VENV_DIR, exist_ok=True)
        cmd = f\"{sys.executable} -m venv {ruta_venv}\"
        return ejecutar(cmd)
    return \"Entorno virtual ya existe.\"

def instalar_dependencias(framework):
    req_file = os.path.join(REQUIREMENTS_DIR, f\"{framework.lower()}.txt\")
    if not os.path.exists(req_file):
        return f\"No existe {req_file}\"\n
    # choose pip inside venv if available
    venv_pip = os.path.join(VENV_DIR, framework.lower(), 'bin', 'pip') if detectar_sistema()!='Windows' else os.path.join(VENV_DIR, framework.lower(), 'Scripts', 'pip.exe')
    if os.path.exists(venv_pip):
        cmd = f'\"{venv_pip}\" install -r \"{req_file}\"'
    else:
        cmd = f'\"{sys.executable}\" -m pip install -r \"{req_file}\"'
    return ejecutar(cmd)

def descargar_rflex():
    os.makedirs(PROJECTS_DIR, exist_ok=True)
    zip_path = os.path.join(PROJECTS_DIR, 'rflex_latest.zip')
    if os.path.exists(zip_path):
        return 'rflex_latest.zip ya existe, omitiendo descarga.'
    if not RREFLEX_URL:
        return 'No se proporcionó URL de descarga y no existe rflex_latest.zip local.'
    try:
        urllib.request.urlretrieve(RREFLEX_URL, zip_path)
        return f'Descargado: {zip_path}'
    except Exception as e:
        return f'Error al descargar: {e}'

def descomprimir_rflex():
    zip_path = os.path.join(PROJECTS_DIR, 'rflex_latest.zip')
    if not os.path.exists(zip_path):
        return 'No se encontró rflex_latest.zip en projects/'
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(PROJECTS_DIR)
        return f'Extraído en {PROJECTS_DIR}'
    except Exception as e:
        return f'Error al extraer: {e}'

def ejecutar_proyecto(framework):
    map_paths = {
        'Flask': os.path.join(PROJECTS_DIR, 'flask_app'),
        'Django': os.path.join(PROJECTS_DIR, 'django_app'),
        'FastAPI': os.path.join(PROJECTS_DIR, 'fastapi_app'),
    }
    proj = map_paths.get(framework)
    if not proj or not os.path.exists(proj):
        return f'No se encontró el proyecto {framework} en {proj}'
    # use venv python if exists
    venv_py = os.path.join(VENV_DIR, framework.lower(), 'bin', 'python') if detectar_sistema()!='Windows' else os.path.join(VENV_DIR, framework.lower(), 'Scripts', 'python.exe')
    if framework=='Flask':
        # Ensure FLASK_APP env or run app.py directly
        app_py = os.path.join(proj, 'app.py')
        if os.path.exists(app_py):
            cmd = f'\"{venv_py}\" \"{app_py}\"' if os.path.exists(venv_py) else f'\"{sys.executable}\" \"{app_py}\"'
            return ejecutar(cmd, cwd=proj)
        return 'No se encontró app.py para Flask.'
    if framework=='Django':
        manage = os.path.join(proj, 'manage.py')
        if os.path.exists(manage):
            cmd = f'\"{venv_py}\" \"{manage}\" runserver' if os.path.exists(venv_py) else f'\"{sys.executable}\" \"{manage}\" runserver'
            return ejecutar(cmd, cwd=proj)
        return 'No se encontró manage.py para Django.'
    if framework=='FastAPI':
        main_py = os.path.join(proj, 'app', 'main.py')
        if os.path.exists(main_py):
            cmd = f'\"{venv_py}\" -m uvicorn app.main:app --reload' if os.path.exists(venv_py) else f'\"{sys.executable}\" -m uvicorn app.main:app --reload'
            return ejecutar(cmd, cwd=proj)
        return 'No se encontró main.py para FastAPI.'
    return 'Framework no soportado.'

class RflexGUI:
    def __init__(self, root):
        self.root = root
        root.title('Rflex Manager GUI')
        root.geometry('880x640')
        ttk.Label(root, text=f'Sistema: {detectar_sistema()}', font=('Arial', 12, 'bold')).pack(pady=8)
        ttk.Label(root, text='Framework:', font=('Arial', 10)).pack()
        self.framework = tk.StringVar(value='Flask')
        ttk.Combobox(root, textvariable=self.framework, values=['Flask','Django','FastAPI'], state='readonly').pack(pady=6)
        frame = ttk.Frame(root)
        frame.pack(pady=6)
        ttk.Button(frame, text='Crear venv', command=self.cmd_crear_venv).grid(row=0,column=0,padx=6)
        ttk.Button(frame, text='Instalar dependencias', command=self.cmd_instalar).grid(row=0,column=1,padx=6)
        ttk.Button(frame, text='Descargar RFlex (si URL)', command=self.cmd_descargar).grid(row=0,column=2,padx=6)
        ttk.Button(frame, text='Descomprimir RFlex', command=self.cmd_descomprimir).grid(row=0,column=3,padx=6)
        ttk.Button(frame, text='Ejecutar proyecto', command=self.cmd_ejecutar).grid(row=0,column=4,padx=6)
        ttk.Button(frame, text='Salir', command=root.quit).grid(row=0,column=5,padx=6)
        ttk.Label(root, text='Salida / Logs:', font=('Arial', 11, 'bold')).pack(pady=6)
        self.out = scrolledtext.ScrolledText(root, width=110, height=30)
        self.out.pack(padx=8, pady=6)
    def log(self, s):
        self.out.insert('end', s + '\n')
        self.out.see('end')
    def cmd_crear_venv(self):
        fw = self.framework.get()
        s = crear_entorno_virtual(fw)
        self.log(s)
        messagebox.showinfo('Info', 'Operación completada.')
    def cmd_instalar(self):
        fw = self.framework.get()
        s = instalar_dependencias(fw)
        self.log(s)
        messagebox.showinfo('Info', 'Instalación finalizada.')
    def cmd_descargar(self):
        s = descargar_rflex()
        self.log(s)
        messagebox.showinfo('Info', 'Descarga (o verificación) completa.')
    def cmd_descomprimir(self):
        s = descomprimir_rflex()
        self.log(s)
        messagebox.showinfo('Info', 'Extracción completa.')
    def cmd_ejecutar(self):
        fw = self.framework.get()
        s = ejecutar_proyecto(fw)
        self.log(s)
        messagebox.showinfo('Info', 'Ejecución iniciada (revisa logs).')

if __name__ == '__main__':
    root = tk.Tk()
    import tkinter.ttk as ttk
    app = RflexGUI(root)
    root.mainloop()
'''

write_path = os.path.join(BASE_DIR, "rflex_installer.py")
with open(write_path, "w", encoding="utf-8") as f:
    f.write(rflex_installer_code)

# 2) requirements files
req_flask = "Flask==2.2.5\nJinja2>=3.1\nWerkzeug>=2.2\n"
req_django = "Django>=4.2\ndjangorestframework>=3.14\n"
req_fastapi = "fastapi>=0.95\nuvicorn[standard]>=0.22\nsqlmodel>=0.0.8\n"

write_file = lambda p, c: open(os.path.join(BASE_DIR, p), "w", encoding="utf-8").write(c)
write_file("requirements/flask.txt", req_flask)
write_file("requirements/django.txt", req_django)
write_file("requirements/fastapi.txt", req_fastapi)

# 3) create projects dir and include existing rflex_scaffold.zip if present
projects_dir = os.path.join(BASE_DIR, "projects")
os.makedirs(projects_dir, exist_ok=True)
src_zip = "/mnt/data/rflex_scaffold.zip"
dst_zip = os.path.join(projects_dir, "rflex_latest.zip")
if os.path.exists(src_zip):
    shutil.copy(src_zip, dst_zip)
else:
    # create a small placeholder zip
    ph = os.path.join(projects_dir, "rflex_latest.zip")
    with zipfile.ZipFile(ph, "w") as z:
        z.writestr("README.txt", "Placeholder RFlex project. Replace with your real rflex_latest.zip")
# 4) add simple README and assets
write_file("README.md", "# Rflex Manager GUI\n\nUse rflex_installer.py to manage projects.\n")
os.makedirs(os.path.join(BASE_DIR, "assets"), exist_ok=True)
open(os.path.join(BASE_DIR, "assets", "logo.png"), "wb").write(b"")  # empty placeholder

# 5) create the final zip
zip_out = "/mnt/data/rflex_manager_gui.zip"
with zipfile.ZipFile(zip_out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(BASE_DIR):
        for fn in files:
            full = os.path.join(root, fn)
            arc = os.path.relpath(full, BASE_DIR)
            zf.write(full, arc)

zip_out

