import random
import os
import time

# Datos para los juegos
oraciones_sujeto_predicado = [
    {"oracion": "El niño juega en el parque", "sujeto": "El niño", "predicado": "juega en el parque"},
    {"oracion": "María estudia matemáticas", "sujeto": "María", "predicado": "estudia matemáticas"},
    {"oracion": "Los pájaros cantan hermosamente", "sujeto": "Los pájaros", "predicado": "cantan hermosamente"},
    {"oracion": "Mi hermano cocina muy bien", "sujeto": "Mi hermano", "predicado": "cocina muy bien"}
]

oraciones_desordenadas = [
    {"desordenada": ["casa", "la", "blanca", "es"], "correcta": "La casa es blanca"},
    {"desordenada": ["perro", "el", "corre", "rápidamente"], "correcta": "El perro corre rápidamente"},
    {"desordenada": ["estudian", "los", "alumnos", "mucho"], "correcta": "Los alumnos estudian mucho"},
    {"desordenada": ["sol", "el", "brilla", "intensamente"], "correcta": "El sol brilla intensamente"}
]

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=" * 50)
    print("       JUEGOS GRAMATICALES - ESPAÑOL/INGLÉS")
    print("=" * 50)
    print("1. Cazador de Sujeto y Predicado")
    print("2. Puzzle de la Oración")
    print("3. Salir")
    print("-" * 50)

def juego_sujeto_predicado():
    limpiar_consola()
    print("🎯 CAZADOR DE SUJETO Y PREDICADO")
    print("=" * 40)
    print("Identifica el sujeto y predicado en las oraciones")
    print("-" * 40)
    
    puntaje = 0
    total_preguntas = min(3, len(oraciones_sujeto_predicado))
    oraciones_mezcladas = random.sample(oraciones_sujeto_predicado, total_preguntas)
    
    for i, item in enumerate(oraciones_mezcladas, 1):
        print(f"\nOración {i}: {item['oracion']}")
        
        # Solicitar sujeto
        sujeto_usuario = input("¿Cuál es el sujeto? ").strip()
        if sujeto_usuario.lower() == item['sujeto'].lower():
            print("✅ ¡Correcto! Sujeto identificado correctamente")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. El sujeto era: {item['sujeto']}")
        
        # Solicitar predicado
        predicado_usuario = input("¿Cuál es el predicado? ").strip()
        if predicado_usuario.lower() == item['predicado'].lower():
            print("✅ ¡Correcto! Predicado identificado correctamente")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. El predicado era: {item['predicado']}")
    
    print(f"\n🎉 Puntuación final: {puntaje}/{total_preguntas*2}")
    input("\nPresiona Enter para continuar...")

def juego_puzzle_oracion():
    limpiar_consola()
    print("🧩 PUZZLE DE LA ORACIÓN")
    print("=" * 40)
    print("Ordena las palabras para formar una oración correcta")
    print("-" * 40)
    
    puntaje = 0
    total_preguntas = min(3, len(oraciones_desordenadas))
    oraciones_mezcladas = random.sample(oraciones_desordenadas, total_preguntas)
    
    for i, item in enumerate(oraciones_mezcladas, 1):
        palabras_mezcladas = item['desordenada'].copy()
        random.shuffle(palabras_mezcladas)
        
        print(f"\nPalabras desordenadas {i}:")
        print(" ".join(palabras_mezcladas))
        
        respuesta_usuario = input("Escribe la oración ordenada: ").strip()
        
        if respuesta_usuario.lower() == item['correcta'].lower():
            print("🎉 ¡Correcto! Oración bien formada ✅")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La oración correcta es: {item['correcta']}")
    
    print(f"\n🏆 Puntuación final: {puntaje}/{total_preguntas}")
    input("\nPresiona Enter para continuar...")

def main():
    while True:
        limpiar_consola()
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            juego_sujeto_predicado()
        elif opcion == "2":
            juego_puzzle_oracion()
        elif opcion == "3":
            print("\n¡Gracias por jugar! Hasta pronto 👋")
            break
        else:
            print("❌ Opción inválida. Por favor selecciona 1, 2 o 3")
            time.sleep(1)

if __name__ == "__main__":
    main()
