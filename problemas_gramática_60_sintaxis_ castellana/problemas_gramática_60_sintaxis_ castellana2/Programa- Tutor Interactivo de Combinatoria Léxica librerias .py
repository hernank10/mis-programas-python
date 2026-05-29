import random
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

# Base de datos de teoría y ejemplos
TEORIA = {
    "movimiento_vertical": {
        "explicacion": "Los verbos de movimiento vertical (subir, bajar, izar, etc.) se combinan con sustantivos que cumplen restricciones semánticas. Por ejemplo:\n- Verbos ascendentes (subir) requieren sustantivos que puedan 'elevarse' físicamente (montaña) o abstractamente (precios).\n- Verbos descendentes (caer) seleccionan sustantivos que implican 'descenso' (bombas) o 'colapso' (imperio).",
        "ejemplos": [
            ("El águila ___ al cielo.", "subió"),
            ("La bolsa ___ tras la crisis.", "cayó"),
            ("___ la bandera al amanecer.", "Izaron")
        ]
    },
    "uso_metafórico": {
        "explicacion": "Muchos verbos proyectan su movimiento literal a dominios abstractos mediante metáforas:\n- 'Subir' puede indicar aumento (precios).\n- 'Caer' sugiere fracaso (imperio) o cambio de estado (enfermo).",
        "ejemplos": [
            ("La motivación ___ tras el éxito.", "subió"),
            ("___ en una depresión profunda.", "Cayó"),
            ("___ los impuestos afectó la economía.", "Subir")
        ]
    }
}

# Base de datos de ejercicios de completación
EJERCICIOS = {
    "caer": {"sustantivos": ["bombas", "imperio", "ánimo"], "pista": "Sustantivos de colapso físico/abstracto."},
    "subir": {"sustantivos": ["montaña", "precios", "moral"], "pista": "Sustantivos de elevación o aumento."},
    "izar": {"sustantivos": ["bandera", "vela", "estandarte"], "pista": "Objetos simbólicos elevados ritualmente."}
}

# Almacenamiento de ejemplos del usuario
ejemplos_usuario = []

def mostrar_teoria():
    print(Fore.CYAN + "\nTEORÍA SOBRE COMBINATORIA LÉXICA")
    for tema, contenido in TEORIA.items():
        print(Fore.YELLOW + f"\n◆ {tema.upper()} ◆")
        print(Fore.WHITE + contenido["explicacion"])
        print(Fore.GREEN + "\nEjemplos:")
        for ejemplo in contenido["ejemplos"]:
            print(f"- {ejemplo[0]} ({ejemplo[1]})")
    input(Fore.MAGENTA + "\nPresiona Enter para continuar...")

def ejercicio_completacion():
    print(Fore.CYAN + "\nEJERCICIO: COMPLETA LAS ORACIONES")
    verbo = random.choice(list(EJERCICIOS.keys()))
    sustantivo_correcto = random.choice(EJERCICIOS[verbo]["sustantivos"])
    oracion = f"Para el verbo '{verbo}', completa: '{verbo.capitalize()} la ___ mientras haya esperanza.'"
    
    print(Fore.WHITE + oracion)
    respuesta = input(Fore.WHITE + "Tu respuesta (sustantivo): ").strip().lower()
    
    if respuesta in EJERCICIOS[verbo]["sustantivos"]:
        print(Fore.GREEN + f"✅ ¡Correcto! '{verbo} la {respuesta}' es válido. {EJERCICIOS[verbo]['pista']}")
    else:
        print(Fore.RED + f"❌ Incorrecto. Opciones válidas: {', '.join(EJERCICIOS[verbo]['sustantivos'])}.")

def guardar_ejemplo(oracion):
    if len(ejemplos_usuario) < 100:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ejemplos_usuario.append((timestamp, oracion))
        print(Fore.GREEN + "✓ Ejemplo guardado exitosamente.")
    else:
        print(Fore.RED + "¡Almacenamiento lleno! Máximo 100 ejemplos.")

def practica_redaccion():
    print(Fore.CYAN + "\nPRÁCTICA DE REDACCIÓN")
    print(Fore.YELLOW + "Instrucciones: Escribe oraciones usando verbos de movimiento vertical y sustantivos compatibles. Ej: 'La empresa subió los salarios'.")
    
    while True:
        oracion = input(Fore.WHITE + "\nEscribe tu oración (o 'salir' para terminar): ").strip()
        if oracion.lower() == "salir":
            break
        if any(verbo in oracion.lower() for verbo in EJERCICIOS.keys()):
            guardar_ejemplo(oracion)
        else:
            print(Fore.RED + "⚠️ Usa verbos como 'subir', 'caer' o 'izar'.")

def menu_principal():
    while True:
        print(Fore.CYAN + "\n" + "="*40)
        print(Fore.YELLOW + " TUTOR DE COMBINATORIA LÉXICA ".center(40))
        print(Fore.CYAN + "="*40)
        print(Fore.WHITE + "1. 📚 Ver teoría y ejemplos")
        print(Fore.WHITE + "2. ✍️ Ejercicio de completación")
        print(Fore.WHITE + "3. 📝 Práctica de redacción")
        print(Fore.WHITE + "4. 🗂️ Ver mis ejemplos guardados")
        print(Fore.WHITE + "5. 🚪 Salir")
        
        opcion = input(Fore.WHITE + "\nElige una opción (1-5): ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_completacion()
        elif opcion == "3":
            practica_redaccion()
        elif opcion == "4":
            print(Fore.GREEN + "\nTus ejemplos guardados:")
            for idx, (fecha, ejemplo) in enumerate(ejemplos_usuario, 1):
                print(f"{idx}. [{fecha}] {ejemplo}")
        elif opcion == "5":
            print(Fore.YELLOW + "¡Hasta luego! 🌟")
            break
        else:
            print(Fore.RED + "Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
