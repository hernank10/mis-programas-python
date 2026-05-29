import time

# Lista de preguntas y respuestas
preguntas = [
    {"pregunta": "¿Cuál es el uso correcto del punto y coma en oraciones adversativas?", 
     "opciones": ["a) Para separar elementos de una lista compleja", 
                  "b) Para relacionar ideas que se contraponen", 
                  "c) Para indicar el final de un párrafo"],
     "respuesta": "b"},
    
    {"pregunta": "¿Qué es una oración compuesta coordinada?", 
     "opciones": ["a) Una oración con un solo verbo", 
                  "b) Una oración que une ideas independientes con nexos", 
                  "c) Una oración con un verbo en subjuntivo"],
     "respuesta": "b"},
    
    {"pregunta": "¿Qué palabra es un ejemplo de diptongo?", 
     "opciones": ["a) País", 
                  "b) Hueso", 
                  "c) Río"],
     "respuesta": "b"}
    # Agrega más preguntas aquí
]

def cuestionario():
    print("Bienvenido al cuestionario interactivo de gramática castellana.\n")
    puntaje = 0

    for i, pregunta in enumerate(preguntas, start=1):
        print(f"Pregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(opcion)
        
        respuesta = input("Tu respuesta (a/b/c): ").lower()
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}.\n")
        time.sleep(1)  # Pausa breve para mejorar la experiencia

    print(f"Has terminado el cuestionario. Tu puntaje final es {puntaje}/{len(preguntas)}.")
    if puntaje == len(preguntas):
        print("¡Excelente trabajo! Has respondido todas las preguntas correctamente.")
    elif puntaje > len(preguntas) / 2:
        print("¡Buen trabajo! Pero puedes mejorar con más práctica.")
    else:
        print("Necesitas practicar más. ¡Sigue intentando!")

# Ejecuta el cuestionario
cuestionario()
