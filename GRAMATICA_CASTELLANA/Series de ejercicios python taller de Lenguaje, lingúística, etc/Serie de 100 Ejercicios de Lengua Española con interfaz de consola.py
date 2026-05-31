# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Lengua Española con interfaz de consola.
# Inspirado en el "Diccionario de Construcción y Régimen de la Lengua Castellana" de R.J. Cuervo.
#
# Este programa presenta una serie de ejercicios interactivos en la terminal.

import random

def main():
    """Función principal del programa."""
    
    # Diccionario de ejercicios
    ejercicios = {
        1: ("Un saludo 'bien bacano'", "Escribe un saludo 'bien bacano' (ej: ¡Qué más, [nombre]! ¿Todo bien o qué?)", "¡Qué más, [nombre]! ¿Todo bien o qué?"),
        2: ("El 'parche' de amigos", "Tienes una lista de amigos. Agrega dos nuevos (ej: 'Sofía', 'Carlos').", "['Juan', 'María', 'Pedro', 'Sofía', 'Carlos']"),
        3: ("Arepa con queso", "Si cada arepa cuesta 2500 COP, ¿cuál es el costo de 3 arepas?", "7500"),
        4: ("Manejar el cambio", "Un producto cuesta 12000 COP y pagas con 20000. ¿Cuál es el cambio?", "8000"),
        5: ("El 'guayabo'", "Si te acuestas tarde y tienes dolor de cabeza, ¿cuál es el resultado?", "guayabo"),
        6: ("El 'achaque' de la palabra", "Escribe el significado de 'achaque' (sentido figurado).", "pretexto"),
        7: ("'Dizque' la sinonimia", "Usa la palabra 'dizque' en una oración.", "Dizque va a llover."),
        8: ("¿'Por' o 'Para'?", "Completa: 'Este regalo es ... mi mamá.'", "para"),
        9: ("El error de bulto", "Corrige la palabra mal escrita: 'haiga'.", "haya"),
        10: ("Etimología de 'guaricha'", "Escribe el origen de la palabra 'guaricha'.", "chibcha"),
        11: ("'Afecto' vs. 'Efecto'", "Completa: 'El ... del calor es el vapor.'", "efecto"),
        12: ("La conjugación de 'haber'", "Completa: '... muchos carros en la calle.'", "hay"),
        13: ("Concordancia verbal", "Completa: 'El carro y la moto ... en la autopista.'", "corren"),
        14: ("La coma vocativa", "Corrige: 'Hola Juan como estas?'", "Hola, Juan, ¿cómo estás?"),
        15: ("La 'ñapa'", "Usa la palabra 'ñapa' en una oración.", "Dame la ñapa."),
        16: ("Palabras compuestas", "Forma una palabra compuesta con 'rompe'.", "rompecabezas"),
        17: ("Acentos diacríticos", "Completa: '... es el mejor.'", "él"),
        18: ("'Hacer el oso'", "Escribe una oración con 'hacer el oso'.", "Hice el oso en la fiesta."),
        19: ("Uso de mayúsculas", "Corrige: 'La ciudad de Bogota.'", "La ciudad de Bogotá."),
        20: ("El refrán", "Completa: 'Al que madruga...' ", "Dios le ayuda."),
        21: ("Ser o Estar", "Completa: 'El café ... caliente.'", "está"),
        22: ("Ser para profesiones", "Completa: 'Mi padre ... médico.'", "es"),
        23: ("Estar para localización", "Completa: 'Juan ... en la casa.'", "está"),
        24: ("Ser/Estar con adjetivos", "Completa: 'La manzana ... verde (color).'", "es"),
        25: ("Ser con hora y fecha", "Completa: 'Hoy ... 15 de marzo.'", "es"),
        26: ("Estar con ánimo", "Completa: 'Mi amigo ... muy feliz.'", "está"),
        27: ("Ser con nacionalidad", "Completa: 'Ella ... colombiana.'", "es"),
        28: ("Ser para origen", "Completa: 'Los estudiantes ... de Cali.'", "son"),
        29: ("Estar para condición", "Completa: 'Yo ... cansado.'", "estoy"),
        30: ("Ser/Estar en pasado", "Completa: 'Ayer, yo ... en la biblioteca.'", "estaba"),
        31: ("Uso de la coma", "Corrige: 'Compre frutas leche y pan.'", "Compré frutas, leche y pan."),
        32: ("Coma vocativa", "Corrige: 'Buenos días papa.'", "Buenos días, papá."),
        33: ("Punto y coma", "Completa con un punto y coma: 'El cielo está nublado... parece que va a llover.'", "El cielo está nublado; parece que va a llover."),
        34: ("Puntos suspensivos", "Completa: 'No sé qué decir...' ", "No sé qué decir..."),
        35: ("Dos puntos", "Completa: 'Mis colores favoritos son:...' ", "Mis colores favoritos son: azul, verde y rojo."),
        36: ("Comillas", "Cita a tu madre: 'El que mucho abarca, poco aprieta.'", "El que mucho abarca, poco aprieta."),
        37: ("Signos de interrogación", "Escribe una pregunta simple.", "¿Cómo estás?"),
        38: ("Signos de exclamación", "Escribe una exclamación.", "¡Qué sorpresa!"),
        39: ("Paréntesis", "Añade un paréntesis: 'El río Magdalena es el más largo de Colombia.'", "El río Magdalena (el más largo de Colombia)."),
        40: ("Guion largo", "Escribe un diálogo con guion largo.", "—¿Cómo estás? —Bien."),
        41: ("Concordancia adjetivo", "Completa: 'La casa ... (rojo).' ", "roja"),
        42: ("Género de sustantivos", "Completa: '... agua.' ", "el"),
        43: ("Concordancia verbal", "Completa: 'El libro y la revista ... interesantes.' ", "son"),
        44: ("Género y plural", "Escribe el plural de 'el lápiz'.", "los lápices"),
        45: ("Concordancia con números", "Completa: 'Veinte ... (día) de febrero.' ", "días"),
        46: ("Pronombres personales", "Sustituye 'Juan y yo' por un pronombre.", "Nosotros"),
        47: ("Concordancia con varios sustantivos", "Completa: 'El libro y la revista son ... (interesante).'", "interesantes"),
        48: ("Género de nombres", "Completa: '... Madrid.' ", "el"),
        49: ("Plural de 'z'", "Escribe el plural de 'pez'.", "peces"),
        50: ("Concordancia pronominal", "Sustituye 'a María' por un pronombre: 'Vi a María en el cine.'", "la vi"),
        51: ("Preposición 'a'", "Completa: 'Voy ... la escuela.' ", "a"),
        52: ("Preposición 'de'", "Completa: 'Soy ... Colombia.' ", "de"),
        53: ("Preposición 'con'", "Completa: 'Fui al cine ... mis amigos.' ", "con"),
        54: ("Preposición 'en'", "Completa: 'El libro está ... la mesa.' ", "en"),
        55: ("Preposición 'para'", "Completa: 'Estudio ... mi examen.' ", "para"),
        56: ("Preposición 'por'", "Completa: 'Lo hice ... ti.' ", "por"),
        57: ("Preposición 'entre'", "Completa: 'La tienda abre ... 8 a.m. y 6 p.m.' ", "entre"),
        58: ("Preposición 'sin'", "Completa: 'No puedo ver ... mis gafas.' ", "sin"),
        59: ("Preposición 'sobre'", "Completa: 'El libro está ... la mesa.' ", "sobre"),
        60: ("Preposición 'hasta'", "Completa: 'Corrí ... el final de la calle.' ", "hasta"),
        61: ("'Sino' vs. 'si no'", "Completa: 'No es blanco, ... negro.' ", "sino"),
        62: ("'Porque' vs. 'por qué'", "Completa: '¿... no fuiste?' ", "por qué"),
        63: ("'También' vs. 'tan bien'", "Completa: 'Cantas ... que me emocionas.' ", "tan bien"),
        64: ("'Adonde' vs. 'a donde'", "Completa: 'No sé ... vamos.' ", "a dónde"),
        65: ("'Demás' vs. 'de más'", "Completa: 'Los ... no vinieron.' ", "demás"),
        66: ("'Asimismo' vs. 'a sí mismo'", "Completa: 'Se habla ... cuando está solo.' ", "a sí mismo"),
        67: ("'Conque', 'con que', 'con qué'", "Completa: '¿... dinero compraste eso?' ", "con qué"),
        68: ("'Haber' vs. 'a ver'", "Completa: 'Tiene que ... un error.' ", "haber"),
        69: ("'Acerca de' vs. 'a cerca de'", "Completa: 'Hablamos ... la película.' ", "acerca de"),
        70: ("'Porvenir' vs. 'por venir'", "Completa: 'El ... es incierto.' ", "porvenir"),
        71: ("Leísmo vs Loísmo", "Corrige la frase: 'Le vi a Juan.' ", "Lo vi a Juan."),
        72: ("Leísmo de cortesía", "Completa: 'A su padre, ... respeto mucho.' ", "le"),
        73: ("Laísmo", "Completa: 'A mi hermana, ... vi en el parque.' ", "la"),
        74: ("Loísmo", "Corrige: 'A mi hermano, le vi.' ", "Lo vi."),
        75: ("Pronombre O.D.", "Sustituye 'la camisa': 'Compré la camisa.' ", "La compré."),
        76: ("Pronombre O.I.", "Sustituye 'a María': 'Di el libro a María.' ", "Le di el libro."),
        77: ("Combinación de pronombres", "Combina: 'Di el libro a Juan.' ", "Se lo di."),
        78: ("Leísmo plural", "Corrige: 'A los niños, les vi.' ", "Los vi."),
        79: ("Laísmo plural", "Completa: 'A las niñas, ... vi.' ", "las"),
        80: ("Loísmo plural", "Corrige: 'A mis amigos, los compré un regalo.' ", "Les compré un regalo."),
        81: ("Arcaísmo 'doquier'", "Usa la palabra 'doquier'.", "Voy doquier."),
        82: ("Arcaísmo 'empero'", "Usa la palabra 'empero'.", "Empero, no voy."),
        83: ("Arcaísmo 'maguer'", "Usa la palabra 'maguer'.", "Maguer el sol, salí."),
        84: ("Arcaísmo 'enderezar'", "Usa 'enderezar' en su sentido antiguo.", "Enderezó el rumbo."),
        85: ("Arcaísmo 'cuita'", "Usa la palabra 'cuita'.", "Sentía una gran cuita."),
        86: ("Arcaísmo 'encono'", "Usa la palabra 'encono'.", "Su encono era profundo."),
        87: ("Arcaísmo 'caduco'", "Usa la palabra 'caduco'.", "El reloj es caduco."),
        88: ("'A sabiendas de'", "Usa 'a sabiendas de' en una oración.", "Lo hizo a sabiendas de todo."),
        89: ("'Verbigracia'", "Usa la palabra 'verbigracia'.", "Verbigracia, el perro."),
        90: ("Arcaísmo 'crespo'", "Usa 'crespo' con sentido de ira.", "Se puso crespo."),
        91: ("Dicho: 'no dar papaya'", "Explica 'no dar papaya' y úsalo.", "No des papaya."),
        92: ("Dicho: 'mamando gallo'", "Explica 'estar mamando gallo' y úsalo.", "Estás mamando gallo."),
        93: ("Dicho: 'agarrar el palo'", "Explica 'agarrar el palo' y úsalo.", "Agarré el palo rápido."),
        94: ("Dicho: 'tener la pata mala'", "Explica 'tener la pata mala' y úsalo.", "Tengo la pata mala hoy."),
        95: ("Refrán: 'Al mal tiempo...' ", "Completa: 'Al mal tiempo, ...'", "buena cara."),
        96: ("Refrán: 'Más vale tarde...' ", "Completa: 'Más vale tarde que ...'", "nunca"),
        97: ("Refrán: 'No hay mal...' ", "Completa: 'No hay mal que por bien no ...'", "venga"),
        98: ("Refrán: 'A quien madruga...' ", "Completa: 'A quien madruga, ...'", "Dios le ayuda."),
        99: ("Refrán: 'El que mucho abarca...' ", "Completa: 'El que mucho abarca, poco ...'", "aprieta"),
        100: ("Refrán: 'Más sabe el diablo...' ", "Completa: 'Más sabe el diablo por viejo ...'", "que por diablo"),
    }

    print("¡Bienvenido al reto de gramática, al estilo de Cuervo!")
    print("-----------------------------------------------------")

    while True:
        try:
            # Selecciona un ejercicio al azar
            numero_ejercicio = random.choice(list(ejercicios.keys()))
            titulo, tarea, respuesta_correcta = ejercicios[numero_ejercicio]
            
            print(f"\n[Ejercicio {numero_ejercicio}: {titulo}]")
            print(tarea)
            
            respuesta_usuario = input("Tu respuesta: ").strip()

            if respuesta_usuario.lower() == respuesta_correcta.lower():
                print("¡Correcto! ¡Qué bien!")
            else:
                print(f"Incorrecto. La respuesta esperada era: '{respuesta_correcta}'")

            continuar = input("\n¿Quieres otro ejercicio? (s/n): ").lower()
            if continuar != 's':
                print("¡Hasta pronto!")
                break

        except (KeyboardInterrupt, EOFError):
            print("\n¡Adiós!")
            break

if __name__ == "__main__":
    main()
