import json
import random
import time
from datetime import datetime

# Archivo para guardar las preguntas
ARCHIVO_PREGUNTAS = "colocaciones.json"

# Configuración inicial
VIDAS_INICIALES = 3
TIEMPO_POR_NIVEL = {1: 20, 2: 15, 3: 10}

# Cargar preguntas desde archivo
def cargar_preguntas():
    try:
        with open(ARCHIVO_PREGUNTAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(ARCHIVO_PREGUNTAS, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []

# Guardar nuevas preguntas
def guardar_pregunta(pregunta):
    preguntas = cargar_preguntas()
    preguntas.append(pregunta)
    with open(ARCHIVO_PREGUNTAS, "w", encoding="utf-8") as f:
        json.dump(preguntas, f, ensure_ascii=False, indent=2)

# Preguntas base + las que agregue el usuario
preguntas_base = [
    {
        "pregunta": "¿Qué verbo se usa con 'vuelta'?",
        "opciones": ["hacer", "dar", "tomar", "crear"],
        "respuesta": "dar",
        "explicacion": "RAE: 'Dar una vuelta' es convención idiomática histórica.",
        "dificultad": 1
    },
    {
        "pregunta": "¿Qué verbo acompaña a 'matrimonio'?",
        "opciones": ["contraer", "hacer", "construir", "desarrollar"],
        "respuesta": "contraer",
        "explicacion": "RAE: 'Contraer matrimonio' viene del latín 'contrahere' (unir).",
        "dificultad": 2
    },
    {
        "pregunta": "¿Cómo se completa? 'Desarrollar ______'",
        "opciones": ["velocidad", "desaliento", "sacerdocio", "virtud"],
        "respuesta": "velocidad",
        "explicacion": "RAE: Colocación técnica aceptada (vs 'ejercitar virtud').",
        "dificultad": 3
    },
    {
        "pregunta": "¿Qué preposición usa 'inverso'?",
        "opciones": ["a", "de", "en", "por"],
        "respuesta": "de",
        "explicacion": "RAE: 'Inverso de' es la forma normativa correcta.",
        "dificultad": 2
    },
    {
        "pregunta": "¿Qué verbo NO es correcto? '______ influencia'",
        "opciones": ["ejercer", "tener", "contraer", "desplegar"],
        "respuesta": "contraer",
        "explicacion": "RAE: 'Contraer' solo para deudas/enfermedades.",
        "dificultad": 3
    }
]

# Cargar todas las preguntas
todas_preguntas = preguntas_base + cargar_preguntas()

def agregar_ejemplo():
    print("\n🚀 Crear nueva pregunta:")
    nueva_pregunta = {
        "pregunta": input("Enunciado de la pregunta: "),
        "opciones": [input(f"Opción {i+1}: ") for i in range(4)],
        "respuesta": input("Respuesta correcta: "),
        "explicacion": input("Explicación RAE: "),
        "dificultad": int(input("Dificultad (1-3): "))
    }
    guardar_pregunta(nueva_pregunta)
    print("✅ ¡Pregunta guardada para futuras prácticas!")

def practicar_colocaciones():
    random.shuffle(todas_preguntas)
    vidas = VIDAS_INICIALES
    puntaje = 0
    nivel = int(input("Elige nivel (1-3): "))
    
    print(f"\n⏳ Tienes {TIEMPO_POR_NIVEL[nivel]} segundos por pregunta. ¡Vamos!")
    
    for i, pregunta in enumerate(todas_preguntas):
        if pregunta['dificultad'] > nivel:
            continue
            
        print(f"\nVidas: ❤️ × {vidas} | Puntaje: {puntaje}")
        print(f"\nPregunta {i+1}: {pregunta['pregunta']}")
        
        for idx, opcion in enumerate(pregunta['opciones'], 1):
            print(f"{idx}. {opcion}")
            
        inicio = time.time()
        
        try:
            respuesta = int(input("\nTu respuesta: ")) - 1
            tiempo = time.time() - inicio
        except:
            print("¡Respuesta inválida!")
            continue
            
        if tiempo > TIEMPO_POR_NIVEL[nivel]:
            print(f"⏰ ¡Tiempo agotado! (-1 vida)")
            vidas -= 1
        else:
            opcion_elegida = pregunta['opciones'][respuesta]
            correcta = pregunta['respuesta']
            
            if opcion_elegida == correcta:
                print(f"✅ ¡Correcto! +10 puntos")
                puntaje += 10
            else:
                print(f"❌ Incorrecto. La respuesta era: {correcta}")
                vidas -= 1
                print(f"Explicación: {pregunta['explicacion']}")
        
        if vidas <= 0:
            print("\n💀 ¡Game Over! Se acabaron las vidas")
            break

    print(f"\n🏁 Puntaje final: {puntaje}")
    if puntaje >= 80:
        print("🎖️ ¡Excelente dominio de las colocaciones!")
    elif puntaje >= 50:
        print("👍 ¡Buen trabajo, sigue mejorando!")

def menu_principal():
    while True:
        print("\n" + "═"*50)
        print(" MENÚ PRINCIPAL ".center(50, "⚡"))
        print("1. Practicar colocaciones léxicas")
        print("2. Crear y guardar nuevo ejemplo")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            practicar_colocaciones()
        elif opcion == "2":
            agregar_ejemplo()
        elif opcion == "3":
            print("¡Hasta la próxima! 📚")
            break

# Ejecutar programa
if __name__ == "__main__":
    menu_principal()
