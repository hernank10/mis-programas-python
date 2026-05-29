import json
import random
from collections import deque
from os import system
import sys
from language_tool_python import LanguageTool  # Requiere instalación: pip install language-tool-python

# Configuración
EMOJIS = {
    "error": "❌",
    "correcto": "✅",
    "advertencia": "⚠️",
    "guardar": "💾",
    "gramatica": "📝"
}
ARCHIVO_EJEMPLOS = "oraciones_usuario.json"
MAX_EJEMPLOS = 100

def verificar_gramatica(texto):
    try:
        tool = LanguageTool('es-ES')
        errores = tool.check(texto)
        return [{
            'mensaje': error.message,
            'contexto': error.context,
            'sugerencias': error.replacements
        } for error in errores]
    except Exception as e:
        print(f"{EMOJIS['advertencia']} Error en verificador gramatical: {str(e)}")
        return []

def crear_oraciones(ejemplos):
    system('cls' if sys.platform == 'win32' else 'clear')
    print("\n📝 CREAR ORACIONES")
    
    # Generar palabra sugerida
    palabra = random.choice([
        "polisílabo", "multicolor", "pluricelular", "monocromo", 
        "bicéfalo", "tricolor", "antinatural"
    ])
    
    print(f"\n{EMOJIS['gramatica']} Palabra sugerida: {palabra}")
    
    # Solicitar oraciones
    simple = input("\n1. Escribe una oración simple: ")
    compuesta = input("\n2. Escribe una oración compuesta: ")
    
    # Verificación gramatical
    errores_simple = verificar_gramatica(simple)
    errores_compuesta = verificar_gramatica(compuesta)
    
    # Mostrar resultados
    print(f"\n{EMOJIS['gramatica']} Verificación:")
    mostrar_errores(errores_simple, "Oración simple")
    mostrar_errores(errores_compuesta, "Oración compuesta")
    
    # Confirmar guardado
    guardar = input("\n¿Guardar ejemplos? (s/n): ").lower()
    if guardar == 's':
        ejemplo = {
            'palabra': palabra,
            'simple': simple,
            'compuesta': compuesta,
            'errores_simple': errores_simple,
            'errores_compuesta': errores_compuesta
        }
        guardar_ejemplo(ejemplo, ejemplos)
        print(f"{EMOJIS['guardar']} ¡Ejemplos guardados!")

def mostrar_errores(errores, tipo):
    if errores:
        print(f"\n{EMOJIS['error']} {tipo}:")
        for error in errores[:2]:  # Mostrar máximo 2 errores
            print(f" • {error['mensaje']}")
            print(f"   Sugerencias: {', '.join(error['sugerencias'][:3])}")
    else:
        print(f"\n{EMOJIS['correcto']} {tipo} correcta")

def guardar_ejemplo(ejemplo, ejemplos):
    ejemplos.append(ejemplo)
    with open(ARCHIVO_EJEMPLOS, 'w') as f:
        json.dump(list(ejemplos), f, indent=2, ensure_ascii=False)

def ver_oraciones(ejemplos):
    system('cls' if sys.platform == 'win32' else 'clear')
    print("\n📚 TUS ORACIONES GUARDADAS")
    
    if not ejemplos:
        print("\nAún no tienes ejemplos guardados.")
        return
    
    for idx, ej in enumerate(ejemplos, 1):
        print(f"\n{idx}. Palabra: {ej['palabra']}")
        print(f"   Simple: {ej['simple']}")
        print(f"   Compuesta: {ej['compuesta']}")
        
        if ej['errores_simple'] or ej['errores_compuesta']:
            print(f"   {EMOJIS['error']} Errores detectados")
    
    input("\nPresiona Enter para continuar...")

def menu_principal():
    ejemplos = cargar_ejemplos()
    
    while True:
        system('cls' if sys.platform == 'win32' else 'clear')
        print("\n📚 MENÚ INTERACTIVO DE ORACIONES")
        print("1. Crear nuevas oraciones")
        print("2. Ver oraciones guardadas")
        print("3. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == '1':
            crear_oraciones(ejemplos)
        elif opcion == '2':
            ver_oraciones(ejemplos)
        elif opcion == '3':
            print("\n¡Hasta luego! 👋")
            break
        else:
            print(f"{EMOJIS['advertencia']} Opción no válida")

def cargar_ejemplos():
    try:
        with open(ARCHIVO_EJEMPLOS, 'r') as f:
            return deque(json.load(f), maxlen=MAX_EJEMPLOS)
    except (FileNotFoundError, json.JSONDecodeError):
        return deque(maxlen=MAX_EJEMPLOS)

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n{EMOJIS['advertencia']} Programa interrumpido")
