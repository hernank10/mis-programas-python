import random
import time

oraciones = [
    {
        "texto": "El gato duerme plácidamente en el sillón.",
        "pregunta": "¿Cuál es el complemento circunstancial?",
        "opciones": ["El gato", "duerme", "plácidamente en el sillón", "gato duerme"],
        "respuesta": "plácidamente en el sillón"
    },
    {
        "texto": "Mi hermana cocina galletas con chocolate los domingos.",
        "pregunta": "¿Cuál es el sujeto de la oración?",
        "opciones": ["Mi hermana", "cocina", "galletas con chocolate", "los domingos"],
        "respuesta": "Mi hermana"
    },
    {
        "texto": "Los estudiantes escriben sus ensayos con dedicación.",
        "pregunta": "¿Cuál es el verbo?",
        "opciones": ["Los estudiantes", "escriben", "sus ensayos", "con dedicación"],
        "respuesta": "escriben"
    },
]

vidas = 3
puntos = 0

print("\n🎮 ¡Bienvenido al Laberinto del Predicado!")
print("Responde correctamente para avanzar. Tienes 3 vidas.\n")

for ronda, oracion in enumerate(oraciones, 1):
    print(f"🧠 Nivel {ronda}:")
    print(f"📜 Oración: {oracion['texto']}")
    print(f"❓ Pregunta: {oracion['pregunta']}\n")
    
    opciones = oracion["opciones"]
    random.shuffle(opciones)
    
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    
    eleccion = input("👉 Elige la opción correcta (1-4): ")
    
    try:
        eleccion_int = int(eleccion) - 1
        if opciones[eleccion_int] == oracion["respuesta"]:
            puntos += 1
            print("✅ ¡Correcto! Has avanzado en el laberinto.\n")
        else:
            vidas -= 1
            print(f"❌ Incorrecto. Te quedan {vidas} vidas.\n")
        time.sleep(1)
    except:
        print("⚠️ Entrada no válida. Pierdes una vida.\n")
        vidas -= 1
        time.sleep(1)
    
    if vidas == 0:
        print("💀 Has perdido todas tus vidas. El laberinto te atrapó...\n")
        break

if vidas > 0:
    print(f"🎉 ¡Felicitaciones! Completaste el laberinto con {puntos} respuestas correctas.\n")
