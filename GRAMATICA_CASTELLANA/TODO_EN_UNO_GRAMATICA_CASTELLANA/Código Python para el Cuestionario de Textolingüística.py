import random

# Preguntas y respuestas
preguntas = [
    # Cohesión textual
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué es la cohesión textual?",
     "opciones": ["A) La secuencia lógica de ideas en un texto",
                  "B) El uso de conectores y recursos cohesivos",
                  "C) La correcta ortografía de las palabras",
                  "D) La calidad estética de un texto"], "respuesta": "B"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛 (F O V) La cohesión y la coherencia son lo mismo.", "respuesta": "F"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛 Menciona un ejemplo de un recurso cohesivo.",
     "respuesta": "Conjunciones"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué tipo de conector introduce una causa?",
     "opciones": ["A) Contraste", "B) Aditivo", "C) Causal", "D) Temporal"], "respuesta": "C"},
    
    # Coherencia textual
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué es la coherencia textual?",
     "opciones": ["A) La corrección gramatical de las oraciones",
                  "B) Las relaciones lógicas entre las ideas en un texto",
                  "C) La extensión de un párrafo",
                  "D) La riqueza del vocabulario"], "respuesta": "B"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛 (F O V) Un texto coherente puede carecer de cohesión.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛¿Qué principio asegura que el texto tenga sentido como un todo?",
     "respuesta": "Coherencia"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué se requiere para que un texto tenga coherencia global?",
     "opciones": ["A) Uso adecuado de los tiempos verbales",
                  "B) Una idea principal clara",
                  "C) Oraciones cortas",
                  "D) Un vocabulario amplio"], "respuesta": "B"},
    
    # Tipos de textos
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué tipo de texto explica o informa sobre un tema?",
     "opciones": ["A) Narrativo", "B) Descriptivo", "C) Expositivo", "D) Argumentativo"], "respuesta": "C"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛 (F O V) Los textos narrativos siempre incluyen diálogos.", "respuesta": "F"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛¿Qué tipo de texto presenta y defiende un punto de vista?",
     "respuesta": "Argumentativo"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Cuál de estos NO es un tipo de texto?",
     "opciones": ["A) Instructivo", "B) Persuasivo", "C) Poético", "D) Inventivo"], "respuesta": "D"},
    
    # Gramática y sintaxis en los textos
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Cuál es la función de una oración temática en un párrafo?",
     "opciones": ["A) Agregar ejemplos",
                  "B) Resumir el párrafo",
                  "C) Introducir la idea principal",
                  "D) Concluir el texto"], "respuesta": "C"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛 (F O V) Una oración compuesta contiene al menos dos proposiciones.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛¿Qué término se refiere a una proposición que depende de otra en una oración?",
     "respuesta": "Proposición subordinada"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Cuál es la función de los signos de puntuación en un texto?",
     "opciones": ["A) Decorar el texto",
                  "B) Agregar ritmo",
                  "C) Clarificar el significado",
                  "D) Proveer cohesión"], "respuesta": "C"},
    
    # Producción de textos
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Cuál es el primer paso en la producción de un texto?",
     "opciones": ["A) Redacción", "B) Revisión", "C) Planificación", "D) Edición"], "respuesta": "C"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛 (F O V) Un texto bien estructurado siempre tiene introducción, desarrollo y conclusión.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛¿Qué proceso implica verificar la corrección gramatical de un texto?",
     "respuesta": "Corrección de estilo"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Cuál es un elemento clave en los textos narrativos?",
     "opciones": ["A) Argumentos", "B) Personajes", "C) Explicaciones", "D) Sinónimos"], "respuesta": "B"},
    
    # Análisis del discurso
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué estudia el análisis del discurso?",
     "opciones": ["A) La estructura gramatical de las oraciones",
                  "B) Cómo se interpretan los textos en contexto",
                  "C) La historia de las lenguas",
                  "D) El origen de las palabras"], "respuesta": "B"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛 (F O V) El análisis del discurso solo aplica a textos escritos.", "respuesta": "F"},
    {"tipo": "abierta", "pregunta": "¿pregunta abierta📜✏️🕵🏛Qué término se usa para referirse al significado implícito detrás de un texto?",
     "respuesta": "Pragmática"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Cuál de estos es un ejemplo de discurso oral?",
     "opciones": ["A) Una novela", "B) Una conversación", "C) Un informe", "D) Una biografía"], "respuesta": "B"},
    
    # Pragmática y contexto
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué aporta el contexto a la interpretación de un texto?",
     "opciones": ["A) Coherencia", "B) Reglas ortográficas", "C) Vocabulario", "D) Significado"], "respuesta": "D"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛 (F O V) El contexto incluye el trasfondo social y cultural de la comunicación.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛¿Cómo se denomina al receptor de un texto?", "respuesta": "Audiencia"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué término se refiere al significado implícito en la comunicación?",
     "opciones": ["A) Denotación", "B) Connotación", "C) Inferencia", "D) Sintaxis"], "respuesta": "B"},
]

# Funciones de ejecución del cuestionario
def mostrar_pregunta(pregunta):
    print("\n" + pregunta["pregunta"])
    if pregunta["tipo"] == "opcion_multiple":
        for opcion in pregunta["opciones"]:
            print(opcion)
    respuesta = input("Tu respuesta: ").strip()
    return respuesta

def validar_respuesta(pregunta, respuesta):
    if pregunta["tipo"] == "abierta":
        return respuesta.lower() == pregunta["respuesta"].lower()
    return respuesta.upper() == pregunta["respuesta"].upper()

def cuestionario():
    puntaje = 0
    random.shuffle(preguntas)  # Mezclar preguntas
    for i, pregunta in enumerate(preguntas[:20]):  # Limitar a 20 preguntas
        print(f"\nPregunta {i + 1}:")
        respuesta = mostrar_pregunta(pregunta)
        if validar_respuesta(pregunta, respuesta):
            print("¡Correcto!✅")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era: {pregunta['respuesta']}")
    print(f"\n¡Completaste el cuestionario! Tu puntaje final es {puntaje}/{len(preguntas[:20])}.")

# Ejecutar el cuestionario
cuestionario()
