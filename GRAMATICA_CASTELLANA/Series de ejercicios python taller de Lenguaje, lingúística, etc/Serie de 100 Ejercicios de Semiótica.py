# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Semiótica
# Inspirado en las obras del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los conceptos fundamentales de la semiótica,
# incluyendo el signo, sus componentes, los teóricos principales y sus aplicaciones.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de semiótica
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Generalidades", "La semiótica es la ciencia que estudia: (a) los signos, (b) los símbolos, (c) el lenguaje.", "a"),
        2: ("Saussure", "Según Ferdinand de Saussure, el signo lingüístico está compuesto por: (a) significante y símbolo, (b) significante y significado, (c) denotación y connotación.", "b"),
        3: ("Saussure", "El 'significante' de un signo es: (a) la idea o concepto, (b) la imagen acústica, (c) el objeto real.", "b"),
        4: ("Saussure", "La relación entre el significante y el significado es: (a) natural, (b) icónica, (c) arbitraria.", "c"),
        5: ("Peirce", "El modelo de signo de Charles Sanders Peirce es: (a) binario, (b) triádico, (c) cuaternario.", "b"),
        6: ("Peirce", "Según Peirce, un 'ícono' es un signo que se relaciona con su objeto por: (a) semejanza, (b) contigüidad, (c) convención.", "a"),
        7: ("Peirce", "Un 'índice' es un signo que tiene una relación de causalidad con su objeto. (Verdadero/Falso)", "verdadero"),
        8: ("Peirce", "Un 'símbolo' es un signo que se relaciona con su objeto por: (a) semejanza, (b) causalidad, (c) convención.", "c"),
        9: ("Tipos de signos", "¿Un mapa es un ejemplo de ícono? (Sí/No)", "sí"),
        10: ("Tipos de signos", "El humo es un índice de fuego. (Verdadero/Falso)", "verdadero"),
        11: ("Tipos de signos", "Las letras del alfabeto son ejemplos de: (a) íconos, (b) índices, (c) símbolos.", "c"),
        12: ("Generalidades", "La 'semiología' es un término usado por Saussure para referirse a la semiótica. (Verdadero/Falso)", "verdadero"),
        13: ("Semántica", "La 'denotación' de un signo es su significado: (a) literal, (b) figurado, (c) contextual.", "a"),
        14: ("Semántica", "La 'connotación' de un signo incluye los valores asociados a él. (Verdadero/Falso)", "verdadero"),
        15: ("Pragmática", "La 'pragmática' semiótica estudia el uso de los signos en un contexto. (Verdadero/Falso)", "verdadero"),
        16: ("Sintaxis", "La 'sintaxis' semiótica estudia la relación de los signos entre sí. (Verdadero/Falso)", "verdadero"),
        17: ("Aplicaciones", "La semiótica de la moda estudia los signos en: (a) la ropa, (b) la publicidad, (c) los colores.", "a"),
        18: ("Aplicaciones", "El estudio de los signos en la publicidad se llama semiótica de la publicidad. (Verdadero/Falso)", "verdadero"),
        19: ("Códigos", "Un 'código' es un sistema de signos que comparten los miembros de una cultura. (Verdadero/Falso)", "verdadero"),
        20: ("Generalidades", "¿El 'contexto' es esencial para la interpretación de los signos? (Sí/No)", "sí"),
        21: ("Saussure", "El 'valor' de un signo se define por su relación con otros signos en el sistema. (Verdadero/Falso)", "verdadero"),
        22: ("Peirce", "El 'interpretante' de un signo es: (a) el objeto físico, (b) la idea o efecto mental, (c) el significado social.", "b"),
        23: ("Tipos de signos", "La fotografía de una persona es un ícono. (Verdadero/Falso)", "verdadero"),
        24: ("Tipos de signos", "La huella de un zapato es un: (a) ícono, (b) índice, (c) símbolo.", "b"),
        25: ("Tipos de signos", "La señal de 'stop' es un símbolo. (Verdadero/Falso)", "verdadero"),
        26: ("Generalidades", "El 'signo' es la unidad básica de la semiótica. (Verdadero/Falso)", "verdadero"),
        27: ("Saussure", "El lenguaje es una 'institución social' según Saussure. (Verdadero/Falso)", "verdadero"),
        28: ("Peirce", "El 'objeto' de un signo es la cosa o evento a la que se refiere. (Verdadero/Falso)", "verdadero"),
        29: ("Semántica", "El término 'gato' denota un animal, pero puede connotar: (a) cariño, (b) malicia, (c) las dos.", "c"),
        30: ("Pragmática", "Un gesto con la mano puede tener significados diferentes en distintos países. (Verdadero/Falso)", "verdadero"),
        31: ("Sintaxis", "El orden de las palabras en una frase es un ejemplo de sintaxis semiótica. (Verdadero/Falso)", "verdadero"),
        32: ("Aplicaciones", "Los 'emojis' son un ejemplo de signos estudiados por la semiótica. (Verdadero/Falso)", "verdadero"),
        33: ("Códigos", "¿El código Morse es un sistema de signos? (Sí/No)", "sí"),
        34: ("Generalidades", "La semiótica no se limita a la comunicación verbal. (Verdadero/Falso)", "verdadero"),
        35: ("Saussure", "¿Saussure se enfocó en el estudio del lenguaje como un sistema sincrónico? (Sí/No)", "sí"),
        36: ("Peirce", "El 'representamen' es la forma física del signo. (Verdadero/Falso)", "verdadero"),
        37: ("Tipos de signos", "El 'ladrido' de un perro es un índice de su presencia. (Verdadero/Falso)", "verdadero"),
        38: ("Tipos de signos", "Un 'dibujo' de un árbol es un ícono. (Verdadero/Falso)", "verdadero"),
        39: ("Tipos de signos", "La paloma de la paz es un: (a) ícono, (b) índice, (c) símbolo.", "c"),
        40: ("Generalidades", "La 'semiótica cultural' estudia los signos y símbolos en la cultura. (Verdadero/Falso)", "verdadero"),
        41: ("Saussure", "El 'lenguaje' según Saussure es el sistema en abstracto, mientras que el 'habla' es el uso individual. (Verdadero/Falso)", "verdadero"),
        42: ("Peirce", "La 'interpretación' de un signo es el proceso por el cual el interpretante se forma en la mente. (Verdadero/Falso)", "verdadero"),
        43: ("Semántica", "El significado literal de 'corazón de piedra' es el mismo que su significado figurado. (Verdadero/Falso)", "falso"),
        44: ("Pragmática", "El 'tono de voz' es un signo pragmático. (Verdadero/Falso)", "verdadero"),
        45: ("Sintaxis", "¿La 'gramática' de una lengua es un ejemplo de sintaxis semiótica? (Sí/No)", "sí"),
        46: ("Aplicaciones", "Un 'logo' es un tipo de signo. (Verdadero/Falso)", "verdadero"),
        47: ("Códigos", "Un 'código no verbal' es un sistema de signos no lingüísticos. (Verdadero/Falso)", "verdadero"),
        48: ("Generalidades", "La semiótica es una disciplina reciente. (Verdadero/Falso)", "falso"),
        49: ("Saussure", "El 'significado' de un signo es su componente material. (Verdadero/Falso)", "falso"),
        50: ("Peirce", "El 'objeto dinámico' es el objeto en sí mismo, independiente del signo. (Verdadero/Falso)", "verdadero"),
        51: ("Tipos de signos", "Una 'flecha' que indica una dirección es un índice. (Verdadero/Falso)", "verdadero"),
        52: ("Tipos de signos", "Un 'emoji' de una cara feliz es un ícono. (Verdadero/Falso)", "verdadero"),
        53: ("Tipos de signos", "La bandera de un país es un símbolo. (Verdadero/Falso)", "verdadero"),
        54: ("Generalidades", "¿Los gestos son parte del estudio de la semiótica? (Sí/No)", "sí"),
        55: ("Saussure", "La 'diacronía' estudia el lenguaje a lo largo del tiempo. (Verdadero/Falso)", "verdadero"),
        56: ("Peirce", "El 'interpretante inmediato' es la primera impresión que produce el signo. (Verdadero/Falso)", "verdadero"),
        57: ("Semántica", "La 'polisemia' ocurre cuando una palabra tiene un solo significado. (Verdadero/Falso)", "falso"),
        58: ("Pragmática", "La 'intención comunicativa' es un concepto clave en la pragmática. (Verdadero/Falso)", "verdadero"),
        59: ("Sintaxis", "La 'puntuación' es un sistema de signos con reglas sintácticas. (Verdadero/Falso)", "verdadero"),
        60: ("Aplicaciones", "La 'semiótica visual' analiza imágenes, películas y artes visuales. (Verdadero/Falso)", "verdadero"),
        61: ("Códigos", "Un 'código de vestimenta' es un sistema de signos. (Verdadero/Falso)", "verdadero"),
        62: ("Generalidades", "La semiótica se relaciona con la lingüística y la filosofía. (Verdadero/Falso)", "verdadero"),
        63: ("Saussure", "El 'significante' de la palabra 'sol' es el astro. (Verdadero/Falso)", "falso"),
        64: ("Peirce", "El 'objeto inmediato' es la representación del objeto en la mente. (Verdadero/Falso)", "verdadero"),
        65: ("Tipos de signos", "Las 'señales de tráfico' son una mezcla de íconos, índices y símbolos. (Verdadero/Falso)", "verdadero"),
        66: ("Tipos de signos", "La 'sirena' de una ambulancia es un índice. (Verdadero/Falso)", "verdadero"),
        67: ("Tipos de signos", "Una 'palabra' es principalmente un símbolo. (Verdadero/Falso)", "verdadero"),
        68: ("Generalidades", "Un 'signo' no necesita un intérprete. (Verdadero/Falso)", "falso"),
        69: ("Saussure", "El 'significado' es un concepto mental. (Verdadero/Falso)", "verdadero"),
        70: ("Peirce", "La 'semiosis' es el proceso de creación de significado. (Verdadero/Falso)", "verdadero"),
        71: ("Semántica", "La 'sinonimia' es la relación entre palabras de significados opuestos. (Verdadero/Falso)", "falso"),
        72: ("Pragmática", "El 'contexto social' afecta la interpretación de los signos. (Verdadero/Falso)", "verdadero"),
        73: ("Sintaxis", "La 'concordancia gramatical' es un ejemplo de sintaxis semiótica. (Verdadero/Falso)", "verdadero"),
        74: ("Aplicaciones", "La 'publicidad' utiliza la semiótica para persuadir. (Verdadero/Falso)", "verdadero"),
        75: ("Códigos", "Un 'código de lenguaje de señas' es un sistema semiótico. (Verdadero/Falso)", "verdadero"),
        76: ("Generalidades", "El estudio de la semiótica puede ayudar a interpretar el mundo. (Verdadero/Falso)", "verdadero"),
        77: ("Saussure", "El 'significado' de un signo es una imagen mental. (Verdadero/Falso)", "verdadero"),
        78: ("Peirce", "El 'interpretante final' es la interpretación más completa del signo. (Verdadero/Falso)", "verdadero"),
        79: ("Semántica", "La 'metáfora' es un tipo de connotación. (Verdadero/Falso)", "verdadero"),
        80: ("Pragmática", "La 'ironía' es un fenómeno pragmático. (Verdadero/Falso)", "verdadero"),
        81: ("Sintaxis", "El 'orden de lectura' de una oración es un aspecto sintáctico. (Verdadero/Falso)", "verdadero"),
        82: ("Aplicaciones", "El 'cine' es un campo de estudio para la semiótica. (Verdadero/Falso)", "verdadero"),
        83: ("Códigos", "El 'código binario' es un código. (Verdadero/Falso)", "verdadero"),
        84: ("Generalidades", "La semiótica estudia solo la comunicación humana. (Verdadero/Falso)", "falso"),
        85: ("Saussure", "La 'lengua' es el sistema de signos, y el 'habla' es su uso. (Verdadero/Falso)", "verdadero"),
        86: ("Peirce", "El 'ícono' siempre es una imagen visual. (Verdadero/Falso)", "falso"),
        87: ("Tipos de signos", "Una 'firma' es un ícono. (Verdadero/Falso)", "falso"),
        88: ("Tipos de signos", "La 'fiebre' es un índice de enfermedad. (Verdadero/Falso)", "verdadero"),
        89: ("Tipos de signos", "Los 'números' son símbolos. (Verdadero/Falso)", "verdadero"),
        90: ("Generalidades", "La semiótica nos ayuda a entender cómo se construye la realidad social. (Verdadero/Falso)", "verdadero"),
        91: ("Saussure", "El 'significante' de un signo puede cambiar con el tiempo. (Verdadero/Falso)", "verdadero"),
        92: ("Peirce", "El 'objeto' de un signo es su referente. (Verdadero/Falso)", "verdadero"),
        93: ("Semántica", "El 'significado' es el mismo para todas las personas. (Verdadero/Falso)", "falso"),
        94: ("Pragmática", "Las 'reglas de cortesía' son un ejemplo de reglas pragmáticas. (Verdadero/Falso)", "verdadero"),
        95: ("Sintaxis", "El 'orden de los párrafos' en un texto es un aspecto sintáctico. (Verdadero/Falso)", "verdadero"),
        96: ("Aplicaciones", "La 'narratología' es una disciplina semiótica. (Verdadero/Falso)", "verdadero"),
        97: ("Códigos", "¿El 'lenguaje de programación' es un código? (Sí/No)", "sí"),
        98: ("Generalidades", "La 'lectura del mundo' es un proceso semiótico. (Verdadero/Falso)", "verdadero"),
        99: ("Saussure", "La 'arbitrariedad' del signo implica que no hay una razón natural para la relación entre el significante y el significado. (Verdadero/Falso)", "verdadero"),
        100: ("Peirce", "La 'interpretación' de un signo es un proceso infinito. (Verdadero/Falso)", "verdadero"),
    }

    print("¡Bienvenido al reto de Semiótica!")
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
