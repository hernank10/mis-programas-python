import time
import sys

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

# Función de temporizador
def temporizador_visual(segundos):
    for i in range(segundos, 0, -1):
        sys.stdout.write(f"\rTiempo restante: {i} segundos")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rTiempo agotado.                 \n")

# Función del cuestionario
def cuestionario_con_temporizador(tiempo_limite):
    print("Bienvenido al cuestionario interactivo de gramática castellana.\n")
    puntaje = 0

    for i, pregunta in enumerate(preguntas, start=1):
        print(f"Pregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(opcion)

        print(f"Tienes {tiempo_limite} segundos para responder.")
        
        # Variable para rastrear si se respondió a tiempo
        respondido = False
        respuesta = ""

        # Temporizador integrado con respuesta
        tiempo_inicio = time.time()
        while time.time() - tiempo_inicio < tiempo_limite:
            respuesta = input("Tu respuesta (a/b/c): ").lower()
            if respuesta:
                respondido = True
                break

        if not respondido:
            print("¡Se agotó el tiempo!")
        elif respuesta == pregunta["respuesta"]:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}.\n")
        
        time.sleep(1)  # Pausa breve antes de la siguiente pregunta

    print(f"Has terminado el cuestionario. Tu puntaje final es {puntaje}/{len(preguntas)}.")
    if puntaje == len(preguntas):
        print("¡Excelente trabajo! Has respondido todas las preguntas correctamente.")
    elif puntaje > len(preguntas) / 2:
        print("¡Buen trabajo! Pero puedes mejorar con más práctica.")
    else:
        print("Necesitas practicar más. ¡Sigue intentando!")

# Ejecuta el cuestionario con un tiempo límite por pregunta
tiempo_limite = 10  # Tiempo en segundos para responder cada pregunta
cuestionario_con_temporizador(tiempo_limite)
