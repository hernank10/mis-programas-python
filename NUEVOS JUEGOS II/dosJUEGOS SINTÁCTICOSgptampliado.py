import random

# ================================
#  JUEGO 1: CAZADOR DE SUJETO Y PREDICADO
# ================================
ejercicios_suj_pred = [
    {"oracion": "El perro ladra fuerte.", "sujeto": "El perro", "predicado": "ladra fuerte"},
    {"oracion": "Los niños juegan en el parque.", "sujeto": "Los niños", "predicado": "juegan en el parque"},
    {"oracion": "María canta una canción.", "sujeto": "María", "predicado": "canta una canción"},
    {"oracion": "El profesor explicó la lección.", "sujeto": "El profesor", "predicado": "explicó la lección"},
    {"oracion": "La lluvia cae suavemente.", "sujeto": "La lluvia", "predicado": "cae suavemente"},
    {"oracion": "Mi hermano corre rápido.", "sujeto": "Mi hermano", "predicado": "corre rápido"},
    {"oracion": "El gato duerme en el sofá.", "sujeto": "El gato", "predicado": "duerme en el sofá"},
    {"oracion": "Ana lee un libro interesante.", "sujeto": "Ana", "predicado": "lee un libro interesante"},
    {"oracion": "Los pájaros vuelan alto.", "sujeto": "Los pájaros", "predicado": "vuelan alto"},
    {"oracion": "La maestra enseña matemáticas.", "sujeto": "La maestra", "predicado": "enseña matemáticas"},
    {"oracion": "El tren llega a la estación.", "sujeto": "El tren", "predicado": "llega a la estación"},
    {"oracion": "Carlos dibuja en su cuaderno.", "sujeto": "Carlos", "predicado": "dibuja en su cuaderno"},
    {"oracion": "Las flores crecen en el jardín.", "sujeto": "Las flores", "predicado": "crecen en el jardín"},
    {"oracion": "El viento sopla fuerte.", "sujeto": "El viento", "predicado": "sopla fuerte"},
    {"oracion": "Mi abuela cocina muy bien.", "sujeto": "Mi abuela", "predicado": "cocina muy bien"},
    {"oracion": "El coche acelera en la carretera.", "sujeto": "El coche", "predicado": "acelera en la carretera"},
    {"oracion": "Los estudiantes escriben en sus cuadernos.", "sujeto": "Los estudiantes", "predicado": "escriben en sus cuadernos"},
    {"oracion": "El médico atiende a sus pacientes.", "sujeto": "El médico", "predicado": "atiende a sus pacientes"},
    {"oracion": "La computadora funciona rápido.", "sujeto": "La computadora", "predicado": "funciona rápido"},
    {"oracion": "El panadero prepara el pan.", "sujeto": "El panadero", "predicado": "prepara el pan"},
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
    {"oracion": "Estudia mucho; aprobarás el examen.", "tipo": "yuxtapuesta"},
    {"oracion": "Los estudiantes leen libros.", "tipo": "simple"},
    {"oracion": "Me levanté y desayuné rápido.", "tipo": "compuesta coordinada"},
    {"oracion": "No salgas si está lloviendo.", "tipo": "compuesta subordinada"},
    {"oracion": "Ayer viajé a Bogotá; hoy estoy en Medellín.", "tipo": "yuxtapuesta"},
    {"oracion": "El bebé duerme plácidamente.", "tipo": "simple"},
    {"oracion": "El perro ladra y el gato maúlla.", "tipo": "compuesta coordinada"},
    {"oracion": "Te ayudaré cuando lo necesites.", "tipo": "compuesta subordinada"},
    {"oracion": "Luis pintó el cuadro; Ana lo vendió.", "tipo": "yuxtapuesta"},
    {"oracion": "Mi padre trabaja mucho.", "tipo": "simple"},
    {"oracion": "Escribí una carta y envié un correo.", "tipo": "compuesta coordinada"},
    {"oracion": "Estudia para que apruebes el examen.", "tipo": "compuesta subordinada"},
    {"oracion": "El avión despegó; todos aplaudieron.", "tipo": "yuxtapuesta"},
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
        print("🎮 JUEGOS SINTÁCTICOS (Versión Ampliada) 🎮")
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
