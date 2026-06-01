import os
import sys
import subprocess
import platform
import json
from datetime import datetime

# ==============================
# CONFIGURACIÓN GLOBAL
# ==============================

DEPENDENCIAS = [
    "django",
    "fastapi",
    "uvicorn",
    "reflex",
    "psycopg2-binary",
    "reportlab",
    "pdfkit",
    "pandas",
    "openpyxl",
    "python-docx",
    "python-pptx",
    "odfpy",
    "pypandoc",
    "requests",
    "difflib",
    "flask-socketio",
    "websockets",
    "aiohttp",
    "PyJWT",
    "python-dotenv"
]

LOG_FILE = "edu_installer_log.json"

# ==============================
# FUNCIONES UTILITARIAS
# ==============================

def ejecutar_comando(comando):
    """Ejecuta un comando del sistema y devuelve el resultado."""
    try:
        resultado = subprocess.run(
            comando, shell=True, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando: {comando}")
        print(e.stderr)
        return None


def instalar_dependencia(paquete):
    """Instala o actualiza una dependencia de Python."""
    print(f"📦 Instalando/verificando {paquete}...")
    return ejecutar_comando(f"{sys.executable} -m pip install --upgrade {paquete}")


def verificar_dependencia(paquete):
    """Verifica si una dependencia está instalada."""
    try:
        __import__(paquete.split('==')[0])
        print(f"✅ {paquete} ya está instalada.")
        return True
    except ImportError:
        print(f"⚠️ {paquete} no está instalada.")
        return False


def guardar_log(accion, detalle):
    """Registra la actividad en un archivo JSON."""
    log = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "accion": accion,
        "detalle": detalle
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    logs.append(log)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def detectar_sistema():
    """Detecta el sistema operativo actual."""
    so = platform.system().lower()
    print(f"💻 Sistema detectado: {so}")
    if "darwin" in so:
        return "macOS"
    elif "windows" in so:
        return "Windows"
    elif "linux" in so:
        if "android" in platform.platform().lower():
            return "Termux/Android"
        return "Linux"
    else:
        return "Desconocido"


# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu():
    while True:
        print("\n📚 MENÚ EDUCAREFLEX INSTALLER")
        print("1. Instalar todas las dependencias")
        print("2. Verificar dependencias")
        print("3. Actualizar dependencias")
        print("4. Mostrar historial de instalación")
        print("5. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            for dep in DEPENDENCIAS:
                instalar_dependencia(dep)
            guardar_log("instalación", "Instaladas todas las dependencias.")
        elif opcion == "2":
            for dep in DEPENDENCIAS:
                verificar_dependencia(dep)
            guardar_log("verificación", "Verificadas todas las dependencias.")
        elif opcion == "3":
            for dep in DEPENDENCIAS:
                instalar_dependencia(dep)
            guardar_log("actualización", "Actualizadas todas las dependencias.")
        elif opcion == "4":
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r") as f:
                    logs = json.load(f)
                    print(json.dumps(logs, indent=4))
            else:
                print("🗒 No hay historial disponible.")
        elif opcion == "5":
            print("👋 Saliendo del instalador EducaReflex...")
            break
        else:
            print("❌ Opción no válida.")


# ==============================
# PUNTO DE ENTRADA
# ==============================

if __name__ == "__main__":
    print("🚀 Bienvenido al instalador automático de EducaReflex")
    sistema = detectar_sistema()
    print(f"Configurando entorno para {sistema}...")
    menu()
