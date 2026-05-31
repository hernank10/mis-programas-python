# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Redacción y Periodismo
# Inspirado en las obras del Instituto Caro y Cuervo.
#
# Este programa de consola presenta ejercicios sobre los conceptos fundamentales de la
# redacción y el periodismo, incluyendo géneros, estilo, ética y estructura.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de redacción y periodismo
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Generalidades", "La estructura más común en la noticia, que organiza la información de lo más a lo menos relevante, se conoce como: (a) pirámide invertida, (b) relato lineal, (c) círculo temático.", "a"),
        2: ("Géneros", "Un texto que presenta una opinión sobre un tema actual, firmado por un autor, es un: (a) reportaje, (b) artículo de opinión, (c) crónica.", "b"),
        3: ("Redacción", "La cualidad del estilo que se refiere a usar solo las palabras necesarias para expresar una idea es: (a) claridad, (b) concisión, (c) precisión.", "b"),
        4: ("Estilo", "El uso de oraciones cortas y un lenguaje directo es característico del estilo: (a) literario, (b) periodístico, (c) académico.", "b"),
        5: ("Titulación", "Un titular efectivo debe ser informativo y: (a) largo, (b) ambiguo, (c) atractivo.", "c"),
        6: ("Ética", "El principio de 'verificación de la información' implica que un periodista debe: (a) confiar en una sola fuente, (b) contrastar datos, (c) especular.", "b"),
        7: ("Fuentes", "¿Qué tipo de fuente es una entrevista con un experto? (a) fuente primaria, (b) fuente secundaria, (c) fuente indirecta.", "a"),
        8: ("Noticia", "¿El 'lead' o 'cuerpo' de una noticia contiene la información más relevante? (Sí/No)", "sí"),
        9: ("Reportaje", "Un género periodístico que profundiza en un tema y requiere investigación extensa es el: (a) reportaje, (b) editorial, (c) suelto.", "a"),
        10: ("Crónica", "La 'crónica' es un género que mezcla información con: (a) ficción, (b) opinión del autor, (c) datos estadísticos.", "b"),
        11: ("Entrevista", "Una entrevista en la que el periodista hace preguntas para obtener información es una entrevista: (a) de semblanza, (b) informativa, (c) de opinión.", "b"),
        12: ("Ortografía", "El uso de la coma en el periodismo es fundamental para: (a) separar ideas, (b) decorar el texto, (c) hacer pausas dramáticas.", "a"),
        13: ("Gramática", "El 'sujeto tácito' es aquel que no está expresado explícitamente pero se entiende. (Verdadero/Falso)", "verdadero"),
        14: ("Estilo", "El uso de metáforas complejas en la noticia es un principio de concisión. (Verdadero/Falso)", "falso"),
        15: ("Generalidades", "El 'cuerpo de la noticia' se encarga de desarrollar la información del lead. (Verdadero/Falso)", "verdadero"),
        16: ("Ética", "El 'plagio' es la acción de usar ideas de otro sin dar crédito. (Verdadero/Falso)", "verdadero"),
        17: ("Géneros", "Una reseña es un tipo de texto que busca dar una opinión sobre una obra. (Verdadero/Falso)", "verdadero"),
        18: ("Redacción", "¿Es la claridad una cualidad esencial de la redacción periodística? (Sí/No)", "sí"),
        19: ("Titulación", "Un 'antetítulo' es una frase corta que complementa el titular. (Verdadero/Falso)", "verdadero"),
        20: ("Fuentes", "Las fuentes 'directas' son personas que presenciaron un evento. (Verdadero/Falso)", "verdadero"),
        21: ("Noticia", "El 'quién', 'qué', 'cuándo', 'dónde' y 'por qué' son las 5W y 1H de la noticia. (Verdadero/Falso)", "verdadero"),
        22: ("Reportaje", "El reportaje 'objetivo' es aquel en el que el autor no muestra su opinión. (Verdadero/Falso)", "verdadero"),
        23: ("Entrevista", "La 'entrevista de perfil' busca conocer la personalidad de un entrevistado. (Verdadero/Falso)", "verdadero"),
        24: ("Ortografía", "El uso incorrecto de las tildes puede cambiar el significado de una palabra. (Verdadero/Falso)", "verdadero"),
        25: ("Géneros", "Un 'suelto' es un texto de opinión breve y sin firma. (Verdadero/Falso)", "falso"),
        26: ("Ética", "La 'objetividad' en el periodismo es un principio que exige presentar los hechos sin sesgos personales. (Verdadero/Falso)", "verdadero"),
        27: ("Redacción", "La 'precisión' implica usar las palabras adecuadas para expresar un concepto. (Verdadero/Falso)", "verdadero"),
        28: ("Fuentes", "Una 'fuente anónima' es una fuente que no se puede revelar. (Verdadero/Falso)", "verdadero"),
        29: ("Generalidades", "¿El 'sumario' de una noticia es un párrafo que resume la información más importante? (Sí/No)", "sí"),
        30: ("Géneros", "El 'editorial' es la opinión del periódico sobre un tema, no de un autor. (Verdadero/Falso)", "verdadero"),
        31: ("Redacción", "La 'fluidez' en la redacción se logra con oraciones complejas y largas. (Verdadero/Falso)", "falso"),
        32: ("Noticia", "Los 'detalles secundarios' en una noticia se encuentran en el lead. (Verdadero/Falso)", "falso"),
        33: ("Ética", "El principio de 'autocensura' es una práctica ética en el periodismo. (Verdadero/Falso)", "falso"),
        34: ("Fuentes", "Las 'fuentes primarias' son documentos originales o testigos directos. (Verdadero/Falso)", "verdadero"),
        35: ("Generalidades", "¿Es la 'jerarquía de la información' un principio de la pirámide invertida? (Sí/No)", "sí"),
        36: ("Géneros", "Un 'reportaje de investigación' requiere meses o años de trabajo. (Verdadero/Falso)", "verdadero"),
        37: ("Redacción", "El uso de la 'voz activa' hace el texto más dinámico y claro. (Verdadero/Falso)", "verdadero"),
        38: ("Titulación", "El 'subtítulo' o 'bajante' complementa el titular y el antetítulo. (Verdadero/Falso)", "verdadero"),
        39: ("Ética", "La 'imparcialidad' se refiere a tomar partido por una de las partes de una historia. (Verdadero/Falso)", "falso"),
        40: ("Fuentes", "¿Las 'fuentes secundarias' son documentos que analizan fuentes primarias? (Sí/No)", "sí"),
        41: ("Generalidades", "La 'credibilidad' en el periodismo se construye con la confianza del público. (Verdadero/Falso)", "verdadero"),
        42: ("Géneros", "Una 'crítica' es un género que evalúa una obra de arte o un evento. (Verdadero/Falso)", "verdadero"),
        43: ("Redacción", "El uso de la 'voz pasiva' es recomendado para la redacción periodística. (Verdadero/Falso)", "falso"),
        44: ("Noticia", "El 'lead' de una noticia debe responder a las 5W y 1H. (Verdadero/Falso)", "verdadero"),
        45: ("Ética", "Un periodista debe revelar su 'conflicto de interés' al reportar. (Verdadero/Falso)", "verdadero"),
        46: ("Fuentes", "Las fuentes 'indirectas' son aquellas a las que se accede a través de otras personas. (Verdadero/Falso)", "verdadero"),
        47: ("Generalidades", "La 'objetividad' absoluta es un ideal en el periodismo. (Verdadero/Falso)", "verdadero"),
        48: ("Géneros", "La 'entrevista de opinión' busca conocer las ideas y posturas de un personaje. (Verdadero/Falso)", "verdadero"),
        49: ("Redacción", "La 'gramática' es irrelevante para la redacción periodística. (Verdadero/Falso)", "falso"),
        50: ("Titulación", "¿Un titular puede ser una pregunta? (Sí/No)", "sí"),
        51: ("Ética", "El 'derecho a la rectificación' le permite a una persona corregir una información falsa. (Verdadero/Falso)", "verdadero"),
        52: ("Fuentes", "Un 'experto' es una fuente de información de alto valor. (Verdadero/Falso)", "verdadero"),
        53: ("Generalidades", "El 'estilo' en el periodismo es una marca personal de cada periodista. (Verdadero/Falso)", "verdadero"),
        54: ("Géneros", "Un 'artículo de fondo' es un género que profundiza en un tema sin la inmediatez de la noticia. (Verdadero/Falso)", "verdadero"),
        55: ("Redacción", "El uso de 'clichés' o frases hechas en el periodismo es un signo de originalidad. (Verdadero/Falso)", "falso"),
        56: ("Noticia", "La 'pirámide invertida' es una forma de organizar los hechos de manera cronológica. (Verdadero/Falso)", "falso"),
        57: ("Ética", "Un 'código de ética' periodística establece las normas de conducta profesional. (Verdadero/Falso)", "verdadero"),
        58: ("Fuentes", "¿Una 'conferencia de prensa' es una fuente de información? (Sí/No)", "sí"),
        59: ("Generalidades", "La 'precisión' en la redacción se logra con un vocabulario limitado. (Verdadero/Falso)", "falso"),
        60: ("Géneros", "Un 'reportaje' siempre se publica en formato impreso. (Verdadero/Falso)", "falso"),
        61: ("Redacción", "El uso de conectores lógicos es vital para la 'cohesión' del texto. (Verdadero/Falso)", "verdadero"),
        62: ("Titulación", "¿Un titular puede omitir el sujeto de la oración? (Sí/No)", "sí"),
        63: ("Ética", "La 'filtración' de información confidencial es siempre una acción no ética. (Verdadero/Falso)", "falso"),
        64: ("Fuentes", "Las 'fuentes documentales' son archivos, informes o libros. (Verdadero/Falso)", "verdadero"),
        65: ("Generalidades", "El 'género periodístico' se refiere a la forma en que se presenta la información. (Verdadero/Falso)", "verdadero"),
        66: ("Géneros", "El 'perfil' es un tipo de reportaje que se enfoca en la biografía de un personaje. (Verdadero/Falso)", "verdadero"),
        67: ("Redacción", "La 'claridad' se logra evitando la jerga técnica. (Verdadero/Falso)", "verdadero"),
        68: ("Noticia", "¿El 'antetítulo' de una noticia es la frase que va después del titular? (Sí/No)", "no"),
        69: ("Ética", "La 'responsabilidad social' del periodista es informar a la sociedad. (Verdadero/Falso)", "verdadero"),
        70: ("Fuentes", "La 'diversidad de fuentes' es un principio ético. (Verdadero/Falso)", "verdadero"),
        71: ("Generalidades", "La 'credibilidad' de un medio se ve afectada por los errores de ortografía. (Verdadero/Falso)", "verdadero"),
        72: ("Géneros", "Un 'micro-relato' es un género periodístico. (Verdadero/Falso)", "falso"),
        73: ("Redacción", "El 'estilo directo' se usa para citar a alguien textualmente. (Verdadero/Falso)", "verdadero"),
        74: ("Titulación", "El 'titular de sumario' presenta un resumen de la información. (Verdadero/Falso)", "verdadero"),
        75: ("Ética", "La 'privacidad' de las personas debe ser respetada por los periodistas. (Verdadero/Falso)", "verdadero"),
        76: ("Fuentes", "Un 'testigo ocular' es una fuente primaria. (Verdadero/Falso)", "verdadero"),
        77: ("Generalidades", "El 'reportero' es la persona que se encarga de la edición del texto. (Verdadero/Falso)", "falso"),
        78: ("Géneros", "El 'ensayo periodístico' es un género de opinión y análisis. (Verdadero/Falso)", "verdadero"),
        79: ("Redacción", "¿Los 'verbos de acción' hacen más dinámico el texto? (Sí/No)", "sí"),
        80: ("Titulación", "Un 'titular emotivo' puede ser usado en la noticia. (Verdadero/Falso)", "falso"),
        81: ("Ética", "El 'derecho a la información' es un derecho fundamental del ciudadano. (Verdadero/Falso)", "verdadero"),
        82: ("Fuentes", "El uso de una 'fuente falsa' es una práctica común en el periodismo. (Verdadero/Falso)", "falso"),
        83: ("Generalidades", "El 'periódico' es el único medio de comunicación masiva. (Verdadero/Falso)", "falso"),
        84: ("Géneros", "La 'entrevista de semblanza' es un género de la radio. (Verdadero/Falso)", "falso"),
        85: ("Redacción", "La 'puntuación' es vital para la claridad del texto. (Verdadero/Falso)", "verdadero"),
        86: ("Titulación", "El 'titular de sorpresa' es aquel que no revela toda la información. (Verdadero/Falso)", "verdadero"),
        87: ("Ética", "La 'ética periodística' es un conjunto de reglas universales. (Verdadero/Falso)", "verdadero"),
        88: ("Fuentes", "El 'secreto profesional' es el derecho del periodista a no revelar sus fuentes. (Verdadero/Falso)", "verdadero"),
        89: ("Generalidades", "El 'editor' es el responsable final del contenido de la publicación. (Verdadero/Falso)", "verdadero"),
        90: ("Géneros", "La 'columna' es un género de opinión que tiene una periodicidad fija. (Verdadero/Falso)", "verdadero"),
        91: ("Redacción", "El 'estilo indirecto' se usa para parafrasear lo que alguien dijo. (Verdadero/Falso)", "verdadero"),
        92: ("Titulación", "¿Un titular de 'llamada' es aquel que invita a leer el texto? (Sí/No)", "sí"),
        93: ("Ética", "La 'neutralidad' es un principio ético que exige al periodista no tomar partido. (Verdadero/Falso)", "verdadero"),
        94: ("Fuentes", "Un 'reporte de prensa' es una fuente primaria. (Verdadero/Falso)", "falso"),
        95: ("Generalidades", "La 'línea editorial' de un medio es la postura que mantiene sobre los temas. (Verdadero/Falso)", "verdadero"),
        96: ("Géneros", "El 'género narrativo' se usa en el periodismo para contar historias. (Verdadero/Falso)", "verdadero"),
        97: ("Redacción", "El 'adjetivo' debe usarse con moderación en el periodismo. (Verdadero/Falso)", "verdadero"),
        98: ("Titulación", "El 'titular de cita' reproduce textualmente una frase importante. (Verdadero/Falso)", "verdadero"),
        99: ("Ética", "La 'honestidad' es un valor fundamental en el periodismo. (Verdadero/Falso)", "verdadero"),
        100: ("Generalidades", "El 'periodismo' es la actividad de buscar, procesar y difundir información. (Verdadero/Falso)", "verdadero"),
    }

    print("¡Bienvenido al reto de Redacción y Periodismo!")
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
