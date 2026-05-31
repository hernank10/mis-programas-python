# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Python inspirados en el español de Colombia
# Basado en el "Diccionario de Construcción y Régimen de la Lengua Castellana" de R.J. Cuervo.
#
# Este programa presenta una serie de ejercicios interactivos en la consola.
# ¡"Pilas" para que no te quedes "con las manos cruzadas"!

import os

def limpiar_consola():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- MÓDULOS DE EJERCICIOS ---

def ejecutar_ejercicio(titulo, tarea, logica, ayuda=None):
    """Función genérica para ejecutar ejercicios."""
    print(f"--- {titulo} ---")
    print(f"¡Pilas! Completa la siguiente tarea:\n\n{tarea}\n")
    try:
        logica()
    except Exception as e:
        print(f"\n¡Uy! Ocurrió un error: {e}")
        if ayuda:
            print(f"Pista: {ayuda}")
    finally:
        input("\nPresiona Enter para continuar...")
        limpiar_consola()

# --- EJERCICIOS (1-5) - Jerga y cultura local ---

def ejercicio_1_saludo_colombiano():
    ejecutar_ejercicio(
        "Ejercicio 1: Un saludo 'bien bacano'",
        "Escribe un programa que pida tu nombre y luego imprima un saludo con una expresión típica colombiana.\nEjemplo de salida: ¡Qué más, [nombre]! ¿Todo bien o qué?",
        lambda: print(f"¡Qué más, {input('¿Cuál es tu nombre? ')}! ¿Todo bien o qué?"),
        ayuda="Usa una f-string para insertar el nombre en el saludo."
    )

def ejercicio_2_parche_de_amigos():
    ejecutar_ejercicio(
        "Ejercicio 2: El 'parche' de amigos",
        "Tienes una lista de amigos. Agrega dos nuevos amigos a esta lista e imprime la lista completa.",
        lambda: (
            parche := ["Juan", "María", "Pedro"],
            print(f"Tu parche original es: {parche}"),
            parche.extend(["Sofía", "Carlos"]),
            print(f"Tu nuevo parche es: {parche}")
        )
    )

def ejercicio_3_arepa_con_queso():
    ejecutar_ejercicio(
        "Ejercicio 3: Las 'arepas con queso'",
        "Escribe una función que reciba el número de arepas que quieres y calcule el costo total. Supón que cada arepa cuesta 2500 COP.",
        lambda: (
            costo := int(input("¿Cuántas arepas con queso quieres? ")) * 2500,
            print(f"El costo total es de {costo} COP. ¡Qué delicia!")
        )
    )

def ejercicio_4_calcular_el_cambio():
    ejecutar_ejercicio(
        "Ejercicio 4: 'Manejar' el cambio",
        "Tienes el costo de un producto y el dinero que pagaste. Calcula el cambio que debes recibir.",
        lambda: (
            costo_producto := float(input("¿Cuánto cuesta el producto? ")),
            dinero_pagado := float(input("¿Cuánto dinero pagaste? ")),
            print(f"Tu cambio es de {dinero_pagado - costo_producto} COP.") if dinero_pagado >= costo_producto else print("¡Qué pena! Te falta dinero para completar la compra.")
        ),
        ayuda="Usa una condicional (if/else) para determinar si hay cambio."
    )

def ejercicio_5_guayabo_del_bueno():
    ejecutar_ejercicio(
        "Ejercicio 5: El 'guayabo' del fin de semana",
        "Crea un programa que determine si alguien tiene 'guayabo' basado en si se acostó tarde y si tiene dolor de cabeza.",
        lambda: (
            acosto_tarde := input("¿Te acostaste tarde el fin de semana? (s/n) ").lower() == 's',
            dolor_cabeza := input("¿Tienes dolor de cabeza? (s/n) ").lower() == 's',
            print("¡Tienes un 'guayabo' del bueno! Ve por un caldo de costilla.") if acostado_tarde and dolor_cabeza else (
                print("Parece que tienes un 'guayabo' suave. ¡Ánimo!") if acostado_tarde or dolor_cabeza else print("¡Qué chimba! Te libraste del 'guayabo'.")
            )
        )
    )

# --- EJERCICIOS (6-10) - El espíritu del diccionario de Cuervo: Ortografía y Sintaxis ---

def ejercicio_6_cuervo_palabra_del_dia():
    ejecutar_ejercicio(
        "Ejercicio 6: El 'achaque' de la palabra del día",
        "Simula la explicación de Cuervo. Muestra una palabra, su definición y un par de frases de ejemplo.",
        lambda: (
            palabra, definicion, ejemplos == "achaque", "f. Cargo, obligación, pretexto, achaque. Uso antiguo y moderno, con sentidos variados.", ["Cuénteme de un achaque del que pueda librarme.", "Esto es un achaque del destino, pero no es para tanto."],
            print(f"Palabra: {palabra}\nDefinición: {definicion}\n\nEjemplos:"),
            [print(f"{i}. {frase}") for i, frase in enumerate(ejemplos, 1)]
        )
    )

def ejercicio_7_cuervo_sinonimos():
    ejecutar_ejercicio(
        "Ejercicio 7: 'Dizque' la sinonimia",
        "Muestra un par de sinónimos (o palabras con uso similar) y pide al usuario que elija la mejor para una frase.",
        lambda: (
            opciones, frase, respuesta == ["Dizque", "Parece que"], "... va a llover, mejor llevemos paraguas.", input(f"Frase: {frase}\nOpciones: {opciones}\n¿Qué palabra completa mejor la frase? ").lower(),
            print("¡Genial! 'Dizque' es perfecto para expresar que la información es de oídas.") if respuesta == "dizque" else print("Buena elección, pero 'dizque' tiene un toque más informal y colombiano.")
        )
    )

def ejercicio_8_cuervo_el_uso_correcto():
    ejecutar_ejercicio(
        "Ejercicio 8: ¿'Por' o 'Para'?",
        "Pide al usuario que elija la preposición correcta ('por' o 'para') en una oración y justifica por qué.",
        lambda: (
            frase, respuesta == "Este regalo es ... mi mamá.", input(f"Frase: {frase}\nElige 'por' o 'para': ").lower(),
            print("¡Correcto! 'Para' indica el destino o el destinatario del regalo.") if respuesta == "para" else print("Incorrecto. 'Por' se usa para indicar la causa o el motivo, no el destinatario.")
        )
    )

def ejercicio_9_cuervo_ortografia():
    ejecutar_ejercicio(
        "Ejercicio 9: 'El error de bulto'",
        "Crea un programa que tenga una lista de palabras mal escritas y pida al usuario que las corrija.",
        lambda: (
            palabras_erroneas, palabras_correctas == ["haiga", "ves", "hiban", "hallá"], ["haya", "vez", "iban", "allá"],
            print("Corrige las siguientes palabras:"),
            [print("¡Correcto!") if input(f"¿Cómo se escribe '{palabra}'? ").lower() == palabras_correctas[palabras_erroneas.index(palabra)] else print(f"¡Incorrecto! La palabra correcta es '{palabras_correctas[palabras_erroneas.index(palabra)]}'.") for palabra in palabras_erroneas]
        )
    )

def ejercicio_10_cuervo_el_origen_de_la_palabra():
    ejecutar_ejercicio(
        "Ejercicio 10: La etimología de la 'guaricha'",
        "Explica el origen de una palabra colombiana y haz un pequeño test para verificar que el usuario entendió.",
        lambda: (
            print("La palabra 'guaricha' en Colombia se usa despectivamente para referirse a una mujer de la calle.\nSu origen proviene del idioma chibcha, donde 'guaricha' significa 'princesa' o 'mujer joven'.\nEl uso de la palabra cambió drásticamente con la conquista."),
            respuesta_correcta, pregunta == "chibcha", "¿De qué idioma proviene la palabra 'guaricha'?",
            print("¡Correcto! Qué interesante, ¿verdad?") if input(f"\n{pregunta} ").lower() == respuesta_correcta else print("¡Incorrecto! La palabra proviene del idioma chibcha.")
        )
    )

# --- EJERCICIOS (11-20) - Riqueza y precisión lingüística de Cuervo ---

def ejercicio_6_cuervo_palabra_del_dia():
    ejecutar_ejercicio(
        "Ejercicio 6: El 'achaque' de la palabra del día",
        "Simula la explicación de Cuervo. Muestra una palabra, su definición y un par de frases de ejemplo.",
        lambda: (
            palabra, definicion, ejemplos == "achaque", "f. Cargo, obligación, pretexto, achaque. Uso antiguo y moderno, con sentidos variados.", ["Cuénteme de un achaque del que pueda librarme.", "Esto es un achaque del destino, pero no es para tanto."],
            print(f"Palabra: {palabra}\nDefinición: {definicion}\n\nEjemplos:"),
            [print(f"{i}. {frase}") for i, frase in enumerate(ejemplos, 1)]
        )
    )

def ejercicio_12_cuervo_la_conjugacion_correcta():
    ejecutar_ejercicio(
        "Ejercicio 12: La conjugación de 'haber'",
        "Completa la oración con la forma correcta del verbo 'haber'.\n'... muchos carros en la calle.'",
        lambda: (
            respuesta_correcta == "hay",
            print("¡Correcto!") if input("Completa: ").lower() == respuesta_correcta else print(f"¡Incorrecto! La forma correcta es '{respuesta_correcta}'.")
        )
    )

def ejercicio_13_cuervo_concordancia_verbal():
    ejecutar_ejercicio(
        "Ejercicio 13: La concordancia del verbo",
        "Pide al usuario que elija el verbo correcto para una oración con un sujeto compuesto.",
        lambda: (
            respuesta_correcta == "corren",
            print("¡Correcto!") if input("Elige 'corren' o 'corre': 'El carro y la moto ... en la autopista'.\nTu respuesta: ").lower() == respuesta_correcta else print(f"¡Incorrecto! La forma correcta es '{respuesta_correcta}' (plural).")
        )
    )

def ejercicio_14_cuervo_el_uso_de_las_comas():
    ejecutar_ejercicio(
        "Ejercicio 14: La coma vocativa",
        "Corrige la oración añadiendo la coma que falta:\n'Hola Juan cómo estás?'",
        lambda: (
            respuesta == input("Escribe la oración corregida: "),
            print("¡Correcto!") if respuesta.lower().strip() in ("hola, juan, cómo estás?", "hola, juan cómo estás?") else print("¡Incorrecto! La coma debe ir después de 'hola' o 'Juan'.")
        )
    )

def ejercicio_15_cuervo_el_significado_de_una_frase():
    ejecutar_ejercicio(
        "Ejercicio 15: La 'ñapa'",
        "La palabra 'ñapa' se refiere a un extra o un regalo que se da por la compra de algo. Usa 'ñapa' en una oración.",
        lambda: (
            frase == input("Escribe una oración con la palabra 'ñapa': "),
            print("¡Excelente! Esa es una 'ñapa' de un buen ejercicio.")
        )
    )

def ejercicio_16_cuervo_palabras_compuestas():
    ejecutar_ejercicio(
        "Ejercicio 16: Palabras compuestas",
        "Las palabras compuestas se forman uniendo dos o más palabras. Ejemplo: 'abre-latas'. Forma una palabra compuesta con 'rompe' y otra palabra.",
        lambda: (
            respuesta == input("Forma una palabra compuesta con 'rompe': "),
            print("¡Muy bien!") if respuesta.startswith("rompe") else print("Inténtalo de nuevo. Asegúrate de que empiece con 'rompe'.")
        )
    )

def ejercicio_17_cuervo_acentos_diacriticos():
    ejecutar_ejercicio(
        "Ejercicio 17: Acentos diacríticos",
        "Elige la palabra correcta: '... perro de mi amigo es muy grande.' y '... es el mejor jugador del equipo'.",
        lambda: (
            respuesta1 == input("Primera palabra (el/él): ").lower(),
            respuesta2 == input("Segunda palabra (el/él): ").lower(),
            print("¡Correcto!") if respuesta1 == "el" and respuesta2 == "él" else print("¡Incorrecto! 'El' sin acento es un artículo, 'él' con acento es un pronombre.")
        )
    )

def ejercicio_18_cuervo_expresiones_colombianas():
    ejecutar_ejercicio(
        "Ejercicio 18: 'Hacer el oso'",
        "La expresión 'hacer el oso' significa hacer el ridículo. Usa esta frase en una oración.",
        lambda: (
            frase == input("Escribe una oración con 'hacer el oso': "),
            print("¡Qué bien! Ya sabes cómo 'hacer el oso' en una frase.")
        )
    )

def ejercicio_19_cuervo_uso_de_mayusculas():
    ejecutar_ejercicio(
        "Ejercicio 19: Mayúsculas y minúsculas",
        "Corrige la oración:\n'La Ciudad de Bogotá es la capital de Colombia.'",
        lambda: (
            respuesta == input("Escribe la oración corregida: "),
            print("¡Correcto!") if respuesta.lower().strip() == "la ciudad de bogotá es la capital de colombia." else print("¡Incorrecto! Las mayúsculas solo van en nombres propios.")
        )
    )

def ejercicio_20_cuervo_refranes():
    ejecutar_ejercicio(
        "Ejercicio 20: El refrán",
        "Completa el refrán: 'Al que madruga...' ",
        lambda: (
            respuesta == input("Completa la frase: ").lower(),
            print("¡Correcto! 'Dios le ayuda'.") if 'dios le ayuda' in respuesta else print("¡Esa no es! La respuesta es 'Dios le ayuda'.")
        )
    )

# --- EJERCICIOS (21-30) - Verbos: Ser y Estar ---

def ejercicio_22_ser_o_estar_con_profesiones():
    ejecutar_ejercicio(
        "Ejercicio 22: Ser para profesiones",
        "Usa 'ser' para completar la oración que indica una profesión.\n'Mi padre ... médico.'",
        lambda: (
            respuesta == input("Completa la oración: 'Mi padre ... médico.' "),
            print("¡Correcto!") if respuesta.lower() == "es" else print("¡Incorrecto! 'Ser' se usa para profesiones.")
        )
    )


def ejercicio_22_ser_o_estar_con_profesiones():
    ejecutar_ejercicio(
        "Ejercicio 22: Ser para profesiones",
        "Usa 'ser' para completar la oración que indica una profesión.\n'Mi padre ... médico.'",
        lambda: (
            respuesta == input("Completa la oración: 'Mi padre ... médico.' "),
            print("¡Correcto!") if respuesta.lower() == "es" else print("¡Incorrecto! 'Ser' se usa para profesiones.")
        )
    )

def ejercicio_23_ser_o_estar_con_localizacion():
    ejecutar_ejercicio(
        "Ejercicio 23: Estar para la localización",
        "Usa 'estar' para indicar la ubicación de una persona.\n'Juan ... en la casa de María.'",
        lambda: (
            respuesta == input("Completa la oración: 'Juan ... en la casa de María.' "),
            print("¡Correcto!") if respuesta.lower() == "está" else print("¡Incorrecto! 'Estar' se usa para indicar una ubicación.")
        )
    )

def ejercicio_25_ser_con_hora_y_fecha():
    ejecutar_ejercicio(
        "Ejercicio 25: Ser con hora y fecha",
        "Usa 'ser' para dar la hora y la fecha. Completa:\n'Hoy ... 15 de marzo.'\n'Son las 10 de la mañana.'",
        lambda: (
            respuesta == input("Completa la oración: 'Hoy ... 15 de marzo.' ").lower(),
            print("¡Correcto!") if respuesta == "es" else print("¡Incorrecto! 'Ser' se usa para dar la fecha.")
        )
    )


def ejercicio_25_ser_con_hora_y_fecha():
    ejecutar_ejercicio(
        "Ejercicio 25: Ser con hora y fecha",
        "Usa 'ser' para dar la hora y la fecha. Completa:\n'Hoy ... 15 de marzo.'\n'Son las 10 de la mañana.'",
        lambda: (
            respuesta == input("Completa la oración: 'Hoy ... 15 de marzo.' ").lower(),
            print("¡Correcto!") if respuesta == "es" else print("¡Incorrecto! 'Ser' se usa para dar la fecha.")
        )
    )

def ejercicio_26_estar_con_estado_de_animo():
    ejecutar_ejercicio(
        "Ejercicio 26: Estar con estados de ánimo",
        "Usa 'estar' para describir un estado de ánimo. Completa:\n'Mi amigo ... muy feliz hoy.'",
        lambda: (
            respuesta == input("Completa la oración: 'Mi amigo ... muy feliz hoy.' ").lower(),
            print("¡Correcto!") if respuesta == "está" else print("¡Incorrecto! 'Estar' se usa para estados temporales.")
        )
    )

def ejercicio_27_ser_o_estar_con_nacionalidad():
    ejecutar_ejercicio(
        "Ejercicio 27: Ser con nacionalidad",
        "Usa 'ser' para indicar la nacionalidad.\n'Ella ... colombiana.'",
        lambda: (
            respuesta == input("Completa la oración: 'Ella ... colombiana.' ").lower(),
            print("¡Correcto!") if respuesta == "es" else print("¡Incorrecto! 'Ser' se usa para nacionalidades.")
        )
    )

def ejercicio_28_ser_para_origen():
    ejecutar_ejercicio(
        "Ejercicio 28: Ser para el origen",
        "Usa 'ser' para indicar el origen. Completa:\n'Los estudiantes ... de Cali.'",
        lambda: (
            respuesta == input("Completa la oración: 'Los estudiantes ... de Cali.' ").lower(),
            print("¡Correcto!") if respuesta == "son" else print("¡Incorrecto! 'Ser' se usa para el origen.")
        )
    )

def ejercicio_29_estar_para_condicion():
    ejecutar_ejercicio(
        "Ejercicio 29: Estar para una condición",
        "Usa 'estar' para describir una condición física o estado temporal. Completa:\n'Yo ... cansado.'",
        lambda: (
            respuesta == input("Completa la oración: 'Yo ... cansado.' ").lower(),
            print("¡Correcto!") if respuesta == "estoy" else print("¡Incorrecto! 'Estar' se usa para condiciones.")
        )
    )

def ejercicio_31_uso_de_la_coma():
    ejecutar_ejercicio(
        "Ejercicio 31: Uso de la coma",
        "Añade una coma para separar los elementos de una enumeración. 'Compré frutas leche y pan.'",
        lambda: (
            respuesta == input("Escribe la oración con comas: "),
            print("¡Correcto!") if "," in respuesta else print("¡Incorrecto! Faltan comas para separar los elementos.")
        )
    )


# --- EJERCICIOS (31-40) - Puntuación y signos ortográficos ---

def ejercicio_31_uso_de_la_coma():
    ejecutar_ejercicio(
        "Ejercicio 31: Uso de la coma",
        "Añade una coma para separar los elementos de una enumeración. 'Compré frutas leche y pan.'",
        lambda: (
            respuesta == input("Escribe la oración con comas: "),
            print("¡Correcto!") if "," in respuesta else print("¡Incorrecto! Faltan comas para separar los elementos.")
        )
    )

def ejercicio_32_coma_vocativa():
    ejecutar_ejercicio(
        "Ejercicio 32: La coma vocativa",
        "Corrige la oración añadiendo la coma que falta:\n'Buenos días papá cómo estás?'",
        lambda: (
            respuesta == input("Escribe la oración corregida: "),
            print("¡Correcto!") if respuesta.lower().strip() in ("buenos días, papá, cómo estás?", "buenos días, papá cómo estás?") else print("¡Incorrecto! La coma debe ir después de 'días' o 'papá'.")
        )
    )

def ejercicio_33_punto_y_coma():
    ejecutar_ejercicio(
        "Ejercicio 33: El punto y coma",
        "Usa un punto y coma para unir dos oraciones relacionadas. 'El cielo está nublado; parece que va a llover.'",
        lambda: (
            respuesta == input("Escribe una oración usando punto y coma: "),
            print("¡Correcto!") if ";" in respuesta else print("¡Incorrecto! El punto y coma une oraciones relacionadas.")
        )
    )

def ejercicio_34_puntos_suspensivos():
    ejecutar_ejercicio(
        "Ejercicio 34: Puntos suspensivos",
        "Usa los puntos suspensivos para indicar una interrupción. 'No sé qué decir...'",
        lambda: (
            respuesta == input("Escribe una oración que termine con puntos suspensivos: "),
            print("¡Correcto!") if "..." in respuesta else print("¡Incorrecto! Los puntos suspensivos son tres puntos seguidos.")
        )
    )

def ejercicio_35_dos_puntos():
    ejecutar_ejercicio(
        "Ejercicio 35: Dos puntos",
        "Usa dos puntos para introducir una enumeración. 'Mis colores favoritos son: azul, verde y rojo.'",
        lambda: (
            respuesta == input("Escribe una oración que use dos puntos para introducir una lista: "),
            print("¡Correcto!") if ":" in respuesta else print("¡Incorrecto! Los dos puntos introducen una lista o una explicación.")
        )
    )

def ejercicio_36_comillas():
    ejecutar_ejercicio(
        "Ejercicio 36: Uso de comillas",
        "Usa comillas para citar algo. 'Mi mamá siempre dice: 'El que mucho abarca, poco aprieta.''",
        lambda: (
            respuesta == input("Escribe una oración con comillas para una cita: "),
            print("¡Correcto!") if '"' in respuesta or "'" in respuesta else print("¡Incorrecto! Las comillas se usan para citas o para resaltar palabras.")
        )
    )

def ejercicio_37_signos_de_interrogacion():
    ejecutar_ejercicio(
        "Ejercicio 37: Signos de interrogación",
        "Usa los signos de interrogación para una pregunta. '¿Cómo estás?'",
        lambda: (
            respuesta == input("Escribe una pregunta: "),
            print("¡Correcto!") if "?" in respuesta and "¿" in respuesta else print("¡Incorrecto! Las preguntas en español usan '¿' al principio y '?' al final.")
        )
    )

def ejercicio_38_signos_de_exclamacion():
    ejecutar_ejercicio(
        "Ejercicio 38: Signos de exclamación",
        "Usa los signos de exclamación para una expresión de sorpresa. '¡Qué sorpresa!'",
        lambda: (
            respuesta == input("Escribe una exclamación: "),
            print("¡Correcto!") if "!" in respuesta and "¡" in respuesta else print("¡Incorrecto! Las exclamaciones en español usan '¡' al principio y '!' al final.")
        )
    )

def ejercicio_39_parentesis():
    ejecutar_ejercicio(
        "Ejercicio 39: El uso de paréntesis",
        "Usa paréntesis para añadir información adicional. 'El río Magdalena (el más largo de Colombia) es vital.'",
        lambda: (
            respuesta == input("Escribe una oración que use paréntesis: "),
            print("¡Correcto!") if "(" in respuesta and ")" in respuesta else print("¡Incorrecto! Los paréntesis se usan para información extra.")
        )
    )

def ejercicio_40_guion_largo():
    ejecutar_ejercicio(
        "Ejercicio 40: El guion largo",
        "Usa un guion largo para introducir un diálogo. '—¿Cómo estás? —Bien, gracias.'",
        lambda: (
            respuesta == input("Escribe un diálogo usando guion largo: "),
            print("¡Correcto!") if "—" in respuesta else print("¡Incorrecto! El guion largo se usa para diálogos.")
        )
    )

# --- EJERCICIOS (41-50) - Concordancia y género ---

def ejercicio_42_genero_de_sustantivos():
    ejecutar_ejercicio(
        "Ejercicio 42: El género de los sustantivos",
        "Elige el artículo correcto: '... agua' y '... problema'.",
        lambda: (
            print("1. ... agua."),
            print("2. ... problema."),
            respuestas == {"1": "el", "2": "el"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_42_genero_de_sustantivos():
    ejecutar_ejercicio(
        "Ejercicio 42: El género de los sustantivos",
        "Elige el artículo correcto: '... agua' y '... problema'.",
        lambda: (
            print("1. ... agua."),
            print("2. ... problema."),
            respuestas == {"1": "el", "2": "el"},
            for num, correcta in respuestas.items():
                respuesta == input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_43_concordancia_verbal_compuesta():
    ejecutar_ejercicio(
        "Ejercicio 43: Concordancia verbal con sujeto compuesto",
        "Completa la frase: 'La música y el cine ... populares.'",
        lambda: (
            respuesta = input("Completa con el verbo correcto: "),
            print("¡Correcto!") if respuesta.lower() == "son" else print("¡Incorrecto! El sujeto compuesto exige el verbo en plural.")
        )
    )

def ejercicio_44_genero_y_plural():
    ejecutar_ejercicio(
        "Ejercicio 44: Género y plural",
        "Completa la frase con el artículo y sustantivo correctos: '... lápiz' -> plural.",
        lambda: (
            respuesta = input("Plural de 'el lápiz': "),
            print("¡Correcto!") if respuesta.lower() == "los lápices" else print("¡Incorrecto! No olvides cambiar el artículo y la terminación del sustantivo.")
        )
    )

def ejercicio_45_concordancia_con_numeros():
    ejecutar_ejercicio(
        "Ejercicio 45: Concordancia con números",
        "Completa la frase: 'Veinte ... (día) de febrero.'",
        lambda: (
            respuesta = input("Completa la frase: "),
            print("¡Correcto!") if respuesta.lower() == "días" else print("¡Incorrecto! El número 'veinte' exige el sustantivo en plural.")
        )
    )

def ejercicio_46_pronombres_personales():
    ejecutar_ejercicio(
        "Ejercicio 46: Pronombres personales",
        "Sustituye el nombre por el pronombre correcto: 'Juan y yo vamos al cine.'",
        lambda: (
            respuesta = input("Escribe la oración usando un pronombre: "),
            print("¡Correcto!") if "nosotros" in respuesta.lower() else print("¡Incorrecto! El pronombre es 'nosotros'.")
        )
    )

def ejercicio_47_concordancia_adjetivo_con_varios_sustantivos():
    ejecutar_ejercicio(
        "Ejercicio 47: Concordancia con varios sustantivos",
        "Completa la frase: 'El libro y la revista son ... (interesante).'",
        lambda: (
            respuesta = input("Completa la frase: "),
            print("¡Correcto!") if respuesta.lower() == "interesantes" else print("¡Incorrecto! El adjetivo debe concordar en plural.")
        )
    )

def ejercicio_48_genero_de_nombres_propios():
    ejecutar_ejercicio(
        "Ejercicio 48: Género de nombres propios",
        "Elige el artículo correcto: '... Madrid' y '... Bogotá'.",
        lambda: (
            print("1. ... Madrid."),
            print("2. ... Bogotá."),
            respuestas = {"1": "el", "2": "la"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print("¡Incorrecto! La forma correcta es 'el Madrid' y 'la Bogotá'.")
        )
    )

def ejercicio_49_plural_de_palabras_terminadas_en_z():
    ejecutar_ejercicio(
        "Ejercicio 49: Plural de palabras terminadas en 'z'",
        "Escribe el plural de 'pez' y 'luz'.",
        lambda: (
            respuesta1 = input("Plural de 'pez': "),
            respuesta2 = input("Plural de 'luz': "),
            print("¡Correcto!") if respuesta1.lower() == "peces" and respuesta2.lower() == "luces" else print("¡Incorrecto! Las palabras terminadas en 'z' hacen el plural con '-ces'.")
        )
    )

def ejercicio_50_concordancia_pronominal():
    ejecutar_ejercicio(
        "Ejercicio 50: Concordancia pronominal",
        "Sustituye la palabra por el pronombre correcto: 'Vi a María en el cine.'",
        lambda: (
            respuesta = input("Reescribe la oración usando un pronombre: "),
            print("¡Correcto!") if "la vi" in respuesta.lower() else print("¡Incorrecto! El pronombre de objeto directo para 'María' es 'la'.")
        )
    )

# --- EJERCICIOS (51-60) - Uso de preposiciones ---

def ejercicio_51_preposicion_a_con_verbos_de_movimiento():
    ejecutar_ejercicio(
        "Ejercicio 51: Preposición 'a'",
        "Usa la preposición 'a' para indicar movimiento. Completa: 'Voy ... la escuela.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "a" else print("¡Incorrecto! 'A' se usa para indicar destino.")
        )
    )

def ejercicio_52_preposicion_de_con_origen():
    ejecutar_ejercicio(
        "Ejercicio 52: Preposición 'de'",
        "Usa la preposición 'de' para indicar origen. Completa: 'Soy ... Colombia.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "de" else print("¡Incorrecto! 'De' indica procedencia.")
        )
    )

def ejercicio_53_preposicion_con_para_compania():
    ejecutar_ejercicio(
        "Ejercicio 53: Preposición 'con'",
        "Usa la preposición 'con' para indicar compañía. Completa: 'Fui al cine ... mis amigos.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "con" else print("¡Incorrecto! 'Con' indica compañía.")
        )
    )

def ejercicio_54_preposicion_en_con_lugar():
    ejecutar_ejercicio(
        "Ejercicio 54: Preposición 'en'",
        "Usa la preposición 'en' para indicar un lugar. Completa: 'El libro está ... la mesa.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "en" else print("¡Incorrecto! 'En' indica ubicación.")
        )
    )

def ejercicio_55_preposicion_para_con_proposito():
    ejecutar_ejercicio(
        "Ejercicio 55: Preposición 'para'",
        "Usa la preposición 'para' para indicar propósito. Completa: 'Estudio ... mi examen.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "para" else print("¡Incorrecto! 'Para' indica la finalidad.")
        )
    )

def ejercicio_56_preposicion_por_con_causa():
    ejecutar_ejercicio(
        "Ejercicio 56: Preposición 'por'",
        "Usa la preposición 'por' para indicar causa o motivo. Completa: 'Lo hice ... ti.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "por" else print("¡Incorrecto! 'Por' se usa para la causa.")
        )
    )

def ejercicio_57_preposicion_entre_con_intervalo():
    ejecutar_ejercicio(
        "Ejercicio 57: Preposición 'entre'",
        "Usa la preposición 'entre' para indicar un intervalo. Completa: 'La tienda abre ... 8 a.m. y 6 p.m.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "entre" else print("¡Incorrecto! 'Entre' se usa para intervalos.")
        )
    )

def ejercicio_58_preposicion_sin_con_carencia():
    ejecutar_ejercicio(
        "Ejercicio 58: Preposición 'sin'",
        "Usa la preposición 'sin' para indicar falta de algo. Completa: 'No puedo ver ... mis gafas.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "sin" else print("¡Incorrecto! 'Sin' indica carencia.")
        )
    )

def ejercicio_59_preposicion_sobre_con_lugar():
    ejecutar_ejercicio(
        "Ejercicio 59: Preposición 'sobre'",
        "Usa la preposición 'sobre' para indicar que algo está encima de otra cosa. Completa: 'El libro está ... la mesa.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "sobre" else print("¡Incorrecto! 'Sobre' indica una posición superior.")
        )
    )

def ejercicio_60_preposicion_hasta_con_limite():
    ejecutar_ejercicio(
        "Ejercicio 60: Preposición 'hasta'",
        "Usa la preposición 'hasta' para indicar un límite. Completa: 'Corrí ... el final de la calle.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "hasta" else print("¡Incorrecto! 'Hasta' indica un límite o punto final.")
        )
    )

# --- EJERCICIOS (61-70) - Diferencias léxicas ---

def ejercicio_61_sino_vs_si_no():
    ejecutar_ejercicio(
        "Ejercicio 61: 'Sino' vs. 'si no'",
        "Elige la opción correcta. 'No es blanco, ... negro.' y '... estudias, no apruebas.'",
        lambda: (
            print("1. No es blanco, ... negro."),
            print("2. ... estudias, no apruebas."),
            respuestas = {"1": "sino", "2": "si no"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_62_porque_vs_por_que():
    ejecutar_ejercicio(
        "Ejercicio 62: 'Porque' vs. 'por qué'",
        "Completa: '¿... no fuiste?' y 'No fui ... estaba enfermo.'",
        lambda: (
            print("1. ¿... no fuiste?"),
            print("2. No fui ... estaba enfermo."),
            respuestas = {"1": "por qué", "2": "porque"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_63_tambien_vs_tan_bien():
    ejecutar_ejercicio(
        "Ejercicio 63: 'También' vs. 'tan bien'",
        "Completa: 'Yo ... quiero ir.' y 'Cantas ... que me emocionas.'",
        lambda: (
            print("1. Yo ... quiero ir."),
            print("2. Cantas ... que me emocionas."),
            respuestas = {"1": "también", "2": "tan bien"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_64_adonde_vs_a_donde():
    ejecutar_ejercicio(
        "Ejercicio 64: 'Adonde' vs. 'a donde'",
        "Completa: 'No sé ... vamos.' y '... vayas, te seguiré.'",
        lambda: (
            print("1. No sé ... vamos."),
            print("2. ... vayas, te seguiré."),
            respuestas = {"1": "a dónde", "2": "adonde"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_65_demas_vs_de_mas():
    ejecutar_ejercicio(
        "Ejercicio 65: 'Demás' vs. 'de más'",
        "Completa: 'Los ... no vinieron.' y 'No compres comida ... .'",
        lambda: (
            print("1. Los ... no vinieron."),
            print("2. No compres comida ... ."),
            respuestas = {"1": "demás", "2": "de más"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_66_asimismo_vs_a_si_mismo():
    ejecutar_ejercicio(
        "Ejercicio 66: 'Asimismo' vs. 'a sí mismo'",
        "Completa: 'Quiero un café, ... un pastel.' y 'Se habla ... cuando está solo.'",
        lambda: (
            print("1. Quiero un café, ... un pastel."),
            print("2. Se habla ... cuando está solo."),
            respuestas = {"1": "asimismo", "2": "a sí mismo"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_67_conque_vs_con_que_vs_con_que():
    ejecutar_ejercicio(
        "Ejercicio 67: 'Conque', 'con que', 'con qué'",
        "Completa: '... no fuiste a la fiesta.', 'La razón ... te llamé es importante.' y '¿... dinero compraste eso?'",
        lambda: (
            print("1. ... no fuiste a la fiesta."),
            print("2. La razón ... te llamé es importante."),
            print("3. ¿... dinero compraste eso?"),
            respuestas = {"1": "conque", "2": "con que", "3": "con qué"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_68_haber_vs_a_ver():
    ejecutar_ejercicio(
        "Ejercicio 68: 'Haber' vs. 'a ver'",
        "Completa: 'Tiene que ... un error.' y '... si me escuchas.'",
        lambda: (
            print("1. Tiene que ... un error."),
            print("2. ... si me escuchas."),
            respuestas = {"1": "haber", "2": "a ver"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_69_acerca_de_vs_a_cerca_de():
    ejecutar_ejercicio(
        "Ejercicio 69: 'Acerca de' vs. 'a cerca de'",
        "Completa: 'Hablamos ... la película.' y 'Vive ... la estación.'",
        lambda: (
            print("1. Hablamos ... la película."),
            print("2. Vive ... la estación."),
            respuestas = {"1": "acerca de", "2": "a cerca de"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

def ejercicio_70_porvenir_vs_por_venir():
    ejecutar_ejercicio(
        "Ejercicio 70: 'Porvenir' vs. 'por venir'",
        "Completa: 'El ... es incierto.' y 'Falta mucho ... la cosecha.'",
        lambda: (
            print("1. El ... es incierto."),
            print("2. Falta mucho ... la cosecha."),
            respuestas = {"1": "porvenir", "2": "por venir"},
            for num, correcta in respuestas.items():
                respuesta = input(f"Respuesta {num}: ").lower()
                print("¡Correcto!") if respuesta == correcta else print(f"¡Incorrecto! La forma correcta es '{correcta}'.")
        )
    )

# --- EJERCICIOS (71-80) - Pronombres: Leísmo, Laísmo, Loísmo ---

def ejercicio_71_leismo_vs_loismo():
    ejecutar_ejercicio(
        "Ejercicio 71: Leísmo vs Loísmo",
        "Corrige la oración si es necesario: 'Vi a Juan y le saludé.'",
        lambda: (
            respuesta = input("¿Es correcta la oración? (s/n) "),
            print("¡Correcto! Es leísmo, se debería usar 'lo'.") if respuesta.lower() == "s" else print("¡Incorrecto! La forma correcta en español neutro es 'lo saludé'.")
        )
    )

def ejercicio_72_leismo_de_cortesia():
    ejecutar_ejercicio(
        "Ejercicio 72: Leísmo de cortesía",
        "Usa 'le' para referirte a 'usted'. Completa: 'A su padre, ... respeto mucho.'",
        lambda: (
            respuesta = input("Completa la oración: "),
            print("¡Correcto!") if respuesta.lower() == "le" else print("¡Incorrecto! El leísmo de cortesía es aceptado con 'usted'.")
        )
    )

def ejercicio_73_laismo_vs_loismo_femenino():
    ejecutar_ejercicio(
        "Ejercicio 73: Laísmo vs Loísmo (femenino)",
        "Corrige la oración: 'A mi hermana, la he visto en el parque.'",
        lambda: (
            respuesta = input("¿Es correcta la oración? (s/n) "),
            print("¡Correcto!") if respuesta.lower() == "s" else print("¡Incorrecto! La frase es correcta. 'La' es el pronombre de objeto directo para un sustantivo femenino.")
        )
    )

def ejercicio_74_loismo_vs_leismo_masculino():
    ejecutar_ejercicio(
        "Ejercicio 74: Loísmo vs Leísmo (masculino)",
        "Corrige la oración: 'A mi hermano, le vi en la calle.'",
        lambda: (
            respuesta = input("¿Es correcta la oración? (s/n) "),
            print("¡Correcto!") if respuesta.lower() == "n" else print("¡Incorrecto! La forma correcta es 'lo vi', no 'le vi'.")
        )
    )

def ejercicio_75_pronombre_de_objeto_directo():
    ejecutar_ejercicio(
        "Ejercicio 75: Pronombre de objeto directo",
        "Sustituye el objeto por el pronombre correcto: 'Compré la camisa.'",
        lambda: (
            respuesta = input("Reescribe la oración: "),
            print("¡Correcto!") if "la compré" in respuesta.lower() else print("¡Incorrecto! 'La' es el pronombre de objeto directo.")
        )
    )

def ejercicio_76_pronombre_de_objeto_indirecto():
    ejecutar_ejercicio(
        "Ejercicio 76: Pronombre de objeto indirecto",
        "Sustituye el objeto por el pronombre correcto: 'Di el libro a María.'",
        lambda: (
            respuesta = input("Reescribe la oración: "),
            print("¡Correcto!") if "le di el libro" in respuesta.lower() else print("¡Incorrecto! 'Le' es el pronombre de objeto indirecto.")
        )
    )

def ejercicio_77_combinacion_de_pronombres():
    ejecutar_ejercicio(
        "Ejercicio 77: Combinación de pronombres",
        "Combina los pronombres para reescribir la frase: 'Di el libro a Juan.'",
        lambda: (
            respuesta = input("Reescribe la oración usando pronombres: "),
            print("¡Correcto!") if "se lo di" in respuesta.lower() else print("¡Incorrecto! 'Se lo di' es la forma correcta.")
        )
    )

def ejercicio_78_leismo_plural():
    ejecutar_ejercicio(
        "Ejercicio 78: Leísmo plural",
        "Corrige la oración si es necesario: 'A los niños, les vi en el parque.'",
        lambda: (
            respuesta = input("¿Es correcta la oración? (s/n) "),
            print("¡Correcto! Es leísmo, se debería usar 'los'.") if respuesta.lower() == "s" else print("¡Incorrecto! La forma correcta es 'los vi'.")
        )
    )

def ejercicio_79_laismo_plural():
    ejecutar_ejercicio(
        "Ejercicio 79: Laísmo plural",
        "Corrige la oración si es necesario: 'A las niñas, las vi en el parque.'",
        lambda: (
            respuesta = input("¿Es correcta la oración? (s/n) "),
            print("¡Correcto!") if respuesta.lower() == "s" else print("¡Incorrecto! La oración es correcta.")
        )
    )

def ejercicio_80_loismo_plural():
    ejecutar_ejercicio(
        "Ejercicio 80: Loísmo plural",
        "Corrige la oración si es necesario: 'A mis amigos, los compré un regalo.'",
        lambda: (
            respuesta = input("¿Es correcta la oración? (s/n) "),
            print("¡Correcto! Es loísmo, se debería usar 'les'.") if respuesta.lower() == "n" else print("¡Incorrecto! El verbo 'comprar' exige objeto indirecto ('les').")
        )
    )

# --- EJERCICIOS (81-90) - Arcaísmos y palabras en desuso (inspiradas en Cuervo) ---

def ejercicio_81_palabra_arcaica_doquier():
    ejecutar_ejercicio(
        "Ejercicio 81: El 'doquier' de Cuervo",
        "Usa la palabra 'doquier' (dondequiera) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'doquier': "),
            print("¡Excelente! 'Doquier' es un buen ejemplo de una palabra en desuso.")
        )
    )

def ejercicio_82_palabra_arcaica_empero():
    ejecutar_ejercicio(
        "Ejercicio 82: El 'empero' de la tradición",
        "Usa la palabra 'empero' (sin embargo) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'empero': "),
            print("¡Perfecto! 'Empero' da un toque de formalidad a tu frase.")
        )
    )

def ejercicio_83_palabra_arcaica_maguer():
    ejecutar_ejercicio(
        "Ejercicio 83: El 'maguer' desconocido",
        "Usa la palabra 'maguer' (a pesar de) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'maguer': "),
            print("¡Fantástico! Has revivido un arcaísmo.")
        )
    )

def ejercicio_84_palabra_arcaica_enderezar():
    ejecutar_ejercicio(
        "Ejercicio 84: 'Enderezar' el camino",
        "Usa la palabra 'enderezar' (poner derecho) en una oración. En la obra de Cuervo esta palabra tenía un uso específico.",
        lambda: (
            respuesta = input("Escribe una oración con 'enderezar': "),
            print("¡Bien! 'Enderezar' puede usarse literal o figurativamente.")
        )
    )

def ejercicio_85_palabra_desuso_cuita():
    ejecutar_ejercicio(
        "Ejercicio 85: La 'cuita' del alma",
        "Usa la palabra 'cuita' (pena, aflicción) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'cuita': "),
            print("¡Magnífico! 'Cuita' es una palabra con mucha expresividad.")
        )
    )

def ejercicio_86_palabra_desuso_encono():
    ejecutar_ejercicio(
        "Ejercicio 86: El 'encono' del pasado",
        "Usa la palabra 'encono' (odio, rencor) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'encono': "),
            print("¡Excelente! El 'encono' es un sentimiento que Cuervo analizaba.")
        )
    )

def ejercicio_87_palabra_desuso_caduco():
    ejecutar_ejercicio(
        "Ejercicio 87: Lo 'caduco' del tiempo",
        "Usa la palabra 'caduco' (obsoleto, que ha pasado de moda) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'caduco': "),
            print("¡Muy bien! 'Caduco' se usa para lo que ya no tiene vigencia.")
        )
    )

def ejercicio_88_palabra_desuso_a_sabiendas_de():
    ejecutar_ejercicio(
        "Ejercicio 88: 'A sabiendas de'",
        "Usa la locución 'a sabiendas de' (sabiendo algo) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'a sabiendas de': "),
            print("¡Perfecto! Esta locución es muy formal.")
        )
    )

def ejercicio_89_palabra_desuso_verbigracia():
    ejecutar_ejercicio(
        "Ejercicio 89: El 'verbigracia' de los ejemplos",
        "Usa la palabra 'verbigracia' (por ejemplo) en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'verbigracia': "),
            print("¡Fantástico! 'Verbigracia' es una palabra elegante para dar ejemplos.")
        )
    )

def ejercicio_90_palabra_desuso_crespo():
    ejecutar_ejercicio(
        "Ejercicio 90: El 'crespo' de la ira",
        "En la obra de Cuervo, 'crespo' a veces se usaba para referirse a la ira. Usa esta acepción en una oración.",
        lambda: (
            respuesta = input("Escribe una oración con 'crespo' en este sentido: "),
            print("¡Bien! Has descubierto una acepción inusual.")
        )
    )

# --- EJERCICIOS (91-100) - Expresiones idiomáticas y refranes ---

def ejercicio_91_dicho_colombiano_no_dar_papaya():
    ejecutar_ejercicio(
        "Ejercicio 91: 'No dar papaya'",
        "Explica el significado de la frase 'no dar papaya' y úsala en una oración.",
        lambda: (
            print("Significa no dar oportunidad para que algo malo suceda.\n"),
            respuesta = input("Usa 'no dar papaya' en una oración: "),
            print("¡Correcto! Es una de las frases más usadas en Colombia.")
        )
    )

def ejercicio_92_dicho_colombiano_estar_mamando_gallo():
    ejecutar_ejercicio(
        "Ejercicio 92: 'Estar mamando gallo'",
        "Explica el significado de 'estar mamando gallo' y úsala en una oración.",
        lambda: (
            print("Significa estar bromeando o perdiendo el tiempo.\n"),
            respuesta = input("Usa 'estar mamando gallo' en una oración: "),
            print("¡Perfecto! Ya eres un 'mamo gallo' experto.")
        )
    )

def ejercicio_93_dicho_colombiano_agarrar_el_palo():
    ejecutar_ejercicio(
        "Ejercicio 93: 'Agarrar el palo'",
        "Explica el significado de 'agarrar el palo' y úsala en una oración.",
        lambda: (
            print("Significa entender un concepto o habilidad de forma rápida.\n"),
            respuesta = input("Usa 'agarrar el palo' en una oración: "),
            print("¡Así es! Has 'agarrado el palo' a esta lección.")
        )
    )

def ejercicio_94_dicho_colombiano_tener_la_pata_mala():
    ejecutar_ejercicio(
        "Ejercicio 94: 'Tener la pata mala'",
        "Explica el significado de 'tener la pata mala' y úsala en una oración.",
        lambda: (
            print("Significa tener mala suerte.\n"),
            respuesta = input("Usa 'tener la pata mala' en una oración: "),
            print("¡Muy bien! Esperemos que no tengas la pata mala.")
        )
    )

def ejercicio_95_refran_al_mal_tiempo_buena_cara():
    ejecutar_ejercicio(
        "Ejercicio 95: Refrán 'Al mal tiempo, buena cara'",
        "Explica el significado de este refrán y completa la frase.",
        lambda: (
            print("Significa que hay que ser optimista ante las adversidades.\n"),
            respuesta = input("Completa el refrán: 'Al mal tiempo, ... ' "),
            print("¡Correcto! 'buena cara'.") if respuesta.lower() == "buena cara" else print("¡Esa no es! La respuesta es 'buena cara'.")
        )
    )

def ejercicio_96_refran_mas_vale_tarde_que_nunca():
    ejecutar_ejercicio(
        "Ejercicio 96: Refrán 'Más vale tarde que nunca'",
        "Explica el significado de este refrán y completa la frase.",
        lambda: (
            print("Significa que es mejor hacer algo tarde que no hacerlo en absoluto.\n"),
            respuesta = input("Completa el refrán: 'Más vale ... ' "),
            print("¡Correcto! 'tarde que nunca'.") if "tarde que nunca" in respuesta.lower() else print("¡Esa no es! La respuesta es 'tarde que nunca'.")
        )
    )

def ejercicio_97_refran_no_hay_mal_que_por_bien_no_venga():
    ejecutar_ejercicio(
        "Ejercicio 97: Refrán 'No hay mal que por bien no venga'",
        "Explica el significado de este refrán y completa la frase.",
        lambda: (
            print("Significa que de una situación mala se puede sacar algo bueno.\n"),
            respuesta = input("Completa el refrán: 'No hay mal que por ... ' "),
            print("¡Correcto! 'bien no venga'.") if "bien no venga" in respuesta.lower() else print("¡Esa no es! La respuesta es 'bien no venga'.")
        )
    )

def ejercicio_98_refran_a_quien_madruga():
    ejecutar_ejercicio(
        "Ejercicio 98: Refrán 'A quien madruga'",
        "Explica el significado de este refrán y completa la frase.",
        lambda: (
            print("Significa que la persona que es diligente obtiene beneficios.\n"),
            respuesta = input("Completa el refrán: 'A quien madruga, ... ' "),
            print("¡Correcto! 'Dios le ayuda'.") if "dios le ayuda" in respuesta.lower() else print("¡Esa no es! La respuesta es 'Dios le ayuda'.")
        )
    )

def ejercicio_99_refran_el_que_mucho_abarca():
    ejecutar_ejercicio(
        "Ejercicio 99: Refrán 'El que mucho abarca...'",
        "Explica el significado de este refrán y completa la frase.",
        lambda: (
            print("Significa que es mejor no intentar hacer demasiadas cosas a la vez, pues no se completará bien ninguna.\n"),
            respuesta = input("Completa el refrán: 'El que mucho abarca, ... ' "),
            print("¡Correcto! 'poco aprieta'.") if "poco aprieta" in respuesta.lower() else print("¡Esa no es! La respuesta es 'poco aprieta'.")
        )
    )

def ejercicio_100_refran_mas_sabe_el_diablo():
    ejecutar_ejercicio(
        "Ejercicio 100: Refrán 'Más sabe el diablo...'",
        "Explica el significado de este refrán y completa la frase.",
        lambda: (
            print("Significa que la experiencia es más valiosa que el conocimiento teórico o la juventud.\n"),
            respuesta = input("Completa el refrán: 'Más sabe el diablo por ... que por diablo.' "),
            print("¡Correcto! 'viejo'.") if "viejo" in respuesta.lower() else print("¡Esa no es! La respuesta es 'viejo'.")
        )
    )

# --- MENÚ PRINCIPAL ---
def mostrar_menu():
    """Muestra el menú de ejercicios."""
    print("--- Serie de Ejercicios: Español de Colombia ---")
    print("¡Elige un ejercicio para practicar! (o 's' para salir)")
    for i in range(1, 101):
        print(f"{i}. {ejercicios[str(i)].__name__.replace('_', ' ').replace('ejercicio ', '').title()}")
    
    print("\n--- ¡Has completado la serie de 100 ejercicios! ---")

def main():
    """Función principal para ejecutar el programa."""
    limpiar_consola()
    
    ejercicios = {
        str(i): globals()[f"ejercicio_{i}"] for i in range(1, 101)
    }
    
    while True:
        mostrar_menu()
        opcion = input("Ingresa el número del ejercicio: ").lower()
        
        if opcion == 's':
            print("¡Chao, pues! Vuelve pronto.")
            break
        
        if opcion in ejercicios:
            ejercicios[opcion]()
        else:
            print("Opción no válida. ¡Intenta de nuevo!")
            input("\nPresiona Enter para continuar...")
            limpiar_consola()

if __name__ == '__main__':
    main()
