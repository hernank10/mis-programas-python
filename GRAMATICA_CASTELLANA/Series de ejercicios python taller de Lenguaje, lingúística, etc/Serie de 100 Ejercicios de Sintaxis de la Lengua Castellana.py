# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Sintaxis de la Lengua Castellana
# Inspirado en las obras del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los conceptos fundamentales de la sintaxis,
# incluyendo sujeto, predicado, sintagmas y los diferentes tipos de complementos verbales.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de sintaxis
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Sujeto", "En la oración 'El perro ladra fuerte', el sujeto es: (a) El perro, (b) fuerte, (c) ladra.", "a"),
        2: ("Predicado", "En la oración 'Mi hermana compró un libro', el predicado es: (a) Mi hermana, (b) compró, (c) compró un libro.", "c"),
        3: ("Núcleo del Sujeto", "El núcleo del sujeto en 'El coche rojo es veloz' es: (a) El, (b) coche, (c) rojo.", "b"),
        4: ("Núcleo del Predicado", "El núcleo del predicado en 'Los estudiantes leen libros' es: (a) Los estudiantes, (b) leen, (c) libros.", "b"),
        5: ("Sintagma Nominal", "Un Sintagma Nominal tiene como núcleo un: (a) verbo, (b) sustantivo, (c) adjetivo.", "b"),
        6: ("Sintagma Verbal", "Un Sintagma Verbal tiene como núcleo un: (a) adverbio, (b) verbo, (c) preposición.", "b"),
        7: ("Oración Simple", "Una oración simple contiene un solo verbo conjugado. (Verdadero/Falso)", "verdadero"),
        8: ("Oración Compuesta", "Una oración compuesta tiene dos o más verbos. (Verdadero/Falso)", "verdadero"),
        9: ("Objeto Directo", "En 'Ella compró una manzana', 'una manzana' es: (a) objeto directo, (b) objeto indirecto, (c) complemento circunstancial.", "a"),
        10: ("Objeto Indirecto", "En 'Di la carta a mi mamá', 'a mi mamá' es: (a) objeto directo, (b) objeto indirecto, (c) complemento circunstancial.", "b"),
        11: ("Comp. Circunstancial", "En 'Estudié en la biblioteca', 'en la biblioteca' es: (a) de lugar, (b) de modo, (c) de tiempo.", "a"),
        12: ("Comp. Circunstancial", "En 'Corrió rápidamente', 'rápidamente' es un complemento circunstancial de: (a) lugar, (b) modo, (c) tiempo.", "b"),
        13: ("Atributo", "En 'María es inteligente', 'inteligente' es un: (a) objeto directo, (b) atributo, (c) complemento circunstancial.", "b"),
        14: ("Oración Predicativa", "Una oración 'predicativa' tiene verbos como ser, estar o parecer. (Verdadero/Falso)", "falso"),
        15: ("Oración Copulativa", "Una oración 'copulativa' tiene verbos como ser, estar o parecer. (Verdadero/Falso)", "verdadero"),
        16: ("Comp. de Régimen", "En 'El niño confía en su padre', 'en su padre' es: (a) objeto directo, (b) complemento de régimen, (c) complemento circunstancial.", "b"),
        17: ("Complemento Agente", "En 'El libro fue escrito por el autor', 'por el autor' es: (a) objeto directo, (b) complemento agente, (c) atributo.", "b"),
        18: ("Oración Activa", "En la voz activa, el sujeto realiza la acción. (Verdadero/Falso)", "verdadero"),
        19: ("Oración Pasiva", "En 'La casa fue construida por los obreros', la oración está en voz: (a) activa, (b) pasiva.", "b"),
        20: ("Sujeto Omitido", "En la oración 'Cantamos en el coro', el sujeto está: (a) presente, (b) omitido.", "b"),
        21: ("Sintagma Preposicional", "Un sintagma preposicional está encabezado por una: (a) preposición, (b) conjunción, (c) adverbio.", "a"),
        22: ("Sintagma Adjetival", "Un Sintagma Adjetival tiene como núcleo un: (a) verbo, (b) sustantivo, (c) adjetivo.", "c"),
        23: ("Sintagma Adverbial", "Un Sintagma Adverbial tiene como núcleo un: (a) adverbio, (b) verbo, (c) preposición.", "a"),
        24: ("Oraciones Coordinadas", "Las oraciones coordinadas se unen por: (a) conjunciones, (b) verbos, (c) preposiciones.", "a"),
        25: ("Coord. Copulativa", "Las conjunciones 'y', 'e', 'ni' son: (a) copulativas, (b) adversativas, (c) disyuntivas.", "a"),
        26: ("Coord. Disyuntiva", "Las conjunciones 'o', 'u' son: (a) copulativas, (b) adversativas, (c) disyuntivas.", "c"),
        27: ("Coord. Adversativa", "La conjunción 'pero' es: (a) copulativa, (b) adversativa, (c) disyuntiva.", "b"),
        28: ("Oraciones Subordinadas", "Las oraciones subordinadas dependen de una principal. (Verdadero/Falso)", "verdadero"),
        29: ("Sub. Sustantiva", "La oración subordinada que funciona como un sustantivo es: (a) sustantiva, (b) adjetiva, (c) adverbial.", "a"),
        30: ("Sub. Adjetiva", "La oración subordinada que funciona como un adjetivo es: (a) sustantiva, (b) adjetiva, (c) adverbial.", "b"),
        31: ("Sub. Adverbial", "La oración subordinada que funciona como un adverbio es: (a) sustantiva, (b) adjetiva, (c) adverbial.", "c"),
        32: ("Análisis sintáctico", "Identificar las partes de una oración se conoce como: (a) análisis morfológico, (b) análisis sintáctico.", "b"),
        33: ("Sujeto", "El 'sujeto léxico' aparece expresamente en la oración. (Verdadero/Falso)", "verdadero"),
        34: ("Sujeto", "El 'sujeto gramatical' se infiere del verbo. (Verdadero/Falso)", "verdadero"),
        35: ("Predicado", "El 'predicado nominal' tiene un verbo copulativo. (Verdadero/Falso)", "verdadero"),
        36: ("Predicado", "El 'predicado verbal' tiene un verbo predicativo. (Verdadero/Falso)", "verdadero"),
        37: ("Objeto Directo", "¿El objeto directo se puede sustituir por 'lo', 'la', 'los', 'las'? (Sí/No)", "sí"),
        38: ("Objeto Indirecto", "¿El objeto indirecto se puede sustituir por 'le', 'les'? (Sí/No)", "sí"),
        39: ("Complemento Circunstancial", "Un complemento circunstancial de 'causa' responde a '¿por qué?'. (Verdadero/Falso)", "verdadero"),
        40: ("Complemento Predicativo", "En 'Los niños llegaron cansados', 'cansados' es un: (a) atributo, (b) complemento predicativo, (c) complemento de régimen.", "b"),
        41: ("Complemento Circunstancial", "El complemento circunstancial de 'compañía' responde a '¿con quién?'. (Verdadero/Falso)", "verdadero"),
        42: ("Complemento Circunstancial", "En 'Escribí con el lápiz', 'con el lápiz' es un complemento circunstancial de: (a) instrumento, (b) compañía, (c) modo.", "a"),
        43: ("Análisis sintáctico", "La función de 'núcleo' es la más importante de un sintagma. (Verdadero/Falso)", "verdadero"),
        44: ("Sintagma Adjetival", "En 'muy alto', 'alto' es el núcleo del sintagma adjetival. (Verdadero/Falso)", "verdadero"),
        45: ("Sintagma Adverbial", "En 'muy cerca', 'cerca' es el núcleo del sintagma adverbial. (Verdadero/Falso)", "verdadero"),
        46: ("Comp. de Régimen", "El complemento de régimen es exigido por el verbo. (Verdadero/Falso)", "verdadero"),
        47: ("Oración Impersonal", "Una oración impersonal no tiene sujeto. (Verdadero/Falso)", "verdadero"),
        48: ("Oración Impersonal", "¿'Llueve' es una oración impersonal? (Sí/No)", "sí"),
        49: ("Oración Exclamativa", "Una oración exclamativa expresa una emoción. (Verdadero/Falso)", "verdadero"),
        50: ("Oración Interrogativa", "Una oración interrogativa formula una pregunta. (Verdadero/Falso)", "verdadero"),
        51: ("Oración Declarativa", "Una oración declarativa informa sobre algo. (Verdadero/Falso)", "verdadero"),
        52: ("Oración Imperativa", "Una oración imperativa expresa una orden o ruego. (Verdadero/Falso)", "verdadero"),
        53: ("Sintagmas", "En 'El amigo de Pedro', 'de Pedro' es un: (a) Sintagma Verbal, (b) Sintagma Preposicional, (c) Sintagma Adjetival.", "b"),
        54: ("Sub. Sustantiva", "En 'Me gusta que vengas', 'que vengas' es una subordinada sustantiva. (Verdadero/Falso)", "verdadero"),
        55: ("Sub. Adjetiva", "En 'La casa que me gusta', 'que me gusta' es una subordinada adjetiva. (Verdadero/Falso)", "verdadero"),
        56: ("Sub. Adverbial", "En 'Iré cuando pueda', 'cuando pueda' es una subordinada adverbial. (Verdadero/Falso)", "verdadero"),
        57: ("Análisis sintáctico", "La función del sujeto es realizar la acción. (Verdadero/Falso)", "verdadero"),
        58: ("Sintaxis", "El 'predicado nominal' contiene el verbo 'ser', 'estar' o 'parecer'. (Verdadero/Falso)", "verdadero"),
        59: ("Comp. Circunstancial", "En 'Hizo el trabajo por la mañana', 'por la mañana' es un complemento circunstancial de: (a) lugar, (b) tiempo, (c) causa.", "b"),
        60: ("Oración Impersonal", "¿'Hay mucha gente' es una oración impersonal? (Sí/No)", "sí"),
        61: ("Sujeto", "En 'Me duele la cabeza', el sujeto es: (a) Me, (b) duele, (c) la cabeza.", "c"),
        62: ("Predicado", "En 'Se venden casas', el predicado es: (a) se, (b) venden casas, (c) casas.", "b"),
        63: ("Objeto Directo", "En 'Traje flores a mamá', 'flores' es: (a) objeto directo, (b) objeto indirecto, (c) complemento circunstancial.", "a"),
        64: ("Objeto Indirecto", "En 'Traje flores a mamá', 'a mamá' es: (a) objeto directo, (b) objeto indirecto, (c) complemento circunstancial.", "b"),
        65: ("Comp. Circunstancial", "El complemento circunstancial de 'fin' responde a '¿para qué?'. (Verdadero/Falso)", "verdadero"),
        66: ("Comp. Predicativo", "El predicativo concuerda en género y número con el sujeto u objeto. (Verdadero/Falso)", "verdadero"),
        67: ("Sintagma Adverbial", "En 'El examen es muy difícil', 'muy' es un Sintagma: (a) Adjetival, (b) Adverbial, (c) Preposicional.", "b"),
        68: ("Subordinadas", "Las subordinadas adverbiales pueden ser de tiempo, lugar, modo, causa, etc. (Verdadero/Falso)", "verdadero"),
        69: ("Subordinadas", "Las subordinadas sustantivas pueden ser de sujeto, objeto directo, etc. (Verdadero/Falso)", "verdadero"),
        70: ("Subordinadas", "Las subordinadas adjetivas se introducen por un pronombre relativo. (Verdadero/Falso)", "verdadero"),
        71: ("Sintagma Nominal", "En 'El niño de la casa', 'de la casa' es un complemento del: (a) verbo, (b) nombre.", "b"),
        72: ("Sintagma Verbal", "En 'Compra los libros', 'los libros' es un complemento del: (a) nombre, (b) verbo.", "b"),
        73: ("Objeto Directo", "En 'La compró', 'La' sustituye al: (a) objeto directo, (b) objeto indirecto.", "a"),
        74: ("Objeto Indirecto", "En 'Le dio un regalo', 'Le' sustituye al: (a) objeto directo, (b) objeto indirecto.", "b"),
        75: ("Voz Pasiva", "La voz pasiva se construye con el verbo 'ser' más el participio. (Verdadero/Falso)", "verdadero"),
        76: ("Oración", "Una oración puede estar formada por una sola palabra. (Verdadero/Falso)", "verdadero"),
        77: ("Oración Unimembre", "¿'¡Hola!' es una oración unimembre? (Sí/No)", "sí"),
        78: ("Oración Bimembre", "Una oración 'bimembre' tiene sujeto y predicado. (Verdadero/Falso)", "verdadero"),
        79: ("Sintaxis", "El sintagma es la unidad gramatical intermedia entre la palabra y la oración. (Verdadero/Falso)", "verdadero"),
        80: ("Atributo", "El atributo concuerda en género y número con el sujeto. (Verdadero/Falso)", "verdadero"),
        81: ("Predicado Nominal", "En 'El cielo está nublado', 'nublado' es un: (a) objeto directo, (b) atributo, (c) complemento circunstancial.", "b"),
        82: ("Sujeto", "¿El sujeto puede estar después del verbo? (Sí/No)", "sí"),
        83: ("Objeto Indirecto", "El objeto indirecto suele ir precedido por la preposición 'a'. (Verdadero/Falso)", "verdadero"),
        84: ("Comp. Circunstancial", "En 'Caminé tres kilómetros', 'tres kilómetros' es un complemento circunstancial de: (a) lugar, (b) cantidad, (c) tiempo.", "b"),
        85: ("Oración Enunciativa", "Las oraciones enunciativas pueden ser afirmativas o negativas. (Verdadero/Falso)", "verdadero"),
        86: ("Sub. Adverbial", "Las subordinadas adverbiales pueden ser sustituidas por un adverbio. (Verdadero/Falso)", "verdadero"),
        87: ("Sintagma Nominal", "En 'Un coche deportivo', 'deportivo' es un complemento del: (a) nombre, (b) verbo, (c) adjetivo.", "a"),
        88: ("Sintagma Verbal", "El Sintagma Verbal cumple la función de: (a) sujeto, (b) predicado.", "b"),
        89: ("Sintagma Nominal", "El Sintagma Nominal cumple la función de: (a) sujeto, (b) predicado.", "a"),
        90: ("Comp. de Régimen", "El complemento de régimen no se puede eliminar sin cambiar el sentido de la oración. (Verdadero/Falso)", "verdadero"),
        91: ("Sintaxis", "El 'complemento predicativo' complementa al verbo y al sujeto o al objeto directo. (Verdadero/Falso)", "verdadero"),
        92: ("Oración Simple", "¿'Corrí y canté' es una oración simple? (Sí/No)", "no"),
        93: ("Oración Compuesta", "Las oraciones compuestas se dividen en coordinadas y subordinadas. (Verdadero/Falso)", "verdadero"),
        94: ("Sub. Sustantiva", "En 'Me dijo que no vendría', 'que no vendría' es una subordinada: (a) sustantiva, (b) adjetiva, (c) adverbial.", "a"),
        95: ("Sub. Adjetiva", "En 'El chico que vino es mi amigo', 'que vino' es una subordinada: (a) sustantiva, (b) adjetiva, (c) adverbial.", "b"),
        96: ("Sub. Adverbial", "En 'Cuando salgas, cierra la puerta', 'cuando salgas' es una subordinada: (a) sustantiva, (b) adjetiva, (c) adverbial.", "c"),
        97: ("Análisis sintáctico", "La concordancia verbal se establece entre el verbo y el: (a) objeto directo, (b) sujeto, (c) complemento circunstancial.", "b"),
        98: ("Complemento Agente", "El complemento agente siempre va precedido por la preposición 'por'. (Verdadero/Falso)", "verdadero"),
        99: ("Sintaxis", "La 'disyunción' en una oración coordinada se indica con 'o' o 'u'. (Verdadero/Falso)", "verdadero"),
        100: ("Repaso", "La sintaxis es el estudio de la función de las palabras en la oración. (Verdadero/Falso)", "verdadero"),
    }

    print("¡Bienvenido al reto de Sintaxis de la Lengua Castellana!")
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
