import random

# Preguntas y respuestas
preguntas = [
    # Historia de Colombia
    {"tipo": "opcion", "pregunta": "🌟📜✏️🕵¿En qué año se firmó la independencia de Colombia?", 
     "opciones": ["A) 1810", "B) 1819", "C) 1821", "D) 1830"], "respuesta": "B"},
    {"tipo": "vf", "pregunta": "🌟📜✏️🕵(F O V)La Batalla de Boyacá ocurrió el 7 de agosto de 1819.", "respuesta": "V"},
    {"tipo": "abierta", "pregunta": "🌟📜✏️🕵¿Quién fue el libertador de Colombia?", "respuesta": "Simón Bolívar"},
    {"tipo": "opcion", "pregunta": "🌟📜✏️🕵¿Cómo se llamó la unión de Colombia, Venezuela, Ecuador y Panamá en el siglo XIX?", 
     "opciones": ["A) Confederación Andina", "B) Gran Colombia", "C) Virreinato de la Nueva Granada", "D) República de Bolívar"], "respuesta": "B"},
    # Lengua Castellana
    {"tipo": "opcion", "pregunta": "🌟📜✏️🕵¿Qué es un diptongo?", 
     "opciones": ["A) La unión de dos vocales abiertas", "B) La unión de una vocal abierta y una cerrada", 
                  "C) La separación de dos vocales en distintas sílabas", "D) Ninguna de las anteriores"], "respuesta": "B"},
    {"tipo": "vf", "pregunta": "🌟📜✏️🕵(F O V)La palabra 'mariposa' tiene un hiato.", "respuesta": "F"},
    {"tipo": "abierta", "pregunta": "¿Cómo se llama la figura literaria que consiste en comparar dos cosas usando 'como'?", 
     "respuesta": "Símil"},
    {"tipo": "opcion", "pregunta": "🌟📜✏️🕵¿Qué tipo de oración es: 'Quiero que vengas a la reunión'?", 
     "opciones": ["A) Simple", "B) Compuesta coordinada", "C) Compuesta subordinada", "D) Yuxtapuesta"], "respuesta": "C"},
    # Más preguntas (puedes agregar hasta completar las 50)
]

# Función para mostrar preguntas
def mostrar_pregunta(pregunta):
    print("\n" + pregunta["pregunta"])
    if pregunta["tipo"] == "opcion":
        for opcion in pregunta["opciones"]:
            print(opcion)
    respuesta = input("Tu respuesta: ").strip()
    return respuesta

# Validar respuestas
def validar_respuesta(pregunta, respuesta):
    if pregunta["tipo"] == "abierta":
        return respuesta.lower() == pregunta["respuesta"].lower()
    return respuesta.upper() == pregunta["respuesta"].upper()

# Juego principal
def cuestionario():
    puntaje = 0
    random.shuffle(preguntas)  # Barajar preguntas
    for i, pregunta in enumerate(preguntas[:50]):  # Limitar a 50 preguntas
        print(f"\nPregunta {i + 1}:")
        respuesta = mostrar_pregunta(pregunta)
        if validar_respuesta(pregunta, respuesta):
            print("🌟📜✏️🕵¡Correcto!✅")
            puntaje += 1
        else:
            print(f"Incorrecto❌. La respuesta correcta era: {pregunta['respuesta']}")
    print(f"\n🌟📜✏️🕵¡Has terminado el cuestionario! Tu puntaje final es {puntaje}/{len(preguntas[:50])}.")

# Ejecutar el cuestionario
cuestionario()
