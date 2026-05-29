import random
import matplotlib.pyplot as plt

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
        ("Luis respondió la pregunta ___ pensar demasiado.", "sin"),
        ("Miguel resolvió el problema ___ dudar.", "sin"),
        ("El escritor terminó su novela ___ detenerse a corregir.", "sin"),
        ("Ella logró la medalla ___ descansar en la carrera.", "sin"),
        ("Terminaron el proyecto ___ retrasarse en las entregas.", "sin"),
        ("El ciclista cruzó la meta ___ perder velocidad.", "sin")
    ]
    return random.choice(ejemplos)

def mostrar_progreso(puntajes):
    """Muestra un gráfico de progreso del usuario."""
    plt.plot(range(1, len(puntajes) + 1), puntajes, marker='o', linestyle='-', color='b')
    plt.xlabel("Intentos")
    plt.ylabel("Puntos")
    plt.title("Progreso del Usuario")
    plt.show()

def autoevaluacion():
    """Permite al usuario responder y obtiene retroalimentación inmediata."""
    puntos = 0
    intentos = 0
    puntajes = []
    logros = []
    
    while intentos < 5:
        ejercicio, respuesta_correcta = generar_ejercicio()
        respuesta_usuario = input(f"{ejercicio}\nRespuesta: ").strip().lower()
        if respuesta_usuario == respuesta_correcta:
            print("✅ ¡Correcto!")
            puntos += 10
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: '{respuesta_correcta}'")
        intentos += 1
        puntajes.append(puntos)
    
    if puntos >= 40:
        logros.append("🏆 Maestro en negación con gerundio")
    elif puntos >= 30:
        logros.append("🎖 Avanzado en negación con gerundio")
    elif puntos >= 20:
        logros.append("📜 Aprendiz en negación con gerundio")
    
    mostrar_progreso(puntajes)
    return puntos, logros

def modo_desafio():
    """Ejecuta un modo desafío cronometrado."""
    import time
    print("⏳ Modo Desafío: Responde en el menor tiempo posible!")
    inicio = time.time()
    puntos, _ = autoevaluacion()
    tiempo_total = time.time() - inicio
    print(f"⏱ Tiempo total: {tiempo_total:.2f} segundos")
    print(f"🏅 Puntos obtenidos: {puntos}")

def analizar_errores(respuestas):
    """Analiza la frecuencia de errores del usuario."""
    errores = {}
    for respuesta, correcta in respuestas:
        if respuesta != correcta:
            errores[correcta] = errores.get(correcta, 0) + 1
    print("\n🔎 Análisis de errores:")
    for error, frecuencia in errores.items():
        print(f"- '{error}' fue respondido incorrectamente {frecuencia} veces.")

def ejemplos_textos():
    """Muestra ejemplos de textos literarios reales con negación de gerundio."""
    ejemplos = [
        "Don Quijote cabalgaba no pensando en las consecuencias de su aventura.",
        "Ella leía el poema no sintiendo el paso del tiempo.",
        "Las olas golpeaban la costa sin dejar de bramar en la noche oscura."
    ]
    for ejemplo in ejemplos:
        print(f"📖 {ejemplo}")

def main():
    print("📖 Bienvenido al programa de práctica sobre la negación con gerundio.")
    nivel = 1
    respuestas_usuario = []
    while nivel <= 3:
        print(f"\n🌟 Nivel {nivel}")
        puntos, logros = autoevaluacion()
        print(f"🎯 Puntos obtenidos: {puntos}")
        if logros:
            print("🏅 Logros obtenidos:", ", ".join(logros))
        if puntos >= 30:
            print("¡Felicidades! Has avanzado al siguiente nivel.")
            nivel += 1
        else:
            print("Inténtalo de nuevo para mejorar tu precisión.")
            break
    analizar_errores(respuestas_usuario)
    ejemplos_textos()
    print("Gracias por participar. ¡Sigue practicando!")

if __name__ == "__main__":
    main()
