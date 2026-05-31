# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Semántica y Pragmática
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre el significado de las palabras,
# las oraciones y el papel del contexto en la comunicación.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    exercises = {
        1: ("Significado Léxico", "¿La relación de significado en la que una palabra (ej. 'animal') incluye a otra (ej. 'gato') se llama: (a) sinonimia, (b) antonimia, (c) hiponimia?", "c"),
        2: ("Antonimia", "Los pares de palabras 'caliente' y 'frío' son ejemplos de antónimos: (a) complementarios, (b) graduales, (c) conversivos.", "b"),
        3: ("Polisemia", "¿La palabra 'banco' (asiento y entidad financiera) es un ejemplo de: (a) homonimia, (b) polisemia, (c) sinonimia?", "b"),
        4: ("Actos de Habla", "La afirmación 'Te prometo que lo haré' es un ejemplo de acto de habla: (a) asertivo, (b) directivo, (c) conmisivo.", "c"),
        5: ("Principio de Cooperación de Grice", "La máxima que establece que debemos ser veraces en lo que decimos es la Máxima de: (a) Cantidad, (b) Calidad, (c) Relevancia.", "b"),
        6: ("Referencia", "En la oración 'La capital de Colombia es Bogotá', 'Bogotá' es el: (a) sentido, (b) referente, (c) significado.", "b"),
        7: ("Sinonimia", "Las palabras 'casa' y 'hogar' son sinónimos: (a) perfectos, (b) aproximados, (c) homónimos.", "b"),
        8: ("Homofonía", "¿Las palabras 'hola' y 'ola' son homófonos? (Sí/No)", "sí"),
        9: ("Ambigüedad", "La oración 'Vi a Juan con los binoculares' es un ejemplo de ambigüedad: (a) léxica, (b) estructural, (c) referencial.", "b"),
        10: ("Connotación", "El significado cultural o emocional asociado a la palabra 'rojo' (pasión, peligro) es su: (a) denotación, (b) connotación, (c) referencia.", "b"),
        11: ("Semántica de Marcos", "Para entender la palabra 'restaurante', activamos un marco de conocimiento que incluye 'mesas', 'comida', 'camareros'. (Verdadero/Falso)", "verdadero"),
        12: ("Pragmática", "El estudio de cómo el contexto contribuye al significado se llama: (a) semántica formal, (b) sintaxis, (c) pragmática.", "c"),
        13: ("Homonimia", "La palabra 'llama' (animal y fuego) es un ejemplo de: (a) homonimia, (b) polisemia, (c) hiponimia.", "a"),
        14: ("Hiponimia", "¿Es 'manzana' un hipónimo de 'fruta'? (Sí/No)", "sí"),
        15: ("Actos de Habla Indirectos", "Decir '¿Tienes la hora?' para pedir que te digan la hora es un acto de habla: (a) asertivo, (b) indirecto, (c) declarativo.", "b"),
        16: ("Máxima de Relevancia", "Decir 'Estoy cansado' en respuesta a '¿Quieres ir al cine?' viola la Máxima de Relevancia. (Verdadero/Falso)", "falso"),
        17: ("Antonimia", "¿'Vivir' y 'morir' son antónimos complementarios? (Sí/No)", "sí"),
        18: ("Metáfora", "La frase 'El tiempo es dinero' es un ejemplo de: (a) metonimia, (b) metáfora, (c) sinestesia.", "b"),
        19: ("Principio de Cooperación", "La máxima que dice 'Sé breve, conciso y ordenado' es la Máxima de: (a) Cantidad, (b) Calidad, (c) Manera.", "c"),
        20: ("Campo Semántico", "Las palabras 'doctor', 'enfermera', 'hospital', 'paciente' pertenecen al campo semántico de: (a) la salud, (b) las profesiones, (c) los lugares.", "a"),
        21: ("Presuposiciones", "La oración 'Lamento haber llegado tarde' presupone que el hablante: (a) llegó temprano, (b) llegó tarde, (c) no llegó.", "b"),
        22: ("Sentido vs. Referencia", "¿El sentido de la expresión 'el lucero de la mañana' es el mismo que el de 'el lucero de la tarde'? (Sí/No)", "sí"),
        23: ("Ambigüedad Léxica", "La oración 'La hoja está en el escritorio' es ambigua léxicamente. (Verdadero/Falso)", "verdadero"),
        24: ("Pragmática", "Una 'implicatura' es un significado que no se dice explícitamente, pero se infiere. (Verdadero/Falso)", "verdadero"),
        25: ("Actos de Habla", "Un acto de habla que compromete al hablante a seguir un curso de acción se llama: (a) expresivo, (b) declarativo, (c) conmisivo.", "c"),
        26: ("Antonimia", "¿'Entrar' y 'salir' son antónimos conversivos? (Sí/No)", "sí"),
        27: ("Hiponimia", "¿'Vehículo' es un hiperónimo de 'automóvil'? (Sí/No)", "sí"),
        28: ("Polisemia", "¿La palabra 'cresta' (de un gallo, de una ola) es un ejemplo de polisemia? (Sí/No)", "sí"),
        29: ("Denotación", "El significado literal de la palabra 'sol' es una estrella. (Verdadero/Falso)", "verdadero"),
        30: ("Sinonimia", "Las palabras 'rápido' y 'veloz' son sinónimos. (Verdadero/Falso)", "verdadero"),
        31: ("Metonimia", "¿Decir 'He leído a Gabriel García Márquez' en vez de 'He leído una obra de Gabriel García Márquez' es un ejemplo de metonimia? (Sí/No)", "sí"),
        32: ("Implicatura", "Si alguien dice 'La película es muy buena', pero su tono es irónico, está generando una implicatura. (Verdadero/Falso)", "verdadero"),
        33: ("Antonimia", "¿'Arriba' y 'abajo' son antónimos de tipo gradual? (Sí/No)", "no"),
        34: ("Campos Semánticos", "Las palabras 'claro', 'oscuro', 'brillante', 'opaco' pertenecen al campo semántico del: (a) color, (b) la luz, (c) la percepción.", "b"),
        35: ("Actos de Habla", "La oración 'Te ordeno que te sientes' es un acto de habla: (a) directivo, (b) asertivo, (c) expresivo.", "a"),
        36: ("Ambigüedad", "La frase 'No podemos confiar en los hombres de la tienda' es ambigua. (Verdadero/Falso)", "verdadero"),
        37: ("Homonimia", "La palabra 'vino' (verbo venir y bebida) es un caso de: (a) polisemia, (b) homonimia, (c) sinonimia.", "b"),
        38: ("Presuposiciones", "La oración 'Juan dejó de fumar' presupone que antes: (a) fumaba, (b) no fumaba, (c) nunca fumó.", "a"),
        39: ("Homonimia", "¿Las palabras 'sierra' (herramienta y montaña) son homónimos? (Sí/No)", "sí"),
        40: ("Sentido", "El 'sentido' de una expresión es su lugar en un sistema de relaciones con otras expresiones. (Verdadero/Falso)", "verdadero"),
        41: ("Pragmática", "La 'deixis' se refiere al uso de palabras que dependen del contexto para su significado, como 'yo', 'aquí', 'ahora'. (Verdadero/Falso)", "verdadero"),
        42: ("Metonimia", "¿La frase 'El violín está desafinado' es un ejemplo de metonimia 'INSTRUMENTO POR PRODUCTO'? (Sí/No)", "no"),
        43: ("Antonimia", "¿'Esposo' y 'esposa' son antónimos conversivos? (Sí/No)", "sí"),
        44: ("Campo Semántico", "Las palabras 'triste', 'feliz', 'enfadado', 'calmado' pertenecen al campo semántico de las emociones. (Verdadero/Falso)", "verdadero"),
        45: ("Actos de Habla", "Los actos de habla 'declarativos' cambian el estado del mundo. (Verdadero/Falso)", "verdadero"),
        46: ("Hiponimia", "¿'Gato' es un hiperónimo de 'felino'? (Sí/No)", "no"),
        47: ("Máxima de Relevancia", "Si alguien pregunta '¿Qué hora es?' y respondes 'La oficina de correos ya cerró', estás violando la Máxima de Relevancia. (Verdadero/Falso)", "verdadero"),
        48: ("Polisemia", "La palabra 'llama' (del fuego y animal) es un ejemplo de polisemia. (Verdadero/Falso)", "falso"),
        49: ("Sinonimia", "¿'Automóvil' y 'coche' son sinónimos aproximados? (Sí/No)", "no"),
        50: ("Connotación", "La connotación de la palabra 'serpiente' suele ser negativa. (Verdadero/Falso)", "verdadero"),
        51: ("Actos de Habla", "Un acto de habla 'asertivo' compromete al hablante con la verdad de una proposición. (Verdadero/Falso)", "verdadero"),
        52: ("Antonimia", "¿'Vivo' y 'muerto' son antónimos graduales? (Sí/No)", "no"),
        53: ("Metonimia", "El uso de 'la espada' para referirse al 'poder militar' es un ejemplo de metonimia. (Verdadero/Falso)", "verdadero"),
        54: ("Pragmática", "Las 'implicaturas convencionales' se derivan del significado de las palabras, no del contexto. (Verdadero/Falso)", "verdadero"),
        55: ("Hiponimia", "Los hipónimos de 'herramienta' incluyen 'martillo' y 'sierra'. (Verdadero/Falso)", "verdadero"),
        56: ("Semántica de Marcos", "El marco de conocimiento para la palabra 'cumpleaños' incluye 'pastel', 'velas' y 'regalos'. (Verdadero/Falso)", "verdadero"),
        57: ("Homonimia", "¿Las palabras 'tubo' y 'tuvo' son homógrafas? (Sí/No)", "no"),
        58: ("Ambigüedad", "La frase 'La gente del pueblo es muy hospitalaria' es un ejemplo de ambigüedad. (Verdadero/Falso)", "falso"),
        59: ("Campo Semántico", "Las palabras 'desayuno', 'almuerzo', 'cena' pertenecen al campo semántico de las comidas. (Verdadero/Falso)", "verdadero"),
        60: ("Principio de Cooperación", "Violar una máxima de Grice para generar una implicatura se llama: (a) malversación, (b) violación, (c) transgresión.", "c"),
        61: ("Referencia", "El 'referente' de una expresión es el objeto o entidad en el mundo real al que se refiere. (Verdadero/Falso)", "verdadero"),
        62: ("Polisemia", "La palabra 'raíz' (de un árbol, de un problema) es un ejemplo de polisemia. (Verdadero/Falso)", "verdadero"),
        63: ("Actos de Habla", "¿'Te declaro marido y mujer' es un acto de habla declarativo? (Sí/No)", "sí"),
        64: ("Antonimia", "¿'Comprar' y 'vender' son antónimos conversivos? (Sí/No)", "sí"),
        65: ("Connotación", "La palabra 'solterón' tiene una connotación negativa en comparación con 'soltero'. (Verdadero/Falso)", "verdadero"),
        66: ("Homonimia", "Las palabras 'raya' (línea y pez) son un ejemplo de homonimia. (Verdadero/Falso)", "verdadero"),
        67: ("Pragmática", "El significado que se infiere de la frase 'Hace frío aquí' para que alguien cierre la puerta es una implicatura: (a) convencional, (b) conversacional, (c) semántica.", "b"),
        68: ("Hiponimia", "¿'Flor' es un hiperónimo de 'rosa'? (Sí/No)", "sí"),
        69: ("Actos de Habla", "La oración '¡Qué día tan bonito!' es un acto de habla: (a) asertivo, (b) expresivo, (c) directivo.", "b"),
        70: ("Metáfora", "La metáfora 'LOS ARGUMENTOS SON EDIFICIOS' se basa en la frase 'El fundamento de tu argumento'. (Verdadero/Falso)", "verdadero"),
        71: ("Ambigüedad", "La frase 'El carro de mi primo está roto' es ambigua. (Verdadero/Falso)", "falso"),
        72: ("Campo Semántico", "Las palabras 'rojo', 'azul', 'amarillo', 'verde' pertenecen al campo semántico de los colores. (Verdadero/Falso)", "verdadero"),
        73: ("Polisemia", "¿La palabra 'corte' (de carne y de cabello) es un ejemplo de polisemia? (Sí/No)", "sí"),
        74: ("Sinonimia", "Las palabras 'alegre' y 'contento' son sinónimos. (Verdadero/Falso)", "verdadero"),
        75: ("Presuposiciones", "La pregunta '¿Cuándo nació Juan?' presupone que: (a) Juan murió, (b) Juan nació, (c) Juan es un adulto.", "b"),
        76: ("Antonimia", "¿'Fácil' y 'difícil' son antónimos graduales? (Sí/No)", "sí"),
        77: ("Homonimia", "Las palabras 'baca' y 'vaca' son homófonos. (Verdadero/Falso)", "verdadero"),
        78: ("Pragmática", "La 'cortesía' en la comunicación es un concepto estudiado por la pragmática. (Verdadero/Falso)", "verdadero"),
        79: ("Hipo-hiperonimia", "La relación entre 'fruta' y 'manzana' es de hiponimia. (Verdadero/Falso)", "verdadero"),
        80: ("Actos de Habla", "Un acto de habla que sirve para que el hablante se disculpe o felicite se llama: (a) directivo, (b) expresivo, (c) declarativo.", "b"),
        81: ("Ambigüedad Estructural", "¿La frase 'El perro de la casa es grande' tiene ambigüedad estructural? (Sí/No)", "no"),
        82: ("Metonimia", "¿La frase 'Necesito un bolígrafo' cuando en realidad necesitas tinta es un ejemplo de metonimia? (Sí/No)", "no"),
        83: ("Campo Semántico", "Las palabras 'correr', 'saltar', 'caminar', 'nadar' pertenecen al campo semántico de los verbos de movimiento. (Verdadero/Falso)", "verdadero"),
        84: ("Referencia", "La expresión 'la reina de Inglaterra' es un ejemplo de: (a) referencia fija, (b) referencia variable, (c) referencia semántica.", "a"),
        85: ("Polisemia", "La palabra 'pico' (de ave, de montaña, de herramienta) es un ejemplo de polisemia. (Verdadero/Falso)", "verdadero"),
        86: ("Principio de Cooperación", "Si alguien te pregunta '¿A qué hora cierran los bancos?' y respondes 'La oficina de correos ya cerró', estás violando la máxima de: (a) cantidad, (b) calidad, (c) relevancia.", "c"),
        87: ("Sinonimia", "Las palabras 'guerra' y 'conflicto' son sinónimos. (Verdadero/Falso)", "verdadero"),
        88: ("Actos de Habla", "¿'Bautizo esta nave con el nombre de Colombia' es un acto de habla declarativo? (Sí/No)", "sí"),
        89: ("Homonimia", "¿Las palabras 'sal' (condimento y del verbo salir) son homónimos? (Sí/No)", "sí"),
        90: ("Antonimia", "Los antónimos 'grande' y 'pequeño' son antónimos: (a) graduales, (b) complementarios, (c) conversivos.", "a"),
        91: ("Campo Semántico", "Las palabras 'correr', 'caminar', 'nadar' y 'volar' pertenecen al campo semántico del movimiento. (Verdadero/Falso)", "verdadero"),
        92: ("Pragmática", "¿La semántica y la pragmática son ramas de la lingüística que estudian el significado? (Sí/No)", "sí"),
        93: ("Hiponimia", "La relación entre 'animal' y 'perro' es de: (a) sinonimia, (b) hiponimia, (c) hiperonimia.", "b"),
        94: ("Connotación", "La connotación de 'dictadura' es negativa. (Verdadero/Falso)", "verdadero"),
        95: ("Actos de Habla", "¿La oración '¡Qué bonita!' puede ser un acto de habla expresivo? (Sí/No)", "sí"),
        96: ("Homonimia", "Las palabras 'caro' y 'carro' son homófonos en la mayoría de los dialectos de español. (Verdadero/Falso)", "falso"),
        97: ("Antonimia", "¿'Comprar' y 'vender' son antónimos conversivos? (Sí/No)", "sí"),
        98: ("Campo Semántico", "Las palabras 'computador', 'teclado', 'ratón', 'pantalla' pertenecen al campo semántico de la tecnología. (Verdadero/Falso)", "verdadero"),
        99: ("Pragmática", "El significado que se comunica en la oración 'Estoy en el banco' depende de: (a) la sintaxis, (b) el contexto, (c) la morfología.", "b"),
        100: ("Semántica", "La semántica formal se centra en el significado en relación a la lógica y la verdad. (Verdadero/Falso)", "verdadero"),
    }

    print("¡Bienvenido al reto de Semántica!")
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
