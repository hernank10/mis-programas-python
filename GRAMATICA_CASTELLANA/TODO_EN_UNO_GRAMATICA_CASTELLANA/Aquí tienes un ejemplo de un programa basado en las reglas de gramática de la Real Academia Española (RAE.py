def mostrar_menu():
    print("\n---🌟📜✏️🕵🏛 Cuestionario: Gramática según la RAE 🌟📜✏️🕵🏛---")
    print("1️⃣ Ortografía")
    print("2️⃣  Sintaxis")
    print("️3️⃣  Morfología")
    print("4️⃣  Semántica")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")
    return opcion

def cuestionario_ortografia():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Cuál es la regla principal para el uso de la 'b' después de 'm'?": 
        "Siempre se usa 'b' después de 'm'.",
        "🌟📜✏️🕵🏛¿Qué palabras llevan tilde según las reglas generales?": 
        "Palabras agudas terminadas en vocal, 'n' o 's'; graves no terminadas en vocal, 'n' o 's'; y esdrújulas siempre.",
        "🌟📜✏️🕵🏛¿Cuál es la diferencia entre 'porque', 'porqué', 'por qué' y 'por que'?": 
        "'Porque' indica causa, 'porqué' es un sustantivo, 'por qué' introduce preguntas y 'por que' une preposición y conjunción.",
    }
    realizar_cuestionario(preguntas_respuestas)

def cuestionario_sintaxis():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué es una oración simple según la RAE?": 
        "Una oración con un solo predicado.",
        "🌟📜✏️🕵🏛¿Cómo se clasifican las oraciones según la actitud del hablante?": 
        "Enunciativas, interrogativas, exclamativas, imperativas, desiderativas y dubitativas.",
        "🌟📜✏️🕵🏛¿Qué son los modificadores directos e indirectos en sintaxis?": 
        "Directos modifican al núcleo directamente; indirectos usan enlaces como preposiciones.",
    }
    realizar_cuestionario(preguntas_respuestas)

def cuestionario_morfologia():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué diferencia hay entre un morfema derivativo y uno flexivo?": 
        "El derivativo crea palabras nuevas y el flexivo indica género, número, etc.",
        "🌟📜✏️🕵🏛¿Qué es un sufijo según la RAE?": 
        "Un morfema que se agrega al final de una palabra para modificar su significado.",
        "🌟📜✏️🕵🏛¿Qué son los determinantes?": 
        "Palabras que concretan el significado de los sustantivos.",
    }
    realizar_cuestionario(preguntas_respuestas)

def cuestionario_semantica():
    preguntas_respuestas = {
        "🌟📜✏️🕵🏛¿Qué es un sinónimo según la RAE?": 
        "Palabras con significados equivalentes o muy similares.",
        "🌟📜✏️🕵🏛¿Qué diferencia hay entre polisemia y homonimia?": 
        "La polisemia es un término con varios significados; la homonimia son palabras diferentes con la misma forma.",
        "🌟📜✏️🕵🏛¿Qué es la antonimia?": 
        "Relación entre palabras con significados opuestos.",
    }
    realizar_cuestionario(preguntas_respuestas)

def realizar_cuestionario(preguntas_respuestas):
    puntaje = 0
    for pregunta, respuesta_correcta in preguntas_respuestas.items():
        print(f"\nPregunta: {pregunta}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == respuesta_correcta.lower():
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta es: {respuesta_correcta}")
    print(f"\nTu puntaje final: {puntaje}/{len(preguntas_respuestas)}")

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
        print("🌟📜✏️🕵🏛¡Gracias por participar! Hasta la próxima.✅")
        break
    else:
        print("Opción inválida❌. Intente de nuevo.")
