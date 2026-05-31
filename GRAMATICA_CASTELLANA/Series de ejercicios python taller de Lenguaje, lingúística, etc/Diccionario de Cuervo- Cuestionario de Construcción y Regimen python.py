import random
import sys

def obtener_ejercicios():
    """
    Función que devuelve la lista de ejercicios.
    Cada ejercicio es un diccionario con la pregunta, las opciones,
    la respuesta correcta y una breve explicación.
    Puedes expandir esta lista a 100 o más ejercicios.
    """
    return [
        {
            "pregunta": "¿Qué preposición es la correcta en la oración 'Estoy seguro ... mi decisión'?",
            "opciones": ["a) de", "b) en", "c) sobre", "d) con"],
            "respuesta": "a",
            "explicacion": "El verbo 'estar seguro' rige la preposición 'de'.",
        },
        {
            "pregunta": "¿Cuál es la forma correcta del participio de 'proveer'?",
            "opciones": ["a) proveído", "b) provisto", "c) proveyido", "d) proveído o provisto"],
            "respuesta": "d",
            "explicacion": "El verbo 'proveer' tiene dos participios correctos: 'proveído' (regular) y 'provisto' (irregular).",
        },
        {
            "pregunta": "¿Cuál de estas oraciones utiliza la preposición de forma incorrecta?",
            "opciones": [
                "a) El libro se lo di a Juan.",
                "b) La casa está a cinco kilómetros de la ciudad.",
                "c) No me he percatado de su presencia.",
                "d) La taza se rompió por accidente."
            ],
            "respuesta": "c",
            "explicacion": "La preposición correcta para 'percatarse' es 'de', por lo tanto, la oración es correcta. La opción 'd' es la incorrecta ya que el verbo romper no necesita preposición 'por'. El resto es correcto.",
        },
        {
            "pregunta": "En la frase 'El camino es difícil ... transitar', ¿qué preposición debe usarse?",
            "opciones": ["a) de", "b) a", "c) para", "d) sin"],
            "respuesta": "d",
            "explicacion": "La expresión correcta es 'difícil de transitar'.",
        },
        {
            "pregunta": "¿Es correcto decir 'caber el examen'?",
            "opciones": ["a) Sí, es sinónimo de aprobar.", "b) No, el verbo 'caber' no se usa con ese significado.", "c) Sí, pero solo en contextos informales."],
            "respuesta": "b",
            "explicacion": "El verbo 'caber' significa 'entrar en un lugar' o 'ser posible, lícito', no se utiliza con el significado de 'aprobar' o 'superar'.",
        },
        {
            "pregunta": "¿Cuál es el plural de 'sándwich'?",
            "opciones": ["a) sándwichs", "b) sándwiches", "c) sándwiches o sándwichs", "d) sanduichs"],
            "respuesta": "b",
            "explicacion": "El plural de 'sándwich' es 'sándwiches', siguiendo la regla de añadir '-es' a las palabras que terminan en '-ch'.",
        },
        {
            "pregunta": "En la frase 'Se ha acordado ... ir de viaje', ¿qué preposición es la correcta?",
            "opciones": ["a) en", "b) de", "c) con", "d) para"],
            "respuesta": "b",
            "explicacion": "El verbo 'acordarse' rige la preposición 'de'. 'Acordar' (sin pronombre 'se') se usa con el significado de 'determinar de común acuerdo'.",
        },
        {
            "pregunta": "¿Es correcto decir 'la calor'?",
            "opciones": ["a) Sí, es un arcaísmo válido.", "b) No, la forma correcta es 'el calor'.", "c) Sí, en algunas regiones."],
            "respuesta": "b",
            "explicacion": "La palabra 'calor' es de género masculino, por lo que la forma correcta es 'el calor'.",
        },
        {
            "pregunta": "¿Cuál es la forma correcta del plural de 'tabú'?",
            "opciones": ["a) tabús", "b) tabúes", "c) tabús o tabúes", "d) tabues"],
            "respuesta": "c",
            "explicacion": "El sustantivo 'tabú' admite los dos plurales, 'tabús' y 'tabúes', siendo más frecuente el primero.",
        },
        {
            "pregunta": "La expresión 'a grosso modo' es correcta?",
            "opciones": ["a) Sí", "b) No, la forma correcta es 'grosso modo'.", "c) No, la forma correcta es 'a grosso modo'.", "d) Ambas son correctas."],
            "respuesta": "b",
            "explicacion": "La expresión correcta es 'grosso modo' (sin la preposición 'a'), que significa 'a grandes rasgos' o 'aproximadamente'.",
        },
        # Más ejercicios para completar hasta 100.
        # Puedes copiar y pegar este bloque para añadir más preguntas.
        # Asegúrate de que las preguntas, opciones y respuestas sean coherentes.
    ]

def ejecutar_cuestionario(ejercicios):
    """
    Ejecuta un cuestionario con una selección aleatoria de 10 ejercicios.
    """
    score = 0
    num_preguntas_a_mostrar = 10 if len(ejercicios) >= 10 else len(ejercicios)
    
    # Selecciona preguntas aleatorias sin repetición
    ejercicios_seleccionados = random.sample(ejercicios, num_preguntas_a_mostrar)
    
    print("--- Diccionario de Cuervo: Cuestionario de Construcción y Regimen ---")
    print("Responde las siguientes preguntas. Escribe la letra de la opción correcta.")
    print("---------------------------------------------------------------------")

    for i, ejercicio in enumerate(ejercicios_seleccionados):
        print(f"\nEjercicio {i + 1} de {num_preguntas_a_mostrar}:")
        print(ejercicio["pregunta"])
        for opcion in ejercicio["opciones"]:
            print(f"    {opcion}")

        respuesta_usuario = input("Tu respuesta: ").strip().lower()

        if respuesta_usuario == ejercicio["respuesta"]:
            print("¡Respuesta correcta!")
            score += 1
        else:
            print("Respuesta incorrecta.")
            print(f"La respuesta correcta es '{ejercicio['respuesta']}'.")
            
        print(f"Explicación: {ejercicio['explicacion']}")
        
    print("\n--- Resultados ---")
    print(f"Has obtenido {score} de {num_preguntas_a_mostrar} puntos.")
    print("¡Gracias por participar!")

def main():
    """
    Función principal del programa.
    """
    ejercicios = obtener_ejercicios()

    if not ejercicios:
        print("No hay ejercicios disponibles para ejecutar. Por favor, añade ejercicios a la lista.")
        sys.exit()

    while True:
        try:
            ejecutar_cuestionario(ejercicios)
        except (ValueError, IndexError):
            print("\nError al ejecutar el cuestionario. Asegúrate de que los ejercicios estén bien definidos.")
            sys.exit()

        jugar_de_nuevo = input("\n¿Quieres intentar de nuevo? (s/n): ").strip().lower()
        if jugar_de_nuevo != 's':
            print("¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
