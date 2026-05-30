import random

# Lista de preguntas con opciones y respuestas correctas
preguntas = [
    {
        "enunciado": "¿Cuál es la colocación correcta?",
        "frase": "Voy a ___ una vuelta por el parque.",
        "opciones": ["hacer", "dar", "tomar", "crear"],
        "respuesta": "dar"
    },
    {
        "enunciado": "¿Qué verbo se asocia correctamente con 'desaliento'?",
        "frase": "En el equipo ___ el desaliento tras la derrota.",
        "opciones": ["cunde", "aparece", "brota", "surge"],
        "respuesta": "cunde"
    },
    {
        "enunciado": "¿Cuál es la expresión idiomática aceptada?",
        "frase": "Van a ___ matrimonio el próximo mes.",
        "opciones": ["formar", "hacer", "contraer", "crear"],
        "respuesta": "contraer"
    },
    {
        "enunciado": "¿Qué combinación es correcta?",
        "frase": "Es importante ___ la virtud desde la infancia.",
        "opciones": ["ejercer", "ejercitar", "imponer", "proyectar"],
        "respuesta": "ejercitar"
    },
    {
        "enunciado": "¿Cuál es la preposición correcta con 'inverso'?",
        "frase": "La operación es inversa __ la anterior.",
        "opciones": ["a", "de", "con", "por"],
        "respuesta": "de"
    },
    {
        "enunciado": "¿Qué forma es correcta según el uso idiomático?",
        "frase": "Debemos ___ la actividad empresarial.",
        "opciones": ["activar", "desarrollar", "generar", "organizar"],
        "respuesta": "desarrollar"
    },
    {
        "enunciado": "¿Cuál es la construcción verbal adecuada?",
        "frase": "___ influencia en su entorno.",
        "opciones": ["Ejercita", "Ejecuta", "Ejerce", "Ejercita"],
        "respuesta": "Ejerce"
    },
    {
        "enunciado": "¿Con qué preposición se construye correctamente 'contrario'?",
        "frase": "Este argumento es contrario __ tu punto de vista.",
        "opciones": ["a", "de", "con", "en"],
        "respuesta": "a"
    }
]

def jugar():
    random.shuffle(preguntas)
    puntaje = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta['enunciado']}")
        print(pregunta["frase"])
        for idx, opcion in enumerate(pregunta["opciones"], 1):
            print(f"  {idx}. {opcion}")
        try:
            respuesta_usuario = int(input("Tu respuesta (número): "))
            seleccionada = pregunta["opciones"][respuesta_usuario - 1]
            if seleccionada == pregunta["respuesta"]:
                print("✅ ¡Correcto!")
                puntaje += 1
            else:
                print(f"❌ Incorrecto. La respuesta correcta es: '{pregunta['respuesta']}'")
        except (ValueError, IndexError):
            print("❗ Entrada inválida. Por favor, escribe el número de una opción válida.")
    print(f"\n🎯 Tu puntaje final es: {puntaje}/{len(preguntas)}")

# Inicio del programa
print("🧠 Bienvenido al juego de afinidades léxicas del español\n")
jugar()
