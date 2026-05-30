import time
import sys

# Preguntas por estilo con íconos variados
preguntas_opcion_multiple = [
    {"pregunta": "✏️ ¿Cuál es el uso correcto del punto y coma en oraciones adversativas?",
     "opciones": ["a) Para separar elementos de una lista compleja",
                  "b) Para relacionar ideas que se contraponen",
                  "c) Para indicar el final de un párrafo"],
     "respuesta": "b"}
]

preguntas_verdadero_falso = [
    {"pregunta": "🖋️ Las oraciones compuestas siempre tienen un solo verbo. (Verdadero/Falso)",
     "respuesta": "falso"}
]

preguntas_abiertas = [
    {"pregunta": "📜 Escribe un ejemplo de oración que use correctamente el punto y coma.",
     "respuesta": "personalizado"}
]

preguntas_completar = [
    {"pregunta": "🖌️ Completa: El sujeto de una oración indica ___ realiza la acción del verbo.",
     "respuesta": "quién"}
]

# Función para manejar opción múltiple
def opcion_multiple(tiempo_restante):
    puntaje = 0
    for pregunta in preguntas_opcion_multiple:
        if tiempo_restante() <= 0:
            print("⏳ El tiempo del taller se ha agotado.")
            break
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta = input("Tu respuesta (a/b/c): ").lower()
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto! 🌟")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {pregunta['respuesta']}.")
        time.sleep(1)
    return puntaje

# Función para manejar verdadero/falso
def verdadero_falso(tiempo_restante):
    puntaje = 0
    for pregunta in preguntas_verdadero_falso:
        if tiempo_restante() <= 0:
            print("⏳ El tiempo del taller se ha agotado.")
            break
        print(pregunta["pregunta"])
        respuesta = input("Tu respuesta (Verdadero/Falso): ").lower()
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto! 🌟")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {pregunta['respuesta']}.")
        time.sleep(1)
    return puntaje

# Función para manejar preguntas abiertas
def preguntas_abiertas(tiempo_restante):
    for pregunta in preguntas_abiertas:
        if tiempo_restante() <= 0:
            print("⏳ El tiempo del taller se ha agotado.")
            break
        print(pregunta["pregunta"])
        respuesta = input("Escribe tu respuesta: ")
        print(f"Respuesta recibida: {respuesta}. ¡Revisa con tu instructor para verificarla! 😊")
        time.sleep(1)

# Función para manejar completar espacios
def completar_espacios(tiempo_restante):
    puntaje = 0
    for pregunta in preguntas_completar:
        if tiempo_restante() <= 0:
            print("⏳ El tiempo del taller se ha agotado.")
            break
        print(pregunta["pregunta"])
        respuesta = input("Completa: ").lower()
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto! 🌟")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {pregunta['respuesta']}.")
        time.sleep(1)
    return puntaje

# Menú principal con temporizador global
def menu_principal():
    print("🎓 Bienvenido al taller interactivo de gramática castellana.\n")
    print("1. Opción múltiple ✏️")
    print("2. Verdadero/Falso 🖋️")
    print("3. Preguntas abiertas 📜")
    print("4. Completar espacios 🖌️")
    print("5. Salir 🚪")
    
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
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            puntaje_total += opcion_multiple(tiempo_restante)
        elif opcion == "2":
            puntaje_total += verdadero_falso(tiempo_restante)
        elif opcion == "3":
            preguntas_abiertas(tiempo_restante)
        elif opcion == "4":
            puntaje_total += completar_espacios(tiempo_restante)
        elif opcion == "5":
            print(f"🏆 Has terminado el taller. Tu puntaje final es: {puntaje_total}")
            break
        else:
            print("⚠️ Opción no válida. Inténtalo nuevamente.")
        print("\n")

# Ejecutar el programa
menu_principal()
