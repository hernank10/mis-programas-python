import threading
import time
from playsound import playsound

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n---🌟📜✏️🕵🏛 Cuestionario: Gramática según la RAE 🌟📜✏️🕵🏛---")
    print("1️⃣  Ortografía")
    print("2️⃣  Sintaxis")
    print("️3️⃣  Morfología")
    print("4️⃣ Semántica")
    print("5. Ver progreso")
    print("6. Salir")
    opcion = input("🌟📜✏️🕵🏛Seleccione una opción (1-6): ")
    return opcion

# Temporizador
respuesta_recibida = False

def temporizador(tiempo):
    global respuesta_recibida
    for i in range(tiempo):
        if respuesta_recibida:
            return
        time.sleep(1)
    if not respuesta_recibida:
        print("\n🌟📜✏️🕵🏛¡Tiempo agotado!")

# Función para realizar un cuestionario
def realizar_cuestionario(preguntas_respuestas, categoria):
    global respuesta_recibida
    puntaje = 0
    respuestas = []
    tiempo_por_pregunta = 10  # segundos

    for pregunta, respuesta_correcta in preguntas_respuestas.items():
        print(f"\nPregunta ({categoria}): {pregunta}")
        respuesta_recibida = False
        timer = threading.Thread(target=temporizador, args=(tiempo_por_pregunta,))
        timer.start()
        
        respuesta = input("Tu respuesta: ").strip()
        respuesta_recibida = True
        timer.join()

        if respuesta.lower() == respuesta_correcta.lower():
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            puntaje += 1
            respuestas.append((pregunta, respuesta, "Correcto"))
        else:
            print(f"Incorrecto.❌ La respuesta correcta es: {respuesta_correcta}")
            respuestas.append((pregunta, respuesta, "Incorrecto"))

    guardar_progreso(categoria, puntaje, respuestas)
    print(f"\nTu puntaje final en {categoria}: {puntaje}/{len(preguntas_respuestas)}")

# Función para guardar el progreso
def guardar_progreso(categoria, puntaje, respuestas):
    with open("progreso.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\n--- Progreso en {categoria} ---\n")
        archivo.write(f"Puntaje: {puntaje}/{len(respuestas)}\n")
        for pregunta, respuesta, estado in respuestas:
            archivo.write(f"Pregunta: {pregunta}\nRespuesta: {respuesta}\nResultado: {estado}\n")
        archivo.write("\n")

# Función para mostrar el progreso guardado
def ver_progreso():
    try:
        with open("progreso.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("\n--- Progreso guardado ---")
            print(contenido)
    except FileNotFoundError:
        print("\nNo hay progreso guardado aún.")

# Cuestionarios de ejemplo
def cuestionario_ortografia():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué palabras llevan tilde según las reglas generales?": 
        "Palabras agudas terminadas en vocal, 'n' o 's'; graves no terminadas en vocal, 'n' o 's'; y esdrújulas siempre.",
        "🌟📜✏️🕵🏛¿Cómo se escribe correctamente: 'haber' o 'a ver'?": 
        "Depende del contexto.",
    }
    realizar_cuestionario(preguntas_respuestas, "Ortografía")

def cuestionario_sintaxis():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué es una oración simple según la RAE?": 
        "Una oración con un solo predicado.",
        "🌟📜✏️🕵🏛¿Cómo se clasifican las oraciones según la actitud del hablante?": 
        "Enunciativas, interrogativas, exclamativas, imperativas, desiderativas y dubitativas.",
    }
    realizar_cuestionario(preguntas_respuestas, "Sintaxis")

def cuestionario_morfologia():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué es un sufijo según la RAE?": 
        "Un morfema que se agrega al final de una palabra para modificar su significado.",
        "🌟📜✏️🕵🏛¿Qué son los determinantes?": 
        "Palabras que concretan el significado de los sustantivos.",
    }
    realizar_cuestionario(preguntas_respuestas, "Morfología")

def cuestionario_semantica():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué es un sinónimo según la RAE?": 
        "Palabras con significados equivalentes o muy similares.",
        "🌟📜✏️🕵🏛¿Qué diferencia hay entre polisemia y homonimia?": 
        "La polisemia es un término con varios significados; la homonimia son palabras diferentes con la misma forma.",
    }
    realizar_cuestionario(preguntas_respuestas, "Semántica")

# Reproducir sonido inicial
playsound("intro.mp3")

# Programa principal
while True:
    opcion = mostrar_menu()
    if opcion == "1":
        cuestionario_ortografia()
    elif opcion == "2":
        cuestionario_sintaxis()
    elif opcion == "3":
        cuestionario_morfologia()
    elif opcion == "4":
        cuestionario_semantica()
    elif opcion == "5":
        ver_progreso()
    elif opcion == "6":
        print("🌟📜✏️🕵🏛¡Gracias por participar! Hasta la próxima.✅")
        break
    else:
        print("Opción inválida.❌ Intente de nuevo.")
