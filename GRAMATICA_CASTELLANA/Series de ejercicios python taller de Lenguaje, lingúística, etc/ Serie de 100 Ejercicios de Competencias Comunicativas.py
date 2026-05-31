# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Competencias Comunicativas
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los distintos tipos de competencias
# necesarias para la comunicación efectiva: lingüística, sociolingüística, pragmática, y textual.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de competencias comunicativas
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Generalidades", "El emisor, receptor, mensaje y canal son elementos del modelo de: (a) la comunicación, (b) el lenguaje, (c) la semántica.", "a"),
        2: ("Lingüística", "La capacidad de usar la gramática y el vocabulario de manera correcta se conoce como competencia: (a) pragmática, (b) lingüística, (c) sociolingüística.", "b"),
        3: ("Pragmática", "El conocimiento de cómo usar el lenguaje en diferentes situaciones sociales se llama competencia: (a) discursiva, (b) estratégica, (c) pragmática.", "c"),
        4: ("Sociolingüística", "Saber adaptar el registro del lenguaje a una situación formal es un ejemplo de competencia: (a) lingüística, (b) sociolingüística, (c) textual.", "b"),
        5: ("Textual", "La capacidad de construir textos coherentes y cohesionados es parte de la competencia: (a) textual, (b) estratégica, (c) pragmática.", "a"),
        6: ("Pragmática", "Un 'acto de habla' es un enunciado con una función específica en la comunicación. (Verdadero/Falso)", "verdadero"),
        7: ("Lingüística", "La fonología estudia los sonidos del lenguaje. (Verdadero/Falso)", "verdadero"),
        8: ("Sociolingüística", "La elección de un dialecto u otro en una conversación es parte de la competencia sociolingüística. (Verdadero/Falso)", "verdadero"),
        9: ("Generalidades", "El contexto es el conjunto de circunstancias en las que se produce la comunicación. (Verdadero/Falso)", "verdadero"),
        10: ("Pragmática", "Una 'implicatura' es lo que el hablante quiere comunicar sin decirlo explícitamente. (Verdadero/Falso)", "verdadero"),
        11: ("Textual", "La 'coherencia' de un texto se refiere a la conexión de ideas en un nivel superficial. (Verdadero/Falso)", "falso"),
        12: ("Lingüística", "La sintaxis se encarga del orden de las palabras en una oración. (Verdadero/Falso)", "verdadero"),
        13: ("Sociolingüística", "La 'variedad estándar' de una lengua es la más usada y formal. (Verdadero/Falso)", "verdadero"),
        14: ("Pragmática", "Un 'acto directivo' busca que el oyente realice una acción. (Verdadero/Falso)", "verdadero"),
        15: ("Textual", "La 'cohesión' es la conexión interna del texto a través de elementos gramaticales y léxicos. (Verdadero/Falso)", "verdadero"),
        16: ("Lingüística", "El significado literal de una palabra es su: (a) connotación, (b) denotación, (c) paráfrasis.", "b"),
        17: ("Sociolingüística", "Un 'argot' es una variedad de la lengua usada por un grupo social. (Verdadero/Falso)", "verdadero"),
        18: ("Pragmática", "El principio de cooperación de Grice se basa en la idea de que los participantes de una conversación son cooperativos. (Verdadero/Falso)", "verdadero"),
        19: ("Textual", "Una 'narración' es un tipo de texto que busca describir personas o lugares. (Verdadero/Falso)", "falso"),
        20: ("Lingüística", "La morfología estudia la estructura interna de las palabras. (Verdadero/Falso)", "verdadero"),
        21: ("Generalidades", "El 'ruido' es cualquier interferencia que distorsiona el mensaje. (Verdadero/Falso)", "verdadero"),
        22: ("Lingüística", "Los fonemas son las unidades mínimas distintivas del lenguaje. (Verdadero/Falso)", "verdadero"),
        23: ("Pragmática", "Los 'deícticos' son palabras que señalan a personas, lugares o momentos específicos. (Verdadero/Falso)", "verdadero"),
        24: ("Sociolingüística", "El conocimiento de los 'tabúes' lingüísticos es parte de la competencia sociolingüística. (Verdadero/Falso)", "verdadero"),
        25: ("Textual", "La 'exposición' es un tipo de texto que busca convencer al lector. (Verdadero/Falso)", "falso"),
        26: ("Generalidades", "El 'feedback' es la respuesta del receptor al mensaje del emisor. (Verdadero/Falso)", "verdadero"),
        27: ("Lingüística", "El 'léxico' es el conjunto de palabras de una lengua. (Verdadero/Falso)", "verdadero"),
        28: ("Pragmática", "Un 'acto declarativo' tiene el poder de cambiar la realidad. (Verdadero/Falso)", "verdadero"),
        29: ("Sociolingüística", "Un 'sociolecto' es una variedad de la lengua de un grupo social. (Verdadero/Falso)", "verdadero"),
        30: ("Textual", "La 'argumentación' es un tipo de texto que presenta una opinión con pruebas. (Verdadero/Falso)", "verdadero"),
        31: ("Lingüística", "La 'polisemia' ocurre cuando una palabra tiene un solo significado. (Verdadero/Falso)", "falso"),
        32: ("Pragmática", "Las 'máximas de Grice' son reglas que rigen la conversación. (Verdadero/Falso)", "verdadero"),
        33: ("Sociolingüística", "Un 'idiolecto' es la forma de hablar de una persona individual. (Verdadero/Falso)", "verdadero"),
        34: ("Textual", "La 'descripción' se enfoca en presentar las características de algo. (Verdadero/Falso)", "verdadero"),
        35: ("Generalidades", "¿El 'canal' de comunicación es el medio físico por el que viaja el mensaje? (Sí/No)", "sí"),
        36: ("Lingüística", "La 'hiponimia' es una relación de inclusión de significado. (Verdadero/Falso)", "verdadero"),
        37: ("Pragmática", "La 'cortesía' es una estrategia para evitar conflictos en la comunicación. (Verdadero/Falso)", "verdadero"),
        38: ("Sociolingüística", "La 'diglosia' es una situación en la que dos dialectos coexisten sin jerarquía. (Verdadero/Falso)", "falso"),
        39: ("Textual", "El 'estilo' de un texto depende de la elección de palabras y estructuras. (Verdadero/Falso)", "verdadero"),
        40: ("Lingüística", "La 'sintaxis' es el estudio del sonido de las palabras. (Verdadero/Falso)", "falso"),
        41: ("Pragmática", "Un 'acto comisivo' compromete al hablante a realizar una acción futura. (Verdadero/Falso)", "verdadero"),
        42: ("Sociolingüística", "El conocimiento de los 'registros' (formal, informal) es parte de la competencia sociolingüística. (Verdadero/Falso)", "verdadero"),
        43: ("Textual", "Un texto es 'coherente' si sus partes están lógicamente conectadas. (Verdadero/Falso)", "verdadero"),
        44: ("Lingüística", "La 'semántica' estudia el significado de las palabras y oraciones. (Verdadero/Falso)", "verdadero"),
        45: ("Pragmática", "El 'contexto social' de una conversación es irrelevante para la pragmática. (Verdadero/Falso)", "falso"),
        46: ("Sociolingüística", "La 'jerga' es un tipo de argot. (Verdadero/Falso)", "verdadero"),
        47: ("Textual", "La 'introducción' de un texto presenta el tema y la tesis. (Verdadero/Falso)", "verdadero"),
        48: ("Generalidades", "El 'código' es un sistema de signos y reglas. (Verdadero/Falso)", "verdadero"),
        49: ("Lingüística", "Un 'morfema' es la unidad mínima con significado. (Verdadero/Falso)", "verdadero"),
        50: ("Pragmática", "Una 'disputa' es un ejemplo de un acto de habla asertivo. (Verdadero/Falso)", "falso"),
        51: ("Sociolingüística", "El 'bilingüismo' es la capacidad de una persona de hablar dos lenguas. (Verdadero/Falso)", "verdadero"),
        52: ("Textual", "La 'estructura' de un texto narrativo incluye el inicio, nudo y desenlace. (Verdadero/Falso)", "verdadero"),
        53: ("Generalidades", "La comunicación es un proceso de intercambio de información. (Verdadero/Falso)", "verdadero"),
        54: ("Lingüística", "La 'homonimia' es la relación entre dos palabras con significados diferentes pero igual forma. (Verdadero/Falso)", "verdadero"),
        55: ("Pragmática", "¿Los 'indicadores deícticos' son palabras que apuntan a la situación comunicativa? (Sí/No)", "sí"),
        56: ("Sociolingüística", "El conocimiento de las normas de 'cortesía' es parte de la competencia sociolingüística. (Verdadero/Falso)", "verdadero"),
        57: ("Textual", "Un texto 'instructivo' busca dar instrucciones. (Verdadero/Falso)", "verdadero"),
        58: ("Lingüística", "¿La 'ortografía' es parte de la competencia fonológica? (Sí/No)", "no"),
        59: ("Pragmática", "¿Un acto 'expresivo' expresa un estado psicológico del hablante? (Sí/No)", "sí"),
        60: ("Sociolingüística", "El 'dialecto' es una variedad de la lengua de un grupo geográfico. (Verdadero/Falso)", "verdadero"),
        61: ("Textual", "La 'descripción' se utiliza a menudo en la literatura. (Verdadero/Falso)", "verdadero"),
        62: ("Generalidades", "La 'competencia comunicativa' incluye más que la simple competencia lingüística. (Verdadero/Falso)", "verdadero"),
        63: ("Lingüística", "El 'campo semántico' es un conjunto de palabras relacionadas por su significado. (Verdadero/Falso)", "verdadero"),
        64: ("Pragmática", "¿La 'ironía' es un tipo de implicatura conversacional? (Sí/No)", "sí"),
        65: ("Sociolingüística", "La 'estratificación social' no afecta el uso del lenguaje. (Verdadero/Falso)", "falso"),
        66: ("Textual", "El 'resumen' es un tipo de texto argumentativo. (Verdadero/Falso)", "falso"),
        67: ("Lingüística", "La 'antonimia' es la relación entre palabras con significados opuestos. (Verdadero/Falso)", "verdadero"),
        68: ("Pragmática", "¿El 'contexto' es esencial para entender un acto de habla? (Sí/No)", "sí"),
        69: ("Sociolingüística", "El 'prestigio' de una variante lingüística es subjetivo. (Verdadero/Falso)", "verdadero"),
        70: ("Textual", "La 'narración' relata una secuencia de eventos. (Verdadero/Falso)", "verdadero"),
        71: ("Lingüística", "Un 'sintagma' es una unidad gramatical que se forma alrededor de un núcleo. (Verdadero/Falso)", "verdadero"),
        72: ("Pragmática", "La 'competencia pragmática' incluye saber cuándo y cómo interrumpir en una conversación. (Verdadero/Falso)", "verdadero"),
        73: ("Sociolingüística", "Un 'cambio de código' es el uso de dos o más lenguas en la misma conversación. (Verdadero/Falso)", "verdadero"),
        74: ("Textual", "La 'tesis' de un texto argumentativo es la idea principal que se defiende. (Verdadero/Falso)", "verdadero"),
        75: ("Lingüística", "La 'paráfrasis' es una expresión con significado diferente. (Verdadero/Falso)", "falso"),
        76: ("Pragmática", "El 'silencio' no tiene significado en la comunicación. (Verdadero/Falso)", "falso"),
        77: ("Sociolingüística", "La 'situación comunicativa' influye en la elección del registro. (Verdadero/Falso)", "verdadero"),
        78: ("Textual", "La 'estructura' de un texto informativo debe ser clara y ordenada. (Verdadero/Falso)", "verdadero"),
        79: ("Lingüística", "El 'género' de un sustantivo es parte de la competencia gramatical. (Verdadero/Falso)", "verdadero"),
        80: ("Pragmática", "Los 'turnos de habla' son una parte fundamental de la comunicación. (Verdadero/Falso)", "verdadero"),
        81: ("Sociolingüística", "El 'estilo' de una persona es un rasgo sociolingüístico. (Verdadero/Falso)", "verdadero"),
        82: ("Textual", "La 'argumentación' busca dar información objetiva. (Verdadero/Falso)", "falso"),
        83: ("Generalidades", "¿La 'intención comunicativa' es el propósito que tiene el emisor al enviar un mensaje? (Sí/No)", "sí"),
        84: ("Lingüística", "La 'conjugación verbal' es parte de la competencia sintáctica. (Verdadero/Falso)", "verdadero"),
        85: ("Pragmática", "Los 'principios de cortesía' regulan la distancia social entre hablantes. (Verdadero/Falso)", "verdadero"),
        86: ("Sociolingüística", "El 'edad' es un factor que influye en el uso del lenguaje. (Verdadero/Falso)", "verdadero"),
        87: ("Textual", "La 'conclusión' de un texto narrativo resume el conflicto principal. (Verdadero/Falso)", "verdadero"),
        88: ("Lingüística", "El 'signo lingüístico' está compuesto por un significante y un significado. (Verdadero/Falso)", "verdadero"),
        89: ("Pragmática", "Los 'actos ilocutivos' tienen una fuerza comunicativa. (Verdadero/Falso)", "verdadero"),
        90: ("Sociolingüística", "La 'clase social' no afecta el uso del lenguaje. (Verdadero/Falso)", "falso"),
        91: ("Textual", "La 'tipología textual' clasifica los textos según su función. (Verdadero/Falso)", "verdadero"),
        92: ("Lingüística", "¿La 'ambigüedad' es un rasgo de la competencia fonológica? (Sí/No)", "no"),
        93: ("Pragmática", "La 'felicidad' de un acto de habla se refiere a si es apropiado para el contexto. (Verdadero/Falso)", "verdadero"),
        94: ("Sociolingüística", "El 'género' (masculino/femenino) del hablante no influye en el uso del lenguaje. (Verdadero/Falso)", "falso"),
        95: ("Textual", "Un texto 'dialógico' se presenta en forma de conversación. (Verdadero/Falso)", "verdadero"),
        96: ("Generalidades", "La 'comunicación no verbal' es un aspecto de la competencia comunicativa. (Verdadero/Falso)", "verdadero"),
        97: ("Lingüística", "La 'diacronía' estudia el cambio del lenguaje a lo largo del tiempo. (Verdadero/Falso)", "verdadero"),
        98: ("Pragmática", "La 'ironía' siempre es obvia para el oyente. (Verdadero/Falso)", "falso"),
        99: ("Sociolingüística", "Un 'estilista' del lenguaje es un escritor de alta calidad. (Verdadero/Falso)", "falso"),
        100: ("Generalidades", "La 'competencia comunicativa' es la habilidad para comunicarse de manera efectiva. (Verdadero/Falso)", "verdadero"),
    }

    print("¡Bienvenido al reto de Competencias Comunicativas!")
    print("-------------------------------------------------------------")
    print("Responde las preguntas o introduce 'salir' para terminar.")

    while True:
        try:
            exercise_number = random.choice(list(exercises.keys()))
            title, task, correct_answer = exercises[exercise_number]

            print(f"\n[Ejercicio {exercise_number}: {title}]")
            print(task)

            user_response = input("Tu respuesta: ").strip()

            if user_response.lower() == 'salir':
                print("¡Gracias por participar! ¡Hasta la próxima!")
                break
            
            clean_user_response = user_response.lower().replace(" ", "")
            clean_correct_answer = correct_answer.lower().replace(" ", "")
            
            if clean_user_response == clean_correct_answer:
                print("¡Correcto! ¡Qué bien!")
            else:
                print(f"Incorrecto. La respuesta esperada era: '{correct_answer}'")

            continue_prompt = input("\n¿Quieres otro ejercicio? (s/n): ").lower()
            if continue_prompt != 's':
                print("¡Hasta pronto!")
                break

        except (KeyboardInterrupt, EOFError):
            print("\n¡Gracias por participar! ¡Adiós!")
            break

if __name__ == "__main__":
    main()
