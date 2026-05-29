import os
import sys
import subprocess
from pathlib import Path
from time import sleep

# Configuración para macOS
PYTHON_VERSION = "3.10"
VENV_NAME = "nlp-env"
REQUIREMENTS = [
    "spacy==3.5.0",
    "fastapi==0.95.0",
    "uvicorn==0.21.1",
    "python-dotenv==1.0.0",
    "tkinterweb==3.12.0"
]

class MacInstaller:
    def __init__(self):
        self.home_dir = str(Path.home())
        self.venv_path = Path(self.home_dir) / VENV_NAME
        self.brew_path = "/usr/local/bin/brew"
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'reset': '\033[0m'
        }
        
    def print_color(self, text, color):
        print(f"{self.colors[color]}{text}{self.colors['reset']}")

    def run_command(self, command, check=True):
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=check,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            return False, e.stderr

    def install_homebrew(self):
        self.print_color("\nVerificando Homebrew...", "yellow")
        if not Path(self.brew_path).exists():
            self.print_color("Instalando Homebrew...", "yellow")
            command = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
            success, output = self.run_command(command)
            if not success:
                self.print_color("Error instalando Homebrew", "red")
                sys.exit(1)
            self.print_color("Homebrew instalado correctamente", "green")
            
    def install_python(self):
        self.print_color("\nVerificando Python 3.10...", "yellow")
        command = f'brew list python@{PYTHON_VERSION}'
        success, _ = self.run_command(command, check=False)
        if not success:
            self.print_color(f"Instalando Python {PYTHON_VERSION}...", "yellow")
            commands = [
                'brew update',
                f'brew install python@{PYTHON_VERSION}',
                'brew link --overwrite python@3.10'
            ]
            for cmd in commands:
                success, output = self.run_command(cmd)
                if not success:
                    self.print_color(f"Error en: {cmd}", "red")
                    sys.exit(1)
            self.print_color("Python instalado correctamente", "green")
            
    def setup_venv(self):
        self.print_color("\nConfigurando entorno virtual...", "yellow")
        if not self.venv_path.exists():
            python_bin = f"/usr/local/opt/python@{PYTHON_VERSION}/bin/python3"
            success, _ = self.run_command(f'{python_bin} -m venv {self.venv_path}')
            if success:
                self.print_color("Entorno virtual creado", "green")
            else:
                self.print_color("Error creando entorno virtual", "red")
                sys.exit(1)
                
    def install_dependencies(self):
        self.print_color("\nInstalando dependencias...", "yellow")
        pip_path = self.venv_path / "bin" / "pip"
        commands = [
            f'{pip_path} install --upgrade pip',
            f'{pip_path} install {" ".join(REQUIREMENTS)}',
            f'{pip_path} install https://github.com/explosion/spacy-models/releases/download/es_core_news_sm-3.5.0/es_core_news_sm-3.5.0.tar.gz'
        ]
        for cmd in commands:
            self.print_color(f"Ejecutando: {cmd}", "yellow")
            success, output = self.run_command(cmd)
            if success:
                self.print_color("Dependencias instaladas", "green")
            else:
                self.print_color(f"Error instalando dependencias: {output}", "red")
                sys.exit(1)
                
    def configure_tkinter(self):
        self.print_color("\nConfigurando Tkinter...", "yellow")
        tcl_path = "/usr/local/opt/tcl-tk"
        if not Path(tcl_path).exists():
            self.print_color("Instalando Tcl-Tk...", "yellow")
            success, _ = self.run_command("brew install tcl-tk")
            if not success:
                self.print_color("Error instalando Tcl-Tk", "red")
                sys.exit(1)
                
        # Configurar variables de entorno
        env_vars = f"""
export PATH="/usr/local/opt/tcl-tk/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
export PKG_CONFIG_PATH="/usr/local/opt/tcl-tk/lib/pkgconfig"
        """
        with open(f"{self.home_dir}/.zshrc", "a") as f:
            f.write(env_vars)
            
        self.print_color("Tkinter configurado correctamente", "green")
        
    def verify_installation(self):
        self.print_color("\nVerificando instalación...", "yellow")
        checks = [
            (f"{self.venv_path}/bin/python", "Python"),
            (f"{self.venv_path}/lib/python{PYTHON_VERSION}/site-packages/spacy", "spaCy"),
            (f"{self.venv_path}/lib/python{PYTHON_VERSION}/site-packages/tkinter", "Tkinter")
        ]
        for path, name in checks:
            if not Path(path).exists():
                self.print_color(f"Error: {name} no está instalado correctamente", "red")
                sys.exit(1)
        self.print_color("Todas las verificaciones pasaron con éxito!", "green")
        
    def post_install(self):
        self.print_color("\nInstalación completada!", "green")
        print(f"\nPara activar el entorno virtual ejecuta:")
        print(f"source {self.venv_path}/bin/activate")
        print("\nPara iniciar el servidor de desarrollo:")
        print(f"{self.venv_path}/bin/uvicorn main:app --reload")

    def run(self):
        try:
            self.install_homebrew()
            self.install_python()
            self.setup_venv()
            self.install_dependencies()
            self.configure_tkinter()
            self.verify_installation()
            self.post_install()
        except KeyboardInterrupt:
            self.print_color("\nInstalación cancelada por el usuario", "red")
            sys.exit(1)

if __name__ == "__main__":
    installer = MacInstaller()
    installer.run()
