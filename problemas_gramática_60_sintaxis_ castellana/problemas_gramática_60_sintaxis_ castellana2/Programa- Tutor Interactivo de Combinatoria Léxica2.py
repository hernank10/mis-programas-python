import random
import os
from datetime import datetime
from colorama import Fore, Style, init
import sys
try:
    import pygame  # Para sonidos
    from reportlab.pdfgen import canvas  # Para PDF
except ImportError:
    pass

# Configuración inicial
init(autoreset=True)
THEMA = "oscuro"  # Puede ser 'claro' u 'oscuro'
COLORES = {
    "oscuro": {"fondo": Fore.BLACK, "texto": Fore.WHITE, "acento": Fore.CYAN},
    "claro": {"fondo": Fore.WHITE, "texto": Fore.BLACK, "acento": Fore.BLUE}
}

# Configuración de progreso y logros
progreso = {"ejercicios_completados": 0, "ejemplos_guardados": 0}
logros_desbloqueados = set()

# Base de datos mejorada
TEORIA = { ... }  # Mantener misma estructura del código anterior
EJERCICIOS = { ... }  # Mantener misma estructura

# Sistema de sonidos (usando pygame)
def play_sound(tipo):
    try:
        pygame.mixer.init()
        if tipo == "éxito":
            pygame.mixer.Sound('ding.wav').play()  # Necesitas un archivo de sonido
        elif tipo == "error":
            pygame.mixer.Sound('buzz.wav').play()  # Necesitas un archivo de sonido
    except:
        pass  # Silencia errores si no hay pygame instalado

# Modo visual personalizado
def aplicar_tema():
    color = COLORES[THEMA]
    os.system('cls' if os.name == 'nt' else 'clear')
    print(color["fondo"] + color["texto"], end="")

# Gráficos de progreso ASCII
def mostrar_progreso():
    porcentaje = (progreso["ejercicios_completados"] / 20) * 100
    print(f"\n📊 Progreso general: [{ '█' * int(porcentaje//5) }{'░' * (20 - int(porcentaje//5))}] {min(100, porcentaje)}%")

# Sistema de logros
LOGROS = {
    "novato": {"condicion": lambda: progreso["ejercicios_completados"] >= 5},
    "escritor": {"condicion": lambda: progreso["ejemplos_guardados"] >= 10},
    "maestro": {"condicion": lambda: len(logros_desbloqueados) >= 3}
}

def verificar_logros():
    for nombre, datos in LOGROS.items():
        if nombre not in logros_desbloqueados and datos["condicion"]():
            logros_desbloqueados.add(nombre)
            print(f"🎉 ¡Logro desbloqueado: {nombre.upper()}!")

# Exportación a PDF
def exportar_pdf():
    try:
        filename = f"combinatoria_lexica_{datetime.now().strftime('%Y%m%d')}.pdf"
        c = canvas.Canvas(filename)
        
        # Configuración del documento
        c.setFont("Helvetica", 12)
        c.drawString(100, 800, "Reporte de Progreso - Combinatoria Léxica")
        
        # Sección de logros
        c.drawString(100, 750, "Logros Desbloqueados:")
        y = 730
        for logro in logros_desbloqueados:
            c.drawString(120, y, f"✓ {logro.capitalize()}")
            y -= 20
            
        # Sección de ejemplos
        c.drawString(100, 650, "Ejemplos Guardados:")
        y = 630
        for _, ejemplo in ejemplos_usuario[-10:]:  # Últimos 10 ejemplos
            c.drawString(120, y, f"- {ejemplo}")
            y -= 20
            
        c.save()
        print(f"✅ PDF exportado como {filename}")
    except:
        print("❌ Error: Instala reportlab con 'pip install reportlab'")

# Modificaciones al menú principal
def menu_principal():
    aplicar_tema()
    while True:
        print(COLORES[THEMA]["acento"] + "\n" + "="*40)
        print(f" TUTOR DE COMBINATORIA LÉXICA ".center(40))
        print("="*40 + Style.RESET_ALL)
        
        print(f"1. 📚 Teoría y ejemplos\n2. ✍️ Completar oraciones\n3. 📝 Práctica de redacción\n4. 🗂️ Mis ejemplos\n5. 🌓 Cambiar tema ({THEMA.capitalize()})\n6. 📤 Exportar a PDF\n7. 🚪 Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "5":
            global THEMA
            THEMA = "claro" if THEMA == "oscuro" else "oscuro"
            aplicar_tema()
        elif opcion == "6":
            exportar_pdf()
        # ... (resto de opciones similares al código anterior)
