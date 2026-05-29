import random

# ================================
#  JUEGO 1: CAZADOR DE SUJETO Y PREDICADO
# ================================
ejercicios_suj_pred = [
    {"oracion": "El perro ladra fuerte.", "sujeto": "El perro", "predicado": "ladra fuerte"},
    {"oracion": "Los niños juegan en el parque.", "sujeto": "Los niños", "predicado": "juegan en el parque"},
    {"oracion": "María canta una canción.", "sujeto": "María", "predicado": "canta una canción"},
    {"oracion": "El profesor explicó la lección.", "sujeto": "El profesor", "predicado": "explicó la lección"},
    {"oracion": "La lluvia cae suavemente.", "sujeto": "La lluvia", "predicado": "cae suavemente"}
]

def cazador_sujeto_predicado():
    print("\n🎯 Cazador de Sujeto y Predicado 🎯")
    ejercicio = random.choice(ejercicios_suj_pred)
    print(f"\n👉 Oración: {ejercicio['oracion']}")
    
    sujeto = input("✏️ Escribe el sujeto: ").strip()
    predicado = input("✏️ Escribe el predicado: ").strip()
    
    if sujeto.lower() == ejercicio["sujeto"].lower() and predicado.lower() == ejercicio["predicado"].lower():
        print("✅ ¡Correcto! 🎉 Identificaste bien el sujeto y el predicado.")
    else:
        print("❌ Incorrecto. La respuesta correcta es:")
        print(f"   Sujeto: {ejercicio['sujeto']} | Predicado: {ejercicio['predicado']}")

# ================================
#  JUEGO 2: CLASIFICA LA ORACIÓN
# ================================
ejercicios_clasificacion = [
    {"oracion": "El sol brilla intensamente.", "tipo": "simple"},
    {"oracion": "María estudia y Juan trabaja.", "tipo": "compuesta coordinada"},
    {"oracion": "Salí temprano porque tenía sueño.", "tipo": "compuesta subordinada"},
    {"oracion": "Llegó tarde; no encontró taxi.", "tipo": "yuxtapuesta"},
    {"oracion": "Pedro cocina muy bien.", "tipo": "simple"},
    {"oracion": "Voy al cine pero tú prefieres leer.", "tipo": "compuesta coordinada"},
    {"oracion": "Te llamé cuando llegué a casa.", "tipo": "compuesta subordinada"},
    {"oracion": "Estudia mucho; aprobarás el examen.", "tipo": "yuxtapuesta"}
]

def clasifica_oracion():
    print("\n📚 Clasifica la Oración 📚")
    ejercicio = random.choice(ejercicios_clasificacion)
    print(f"\n👉 Oración: {ejercicio['oracion']}")
    
    print("Opciones: simple | compuesta coordinada | compuesta subordinada | yuxtapuesta")
    respuesta = input("✏️ Clasifícala: ").strip().lower()
    
    if respuesta == ejercicio["tipo"]:
        print("✅ ¡Correcto! 🎉 Clasificaste bien la oración.")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {ejercicio['tipo']}")

# ================================
#  MENÚ PRINCIPAL
# ================================
def menu():
    while True:
        print("\n===============================")
        print("🎮 JUEGOS SINTÁCTICOS 🎮")
        print("===============================")
        print("1. Cazador de Sujeto y Predicado")
        print("2. Clasifica la Oración")
        print("3. Salir")
        
        opcion = input("\n👉 Elige un juego (1-3): ").strip()
        
        if opcion == "1":
            cazador_sujeto_predicado()
        elif opcion == "2":
            clasifica_oracion()
        elif opcion == "3":
            print("👋 Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar menú principal
if __name__ == "__main__":
    menu()
