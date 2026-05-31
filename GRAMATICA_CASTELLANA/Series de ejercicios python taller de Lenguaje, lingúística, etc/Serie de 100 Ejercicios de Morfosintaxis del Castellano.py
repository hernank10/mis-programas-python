# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Morfosintaxis del Castellano
# Inspirado en las obras del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios que combinan los conceptos de morfología
# (estructura de las palabras) y sintaxis (función en la oración).

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de morfosintaxis
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Sujeto y Morfología", "En 'Los estudiantes inteligentes aprenden', identifique el lexema y la función sintáctica de la palabra 'estudiantes'. (a) lexema: estudi-; función: sujeto, (b) lexema: estudiantes; función: predicado, (c) lexema: estudi; función: objeto directo", "a"),
        2: ("Predicado y Morfología", "En 'Ella compró una casa grande', ¿cuál es el núcleo del predicado y qué tipo de morfema flexivo tiene? (a) núcleo: compró; morfema: de persona, (b) núcleo: casa; morfema: de género, (c) núcleo: grande; morfema: de número", "a"),
        3: ("Comp. Directo y Formación", "Analice 'sacacorchos' en la oración 'Usé el sacacorchos'. ¿Qué tipo de formación morfológica tiene y qué función sintáctica cumple? (a) composición; objeto directo, (b) derivación; sujeto, (c) composición; complemento circunstancial", "a"),
        4: ("Atributo y Derivación", "En 'La niña es hermosa', la palabra 'hermosa' es un atributo. ¿Cuál es el sufijo derivativo que forma el adjetivo? (a) -a, (b) -sa, (c) -osa", "c"),
        5: ("Comp. de Régimen y Morfemas", "En la frase 'Se acordó de su amiga', ¿cuál es el núcleo del complemento de régimen y qué tipo de morfema tiene la palabra 'amiga'? (a) núcleo: amiga; morfema: de género, (b) núcleo: de; morfema: de número, (c) núcleo: se; morfema: de persona", "a"),
        6: ("Sujeto y Composición", "En 'El paraguas protege de la lluvia', ¿cómo se forma 'paraguas' y qué función sintáctica tiene en la oración? (a) composición; sujeto, (b) derivación; objeto directo, (c) parasíntesis; sujeto", "a"),
        7: ("Comp. Indirecto y Derivación", "En 'Le dio un libro al librero', identifique la función sintáctica de 'al librero' y el sufijo derivativo de 'librero'. (a) comp. indirecto; sufijo: -ero, (b) comp. directo; sufijo: -o, (c) comp. circunstancial; sufijo: -er", "a"),
        8: ("Oración y Flexión", "En la oración 'Corrimos mucho ayer', el verbo 'corrimos' indica flexión de persona y número. ¿Qué función sintáctica cumple el sujeto omitido? (a) 1ra persona del plural; sujeto, (b) 3ra persona del plural; sujeto, (c) 1ra persona del singular; sujeto", "a"),
        9: ("Sintagmas y Prefijos", "En 'El coche es superveloz', identifique el prefijo en 'superveloz' y la función sintáctica del Sintagma Adjetival. (a) prefijo: super-; atributo, (b) prefijo: super-; complemento predicativo, (c) prefijo: veloz; objeto directo", "a"),
        10: ("Oración Pasiva y Flexión", "En 'La casa fue construida por obreros', ¿qué tipo de flexión verbal tiene 'fue construida' y qué función cumple 'por obreros'? (a) de persona y número; comp. agente, (b) de modo; comp. indirecto, (c) de tiempo y aspecto; comp. circunstancial", "a"),
        11: ("Comp. Circunstancial y Sufijos", "En 'Viajó lentamente', ¿cuál es el sufijo derivativo de 'lentamente' y qué función sintáctica cumple? (a) -mente; comp. circunstancial de modo, (b) -te; comp. circunstancial de tiempo, (c) -a; comp. circunstancial de lugar", "a"),
        12: ("Sujeto y Familia de palabras", "En 'La carpintería abrió hoy', ¿de qué palabra se deriva 'carpintería' y qué función sintáctica tiene? (a) de 'carpintero'; sujeto, (b) de 'carpa'; objeto directo, (c) de 'pintura'; sujeto", "a"),
        13: ("Predicado y Parasíntesis", "En 'Se apoderó de todo', la palabra 'apoderó' es parasintética. ¿Qué función sintáctica cumple en la oración? (a) núcleo del predicado, (b) complemento de régimen, (c) sujeto", "a"),
        14: ("Atributo y Flexión de Género", "En 'Las puertas están abiertas', la palabra 'abiertas' es un atributo. ¿Qué morfema flexivo de género tiene? (a) -a, (b) -s, (c) -as", "c"),
        15: ("Oración y Morfología", "La oración 'Hoy es un día muy soleado' contiene una palabra con un sufijo que indica abundancia. ¿Qué función sintáctica cumple la frase 'muy soleado'? (a) comp. circunstancial; (b) atributo; (c) objeto directo", "b"),
        16: ("Sujeto y Morfología", "En 'El buen hombre lo hizo', identifique el morfema flexivo de número en 'hombre' y la función sintáctica de 'El buen hombre'. (a) -s; sujeto, (b) no tiene; sujeto, (c) -e; predicado", "b"),
        17: ("Sintagmas y Morfología", "En 'Compró una hermosa bicicleta', ¿qué tipo de morfemas flexivos tiene la palabra 'hermosa' y a qué sintagma pertenece? (a) género y número; Sintagma Nominal, (b) tiempo y persona; Sintagma Verbal, (c) género; Sintagma Adjetival", "a"),
        18: ("Complementos y Prefijos", "En 'La acción fue ilegal', ¿cuál es el prefijo de 'ilegal' y la función sintáctica del Sintagma Adjetival? (a) i-; objeto directo, (b) il-; atributo, (c) in-; comp. circunstancial", "b"),
        19: ("Verbo y Flexión", "En 'Ellos cantaban', ¿qué tipo de flexión de tiempo tiene el verbo 'cantaban'? ¿Qué función cumple en la oración? (a) pretérito imperfecto; núcleo del predicado, (b) pretérito perfecto; sujeto, (c) presente; núcleo del predicado", "a"),
        20: ("Sintagmas y Morfología", "En 'muy lejos de aquí', ¿qué tipo de sintagma es 'lejos de aquí' y cuál es el núcleo morfológico de 'lejos'? (a) Sintagma Preposicional; un adverbio, (b) Sintagma Adverbial; un adverbio, (c) Sintagma Nominal; una preposición", "b"),
        21: ("Sujeto", "¿Qué oración tiene un sujeto compuesto? (a) 'Juan y María comen.', (b) 'Juan come con María.', (c) 'El niño come una manzana.'", "a"),
        22: ("Predicado", "¿Qué oración tiene un predicado verbal? (a) 'Pedro es alto.', (b) 'El coche está nuevo.', (c) 'El coche corre rápido.'", "c"),
        23: ("Objeto Directo", "En 'El pintor pintó el cuadro', ¿cuál es el objeto directo? (a) El pintor, (b) pintó, (c) el cuadro", "c"),
        24: ("Objeto Indirecto", "En 'La profesora da libros a los alumnos', ¿cuál es el objeto indirecto? (a) La profesora, (b) libros, (c) a los alumnos", "c"),
        25: ("Comp. Circunstancial", "En 'Salimos a las cinco', 'a las cinco' es un complemento circunstancial de: (a) modo, (b) tiempo, (c) lugar.", "b"),
        26: ("Atributo", "¿Qué oración contiene un atributo? (a) 'El niño come galletas.', (b) 'Mi padre es médico.', (c) 'El gato duerme.'", "b"),
        27: ("Comp. de Régimen", "¿Qué oración tiene un complemento de régimen? (a) 'Se fía de su amigo.', (b) 'Comió con gusto.', (c) 'Escribió una carta.'", "a"),
        28: ("Complemento Agente", "¿Qué oración tiene un complemento agente? (a) 'La torta fue hecha por mi mamá.', (b) 'El niño juega con el perro.', (c) 'Compró un pastel.'", "a"),
        29: ("Oración Pasiva", "¿Qué oración está en voz pasiva? (a) 'El perro mordió al cartero.', (b) 'El cartero fue mordido por el perro.', (c) 'El cartero caminaba rápido.'", "b"),
        30: ("Sujeto Omitido", "En 'Fuimos al cine', el sujeto omitido es: (a) yo, (b) tú, (c) nosotros.", "c"),
        31: ("Oración Coordinada", "¿Qué oración es coordinada? (a) 'Voy al cine si puedo.', (b) 'Leo y escribo.', (c) 'Dijo que vendría.'", "b"),
        32: ("Oración Subordinada", "¿Qué oración es subordinada? (a) 'Jugué y gané.', (b) 'Me gusta que leas.', (c) 'Estudié mucho.'", "b"),
        33: ("Sub. Sustantiva", "En 'Deseo que vengas', 'que vengas' es una subordinada: (a) sustantiva de objeto directo, (b) adjetiva, (c) adverbial", "a"),
        34: ("Sub. Adjetiva", "En 'La casa que compraste es bonita', 'que compraste' es una subordinada: (a) sustantiva, (b) adjetiva, (c) adverbial.", "b"),
        35: ("Sub. Adverbial", "En 'Iremos donde tú digas', 'donde tú digas' es una subordinada: (a) sustantiva, (b) adjetiva, (c) adverbial.", "c"),
        36: ("Lexema", "¿Cuál es el lexema de 'niñas'? (a) niñ-, (b) niñ-a, (c) niña-s", "a"),
        37: ("Morfema Flexivo", "En 'perros', el morfema flexivo de número es: (a) -o, (b) -s, (c) -os", "b"),
        38: ("Morfema Derivativo", "En 'librero', el sufijo '-ero' es: (a) flexivo, (b) derivativo, (c) léxico", "b"),
        39: ("Composición", "La palabra 'abrelatas' se forma por: (a) derivación, (b) composición, (c) parasíntesis", "b"),
        40: ("Derivación", "La palabra 'dulzura' se forma por: (a) derivación, (b) composición, (c) parasíntesis", "a"),
        41: ("Parasíntesis", "La palabra 'envejecer' se forma por: (a) derivación, (b) composición, (c) parasíntesis", "c"),
        42: ("Prefijo", "El prefijo 'im-' en 'imposible' es de: (a) negación, (b) lugar, (c) tiempo", "a"),
        43: ("Sufijo", "El sufijo '-mente' en 'rápidamente' forma un: (a) adjetivo, (b) adverbio, (c) sustantivo", "b"),
        44: ("Flexión Verbal", "En 'comíamos', ¿cuál es el morfema de tiempo y modo? (a) -mos, (b) -íamos, (c) -a", "b"),
        45: ("Función Sintáctica", "En 'Los estudiantes aprobaron el examen', ¿qué función cumple 'el examen'? (a) sujeto, (b) objeto directo, (c) objeto indirecto", "b"),
        46: ("Sintagmas", "En 'El coche rojo', ¿qué tipo de sintagma es 'rojo'? (a) Sintagma Adjetival, (b) Sintagma Nominal, (c) Sintagma Adverbial", "a"),
        47: ("Verbo y Morfemas", "En 'Estudiábamos', el verbo tiene un morfema flexivo de: (a) persona, (b) persona y número, (c) persona, número, tiempo, modo", "c"),
        48: ("Sintagmas y Formación", "En 'Mi primo es pelirrojo', ¿cómo se forma 'pelirrojo' y a qué sintagma pertenece? (a) parasíntesis; Sintagma Adjetival, (b) composición; Sintagma Adjetival, (c) derivación; Sintagma Nominal", "b"),
        49: ("Comp. Predicativo", "En 'Los chicos llegaron cansados', la palabra 'cansados' funciona como: (a) atributo, (b) complemento predicativo, (c) complemento circunstancial", "b"),
        50: ("Sintaxis", "Una oración unimembre es aquella que: (a) no tiene sujeto, (b) no tiene predicado, (c) no se puede dividir en sujeto y predicado", "c"),
        51: ("Composición", "¿'Bocacalle' es una palabra compuesta por: (a) sustantivo+verbo, (b) sustantivo+sustantivo, (c) verbo+sustantivo", "b"),
        52: ("Sintagma y Morfema", "En 'Muy cerca de ti', ¿qué tipo de sintagma es 'muy' y qué tipo de morfema es 'cerca'? (a) adverbial; flexivo, (b) adverbial; léxico, (c) adjetival; derivativo", "b"),
        53: ("Voz Pasiva y Morfología", "En 'El libro fue leído', 'leído' es un: (a) verbo; (b) participio, (c) adjetivo", "b"),
        54: ("Objeto Directo", "En 'La vimos ayer', 'La' es: (a) sujeto, (b) objeto directo, (c) objeto indirecto", "b"),
        55: ("Objeto Indirecto", "En 'Le dimos el regalo', 'Le' es: (a) sujeto, (b) objeto directo, (c) objeto indirecto", "c"),
        56: ("Comp. de Régimen", "El complemento de régimen va siempre: (a) sin preposición, (b) con preposición, (c) con un adverbio", "b"),
        57: ("Comp. Circunstancial", "En 'Fue a pie', 'a pie' es un complemento de: (a) lugar, (b) modo, (c) tiempo", "b"),
        58: ("Sujeto Léxico", "El 'sujeto léxico' está: (a) omitido, (b) expreso, (c) implícito", "b"),
        59: ("Atributo", "El atributo se puede sustituir por el pronombre: (a) 'lo', (b) 'la', (c) 'le'", "a"),
        60: ("Oración", "¿Qué oración es copulativa? (a) 'El niño juega.', (b) 'Mi mamá es alta.', (c) 'El gato duerme.'", "b"),
        61: ("Sintagmas y Morfemas", "En 'La casa blanquísima', ¿qué tipo de sufijo tiene 'blanquísima' y qué sintagma es 'blanquísima'? (a) flexivo; adjetival, (b) derivativo; adjetival, (c) léxico; nominal", "b"),
        62: ("Sintaxis y Morfología", "En 'El coche corre rápido', ¿qué función cumple 'rápido' y qué tipo de palabra es? (a) objeto directo; sustantivo, (b) complemento predicativo; adjetivo, (c) complemento circunstancial; adverbio", "b"),
        63: ("Flexión y Función", "En 'Ellos comen frutas', ¿qué indican los morfemas flexivos del verbo 'comen' y qué función cumple 'Ellos'? (a) 3ra persona y plural; sujeto, (b) 2da persona y singular; sujeto, (c) 3ra persona y plural; objeto directo", "a"),
        64: ("Derivación y Sintaxis", "En 'El niño es un golazo', ¿cómo se forma 'golazo' y qué función tiene en la oración? (a) derivación; atributo, (b) composición; objeto directo, (c) parasíntesis; sujeto", "a"),
        65: ("Composición y Sintagmas", "En 'Mi tío es un guardabosques', ¿qué tipo de sintagma es 'un guardabosques' y cómo se forma la palabra? (a) SN; composición, (b) SV; derivación, (c) SP; composición", "a"),
        66: ("Sujeto y Flexión", "En 'Las aves vuelan', el sujeto es 'Las aves'. ¿Qué morfemas flexivos de género y número tiene el artículo 'Las'? (a) género y número, (b) solo número, (c) solo género", "a"),
        67: ("Sintaxis y Prefijos", "En 'Deshice el nudo', el prefijo 'des-' indica 'negación'. ¿Qué función cumple 'el nudo'? (a) sujeto, (b) objeto directo, (c) objeto indirecto", "b"),
        68: ("Objeto Directo y Morfología", "En 'Leo un libro', ¿cuál es el objeto directo y qué tipo de palabra es 'libro'? (a) Leo; verbo, (b) un libro; sustantivo, (c) un libro; adjetivo", "b"),
        69: ("Objeto Indirecto y Prefijos", "En 'Le presté un libro a la exalumna', ¿cuál es el objeto indirecto y el prefijo de 'exalumna'? (a) a la exalumna; ex-, (b) un libro; a, (c) le; ex-", "a"),
        70: ("Comp. Circunstancial y Derivación", "En 'Estudió por la tarde para aprobar', ¿qué función cumple 'para aprobar' y cómo se forma 'aprobar'? (a) comp. de fin; derivación, (b) comp. de causa; composición, (c) objeto directo; parasíntesis", "a"),
        71: ("Sintagma y Flexión", "En 'La blusa azul', 'blusa' tiene morfemas de género y número. ¿A qué sintagma pertenece? (a) Sintagma Adjetival, (b) Sintagma Verbal, (c) Sintagma Nominal", "c"),
        72: ("Sintagmas y Derivación", "En 'El camino era pedregoso', ¿qué tipo de sintagma es 'pedregoso' y cómo se forma morfológicamente? (a) Sintagma Nominal; composición, (b) Sintagma Adjetival; derivación, (c) Sintagma Preposicional; parasíntesis", "b"),
        73: ("Comp. de Régimen y Morfología", "En 'Nos arrepentimos de la decisión', ¿cuál es el verbo que rige el complemento de régimen y qué tipo de palabra es 'decisión'? (a) arrepentimos; sustantivo, (b) nos; pronombre, (c) la; artículo", "a"),
        74: ("Flexión y Predicado", "En 'Ellas son felices', 'son' es el verbo. ¿Qué morfemas flexivos tiene y qué tipo de predicado hay? (a) persona y número; nominal, (b) tiempo y modo; verbal, (c) persona; copulativo", "a"),
        75: ("Voz Pasiva y Morfología", "En 'La canción fue cantada', ¿qué función cumple 'cantada' y qué tipo de palabra es? (a) verbo; verbo, (b) complemento; sustantivo, (c) núcleo del predicado; participio", "c"),
        76: ("Sintagmas y Composición", "En 'La casa tiene un tragaluz', ¿qué tipo de sintagma es 'un tragaluz' y qué tipo de formación morfológica tiene 'tragaluz'? (a) SN; composición, (b) SA; derivación, (c) SV; parasíntesis", "a"),
        77: ("Parasíntesis y Sintaxis", "En 'El barco se hizo a-terrizar', ¿cómo se forma 'aterrizar' y qué función cumple el sintagma verbal? (a) composición; predicado, (b) derivación; sujeto, (c) parasíntesis; predicado", "c"),
        78: ("Sintagmas y Derivación", "En 'Es un perro amoroso', ¿cómo se forma 'amoroso' y a qué sintagma pertenece? (a) derivación; SN, (b) derivación; SA, (c) composición; SV", "b"),
        79: ("Coordinadas y Flexión", "En 'Estudié y aprendí', ¿qué tipo de oraciones son y qué morfema flexivo comparten los verbos? (a) subordinadas; de persona, (b) coordinadas; de persona y número, (c) coordinadas; de tiempo", "b"),
        80: ("Lexema y Sintaxis", "En 'La flor florecía', ¿cuál es el lexema de 'florecía' y qué función sintáctica cumple? (a) flor-; predicado, (b) flor-; sujeto, (c) flor; complemento", "a"),
        81: ("Morfología y Sintaxis", "En 'La superestrella cantó', ¿qué es 'super-' y qué función cumple 'La superestrella'? (a) sufijo; objeto directo, (b) prefijo; sujeto, (c) prefijo; predicado", "b"),
        82: ("Sintagmas y Derivación", "En 'La limpieza de la casa', ¿qué sintagma es 'de la casa' y qué tipo de morfema tiene 'limpieza'? (a) SN; derivativo, (b) SP; derivativo, (c) SV; flexivo", "b"),
        83: ("Comp. Circunstancial y Composición", "En 'Me desperté al amanecer', ¿qué función cumple 'al amanecer' y cómo se forma la palabra? (a) comp. de tiempo; parasíntesis, (b) comp. de lugar; composición, (c) comp. de modo; derivación", "a"),
        84: ("Oración y Prefijos", "En 'El examen es irregular', ¿cuál es el prefijo de 'irregular' y qué tipo de oración es? (a) ir-; predicativa, (b) irre-; copulativa, (c) ir-; copulativa", "c"),
        85: ("Comp. de Régimen y Morfología", "En 'Se quejó de todo', ¿qué función cumple 'de todo' y qué tipo de morfema tiene la palabra 'quejó'? (a) objeto directo; flexivo, (b) comp. de régimen; flexivo, (c) comp. circunstancial; derivativo", "b"),
        86: ("Sujeto y Parasíntesis", "En 'El afortunado ganó', ¿qué tipo de palabra es 'afortunado' y qué función sintáctica cumple en la oración? (a) derivado; sujeto, (b) parasintética; sujeto, (c) compuesto; predicado", "b"),
        87: ("Oración y Morfología", "En 'Vienen deprisa', ¿es una palabra compuesta 'deprisa' y qué tipo de oración es? (a) sí; unimembre, (b) no; bimembre, (c) no; unimembre", "b"),
        88: ("Sintagmas y Flexión", "En 'El coche nuevo', ¿qué morfemas flexivos tiene 'nuevo' y a qué sintagma pertenece? (a) género y número; SN, (b) género; SA, (c) género y número; SA", "c"),
        89: ("Predicado y Composición", "En 'El ciempiés se movía', ¿cómo se forma 'ciempiés' y qué función cumple 'se movía'? (a) composición; predicado verbal, (b) derivación; predicado nominal, (c) parasíntesis; sujeto", "a"),
        90: ("Objeto Directo y Derivación", "En 'Leí la novelita', ¿cuál es el objeto directo y cómo se forma la palabra 'novelita'? (a) leí; derivación, (b) la novelita; derivación, (c) la novelita; composición", "b"),
        91: ("Atributo y Parasíntesis", "En 'La chica estaba empobrecida', ¿cómo se forma 'empobrecida' y qué función cumple en la oración? (a) derivación; atributo, (b) parasíntesis; atributo, (c) composición; objeto directo", "b"),
        92: ("Comp. Circunstancial y Flexión", "En 'Mi hermano canta alegremente', ¿qué función cumple 'alegremente' y qué tipo de flexión tiene 'canta'? (a) CC de modo; de persona y número, (b) CC de lugar; de tiempo, (c) OD; de modo", "a"),
        93: ("Oraciones Subordinadas y Morfología", "En 'El niño que lloraba se fue', ¿qué función cumple 'que lloraba' y qué tipo de morfema tiene el verbo? (a) sustantiva; flexivo, (b) adjetiva; flexivo, (c) adverbial; derivativo", "b"),
        94: ("Lexema y Flexión", "En 'Los perros corrían', identifique el lexema de 'perros' y el morfema flexivo de tiempo de 'corrían'. (a) perr-; corrían, (b) perro-; -rrían, (c) perr-; -ían", "c"),
        95: ("Sintagmas y Formación", "En 'Estaba muy triste', ¿qué tipo de sintagma es 'triste' y qué tipo de palabra es? (a) Sintagma Adjetival; derivativa, (b) Sintagma Adjetival; simple, (c) Sintagma Adverbial; simple", "b"),
        96: ("Objeto Indirecto y Morfología", "En 'Le escribí una carta', ¿cuál es el objeto indirecto y qué tipo de palabra es 'escribí'? (a) Le; simple, (b) una carta; compuesta, (c) Le; derivada", "a"),
        97: ("Sintaxis y Derivación", "En 'Llevaba una vida desordenada', ¿qué función cumple 'desordenada' y cómo se forma? (a) atributo; derivación, (b) complemento del nombre; derivación, (c) complemento circunstancial; composición", "b"),
        98: ("Comp. Agente y Morfología", "En 'La mesa fue limpiada por la limpiadora', ¿qué función cumple 'la limpiadora' y cómo se forma esa palabra? (a) sujeto; derivación, (b) complemento agente; derivación, (c) complemento agente; composición", "b"),
        99: ("Análisis Morfosintáctico", "En 'El cortauñas es nuevo', analice morfológicamente 'cortauñas' y sintácticamente 'El cortauñas'. (a) composición; sujeto, (b) derivación; objeto directo, (c) parasíntesis; sujeto", "a"),
        100: ("Repaso Final", "En 'Los estudiantes estudian mucho', ¿qué tipo de palabra es 'estudian' y qué función cumple? (a) simple; núcleo del predicado, (b) derivada; sujeto, (c) simple; complemento", "a"),
    }

    print("¡Bienvenido al reto de Morfosintaxis del Castellano!")
    print("-------------------------------------------------------------")
    print("Responda las preguntas o introduzca 'salir' para terminar.")

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
