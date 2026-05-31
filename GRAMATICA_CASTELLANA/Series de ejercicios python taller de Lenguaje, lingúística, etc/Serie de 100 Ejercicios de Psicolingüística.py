# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Psicolingüística
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre la relación entre el lenguaje
# y los procesos cognitivos y neurológicos del ser humano.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    exercises = {
        1: ("Adquisición del Lenguaje", "Según Noam Chomsky, los niños nacen con una habilidad innata para el lenguaje llamada: (a) gramática universal, (b) capacidad sintáctica, (c) léxico mental.", "a"),
        2: ("Neurolingüística", "El área del cerebro responsable de la producción del lenguaje se llama: (a) Área de Wernicke, (b) Lóbulo temporal, (c) Área de Broca.", "c"),
        3: ("Afasia", "Una persona con dificultad para producir un habla fluida, pero con buena comprensión, podría tener afasia de: (a) Wernicke, (b) Broca, (c) Conducción.", "b"),
        4: ("Léxico Mental", "El 'diccionario' mental que contiene todas las palabras que conocemos se denomina: (a) léxico cerebral, (b) diccionario cognitivo, (c) léxico mental.", "c"),
        5: ("Percepción del Habla", "El fenómeno por el cual el cerebro 'llena' los sonidos faltantes en una palabra para completar el mensaje es el efecto de: (a) restauración fonémica, (b) asimilación, (c) codificación fonética.", "a"),
        6: ("Teoría de Sapir-Whorf", "La hipótesis que propone que la lengua que hablamos influye en la forma en que pensamos se conoce como: (a) Relatividad Lingüística, (b) Gramática Transformacional, (c) Hipótesis del Lenguaje.", "a"),
        7: ("Adquisición L2", "La 'edad crítica' para la adquisición de un segundo idioma se refiere a que, después de cierta edad, es más difícil alcanzar: (a) fluidez, (b) acento nativo, (c) vocabulario avanzado.", "b"),
        8: ("Error de Habla", "Un 'lapsus linguae' o 'slips of the tongue' es un error en el proceso de: (a) comprensión, (b) producción, (c) memoria.", "b"),
        9: ("Prosodia", "El uso del tono, el ritmo y el acento para transmitir significado se conoce como: (a) semántica, (b) sintaxis, (c) prosodia.", "c"),
        10: ("Bilingüismo", "El fenómeno de cambiar entre dos lenguas en la misma conversación se llama: (a) diglosia, (b) code-switching, (c) préstamos.", "b"),
        11: ("Procesamiento Cognitivo", "El proceso mental de entender lo que se escucha o lee se llama: (a) producción, (b) comprensión, (c) codificación.", "b"),
        12: ("Desarrollo Infantil", "La etapa del desarrollo del lenguaje donde los bebés emiten sonidos vocálicos como 'ooh' o 'aah' es el: (a) balbuceo, (b) arrullo, (c) gritos.", "b"),
        13: ("Etapa de una Palabra", "Un niño que usa 'leche' para referirse a la leche, pero también al vaso y al refrigerador, está haciendo una: (a) sobregeneralización, (b) subextensión, (c) sobreextensión.", "c"),
        14: ("Etapa de dos Palabras", "La expresión 'mamá zapato' para decir 'el zapato de mamá' es un ejemplo de: (a) habla telegráfica, (b) sintaxis básica, (c) oración completa.", "a"),
        15: ("Afasia", "La afasia que se caracteriza por una comprensión deficiente del lenguaje, pero una producción de habla fluida (aunque incoherente), es la de: (a) Wernicke, (b) Broca, (c) Conducción.", "a"),
        16: ("Neurociencia Cognitiva", "¿La mayoría de las personas tienen el área de lenguaje lateralizada en el hemisferio derecho? (Sí/No)", "no"),
        17: ("Priming", "Cuando ver la palabra 'médico' hace que reconozcamos más rápido la palabra 'enfermera', es un ejemplo de: (a) priming semántico, (b) activación sintáctica, (c) facilitación motora.", "a"),
        18: ("Dislexia", "Un trastorno específico del aprendizaje que se caracteriza por la dificultad para leer con precisión y fluidez es: (a) afasia, (b) dislexia, (c) tartamudeo.", "b"),
        19: ("Tartamudeo", "Un trastorno de la fluidez del habla, caracterizado por repeticiones o prolongaciones de sonidos, se denomina: (a) afasia, (b) disartria, (c) tartamudeo.", "c"),
        20: ("Neurolingüística", "¿Cuál de las siguientes técnicas se utiliza para mapear la actividad cerebral relacionada con el lenguaje? (a) IRMf, (b) PET, (c) Ambas.", "c"),
        21: ("Lenguaje y Pensamiento", "¿Según la hipótesis de Sapir-Whorf, una lengua sin futuro gramatical no permite a sus hablantes pensar en el futuro? (Sí/No)", "no"),
        22: ("Adquisición del Lenguaje", "Los errores de sobregeneralización, como decir 'ponido' en lugar de 'puesto', indican que los niños están aprendiendo las reglas: (a) de fonología, (b) de morfología, (c) de sintaxis.", "b"),
        23: ("Léxico Mental", "El modelo de red semántica para el léxico mental sugiere que las palabras están conectadas por: (a) significado, (b) sonido, (c) ambas.", "c"),
        24: ("Procesamiento del Habla", "El proceso por el cual el oyente convierte las ondas sonoras en un mensaje con significado es: (a) producción, (b) percepción del habla, (c) codificación.", "b"),
        25: ("Afasia", "La afasia que afecta la capacidad de un individuo para repetir palabras y frases, pero no afecta la comprensión o la producción del habla, es la de: (a) Wernicke, (b) Broca, (c) Conducción.", "c"),
        26: ("Neurolingüística", "El lóbulo temporal del cerebro es importante para la: (a) producción del habla, (b) comprensión del habla, (c) planificación motora del habla.", "b"),
        27: ("Neurolingüística", "¿La mayoría de las personas diestras tienen el lenguaje lateralizado en el hemisferio izquierdo? (Sí/No)", "sí"),
        28: ("Neurolingüística", "¿El área del cerebro que controla la comprensión del lenguaje se llama Área de Wernicke? (Sí/No)", "sí"),
        29: ("Bilingüismo", "El bilingüismo en el que un niño aprende las dos lenguas simultáneamente desde el nacimiento es el: (a) bilingüismo simultáneo, (b) bilingüismo secuencial, (c) bilingüismo aditivo.", "a"),
        30: ("Adquisición", "La etapa de desarrollo del lenguaje en la que los bebés empiezan a producir sílabas repetidas ('ba-ba-ba') es el: (a) balbuceo canónico, (b) arrullo, (c) habla telegráfica.", "a"),
        31: ("Neurolingüística", "La incapacidad de reconocer caras (prosopagnosia) se relaciona con el área del lenguaje. (Verdadero/Falso)", "falso"),
        32: ("Léxico Mental", "Los verbos irregulares como 'decir' (dije) o 'saber' (supe) se aprenden generalmente por: (a) regla, (b) memorización, (c) analogía.", "b"),
        33: ("Teoría Cognitiva", "El lenguaje se considera una parte de la cognición general en la teoría: (a) innatista, (b) social, (c) cognitiva.", "c"),
        34: ("Adquisición", "El 'vocabulario pasivo' de un niño es el que: (a) comprende pero no produce, (b) produce pero no comprende, (c) no usa en absoluto.", "a"),
        35: ("Neurolingüística", "El fascículo arqueado es una banda de fibras nerviosas que conecta el área de Broca y la de Wernicke. (Verdadero/Falso)", "verdadero"),
        36: ("Léxico Mental", "La teoría de la 'red de activación' sugiere que cuando una palabra se activa, otras palabras relacionadas también se activan, facilitando su acceso. (Verdadero/Falso)", "verdadero"),
        37: ("Lenguaje y Pensamiento", "¿La falta de un color en el léxico de una lengua (como el 'azul' en algunas lenguas amazónicas) implica que sus hablantes no pueden percibir ese color? (Sí/No)", "no"),
        38: ("Bilingüismo", "Se considera bilingüismo 'substractivo' cuando el aprendizaje de una segunda lengua debilita el conocimiento de la primera. (Verdadero/Falso)", "verdadero"),
        39: ("Adquisición", "El habla telegráfica se caracteriza por el uso de: (a) solo sustantivos y verbos, (b) solo oraciones completas, (c) una sola palabra.", "a"),
        40: ("Neurolingüística", "El córtex prefrontal es importante para la: (a) percepción del habla, (b) producción del habla, (c) memoria de trabajo lingüística.", "c"),
        41: ("Procesamiento Sintáctico", "La ambigüedad en una frase como 'El perro del vecino, que es grande, me mordió' se resuelve por el procesamiento: (a) fonético, (b) sintáctico, (c) semántico.", "b"),
        42: ("Psicología del Lenguaje", "El tiempo que tarda una persona en decir una palabra después de ver una imagen se utiliza para medir el proceso de: (a) producción, (b) comprensión, (c) memorización.", "a"),
        43: ("Afasia", "La afasia global es una lesión extensa en las áreas del lenguaje que afecta: (a) solo la comprensión, (b) solo la producción, (c) ambas.", "c"),
        44: ("Procesamiento Fonológico", "El proceso de identificar los sonidos individuales de una palabra ('gato' -> /g/, /a/, /t/, /o/) se llama: (a) análisis fonémico, (b) decodificación, (c) síntesis.", "a"),
        45: ("Adquisición", "¿Los niños aprenden a hablar principalmente por imitación de sus padres? (Sí/No)", "no"),
        46: ("Teoría Modular", "La teoría que propone que la mente tiene módulos separados para cada función cognitiva, incluido el lenguaje, es la de: (a) la mente modular, (b) la cognición general, (c) el conexionismo.", "a"),
        47: ("Psicología Cognitiva", "El 'principio de cooperación' de Grice se relaciona con el estudio de: (a) fonología, (b) pragmática, (c) sintaxis.", "b"),
        48: ("Lectura", "El proceso de convertir grafemas (letras) en fonemas (sonidos) es la: (a) decodificación, (b) comprensión, (c) fluidez.", "a"),
        49: ("Dislexia", "La dificultad en la decodificación de las palabras es una característica clave de la: (a) afasia, (b) dislexia, (c) tartamudeo.", "b"),
        50: ("Bilingüismo", "El bilingüismo 'equilibrado' se refiere a un hablante que tiene el mismo dominio en ambas lenguas. (Verdadero/Falso)", "verdadero"),
        51: ("Conexionismo", "Las redes neuronales artificiales que simulan el aprendizaje del lenguaje se basan en el modelo: (a) innatista, (b) conexionista, (c) social.", "b"),
        52: ("Neurolingüística", "El síndrome de Wernicke se relaciona con un daño en la corteza auditiva primaria. (Verdadero/Falso)", "falso"),
        53: ("Adquisición", "La etapa de balbuceo no canónico es la primera en la producción de sonidos en los bebés. (Verdadero/Falso)", "verdadero"),
        54: ("Psicología del Lenguaje", "La 'punta de la lengua' (tip-of-the-tongue) es un fenómeno de: (a) comprensión, (b) producción, (c) percepción.", "b"),
        55: ("Procesamiento Semántico", "La ambigüedad de una palabra como 'banco' (de sentarse o de dinero) se resuelve por el contexto: (a) fonológico, (b) sintáctico, (c) semántico.", "c"),
        56: ("Bilingüismo", "El bilingüismo en el que un niño aprende una lengua y luego, más tarde, una segunda lengua, es el bilingüismo: (a) simultáneo, (b) secuencial, (c) aditivo.", "b"),
        57: ("Neurolingüística", "El área del cerebro responsable de la comprensión del lenguaje se llama: (a) Área de Broca, (b) Área de Wernicke, (c) Lóbulo frontal.", "b"),
        58: ("Psicología del Lenguaje", "El procesamiento del lenguaje es un proceso: (a) lento y secuencial, (b) rápido y en paralelo, (c) lento y en paralelo.", "b"),
        59: ("Adquisición", "¿La primera palabra de un niño suele ser un sustantivo? (Sí/No)", "sí"),
        60: ("Neurolingüística", "La agnosia auditiva se caracteriza por la incapacidad de reconocer el sonido del habla. (Verdadero/Falso)", "verdadero"),
        61: ("Psicología Cognitiva", "El 'efecto Stroop' se utiliza para estudiar la: (a) memoria, (b) atención selectiva, (c) comprensión.", "b"),
        62: ("Lenguaje y Pensamiento", "La hipótesis de 'pensamiento para el lenguaje' sugiere que el lenguaje está diseñado para: (a) expresar el pensamiento, (b) moldear el pensamiento, (c) ambas.", "a"),
        63: ("Afasia", "Un tipo de afasia que se caracteriza por una producción de habla no fluida y una comprensión limitada es la afasia: (a) de Broca, (b) de Wernicke, (c) global.", "c"),
        64: ("Psicología del Lenguaje", "El 'priming' se refiere a la influencia que un estímulo tiene sobre la respuesta a un estímulo posterior. (Verdadero/Falso)", "verdadero"),
        65: ("Neurolingüística", "¿Cuál de las siguientes áreas no está directamente relacionada con el lenguaje? (a) Lóbulo occipital, (b) Área de Broca, (c) Área de Wernicke.", "a"),
        66: ("Adquisición", "La 'sobregeneralización' de las reglas gramaticales es un signo de que un niño está aprendiendo las reglas. (Verdadero/Falso)", "verdadero"),
        67: ("Psicología del Lenguaje", "El 'efecto de la punta de la lengua' es un ejemplo de un fallo en la recuperación: (a) sintáctica, (b) fonológica, (c) semántica.", "b"),
        68: ("Bilingüismo", "El bilingüismo 'simultáneo' es cuando el niño aprende dos lenguas desde el nacimiento. (Verdadero/Falso)", "verdadero"),
        69: ("Neurolingüística", "El lóbulo frontal está relacionado con las funciones ejecutivas y el lenguaje. (Verdadero/Falso)", "verdadero"),
        70: ("Procesamiento", "El proceso de decodificación de las palabras es: (a) bottom-up, (b) top-down, (c) ambas.", "a"),
        71: ("Procesamiento", "El procesamiento 'top-down' en la comprensión del lenguaje se basa en: (a) el sonido de las palabras, (b) el conocimiento previo y el contexto, (c) la sintaxis de la frase.", "b"),
        72: ("Afasia", "La afasia que se caracteriza por una producción de habla fluida, pero con parafasias fonémicas y semánticas, es la de: (a) Wernicke, (b) Broca, (c) Conducción.", "a"),
        73: ("Neurolingüística", "El área de Broca se encuentra en el lóbulo: (a) temporal, (b) parietal, (c) frontal.", "c"),
        74: ("Neurolingüística", "El área de Wernicke se encuentra en el lóbulo: (a) temporal, (b) parietal, (c) frontal.", "a"),
        75: ("Adquisición", "El 'lenguaje interno' o 'habla interna' es el lenguaje que usamos para pensar. (Verdadero/Falso)", "verdadero"),
        76: ("Procesamiento", "Un 'error de anticipación' en la producción del habla es cuando un sonido se adelanta en la palabra. (Verdadero/Falso)", "verdadero"),
        77: ("Léxico Mental", "El acceso a las palabras en el léxico mental se basa en: (a) la frecuencia de uso, (b) el contexto, (c) ambas.", "c"),
        78: ("Psicolingüística", "La psicolingüística es el estudio de: (a) el lenguaje, (b) la mente, (c) el lenguaje en relación con la mente.", "c"),
        79: ("Lectura", "El proceso de 'skimming' o lectura rápida es un ejemplo de procesamiento: (a) bottom-up, (b) top-down, (c) fonológico.", "b"),
        80: ("Adquisición", "El período en el que un niño es más sensible a aprender un idioma es conocido como el período: (a) sensible, (b) crítico, (c) de balbuceo.", "b"),
        81: ("Neurolingüística", "La 'afasia de conducción' es un trastorno del lenguaje que se produce por la desconexión entre el área de Broca y el área de Wernicke. (Verdadero/Falso)", "verdadero"),
        82: ("Bilingüismo", "¿El bilingüismo puede retrasar el desarrollo del lenguaje en los niños? (Sí/No)", "no"),
        83: ("Psicología del Lenguaje", "El 'efecto de frecuencia' en el procesamiento de palabras se refiere a que las palabras más comunes se procesan más rápido. (Verdadero/Falso)", "verdadero"),
        84: ("Neurolingüística", "La 'disfasia' es un término que se utiliza a veces para referirse a la afasia. (Verdadero/Falso)", "verdadero"),
        85: ("Adquisición", "El 'input' lingüístico es el lenguaje que el niño: (a) produce, (b) escucha, (c) imita.", "b"),
        86: ("Procesamiento Sintáctico", "La 'ambigüedad estructural' se refiere a frases que pueden ser analizadas de diferentes maneras sintácticamente. (Verdadero/Falso)", "verdadero"),
        87: ("Neurolingüística", "La 'agrafia' es la pérdida de la capacidad para escribir. (Verdadero/Falso)", "verdadero"),
        88: ("Léxico Mental", "Las palabras en el léxico mental se organizan por: (a) significado, (b) fonología, (c) ambas.", "c"),
        89: ("Psicología del Lenguaje", "El modelo de 'cascada' en el procesamiento del lenguaje sugiere que las etapas se procesan secuencialmente. (Verdadero/Falso)", "verdadero"),
        90: ("Adquisición", "La 'sobreextensión' es cuando un niño usa una palabra para referirse a un conjunto más amplio de objetos de lo que debería. (Verdadero/Falso)", "verdadero"),
        91: ("Neurolingüística", "El 'Síndrome de Gerstmann' se relaciona con una lesión en el lóbulo parietal. (Verdadero/Falso)", "verdadero"),
        92: ("Psicología del Lenguaje", "La 'fluidez' en la lectura se refiere a la capacidad de leer: (a) rápido, (b) sin esfuerzo, (c) con comprensión.", "b"),
        93: ("Neurolingüística", "El 'cerebelo' está involucrado en la fluidez y el ritmo del habla. (Verdadero/Falso)", "verdadero"),
        94: ("Adquisición", "Los 'errores de overregularización' en los niños indican que están aplicando una regla gramatical a una excepción. (Verdadero/Falso)", "verdadero"),
        95: ("Procesamiento Semántico", "La 'ambigüedad léxica' se refiere a la existencia de varias palabras con el mismo sonido. (Verdadero/Falso)", "falso"),
        96: ("Neurolingüística", "El 'giro angular' es una parte del cerebro que se relaciona con la lectura y la escritura. (Verdadero/Falso)", "verdadero"),
        97: ("Bilingüismo", "El 'cambio de código' (code-switching) es un signo de déficit lingüístico en los bilingües. (Verdadero/Falso)", "falso"),
        98: ("Adquisición", "Los niños de 3 años ya han adquirido la mayor parte de la sintaxis básica de su lengua materna. (Verdadero/Falso)", "verdadero"),
        99: ("Psicología del Lenguaje", "La 'hipótesis de la mente modular' sugiere que el lenguaje se procesa de forma independiente de otras funciones cognitivas. (Verdadero/Falso)", "verdadero"),
        100: ("Neurolingüística", "La 'alexia' es la pérdida de la capacidad para leer. (Verdadero/Falso)", "verdadero"),
    }

    print("¡Bienvenido al reto de Psicolingüística!")
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
