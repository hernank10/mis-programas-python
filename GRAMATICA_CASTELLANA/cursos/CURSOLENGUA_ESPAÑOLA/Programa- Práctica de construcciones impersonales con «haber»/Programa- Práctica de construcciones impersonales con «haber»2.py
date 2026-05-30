puntaje_total = 0  # Variable global para acumular puntos

def mostrar_teoria():
    # ... (igual que antes) ...

def ejercicio_redaccion():
    global puntaje_total
    ejercicios = [
        # ... (igual que antes) ...
    ]
    
    print("\n=== EJERCICIOS DE REDACCIÓN ===")
    print("Cada respuesta correcta suma 3 puntos.\n")
    for i, ejercicio in enumerate(ejercicios, 1):
        print(f"Ejercicio {i}: {ejercicio['frase']}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == ejercicio["solucion"].lower():
            puntaje_total += 3
            print("✅ ¡Correcto! +3 puntos.")
        else:
            print(f"❌ Mejorable. Solución: {ejercicio['solucion']}")
    print(f"\nPuntos acumulados: {puntaje_total}\n")

def cuestionario():
    global puntaje_total
    preguntas = [
        # ... (igual que antes) ...
    ]
    
    print("\n=== CUESTIONARIO ===")
    print("Cada respuesta correcta suma 2 puntos.\n")
    for i, pregunta in enumerate(preguntas, 1):
        print(f"Pregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)
        respuesta = input("Elige (A/B/C): ").upper()
        if respuesta == pregunta['respuesta']:
            puntaje_total += 2
            print("✅ Correcto! +2 puntos.")
        else:
            print(f"❌ Incorrecto. Respuesta: {pregunta['respuesta']}")
    print(f"\nPuntos acumulados: {puntaje_total}\n")

def analisis_sintactico():
    global puntaje_total
    ejercicios = [
        {
            "oracion": "No hay que correr en la biblioteca.",
            "analisis_correcto": ["No hay que", "correr en la biblioteca"],
            "explicacion": "La negación afecta a 'haber' (no hay que) + acción prohibida (correr...)."
        },
        {
            "oracion": "Hay que no subestimar los riesgos.",
            "analisis_correcto": ["Hay que", "no subestimar los riesgos"],
            "explicacion": "La negación está en el infinitivo, estructura menos común."
        }
    ]
    
    print("\n=== ANÁLISIS SINTÁCTICO ===")
    print("Descompón cada oración en sus partes estructurales (ej: 'No hay que' + 'acción').\nCada acierto suma 5 puntos.\n")
    
    for ejercicio in ejercicios:
        print(f"Oración: {ejercicio['oracion']}")
        parte1 = input("Primera parte (ej: 'No hay que'): ").strip()
        parte2 = input("Segunda parte (ej: 'correr aquí'): ").strip()
        
        if [parte1.lower(), parte2.lower()] == [ejercicio['analisis_correcto'][0].lower(), ejercicio['analisis_correcto'][1].lower()]:
            puntaje_total += 5
            print(f"✅ ¡Análisis perfecto! +5 puntos.\nExplicación: {ejercicio['explicacion']}\n")
        else:
            print(f"❌ Mejorable. Estructura correcta:\n1. {ejercicio['analisis_correcto'][0]}\n2. {ejercicio['analisis_correcto'][1]}\n")
    
    print(f"Puntos acumulados: {puntaje_total}\n")

def main():
    global puntaje_total
    print("""
    ¡Bienvenido al programa de práctica con «haber» impersonal!
    Elige una opción:
    1. Ver teoría
    2. Hacer ejercicios de redacción (3 pts/correcta)
    3. Realizar cuestionario (2 pts/correcta)
    4. Análisis sintáctico (5 pts/correcta)
    5. Ver puntaje total
    6. Salir
    """)
    
    while True:
        opcion = input("Opción (1-6): ").strip()
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_redaccion()
        elif opcion == "3":
            cuestionario()
        elif opcion == "4":
            analisis_sintactico()
        elif opcion == "5":
            print(f"\n⭐ Puntaje total acumulado: {puntaje_total} puntos\n")
        elif opcion == "6":
            print(f"¡Hasta pronto! Puntaje final: {puntaje_total} ✨")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
