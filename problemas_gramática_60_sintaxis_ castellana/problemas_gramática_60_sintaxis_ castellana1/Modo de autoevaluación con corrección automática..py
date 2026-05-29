import random

def clasificar_verbo(verbo):
    """Clasifica el verbo en logro, actividad, estado o semelfactivo."""
    verbos_logro = ["descubrir", "ganar", "llegar", "morir", "nacer"]
    verbos_actividad = ["correr", "leer", "nadar", "escribir", "estudiar"]
    verbos_estado = ["ser", "estar", "parecer", "existir", "conocer"]
    verbos_semelfactivos = ["toser", "pestañear", "golpear", "chasquear", "saltar"]
    
    if verbo in verbos_logro:
        return "logro"
    elif verbo in verbos_actividad:
        return "actividad"
    elif verbo in verbos_estado:
        return "estado"
    elif verbo in verbos_semelfactivos:
        return "semelfactivo"
    else:
        return "desconocido"

def generar_ejercicio():
    """Genera un ejercicio de completación con la negación del gerundio."""
    ejemplos = [
        ("Aprobó el examen ___ estudiar.", "sin"),
        ("Juan caminaba ___ prestar atención.", "sin"),
        ("El profesor explicó la lección ___ repetir las instrucciones.", "sin"),
        ("María entró al salón ___ tocar la puerta.", "sin"),
        ("Luis respondió la pregunta ___ pensar demasiado.", "sin")
    ]
    return random.choice(ejemplos)

def autoevaluacion():
    """Permite al usuario responder y obtiene retroalimentación inmediata."""
    puntos = 0
    intentos = 0
    while intentos < 5:
        ejercicio, respuesta_correcta = generar_ejercicio()
        respuesta_usuario = input(f"{ejercicio}\nRespuesta: ").strip().lower()
        if respuesta_usuario == respuesta_correcta:
            print("✅ ¡Correcto!")
            puntos += 10
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: '{respuesta_correcta}'")
        intentos += 1
    return puntos

def analizar_errores(respuestas):
    """Analiza la frecuencia de errores del usuario."""
    errores = {}
    for respuesta, correcta in respuestas:
        if respuesta != correcta:
            errores[correcta] = errores.get(correcta, 0) + 1
    print("\n🔎 Análisis de errores:")
    for error, frecuencia in errores.items():
        print(f"- '{error}' fue respondido incorrectamente {frecuencia} veces.")

def main():
    print("📖 Bienvenido al programa de práctica sobre la negación con gerundio.")
    nivel = 1
    respuestas_usuario = []
    while nivel <= 3:
        print(f"\n🌟 Nivel {nivel}")
        puntos = autoevaluacion()
        print(f"🎯 Puntos obtenidos: {puntos}")
        if puntos >= 30:
            print("¡Felicidades! Has avanzado al siguiente nivel.")
            nivel += 1
        else:
            print("Inténtalo de nuevo para mejorar tu precisión.")
            break
    analizar_errores(respuestas_usuario)
    print("Gracias por participar. ¡Sigue practicando!")

if __name__ == "__main__":
    main()
