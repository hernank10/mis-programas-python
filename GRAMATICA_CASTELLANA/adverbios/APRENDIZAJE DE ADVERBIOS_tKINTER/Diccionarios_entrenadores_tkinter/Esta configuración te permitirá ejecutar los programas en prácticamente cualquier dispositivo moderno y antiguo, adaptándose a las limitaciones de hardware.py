import os
import sys
import platform
import subprocess
import json
from enum import Enum
from colorama import Fore, Style, init

init(autoreset=True)  # Para colores en la terminal

class Environment(Enum):
    MACOS = "macOS"
    WINDOWS = "Windows"
    LINUX = "Linux"
    TERMUX = "Android-Termux"
    IOS = "iOS"

class DependencyManager:
    def __init__(self):
        self.config = self.load_config()
        self.current_env = self.detect_environment()
        
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
            raise NotImplementedError("Sistema no soportado")

    def run_command(self, command, shell_type=None):
        """Ejecuta comandos adaptados a cada sistema"""
        try:
            if self.current_env == Environment.TERMUX:
                full_cmd = ['termux-chroot'] + command
            else:
                full_cmd = command
                
            result = subprocess.run(
                full_cmd,
                check=True,
                shell=shell_type or (self.current_env == Environment.WINDOWS),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print(Fore.GREEN + f"Éxito: {result.stdout}")
            return True
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error: {e.stderr}")
            return False

    def setup_venv(self):
        """Crea y activa un entorno virtual"""
        venv_path = 'venv' if self.current_env != Environment.TERMUX else 'venv-termux'
        
        if not os.path.exists(venv_path):
            print(Fore.CYAN + "Creando entorno virtual...")
            self.run_command([sys.executable, '-m', 'venv', venv_path])
        
        activate_script = {
            Environment.WINDOWS: f'{venv_path}\\Scripts\\activate.bat',
            Environment.TERMUX: f'source {venv_path}/bin/activate',
            Environment.MACOS: f'source {venv_path}/bin/activate',
            Environment.LINUX: f'source {venv_path}/bin/activate'
        }[self.current_env]
        
        print(Fore.YELLOW + f"Ejecuta: {activate_script} para activar el entorno")

    def install_dependencies(self):
        """Instala dependencias específicas para cada entorno"""
        env_deps = self.config[str(self.current_env.value)]
        
        print(Fore.BLUE + f"Instalando dependencias para {self.current_env.value}...")
        
        # Instalar paquetes del sistema primero
        if 'system_packages' in env_deps:
            pkg_manager = {
                Environment.MACOS: 'brew',
                Environment.LINUX: 'apt-get',
                Environment.TERMUX: 'pkg',
                Environment.WINDOWS: 'choco'
            }[self.current_env]
            
            for pkg in env_deps['system_packages']:
                install_cmd = {
                    'brew': ['brew', 'install', pkg],
                    'apt-get': ['sudo', 'apt-get', 'install', '-y', pkg],
                    'pkg': ['pkg', 'install', '-y', pkg],
                    'choco': ['choco', 'install', '-y', pkg]
                }[pkg_manager]
                
                self.run_command(install_cmd)

        # Instalar paquetes Python
        self.setup_venv()
        pip_cmd = [
            'pip', 'install', 
            '--no-cache-dir', 
            '--prefix=${PREFIX}' if self.current_env == Environment.TERMUX else '',
            *env_deps['python_packages']
        ]
        self.run_command(pip_cmd)

    def run_application(self, app_type):
        """Ejecuta la aplicación adecuada para el entorno"""
        entry_points = {
            'tkinter': ['python', 'tkinter_app.py'],
            'kivy': ['python', 'kivy_app.py'],
            'fastapi': ['uvicorn', 'fastapi_app:app', '--host', '0.0.0.0']
        }
        
        if self.current_env == Environment.TERMUX:
            print(Fore.MAGENTA + "Iniciando servicio en Termux...")
            self.run_command(['termux-wake-lock'])
            self.run_command(['termux-notification', '-t', 'Laboratorio Rural'])
        
        self.run_command(entry_points[app_type])

    def configure_ios(self):
        """Guía de configuración para iOS"""
        print(Fore.CYAN + """
        Configuración para iOS:
        1. Instalar Pythonista desde App Store
        2. Conectar el dispositivo a la computadora
        3. Copiar los archivos vía iTunes File Sharing
        4. Ejecutar manualmente desde Pythonista
        """)

if __name__ == "__main__":
    manager = DependencyManager()
    
    print(Fore.YELLOW + f"Entorno detectado: {manager.current_env.value}")
    
    # Menú interactivo
    while True:
        print(f"\n{Fore.CYAN}Menú Principal:")
        print("1. Instalar dependencias")
        print("2. Ejecutar aplicación Tkinter")
        print("3. Ejecutar aplicación Kivy")
        print("4. Ejecutar API FastAPI")
        print("5. Configurar iOS")
        print("6. Salir")
        
        choice = input(f"{Fore.GREEN}Selecciona una opción: ")
        
        if choice == '1':
            manager.install_dependencies()
        elif choice == '2':
            manager.run_application('tkinter')
        elif choice == '3':
            manager.run_application('kivy')
        elif choice == '4':
            manager.run_application('fastapi')
        elif choice == '5':
            manager.configure_ios()
        elif choice == '6':
            break
        else:
            print(Fore.RED + "Opción no válida")
