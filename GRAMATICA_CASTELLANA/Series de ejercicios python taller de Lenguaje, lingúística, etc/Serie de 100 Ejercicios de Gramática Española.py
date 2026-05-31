# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Gramática Española
# Inspirado en las obras del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los conceptos fundamentales de la gramática,
# incluyendo sintaxis, morfología, ortografía, puntuación y más.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de gramática
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Sustantivos", "Un sustantivo que nombra un ser o un objeto de forma individual es: (a) común, (b) propio, (c) abstracto.", "b"),
        2: ("Verbos", "La parte de la oración que expresa una acción, un estado o un proceso es el: (a) adjetivo, (b) verbo, (c) adverbio.", "b"),
        3: ("Adjetivos", "Un adjetivo calificativo describe una cualidad del sustantivo. (Verdadero/Falso)", "verdadero"),
        4: ("Adverbios", "Un adverbio de modo responde a la pregunta '¿cómo?'. (Verdadero/Falso)", "verdadero"),
        5: ("Preposiciones", "La palabra 'para' es una: (a) preposición, (b) conjunción, (c) interjección.", "a"),
        6: ("Artículos", "Los artículos 'el', 'la', 'los', 'las' son: (a) definidos, (b) indefinidos, (c) neutros.", "a"),
        7: ("Puntuación", "La coma se usa para separar los elementos de una enumeración. (Verdadero/Falso)", "verdadero"),
        8: ("Sujeto", "En la oración 'El perro corrió velozmente', el sujeto es: (a) velozmente, (b) corrió, (c) El perro.", "c"),
        9: ("Predicado", "En la oración 'Mi hermana compró un libro', el predicado es: (a) un libro, (b) Mi hermana, (c) compró un libro.", "c"),
        10: ("Conjugación", "La conjugación verbal es la variación del verbo según persona, número, tiempo y modo. (Verdadero/Falso)", "verdadero"),
        11: ("Tiempos verbales", "El tiempo verbal 'he cantado' está en: (a) pretérito perfecto compuesto, (b) futuro, (c) presente.", "a"),
        12: ("Acentuación", "Las palabras agudas llevan tilde cuando terminan en n, s o vocal. (Verdadero/Falso)", "verdadero"),
        13: ("Acentuación", "La palabra 'árbol' es: (a) aguda, (b) grave, (c) esdrújula.", "b"),
        14: ("Ortografía", "El uso de la 'b' en 'ambulancia' es correcto. (Verdadero/Falso)", "verdadero"),
        15: ("Ortografía", "La palabra 'jirafa' se escribe con 'j'. (Verdadero/Falso)", "verdadero"),
        16: ("Pronombres", "Un pronombre sustituye a un: (a) verbo, (b) sustantivo, (c) adjetivo.", "b"),
        17: ("Complemento directo", "En 'Ella lee un libro', 'un libro' es el: (a) complemento indirecto, (b) complemento circunstancial, (c) complemento directo.", "c"),
        18: ("Complemento indirecto", "En 'Di la carta a mi mamá', 'a mi mamá' es el: (a) complemento directo, (b) complemento indirecto, (c) sujeto.", "b"),
        19: ("Oración simple", "Una oración simple contiene un solo verbo conjugado. (Verdadero/Falso)", "verdadero"),
        20: ("Oración compuesta", "Una oración compuesta tiene dos o más verbos. (Verdadero/Falso)", "verdadero"),
        21: ("Concordancia", "La concordancia se refiere a la relación entre palabras. (Verdadero/Falso)", "verdadero"),
        22: ("Acentuación", "La palabra 'camión' es aguda y lleva tilde. (Verdadero/Falso)", "verdadero"),
        23: ("Puntuación", "El punto y coma separa elementos de una enumeración larga. (Verdadero/Falso)", "verdadero"),
        24: ("Mayúsculas", "Se usa mayúscula al inicio de una oración y en nombres propios. (Verdadero/Falso)", "verdadero"),
        25: ("Sinónimos", "Las palabras con el mismo o similar significado son: (a) sinónimos, (b) antónimos, (c) homónimos.", "a"),
        26: ("Antónimos", "Las palabras con significados opuestos son: (a) sinónimos, (b) antónimos, (c) parónimos.", "b"),
        27: ("Sintaxis", "El 'orden de las palabras' es la estructura sintáctica de la oración. (Verdadero/Falso)", "verdadero"),
        28: ("Adverbios", "La palabra 'lentamente' es un adverbio de: (a) tiempo, (b) lugar, (c) modo.", "c"),
        29: ("Verbos", "El modo indicativo expresa acciones reales y objetivas. (Verdadero/Falso)", "verdadero"),
        30: ("Verbos", "El modo subjuntivo expresa deseos, dudas o posibilidades. (Verdadero/Falso)", "verdadero"),
        31: ("Ortografía", "La palabra 'hielo' se escribe con 'h'. (Verdadero/Falso)", "verdadero"),
        32: ("Puntuación", "Los dos puntos se usan para introducir una cita textual. (Verdadero/Falso)", "verdadero"),
        33: ("Gramática", "La gramática es el estudio de las reglas del lenguaje. (Verdadero/Falso)", "verdadero"),
        34: ("Sustantivos", "Un sustantivo 'colectivo' nombra un conjunto de seres u objetos. (Verdadero/Falso)", "verdadero"),
        35: ("Género", "El género gramatical puede ser masculino o femenino. (Verdadero/Falso)", "verdadero"),
        36: ("Número", "El número gramatical puede ser singular o plural. (Verdadero/Falso)", "verdadero"),
        37: ("Adjetivos", "Un adjetivo 'demostrativo' indica la posición de un sustantivo. (Verdadero/Falso)", "verdadero"),
        38: ("Adjetivos", "Un adjetivo 'posesivo' indica pertenencia. (Verdadero/Falso)", "verdadero"),
        39: ("Pronombres", "La palabra 'ella' es un pronombre personal. (Verdadero/Falso)", "verdadero"),
        40: ("Conjunciones", "La conjunción 'y' es copulativa. (Verdadero/Falso)", "verdadero"),
        41: ("Conjunciones", "La conjunción 'pero' es adversativa. (Verdadero/Falso)", "verdadero"),
        42: ("Interjecciones", "Las interjecciones expresan emociones. (Verdadero/Falso)", "verdadero"),
        43: ("Locuciones", "Una 'locución adverbial' es un grupo de palabras que funciona como un adverbio. (Verdadero/Falso)", "verdadero"),
        44: ("Voz", "La voz activa indica que el sujeto realiza la acción. (Verdadero/Falso)", "verdadero"),
        45: ("Voz", "En 'El libro fue leído por el niño', la voz es: (a) activa, (b) pasiva.", "b"),
        46: ("Verbos", "El infinitivo de un verbo termina en: (a) -ar, -er, -ir, (b) -ado, -ido, (c) -ando, -iendo.", "a"),
        47: ("Verbos", "El gerundio de un verbo termina en: (a) -ar, -er, -ir, (b) -ado, -ido, (c) -ando, -iendo.", "c"),
        48: ("Verbos", "El participio de un verbo termina en: (a) -ar, -er, -ir, (b) -ado, -ido, (c) -ando, -iendo.", "b"),
        49: ("Acentuación", "Las palabras graves llevan tilde si no terminan en n, s o vocal. (Verdadero/Falso)", "verdadero"),
        50: ("Acentuación", "La palabra 'pájaro' es: (a) aguda, (b) grave, (c) esdrújula.", "c"),
        51: ("Ortografía", "La palabra 'vaca' se escribe con 'v'. (Verdadero/Falso)", "verdadero"),
        52: ("Puntuación", "Los signos de interrogación y exclamación se usan para preguntar y exclamar. (Verdadero/Falso)", "verdadero"),
        53: ("Sintaxis", "El 'núcleo del sujeto' es la palabra más importante del sujeto. (Verdadero/Falso)", "verdadero"),
        54: ("Sintaxis", "El 'núcleo del predicado' es siempre un verbo. (Verdadero/Falso)", "verdadero"),
        55: ("Oración", "¿Una oración debe tener sujeto y predicado? (Sí/No)", "no"),
        56: ("Oración", "Las oraciones 'unimembres' no se pueden dividir en sujeto y predicado. (Verdadero/Falso)", "verdadero"),
        57: ("Ortografía", "El uso de la 'h' en 'hacer' es correcto. (Verdadero/Falso)", "verdadero"),
        58: ("Mayúsculas", "Los nombres de los días de la semana se escriben con mayúscula. (Verdadero/Falso)", "falso"),
        59: ("Coma", "Se usa una coma antes de una conjunción adversativa como 'pero'. (Verdadero/Falso)", "verdadero"),
        60: ("Concordancia", "El verbo debe concordar con el sujeto en número y persona. (Verdadero/Falso)", "verdadero"),
        61: ("Ortografía", "La palabra 'gente' se escribe con 'g'. (Verdadero/Falso)", "verdadero"),
        62: ("Sustantivos", "Un sustantivo que nombra un concepto o idea es: (a) concreto, (b) abstracto.", "b"),
        63: ("Adjetivos", "Los adjetivos se clasifican en: (a) calificativos y relacionales, (b) definidos y indefinidos.", "a"),
        64: ("Pronombres", "¿'Quién' es un pronombre interrogativo? (Sí/No)", "sí"),
        65: ("Determinantes", "Los artículos, demostrativos y posesivos son tipos de: (a) verbos, (b) determinantes, (c) adverbios.", "b"),
        66: ("Puntuación", "El punto y seguido separa oraciones dentro de un mismo párrafo. (Verdadero/Falso)", "verdadero"),
        67: ("Tiempos verbales", "El tiempo 'cantaré' está en: (a) presente, (b) pretérito, (c) futuro.", "c"),
        68: ("Puntuación", "El punto final se usa al terminar un escrito. (Verdadero/Falso)", "verdadero"),
        69: ("Acentuación", "Las palabras esdrújulas siempre llevan tilde. (Verdadero/Falso)", "verdadero"),
        70: ("Diptongos", "Un diptongo es la unión de dos vocales en una misma sílaba. (Verdadero/Falso)", "verdadero"),
        71: ("Hiatos", "Un hiato es la separación de dos vocales en sílabas diferentes. (Verdadero/Falso)", "verdadero"),
        72: ("Sintaxis", "Un 'complemento circunstancial' indica las circunstancias de la acción verbal. (Verdadero/Falso)", "verdadero"),
        73: ("Ortografía", "La palabra 'bilingüe' se escribe con 'güe'. (Verdadero/Falso)", "verdadero"),
        74: ("Pronombres", "La palabra 'me' en 'me lo dijo' es un pronombre personal. (Verdadero/Falso)", "verdadero"),
        75: ("Voz", "En 'El chef cocinó la sopa', la voz es: (a) activa, (b) pasiva.", "a"),
        76: ("Tiempos verbales", "El tiempo 'había comido' está en: (a) pretérito pluscuamperfecto, (b) futuro perfecto.", "a"),
        77: ("Modos verbales", "El modo imperativo se usa para dar órdenes o mandatos. (Verdadero/Falso)", "verdadero"),
        78: ("Puntuación", "Los paréntesis se usan para insertar información adicional. (Verdadero/Falso)", "verdadero"),
        79: ("Ortografía", "La palabra 'submarino' se escribe con 'b'. (Verdadero/Falso)", "verdadero"),
        80: ("Clases de palabras", "Las palabras se clasifican en: (a) variables e invariables, (b) cortas y largas.", "a"),
        81: ("Concordancia", "La frase 'las niñas inteligente' tiene un error de concordancia. (Verdadero/Falso)", "verdadero"),
        82: ("Sintaxis", "Una oración 'subordinada' no tiene sentido por sí sola. (Verdadero/Falso)", "verdadero"),
        83: ("Ortografía", "La palabra 'explicación' se escribe con 'x'. (Verdadero/Falso)", "verdadero"),
        84: ("Acentuación", "La palabra 'lápiz' lleva tilde porque es una palabra grave que no termina en n, s o vocal. (Verdadero/Falso)", "verdadero"),
        85: ("Tipos de oraciones", "Una oración 'enunciativa' afirma o niega algo. (Verdadero/Falso)", "verdadero"),
        86: ("Tipos de oraciones", "Una oración 'interrogativa' hace una pregunta. (Verdadero/Falso)", "verdadero"),
        87: ("Tipos de oraciones", "Una oración 'exclamativa' expresa una emoción. (Verdadero/Falso)", "verdadero"),
        88: ("Mayúsculas", "Los nombres de los meses del año se escriben con mayúscula. (Verdadero/Falso)", "falso"),
        89: ("Puntuación", "La 'punto y aparte' se usa para cambiar de tema o subtema. (Verdadero/Falso)", "verdadero"),
        90: ("Ortografía", "La palabra 'ejercicio' se escribe con 'j'. (Verdadero/Falso)", "verdadero"),
        91: ("Diptongos", "¿La palabra 'aire' tiene un diptongo? (Sí/No)", "sí"),
        92: ("Hiatos", "¿La palabra 'poeta' tiene un hiato? (Sí/No)", "sí"),
        93: ("Ortografía", "Las palabras que empiezan con 'geo' se escriben con 'g'. (Verdadero/Falso)", "verdadero"),
        94: ("Ortografía", "La palabra 'vulnerabilidad' se escribe con 'v'. (Verdadero/Falso)", "verdadero"),
        95: ("Gramática", "La 'morfología' estudia la estructura interna de las palabras. (Verdadero/Falso)", "verdadero"),
        96: ("Puntuación", "El punto y coma es más fuerte que la coma pero menos que el punto. (Verdadero/Falso)", "verdadero"),
        97: ("Verbos", "El 'futuro simple' de 'ser' es 'será'. (Verdadero/Falso)", "verdadero"),
        98: ("Sintaxis", "El 'atributo' es un complemento que califica al sujeto a través de un verbo copulativo. (Verdadero/Falso)", "verdadero"),
        99: ("Ortografía", "La palabra 'había' se escribe con 'h' intermedia. (Verdadero/Falso)", "falso"),
        100: ("Gramática", "La 'semántica' estudia el significado de las palabras y oraciones. (Verdadero/Falso)", "verdadero"),
    }

    print("¡Bienvenido al reto de Gramática Española!")
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
