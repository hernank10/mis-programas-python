import random

# Preguntas y respuestas
preguntas = [
    # Orígenes y evolución del español
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛 ¿De qué lengua proviene principalmente el español?",
     "opciones": ["A) Árabe", "B) Latín", "C) Griego", "D) Germánico"], "respuesta": "B"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛(F O V) El español es una lengua romance.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "🌟📜✏️🕵🏛 pregunta abierta ¿Qué nombre se le da al latín del cual deriva el español?",
     "respuesta": "Latín vulgar"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛 ¿En qué siglo se consolidó el castellano como lengua escrita estándar?",
     "opciones": ["A) Siglo VIII", "B) Siglo X", "C) Siglo XIII", "D) Siglo XV"], "respuesta": "C"},
    
    # Influencias externas
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Cuál de estas lenguas influyó significativamente en el español medieval?",
     "opciones": ["A) Árabe", "B) Inglés", "C) Portugués", "D) Francés"], "respuesta": "A"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛(F O V) El árabe introdujo más de 4,000 palabras al español.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛Menciona una palabra española de origen árabe.",
     "respuesta": "Ojalá (u otras similares)"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛 ¿Qué pueblo introdujo términos relacionados con la guerra al español?",
     "opciones": ["A) Visigodos", "B) Romanos", "C) Celtíberos", "D) Fenicios"], "respuesta": "A"},
    
    # Etapas de desarrollo del español
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛 ¿Cuál es la primera etapa del español?",
     "opciones": ["A) Castellano medieval", "B) Español moderno", "C) Castellano primitivo", "D) Latín vulgar"], "respuesta": "C"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛(F O V) El español moderno comenzó a desarrollarse en el siglo XVII.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "🌟📜✏️🕵🏛pregunta abierta  ¿Qué hecho histórico marcó la unificación del español como lengua oficial en España?",
     "respuesta": "La publicación de la Gramática de Nebrija"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué etapa del español estuvo marcada por el enriquecimiento léxico y estilístico debido al Siglo de Oro?",
     "opciones": ["A) Español medieval", "B) Español moderno temprano", "C) Español contemporáneo", "D) Castellano primitivo"], "respuesta": "B"},
    
    # Cambios lingüísticos
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué cambio fonético explica la desaparición de la 'f' inicial latina en palabras como *farina* > *harina*?",
     "opciones": ["A) Asimilación", "B) Lenición", "C) Sonorización", "D) Aspiración"], "respuesta": "D"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛(F O V) La sonorización es un cambio en el que un sonido sordo se convierte en sonoro.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "pregunta abierta📜✏️🕵🏛¿Qué fenómeno explica el cambio de *octo* a *ocho* en español?",
     "respuesta": "Diptongación"},
    {"tipo": "opcion_multiple", "pregunta": "¿Qué tipo de cambio lingüístico afecta el significado de las palabras?",
     "opciones": ["A) Fonético", "B) Morfológico", "C) Semántico", "D) Sintáctico"], "respuesta": "C"},
    
    # Expansión del español
    {"tipo": "opcion_multiple", "pregunta": "¿En qué siglo comenzó la expansión del español a América?",
     "opciones": ["A) Siglo XV", "B) Siglo XVI", "C) Siglo XVII", "D) Siglo XVIII"], "respuesta": "B"},
    {"tipo": "verdadero_falso", "🌟📜✏️🕵🏛(F O V) pregunta": "El español se expandió principalmente durante la colonización americana.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "🌟📜✏️🕵🏛 pregunta abierta ¿Qué fenómeno lingüístico describe la influencia de lenguas indígenas en el español de América?",
     "respuesta": "Préstamo lingüístico"},
    {"tipo": "opcion_multiple", "pregunta": "¿Qué lengua indígena influyó más en el español de México?",
     "opciones": ["A) Quechua", "B) Náhuatl", "C) Guaraní", "D) Mapudungun"], "respuesta": "B"},
    
    # Instituciones y normatividad
    {"tipo": "opcion_multiple", "pregunta": "¿Qué institución regula actualmente el uso del español?",
     "opciones": ["A) Real Academia Española", "B) Instituto Cervantes", "C) Academia Mexicana de la Lengua", "D) Academia de Historia"], "respuesta": "A"},
    {"tipo": "verdadero_falso", "pregunta": "🌟📜✏️🕵🏛(F O V) La Real Academia Española fue fundada en el siglo XVIII.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "🌟📜✏️🕵🏛 pregunta abierta ¿Qué obra es considerada el primer intento de normalizar el uso del español?",
     "respuesta": "Gramática de Nebrija"},
    {"tipo": "opcion_multiple", "pregunta": "🌟📜✏️🕵🏛¿Qué país tiene más hablantes nativos de español en el mundo?",
     "opciones": ["A) España", "B) México", "C) Argentina", "D) Colombia"], "respuesta": "B"},
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
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era: {pregunta['respuesta']}")
    print(f"\n¡Completaste el cuestionario! Tu puntaje final es {puntaje}/{len(preguntas[:20])}.")

# Ejecutar el cuestionario
cuestionario()
