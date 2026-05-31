# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Filosofía del Lenguaje
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los conceptos fundamentales de la filosofía del lenguaje.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de filosofía del lenguaje
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Generalidades", "La rama de la filosofía que estudia la naturaleza del significado, la referencia y el uso del lenguaje es la: (a) metafísica, (b) estética, (c) filosofía del lenguaje.", "c"),
        2: ("Semántica", "La relación entre una palabra y el objeto o concepto que representa se llama: (a) referencia, (b) sentido, (c) denotación.", "a"),
        3: ("Pragmática", "La teoría que afirma que el lenguaje no solo describe la realidad sino que también realiza acciones se conoce como la teoría de los: (a) actos de habla, (b) juegos del lenguaje, (c) universales lingüísticos.", "a"),
        4: ("Filósofos", "¿Quién propuso la famosa distinción entre 'sentido' y 'referencia'? (a) Ludwig Wittgenstein, (b) Gottlob Frege, (c) Ferdinand de Saussure.", "b"),
        5: ("Lenguaje y Pensamiento", "La hipótesis de Sapir-Whorf postula que el lenguaje que hablamos afecta la forma en que pensamos. (Verdadero/Falso)", "verdadero"),
        6: ("Actos de Habla", "¿Un acto locutivo es el acto de decir algo con un significado concreto? (Sí/No)", "sí"),
        7: ("Semántica", "La 'connotación' de una palabra se refiere a su significado literal. (Verdadero/Falso)", "falso"),
        8: ("Filósofos", "El concepto de 'juegos del lenguaje' es central en la obra del filósofo: (a) John L. Austin, (b) J. R. Searle, (c) Ludwig Wittgenstein.", "c"),
        9: ("Pragmática", "Un 'acto ilocutivo' es el efecto que una expresión produce en el oyente. (Verdadero/Falso)", "falso"),
        10: ("Semántica", "¿La ambigüedad léxica se produce cuando una palabra tiene más de un significado? (Sí/No)", "sí"),
        11: ("Filósofos", "El filósofo Ferdinand de Saussure es considerado el padre de la lingüística moderna. (Verdadero/Falso)", "verdadero"),
        12: ("Actos de Habla", "¿Qué tipo de acto de habla es 'Te prometo que llegaré a tiempo'? (a) asertivo, (b) directivo, (c) compromisorio.", "c"),
        13: ("Semántica", "El 'significado' de una palabra es el conjunto de sus características que la distinguen de otras. (Verdadero/Falso)", "verdadero"),
        14: ("Lenguaje y Pensamiento", "La idea de que el pensamiento es posible sin el lenguaje se conoce como 'mentalismo'. (Verdadero/Falso)", "verdadero"),
        15: ("Filósofos", "J. L. Austin es conocido por su contribución a la teoría de: (a) la gramática generativa, (b) la teoría de los actos de habla, (c) la semántica formal.", "b"),
        16: ("Pragmática", "El acto de habla '¿Puedes pasarme la sal?' es un ejemplo de un acto: (a) directo, (b) indirecto, (c) ilocutivo.", "b"),
        17: ("Semántica", "¿'Sustancia' es un concepto central en la semántica de Noam Chomsky? (Sí/No)", "no"),
        18: ("Filósofos", "¿Qué filósofo argumentó que la referencia es una relación causal entre un nombre y su referente? (a) Kripke, (b) Frege, (c) Russell.", "a"),
        19: ("Actos de Habla", "Un 'acto perlocutivo' es el efecto de la acción de hablar. (Verdadero/Falso)", "verdadero"),
        20: ("Generalidades", "La dicotomía 'lengua' (sistema abstracto) y 'habla' (uso individual) es de: (a) Chomsky, (b) Wittgenstein, (c) Saussure.", "c"),
        21: ("Semántica", "Una tautología es una frase que siempre es verdadera. (Verdadero/Falso)", "verdadero"),
        22: ("Filósofos", "Noam Chomsky es el principal representante de la: (a) gramática transformacional, (b) gramática descriptiva, (c) gramática normativa.", "a"),
        23: ("Pragmática", "La máxima de Grice de 'ser relevante' pertenece al principio de: (a) calidad, (b) cantidad, (c) relación.", "c"),
        24: ("Lenguaje y Pensamiento", "¿La idea de que el lenguaje determina el pensamiento es conocida como 'determinismo lingüístico'? (Sí/No)", "sí"),
        25: ("Semántica", "¿Cuál de estos filósofos no trabajó en semántica formal? (a) Frege, (b) Tarski, (c) Heidegger.", "c"),
        26: ("Generalidades", "¿La filosofía del lenguaje se ocupa de cómo el lenguaje 'crea' la realidad social? (Sí/No)", "sí"),
        27: ("Actos de Habla", "La afirmación 'Declaro la sesión abierta' es un ejemplo de un acto de habla: (a) asertivo, (b) declarativo, (c) expresivo.", "b"),
        28: ("Filósofos", "La teoría de las descripciones definidas es de: (a) Bertrand Russell, (b) Gottlob Frege, (c) John L. Austin.", "a"),
        29: ("Semántica", "Un sinónimo perfecto tiene exactamente el mismo significado que otra palabra. (Verdadero/Falso)", "verdadero"),
        30: ("Generalidades", "El estudio de la forma en que las personas usan el lenguaje en la comunicación se llama: (a) semántica, (b) pragmática, (c) sintaxis.", "b"),
        31: ("Lenguaje y Pensamiento", "¿La idea de que el lenguaje simplemente refleja el pensamiento se conoce como 'reflejo lingüístico'? (Sí/No)", "sí"),
        32: ("Actos de Habla", "Un acto de habla 'directivo' tiene la intención de comprometer al oyente a una acción futura. (Verdadero/Falso)", "falso"),
        33: ("Filósofos", "La obra 'Investigaciones filosóficas' es una de las principales de: (a) Wittgenstein, (b) Quine, (c) Austin.", "a"),
        34: ("Semántica", "Un 'paradigma' es un conjunto de elementos lingüísticos con una función similar. (Verdadero/Falso)", "verdadero"),
        35: ("Generalidades", "¿La filosofía del lenguaje se preocupa por la gramática de una lengua? (Sí/No)", "no"),
        36: ("Lenguaje y Pensamiento", "La hipótesis de Whorf se considera una forma de relativismo lingüístico. (Verdadero/Falso)", "verdadero"),
        37: ("Pragmática", "La 'cortesía' en la comunicación es un concepto de la semántica. (Verdadero/Falso)", "falso"),
        38: ("Filósofos", "La teoría de los 'nombres propios' de Kripke es una crítica a la teoría de la referencia de: (a) Wittgenstein, (b) Frege, (c) Saussure.", "b"),
        39: ("Actos de Habla", "¿Un acto 'expresivo' expresa un estado psicológico del hablante? (Sí/No)", "sí"),
        40: ("Semántica", "La 'polisemia' ocurre cuando una palabra tiene varios significados relacionados. (Verdadero/Falso)", "verdadero"),
        41: ("Generalidades", "¿El lenguaje es una herramienta para expresar pensamientos preexistentes? (Sí/No)", "sí"),
        42: ("Pragmática", "El contexto es irrelevante para la pragmática. (Verdadero/Falso)", "falso"),
        43: ("Filósofos", "La teoría de los 'indicadores' de Charles Sanders Peirce se relaciona con: (a) la sintaxis, (b) la semiótica, (c) la fonología.", "b"),
        44: ("Actos de Habla", "Un acto 'comisivo' compromete al hablante a realizar un acto futuro. (Verdadero/Falso)", "verdadero"),
        45: ("Semántica", "Una 'contradicción' es una frase que siempre es falsa. (Verdadero/Falso)", "verdadero"),
        46: ("Lenguaje y Pensamiento", "La teoría de 'La jaula de Wittgenstein' es un argumento contra el lenguaje privado. (Verdadero/Falso)", "verdadero"),
        47: ("Filósofos", "El filósofo John Searle es conocido por su clasificación de los actos de habla. (Verdadero/Falso)", "verdadero"),
        48: ("Pragmática", "La 'implicatura' es lo que un hablante quiere comunicar sin decirlo explícitamente. (Verdadero/Falso)", "verdadero"),
        49: ("Semántica", "La 'ambigüedad estructural' se da cuando una oración puede tener múltiples interpretaciones sintácticas. (Verdadero/Falso)", "verdadero"),
        50: ("Generalidades", "La filosofía del lenguaje es una disciplina analítica. (Verdadero/Falso)", "verdadero"),
        51: ("Actos de Habla", "Un acto 'representativo' compromete al hablante a la verdad de la proposición expresada. (Verdadero/Falso)", "verdadero"),
        52: ("Filósofos", "La obra 'El origen de las especies' es de: (a) Darwin, (b) Chomsky, (c) Frege.", "a"),
        53: ("Semántica", "La 'relación de hiponimia' se da entre una palabra más general y otra más específica. (Verdadero/Falso)", "verdadero"),
        54: ("Pragmática", "La 'presuposición' es información que se asume como verdadera en un enunciado. (Verdadero/Falso)", "verdadero"),
        55: ("Generalidades", "La 'lingüística' es una rama de la filosofía del lenguaje. (Verdadero/Falso)", "falso"),
        56: ("Filósofos", "¿Quién propuso la 'tabla de la verdad' para la lógica proposicional? (a) Wittgenstein, (b) Frege, (c) Russell.", "c"),
        57: ("Semántica", "La 'antonimia' se refiere a la relación de significado opuesto entre palabras. (Verdadero/Falso)", "verdadero"),
        58: ("Actos de Habla", "Un acto 'declarativo' tiene la capacidad de cambiar la realidad. (Verdadero/Falso)", "verdadero"),
        59: ("Lenguaje y Pensamiento", "¿La teoría de Chomsky apoya el determinismo lingüístico? (Sí/No)", "no"),
        60: ("Generalidades", "La filosofía del lenguaje se preocupa por la moral del lenguaje. (Verdadero/Falso)", "falso"),
        61: ("Filósofos", "¿Qué filósofo es conocido por su análisis de los 'nombres de familia'? (a) Wittgenstein, (b) Austin, (c) Saussure.", "a"),
        62: ("Semántica", "Una 'metáfora' se basa en la referencia literal de las palabras. (Verdadero/Falso)", "falso"),
        63: ("Pragmática", "El 'principio de cooperación' de Grice se aplica a las conversaciones. (Verdadero/Falso)", "verdadero"),
        64: ("Lenguaje y Pensamiento", "El 'relativismo lingüístico' postula que las diferencias en los lenguajes causan diferencias en el pensamiento. (Verdadero/Falso)", "verdadero"),
        65: ("Semántica", "La 'semántica composicional' se refiere a cómo el significado de una oración se construye a partir de sus partes. (Verdadero/Falso)", "verdadero"),
        66: ("Filósofos", "La obra 'Tractatus Logico-Philosophicus' es una de las primeras de: (a) Wittgenstein, (b) Russell, (c) Frege.", "a"),
        67: ("Actos de Habla", "Un acto 'expresivo' tiene un efecto directo en el mundo. (Verdadero/Falso)", "falso"),
        68: ("Pragmática", "¿Los 'deícticos' son palabras cuyo significado depende del contexto (ej. 'aquí', 'ahora')? (Sí/No)", "sí"),
        69: ("Semántica", "La 'homonimia' ocurre cuando dos palabras se escriben igual pero tienen significados no relacionados. (Verdadero/Falso)", "verdadero"),
        70: ("Generalidades", "La filosofía del lenguaje es una disciplina exclusivamente moderna. (Verdadero/Falso)", "falso"),
        71: ("Filósofos", "¿Quién propuso el famoso 'criterio de verificabilidad' del positivismo lógico? (a) Ayer, (b) Quine, (c) Wittgenstein.", "a"),
        72: ("Pragmática", "¿Las 'implicaturas conversacionales' se dan en la forma de oraciones literales? (Sí/No)", "no"),
        73: ("Semántica", "La 'ambigüedad referencial' se produce cuando un pronombre puede referirse a varios antecedentes. (Verdadero/Falso)", "verdadero"),
        74: ("Lenguaje y Pensamiento", "La 'teoría del lenguaje de pensamiento' postula que el pensamiento ocurre en un lenguaje mental innato. (Verdadero/Falso)", "verdadero"),
        75: ("Filósofos", "El filósofo John Austin es el autor de la frase 'Decir es hacer'. (Verdadero/Falso)", "verdadero"),
        76: ("Actos de Habla", "¿Un acto de habla 'asertivo' tiene el objetivo de comprometer al hablante con la verdad de una proposición? (Sí/No)", "sí"),
        77: ("Semántica", "El 'sentido' de una palabra es el modo en que se nos presenta su referente. (Verdadero/Falso)", "verdadero"),
        78: ("Filósofos", "La 'navaja de Ockham' es un principio que se aplica a la semántica formal. (Verdadero/Falso)", "falso"),
        79: ("Pragmática", "Las 'máximas de Grice' son principios que rigen la comunicación. (Verdadero/Falso)", "verdadero"),
        80: ("Generalidades", "La filosofía del lenguaje es una disciplina que estudia el lenguaje como un fenómeno puramente biológico. (Verdadero/Falso)", "falso"),
        81: ("Filósofos", "¿Quién propuso el concepto de 'analogía de la familia'? (a) Chomsky, (b) Wittgenstein, (c) Saussure.", "b"),
        82: ("Semántica", "¿'Sinonimia' es la relación entre dos palabras con significados opuestos? (Sí/No)", "no"),
        83: ("Actos de Habla", "Un acto de habla 'declarativo' tiene una dirección de ajuste mundo-a-palabra. (Verdadero/Falso)", "verdadero"),
        84: ("Lenguaje y Pensamiento", "La 'teoría del pensamiento sin lenguaje' es una teoría de: (a) Piaget, (b) Chomsky, (c) Fodor.", "a"),
        85: ("Filósofos", "El filósofo W. V. O. Quine es conocido por su trabajo en la: (a) semántica formal, (b) pragmática, (c) filosofía de la ciencia y el lenguaje.", "c"),
        86: ("Semántica", "La 'pragmática' se enfoca en el significado de la oración independientemente del contexto. (Verdadero/Falso)", "falso"),
        87: ("Actos de Habla", "¿La 'felicidad' de un acto de habla se refiere a si tiene éxito o no? (Sí/No)", "sí"),
        88: ("Filósofos", "La teoría de los 'nombres rígidamente designadores' es de: (a) Kripke, (b) Austin, (c) Frege.", "a"),
        89: ("Generalidades", "La filosofía del lenguaje es una disciplina que estudia la relación entre la lengua y la sociedad. (Verdadero/Falso)", "verdadero"),
        90: ("Pragmática", "La 'ilicitud' es un aspecto de la teoría de los actos de habla. (Verdadero/Falso)", "falso"),
        91: ("Semántica", "¿La 'hiponimia' es la relación entre un concepto más general y uno más específico? (Sí/No)", "sí"),
        92: ("Filósofos", "¿Qué filósofo es conocido por su teoría de la 'distinción entre analítico y sintético'? (a) Kant, (b) Quine, (c) Frege.", "b"),
        93: ("Actos de Habla", "Un acto 'expresivo' tiene una dirección de ajuste mundo-a-palabra. (Verdadero/Falso)", "falso"),
        94: ("Generalidades", "El 'significado' de una palabra es lo que se conoce como 'referencia'. (Verdadero/Falso)", "falso"),
        95: ("Pragmática", "La 'deixis' es un concepto central en la pragmática. (Verdadero/Falso)", "verdadero"),
        96: ("Semántica", "¿La 'polisemia' se da cuando dos palabras tienen el mismo sonido pero diferentes significados? (Sí/No)", "no"),
        97: ("Filósofos", "El filósofo J. L. Austin es el autor de 'Cómo hacer cosas con palabras'. (Verdadero/Falso)", "verdadero"),
        98: ("Pragmática", "Las 'implicaturas' son explícitas en la comunicación. (Verdadero/Falso)", "falso"),
        99: ("Semántica", "La 'paráfrasis' es una oración que tiene un significado similar a otra. (Verdadero/Falso)", "verdadero"),
        100: ("Generalidades", "¿La filosofía del lenguaje es una disciplina que estudia la forma de hablar de una persona individual? (Sí/No)", "no"),
    }

    print("¡Bienvenido al reto de Filosofía del Lenguaje!")
    print("---------------------------------------------------------")
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
