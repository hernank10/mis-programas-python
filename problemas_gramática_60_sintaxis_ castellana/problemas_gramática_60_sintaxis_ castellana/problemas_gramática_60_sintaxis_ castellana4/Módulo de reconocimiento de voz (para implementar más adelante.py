import time
import difflib
import json
from datetime import datetime

# Módulos para voz y reconocimiento (a integrar después)
# import pyttsx3
# import speech_recognition as sr

# Diccionario de relaciones retóricas y ejemplos
relaciones = {
    "Narración": {
        "definición": "Relación entre oraciones en las que un hecho ocurre antes que el siguiente (secuencia temporal).",
        "ejemplo": "María se levantó. Juan la saludó."
    },
    "Resultado": {
        "definición": "Un hecho es resultado de otro anterior.",
        "ejemplo": "María empujó a Juan. Juan se cayó."
    },
    "Ampliación": {
        "definición": "Una oración amplía o detalla información de otra.",
        "ejemplo": "María pintó un cuadro. Usó acrílicas y óleo."
    },
    "Contraste": {
        "definición": "Se presentan ideas opuestas o contrastantes.",
        "ejemplo": "María es rubia. Pero Juan es moreno."
    },
    "Paralelo": {
        "definición": "Se presentan ideas similares o equivalentes.",
        "ejemplo": "María es rubia. Juan también es rubio."
    }
}

usuario_ejemplos = []


def mostrar_menu():
    print("\nMENÚ PRINCIPAL")
    print("1. Estudiar teoría")
    print("2. Practicar conceptos con temporizador")
    print("3. Evaluar escritura de memoria")
    print("4. Agregar ejemplo propio")
    print("5. Exportar progreso")
    print("6. Salir")

def estudiar_teoria():
    for nombre, contenido in relaciones.items():
        print(f"\n--- {nombre.upper()} ---")
        print("Definición:", contenido["definición"])
        print("Ejemplo:", contenido["ejemplo"])
        input("Presiona Enter para continuar...")

        # Sintetizar voz (opcional)
        # sintetizar_voz(f"{nombre}. {contenido['definición']}. Ejemplo: {contenido['ejemplo']}")

def practicar_conceptos():
    for nombre, contenido in relaciones.items():
        print(f"\nEscribe de nuevo el concepto de: {nombre}")
        input("Presiona Enter para mostrar definición...")
        print("Definición:", contenido["definición"])
        tiempo = int(input("\n¿En cuántos segundos deseas volver a escribirlo de memoria?: "))
        print(f"Espera {tiempo} segundos para memorizar...")
        time.sleep(tiempo)
        print("\nAhora escribe la definición de memoria:")
        respuesta = input("→ ")
        evaluar_respuesta(contenido["definición"], respuesta)

def evaluar_respuesta(original, respuesta):
    sm = difflib.SequenceMatcher(None, original.lower(), respuesta.lower())
    porcentaje = round(sm.ratio() * 100, 2)
    print(f"\nCoincidencia: {porcentaje}%")
    if porcentaje >= 90:
        print("✅ ¡Muy bien! Lo memorizaste casi perfectamente.")
    elif porcentaje >= 70:
        print("✔️ Casi perfecto, sigue practicando.")
    else:
        print("❌ Sigue practicando. Revisa la teoría nuevamente.")

def agregar_ejemplo():
    if len(usuario_ejemplos) >= 100:
        print("⚠️ Ya has alcanzado el límite de 100 ejemplos guardados.")
        return
    tipo = input("Tipo de relación (Narración, Resultado, etc.): ")
    ejemplo = input("Escribe tu ejemplo: ")
    usuario_ejemplos.append({"tipo": tipo, "ejemplo": ejemplo})
    print("✅ Ejemplo guardado con éxito.")

def exportar():
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archivo = f"progreso_{fecha}.txt"
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write("PROGRESO DEL USUARIO\n")
        f.write("Ejemplos personalizados:\n")
        for i, ej in enumerate(usuario_ejemplos):
            f.write(f"{i+1}. [{ej['tipo']}] {ej['ejemplo']}\n")
    print(f"✅ Progreso exportado exitosamente en '{archivo}'")

# Módulo de voz (para implementar más adelante)
# def sintetizar_voz(texto):
#     engine = pyttsx3.init()
#     engine.say(texto)
#     engine.runAndWait()

# Módulo de reconocimiento de voz (para implementar más adelante)
# def reconocer_voz():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Habla ahora...")
#         audio = recognizer.listen(source)
#     try:
#         texto = recognizer.recognize_google(audio, language='es-ES')
#         print("Texto reconocido:", texto)
#         return texto
#     except sr.UnknownValueError:
#         print("No se entendió lo que dijiste.")
#     except sr.RequestError:
#         print("Error al conectar con el servicio de reconocimiento.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")

    if opcion == "1":
        estudiar_teoria()
    elif opcion == "2":
        practicar_conceptos()
    elif opcion == "3":
        practicar_conceptos()
    elif opcion == "4":
        agregar_ejemplo()
    elif opcion == "5":
        exportar()
    elif opcion == "6":
        print("¡Hasta la próxima! 👋")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
