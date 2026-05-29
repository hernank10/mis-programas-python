"""
Programa educativo sobre la perífrasis 'ir a + infinitivo'
Autor: Asistente AI
Versión: 2.0 (con ejercicios de completación y registro de ejemplos)
"""

import os
import sys

ARCHIVO_EJEMPLOS = "ejemplos_usuario.txt"
MAX_EJEMPLOS = 100

# ---------------------- FUNCIONES DE ARCHIVOS ----------------------
def guardar_ejemplo(ejemplo):
    """Guarda ejemplos manteniendo un máximo de 100 entradas"""
    try:
        # Leer ejemplos existentes
        if os.path.exists(ARCHIVO_EJEMPLOS):
            with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
                lineas = f.readlines()[-MAX_EJEMPLOS+1:]  # Mantener últimos 99
        else:
            lineas = []
        
        # Añadir nuevo ejemplo
        with open(ARCHIVO_EJEMPLOS, "w", encoding="utf-8") as f:
            lineas.append(ejemplo + "\n")
            f.writelines(lineas[-MAX_EJEMPLOS:])  # Conservar solo los últimos 100
        
        return True
    except Exception as e:
        print(f"Error al guardar: {str(e)}")
        return False

def cargar_ejemplos():
    """Carga los ejemplos guardados"""
    try:
        if os.path.exists(ARCHIVO_EJEMPLOS):
            with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
                return [linea.strip() for linea in f.readlines()]
        return []
    except Exception as e:
        print(f"Error al cargar: {str(e)}")
        return []

# ---------------------- MÓDULO TEÓRICO ----------------------
def mostrar_teoria():
    teoria = {
        # ... (el contenido teórico anterior se mantiene igual)
    }

    for seccion, contenido in teoria.items():
        print(f"\n=== {seccion.upper()} ===")
        print(contenido)
        input("Presiona Enter para continuar...")

# ---------------------- EJERCICIOS MEJORADOS ----------------------
def ejercicios():
    puntaje = 0
    ejercicios = [
        # Ejercicios originales...
        # Nuevos ejercicios de completación
        {
            "tipo": "completacion",
            "pregunta": "Completa la oración:\nEl ministro duda que el presupuesto ______ (aprobarse/ir a aprobarse)",
            "respuesta": "vaya a aprobarse",
            "explicacion": "Correcto! 'Dudar' permite 'ir a' + subjuntivo dubitativo"
        },
        {
            "tipo": "completacion",
            "pregunta": "Completa la oración (afirmativa):\nEl jefe exige que ______ (entregar/ir a entregar) el informe",
            "respuesta": "entreguemos",
            "explicacion": "¡Exacto! En volitivos afirmativos se usa subjuntivo simple"
        },
        # ... (añadir más ejercicios)
    ]

    print("\n=== EJERCICIOS MEJORADOS ===")
    for i, ej in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}: {ej['pregunta']}")
        user_resp = input("Tu respuesta: ").strip().lower()
        
        # Sistema de evaluación mejorado
        if ej.get('tipo') == "completacion":
            if any(palabra in user_resp for palabra in ej["respuesta"].split()):
                puntaje +=1
                print(f"✅ {ej['explicacion']}")
            else:
                print(f"❌ Mejor respuesta: {ej['respuesta']}")
        else:
            # Lógica para otros tipos de ejercicio...
            pass
        
        print("-"*50)

    print(f"\nPuntuación final: {puntaje}/{len(ejercicios)}")
    # ... (resto de lógica de puntuación)

# ---------------------- NUEVO MÓDULO DE REDACCIÓN ----------------------
def redaccion_ejemplos():
    print("\n=== REDACCIÓN DE EJEMPLOS ===")
    print("Escribe oraciones usando 'ir a + infinitivo' en contextos modales.")
    print("Ejemplo válido: 'Es improbable que vayan a aceptar la propuesta'")
    print("Escribe 'salir' para volver al menú\n")
    
    while True:
        ejemplo = input("Escribe tu oración:\n> ").strip()
        if ejemplo.lower() == "salir":
            break
        
        if "ir a " in ejemplo:
            if guardar_ejemplo(ejemplo):
                print("✅ Ejemplo guardado correctamente")
            else:
                print("❌ Error al guardar")
        else:
            print("⚠ La oración debe contener 'ir a + infinitivo'")

def ver_mis_ejemplos():
    ejemplos = cargar_ejemplos()
    print(f"\n=== TUS ÚLTIMOS {len(ejemplos)} EJEMPLOS ===")
    for i, ej in enumerate(ejemplos, 1):
        print(f"{i}. {ej}")
    input("\nPresiona Enter para continuar...")

# ---------------------- MENÚ PRINCIPAL MEJORADO ----------------------
def main():
    while True:
        print("\n" + "="*50)
        print(" ESTUDIO DE 'IR A + INFINITIVO' (VERSIÓN 2.0)")
        print("="*50)
        print("1. Ver teoría")
        print("2. Realizar ejercicios")
        print("3. Redactar y guardar ejemplos")
        print("4. Ver mis ejemplos guardados")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicios()
        elif opcion == "3":
            redaccion_ejemplos()
        elif opcion == "4":
            ver_mis_ejemplos()
        elif opcion == "5":
            print("¡Hasta pronto! Recuerda revisar tus ejemplos guardados.")
            sys.exit()
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
