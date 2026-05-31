# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Lingüística Española
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre morfología, sintaxis,
# semántica, historia del español y otros campos de la lingüística.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    exercises = {
        1: ("Morfología: Raíz", "Identifica la raíz de la palabra 'inalcanzable'.", "alcanz"),
        2: ("Morfología: Prefijo", "Identifica el prefijo en la palabra 'submarino'.", "sub"),
        3: ("Morfología: Sufijo", "Identifica el sufijo en la palabra 'amiguito'.", "ito"),
        4: ("Sintaxis: Sujeto", "En la oración 'El perro corrió muy rápido', ¿cuál es el sujeto?", "el perro"),
        5: ("Sintaxis: Predicado", "En la oración 'La casa tiene un jardín grande', ¿cuál es el predicado?", "tiene un jardín grande"),
        6: ("Sintaxis: Objeto Directo", "Identifica el objeto directo en 'María compró flores'.", "flores"),
        7: ("Semántica: Sinónimos", "Escribe un sinónimo para la palabra 'hermoso'.", "bello"),
        8: ("Semántica: Antónimos", "Escribe un antónimo para la palabra 'rápido'.", "lento"),
        9: ("Semántica: Homónimos", "Explica la diferencia entre 'banco' (entidad financiera) y 'banco' (asiento).", "banco"),
        10: ("Historia del Español", "¿De qué lengua indoeuropea proviene el español?", "latín"),
        11: ("Variación Dialectal", "Un 'bus' en Colombia es un 'camión' en México y una 'guagua' en Puerto Rico. ¿Cómo se llama este fenómeno?", "variación dialectal"),
        12: ("Morfología: Flexión", "Escribe la forma plural de 'lápiz'.", "lápices"),
        13: ("Morfología: Derivación", "Forma una palabra derivada de 'libro'.", "librería"),
        14: ("Sintaxis: Oración Simple", "Crea una oración simple con la palabra 'sol'.", "El sol brilla."),
        15: ("Sintaxis: Oración Compuesta", "Crea una oración compuesta que use la conjunción 'y'.", "Juan corre y María camina."),
        16: ("Pragmática", "Cuando dices '¡Qué frío hace aquí!', y no buscas una respuesta, ¿qué tipo de acto de habla es?", "expresivo"),
        17: ("Gramática", "Define la gramática.", "el estudio de la estructura del lenguaje"),
        18: ("Lexicología", "Define la lexicología.", "el estudio del léxico de una lengua"),
        19: ("Morfología: Morfema", "¿Cuál es la unidad mínima de significado en la morfología?", "morfema"),
        20: ("Sintaxis: Frase Nominal", "En la frase 'mi viejo amigo', ¿cuál es el núcleo?", "amigo"),
        21: ("Semántica: Polisemia", "La palabra 'cresta' tiene varios significados. Menciona uno.", "parte superior de una ola"),
        22: ("Historia del Español", "¿Cómo se llamaban los dialectos romances que dieron origen al español?", "dialectos castellanos"),
        23: ("Sociolingüística", "¿Qué estudia la sociolingüística?", "la relación entre lengua y sociedad"),
        24: ("Pragmática: Deixis", "En la oración 'Ven aquí ahora', identifica un deíctico de lugar.", "aquí"),
        25: ("Morfología: Morfemas Derivativos", "El morfema '-ción' en 'canción' es un morfema: (a) flexivo, (b) derivativo.", "b"),
        26: ("Sintaxis: Complemento del Nombre", "En 'la casa de mi tía', ¿qué es 'de mi tía'?", "complemento del nombre"),
        27: ("Sintaxis: Cláusula", "Define qué es una cláusula.", "una unidad sintáctica con verbo y sujeto"),
        28: ("Semántica: Connotación", "La palabra 'cerdo' puede tener una connotación negativa. ¿Cuál es?", "persona sucia o grosera"),
        29: ("Historia del Español: Arabismos", "Menciona una palabra del español que provenga del árabe.", "almohada"),
        30: ("Variación Dialectal: Fonética", "La aspiración de la /s/ al final de sílaba es común en dialectos de: (a) España, (b) el Caribe, (c) el cono sur.", "b"),
        31: ("Morfología: Composición", "La palabra 'paraguas' se forma por la composición de dos palabras. ¿Cuáles son?", "para y aguas"),
        32: ("Sintaxis: Complemento Circunstancial", "En 'Fui al cine ayer', ¿cuál es el complemento circunstancial de tiempo?", "ayer"),
        33: ("Lexicología: Neologismo", "Define 'neologismo'.", "una palabra nueva en una lengua"),
        34: ("Semántica: Campo Semántico", "Menciona tres palabras del campo semántico de 'música'.", "guitarra, piano, canción"),
        35: ("Historia del Español", "¿Qué fue el 'Siglo de Oro' de la literatura española?", "un periodo de florecimiento"),
        36: ("Tipología Lingüística", "El español es una lengua: (a) aislante, (b) aglutinante, (c) flexiva.", "c"),
        37: ("Morfología: Alomorfos", "Los morfemas 'pode-' y 'pud-' en 'poder' y 'pude' son: (a) prefijos, (b) alomorfos.", "b"),
        38: ("Sintaxis: Verbo", "En 'Yo como una manzana', ¿cuál es el verbo?", "como"),
        39: ("Pragmática: Implicatura", "Si alguien dice 'La puerta está abierta' y tú la cierras, ¿qué inferiste?", "que la cerraras"),
        40: ("Semántica: Homófonos", "Explica la diferencia entre 'hola' y 'ola'.", "sonido igual, significado diferente"),
        41: ("Historia del Español: Latinismos", "Menciona una palabra del español que se tome directamente del latín.", "currículum"),
        42: ("Sociolingüística: Sociolecto", "¿Cómo se llama la variedad de la lengua usada por un grupo social?", "sociolecto"),
        43: ("Morfología: Palabras Derivadas", "Forma una palabra derivada de 'dulce'.", "dulzura"),
        44: ("Sintaxis: Predicado Nominal", "En la oración 'La mesa es grande', ¿qué tipo de predicado es?", "nominal"),
        45: ("Semántica: Denotación", "Define la denotación de una palabra.", "su significado literal"),
        46: ("Historia del Español: Préstamos", "La palabra 'internet' es un préstamo de: (a) el francés, (b) el inglés.", "b"),
        47: ("Morfología: Afijos", "Los prefijos y sufijos son tipos de: (a) raíces, (b) afijos.", "b"),
        48: ("Sintaxis: Complemento Indirecto", "Identifica el objeto indirecto en 'Le di un regalo a mi mamá'.", "a mi mamá"),
        49: ("Semántica: Sinonimia Parcial", "Explica la diferencia entre 'coche' y 'automóvil'.", "son sinónimos pero con diferente uso"),
        50: ("Historia del Español", "¿Cuál fue la primera obra literaria escrita en español?", "el Cantar de mio Cid"),
        51: ("Morfología: Morfema Cero", "En la palabra 'pez', ¿hay algún morfema de plural? (a) sí, (b) no.", "b"),
        52: ("Sintaxis: Complemento de Régimen", "En 'El libro trata de un mago', ¿qué es 'de un mago'?", "complemento de régimen"),
        53: ("Semántica: Antonimia Gradual", "Escribe un antónimo gradual para 'caliente'.", "tibio"),
        54: ("Historia del Español", "¿Qué fue la 'diglosia' en el latín de la Edad Media?", "la coexistencia de latín culto y vulgar"),
        55: ("Morfología: Palabras Compuestas", "Menciona una palabra compuesta que no sea 'paraguas'.", "telaraña"),
        56: ("Sintaxis: Voz Pasiva", "Convierte la oración 'El niño come el pastel' a voz pasiva.", "el pastel es comido por el niño"),
        57: ("Semántica: Hiperónimo", "El hiperónimo de 'manzana' y 'pera' es: (a) verdura, (b) fruta, (c) alimento.", "b"),
        58: ("Semántica: Hipónimo", "El hipónimo de 'flor' es: (a) planta, (b) rosa, (c) hoja.", "b"),
        59: ("Historia del Español: Mozárabe", "¿Cómo se llamaba la lengua romance hablada en Al-Ándalus?", "mozárabe"),
        60: ("Morfología: Familia de Palabras", "Menciona tres palabras de la familia de 'pan'.", "panadería, panadero, panecillo"),
        61: ("Sintaxis: Oración Impersonal", "Escribe una oración impersonal.", "Hay muchos carros."),
        62: ("Semántica: Antonimia Complementaria", "Escribe un par de antónimos complementarios.", "vivo y muerto"),
        63: ("Historia del Español", "¿Qué pueblo germano influyó en el español medieval?", "visigodos"),
        64: ("Sintaxis: Cláusula Subordinada", "En 'Pienso que es una buena idea', ¿cuál es la cláusula subordinada?", "que es una buena idea"),
        65: ("Morfología: Raíz y Afijos", "Divide la palabra 'desordenado' en raíz, prefijo y sufijo.", "prefijo: des, raíz: orden, sufijo: ado"),
        66: ("Semántica: Ambigüedad", "La oración 'Vi a Juan con el telescopio' es ambigua. Explica por qué.", "no se sabe quién tiene el telescopio"),
        67: ("Historia del Español: Síncopa", "El paso de 'populu' (latín) a 'pueblo' es un caso de: (a) síncopa, (b) metatesis.", "a"),
        68: ("Sintaxis: Adjetivo", "En 'El carro rojo', ¿cuál es el adjetivo?", "rojo"),
        69: ("Morfología: Sustantivos Derivados", "Menciona dos sustantivos derivados de verbos.", "lectura, escritura"),
        70: ("Historia del Español: Diptongación", "El paso de 'nova' (latín) a 'nueva' es un caso de: (a) diptongación, (b) hiato.", "a"),
        71: ("Sintaxis: Artículo", "En 'un árbol', ¿qué es 'un'?", "artículo"),
        72: ("Semántica: Metáfora", "Explica la metáfora en la oración 'Sus ojos son dos luceros'.", "los ojos son brillantes"),
        73: ("Historia del Español: Leísmo", "El leísmo es el uso de 'le' por 'lo'. ¿Es un fenómeno: (a) normativo, (b) dialectal?", "b"),
        74: ("Morfología: Morfemas Flexivos", "Los morfemas que indican número y género son: (a) derivativos, (b) flexivos.", "b"),
        75: ("Sintaxis: Adverbio", "En 'camina lentamente', ¿cuál es el adverbio?", "lentamente"),
        76: ("Historia del Español: Fonema 'h'", "La 'h' inicial del español proviene de la 'f' del latín. ¿Verdadero o falso?", "verdadero"),
        77: ("Semántica: Eufemismo", "La palabra 'tercera edad' es un eufemismo para: (a) viejo, (b) joven.", "a"),
        78: ("Sintaxis: Voz Activa", "Convierte la oración 'El libro es leído por Juan' a voz activa.", "Juan lee el libro"),
        79: ("Morfología: Composición y Derivación", "La palabra 'sacapuntas' es un caso de: (a) composición, (b) derivación.", "a"),
        80: ("Semántica: Sinestesia", "La expresión 'un sonido dulce' es un ejemplo de: (a) hipérbole, (b) sinestesia.", "b"),
        81: ("Historia del Español", "La 'j' y la 'x' se pronunciaban de forma diferente en el español antiguo. ¿Qué fonema es hoy la 'x'?", "jota"),
        82: ("Sintaxis: Complemento Directo", "En 'Vi a mi hermano', el complemento directo es: (a) a mi hermano, (b) mi hermano.", "a"),
        83: ("Semántica: Antonimia Inversa", "Escribe un par de antónimos inversos.", "comprar y vender"),
        84: ("Historia del Español", "La evolución del español ocurrió entre los siglos: (a) V-VIII, (b) VIII-X, (c) X-XV.", "c"),
        85: ("Morfología: Palabras Compuestas", "Menciona una palabra compuesta que use 'auto'.", "autobiografía"),
        86: ("Sintaxis: Verbo Copulativo", "El verbo 'ser' en la oración 'Ella es inteligente' es: (a) copulativo, (b) predicativo.", "a"),
        87: ("Semántica: Paronimia", "Las palabras 'especie' y 'especia' son un ejemplo de: (a) paronimia, (b) homonimia.", "a"),
        88: ("Historia del Español", "El 'Libro de buen amor' de Juan Ruiz es una obra del: (a) siglo XIII, (b) siglo XIV, (c) siglo XV.", "b"),
        89: ("Sintaxis: Atributo", "En 'Ella es inteligente', ¿qué es 'inteligente'?", "atributo"),
        90: ("Morfología: Sufijos Apreciativos", "El sufijo '-ón' en 'cajón' es: (a) aumentativo, (b) diminutivo.", "a"),
        91: ("Historia del Español: Fonema 'v'", "La 'v' y la 'b' se pronuncian igual en español. ¿A qué se debe esto?", "betacismo"),
        92: ("Semántica: Metonimia", "La metonimia en la oración 'Se comió dos platos' es: (a) el plato, (b) la comida.", "a"),
        93: ("Sintaxis: Conjunción", "En 'No sé si iré', ¿qué palabra es la conjunción?", "si"),
        94: ("Morfología: Verbos Regulares", "Menciona un verbo regular en español.", "cantar"),
        95: ("Semántica: Denotación y Connotación", "La denotación de 'zorro' es un animal, pero la connotación puede ser: (a) inteligente, (b) astuto, (c) ambos.", "b"),
        96: ("Historia del Español: Voseo", "El voseo es el uso de 'vos' como pronombre de segunda persona. ¿En qué región se usa comúnmente?", "américa latina"),
        97: ("Sintaxis: Preposición", "En 'el perro de la casa', ¿qué palabra es la preposición?", "de"),
        98: ("Morfología: Sustantivos Colectivos", "La palabra 'ejército' es un sustantivo: (a) abstracto, (b) colectivo.", "b"),
        99: ("Semántica: Símil", "La expresión 'fuerte como un roble' es un ejemplo de: (a) hipérbole, (b) símil.", "b"),
        100: ("Historia del Español", "¿Cómo se llama la rama de la lingüística que estudia los cambios del español a través del tiempo?", "lingüística histórica"),
    }

    print("¡Bienvenido al reto de lingüística española, por el Instituto Caro y Cuervo!")
    print("-------------------------------------------------------------------------")
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
