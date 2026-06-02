#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
INSTALADOR AUTOMÁTICO - mis-programas-python
Ecosistema educativo para aprender Latín, Inglés y Español

Sistemas soportados:
- Windows 10/11
- macOS 10.13+
- Linux (Ubuntu/Debian/Fedora/Arch)
- Android (Termux/Pydroid)
"""

import os
import sys
import platform
import subprocess
import shutil
import tempfile
import zipfile
import json
from pathlib import Path

# Colores para terminal (ANSI)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """Mostrar banner del instalador"""
    print(Colors.HEADER + """
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║     🐍 MIS PROGRAMAS PYTHON - INSTALADOR AUTOMÁTICO 🐍           ║
    ║                                                                  ║
    ║     Ecosistema educativo para aprender Latín, Inglés y Español   ║
    ║     +1,300 programas | +700 lecciones HTML                       ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """ + Colors.END)

def print_step(step, message):
    """Mostrar paso del instalador"""
    print(Colors.BLUE + f"\n📍 {step}. {message}" + Colors.END)

def print_success(message):
    """Mostrar mensaje de éxito"""
    print(Colors.GREEN + f"✅ {message}" + Colors.END)

def print_warning(message):
    """Mostrar mensaje de advertencia"""
    print(Colors.YELLOW + f"⚠️ {message}" + Colors.END)

def print_error(message):
    """Mostrar mensaje de error"""
    print(Colors.RED + f"❌ {message}" + Colors.END)

def get_system_info():
    """Detectar sistema operativo"""
    system = platform.system()
    version = platform.version()
    arch = platform.machine()
    
    info = {
        "os": system,
        "version": version,
        "arch": arch,
        "is_termux": "com.termux" in os.environ.get("PREFIX", ""),
        "is_pydroid": "pydroid" in sys.executable.lower()
    }
    
    return info

def check_python():
    """Verificar versión de Python"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print_success(f"Python {version.major}.{version.minor}.{version.micro} detectado")
        return True
    else:
        print_error(f"Python {version.major}.{version.minor} no es compatible. Se necesita Python 3.7+")
        return False

def install_pip_packages():
    """Instalar paquetes de pip necesarios"""
    packages = [
        "colorama",  # Colores en terminal
        "nltk",      # Procesamiento de lenguaje natural
    ]
    
    print_step(2, "Instalando paquetes de Python")
    
    for package in packages:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package], 
                          check=True, capture_output=True)
            print_success(f"Instalado: {package}")
        except subprocess.CalledProcessError:
            print_warning(f"No se pudo instalar {package}, pero los juegos seguirán funcionando")

def clone_or_pull_repo(repo_url, repo_name, target_dir):
    """Clonar o actualizar repositorio"""
    repo_path = Path(target_dir) / repo_name
    
    if repo_path.exists():
        print(f"   Actualizando {repo_name}...")
        try:
            subprocess.run(["git", "-C", str(repo_path), "pull"], check=True, capture_output=True)
            print_success(f"Actualizado: {repo_name}")
        except:
            print_warning(f"No se pudo actualizar {repo_name}, usando versión existente")
    else:
        print(f"   Clonando {repo_name}...")
        try:
            subprocess.run(["git", "clone", repo_url, str(repo_path)], check=True, capture_output=True)
            print_success(f"Clonado: {repo_name}")
        except subprocess.CalledProcessError as e:
            print_error(f"No se pudo clonar {repo_name}: {e}")
            return False
    return True

def create_launcher_scripts(target_dir):
    """Crear scripts de lanzamiento para cada sistema"""
    repo_path = Path(target_dir) / "mis-programas-python"
    
    # Script para Windows (batch)
    if platform.system() == "Windows":
        bat_path = repo_path / "ejecutar_menu.bat"
        bat_content = f'''@echo off
echo ========================================
echo    MIS PROGRAMAS PYTHON
echo ========================================
echo.
cd "{repo_path}"
python menu_principal.py
pause
'''
        bat_path.write_text(bat_content)
        print_success("Creado: ejecutar_menu.bat")
    
    # Script para Unix (Mac/Linux/Termux)
    sh_path = repo_path / "ejecutar_menu.sh"
    sh_content = f'''#!/bin/bash
echo "========================================"
echo "   MIS PROGRAMAS PYTHON"
echo "========================================"
echo ""
cd "{repo_path}"
python3 menu_principal.py
'''
    sh_path.write_text(sh_content)
    sh_path.chmod(0o755)
    print_success("Creado: ejecutar_menu.sh")

def create_desktop_entry():
    """Crear acceso directo en el escritorio (Linux/Mac)"""
    if platform.system() == "Linux":
        desktop_path = Path.home() / ".local/share/applications/mis-programas-python.desktop"
        desktop_content = f'''[Desktop Entry]
Name=Mis Programas Python
Comment=Ecosistema educativo para aprender idiomas
Exec={os.getcwd()}/mis-programas-python/ejecutar_menu.sh
Icon=applications-education
Terminal=true
Type=Application
Categories=Education;Development;
'''
        desktop_path.write_text(desktop_content)
        print_success("Creado acceso directo en el menú de aplicaciones")

def install_android_termux(target_dir):
    """Instalación específica para Termux"""
    print_step(5, "Configurando para Termux")
    
    # Dar permisos de almacenamiento
    subprocess.run(["termux-setup-storage"], shell=True)
    
    # Instalar dependencias adicionales de Termux
    subprocess.run(["pkg", "install", "python", "git", "-y"], capture_output=True)
    print_success("Dependencias de Termux instaladas")

def generate_quick_guide(target_dir):
    """Generar guía rápida de uso"""
    guide_path = Path(target_dir) / "mis-programas-python" / "GUIA_RAPIDA_USO.txt"
    
    guide_content = """
═══════════════════════════════════════════════════════════════════
                    GUÍA RÁPIDA DE USO
              mis-programas-python - Ecosistema Educativo
═══════════════════════════════════════════════════════════════════

📖 ¿QUÉ TIENES INSTALADO?

  ✓ +1,300 programas Python para aprender idiomas
  ✓ +700 lecciones HTML interactivas
  ✓ 70+ juegos de texto educativos
  ✓ 31 programas de inglés
  ✓ 500+ programas de gramática española
  ✓ 10+ programas de latín

🚀 CÓMO EJECUTAR

  ▶ Menú principal:
     ./ejecutar_menu.sh (Mac/Linux)
     ejecutar_menu.bat   (Windows)
     python menu_principal.py

  ▶ Juegos de texto:
     cd "JUEGOS_DE_TEXTO_ PLANETAS _BIBLIOTECA_colorama"
     python tomson_ciudad_salvaje.py

  ▶ Ver lecciones HTML:
     cd mini-htmls-educativos
     python -m http.server 8000
     Luego abre http://localhost:8000 en tu navegador

📁 ESTRUCTURA

  📂 LATIN/                    → Programas de latín
  📂 INGLES/                   → Programas de inglés
  📂 GRAMATICA_CASTELLANA/     → Gramática española
  📂 NUEVOS JUEGOS II/         → Juegos educativos
  📂 JUEGOS_DE_TEXTO_.../      → 70+ juegos interactivos
  📂 mini-htmls-educativos/    → Lecciones HTML
  📂 INVESTIGACION_PEDAGOGICA/ → Documentos académicos

💡 CONSEJOS

  • Usa python3 en lugar de python en Mac/Linux
  • Los juegos de texto funcionan en cualquier terminal
  • Las lecciones HTML se ven mejor en Chrome/Firefox
  • Para salir de un juego: Ctrl+C

🐛 SOLUCIÓN DE PROBLEMAS

  Error "colorama no encontrado":
     pip install colorama

  Error "git no encontrado":
     Instala Git desde git-scm.com

  Los juegos no se ven en Android:
     Usa Pydroid 3 o Termux

═══════════════════════════════════════════════════════════════════
  📧 Soporte: https://github.com/Hernank10/mis-programas-python
  ⭐ ¡Dale una estrella al proyecto en GitHub!
═══════════════════════════════════════════════════════════════════
"""
    guide_path.write_text(guide_content)
    print_success("Generada guía rápida: GUIA_RAPIDA_USO.txt")

def main():
    """Función principal del instalador"""
    print_banner()
    
    # Detectar sistema
    system_info = get_system_info()
    print(f"\n📊 Sistema detectado: {system_info['os']} {system_info['arch']}")
    
    # Verificar Python
    if not check_python():
        sys.exit(1)
    
    # Directorio de instalación
    default_dir = str(Path.home() / "mis_programas_python")
    print(f"\n📁 Directorio de instalación predeterminado: {default_dir}")
    install_dir = input("¿Usar este directorio? (Enter para sí, o escribe ruta diferente): ").strip()
    
    if not install_dir:
        install_dir = default_dir
    
    Path(install_dir).mkdir(parents=True, exist_ok=True)
    print_success(f"Instalando en: {install_dir}")
    
    # Instalar paquetes pip
    install_pip_packages()
    
    # Clonar repositorios
    print_step(3, "Clonando repositorios")
    
    repos = [
        ("https://github.com/Hernank10/mis-programas-python.git", "mis-programas-python"),
        ("https://github.com/Hernank10/mini-htmls-educativos.git", "mini-htmls-educativos")
    ]
    
    for repo_url, repo_name in repos:
        clone_or_pull_repo(repo_url, repo_name, install_dir)
    
    # Configuración específica por sistema
    if system_info["is_termux"]:
        install_android_termux(install_dir)
    
    # Crear lanzadores
    print_step(4, "Creando lanzadores")
    create_launcher_scripts(install_dir)
    
    # Crear acceso directo (Linux)
    if platform.system() == "Linux" and not system_info["is_termux"]:
        create_desktop_entry()
    
    # Generar guía
    generate_quick_guide(install_dir)
    
    # Resumen final
    print("\n" + "="*60)
    print(Colors.GREEN + "🎉 ¡INSTALACIÓN COMPLETADA CON ÉXITO! 🎉" + Colors.END)
    print("="*60)
    print(f"""
📁 Ubicación: {install_dir}/mis-programas-python

🚀 Para comenzar:

  Windows:
    cd {install_dir}\\mis-programas-python
    ejecutar_menu.bat

  Mac/Linux/Termux:
    cd {install_dir}/mis-programas-python
    ./ejecutar_menu.sh

📖 Ver lecciones HTML:
    cd {install_dir}/mini-htmls-educativos
    python -m http.server 8000
    Luego abre http://localhost:8000 en tu navegador

🎮 Jugar juegos de texto:
    cd "{install_dir}/mis-programas-python/JUEGOS_DE_TEXTO_ PLANETAS _BIBLIOTECA_colorama"
    python tomson_ciudad_salvaje.py

📚 Consulta la guía rápida en:
    {install_dir}/mis-programas-python/GUIA_RAPIDA_USO.txt

⭐ ¡Dale una estrella al proyecto en GitHub!
   https://github.com/Hernank10/mis-programas-python
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_warning("\n\nInstalación cancelada por el usuario")
        sys.exit(0)
    except Exception as e:
        print_error(f"\nError inesperado: {e}")
        sys.exit(1)
