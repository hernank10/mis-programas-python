# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Lingüística Cognitiva
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre la relación entre el lenguaje,
# la cognición y la experiencia corporal humana.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    exercises = {
        1: ("Metáforas Conceptuales", "Según George Lakoff y Mark Johnson, la metáfora 'EL AMOR ES UNA GUERRA' es un ejemplo de: (a) metáfora ontológica, (b) metáfora orientacional, (c) metáfora estructural.", "c"),
        2: ("Teoría de Prototipos", "El concepto de que ciertas entidades son miembros más representativos de una categoría que otras (por ejemplo, un gorrión es un 'pájaro' más prototípico que un pingüino) se llama: (a) efecto de prototipo, (b) categoría básica, (c) radialidad.", "a"),
        3: ("Gramática Cognitiva", "Según Ronald Langacker, la 'figura' es la entidad más prominente dentro de una 'escena' (ground). (Verdadero/Falso)", "verdadero"),
        4: ("Semántica de Marcos", "La teoría de Charles Fillmore que propone que para entender una palabra es necesario activar un conjunto de conocimientos asociados se conoce como: (a) gramática generativa, (b) semántica de marcos, (c) teoría de los espacios mentales.", "b"),
        5: ("Metonimia", "El uso de 'la Casa Blanca' para referirse a la administración presidencial es un ejemplo de: (a) metáfora, (b) metonimia, (c) sinestesia.", "b"),
        6: ("Embodied Cognition", "La hipótesis que sostiene que el lenguaje se basa en nuestra experiencia corporal y sensorial se llama: (a) cognición encarnada, (b) racionalismo, (c) innatismo.", "a"),
        7: ("Espacios Mentales", "Según Gilles Fauconnier, los 'espacios mentales' son estructuras que se crean en la mente para: (a) organizar el léxico, (b) construir significado en el discurso, (c) generar oraciones gramaticales.", "b"),
        8: ("Esquemas de Imagen", "El esquema de imagen 'CONTENEDOR' (container) nos permite entender conceptos como 'entrar' y 'salir'. (Verdadero/Falso)", "verdadero"),
        9: ("Metáfora Conceptual", "La frase 'Estoy en la cima del mundo' es un ejemplo de metáfora: (a) ontológica, (b) orientacional, (c) estructural.", "b"),
        10: ("Gramática Cognitiva", "La 'subjetividad' es un concepto clave en la gramática de Langacker que se refiere a la perspectiva del hablante. (Verdadero/Falso)", "verdadero"),
        11: ("Prototipos", "Según Eleanor Rosch, un 'nivel básico de categorización' es el más informativo y cognitivamente saliente. ¿Es 'mesa' un nivel básico, más que 'mueble' o 'mesa de cocina'? (Sí/No)", "sí"),
        12: ("Blended Spaces", "La 'fusión conceptual' (conceptual blending) ocurre cuando dos o más espacios mentales se combinan para crear un nuevo espacio. (Verdadero/Falso)", "verdadero"),
        13: ("Metáfora Conceptual", "La frase 'El tiempo es dinero' es una metáfora de tipo: (a) estructural, (b) orientacional, (c) ontológica.", "a"),
        14: ("Cognición", "La lingüística cognitiva sostiene que la gramática no es un módulo autónomo, sino que emerge de la: (a) biología, (b) cognición general, (c) sociología.", "b"),
        15: ("Esquemas de Imagen", "Los esquemas de imagen son abstracciones de la experiencia corporal que subyacen a conceptos abstractos. (Verdadero/Falso)", "verdadero"),
        16: ("Modelos Cognitivos Idealizados (ICMs)", "Los ICMs son estructuras de conocimiento organizadas que usamos para dar sentido a las palabras. El ICM del 'soltero' incluye conceptos como 'hombre', 'adulto', 'soltero'. (Verdadero/Falso)", "verdadero"),
        17: ("Semántica Cognitiva", "La frase '¡Se acabó el tiempo!' se basa en la metáfora conceptual: (a) EL TIEMPO ES UN RECURSO FINITO, (b) EL TIEMPO ES UN CONTENEDOR, (c) EL TIEMPO ES UN OBJETO.", "a"),
        18: ("Metonimia", "¿El uso de 'Hollywood' para referirse a la industria cinematográfica es un ejemplo de metonimia? (Sí/No)", "sí"),
        19: ("Gramática Cognitiva", "El 'profile' de una expresión en la Gramática Cognitiva es la parte de su significado que se 'perfila' o se enfatiza. (Verdadero/Falso)", "verdadero"),
        20: ("Blended Spaces", "La frase 'Los ordenadores se están comiendo el mundo' es un ejemplo de: (a) metáfora, (b) metonimia, (c) fusión conceptual.", "c"),
        21: ("Teoría de Prototipos", "Según esta teoría, las categorías no tienen límites definidos, sino que se superponen entre sí. (Verdadero/Falso)", "verdadero"),
        22: ("Esquemas de Imagen", "El esquema de imagen 'FUERZA' (force) se usa para entender conceptos como 'influencia' y 'causa'. (Verdadero/Falso)", "verdadero"),
        23: ("Léxico", "La lingüística cognitiva sugiere que el significado léxico es: (a) estático y definido, (b) dinámico y basado en el uso, (c) independiente del contexto.", "b"),
        24: ("Cognición", "¿La Lingüística Cognitiva se opone a la idea de que el lenguaje tiene una base biológica innata? (Sí/No)", "no"),
        25: ("Metáfora Conceptual", "La frase 'Tengo una larga historia' utiliza la metáfora conceptual 'LA VIDA ES UN VIAJE'. (Verdadero/Falso)", "verdadero"),
        26: ("Espacios Mentales", "Un 'espacio mental de referencia' es el espacio principal que se crea al inicio de un discurso. (Verdadero/Falso)", "verdadero"),
        27: ("Metonimia", "La metonimia 'PARTE POR EL TODO' se usa en la frase: 'Tengo cuatro bocas que alimentar'. (Verdadero/Falso)", "verdadero"),
        28: ("Gramática Cognitiva", "Según Langacker, la 'ruta conceptual' (conceptual path) se utiliza para describir eventos dinámicos. (Verdadero/Falso)", "verdadero"),
        29: ("Prototipos", "¿Un 'silla de playa' es un miembro prototípico de la categoría 'silla'? (Sí/No)", "no"),
        30: ("Embodied Cognition", "La experiencia de 'calor' en la frase 'una cálida bienvenida' se basa en una metáfora sensorial. (Verdadero/Falso)", "verdadero"),
        31: ("Semántica", "La lingüística cognitiva enfatiza la relación entre el significado y la experiencia humana. (Verdadero/Falso)", "verdadero"),
        32: ("Metáfora Conceptual", "La frase 'Está al borde de la desesperación' utiliza la metáfora 'LAS EMOCIONES SON CONTENEDORES'. (Verdadero/Falso)", "falso"),
        33: ("Esquemas de Imagen", "El esquema 'ARRIBA-ABAJO' (up-down) se utiliza para entender conceptos como 'feliz' y 'triste'. (Verdadero/Falso)", "verdadero"),
        34: ("Gramática Cognitiva", "¿El 'ground' o fondo es la entidad más destacada en una escena conceptual? (Sí/No)", "no"),
        35: ("Léxico", "El significado de una palabra se puede representar como una 'red de asociaciones' en el léxico mental. (Verdadero/Falso)", "verdadero"),
        36: ("Blended Spaces", "El resultado de una fusión conceptual se conoce como: (a) espacio genérico, (b) espacio de entrada, (c) espacio fusionado.", "c"),
        37: ("Metáfora", "La metáfora 'LOS ARGUMENTOS SON EDIFICIOS' se basa en la frase: 'Su argumento es sólido'. (Verdadero/Falso)", "verdadero"),
        38: ("Metonimia", "¿La metonimia 'AUTOR POR OBRA' se usa en la frase 'He leído a Cervantes'? (Sí/No)", "sí"),
        39: ("Gramática Cognitiva", "El 'concepto base' de una expresión es el conocimiento enciclopédico sobre el que se construye su significado. (Verdadero/Falso)", "verdadero"),
        40: ("Cognición", "El modelo 'cajón de sastre' de la cognición humana propone que el lenguaje es un módulo aislado. (Verdadero/Falso)", "falso"),
        41: ("Esquemas de Imagen", "El esquema de imagen 'TRAYECTORIA' (path) se usa para entender verbos como 'correr' y 'volar'. (Verdadero/Falso)", "verdadero"),
        42: ("Metáfora Conceptual", "La metáfora 'LA INFLACIÓN ES UN ENFERMO' es un ejemplo de: (a) metáfora ontológica, (b) metáfora orientacional, (c) metáfora estructural.", "a"),
        43: ("Teoría de Prototipos", "¿La 'teoría de la categorización clásica' sostiene que las categorías tienen límites definidos? (Sí/No)", "sí"),
        44: ("Blended Spaces", "La frase 'El cirujano fue un carnicero' es un ejemplo de: (a) metáfora, (b) fusión conceptual, (c) metonimia.", "b"),
        45: ("Cognición", "La lingüística cognitiva se centra en la relación entre lenguaje, mente y: (a) sociedad, (b) neurociencia, (c) experiencia.", "c"),
        46: ("Gramática Cognitiva", "En la gramática de Langacker, la 'prominencia' de un elemento en una escena se llama: (a) figura, (b) ground, (c) perfil.", "a"),
        47: ("Metonimia", "¿La metonimia 'PARTE POR EL TODO' se usa en la frase 'El violín está desafinado'? (Sí/No)", "sí"),
        48: ("Teoría de Prototipos", "¿El color 'rojo' es un prototipo más fuerte que el color 'borgoña'? (Sí/No)", "sí"),
        49: ("Semántica", "La 'polisemia' (múltiples significados relacionados en una palabra) es un fenómeno central en la semántica cognitiva. (Verdadero/Falso)", "verdadero"),
        50: ("Cognición", "La lingüística cognitiva es una reacción a la teoría de Noam Chomsky. (Verdadero/Falso)", "verdadero"),
        51: ("Metáfora Conceptual", "La frase 'Tienes que caminar antes de correr' se basa en la metáfora 'EL DESARROLLO ES UN VIAJE'. (Verdadero/Falso)", "verdadero"),
        52: ("Espacios Mentales", "Un 'espacio de entrada' es un espacio mental que se introduce para construir una fusión conceptual. (Verdadero/Falso)", "verdadero"),
        53: ("Metonimia", "¿La metonimia 'CONTENEDOR POR CONTENIDO' se usa en la frase 'Me he bebido tres vasos'? (Sí/No)", "sí"),
        54: ("Gramática Cognitiva", "El 'punto de vista' de un hablante se conoce como 'perspectivización' en la gramática de Langacker. (Verdadero/Falso)", "verdadero"),
        55: ("Esquemas de Imagen", "El esquema de imagen 'VÍNCULO' (link) se usa para entender relaciones como 'conexión' y 'parentesco'. (Verdadero/Falso)", "verdadero"),
        56: ("Teoría de Prototipos", "Según Rosch, las categorías se definen por: (a) una lista de rasgos esenciales, (b) similitud a un prototipo, (c) ambos.", "b"),
        57: ("Cognición", "¿El estudio del lenguaje en la lingüística cognitiva es independiente de la psicología y la neurociencia? (Sí/No)", "no"),
        58: ("Metáfora Conceptual", "La metáfora 'LAS IDEAS SON COMIDA' se basa en la frase 'Tengo hambre de conocimiento'. (Verdadero/Falso)", "verdadero"),
        59: ("Espacios Mentales", "Los espacios mentales pueden ser de: (a) tiempo, (b) realidad, (c) ambos.", "c"),
        60: ("Gramática Cognitiva", "La 'simbolización' es el proceso de asociar un sonido con un concepto en el léxico. (Verdadero/Falso)", "verdadero"),
        61: ("Embodied Cognition", "La frase 'una idea pesada' se basa en la experiencia de peso físico. (Verdadero/Falso)", "verdadero"),
        62: ("Metonimia", "¿El uso de 'Cerebro' para referirse a una persona inteligente es un ejemplo de metonimia? (Sí/No)", "sí"),
        63: ("Teoría de Prototipos", "El 'efecto de la prototipicidad' se refiere a que los miembros más prototípicos de una categoría son procesados más rápido. (Verdadero/Falso)", "verdadero"),
        64: ("Esquemas de Imagen", "El esquema de imagen 'COMPULSIÓN' (compulsion) se usa para entender verbos como 'forzar' y 'presionar'. (Verdadero/Falso)", "verdadero"),
        65: ("Blended Spaces", "Una fusión conceptual crea una nueva estructura de significado que hereda características de los espacios de entrada. (Verdadero/Falso)", "verdadero"),
        66: ("Metáfora Conceptual", "La frase 'El argumento cayó por su propio peso' se basa en la metáfora: (a) LAS IDEAS SON OBJETOS, (b) LOS ARGUMENTOS SON EDIFICIOS, (c) LAS IDEAS SON PESADAS.", "a"),
        67: ("Gramática Cognitiva", "¿El 'perfil' de una expresión en la gramática de Langacker es un subconjunto de su 'dominio'? (Sí/No)", "sí"),
        68: ("Metonimia", "El uso de 'la espada' para referirse al 'poder militar' es un ejemplo de metonimia 'INSTRUMENTO POR ACCIÓN'. (Verdadero/Falso)", "verdadero"),
        69: ("Cognición", "La lingüística cognitiva se centra en el estudio del lenguaje como un sistema: (a) formal, (b) simbólico, (c) experiencial.", "c"),
        70: ("Espacios Mentales", "El 'espacio genérico' en la teoría de los espacios mentales contiene la estructura compartida por los espacios de entrada. (Verdadero/Falso)", "verdadero"),
        71: ("Esquemas de Imagen", "El esquema de imagen 'COMPLEMENTO' (complement) se usa para entender la relación entre un todo y sus partes. (Verdadero/Falso)", "falso"),
        72: ("Metáfora Conceptual", "La frase 'El debate se calentó' usa la metáfora 'LAS EMOCIONES SON TEMPERATURA'. (Verdadero/Falso)", "verdadero"),
        73: ("Teoría de Prototipos", "La categoría de 'aves' se considera una categoría básica. (Verdadero/Falso)", "verdadero"),
        74: ("Gramática Cognitiva", "La 'convencionalización' en el lenguaje se refiere al proceso de hacer que un uso lingüístico se vuelva una convención social. (Verdadero/Falso)", "verdadero"),
        75: ("Metonimia", "El uso de 'un Picasso' para referirse a un cuadro pintado por Picasso es un ejemplo de metonimia. (Verdadero/Falso)", "verdadero"),
        76: ("Embodied Cognition", "La hipótesis de la cognición encarnada sugiere que las estructuras abstractas del lenguaje se derivan de la experiencia motora. (Verdadero/Falso)", "verdadero"),
        77: ("Espacios Mentales", "¿Los espacios mentales son estructuras permanentes en la mente del hablante? (Sí/No)", "no"),
        78: ("Esquemas de Imagen", "El esquema de imagen 'LINKAGE' se utiliza para entender las relaciones causales. (Verdadero/Falso)", "verdadero"),
        79: ("Cognición", "¿La lingüística cognitiva se enfoca en el lenguaje como un fenómeno social, no solo individual? (Sí/No)", "sí"),
        80: ("Metáfora Conceptual", "La frase 'La ira es una explosión' es un ejemplo de metáfora que se deriva de la experiencia física. (Verdadero/Falso)", "verdadero"),
        81: ("Teoría de Prototipos", "Los 'ejemplares' son miembros específicos de una categoría que se usan como puntos de referencia. (Verdadero/Falso)", "verdadero"),
        82: ("Gramática Cognitiva", "¿El 'dominio' es el conocimiento enciclopédico de fondo para una expresión? (Sí/No)", "sí"),
        83: ("Metonimia", "El uso de 'la prensa' para referirse a 'los periodistas' es un ejemplo de metonimia. (Verdadero/Falso)", "verdadero"),
        84: ("Esquemas de Imagen", "El esquema de imagen 'PROXIMIDAD' (proximity) se usa para entender la cercanía en el espacio y en las relaciones. (Verdadero/Falso)", "verdadero"),
        85: ("Blended Spaces", "La fusión conceptual es un proceso creativo que puede generar nuevos significados. (Verdadero/Falso)", "verdadero"),
        86: ("Metáfora Conceptual", "La frase 'Mi cabeza es una olla a presión' usa la metáfora 'EL CUERPO ES UN CONTENEDOR'. (Verdadero/Falso)", "verdadero"),
        87: ("Cognición", "La lingüística cognitiva considera que la gramática es un sistema de reglas: (a) abstractas, (b) simbólicas, (c) conceptuales.", "c"),
        88: ("Teoría de Prototipos", "¿Un 'elefante' es un prototipo para la categoría 'mamífero'? (Sí/No)", "sí"),
        89: ("Metonimia", "El uso de 'pluma' para referirse al 'estilo de un escritor' es un ejemplo de metonimia 'INSTRUMENTO POR ESTILO'. (Verdadero/Falso)", "verdadero"),
        90: ("Esquemas de Imagen", "El esquema de imagen 'FUERZA' se usa para entender verbos como 'empujar' y 'tirar'. (Verdadero/Falso)", "verdadero"),
        91: ("Blended Spaces", "El 'blending' se refiere a la creación de nuevas ideas a partir de la mezcla de conceptos preexistentes. (Verdadero/Falso)", "verdadero"),
        92: ("Metáfora Conceptual", "¿La metáfora 'LAS TEORÍAS SON EDIFICIOS' se basa en la frase 'El fundamento de la teoría'? (Sí/No)", "sí"),
        93: ("Gramática Cognitiva", "La 'perspectivización' en la gramática de Langacker se refiere al punto de vista del observador. (Verdadero/Falso)", "verdadero"),
        94: ("Cognición", "La lingüística cognitiva se interesa en cómo el lenguaje moldea o es moldeado por el pensamiento. (Verdadero/Falso)", "verdadero"),
        95: ("Teoría de Prototipos", "Los 'miembros periféricos' de una categoría son menos representativos que los prototipos. (Verdadero/Falso)", "verdadero"),
        96: ("Metáfora", "La frase 'El tiempo es un ladrón' se basa en la metáfora: (a) EL TIEMPO ES UN OBJETO, (b) EL TIEMPO ES UNA PERSONA, (c) EL TIEMPO ES UN RECURSO.", "b"),
        97: ("Gramática Cognitiva", "La 'convencionalización' es el proceso por el cual una expresión o construcción se vuelve de uso común en una lengua. (Verdadero/Falso)", "verdadero"),
        98: ("Blended Spaces", "Un 'espacio genérico' contiene elementos que son comunes a los espacios de entrada. (Verdadero/Falso)", "verdadero"),
        99: ("Embodied Cognition", "La frase 'Tengo una idea brillante' se basa en una experiencia sensorial de luz. (Verdadero/Falso)", "verdadero"),
        100: ("Lingüística Cognitiva", "La lingüística cognitiva se centra en el estudio del lenguaje como un sistema abstracto, sin relación con el cuerpo o la mente. (Verdadero/Falso)", "falso"),
    }

    print("¡Bienvenido al reto de Lingüística Cognitiva!")
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
