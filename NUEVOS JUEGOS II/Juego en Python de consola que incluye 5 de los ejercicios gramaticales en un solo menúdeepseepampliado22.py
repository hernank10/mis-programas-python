import random
import os
import time
import re

# Datos para el juego de Carrera de Conectores
carrera_conectores = [
    {
        "contexto": "No fui a la fiesta ______ estaba enfermo",
        "opciones": ["porque", "pero", "aunque"],
        "correcta": 0,
        "tipo": "causal",
        "explicacion": "'porque' indica causa-efecto: la enfermedad es la causa de no ir"
    },
    {
        "contexto": "Estudié mucho ______ aprobé el examen",
        "opciones": ["y", "pero", "aunque"],
        "correcta": 0,
        "tipo": "consecutiva",
        "explicacion": "'y' une dos ideas que se complementan"
    },
    {
        "contexto": "Me gusta el café ______ no tomo mucho",
        "opciones": ["pero", "porque", "cuando"],
        "correcta": 0,
        "tipo": "adversativa",
        "explicacion": "'pero' indica contraste entre gustar y no tomar"
    },
    {
        "contexto": "______ llegues temprano, podremos conversar",
        "opciones": ["Si", "Aunque", "Pero"],
        "correcta": 0,
        "tipo": "condicional",
        "explicacion": "'Si' introduce una condición necesaria"
    },
    {
        "contexto": "______ llovía, fuimos al parque",
        "opciones": ["Aunque", "Porque", "Y"],
        "correcta": 0,
        "tipo": "concesiva",
        "explicacion": "'Aunque' indica una acción a pesar de una dificultad"
    },
    {
        "contexto": "Lo haré ______ me lo pides",
        "opciones": ["porque", "pero", "aunque"],
        "correcta": 0,
        "tipo": "causal",
        "explicacion": "'porque' indica la razón por la que hará algo"
    },
    {
        "contexto": "Trabajó rápido ______ eficientemente",
        "opciones": ["y", "pero", "aunque"],
        "correcta": 0,
        "tipo": "copulativa",
        "explicacion": "'y' une dos cualidades que se suman"
    },
    {
        "contexto": "No vine ______ no me invitaste",
        "opciones": ["porque", "pero", "si"],
        "correcta": 0,
        "tipo": "causal",
        "explicacion": "'porque' explica la razón de no venir"
    },
    {
        "contexto": "______ hace frío, no me pondré abrigo",
        "opciones": ["Aunque", "Porque", "Y"],
        "correcta": 0,
        "tipo": "concesiva",
        "explicacion": "'Aunque' indica una acción contraria a lo esperado"
    },
    {
        "contexto": "______ termines, avísame",
        "opciones": ["Cuando", "Pero", "Porque"],
        "correcta": 0,
        "tipo": "temporal",
        "explicacion": "'Cuando' indica el momento en que debe avisar"
    },
    {
        "contexto": "No solo estudia, ______ también trabaja",
        "opciones": ["sino", "porque", "aunque"],
        "correcta": 0,
        "tipo": "aditiva",
        "explicacion": "'sino' completa una idea de adición"
    },
    {
        "contexto": "______ más lo intento, menos entiendo",
        "opciones": ["Mientras", "Porque", "Pero"],
        "correcta": 0,
        "tipo": "proporcional",
        "explicacion": "'Mientras' indica relación proporcional entre dos acciones"
    },
    {
        "contexto": "Ven aquí ______ te vea mejor",
        "opciones": ["para que", "aunque", "pero"],
        "correcta": 0,
        "tipo": "final",
        "explicacion": "'para que' indica la finalidad de la acción"
    },
    {
        "contexto": "______ no me crees, pregúntale a él",
        "opciones": ["Si", "Aunque", "Y"],
        "correcta": 0,
        "tipo": "condicional",
        "explicacion": "'Si' plantea una condición hipotética"
    },
    {
        "contexto": "______ estudies, pasarás el examen",
        "opciones": ["Si", "Aunque", "Pero"],
        "correcta": 0,
        "tipo": "condicional",
        "explicacion": "'Si' establece una condición necesaria para el resultado"
    }
]

# ... (mantenemos todos los datos anteriores de los otros juegos)

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=" * 60)
    print("           JUEGOS GRAMATICALES - ESPAÑOL/INGLÉS")
    print("=" * 60)
    print("1. 🎯 Cazador de Sujeto y Predicado")
    print("2. 🧩 Puzzle de la Oración")
    print("3. 📊 Clasifica la Oración")
    print("4. ✏️  Corrector de Oraciones")
    print("5. 🧱 Construye tu Propia Oración")
    print("6. 🏎️  Carrera de Conectores")
    print("7. 📈 Ver Estadísticas")
    print("8. ❌ Salir")
    print("-" * 60)

def dibujar_pista(posicion_jugador, longitud_pista=20, meta=15):
    """Dibuja la pista de carreras con el personaje"""
    print("\n" + "="*50)
    print("🏁 CARRERA DE CONECTORES 🏁")
    print("="*50)
    
    pista = ["_"] * longitud_pista
    pista[min(posicion_jugador, longitud_pista-1)] = "🚗"
    pista[meta] = "🏁"  # Meta
    
    print("PISTA: " + "".join(pista))
    print(f"Posición: {posicion_jugador}/{meta}")
    print("="*50)

def juego_carrera_conectores():
    limpiar_consola()
    print("🏎️  CARRERA DE CONECTORES")
    print("=" * 50)
    print("Elige el conector correcto para avanzar en la carrera!")
    print("✅ Correcto: +3 posiciones")
    print("❌ Incorrecto: -1 posición")
    print("🏁 Meta: Llegar a la posición 15")
    print("-" * 50)
    
    posicion = 0
    meta = 15
    preguntas_realizadas = 0
    aciertos = 0
    ejercicios_mezclados = carrera_conectores.copy()
    random.shuffle(ejercicios_mezclados)
    
    while posicion < meta and preguntas_realizadas < len(ejercicios_mezclados):
        ejercicio = ejercicios_mezclados[preguntas_realizadas]
        preguntas_realizadas += 1
        
        dibujar_pista(posicion, 20, meta)
        
        print(f"\n📝 Oración {preguntas_realizadas}:")
        print(f"   {ejercicio['contexto']}")
        print(f"   Tipo de relación: {ejercicio['tipo'].upper()}")
        print("\n🎯 Opciones:")
        
        for i, opcion in enumerate(ejercicio['opciones']):
            print(f"   {i + 1}. {opcion}")
        
        try:
            respuesta = int(input("\nElige el conector correcto (1-3): ")) - 1
            
            if 0 <= respuesta < len(ejercicio['opciones']):
                if respuesta == ejercicio['correcta']:
                    posicion += 3
                    aciertos += 1
                    print(f"\n✅ ¡CORRECTO! +3 posiciones")
                    print(f"💡 {ejercicio['explicacion']}")
                else:
                    posicion = max(0, posicion - 1)  # No retrocede más allá de 0
                    print(f"\n❌ INCORRECTO! -1 posición")
                    print(f"💡 La respuesta correcta era: '{ejercicio['opciones'][ejercicio['correcta']]}'")
                    print(f"💡 {ejercicio['explicacion']}")
            else:
                print("❌ Opción inválida. Pierdes 1 posición por tiempo!")
                posicion = max(0, posicion - 1)
                
        except ValueError:
            print("❌ Por favor ingresa un número. Pierdes 1 posición!")
            posicion = max(0, posicion - 1)
        
        input("\nPresiona Enter para continuar...")
        limpiar_consola()
    
    # Resultado final
    dibujar_pista(min(posicion, 20), 20, meta)
    
    if posicion >= meta:
        print("\n🎉 ¡FELICIDADES! ¡HAS GANADO LA CARRERA! 🏆")
        print("💫 Eres un maestro de los conectores gramaticales!")
    else:
        print("\n💪 ¡Buen intento! Sigue practicando los conectores.")
    
    porcentaje_aciertos = (aciertos / preguntas_realizadas) * 100 if preguntas_realizadas > 0 else 0
    
    print(f"\n📊 ESTADÍSTICAS DE LA CARRERA:")
    print(f"   Preguntas respondidas: {preguntas_realizadas}")
    print(f"   Aciertos: {aciertos}/{preguntas_realizadas}")
    print(f"   Porcentaje de aciertos: {porcentaje_aciertos:.1f}%")
    print(f"   Posición final: {posicion}/{meta}")
    
    # Calcular puntaje (basado en posición y aciertos)
    puntaje = min(100, (posicion * 5) + (porcentaje_aciertos * 0.5))
    
    input("\nPresiona Enter para continuar...")
    return int(puntaje), 100

# ... (las funciones anteriores de los otros juegos se mantienen igual)

def juego_sujeto_predicado():
    # ... (implementación existente)
    pass

def juego_puzzle_oracion():
    # ... (implementación existente)
    pass

def juego_clasifica_oracion():
    # ... (implementación existente)
    pass

def juego_corrector_oraciones():
    # ... (implementación existente)
    pass

def juego_construye_oracion():
    # ... (implementación existente)
    pass

def mostrar_estadisticas(estadisticas):
    limpiar_consola()
    print("📈 ESTADÍSTICAS DE JUEGO")
    print("=" * 50)
    
    if not estadisticas:
        print("Aún no hay estadísticas. ¡Juega algunos juegos!")
    else:
        total_puntos = 0
        total_maximo = 0
        
        for juego, (puntos, maximo) in estadisticas.items():
            porcentaje = (puntos / maximo) * 100 if maximo > 0 else 0
            print(f"\n{juego}:")
            print(f"  Puntos: {puntos}/{maximo}")
            print(f"  Porcentaje: {porcentaje:.1f}%")
            total_puntos += puntos
            total_maximo += maximo
        
        if total_maximo > 0:
            promedio = (total_puntos / total_maximo) * 100
            print(f"\n📊 Total general: {total_puntos}/{total_maximo}")
            print(f"📈 Promedio general: {promedio:.1f}%")
    
    input("\nPresiona Enter para continuar...")

def main():
    estadisticas = {}
    
    while True:
        limpiar_consola()
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-8): ").strip()
        
        if opcion == "1":
            puntos, maximo = juego_sujeto_predicado()
            estadisticas["🎯 Cazador de Sujeto"] = (puntos, maximo)
        elif opcion == "2":
            puntos, maximo = juego_puzzle_oracion()
            estadisticas["🧩 Puzzle de Oración"] = (puntos, maximo)
        elif opcion == "3":
            puntos, maximo = juego_clasifica_oracion()
            estadisticas["📊 Clasifica Oración"] = (puntos, maximo)
        elif opcion == "4":
            puntos, maximo = juego_corrector_oraciones()
            estadisticas["✏️  Corrector Oraciones"] = (puntos, maximo)
        elif opcion == "5":
            puntos, maximo = juego_construye_oracion()
            estadisticas["🧱 Construye Oración"] = (puntos, maximo)
        elif opcion == "6":
            puntos, maximo = juego_carrera_conectores()
            estadisticas["🏎️  Carrera Conectores"] = (puntos, maximo)
        elif opcion == "7":
            mostrar_estadisticas(estadisticas)
        elif opcion == "8":
            print("\n¡Gracias por jugar! Hasta pronto 👋")
            break
        else:
            print("❌ Opción inválida. Por favor selecciona 1-8")
            time.sleep(1)

if __name__ == "__main__":
    main()
