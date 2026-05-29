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
#  JUEGO 3: EL CORRECTOR DE ORACIONES
# ================================
ejercicios_corrector = [
    {
        "incorrecta": "Yo fui a la tienda, y compré pan, pero leche.",
        "opciones": [
            "Yo fui a la tienda y compré pan, pero no leche.",
            "Yo fui a la tienda compré pan pero leche."
        ],
        "correcta": 0
    },
    {
        "incorrecta": "El perro ladra, el gato maúlla, sin embargo los pájaros vuelan.",
        "opciones": [
            "El perro ladra, el gato maúlla y los pájaros vuelan.",
            "El perro ladra y el gato maúlla sin embargo, los pájaros vuelan."
        ],
        "correcta": 0
    },
    {
        "incorrecta": "Fuimos al parque porque hacía sol, pero estaba lloviendo.",
        "opciones": [
            "Fuimos al parque porque hacía sol.",
            "Fuimos al parque pero estaba lloviendo."
        ],
        "correcta": 1
    }
]

def corrector_oraciones():
    print("\n✍️ El Corrector de Oraciones ✍️")
    ejercicio = random.choice(ejercicios_corrector)
    print(f"\n👉 Oración incorrecta: {ejercicio['incorrecta']}")
    
    for i, opcion in enumerate(ejercicio["opciones"]):
        print(f"{i+1}. {opcion}")
    
    respuesta = input("Elige la opción correcta (1 o 2): ").strip()
    
    if respuesta.isdigit() and int(respuesta)-1 == ejercicio["correcta"]:
        print("✅ ¡Correcto! 🎉 Has corregido la oración.")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {ejercicio['opciones'][ejercicio['correcta']]}")

# ================================
#  JUEGO 4: CONSTRUYE TU PROPIA ORACIÓN
# ================================
sujetos = ["El perro", "María", "Los niños", "Mi hermano", "La maestra"]
verbos = ["corre", "canta", "juega", "lee", "enseña"]
complementos = ["en el parque", "una canción", "matemáticas", "muy rápido", "un libro"]

def construye_oracion():
    print("\n🧩 Construye tu Propia Oración 🧩")
    sujeto = random.choice(sujetos)
    verbo = random.choice(verbos)
    complemento = random.choice(complementos)
    
    print(f"👉 Palabras disponibles: {sujeto} | {verbo} | {complemento}")
    print("Forma una oración simple uniendo las tres partes.")
    
    respuesta = input("✏️ Escribe tu oración: ").strip()
    oracion_correcta = f"{sujeto} {verbo} {complemento}"
    
    if respuesta.lower() == oracion_correcta.lower():
        print("✅ ¡Excelente! 🎉 Has formado bien la oración.")
    else:
        print(f"❌ No es correcto. Una opción válida era: {oracion_correcta}")

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
        print("3. El Corrector de Oraciones")
        print("4. Construye tu Propia Oración")
        print("5. Salir")
        
        opcion = input("\n👉 Elige un juego (1-5): ").strip()
        
        if opcion == "1":
            cazador_sujeto_predicado()
        elif opcion == "2":
            clasifica_oracion()
        elif opcion == "3":
            corrector_oraciones()
        elif opcion == "4":
            construye_oracion()
        elif opcion == "5":
            print("👋 Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar menú principal
if __name__ == "__main__":
    menu()
