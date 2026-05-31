# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Fonética y Fonología
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los sonidos del español,
# la acentuación, la fonética y la fonología.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    ejercicios = {
        1: ("Vocales Abiertas", "Identifica la vocal abierta: (a) i, (b) u, (c) a.", "c"),
        2: ("Vocales Cerradas", "Identifica la vocal cerrada: (a) o, (b) e, (c) i.", "c"),
        3: ("Clasificación de Consonantes", "El fonema /p/ es: (a) fricativo, (b) oclusivo, (c) nasal.", "b"),
        4: ("Punto de Articulación", "El fonema /s/ es: (a) labial, (b) alveolar, (c) velar.", "b"),
        5: ("Modo de Articulación", "El fonema /f/ es: (a) oclusivo, (b) fricativo, (c) vibrante.", "b"),
        6: ("Sonoridad", "El fonema /m/ es: (a) sordo, (b) sonoro.", "b"),
        7: ("Sílaba Tónica", "En la palabra 'computadora', ¿cuál es la sílaba tónica?", "do"),
        8: ("Palabras Agudas", "Una palabra aguda lleva la sílaba tónica en: (a) la última sílaba, (b) la penúltima, (c) la antepenúltima.", "a"),
        9: ("Palabras Graves", "Una palabra grave lleva la sílaba tónica en: (a) la última sílaba, (b) la penúltima, (c) la antepenúltima.", "b"),
        10: ("Palabras Esdrújulas", "Una palabra esdrújula lleva la sílaba tónica en: (a) la última sílaba, (b) la penúltima, (c) la antepenúltima.", "c"),
        11: ("Diptongo", "El diptongo es la unión de dos vocales en la misma sílaba. ¿Qué palabra contiene un diptongo?: (a) piano, (b) día, (c) país.", "a"),
        12: ("Hiato", "El hiato es la separación de dos vocales en sílabas distintas. ¿Qué palabra contiene un hiato?: (a) aire, (b) poeta, (c) fuerte.", "b"),
        13: ("Triptongo", "El triptongo es la unión de tres vocales en la misma sílaba. ¿Qué palabra contiene un triptongo?: (a) Paraguay, (b) feo, (c) cuento.", "a"),
        14: ("Sinalefa", "La sinalefa es el fenómeno que une la vocal final de una palabra y la inicial de la siguiente en la misma sílaba. ¿Qué ocurre con 'la uva'?", "se pronuncian en una sílaba"),
        15: ("Yeísmo", "El fenómeno por el que el fonema /ʎ/ (ll) y /ʝ/ (y) se pronuncian igual se llama:", "yeísmo"),
        16: ("Seseo", "El fenómeno por el que los fonemas /s/ y /θ/ (z, c) se pronuncian igual se llama:", "seseo"),
        17: ("Aspiración de /s/", "En la costa Caribe de Colombia, el fonema /s/ final de sílaba a menudo se aspira. ¿Cómo sonaría 'las casas'?", "la(h) casa(h)"),
        18: ("Fonema /x/", "El fonema /x/ (jota) en español es: (a) bilabial, (b) velar, (c) alveolar.", "b"),
        19: ("Consonantes Nasales", "Los fonemas nasales son: (a) /p/, /t/, /k/, (b) /m/, /n/, /ɲ/, (c) /s/, /f/, /x/.", "b"),
        20: ("Consonantes Líquidas", "Los fonemas líquidos son: (a) /l/ y /r/, (b) /b/ y /d/, (c) /t/ y /s/.", "a"),
        21: ("Asimilación", "Define qué es la asimilación fonética.", "cuando un sonido adquiere rasgos de otro"),
        22: ("Disimilación", "Define qué es la disimilación fonética.", "cuando un sonido pierde rasgos de otro"),
        23: ("Metátesis", "En el habla popular, a veces se invierten sonidos. ¿Cómo se llama este fenómeno?", "metátesis"),
        24: ("Fonema /r/", "El fonema /r/ (suave) es: (a) vibrante simple, (b) vibrante múltiple, (c) lateral.", "a"),
        25: ("Fonema /ɾ/", "El fonema /ɾ/ (múltiple) es: (a) vibrante simple, (b) vibrante múltiple, (c) lateral.", "b"),
        26: ("Acento Diacrítico", "La tilde que diferencia palabras idénticas se llama:", "diacrítica"),
        27: ("Sílaba Abierta", "Una sílaba abierta termina en: (a) consonante, (b) vocal.", "b"),
        28: ("Sílaba Cerrada", "Una sílaba cerrada termina en: (a) consonante, (b) vocal.", "a"),
        29: ("El fonema /tʃ/", "El fonema 'ch' es: (a) bilabial, (b) palatal, (c) dental.", "b"),
        30: ("El fonema /j/", "El fonema 'y' es: (a) oclusivo, (b) fricativo, (c) aproximante.", "c"),
        31: ("Diptongo Creciente", "En el diptongo 'ia', la vocal 'i' es: (a) tónica, (b) átona, (c) cerrada.", "c"),
        32: ("Diptongo Decreciente", "En el diptongo 'eu', la vocal 'u' es: (a) tónica, (b) átona, (c) cerrada.", "c"),
        33: ("Acento Ortográfico", "El acento escrito en 'canción' se llama:", "ortográfico"),
        34: ("Acento Prosódico", "En la palabra 'casa', el acento que se oye pero no se escribe es:", "prosódico"),
        35: ("Fonema vs. Grafema", "La unidad mínima de sonido es el fonema. ¿Cuál es la unidad mínima de escritura?", "grafema"),
        36: ("Transcribir 'carro'", "Transcribe fonéticamente la palabra 'carro' (sin símbolos especiales).", "ka-rr-o"),
        37: ("Transcribir 'perro'", "Transcribe fonéticamente la palabra 'perro' (sin símbolos especiales).", "pe-rr-o"),
        38: ("Transcribir 'queso'", "Transcribe fonéticamente la palabra 'queso' (sin símbolos especiales).", "ke-so"),
        39: ("Asimilación de /n/", "En 'un vaso', la /n/ se pronuncia como: (a) nasal, (b) bilabial, (c) alveolar.", "b"),
        40: ("Diptongo 'ui'", "La palabra 'cuidado' contiene un diptongo. ¿Qué tipo de diptongo es?", "ui"),
        41: ("Fenómenos Fonéticos", "Menciona un fenómeno fonético que ocurra en el habla rápida.", "elisión"),
        42: ("Sílabas Gramaticales", "Separa en sílabas la palabra 'paraguas'.", "pa-ra-guas"),
        43: ("Hiato 'eo'", "Separa en sílabas la palabra 'creo'.", "cre-o"),
        44: ("Diferencia de acento", "Explica la diferencia de acento entre 'tomo' (verbo) y 'tomó' (pasado).", "tomo es grave, tomó es aguda"),
        45: ("El fonema /ʎ/", "El fonema 'll' en español es: (a) lateral palatal, (b) fricativo, (c) oclusivo.", "a"),
        46: ("Apócope", "Explica qué es la apócope.", "la pérdida de un sonido o sílaba final"),
        47: ("Síncopa", "Explica qué es la síncopa.", "la pérdida de un sonido o sílaba en el interior de una palabra"),
        48: ("Prótesis", "Explica qué es la prótesis.", "la adición de un sonido o sílaba al inicio de una palabra"),
        49: ("Epéntesis", "Explica qué es la epéntesis.", "la adición de un sonido o sílaba en el interior de una palabra"),
        50: ("Variación regional", "La /s/ se pronuncia como una aspiración en: (a) México, (b) Colombia, (c) España.", "b"),
        51: ("Rasgos supra-segmentales", "Menciona un rasgo supra-segmental del español.", "entonación"),
        52: ("Vocalismo", "El estudio de las vocales se llama:", "vocalismo"),
        53: ("Consonantismo", "El estudio de las consonantes se llama:", "consonantismo"),
        54: ("Fonema /ɲ/", "El fonema 'ñ' en español es: (a) nasal palatal, (b) lateral, (c) oclusivo.", "a"),
        55: ("Minimal Pair", "Cambia un solo fonema para convertir 'casa' en 'cazo'.", "/s/ por /z/"),
        56: ("Vocal /a/", "La vocal 'a' es: (a) anterior, (b) central, (c) posterior.", "b"),
        57: ("Vocal /i/", "La vocal 'i' es: (a) anterior, (b) central, (c) posterior.", "a"),
        58: ("Vocal /u/", "La vocal 'u' es: (a) anterior, (b) central, (c) posterior.", "c"),
        59: ("Fonema /s/ al final", "En la frase 'estamos listos', el fonema /s/ final se pronuncia como una /z/ en contacto con /l/. ¿Cómo se llama este fenómeno?", "asimilación"),
        60: ("La vocal /e/", "La vocal 'e' es: (a) cerrada, (b) semicerrada, (c) abierta.", "b"),
        61: ("La vocal /o/", "La vocal 'o' es: (a) semicerrada, (b) semiabierta, (c) abierta.", "b"),
        62: ("Consonantes alveolares", "Los fonemas /l/, /r/, /ɾ/, /s/ son: (a) bilabiales, (b) alveolares, (c) velares.", "b"),
        63: ("Fonemas Bilabiales", "Los fonemas /p/, /b/, /m/ son: (a) alveolares, (b) bilabiales, (c) labiodentales.", "b"),
        64: ("Fonemas Labiodentales", "El fonema /f/ es: (a) velar, (b) dental, (c) labiodental.", "c"),
        65: ("Fonemas Dentales", "Los fonemas /t/, /d/ son: (a) alveolares, (b) palatales, (c) dentales.", "c"),
        66: ("Fonemas Palatales", "El fonema /ɲ/ es: (a) alveolar, (b) palatal, (c) velar.", "b"),
        67: ("Fonemas Velares", "Los fonemas /k/, /g/, /x/ son: (a) dentales, (b) palatales, (c) velares.", "c"),
        68: ("Acentuación de monosílabos", "La palabra 'fe' no lleva tilde. ¿Por qué?", "es un monosílabo"),
        69: ("Diferencia 'tu' y 'tú'", "La palabra 'tu' es un adjetivo posesivo y 'tú' es un pronombre personal. ¿Qué tipo de tilde llevan?", "diacrítica"),
        70: ("Separación 'baile'", "Separa en sílabas la palabra 'baile'.", "bai-le"),
        71: ("Sílabas de 'cielo'", "Separa en sílabas la palabra 'cielo'.", "cie-lo"),
        72: ("Fenómeno de 'desgracia'", "El fonema /s/ se pronuncia como /z/ antes de /g/. ¿Cómo se llama este fenómeno?", "asimilación"),
        73: ("Transcribir 'chuzo'", "Transcribe fonéticamente la palabra 'chuzo' (sin símbolos especiales).", "tʃu-so"),
        74: ("Transcribir 'calle'", "Transcribe fonéticamente la palabra 'calle' (sin símbolos especiales).", "ka-ʝe"),
        75: ("Hiato por vocal tónica", "La palabra 'maíz' contiene un hiato. ¿Por qué?", "la vocal débil 'i' es tónica"),
        76: ("El fonema /ʝ/", "El fonema /ʝ/ (y) es: (a) oclusivo, (b) fricativo, (c) africado.", "b"),
        77: ("Fonemas Africados", "El fonema /tʃ/ (ch) es: (a) oclusivo, (b) fricativo, (c) africado.", "c"),
        78: ("Variación 'v'", "En el español, el fonema de la 'v' es igual al de la 'b'. ¿Cómo se llama este fenómeno?", "betacismo"),
        79: ("Minimal Pair 2", "Cambia un solo fonema para convertir 'tierra' en 'perra'.", "/t/ por /p/"),
        80: ("Minimal Pair 3", "Cambia un solo fonema para convertir 'bola' en 'bota'.", "/l/ por /t/"),
        81: ("Monoptongo", "El fenómeno fonético por el cual un diptongo se pronuncia como una sola vocal se llama:", "monoptongación"),
        82: ("Fonema /k/", "El fonema /k/ es: (a) sordo, (b) sonoro.", "a"),
        83: ("Fonema /g/", "El fonema /g/ es: (a) sordo, (b) sonoro.", "b"),
        84: ("Acento en palabras compuestas", "¿Dónde recae el acento en 'veintidós'?", "dós"),
        85: ("Diéresis", "El signo diacrítico en 'pingüino' se llama:", "diéresis"),
        86: ("Fonemas y Sílabas", "¿Cuál es la relación entre fonemas y sílabas?", "un fonema puede formar una sílaba"),
        87: ("Acento enfático", "El acento en 'qué' en la pregunta '¿Qué hora es?' es:", "enfático"),
        88: ("Fonética Articulatoria", "¿Qué rama de la fonética estudia cómo se producen los sonidos?", "articulatoria"),
        89: ("Fonología", "¿Qué rama de la lingüística estudia los fonemas?", "fonología"),
        90: ("Ortografía y Fonética", "¿Coinciden siempre la ortografía y la fonética en español?", "no"),
        91: ("Silabeo 'suburbano'", "Separa en sílabas 'suburbano'.", "su-bur-ba-no"),
        92: ("Silabeo 'in-usual'", "Separa en sílabas 'in-usual'.", "i-nu-sual"),
        93: ("Hiato 'alcohol'", "Separa en sílabas 'alcohol'.", "al-co-hol"),
        94: ("Diptongo 'e-u'", "En la palabra 'eurasia', las vocales forman: (a) hiato, (b) diptongo.", "b"),
        95: ("Vocal átona", "En 'teléfono', las vocales 'e' y 'o' son: (a) tónicas, (b) átonas.", "b"),
        96: ("El fonema /d/", "El fonema /d/ es: (a) oclusivo dental, (b) fricativo alveolar, (c) nasal.", "a"),
        97: ("Fenómeno de la /d/", "En el habla rápida, el fonema /d/ entre vocales a veces se pierde. ¿Cómo se llama este fenómeno?", "elisión"),
        98: ("Silabeo de 'acuerdo'", "Separa en sílabas la palabra 'acuerdo'.", "a-cuer-do"),
        99: ("Fonemas y significado", "Si cambiamos /p/ por /b/ en 'palo', la palabra cambia de significado. ¿Qué demuestran los fonemas?", "que tienen valor distintivo"),
        100: ("Epítesis", "En el habla popular, a veces se añade una vocal al final. ¿Cómo se llama este fenómeno?", "epítesis"),
    }

    print("¡Bienvenido al reto de fonética y fonología, por el Instituto Caro y Cuervo!")
    print("-------------------------------------------------------------------------")
    print("Responde las preguntas o introduce 'salir' para terminar.")

    while True:
        try:
            numero_ejercicio = random.choice(list(ejercicios.keys()))
            titulo, tarea, respuesta_correcta = ejercicios[numero_ejercicio]
            
            print(f"\n[Ejercicio {numero_ejercicio}: {titulo}]")
            print(tarea)
            
            respuesta_usuario = input("Tu respuesta: ").strip()

            if respuesta_usuario.lower() == 'salir':
                print("¡Gracias por participar! ¡Hasta la próxima!")
                break
            
            respuesta_limpia = respuesta_usuario.lower().replace(" ", "")
            correcta_limpia = respuesta_correcta.lower().replace(" ", "")

            if respuesta_limpia == correcta_limpia:
                print("¡Correcto! ¡Qué bien!")
            else:
                print(f"Incorrecto. La respuesta esperada era: '{respuesta_correcta}'")

            continuar = input("\n¿Quieres otro ejercicio? (s/n): ").lower()
            if continuar != 's':
                print("¡Hasta pronto!")
                break

        except (KeyboardInterrupt, EOFError):
            print("\n¡Gracias por participar! ¡Adiós!")
            break

if __name__ == "__main__":
    main()
