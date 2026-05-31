# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Lexicografía
# Inspirado en la obra del Instituto Caro y Cuervo.
#
# Este programa de consola presenta una serie de ejercicios sobre palabras,
# sus orígenes, significados y uso en el español de Colombia.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios y el bucle principal
    para presentarlos al usuario.
    """
    ejercicios = {
        1: ("'Ñapa'", "En Colombia, la 'ñapa' es: (a) un tipo de café, (b) un regalo extra, (c) una trampa.", "b"),
        2: ("Origen de 'berraco'", "La palabra 'berraco' (valiente, tenaz) proviene de: (a) el latín, (b) el quechua, (c) el portugués.", "b"),
        3: ("Sinónimo de 'chusco'", "Un sinónimo de 'chusco' (gracioso o divertido) es: (a) formal, (b) jocoso, (c) triste.", "b"),
        4: ("Significado de 'culillo'", "En Colombia, tener 'culillo' significa: (a) tener un poco de frío, (b) tener miedo, (c) tener picazón.", "b"),
        5: ("Etimología de 'cacharro'", "El 'cacharro' (objeto viejo o inútil) tiene su origen en: (a) la cerámica, (b) un animal, (c) una herramienta.", "a"),
        6: ("'Piloso'", "El adjetivo 'piloso' se usa para describir a una persona: (a) muy dormilona, (b) muy inteligente y atenta, (c) muy perezosa.", "b"),
        7: ("Uso de 'chévere'", "Escribe una oración con la palabra 'chévere'.", "La película es chévere."),
        8: ("El verbo 'parar'", "En la expresión 'Me para bolas', el verbo 'parar' significa: (a) prestar atención, (b) detenerse, (c) ponerse de pie.", "a"),
        9: ("'Tote'", "Un 'tote' en Colombia es: (a) una persona gorda, (b) un pedazo de pan, (c) un estallido fuerte.", "c"),
        10: ("Etimología de 'cucho'", "La palabra 'cucho' (anciano) proviene del: (a) latín, (b) quechua, (c) español antiguo.", "b"),
        11: ("'Mamar gallo'", "Explica la expresión 'mamar gallo'.", "perder el tiempo"),
        12: ("'Pola'", "Una 'pola' en Colombia es: (a) una bebida caliente, (b) una cerveza, (c) un tipo de baile.", "b"),
        13: ("'Parce'", "La palabra 'parce' es un apócope de: (a) parcero, (b) parcial, (c) pareja.", "a"),
        14: ("Uso de 'arrecho'", "Escribe una oración con la palabra 'arrecho' (en su sentido colombiano de 'valiente').", "Ese man es muy arrecho."),
        15: ("'Guayaba'", "La palabra 'guayaba' se usa para referirse a: (a) una fruta, (b) una mentira o historia inventada, (c) una canción.", "b"),
        16: ("'Sapo'", "En Colombia, a una persona 'sapa' se le considera: (a) chismosa, (b) callada, (c) aburrida.", "a"),
        17: ("'Estar mamado'", "La expresión 'estar mamado' significa: (a) estar lleno de comida, (b) estar muy cansado, (c) estar enojado.", "b"),
        18: ("'Paila'", "La palabra 'paila' significa: (a) una sartén grande, (b) algo que no tiene remedio, (c) un tipo de comida.", "b"),
        19: ("'Pollo'", "En el argot colombiano, un 'pollo' es: (a) un animal de granja, (b) una persona joven o inexperta, (c) un plato de comida.", "b"),
        20: ("'A la lata'", "La expresión 'a la lata' significa: (a) en exceso, (b) de forma rápida, (c) con dificultad.", "a"),
        21: ("'Calaña'", "El sustantivo 'calaña' se refiere a: (a) un tipo de sombrero, (b) la calidad o naturaleza de alguien, (c) un plato de comida.", "b"),
        22: ("'Zarandear'", "El verbo 'zarandear' significa: (a) caminar despacio, (b) mover a alguien de un lado a otro, (c) mirar algo con detenimiento.", "b"),
        23: ("'Sotobosque'", "El 'sotobosque' es: (a) una bebida, (b) la parte de un bosque debajo de la copa de los árboles, (c) una ciudad.", "b"),
        24: ("'Papiamento'", "El papiamento es: (a) una jerga, (b) una lengua criolla, (c) un baile.", "b"),
        25: ("'Perendengue'", "La palabra 'perendengue' significa: (a) un adorno o detalle insignificante, (b) un tipo de comida, (c) un objeto de madera.", "a"),
        26: ("'Gargajear'", "El verbo 'gargajear' significa: (a) gritar, (b) expulsar flema de la garganta, (c) comer con afán.", "b"),
        27: ("'Pata' en Colombia", "Cuando se dice 'tener buena pata', significa: (a) ser afortunado, (b) caminar bien, (c) tener un buen amigo.", "a"),
        28: ("'Dar papaya'", "Explica la expresión 'dar papaya'.", "darle a alguien una oportunidad"),
        29: ("'Chancletas'", "Las 'chancletas' son: (a) un tipo de baile, (b) chanclas o sandalias, (c) un tipo de comida.", "b"),
        30: ("'Guarapo'", "El 'guarapo' es una bebida hecha con: (a) café, (b) caña de azúcar, (c) maíz.", "b"),
        31: ("'Arrastrado'", "En Colombia, una persona 'arrastrada' es: (a) muy servicial, (b) mentirosa, (c) sinvergüenza y servil.", "c"),
        32: ("'Filo'", "Tener 'filo' en Colombia significa: (a) estar con hambre, (b) tener sed, (c) tener sueño.", "a"),
        33: ("'Jartera'", "Tener 'jartera' es sentir: (a) mucha alegría, (b) fastidio o aburrimiento, (c) mucha energía.", "b"),
        34: ("'Berriondo'", "La palabra 'berriondo' se usa para decir que algo es: (a) sucio, (b) excelente o increíble, (c) ruidoso.", "b"),
        35: ("'Echar los perros'", "La expresión 'echar los perros' significa: (a) pelear, (b) coquetear, (c) dormir.", "b"),
        36: ("'Camellar'", "El verbo 'camellar' significa: (a) caminar, (b) trabajar duro, (c) hablar mucho.", "b"),
        37: ("'Pecueca'", "La 'pecueca' es el olor que produce: (a) los pies, (b) la comida, (c) el ambiente.", "a"),
        38: ("'Chuzo'", "Un 'chuzo' puede ser: (a) una tienda pequeña, (b) un coche, (c) una mascota.", "a"),
        39: ("'Bacano'", "La palabra 'bacano' significa: (a) divertido y agradable, (b) aburrido, (c) cansado.", "a"),
        40: ("'Farra'", "Una 'farra' en Colombia es: (a) una fiesta, (b) una bebida, (c) un plato de comida.", "a"),
        41: ("'Corotos'", "Los 'corotos' son: (a) ropa, (b) objetos, (c) juguetes.", "b"),
        42: ("'Chicanear'", "El verbo 'chicanear' significa: (a) presumir o alardear, (b) comer, (c) dormir.", "a"),
        43: ("'Vaina'", "La palabra 'vaina' se usa para referirse a: (a) un problema, (b) una persona, (c) una cosa sin nombre.", "c"),
        44: ("'Aletear'", "En Colombia, 'aleta' es una persona: (a) que tiene calor, (b) que se va a ir, (c) que se enfada.", "c"),
        45: ("'Chimba'", "La palabra 'chimba' se usa para describir algo: (a) malo, (b) bueno, (c) normal.", "b"),
        46: ("'Parranda'", "Una 'parranda' es: (a) un viaje, (b) una celebración, (c) una broma.", "b"),
        47: ("'Zanahoria'", "Una persona 'zanahoria' es: (a) muy inteligente, (b) aburrida o sin vicios, (c) muy alta.", "b"),
        48: ("'Catre'", "Un 'catre' es: (a) un tipo de cama, (b) un mueble, (c) una silla.", "a"),
        49: ("'Despapaye'", "Un 'despapaye' es: (a) un desorden, (b) una sorpresa, (c) una mentira.", "a"),
        50: ("'Apostillar'", "El verbo 'apostillar' significa: (a) anotar al margen, (b) apostar, (c) hablar.", "a"),
        51: ("'Bochinche'", "Un 'bochinche' es: (a) un rumor, (b) un plato, (c) una herramienta.", "a"),
        52: ("'Canalla'", "El sustantivo 'canalla' se refiere a una persona: (a) noble, (b) de mala calidad moral, (c) fuerte.", "b"),
        53: ("'Dádiva'", "Una 'dádiva' es: (a) un problema, (b) un regalo, (c) una canción.", "b"),
        54: ("'Ebrio'", "El adjetivo 'ebrio' significa: (a) lleno de vida, (b) que está borracho, (c) feliz.", "b"),
        55: ("'Fatuo'", "Una persona 'fatua' es: (a) tonta, (b) valiente, (c) rápida.", "a"),
        56: ("'Gabela'", "La 'gabela' es: (a) una ventaja, (b) una desventaja, (c) un castigo.", "a"),
        57: ("'Hacedero'", "El adjetivo 'hacedero' significa: (a) que se puede hacer, (b) que no tiene futuro, (c) que está roto.", "a"),
        58: ("'Ínclito'", "El adjetivo 'ínclito' significa: (a) ilustre o célebre, (b) pequeño, (c) sucio.", "a"),
        59: ("'Jolgorio'", "El 'jolgorio' es: (a) una comida, (b) una fiesta, (c) un trabajo.", "b"),
        60: ("'Kiosco'", "Un 'kiosco' es: (a) un tipo de árbol, (b) una estructura, (c) un animal.", "b"),
        61: ("'Labriego'", "Un 'labriego' es: (a) un labrador, (b) un abogado, (c) un médico.", "a"),
        62: ("'Mascullador'", "Un 'mascullador' es una persona que: (a) habla en voz baja, (b) camina, (c) come.", "a"),
        63: ("'Nefando'", "El adjetivo 'nefando' significa: (a) algo muy bueno, (b) algo que no se debe nombrar, (c) algo difícil.", "b"),
        64: ("'Óbice'", "Un 'óbice' es: (a) una ayuda, (b) un obstáculo, (c) un libro.", "b"),
        65: ("'Perenne'", "El adjetivo 'perenne' significa: (a) que dura para siempre, (b) que es estacional, (c) que es temporal.", "a"),
        66: ("'Quimera'", "Una 'quimera' es: (a) una fruta, (b) un sueño o fantasía, (c) un animal real.", "b"),
        67: ("'Recóndito'", "Un lugar 'recóndito' es: (a) muy visible, (b) muy escondido, (c) muy lejano.", "b"),
        68: ("'Subrepticio'", "El adjetivo 'subrepticio' significa: (a) que se hace a escondidas, (b) que se hace en público, (c) que es legal.", "a"),
        69: ("'Truculento'", "Una historia 'truculenta' es: (a) aburrida, (b) emocionante, (c) cruel y macabra.", "c"),
        70: ("'Ufano'", "Una persona 'ufana' es: (a) triste, (b) alegre, (c) orgullosa.", "c"),
        71: ("'Vacilación'", "La 'vacilación' es: (a) una decisión rápida, (b) una duda, (c) una mentira.", "b"),
        72: ("'Yermo'", "El adjetivo 'yermo' significa: (a) fértil, (b) muy seco y sin vegetación, (c) muy húmedo.", "b"),
        73: ("'Zozobra'", "La 'zozobra' es: (a) un estado de calma, (b) una inquietud, (c) una enfermedad.", "b"),
        74: ("'Acatar'", "El verbo 'acatar' significa: (a) desobedecer, (b) obedecer, (c) jugar.", "b"),
        75: ("'Baladí'", "El adjetivo 'baladí' se refiere a algo: (a) importante, (b) insignificante, (c) grande.", "b"),
        76: ("'Cariz'", "El 'cariz' de algo es: (a) el olor, (b) la apariencia, (c) el sabor.", "b"),
        77: ("'Dechado'", "Un 'dechado' es: (a) un ejemplo, (b) un error, (c) un tipo de flor.", "a"),
        78: ("'Enjundia'", "La 'enjundia' es: (a) el valor, (b) la tristeza, (c) la suerte.", "a"),
        79: ("'Furtivo'", "El adjetivo 'furtivo' se refiere a algo que se hace: (a) de forma pública, (b) de forma rápida, (c) a escondidas.", "c"),
        80: ("'Garito'", "Un 'garito' es: (a) una casa de juego ilegal, (b) un restaurante, (c) un teatro.", "a"),
        81: ("'Hilarante'", "Algo 'hilarante' es: (a) aburrido, (b) muy divertido, (c) complicado.", "b"),
        82: ("'Ignominia'", "La 'ignominia' es: (a) un honor, (b) una ofensa grave, (c) una amistad.", "b"),
        83: ("'Jolgorio'", "El 'jolgorio' es: (a) un tipo de trabajo, (b) un ambiente de fiesta, (c) una pelea.", "b"),
        84: ("'Ládino'", "Una persona 'ládina' es: (a) sincera, (b) astuta, (c) lenta.", "b"),
        85: ("'Macilento'", "El adjetivo 'macilento' se refiere a una persona: (a) robusta, (b) pálida y enfermiza, (c) alta.", "b"),
        86: ("'Nefasto'", "Algo 'nefasto' es: (a) positivo, (b) negativo, (c) neutral.", "b"),
        87: ("'Orondo'", "Una persona 'oronda' es: (a) triste, (b) satisfecha y contenta, (c) cansada.", "b"),
        88: ("'Pamema'", "La 'pamema' es: (a) una broma, (b) un gesto, (c) un engaño o tontería.", "c"),
        89: ("'Quid'", "El 'quid' de la cuestión es: (a) el problema, (b) el punto principal, (c) la solución.", "b"),
        90: ("'Resiliente'", "El adjetivo 'resiliente' se refiere a la capacidad de: (a) volar, (b) adaptarse a la adversidad, (c) comer.", "b"),
        91: ("'Sobrio'", "Una persona 'sobria' es: (a) elegante, (b) seria, (c) que no está bajo los efectos del alcohol.", "c"),
        92: ("'Tangible'", "Algo 'tangible' es: (a) que se puede tocar, (b) que no existe, (c) que es muy rápido.", "a"),
        93: ("'Ufano'", "Usa la palabra 'ufano' en una oración.", "El equipo, ufano por la victoria, celebró."),
        94: ("'Vástago'", "Un 'vástago' es: (a) una herramienta, (b) un hijo o descendiente, (c) un vegetal.", "b"),
        95: ("'Zafio'", "El adjetivo 'zafio' se usa para describir a una persona: (a) educada, (b) rústica y sin modales, (c) divertida.", "b"),
        96: ("'Jolgorio'", "La palabra 'jolgorio' es un sinónimo de: (a) tristeza, (b) algarabía, (c) calma.", "b"),
        97: ("'Enjundioso'", "Algo 'enjundioso' es: (a) superficial, (b) con mucho contenido, (c) aburrido.", "b"),
        98: ("'Perfidia'", "La 'perfidia' es: (a) la bondad, (b) la traición, (c) la amistad.", "b"),
        99: ("'Abulia'", "El sustantivo 'abulia' significa: (a) falta de voluntad, (b) exceso de energía, (c) un tipo de dolor.", "a"),
        100: ("'Craso'", "Un 'craso error' es un error: (a) insignificante, (b) muy grande, (c) accidental.", "b"),
    }

    print("¡Bienvenido al reto de lexicografía, por el Instituto Caro y Cuervo!")
    print("-----------------------------------------------------------------")
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
            
            # Normalizar las respuestas para comparación
            respuesta_limpia = respuesta_usuario.lower()
            correcta_limpia = respuesta_correcta.lower()

            if respuesta_limpia == correcta_limpia or correcta_limpia in respuesta_limpia:
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
