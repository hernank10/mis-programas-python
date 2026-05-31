# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Lingüística Hispanoamericana
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre las variedades del español
# en Hispanoamérica, su léxico, fonética, sintaxis y contacto de lenguas.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    exercises = {
        1: ("Voseo", "El voseo es el uso de 'vos' en lugar de 'tú'. ¿En qué país es un rasgo común?", "Argentina"),
        2: ("Yeísmo Rehilado", "La pronunciación fricativa de 'll' y 'y' en 'calle' o 'yo' es común en el Cono Sur. ¿Cómo se llama este fenómeno?", "yeísmo rehilado"),
        3: ("Seseo", "¿Es el seseo (pronunciación de 'z' y 'c' como 's') un rasgo fonético predominante en Hispanoamérica? (Sí/No)", "sí"),
        4: ("Indigenismo (Quechua)", "La palabra 'cancha' (terreno deportivo) es un indigenismo. ¿De qué lengua proviene?", "quechua"),
        5: ("Léxico Regional (México)", "En México, la palabra 'chamba' significa: (a) trabajo, (b) fiesta, (c) comida.", "a"),
        6: ("Sintaxis Regional", "El uso de 'por qué' en preguntas indirectas como 'pregúntale por qué vino' es común en: (a) Argentina, (b) México, (c) Colombia.", "b"),
        7: ("Aspiración de 's'", "El fonema /s/ al final de sílaba se aspira o elide en: (a) el Cono Sur, (b) la zona andina, (c) el Caribe.", "c"),
        8: ("Léxico Regional (Caribe)", "En Cuba, una 'guagua' es: (a) un niño, (b) un autobús, (c) un animal.", "b"),
        9: ("Indigenismo (Náhuatl)", "La palabra 'chocolate' es un indigenismo. ¿De qué lengua proviene?", "náhuatl"),
        10: ("Voseo Mixto", "El voseo en Colombia, que combina el pronombre 'vos' con la conjugación verbal de 'tú' ('vos tienes'), es un voseo: (a) verbal, (b) pronominal, (c) mixto.", "c"),
        11: ("Léxico Regional (Colombia)", "En Colombia, una 'luciernaga' se conoce como: (a) chispita, (b) cocuyo, (c) luciérnaga.", "b"),
        12: ("Léxico Regional (Chile)", "En Chile, a un 'niño' se le conoce como: (a) pibe, (b) chamaco, (c) cabro.", "c"),
        13: ("Fonética Regional", "La 'j' (jota) en algunos dialectos caribeños se pronuncia como una 'h' suave. ¿Verdadero o Falso?", "verdadero"),
        14: ("Indigenismo (Guaraní)", "La palabra 'yaguareté' es un indigenismo. ¿De qué lengua proviene?", "guaraní"),
        15: ("Léxico Regional (Cono Sur)", "En Argentina y Uruguay, un 'pibe' es: (a) un niño, (b) un anciano, (c) un animal.", "a"),
        16: ("Contacto de Lenguas", "El 'spanglish' en la frontera de EE. UU. y México es un ejemplo de: (a) criollo, (b) pidgin, (c) lenguas en contacto.", "c"),
        17: ("Léxico Regional (Perú)", "En Perú, 'chullo' (gorro con orejeras) es un préstamo del: (a) Quechua, (b) Aymara, (c) Náhuatl.", "a"),
        18: ("Gramática Regional", "El uso de 'haiga' en lugar de 'haya' es un rasgo: (a) normativo, (b) arcaizante, (c) moderno.", "b"),
        19: ("Léxico Regional (Andino)", "En la zona andina, un 'poncho' es un indigenismo. ¿De qué lengua proviene?", "quechua"),
        20: ("Fonética Regional (Andes)", "La 'v' se pronuncia como 'b' en toda Hispanoamérica. ¿Cómo se llama este fenómeno?", "betacismo"),
        21: ("Léxico Regional (Venezuela)", "En Venezuela, 'chévere' significa: (a) difícil, (b) genial, (c) triste.", "b"),
        22: ("Historia del Español en América", "¿Qué evento marcó el inicio del español en el continente americano?", "el descubrimiento de américa"),
        23: ("Indigenismo (Arawak)", "La palabra 'canoa' es un indigenismo. ¿De qué lengua caribeña proviene?", "arawak"),
        24: ("Léxico Regional (Uruguay)", "En Uruguay, un 'celular' se le dice: (a) móvil, (b) celular, (c) celular.", "c"),
        25: ("Fonética Regional (El Salvador)", "En El Salvador, es común la 's' al final de sílaba con pronunciación: (a) fuerte, (b) aspirada, (c) elidida.", "b"),
        26: ("Léxico Regional (México)", "En México, una 'playera' es: (a) una camiseta, (b) una toalla de playa, (c) una maleta.", "a"),
        27: ("Voseo y Clases Sociales", "¿El voseo es un rasgo de clase social alta, baja o ambas?", "ambas"),
        28: ("Indigenismo (Taino)", "La palabra 'ají' (pimiento) es un indigenismo de: (a) Taíno, (b) Náhuatl.", "a"),
        29: ("Léxico Regional (Perú)", "En Perú, 'palta' es la palabra para: (a) aguacate, (b) sandía, (c) piña.", "a"),
        30: ("Fonética Regional (Chile)", "En Chile, la 'd' intervocálica se pierde en el habla informal. ¿Verdadero o Falso?", "verdadero"),
        31: ("Léxico Regional (Costa Rica)", "En Costa Rica, un 'tico' es: (a) un nativo de Costa Rica, (b) un extranjero, (c) un tipo de árbol.", "a"),
        32: ("Indigenismo (Maya)", "La palabra 'cenote' es un indigenismo del: (a) Quechua, (b) Maya, (c) Guaraní.", "b"),
        33: ("Léxico Regional (Colombia)", "En Colombia, una 'pola' es: (a) una pelota, (b) una cerveza, (c) una persona.", "b"),
        34: ("Fonética Regional (Andes)", "El español andino mantiene la 's' final de sílaba. ¿Verdadero o Falso?", "verdadero"),
        35: ("Léxico Regional (Honduras)", "En Honduras, un 'catracho' es: (a) un animal, (b) un nativo de Honduras, (c) un tipo de fruta.", "b"),
        36: ("Indigenismo (Mapudungún)", "La palabra 'pala' (herramienta) es un indigenismo del: (a) Náhuatl, (b) Mapudungún.", "a"),
        37: ("Léxico Regional (Puerto Rico)", "En Puerto Rico, una 'china' es: (a) una niña, (b) una naranja, (c) una sandía.", "b"),
        38: ("Sintaxis Regional", "El uso del pronombre 'vosotros' es común en Hispanoamérica. (Verdadero o Falso)", "falso"),
        39: ("Léxico Regional (Ecuador)", "En Ecuador, un 'guagua' es: (a) un autobús, (b) un niño, (c) un juguete.", "b"),
        40: ("Fonética Regional (Caribe)", "En el español caribeño, la 'r' final de sílaba se pronuncia como 'l'. ¿Cómo se llama este fenómeno?", "rotacismo"),
        41: ("Léxico Regional (Bolivia)", "En Bolivia, 'chola' se usa para referirse a una mujer: (a) de origen indígena, (b) una mujer de la ciudad, (c) una mujer de clase alta.", "a"),
        42: ("Indigenismo (Taíno)", "La palabra 'huracán' es un indigenismo. ¿De qué lengua proviene?", "taíno"),
        43: ("Léxico Regional (Cuba)", "En Cuba, un 'carro' se conoce como: (a) coche, (b) carro, (c) máquina.", "c"),
        44: ("Fonética Regional (Argentina)", "La pronunciación de 'll' y 'y' como 'sh' es característica de: (a) el voseo, (b) el rioplatense, (c) el seseo.", "b"),
        45: ("Indigenismo (Quechua)", "La palabra 'condor' es un indigenismo. ¿De qué lengua proviene?", "quechua"),
        46: ("Léxico Regional (Centroamérica)", "En Centroamérica, 'patojo' es un término para: (a) niño, (b) adulto, (c) anciano.", "a"),
        47: ("Sintaxis Regional (Colombia)", "El 'ustedeo' es el uso de 'usted' con el verbo de 'tú' en: (a) Colombia, (b) España, (c) México.", "a"),
        48: ("Indigenismo (Náhuatl)", "La palabra 'aguacate' es un indigenismo. ¿De qué lengua proviene?", "náhuatl"),
        49: ("Léxico Regional (Venezuela)", "En Venezuela, 'cotufa' es: (a) palomitas de maíz, (b) un juguete, (c) una comida.", "a"),
        50: ("Historia del Español en América", "¿Qué factor fue más determinante en la evolución de los dialectos hispanoamericanos?", "el aislamiento geográfico"),
        51: ("Fonética Regional (Chile)", "La 'rr' se pronuncia con un sonido más relajado en: (a) México, (b) Colombia, (c) Chile.", "c"),
        52: ("Léxico Regional (Ecuador)", "En Ecuador, 'funda' es: (a) una mochila, (b) una bolsa, (c) una maleta.", "b"),
        53: ("Indigenismo (Tupí)", "La palabra 'jaguar' es un indigenismo. ¿De qué lengua proviene?", "tupí"),
        54: ("Sintaxis Regional (México)", "El uso de la preposición 'a' con verbos como 'hablar a' es común en: (a) Colombia, (b) España, (c) México.", "c"),
        55: ("Léxico Regional (Argentina)", "En Argentina, un 'bondi' es: (a) un coche, (b) un autobús, (c) un tren.", "b"),
        56: ("Fonética Regional (El Salvador)", "En El Salvador, la 'r' intervocálica se pronuncia con una fricción. ¿Cómo se llama este fenómeno?", "asibilación"),
        57: ("Indigenismo (Aymara)", "La palabra 'lápiz' es un indigenismo de: (a) Quechua, (b) Aymara.", "b"),
        58: ("Léxico Regional (Panamá)", "En Panamá, un 'chino' es: (a) un niño, (b) un supermercado, (c) un amigo.", "b"),
        59: ("Fonética Regional (México)", "El español mexicano es conocido por su entonación: (a) plana, (b) ascendente, (c) descendente.", "a"),
        60: ("Indigenismo (Mapudungún)", "La palabra 'mapuche' significa 'gente de la tierra' en: (a) Quechua, (b) Mapudungún, (c) Guaraní.", "b"),
        61: ("Léxico Regional (Colombia)", "En Colombia, 'parce' es un sinónimo de: (a) amigo, (b) comida, (c) trabajo.", "a"),
        62: ("Contacto de Lenguas", "Los 'portuñoles' son ejemplos de lenguas en contacto entre: (a) portugués y español, (b) francés y español.", "a"),
        63: ("Léxico Regional (Ecuador)", "En Ecuador, 'bacán' significa: (a) aburrido, (b) excelente, (c) triste.", "b"),
        64: ("Fonética Regional (Venezuela)", "En Venezuela, la 's' final de sílaba a menudo se elide, ¿verdad?", "verdad"),
        65: ("Léxico Regional (México)", "En México, 'güey' es un término coloquial para: (a) amigo, (b) enemigo, (c) animal.", "a"),
        66: ("Indigenismo (Maya)", "La palabra 'cigarro' tiene un posible origen en: (a) Náhuatl, (b) Maya, (c) Taino.", "b"),
        67: ("Léxico Regional (Perú)", "En Perú, 'chévere' es: (a) un adjetivo para una persona aburrida, (b) un adjetivo para algo bueno, (c) un adjetivo para algo malo.", "b"),
        68: ("Fonética Regional (Argentina)", "La 's' final en 'más o menos' se pronuncia: (a) como 's', (b) como 'z', (c) aspirada.", "c"),
        69: ("Léxico Regional (El Salvador)", "En El Salvador, 'pupusa' es: (a) una bebida, (b) una comida tradicional, (c) un juguete.", "b"),
        70: ("Indigenismo (Araucano)", "La palabra 'quiltro' (perro mestizo) es un préstamo de: (a) Quechua, (b) Araucano, (c) Náhuatl.", "b"),
        71: ("Léxico Regional (Honduras)", "En Honduras, 'churro' se usa para: (a) una persona atractiva, (b) una comida, (c) un trabajo.", "a"),
        72: ("Fonética Regional (Caribe)", "En el español caribeño, la 'r' final de sílaba se pronuncia como 'l', ¿cómo se llama?", "lamdacismo"),
        73: ("Indigenismo (Guaraní)", "La palabra 'piragua' (canoa) es un indigenismo. ¿De qué lengua proviene?", "guaraní"),
        74: ("Léxico Regional (Panamá)", "En Panamá, 'pavo' se usa para: (a) una persona torpe, (b) una comida, (c) un animal.", "a"),
        75: ("Sintaxis Regional (Andes)", "El uso de la forma verbal 'se lo' en 'se lo vendo' es común en: (a) España, (b) Andino, (c) Cono Sur.", "b"),
        76: ("Indigenismo (Náhuatl)", "La palabra 'tomate' es un indigenismo. ¿De qué lengua proviene?", "náhuatl"),
        77: ("Léxico Regional (Chile)", "En Chile, 'polera' es: (a) una camisa, (b) una camiseta, (c) un vestido.", "b"),
        78: ("Fonética Regional (Cono Sur)", "El yeísmo es un fenómeno que afecta a la pronunciación de: (a) 'll', 'y', (b) 's', 'c', (c) 'r', 'l'.", "a"),
        79: ("Léxico Regional (Cuba)", "En Cuba, 'guajiro' es: (a) un campesino, (b) un extranjero, (c) un animal.", "a"),
        80: ("Indigenismo (Quechua)", "La palabra 'papa' (tubérculo) es un indigenismo. ¿De qué lengua proviene?", "quechua"),
        81: ("Léxico Regional (Venezuela)", "En Venezuela, 'palo' es: (a) un bastón, (b) una botella de alcohol, (c) una rama de árbol.", "b"),
        82: ("Sintaxis Regional", "El uso de 'le' como objeto directo para personas masculinas es: (a) un leísmo, (b) un loísmo, (c) un laísmo.", "a"),
        83: ("Fonética Regional (Colombia)", "En Colombia, la 'ch' se pronuncia con un sonido más suave en la zona: (a) andina, (b) caribeña, (c) pacífica.", "b"),
        84: ("Léxico Regional (Argentina)", "En Argentina, 'laburo' es: (a) trabajo, (b) ocio, (c) dinero.", "a"),
        85: ("Indigenismo (Arawak)", "La palabra 'tabaco' es un indigenismo. ¿De qué lengua proviene?", "arawak"),
        86: ("Léxico Regional (Guatemala)", "En Guatemala, 'shuco' es: (a) sucio, (b) feo, (c) caliente.", "a"),
        87: ("Fonética Regional (El Salvador)", "La 's' en 'estos' se pronuncia: (a) como 's', (b) como 'z', (c) aspirada.", "c"),
        88: ("Léxico Regional (Bolivia)", "En Bolivia, 'chala' significa: (a) un saludo, (b) una conversación, (c) una mentira.", "b"),
        89: ("Indigenismo (Quechua)", "La palabra 'alpaca' es un indigenismo. ¿De qué lengua proviene?", "quechua"),
        90: ("Léxico Regional (Ecuador)", "En Ecuador, 'chuta' es una exclamación de: (a) sorpresa, (b) alegría, (c) tristeza.", "a"),
        91: ("Sintaxis Regional (Cono Sur)", "La forma verbal 'cantás' se usa en el voseo de: (a) México, (b) Colombia, (c) Cono Sur.", "c"),
        92: ("Léxico Regional (Chile)", "En Chile, 'huevón' se usa para: (a) una persona tonta, (b) una persona inteligente, (c) un objeto.", "a"),
        93: ("Fonética Regional (Perú)", "En Perú, la 'r' se pronuncia con una fricción alveolar sonora en el español: (a) andino, (b) costeño, (c) amazónico.", "a"),
        94: ("Léxico Regional (Colombia)", "En Colombia, 'chino' se usa para: (a) un niño, (b) un adulto, (c) un extranjero.", "a"),
        95: ("Indigenismo (Náhuatl)", "La palabra 'cacao' es un indigenismo. ¿De qué lengua proviene?", "náhuatl"),
        96: ("Léxico Regional (Argentina)", "En Argentina, 'che' se usa para: (a) llamar la atención, (b) expresar sorpresa, (c) ambas.", "c"),
        97: ("Fonética Regional (Panamá)", "En Panamá, la 's' final de sílaba a menudo se aspira. (Verdadero o Falso)", "verdadero"),
        98: ("Léxico Regional (México)", "En México, 'juguete' se usa para: (a) un niño, (b) un objeto para jugar, (c) un adjetivo.", "b"),
        99: ("Indigenismo (Maya)", "La palabra 'cigarro' tiene un posible origen en: (a) Maya, (b) Náhuatl, (c) Quechua.", "a"),
        100: ("Léxico Regional (Uruguay)", "En Uruguay, un 'omnibus' es: (a) un coche, (b) un autobús, (c) un tren.", "b"),
    }

    print("¡Bienvenido al reto de Lingüística Hispanoamericana!")
    print("----------------------------------------------------")
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
