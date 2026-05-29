import time
import random

# Sonidos de los fonemas (simulando archivos de sonido en una lista)
# Nota: En un entorno real, necesitarías usar una biblioteca como 'pygame' o 'pydub' para reproducir sonidos.
# Aquí solo se simula con texto para la demostración.

sonidos_fonemas = {
    "p": "🔊 Sonido de 'p' como en 'pato'",
    "b": "🔊 Sonido de 'b' como en 'barco'",
    "d": "🔊 Sonido de 'd' como en 'dedo'",
    "t": "🔊 Sonido de 't' como en 'taza'",
    "k": "🔊 Sonido de 'k' como en 'casa'",
    "g": "🔊 Sonido de 'g' como en 'gato'",
    "f": "🔊 Sonido de 'f' como en 'flor'",
    "s": "🔊 Sonido de 's' como en 'serpiente'",
    "m": "🔊 Sonido de 'm' como en 'mano'",
    "n": "🔊 Sonido de 'n' como en 'noche'"
}

# Preguntas basadas en fonología
preguntas_fonemas = [
    {"pregunta": "👂 ¿Qué fonema corresponde al sonido de 'p'?", "respuesta": "p"},
    {"pregunta": "👂 ¿Qué fonema corresponde al sonido de 'b'?", "respuesta": "b"},
    {"pregunta": "👂 ¿Qué fonema corresponde al sonido de 'd'?", "respuesta": "d"},
    {"pregunta": "👂 ¿Qué fonema corresponde al sonido de 't'?", "respuesta": "t"},
    {"pregunta": "👂 ¿Qué fonema corresponde al sonido de 'k'?", "respuesta": "k"},
]

# Función para mostrar las preguntas de fonología
def mostrar_fonema(sonido):
    print(f"{sonido}")

# Función para manejar la interacción del cuestionario
def cuestionario_fonologico(preguntas, tiempo_restante):
    puntaje = 0
    for pregunta in preguntas:
        if tiempo_restante() <= 0:
            print("⏳ El tiempo del taller se ha agotado.")
            break
        print(pregunta["pregunta"])
        sonido = random.choice(list(sonidos_fonemas.values()))
        mostrar_fonema(sonido)  # Reproducir o mostrar el sonido
        respuesta = input("Escribe el fonema correspondiente (p, b, d, t, k): ").lower()
        if respuesta == pregunta["respuesta"]:
            print("✅ Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {pregunta['respuesta']}.")
        time.sleep(1)
    return puntaje

# Función para manejar preguntas abiertas
def preguntas_abiertas_fonologia(preguntas, tiempo_restante):
    for pregunta in preguntas:
        if tiempo_restante() <= 0:
            print("⏳ El tiempo del taller se ha agotado.")
            break
        print(pregunta["pregunta"])
        respuesta = input("Escribe el fonema correspondiente: ").lower()
        if respuesta == pregunta["respuesta"]:
            print("✅ Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {pregunta['respuesta']}.")
        time.sleep(1)

# Menú principal con temporizador
def menu_fonologia():
    print("🎶 Bienvenido al taller interactivo de Fonología Castellana.\n")
    print("1. Fonemas y sus sonidos 🔊")
    print("2. Salir 🚪")

    puntaje_total = 0
    tiempo_maximo = 2 * 60 * 60  # Dos horas en segundos
    tiempo_inicio = time.time()

    # Función para calcular tiempo restante
    def tiempo_restante():
        return tiempo_maximo - (time.time() - tiempo_inicio)

    while True:
        if tiempo_restante() <= 0:
            print("⏳ El tiempo del taller se ha agotado. ¡Gracias por participar!")
            break

        print(f"\n⏰ Tiempo restante del taller: {int(tiempo_restante() // 60)} minutos.")
        opcion = input("Selecciona una opción (1-2): ")
        if opcion == "1":
            puntaje_total += cuestionario_fonologico(preguntas_fonemas, tiempo_restante)
        elif opcion == "2":
            print(f"🏆 Has terminado el taller. Tu puntaje final es: {puntaje_total}")
            break
        else:
            print("⚠️ Opción no válida. Inténtalo nuevamente.")
        print("\n")

# Ejecutar el programa
menu_fonologia()
