# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Sociolingüística Hispanoamericana
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre la relación entre el español
# y los factores sociales, como la clase, la edad y el contacto de lenguas.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    exercises = {
        1: ("Sociolecto", "La variedad de una lengua hablada por un grupo social es un: (a) dialecto, (b) sociolecto, (c) idiolecto.", "b"),
        2: ("Geografía Lingüística", "El español rioplatense (Argentina y Uruguay) se distingue de la zona andina. ¿Qué rama de la sociolingüística estudia esta distribución?", "geografía lingüística"),
        3: ("Clase Social", "¿El uso de 'vos' o 'tú' puede variar según la clase social en algunas regiones de Hispanoamérica? (Sí/No)", "sí"),
        4: ("Actitud Lingüística", "El prejuicio contra un acento regional es un ejemplo de: (a) discriminación, (b) actitud lingüística, (c) asimilación.", "b"),
        5: ("Prestigio Lingüístico", "En muchas comunidades bilingües, la lengua dominante se percibe como la de mayor: (a) prestigio, (b) dificultad, (c) antigüedad.", "a"),
        6: ("Contacto de Lenguas", "El uso de palabras en inglés al hablar español ('ir de shopping') es un ejemplo de: (a) préstamo, (b) calco, (c) código mixto.", "c"),
        7: ("Estilística", "¿El registro formal o informal que usamos al hablar es parte de la variación: (a) dialectal, (b) sociolectal, (c) estilística?", "c"),
        8: ("Diglosia", "La coexistencia de dos lenguas en una sociedad, donde una se usa para funciones formales y la otra para informales, se llama: (a) bilingüismo, (b) diglosia, (c) poliglota.", "b"),
        9: ("Planificación Lingüística", "La creación de un vocabulario técnico para una lengua minoritaria es un ejemplo de: (a) revitalización, (b) política lingüística, (c) planificación lingüística.", "c"),
        10: ("Cambio Lingüístico", "¿El voseo en Hispanoamérica es un ejemplo de un cambio lingüístico que ha sido influido por: (a) factores sociales, (b) factores fonéticos, (c) factores ortográficos?", "a"),
        11: ("Bilingüismo", "Un individuo que habla dos lenguas fluidamente es: (a) bilingüe, (b) políglota, (c) monolingüe.", "a"),
        12: ("Actitud Lingüística", "Cuando una persona de una zona rural aspira a hablar con el acento de la capital, esto demuestra una actitud: (a) positiva, (b) negativa, (c) neutral.", "a"),
        13: ("Fonética Social", "La variación de la /s/ final de sílaba en el Caribe está correlacionada con: (a) la edad, (b) el nivel educativo, (c) el género.", "b"),
        14: ("Léxico Social", "El vocabulario específico de los jóvenes, como 'parce' o 'güey', es parte de su: (a) idiolecto, (b) sociolecto, (c) dialecto.", "b"),
        15: ("Etnolingüística", "¿Qué rama de la sociolingüística estudia la relación entre la lengua y la cultura de un grupo étnico?", "etnolingüística"),
        16: ("Comunidades de Habla", "Un grupo de personas que comparte un conjunto de normas para el uso del lenguaje es una: (a) clase social, (b) comunidad de habla, (c) tribu.", "b"),
        17: ("Prestigio Encubierto", "Una variedad de la lengua que, aunque socialmente 'baja', es valorada por la solidaridad y pertenencia al grupo, tiene prestigio: (a) abierto, (b) encubierto, (c) neutral.", "b"),
        18: ("Disglosia", "La diglosia entre el quechua y el español en la zona andina es un caso de: (a) contacto lingüístico, (b) bilingüismo, (c) ambas.", "c"),
        19: ("Lengua Estándar", "La variedad de un idioma que se enseña en las escuelas y se usa en los medios de comunicación es la: (a) lengua vulgar, (b) jerga, (c) lengua estándar.", "c"),
        20: ("Política Lingüística", "¿El establecimiento del español como idioma oficial en un país es una forma de: (a) estandarización, (b) política lingüística, (c) ambas?", "b"),
        21: ("Registro", "El lenguaje que usamos para un mensaje de texto ('q haces?') es un registro: (a) formal, (b) informal, (c) neutro.", "b"),
        22: ("Acomodación", "La tendencia de los hablantes a imitar el acento o el estilo de su interlocutor es un fenómeno de: (a) mimetismo, (b) acomodación, (c) diglosia.", "b"),
        23: ("Lengua en Contacto", "La adopción de indigenismos como 'cancha' o 'palta' es resultado del contacto con: (a) lenguas indígenas, (b) el portugués, (c) el inglés.", "a"),
        24: ("Léxico Social", "El término 'chévere' en Venezuela se considera un rasgo léxico de un sociolecto: (a) juvenil, (b) formal, (c) rural.", "a"),
        25: ("Dialecto Social", "Una forma de hablar específica de un grupo urbano es: (a) un dialecto, (b) una jerga, (c) ambas.", "c"),
        26: ("Cambio por Generación", "La forma en que se habla el español puede variar significativamente entre los abuelos y los nietos. Este fenómeno es un cambio: (a) por edad, (b) por geografía, (c) por género.", "a"),
        27: ("Actitud Lingüística", "El rechazo a hablar la lengua de los antepasados por considerarla 'menos moderna' es una actitud: (a) positiva, (b) negativa, (c) neutral.", "b"),
        28: ("Contacto con el Inglés", "El 'spanglish' en la frontera de EE. UU. y México es un ejemplo de: (a) pidgin, (b) lengua criolla, (c) mezcla de códigos.", "c"),
        29: ("Variación Diatópica", "La variación del español entre el Cono Sur, el Caribe y la zona andina es: (a) diastrática, (b) diafásica, (c) diatópica.", "c"),
        30: ("Variación Diastrática", "La variación de la lengua según la clase social o el nivel educativo es: (a) diastrática, (b) diafásica, (c) diatópica.", "a"),
        31: ("Variación Diafásica", "La variación del lenguaje según la situación o el registro (formal vs. informal) es: (a) diastrática, (b) diafásica, (c) diatópica.", "b"),
        32: ("Jerga", "El argot de los informáticos es un tipo de: (a) sociolecto, (b) jerga, (c) argot.", "b"),
        33: ("Code-switching", "Una persona que cambia del español al inglés en una misma frase está haciendo: (a) préstamos, (b) code-switching, (c) bilingüismo.", "b"),
        34: ("Prestigio y Género", "¿En algunas culturas, la forma de hablar de las mujeres es percibida como más 'correcta' que la de los hombres? (Sí/No)", "sí"),
        35: ("Política Lingüística", "La promoción de lenguas indígenas en un país es una política de: (a) asimilación, (b) estandarización, (c) revitalización.", "c"),
        36: ("Léxico Rural", "El vocabulario usado en las zonas rurales, a menudo arcaizante, es un ejemplo de un dialecto: (a) urbano, (b) rural, (c) neutro.", "b"),
        37: ("Lenguas en Extinción", "La pérdida gradual del número de hablantes de una lengua se conoce como: (a) revitalización, (b) extinción, (c) normalización.", "b"),
        38: ("Idiolecto", "La variedad lingüística única de un individuo es: (a) dialecto, (b) sociolecto, (c) idiolecto.", "c"),
        39: ("Comunidad de Habla", "¿Los hablantes de español en Nueva York forman una comunidad de habla? (Sí/No)", "sí"),
        40: ("Diglosia", "El español en la zona andina ha tenido una relación de diglosia con: (a) el quechua, (b) el inglés, (c) el portugués.", "a"),
        41: ("Préstamo Lingüístico", "La palabra 'parking' en español es un: (a) calco, (b) préstamo, (c) anglicismo.", "b"),
        42: ("Fonética Social", "La variación en la entonación del español mexicano puede indicar: (a) el nivel educativo, (b) la región de origen, (c) ambas.", "c"),
        43: ("Actitud Lingüística", "Cuando una persona se esfuerza por no perder el dialecto de su tierra natal, demuestra una actitud: (a) negativa, (b) positiva, (c) neutral.", "b"),
        44: ("Léxico Social", "El uso de jerga 'cheto' en Argentina para referirse a la clase alta es un ejemplo de: (a) sociolecto, (b) slang, (c) ambas.", "a"),
        45: ("Variación Etnica", "¿La forma de hablar el español puede variar según la etnia de los hablantes? (Sí/No)", "sí"),
        46: ("Cambio Lingüístico", "La 's' final de sílaba aspirada en el Caribe está en proceso de: (a) desaparición, (b) expansión, (c) normalización.", "b"),
        47: ("Pidgin", "Una lengua simplificada que se desarrolla entre dos grupos que no tienen una lengua en común es un: (a) criollo, (b) pidgin, (c) dialecto.", "b"),
        48: ("Criollo", "Una lengua que surge de un pidgin y se convierte en la lengua materna de una comunidad es un: (a) dialecto, (b) criollo, (c) pidgin.", "b"),
        49: ("Préstamo y Calco", "La palabra 'caliente' en español significa 'hot' en inglés. En la frase 'está caliente', 'hot' se traduciría como 'caliente' y 'hot' en 'es un tema caliente'. ¿Cómo se le llama a este fenómeno?", "calco"),
        50: ("Vitalidad Lingüística", "El uso de una lengua en la vida cotidiana y su transmisión a las nuevas generaciones es su: (a) estandarización, (b) vitalidad, (c) prestigio.", "b"),
        51: ("Políticas de Estandarización", "Las academias de la lengua promueven la: (a) variación, (b) estandarización, (c) desaparición.", "b"),
        52: ("Bilingüismo", "Un niño que aprende español y quechua al mismo tiempo es: (a) bilingüe simultáneo, (b) bilingüe sucesivo.", "a"),
        53: ("Contacto Lingüístico", "El uso de verbos en español con prefijos en inglés, como 'flashearlo', es un ejemplo de: (a) préstamo, (b) calco, (c) contacto lingüístico.", "c"),
        54: ("Fonética Social", "La pronunciación de la 'll' y la 'y' como un sonido fricativo se relaciona con: (a) la región, (b) el estrato social, (c) la edad.", "a"),
        55: ("Léxico Específico", "El uso de 'bacanería' en Colombia es un ejemplo de: (a) dialecto, (b) argot, (c) sociolecto.", "b"),
        56: ("Actitud Lingüística", "El 'leísmo' es un rasgo: (a) normativo, (b) dialectal, (c) vulgar.", "b"),
        57: ("Planificación Lingüística", "La creación de diccionarios y gramáticas para una lengua minoritaria es un ejemplo de: (a) revitalización, (b) normalización, (c) estandarización.", "c"),
        58: ("Variación Diacrónica", "El cambio del español en el tiempo es un ejemplo de variación: (a) sincrónica, (b) diacrónica, (c) sincrónica y diacrónica.", "b"),
        59: ("Bilingüismo", "Una persona que habla español en casa y inglés en la escuela es: (a) bilingüe sucesiva, (b) bilingüe simultánea, (c) bilingüe balanceada.", "a"),
        60: ("Geografía Lingüística", "El 'ceceo' es un rasgo fonético predominante en: (a) España, (b) México, (c) Hispanoamérica.", "a"),
        61: ("Etnolingüística", "El estudio de la forma en que el idioma refleja y moldea el pensamiento cultural es: (a) sociolingüística, (b) etnolingüística, (c) psicolingüística.", "b"),
        62: ("Léxico y Contexto", "El uso de 'vos' o 'tú' depende de: (a) la geografía, (b) la situación social, (c) ambas.", "c"),
        63: ("Actitud Lingüística", "El uso de 'usted' en lugar de 'tú' en algunas zonas de América para mostrar respeto se relaciona con una actitud: (a) positiva, (b) negativa, (c) neutra.", "a"),
        64: ("Variación y Edad", "La variación de la pronunciación de 'r' en los jóvenes de Puerto Rico es un ejemplo de variación por: (a) género, (b) edad, (c) clase.", "b"),
        65: ("Diglosia", "El inglés y el español en Puerto Rico tienen una relación de: (a) diglosia, (b) bilingüismo, (c) ambas.", "c"),
        66: ("Etnolingüística", "Los rituales y ceremonias de un grupo étnico se estudian con un enfoque: (a) sociolingüístico, (b) etnolingüístico, (c) psicolingüístico.", "b"),
        67: ("Léxico y Dialecto", "El uso de 'pana' en Panamá para 'amigo' es un ejemplo de un: (a) sociolecto, (b) idiolecto, (c) dialecto regional.", "c"),
        68: ("Política Lingüística", "El debate sobre si las escuelas deben enseñar español o lenguas indígenas es parte de la: (a) planificación lingüística, (b) revitalización, (c) bilingüismo.", "a"),
        69: ("Contacto Lingüístico", "El 'portuñol' es una lengua de contacto entre: (a) el español y el portugués, (b) el español y el inglés, (c) el español y el francés.", "a"),
        70: ("Vitalidad Lingüística", "Una lengua con pocos hablantes y sin transmisión generacional tiene una vitalidad: (a) alta, (b) baja, (c) estable.", "b"),
        71: ("Fenómeno Fonético", "La pérdida de la 'd' intervocálica ('cansado' -> 'cansao') en el español informal es un fenómeno: (a) sociolingüístico, (b) fonético, (c) ambas.", "c"),
        72: ("Idiolecto", "El conjunto de muletillas y frases únicas de un hablante es parte de su: (a) sociolecto, (b) dialecto, (c) idiolecto.", "c"),
        73: ("Jerga Profesional", "El lenguaje técnico de los abogados es un tipo de: (a) jerga, (b) dialecto, (c) sociolecto.", "a"),
        74: ("Variación y Educación", "¿El nivel educativo de un hablante puede influir en su forma de hablar? (Sí/No)", "sí"),
        75: ("Léxico y Generación", "Las palabras 'guay' en España y 'chévere' en Venezuela se relacionan con el grupo: (a) de clase media, (b) de jóvenes, (c) de ancianos.", "b"),
        76: ("Actitud Lingüística", "El uso de 'usted' y 'vos' puede estar relacionado con una actitud: (a) de respeto, (b) de distancia social, (c) ambas.", "c"),
        77: ("Sociolingüística", "La sociolingüística es el estudio de: (a) el lenguaje, (b) la sociedad, (c) el lenguaje en relación con la sociedad.", "c"),
        78: ("Sintaxis Social", "El uso del pronombre 'se' en construcciones como 'se te ha caído el lápiz' es un rasgo: (a) normativo, (b) dialectal, (c) coloquial.", "c"),
        79: ("Léxico Regional", "La palabra 'bondi' en Argentina es un ejemplo de léxico: (a) informal, (b) regional, (c) ambas.", "c"),
        80: ("Vitalidad Lingüística", "La UNESCO clasifica a las lenguas según su: (a) prestigio, (b) vitalidad, (c) estandarización.", "b"),
        81: ("Geografía Lingüística", "El isoglosas son: (a) fronteras dialectales, (b) fronteras políticas, (c) fronteras geográficas.", "a"),
        82: ("Sintaxis Social", "El uso de la forma 'ustedes' en lugar de 'vosotros' es una característica: (a) dialectal, (b) sociolectal, (c) ambas.", "a"),
        83: ("Préstamo Lingüístico", "La palabra 'fútbol' es un préstamo del: (a) francés, (b) alemán, (c) inglés.", "c"),
        84: ("Diglosia", "El quechua y el español en la zona andina son lenguas con: (a) diglosia, (b) monolingüismo, (c) ambas.", "a"),
        85: ("Léxico y Clase", "¿El uso de 'trabajar' o 'laburar' puede estar relacionado con la clase social? (Sí/No)", "sí"),
        86: ("Actitud Lingüística", "Una persona que cambia de acento para encajar en un grupo muestra una actitud de: (a) adaptación, (b) rechazo, (c) neutralidad.", "a"),
        87: ("Contacto Lingüístico", "El 'calco' es la traducción literal de una expresión de otra lengua. Un ejemplo es 'ratón de biblioteca' del inglés. ¿Verdadero o Falso?", "verdadero"),
        88: ("Sociolecto", "La forma de hablar de los niños es diferente a la de los adultos. Este es un ejemplo de un: (a) cronolecto, (b) dialecto, (c) idiolecto.", "a"),
        89: ("Prestigio", "El prestigio lingüístico es siempre: (a) objetivo, (b) subjetivo, (c) normativo.", "b"),
        90: ("Léxico y Género", "¿El léxico usado por hombres y mujeres es exactamente el mismo? (Sí/No)", "no"),
        91: ("Diglosia", "El español ha tenido una relación de diglosia con lenguas indígenas en: (a) la zona andina, (b) el cono sur, (c) el caribe.", "a"),
        92: ("Contacto Lingüístico", "Los 'tours' son un ejemplo de: (a) préstamos, (b) calcos, (c) ambas.", "a"),
        93: ("Sociolingüística", "La sociolingüística estudia: (a) la fonética, (b) la sintaxis, (c) la variación lingüística.", "c"),
        94: ("Variación y Educación", "El uso de la 's' final de sílaba puede estar correlacionado con: (a) el género, (b) el nivel educativo, (c) la edad.", "b"),
        95: ("Actitud Lingüística", "La creencia de que una forma de hablar es 'mejor' que otra es una: (a) norma, (b) regla, (c) actitud.", "c"),
        96: ("Sociolecto", "La forma de hablar de los abogados se conoce como: (a) jerga, (b) dialecto, (c) ambas.", "a"),
        97: ("Contacto Lingüístico", "El uso de 'troca' en lugar de 'camioneta' en el norte de México es un ejemplo de: (a) calco, (b) préstamo, (c) code-switching.", "b"),
        98: ("Geografía Lingüística", "La línea que separa dos dialectos o variantes lingüísticas es una: (a) isoglosa, (b) frontera, (c) línea de acento.", "a"),
        99: ("Sociolingüística", "El estudio de la variación en la forma de hablar de una persona según su género es parte de la sociolingüística: (a) del género, (b) de la clase, (c) de la edad.", "a"),
        100: ("Actitud Lingüística", "La forma de hablar de una persona puede estar influenciada por su deseo de: (a) pertenecer a un grupo, (b) ser diferente, (c) ambas.", "c"),
    }

    print("¡Bienvenido al reto de Sociolingüística Hispanoamericana!")
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
