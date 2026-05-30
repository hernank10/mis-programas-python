import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import platform
import subprocess
import json
import threading
from enum import Enum
import sys
import os

class Environment(Enum):
    MACOS = "macOS"
    WINDOWS = "Windows"
    LINUX = "Linux"
    TERMUX = "Android-Termux"
    IOS = "iOS"

class DependencyManagerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor Científico Rural")
        self.geometry("800x600")
        self.config = self.load_config()
        self.current_env = self.detect_environment()
        self.running_process = None
        self.create_widgets()
        self.setup_style()
        
    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        
    def load_config(self):
        with open('dependencies.json') as f:
            return json.load(f)
    
    def detect_environment(self):
        system = platform.system()
        if 'ANDROID_ROOT' in os.environ:
            return Environment.TERMUX
        elif system == 'Darwin':
            return Environment.MACOS
        elif system == 'Windows':
            return Environment.WINDOWS
        elif system == 'Linux':
            return Environment.LINUX
        else:
            return Environment.IOS
    
    def create_widgets(self):
        # Panel superior
        header_frame = ttk.Frame(self)
        header_frame.pack(pady=10, fill=tk.X)
        
        ttk.Label(header_frame, 
                text=f"Entorno detectado: {self.current_env.value}",
                style='Header.TLabel').pack(side=tk.LEFT)
        
        # Panel principal
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Panel de control
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        ttk.Button(control_frame, 
                 text="Instalar Dependencias",
                 command=self.start_install).pack(pady=5, fill=tk.X)
        
        ttk.Button(control_frame,
                 text="Ejecutar Tkinter",
                 command=lambda: self.start_app('tkinter')).pack(pady=5, fill=tk.X)
        
        ttk.Button(control_frame,
                 text="Ejecutar Kivy",
                 command=lambda: self.start_app('kivy')).pack(pady=5, fill=tk.X)
        
        ttk.Button(control_frame,
                 text="Ejecutar FastAPI",
                 command=lambda: self.start_app('fastapi')).pack(pady=5, fill=tk.X)
        
        ttk.Button(control_frame,
                 text="Configurar iOS",
                 command=self.show_ios_guide).pack(pady=5, fill=tk.X)
        
        # Consola de salida
        self.console = scrolledtext.ScrolledText(main_frame, 
                                               wrap=tk.WORD,
                                               state='disabled')
        self.console.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Barra de estado
        self.status = ttk.Label(self, text="Listo")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def log(self, message, color="black"):
        self.console.configure(state='normal')
        self.console.insert(tk.END, message + "\n", color)
        self.console.configure(state='disabled')
        self.console.see(tk.END)
    
    def run_command(self, command):
        def thread_target():
            try:
                self.status.config(text="Ejecutando...")
                process = subprocess.Popen(command,
                                         shell=True,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT,
                                         text=True)
                
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        self.log(output.strip(), "green" if process.returncode == 0 else "red")
                
                self.status.config(text="Completado")
            except Exception as e:
                self.log(f"Error: {str(e)}", "red")
                self.status.config(text="Error")
        
        threading.Thread(target=thread_target, daemon=True).start()
    
    def start_install(self):
        env_deps = self.config[str(self.current_env.value)]
        commands = []
        
        # Comandos del sistema
        if 'system_packages' in env_deps:
            pkg_manager = {
                Environment.MACOS: 'brew',
                Environment.LINUX: 'sudo apt-get',
                Environment.TERMUX: 'pkg',
                Environment.WINDOWS: 'choco'
            }[self.current_env]
            
            for pkg in env_deps['system_packages']:
                cmd = {
                    'brew': f'brew install {pkg}',
                    'sudo apt-get': f'sudo apt-get install -y {pkg}',
                    'pkg': f'pkg install -y {pkg}',
                    'choco': f'choco install -y {pkg}'
                }[pkg_manager]
                commands.append(cmd)
        
        # Comandos Python
        commands.append(f'"{sys.executable}" -m pip install --upgrade pip')
        commands.append(f'"{sys.executable}" -m pip install {" ".join(env_deps["python_packages"])}')
        
        full_command = " && ".join(commands)
        self.run_command(full_command)
    
    def start_app(self, app_type):
        entry_points = {
            'tkinter': f'"{sys.executable}" tkinter_app.py',
            'kivy': f'"{sys.executable}" kivy_app.py',
            'fastapi': f'"{sys.executable}" -m uvicorn fastapi_app:app --host 0.0.0.0'
        }
        self.run_command(entry_points[app_type])
    
    def show_ios_guide(self):
        guide = """
        Configuración para iOS:
        1. Instalar Pythonista desde App Store ($9.99)
        2. Conectar el dispositivo a la computadora
        3. Copiar los archivos vía iTunes File Sharing
        4. Abrir main.py en Pythonista
        5. Ejecutar manualmente desde el editor
        """
        messagebox.showinfo("Guía iOS", guide)
    
    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de querer salir?"):
            if self.running_process:
                self.running_process.terminate()
            self.destroy()

if __name__ == "__main__":
    app = DependencyManagerGUI()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
