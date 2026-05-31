# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Dialectología del Español
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre las variedades del español,
# incluyendo diferencias fonéticas, léxicas, morfosintácticas y sociales.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de dialectología
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Generalidades", "El estudio de las variedades geográficas de una lengua se llama: (a) sociolingüística, (b) dialectología, (c) etimología.", "b"),
        2: ("Fonética", "La pronunciación de la 's' al final de sílaba como una aspiración o una oclusión glotal (ej. 'loh niño') es característica de los dialectos: (a) caribeños, (b) andinos, (c) peninsulares del norte.", "a"),
        3: ("Léxico", "En el español de México, la palabra 'chamba' significa: (a) fiesta, (b) trabajo, (c) problema.", "b"),
        4: ("Morfosintaxis", "El uso de 'vos' en lugar de 'tú' (tuteo) es un fenómeno conocido como: (a) voseo, (b) tuteo, (c) ustedeo.", "a"),
        5: ("Fonética", "El 'yeísmo' es la pronunciación de 'll' y 'y' con el mismo sonido. ¿Es 'caballo' y 'cayo' un ejemplo de esto? (Sí/No)", "sí"),
        6: ("Léxico", "En el español de España, ¿cuál es la palabra para 'palomitas de maíz'? (a) cotufas, (b) pochoclo, (c) palomitas.", "c"),
        7: ("Generalidades", "Un 'sociolecto' es una variedad de la lengua utilizada por: (a) una región geográfica, (b) un grupo social, (c) una persona individual.", "b"),
        8: ("Fonética", "¿El seseo (pronunciar la 'c' y la 'z' como 's') es un rasgo fonético del español de América? (Sí/No)", "sí"),
        9: ("Léxico", "En el español de Argentina, 'pochoclo' se refiere a: (a) palomitas de maíz, (b) un tipo de dulce, (c) una bebida.", "a"),
        10: ("Morfosintaxis", "La utilización del 'vos' con la conjugación del 'tú' (ej. 'vos comes') se da en el español de: (a) Argentina, (b) Colombia, (c) Chile.", "b"),
        11: ("Fonética", "El 'ceceo' es la pronunciación de 's', 'c' y 'z' como el sonido de la 'z' española. ¿Es típico de gran parte de Andalucía? (Sí/No)", "sí"),
        12: ("Léxico", "¿En el español de Chile, la palabra 'pololo' se refiere a una pareja romántica? (Sí/No)", "sí"),
        13: ("Generalidades", "La variedad lingüística de un solo hablante se conoce como: (a) dialecto, (b) sociolecto, (c) idiolecto.", "c"),
        14: ("Fonética", "La 'd' intervocálica se pierde en algunos dialectos (ej. 'partío' por 'partido'). ¿Es esto un rasgo de la variación dialectal? (Sí/No)", "sí"),
        15: ("Léxico", "La palabra 'guagua' (autobús) es un léxico común en: (a) el Cono Sur, (b) las Antillas, (c) México.", "b"),
        16: ("Morfosintaxis", "En el español de Chile, ¿es común el uso de 'tenís' en lugar de 'tienes'? (Sí/No)", "sí"),
        17: ("Generalidades", "Un 'isoglosa' es una línea imaginaria que separa áreas con diferentes rasgos lingüísticos. (Verdadero/Falso)", "verdadero"),
        18: ("Léxico", "¿En el español andino de Colombia, se usa 'chola' para referirse a sandalias o chanclas? (Sí/No)", "sí"),
        19: ("Fonética", "La 'j' en palabras como 'caja' o 'ejemplo' se pronuncia más suave en el español caribeño que en el peninsular. (Verdadero/Falso)", "verdadero"),
        20: ("Léxico", "La palabra 'computadora' es más común en Latinoamérica, mientras que 'ordenador' es más común en España. (Verdadero/Falso)", "verdadero"),
        21: ("Léxico", "¿En el español de Venezuela, la palabra 'pana' significa amigo? (Sí/No)", "sí"),
        22: ("Fonética", "La 'll' se pronuncia como un sonido 'sh' en el español rioplatense (ej. 'cabasho'). ¿Cómo se llama este fenómeno? (a) seseo, (b) zheísmo, (c) rotacismo.", "b"),
        23: ("Léxico", "¿En el español de Perú, 'chullo' se refiere a un gorro andino con orejeras? (Sí/No)", "sí"),
        24: ("Fonética", "El debilitamiento de la 'r' final en los infinitivos ('comé' por 'comer') es un rasgo de algunos dialectos. (Verdadero/Falso)", "verdadero"),
        25: ("Léxico", "En el español de Cuba, 'asere' se usa para referirse a un amigo. (Verdadero/Falso)", "verdadero"),
        26: ("Generalidades", "La dialectología se considera una rama de la sociolingüística. (Verdadero/Falso)", "verdadero"),
        27: ("Fonética", "La asimilación de 'n' a la sílaba siguiente (ej. 'un beso' como 'um beso') es un fenómeno común. (Verdadero/Falso)", "verdadero"),
        28: ("Léxico", "La palabra 'pibe' (niño) es típica del español de: (a) España, (b) Argentina, (c) Colombia.", "b"),
        29: ("Morfosintaxis", "El uso de pronombres de objeto directo/indirecto ('leíste el libro' vs. 'lo leíste') varía entre dialectos. (Verdadero/Falso)", "verdadero"),
        30: ("Fonética", "La diferencia fonética entre 'casa' y 'caza' en el español peninsular es conocida como: (a) seseo, (b) yeísmo, (c) distinción.", "c"),
        31: ("Léxico", "¿La palabra 'carro' es más común en Latinoamérica, mientras que 'coche' lo es en España? (Sí/No)", "sí"),
        32: ("Generalidades", "La 'prestigiosa' variedad dialectal es la que tiene mayor número de hablantes. (Verdadero/Falso)", "falso"),
        33: ("Léxico", "En el español de Puerto Rico, 'boricua' significa: (a) nativo puertorriqueño, (b) comida típica, (c) baile tradicional.", "a"),
        34: ("Morfosintaxis", "¿El 'dequeísmo' (ej. 'Pienso de que...' en lugar de 'Pienso que...') es considerado un rasgo dialectal? (Sí/No)", "sí"),
        35: ("Léxico", "La palabra 'torta' en el español de México significa pastel, mientras que en España es una galleta. (Verdadero/Falso)", "falso"),
        36: ("Fonética", "La omisión de la 'd' final en palabras como 'verdad' es un rasgo: (a) peninsular, (b) caribeño, (c) andino.", "a"),
        37: ("Generalidades", "Un 'continuum dialectal' se refiere a la variación gradual de una lengua en un área geográfica. (Verdadero/Falso)", "verdadero"),
        38: ("Léxico", "En el español de Colombia, 'parce' significa: (a) amigo, (b) padre, (c) persona.", "a"),
        39: ("Fonética", "La vocalización de la 'l' final de sílaba (ej. 'autobúi' por 'autobús') es un rasgo del dialecto andaluz. (Verdadero/Falso)", "falso"),
        40: ("Léxico", "¿'Fresa' en el español de México se refiere a una persona 'fina' o 'snob'? (Sí/No)", "sí"),
        41: ("Léxico", "¿En el español de Argentina, 'fiaca' significa pereza? (Sí/No)", "sí"),
        42: ("Fonética", "El 'lambdacismo' es la articulación de la 'r' como 'l' ('cuerpo' por 'cuelpo'). ¿Es común en dialectos caribeños? (Sí/No)", "sí"),
        43: ("Morfosintaxis", "El 'leísmo' (usar 'le' como objeto directo) es una característica de: (a) el español de Chile, (b) el español de España, (c) el español de Argentina.", "b"),
        44: ("Léxico", "En el español de Ecuador, 'chuta' es una expresión de sorpresa. (Verdadero/Falso)", "verdadero"),
        45: ("Fonética", "La pérdida de la 'd' intervocálica en 'cansado' es un rasgo de dialectos peninsulares. (Verdadero/Falso)", "verdadero"),
        46: ("Léxico", "La palabra 'chévere' es un sinónimo de 'cool' o 'genial' en: (a) España, (b) el Caribe, (c) el Cono Sur.", "b"),
        47: ("Morfosintaxis", "La posición del pronombre 'se' en construcciones como 'se cayó' varía en algunas zonas. (Verdadero/Falso)", "verdadero"),
        48: ("Generalidades", "La 'koiné' es una variedad lingüística que surge de la mezcla de dialectos. (Verdadero/Falso)", "verdadero"),
        49: ("Léxico", "¿En el español de México, 'guayaba' es una palabra para referirse a la fruta, no a una mentira? (Sí/No)", "no"),
        50: ("Fonética", "El 'rotacismo' es la articulación de la 'l' como 'r' ('algo' por 'argo'). ¿Es común en el dialecto andaluz? (Sí/No)", "sí"),
        51: ("Léxico", "La palabra 'bacán' (genial) se usa en: (a) el Cono Sur, (b) el Caribe, (c) Perú y Chile.", "c"),
        52: ("Generalidades", "El 'estrato social' es un factor determinante en la variación del habla. (Verdadero/Falso)", "verdadero"),
        53: ("Léxico", "¿En el español de Uruguay y Argentina, 'che' es una interjección para llamar la atención? (Sí/No)", "sí"),
        54: ("Fonética", "La distinción entre 'y' y 'll' es la norma en los dialectos centrales de España y andinos. (Verdadero/Falso)", "verdadero"),
        55: ("Léxico", "La palabra 'chamo' (niño/a) es un término común en el español de: (a) Venezuela, (b) Colombia, (c) México.", "a"),
        56: ("Morfosintaxis", "El 'loísmo' es un fenómeno que se da en algunos dialectos de España. (Verdadero/Falso)", "verdadero"),
        57: ("Léxico", "La palabra 'carajillo' en España se refiere a una bebida alcohólica con café. (Verdadero/Falso)", "verdadero"),
        58: ("Fonética", "En el español caribeño, la 'r' y la 'l' se intercambian a menudo en la coda silábica. (Verdadero/Falso)", "verdadero"),
        59: ("Léxico", "¿La palabra 'camión' es más común en España, mientras que 'autobús' lo es en México? (Sí/No)", "no"),
        60: ("Generalidades", "Un 'dialecto' es un sistema lingüístico derivado de otro pero con diferencias significativas. (Verdadero/Falso)", "verdadero"),
        61: ("Fonética", "¿La aspiración de 'j' ('jefe' como 'hefe') es un rasgo fonético del español de México? (Sí/No)", "sí"),
        62: ("Léxico", "La palabra 'guay' (genial) es un término de jerga en: (a) España, (b) Colombia, (c) México.", "a"),
        63: ("Morfosintaxis", "El uso de 'hágale' o 'dele' para animar a alguien es un rasgo del español de: (a) Argentina, (b) Colombia, (c) Chile.", "b"),
        64: ("Fonética", "La pronunciación de la 'r' final como una vibrante múltiple en 'parque' es típica de dialectos andinos. (Verdadero/Falso)", "falso"),
        65: ("Léxico", "¿En el español de Cuba, 'mango' es una palabra para referirse a un hombre atractivo? (Sí/No)", "sí"),
        66: ("Fonética", "El 'asibilamiento' de la 'rr' (sonido 'zrr') se encuentra en dialectos: (a) caribeños, (b) andinos, (c) rioplatenses.", "b"),
        67: ("Léxico", "La palabra 'frutilla' se usa para referirse a fresa en el Cono Sur. (Verdadero/Falso)", "verdadero"),
        68: ("Generalidades", "La dialectología se relaciona con la geografía, la historia y la sociología. (Verdadero/Falso)", "verdadero"),
        69: ("Léxico", "¿En el español de Puerto Rico, 'china' se refiere a la fruta naranja? (Sí/No)", "sí"),
        70: ("Morfosintaxis", "El uso de la forma 'ustedes' en lugar de 'vosotros' es una característica general del español de América. (Verdadero/Falso)", "verdadero"),
        71: ("Fonética", "La pérdida de la 's' final de sílaba es un rasgo distintivo del español peninsular del norte. (Verdadero/Falso)", "falso"),
        72: ("Léxico", "¿En el español de Guatemala, 'patojo' es una palabra para niño? (Sí/No)", "sí"),
        73: ("Morfosintaxis", "El uso del pretérito simple ('comí') en lugar del compuesto ('he comido') es un rasgo de la mayoría de los dialectos americanos. (Verdadero/Falso)", "verdadero"),
        74: ("Fonética", "El alargamiento de vocales en sílabas tónicas es un rasgo de acento en el español de: (a) Chile, (b) México, (c) Colombia.", "a"),
        75: ("Léxico", "En el español de España, 'plátano' es para la fruta, y 'banana' para un plátano más pequeño. (Verdadero/Falso)", "falso"),
        76: ("Fonética", "¿El 'rehilamiento' de la 'll' y la 'y' ('cabasho') es un rasgo del español de Argentina? (Sí/No)", "sí"),
        77: ("Léxico", "La palabra 'paraguas' es común en España, mientras que 'sombrilla' es más común en Latinoamérica. (Verdadero/Falso)", "falso"),
        78: ("Morfosintaxis", "En el español rioplatense, el pronombre 'vos' se usa con la conjugación del 'tú' (ej. 'vos tenés'). (Verdadero/Falso)", "verdadero"),
        79: ("Léxico", "¿'Cuate' en México es un sinónimo de amigo? (Sí/No)", "sí"),
        80: ("Generalidades", "La 'dialectología social' se centra en la variación de la lengua según el grupo social del hablante. (Verdadero/Falso)", "verdadero"),
        81: ("Léxico", "La palabra 'paisa' en Colombia se refiere a una persona de la región andina. (Verdadero/Falso)", "verdadero"),
        82: ("Fonética", "La omisión de la 'd' al final de sílaba en palabras como 'ciudad' es un rasgo fonético. (Verdadero/Falso)", "verdadero"),
        83: ("Léxico", "En el español de Costa Rica, 'mae' es un término coloquial para 'amigo' o 'tipo'. (Verdadero/Falso)", "verdadero"),
        84: ("Fonética", "La 'ch' se pronuncia más suave en los dialectos caribeños que en otros. (Verdadero/Falso)", "falso"),
        85: ("Morfosintaxis", "El uso de la doble negación (ej. 'No voy a hacer nada') es un rasgo de algunos dialectos. (Verdadero/Falso)", "verdadero"),
        86: ("Léxico", "¿'Puro' en el español de México significa 'muy' o 'realmente'? (Sí/No)", "sí"),
        87: ("Fonética", "El ensordecimiento de la 'd' final en palabras como 'libertad' es un rasgo de la variación dialectal. (Verdadero/Falso)", "verdadero"),
        88: ("Léxico", "La palabra 'chaval' (niño) es típica del español de: (a) Argentina, (b) España, (c) México.", "b"),
        89: ("Generalidades", "La dialectología se centra en la sincronía de una lengua. (Verdadero/Falso)", "verdadero"),
        90: ("Léxico", "¿En el español de España, 'guay' es sinónimo de 'cool'? (Sí/No)", "sí"),
        91: ("Fonética", "La aspiración de la 'j' es un rasgo de algunos dialectos andaluces. (Verdadero/Falso)", "verdadero"),
        92: ("Léxico", "La palabra 'jalar' se usa como sinónimo de 'tirar' en algunos dialectos americanos. (Verdadero/Falso)", "verdadero"),
        93: ("Generalidades", "La dialectología estudia las variaciones diacrónicas de una lengua. (Verdadero/Falso)", "falso"),
        94: ("Fonética", "¿La omisión de la 's' final en 'más' es un fenómeno de las zonas de las tierras altas de América? (Sí/No)", "no"),
        95: ("Léxico", "La palabra 'vosotros' se usa principalmente en el español de: (a) España, (b) México, (c) Colombia.", "a"),
        96: ("Generalidades", "La sociolingüística estudia la relación entre la lengua y la sociedad. (Verdadero/Falso)", "verdadero"),
        97: ("Léxico", "En el español de Colombia, 'berraquera' se refiere a una persona muy talentosa o valiente. (Verdadero/Falso)", "verdadero"),
        98: ("Fonética", "El debilitamiento de la 'r' final en los infinitivos es un rasgo del español andaluz. (Verdadero/Falso)", "verdadero"),
        99: ("Léxico", "¿La palabra 'papas' es un término común para 'patatas' en Latinoamérica? (Sí/No)", "sí"),
        100: ("Generalidades", "El español cuenta con un único y homogéneo dialecto en todo el mundo. (Verdadero/Falso)", "falso"),
    }

    print("¡Bienvenido al reto de Dialectología del Español!")
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
