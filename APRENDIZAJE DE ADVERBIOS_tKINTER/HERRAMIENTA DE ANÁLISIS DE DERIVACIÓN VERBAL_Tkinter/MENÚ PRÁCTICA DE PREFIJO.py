import os
import sys
import subprocess
import platform
from time import sleep

def instalar_dependencias():
    """Instala todas las dependencias necesarias"""
    requerimientos = [
        'tk', 
        'kivy', 
        'fastapi', 
        'uvicorn', 
        'requests', 
        'python-multipart'
    ]
    
    print("🔧 Instalando dependencias...")
    for paquete in requerimientos:
        subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
    
    if platform.system() == "Darwin":  # macOS
        print("⚙️ Instalando dependencias para Kivy en macOS...")
        subprocess.run(['brew', 'install', 'sdl2', 'sdl2_image', 'sdl2_ttf', 'sdl2_mixer', 'portaudio'])

def menu_principal():
    """Muestra el menú interactivo"""
    while True:
        os.system('clear')
        print("""
        🚀 MENÚ PRÁCTICA DE PREFIJOS 🚀
        ----------------------------------
        1. Ejecutar GUI Tkinter (Tablas CRUD)
        2. Ejecutar GUI Kivy (Interfaz móvil)
        3. Iniciar API FastAPI (Backend)
        4. Practicar con prefijos (Modo Quiz)
        5. Salir
        ----------------------------------
        """)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            ejecutar_tkinter()
        elif opcion == '2':
            ejecutar_kivy()
        elif opcion == '3':
            ejecutar_fastapi()
        elif opcion == '4':
            modo_quiz()
        elif opcion == '5':
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
            sleep(1)

def ejecutar_tkinter():
    """Ejecuta la GUI de Tkinter"""
    codigo_tkinter = '''
    # Aquí iría el código completo del programa Tkinter anterior
    '''
    with open('tkinter_app.py', 'w') as f:
        f.write(codigo_tkinter)
    subprocess.Popen([sys.executable, "tkinter_app.py"])

def ejecutar_kivy():
    """Ejecuta la GUI de Kivy"""
    codigo_kivy = '''
    # Aquí iría el código completo del programa Kivy anterior
    '''
    with open('kivy_app.py', 'w') as f:
        f.write(codigo_kivy)
    subprocess.Popen([sys.executable, "kivy_app.py"])

def ejecutar_fastapi():
    """Inicia el servidor FastAPI"""
    print("🌐 Iniciando servidor FastAPI en http://localhost:8000")
    print("📚 Documentación: http://localhost:8000/docs")
    subprocess.Popen([sys.executable, "-m", "uvicorn", "fastapi_app:app", "--reload"])

def modo_quiz():
    """Modo interactivo de práctica"""
    preguntas = {
        "anti-": ["nuclear", "social", "inflación"],
        "des-": ["hacer", "orden", "conectar"],
        "re-": ["escribir", "utilizar", "calificar"]
    }
    
    while True:
        os.system('clear')
        print("📚 MODO QUIZ DE PREFIJOS\n")
        aciertos = 0
        
        for prefijo, palabras in preguntas.items():
            for palabra in palabras:
                respuesta = input(f"Palabra completa para {prefijo + '____'} + {palabra}: ")
                correcta = prefijo + palabra
                
                if respuesta.lower() == correcta:
                    print("✅ ¡Correcto!")
                    aciertos += 1
                else:
                    print(f"❌ Correcto: {correcta}")
                sleep(1)
        
        print(f"\n🏆 Puntuación: {aciertos}/{len(preguntas)*3}")
        if input("\n¿Practicar de nuevo? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    if platform.system() == "Darwin":
        print("🖥  Detectado macOS")
        print("⚠️  Asegúrate de tener Homebrew instalado (https://brew.sh)")
    
    instalar_dependencias()
    menu_principal()
