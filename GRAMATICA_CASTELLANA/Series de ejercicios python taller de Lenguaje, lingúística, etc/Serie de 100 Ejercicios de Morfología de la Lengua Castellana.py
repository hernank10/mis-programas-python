# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Morfología de la Lengua Castellana
# Inspirado en las obras del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los conceptos fundamentales de la morfología,
# incluyendo la estructura de las palabras, los morfemas, la formación de palabras y la flexión.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de morfología
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Conceptos básicos", "La parte de una palabra que contiene el significado principal es el: (a) morfema, (b) lexema, (c) prefijo.", "b"),
        2: ("Conceptos básicos", "La unidad mínima con significado gramatical es el: (a) lexema, (b) sufijo, (c) morfema.", "c"),
        3: ("Morfemas", "Los morfemas que no cambian el significado de la palabra, sino que indican género, número, persona, etc., son: (a) derivativos, (b) flexivos, (c) léxicos.", "b"),
        4: ("Morfemas", "Los morfemas que se añaden al lexema para crear nuevas palabras son: (a) derivativos, (b) flexivos, (c) de género.", "a"),
        5: ("Prefijos", "¿La palabra 'imposible' contiene un prefijo? (Sí/No)", "sí"),
        6: ("Sufijos", "¿La palabra 'librero' contiene un sufijo? (Sí/No)", "sí"),
        7: ("Derivación", "El proceso de formación de palabras con prefijos y sufijos se llama: (a) composición, (b) derivación, (c) parasíntesis.", "b"),
        8: ("Composición", "La palabra 'telaraña' se forma por: (a) derivación, (b) composición, (c) parasíntesis.", "b"),
        9: ("Parasíntesis", "La palabra 'enriquecer' se forma con prefijo, sufijo y lexema. Este proceso es: (a) derivación, (b) composición, (c) parasíntesis.", "c"),
        10: ("Familia de palabras", "¿'Panadero', 'panecillo' y 'panadería' pertenecen a la misma familia de palabras? (Sí/No)", "sí"),
        11: ("Prefijos", "El prefijo 'bi-' en 'bicicleta' significa: (a) uno, (b) dos, (c) tres.", "b"),
        12: ("Prefijos", "El prefijo 're-' en 're-hacer' significa: (a) negación, (b) repetición, (c) intensidad.", "b"),
        13: ("Prefijos", "El prefijo 'in-' en 'invisible' significa: (a) negación, (b) dentro, (c) repetición.", "a"),
        14: ("Prefijos", "La palabra 'submarino' lleva el prefijo: (a) super-, (b) sub-, (c) sobre-.", "b"),
        15: ("Prefijos", "El prefijo 'anti-' en 'antivirus' indica: (a) antes, (b) contra, (c) después.", "b"),
        16: ("Prefijos", "¿La palabra 'extraordinario' lleva un prefijo? (Sí/No)", "sí"),
        17: ("Prefijos", "El prefijo 'pre-' en 'prever' significa: (a) antes, (b) después, (c) mucho.", "a"),
        18: ("Prefijos", "El prefijo 'ex-' en 'exalumno' indica: (a) dentro, (b) fuera, (c) antiguo.", "c"),
        19: ("Prefijos", "El prefijo 'tele-' en 'teléfono' se refiere a la: (a) distancia, (b) cercanía, (c) visión.", "a"),
        20: ("Prefijos", "El prefijo 'co-' en 'colaborar' significa: (a) solo, (b) con, (c) sin.", "b"),
        21: ("Sufijos", "El sufijo '-ero' en 'zapatero' indica: (a) lugar, (b) oficio, (c) cualidad.", "b"),
        22: ("Sufijos", "El sufijo '-dad' en 'bondad' forma un: (a) adjetivo, (b) adverbio, (c) sustantivo abstracto.", "c"),
        23: ("Sufijos", "El sufijo '-mente' en 'rápidamente' forma un: (a) adjetivo, (b) adverbio, (c) verbo.", "b"),
        24: ("Sufijos", "El sufijo '-ción' en 'acción' forma un: (a) sustantivo, (b) adjetivo, (c) verbo.", "a"),
        25: ("Sufijos", "El sufijo '-ble' en 'amable' indica: (a) posibilidad, (b) acción, (c) lugar.", "a"),
        26: ("Sufijos", "El sufijo '-ito' en 'perrito' indica: (a) aumento, (b) diminutivo, (c) desprecio.", "b"),
        27: ("Sufijos", "El sufijo '-azo' en 'golpazo' indica: (a) diminutivo, (b) aumento, (c) lugar.", "b"),
        28: ("Sufijos", "El sufijo '-al' en 'cultural' forma un: (a) sustantivo, (b) adjetivo, (c) adverbio.", "b"),
        29: ("Sufijos", "El sufijo '-ista' en 'dentista' indica: (a) oficio, (b) cualidad, (c) acción.", "a"),
        30: ("Sufijos", "El sufijo '-ificar' en 'clarificar' forma un: (a) sustantivo, (b) adjetivo, (c) verbo.", "c"),
        31: ("Composición", "La palabra 'abrebotellas' se forma por composición. (Verdadero/Falso)", "verdadero"),
        32: ("Composición", "La palabra 'guardacostas' se forma a partir de: (a) dos sustantivos, (b) un verbo y un sustantivo, (c) un adjetivo y un sustantivo.", "b"),
        33: ("Composición", "¿'Bocacalle' es una palabra compuesta? (Sí/No)", "sí"),
        34: ("Composición", "La palabra 'malhumor' se forma por la unión de dos: (a) verbos, (b) adverbios, (c) palabras ya existentes.", "c"),
        35: ("Composición", "Una palabra 'yuxtapuesta' es aquella que se forma sin que las palabras sufran cambios. (Verdadero/Falso)", "verdadero"),
        36: ("Composición", "La palabra 'agridulce' se forma por composición. (Verdadero/Falso)", "verdadero"),
        37: ("Composición", "¿'Limpiaparabrisas' es una palabra compuesta? (Sí/No)", "sí"),
        38: ("Composición", "La palabra 'baloncesto' se forma por composición. (Verdadero/Falso)", "verdadero"),
        39: ("Composición", "La palabra 'bienvenida' se forma por composición. (Verdadero/Falso)", "verdadero"),
        40: ("Composición", "La palabra 'sacapuntas' se forma a partir de un verbo y un sustantivo. (Verdadero/Falso)", "verdadero"),
        41: ("Derivación", "La palabra 'florero' se deriva de 'flor'. (Verdadero/Falso)", "verdadero"),
        42: ("Derivación", "La palabra 'subterráneo' se forma por derivación. (Verdadero/Falso)", "verdadero"),
        43: ("Parasíntesis", "¿La palabra 'encarcelar' es parasintética? (Sí/No)", "sí"),
        44: ("Parasíntesis", "La parasíntesis es la combinación de composición y derivación. (Verdadero/Falso)", "verdadero"),
        45: ("Derivación", "La palabra 'dulzura' se forma por derivación. (Verdadero/Falso)", "verdadero"),
        46: ("Derivación", "La palabra 'prejuicio' se forma por derivación. (Verdadero/Falso)", "verdadero"),
        47: ("Parasíntesis", "La palabra 'aterrizar' es un ejemplo de parasíntesis. (Verdadero/Falso)", "verdadero"),
        48: ("Derivación", "La palabra 'limpieza' se forma por derivación. (Verdadero/Falso)", "verdadero"),
        49: ("Derivación", "La palabra 'deshacer' se forma por derivación. (Verdadero/Falso)", "verdadero"),
        50: ("Derivación", "La palabra 'cacería' se forma por derivación. (Verdadero/Falso)", "verdadero"),
        51: ("Flexión", "El morfema flexivo de género en 'gatas' es: (a) -as, (b) -s, (c) -a.", "c"),
        52: ("Flexión", "El morfema flexivo de número en 'perros' es: (a) -o, (b) -s, (c) -os.", "b"),
        53: ("Flexión", "¿La palabra 'niño' tiene un morfema flexivo de género? (Sí/No)", "sí"),
        54: ("Flexión", "La palabra 'árbol' tiene un morfema flexivo de género. (Verdadero/Falso)", "falso"),
        55: ("Flexión", "El morfema flexivo de número en 'libros' es: (a) -o, (b) -s, (c) -os.", "b"),
        56: ("Flexión", "Los sustantivos y adjetivos tienen morfemas flexivos de género y número. (Verdadero/Falso)", "verdadero"),
        57: ("Flexión", "El morfema flexivo de género en 'jefa' es: (a) -a, (b) -f, (c) -as.", "a"),
        58: ("Flexión", "La palabra 'mesas' tiene morfema de número y género. (Verdadero/Falso)", "verdadero"),
        59: ("Flexión", "¿El plural de 'cruz' es 'cruces'? (Sí/No)", "sí"),
        60: ("Flexión", "¿El plural de 'ley' es 'leyes'? (Sí/No)", "sí"),
        61: ("Flexión Verbal", "La persona verbal 'yo' es la primera persona del singular. (Verdadero/Falso)", "verdadero"),
        62: ("Flexión Verbal", "El morfema de persona y número en 'cantaste' es: (a) -aste, (b) -aste, (c) -aste.", "a"),
        63: ("Flexión Verbal", "El morfema de tiempo en 'comimos' es: (a) -imos, (b) -mimos, (c) -mos.", "a"),
        64: ("Flexión Verbal", "El morfema de modo en 'cantaré' es del modo: (a) indicativo, (b) subjuntivo, (c) imperativo.", "a"),
        65: ("Flexión Verbal", "La palabra 'canten' está en modo: (a) indicativo, (b) subjuntivo, (c) imperativo.", "b"),
        66: ("Flexión Verbal", "El morfema que indica el tiempo verbal se llama 'morfema de: (a) número, (b) modo, (c) tiempo'.", "c"),
        67: ("Flexión Verbal", "El morfema que indica el modo verbal se llama 'morfema de: (a) número, (b) modo, (c) tiempo'.", "b"),
        68: ("Flexión Verbal", "El morfema que indica la persona verbal se llama 'morfema de: (a) persona, (b) modo, (c) tiempo'.", "a"),
        69: ("Flexión Verbal", "El verbo 'habíamos comido' es una forma verbal compuesta. (Verdadero/Falso)", "verdadero"),
        70: ("Flexión Verbal", "¿El verbo 'estudiando' tiene morfemas flexivos de persona y número? (Sí/No)", "no"),
        71: ("Clases de palabras", "Los sustantivos, adjetivos y verbos son palabras: (a) invariables, (b) variables.", "b"),
        72: ("Clases de palabras", "Las preposiciones y conjunciones son palabras: (a) invariables, (b) variables.", "a"),
        73: ("Morfología", "El 'alargamiento' de una palabra se debe a la adición de: (a) lexemas, (b) morfemas, (c) sintagmas.", "b"),
        74: ("Morfemas", "El morfema 'nominal' en sustantivos indica: (a) acción, (b) género y número, (c) cualidad.", "b"),
        75: ("Morfemas", "El morfema 'verbal' en verbos indica: (a) género y número, (b) tiempo y modo, (c) persona, número, tiempo y modo.", "c"),
        76: ("Lexemas", "¿El lexema de 'niñitas' es 'niñ'? (Sí/No)", "sí"),
        77: ("Lexemas", "¿El lexema de 'casas' es 'cas'? (Sí/No)", "sí"),
        78: ("Morfología", "La morfología 'flexiva' estudia las variaciones de una palabra sin cambiar su categoría gramatical. (Verdadero/Falso)", "verdadero"),
        79: ("Morfología", "La morfología 'derivativa' estudia la formación de nuevas palabras. (Verdadero/Falso)", "verdadero"),
        80: ("Afixos", "Los afijos son elementos que se añaden al lexema. (Verdadero/Falso)", "verdadero"),
        81: ("Afixos", "Los afijos que van antes del lexema son: (a) sufijos, (b) prefijos, (c) infijos.", "b"),
        82: ("Afixos", "Los afijos que van después del lexema son: (a) sufijos, (b) prefijos, (c) infijos.", "a"),
        83: ("Afixos", "Los afijos que se insertan dentro del lexema son: (a) sufijos, (b) prefijos, (c) infijos.", "c"),
        84: ("Infijos", "La palabra 'azucar-ill-o' contiene un: (a) prefijo, (b) sufijo, (c) infijo.", "c"),
        85: ("Lexemas", "¿El lexema de 'caminaremos' es 'camin'? (Sí/No)", "sí"),
        86: ("Flexión", "El morfema flexivo de número en 'mesa' es: (a) -a, (b) -s, (c) no tiene.", "c"),
        87: ("Morfología", "La 'familia de palabras' es un conjunto de palabras con el mismo lexema. (Verdadero/Falso)", "verdadero"),
        88: ("Derivación", "¿La palabra 'desordenado' se forma por derivación? (Sí/No)", "sí"),
        89: ("Composición", "La palabra 'mediodía' es una palabra compuesta. (Verdadero/Falso)", "verdadero"),
        90: ("Parasíntesis", "¿La palabra 'a-tarde-cer' es un ejemplo de parasíntesis? (Sí/No)", "sí"),
        91: ("Flexión Verbal", "La 'raíz' del verbo es su lexema. (Verdadero/Falso)", "verdadero"),
        92: ("Morfemas", "¿Los 'alófonos' son variaciones de un morfema? (Sí/No)", "no"),
        93: ("Morfología", "La morfología es una rama de la lingüística que estudia la estructura interna de las palabras. (Verdadero/Falso)", "verdadero"),
        94: ("Conceptos básicos", "El término 'morfología' proviene del griego y significa 'estudio de la forma'. (Verdadero/Falso)", "verdadero"),
        95: ("Derivación", "La palabra 'libertad' se deriva de 'libre'. (Verdadero/Falso)", "verdadero"),
        96: ("Sufijos", "El sufijo '-ista' en 'violinista' indica: (a) oficio o profesión, (b) cualidad, (c) lugar.", "a"),
        97: ("Prefijos", "El prefijo 'extra-' en 'extralargo' indica: (a) dentro, (b) más allá, (c) después.", "b"),
        98: ("Flexión Verbal", "El morfema flexivo de persona en 'leemos' es: (a) -mos, (b) -emos, (c) -le.", "a"),
        99: ("Flexión Nominal", "La palabra 'azul' no tiene morfema de género flexivo. (Verdadero/Falso)", "verdadero"),
        100: ("Repaso", "La palabra 're-com-poner' es un ejemplo de: (a) derivación, (b) composición, (c) parasíntesis.", "c"),
    }

    print("¡Bienvenido al reto de Morfología de la Lengua Castellana!")
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
