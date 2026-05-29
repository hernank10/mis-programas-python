# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios de Cómo Hacer Preguntas en Inglés
# Diseñado para hablantes de español.
#
# Este programa de consola presenta ejercicios que abordan la estructura, verbos auxiliares,
# pronombres interrogativos y errores comunes al formular preguntas en inglés.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios sobre preguntas en inglés
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Preguntas con 'Do'", "La forma correcta de preguntar '¿Te gusta el café?' es: (a) Do you like coffee?, (b) You like coffee?, (c) Are you like coffee?", "a"),
        2: ("'WH' Questions", "Para preguntar '¿Qué estás haciendo?', la estructura es: (a) What are you doing?, (b) What you are doing?, (c) Are you doing what?", "a"),
        3: ("Pasado Simple", "La forma correcta de preguntar '¿Comiste?' es: (a) Did you eat?, (b) Do you ate?, (c) You did eat?", "a"),
        4: ("Verbo 'To Be'", "Para preguntar '¿Estás listo?', la estructura es: (a) Do you are ready?, (b) Are you ready?, (c) You are ready?", "b"),
        5: ("Errores Comunes", "La traducción literal de '¿Tienes frío?' es incorrecta. La forma correcta es: (a) Do you have cold?, (b) Are you cold?, (c) You have cold?", "b"),
        6: ("'WH' Questions", "Para preguntar la razón, usamos la palabra: (a) What, (b) Where, (c) Why.", "c"),
        7: ("Preguntas con 'Does'", "La pregunta correcta para '¿Él habla español?' es: (a) Does he speak Spanish?, (b) Do he speaks Spanish?, (c) He speak Spanish?", "a"),
        8: ("Verbos Modales", "Para preguntar '¿Puedes ayudarme?', la forma correcta es: (a) Can you help me?, (b) Do you can help me?, (c) You can help me?", "a"),
        9: ("Estructura de la Pregunta", "En la pregunta 'What is your name?', 'is' es un verbo: (a) principal, (b) auxiliar, (c) modal.", "b"),
        10: ("'WH' Questions", "Para preguntar por una persona, usamos: (a) Where, (b) When, (c) Who.", "c"),
        11: ("Preguntas con 'Did'", "Completa la pregunta: '... you go to the party last night?' (a) Do, (b) Did, (c) Are", "b"),
        12: ("'WH' Questions", "Para preguntar por un lugar, usamos: (a) Who, (b) What, (c) Where.", "c"),
        13: ("Preguntas Indirectas", "¿Cuál es la forma correcta de preguntar 'I wonder what time it is.'? (a) I wonder what time is it?, (b) I wonder what time it is., (c) I wonder is it what time.", "b"),
        14: ("'Question Tags'", "La 'question tag' para 'You are happy,' es: (a) are you?, (b) aren't you?, (c) don't you?", "b"),
        15: ("Estructura del Presente Continuo", "La pregunta 'Are they watching TV?' tiene la estructura: (a) Sujeto + Verbo + ..., (b) Verbo Auxiliar + Sujeto + Verbo principal + ..., (c) Verbo principal + Sujeto + ...", "b"),
        16: ("Futuro Simple", "Para preguntar '¿Irás a la fiesta?', usamos: (a) Will you go to the party?, (b) Do you go to the party?, (c) Are you going to the party?", "a"),
        17: ("Presente Perfecto", "La pregunta '¿Has estado en Italia?' se traduce como: (a) Did you be in Italy?, (b) Have you been to Italy?, (c) Do you have been to Italy?", "b"),
        18: ("'How' Questions", "Para preguntar '¿Cómo te sientes?', usamos: (a) What do you feel?, (b) How do you feel?, (c) How you feel?", "b"),
        19: ("Preguntas de Objeto", "En 'What did you buy?', 'what' es el: (a) sujeto, (b) objeto directo, (c) verbo auxiliar.", "b"),
        20: ("Preguntas de Sujeto", "En 'Who bought the car?', 'who' es el: (a) objeto, (b) verbo, (c) sujeto.", "c"),
        21: ("Verbos Modales", "Para preguntar '¿Debería estudiar más?', la forma correcta es: (a) Should I study more?, (b) Do I should study more?, (c) I should study more?", "a"),
        22: ("'WH' Questions", "¿Qué palabra usamos para preguntar por una cosa o idea? (a) Who, (b) What, (c) Where.", "b"),
        23: ("Pasado Continuo", "La forma correcta de preguntar '¿Estabas durmiendo?' es: (a) Did you sleep?, (b) Were you sleeping?, (c) You were sleeping?", "b"),
        24: ("Presente Simple vs. Continuo", "La pregunta '¿Juegas fútbol?' se traduce como: (a) Are you playing soccer?, (b) Do you play soccer?, (c) You play soccer?", "b"),
        25: ("'Question Tags'", "La 'question tag' para 'He can swim,' es: (a) can't he?, (b) can he?, (c) does he?", "a"),
        26: ("Preposiciones en Preguntas", "Para preguntar '¿Con quién fuiste?', la preposición va: (a) al principio (With who...), (b) al final (...with), (c) en el medio.", "b"),
        27: ("Preguntas con 'Have'", "La pregunta '¿Tienes un lápiz?' es: (a) Do you have a pencil?, (b) Are you having a pencil?, (c) You have a pencil?", "a"),
        28: ("'How many' vs. 'How much'", "Para preguntar por un sustantivo contable (e.g. 'libros'), usamos: (a) How much, (b) How many, (c) How.", "b"),
        29: ("'How many' vs. 'How much'", "Para preguntar por un sustantivo incontable (e.g. 'agua'), usamos: (a) How much, (b) How many, (c) How.", "a"),
        30: ("Oración Interrogativa", "Una pregunta en inglés siempre termina con: (a) un punto, (b) una coma, (c) un signo de interrogación.", "c"),
        31: ("Verbo 'To Be'", "La forma de 'to be' para el sujeto 'she' es: (a) are, (b) is, (c) am.", "b"),
        32: ("Pasado Simple de 'To Be'", "La pregunta '¿Ella estaba en casa?' es: (a) Did she be at home?, (b) Was she at home?, (c) Is she at home?", "b"),
        33: ("'Question Tags'", "La 'question tag' para 'They don't like it,' es: (a) do they?, (b) don't they?, (c) are they?", "a"),
        34: ("'What' vs. 'Which'", "Para preguntar '¿Cuál es tu color favorito?', usamos: (a) What is your favorite color?, (b) Which is your favorite color?, (c) What is your most favorite color?", "a"),
        35: ("'How long'", "Para preguntar por la duración de un evento, usamos: (a) How far, (b) How long, (c) How much.", "b"),
        36: ("Preguntas de Sujeto", "En 'Who lives here?', no se usa el verbo auxiliar 'do'. (Verdadero/Falso)", "verdadero"),
        37: ("Voz Pasiva", "La forma correcta de preguntar '¿Fue escrita la carta?' es: (a) Was the letter written?, (b) Did the letter write?, (c) The letter was written?", "a"),
        38: ("Preguntas con 'Where'", "Para preguntar '¿Dónde viven tus padres?', usamos: (a) Where live your parents?, (b) Where do your parents live?, (c) Where your parents live?", "b"),
        39: ("'WH' Questions", "Para preguntar por un momento específico en el tiempo, usamos: (a) Where, (b) When, (c) What.", "b"),
        40: ("Verbos Modales", "¿Cómo se pregunta '¿Debería ir?'?: (a) Should I go?, (b) Do I should go?, (c) I should go?", "a"),
        41: ("Presente Perfecto Continuo", "La pregunta '¿Cuánto tiempo has estado estudiando?' es: (a) How long have you been studying?, (b) How long do you study?, (c) How long are you studying?", "a"),
        42: ("Estructura de la Pregunta", "En una pregunta 'WH', el orden es: (a) WH + Sujeto + Verbo..., (b) WH + Verbo Auxiliar + Sujeto + Verbo..., (c) Sujeto + Verbo + WH...", "b"),
        43: ("'Why' vs. 'What for'", "Para preguntar '¿Para qué sirve esto?', la forma común es: (a) Why is this for?, (b) What is this for?, (c) Why this is for?", "b"),
        44: ("Verbo 'To Be'", "Para preguntar '¿Eres un doctor?', la forma correcta es: (a) Are you a doctor?, (b) Do you are a doctor?, (c) You are a doctor?", "a"),
        45: ("Estructura del Presente Simple", "La estructura de la pregunta es: (a) Verbo + Sujeto, (b) Sujeto + Verbo, (c) Auxiliar + Sujeto + Verbo", "c"),
        46: ("Pasado Simple", "La pregunta '¿Llegaron tarde?' se traduce como: (a) They arrived late?, (b) Did they arrive late?, (c) Do they arrived late?", "b"),
        47: ("Verbos Modales", "Para preguntar '¿Podrías abrir la ventana?', la forma más cortés es: (a) Can you open..., (b) Could you open..., (c) Do you open...", "b"),
        48: ("'Question Tags'", "La 'question tag' para 'It's cold,' es: (a) is it?, (b) isn't it?, (c) don't it?", "b"),
        49: ("'How' Questions", "Para preguntar por la manera o el modo, usamos: (a) How, (b) What, (c) Why.", "a"),
        50: ("Preguntas de Objeto", "En 'What did he see?', 'what' es el: (a) sujeto, (b) objeto, (c) verbo.", "b"),
        51: ("'Where'", "La pregunta '¿Dónde está la biblioteca?' es: (a) Where is the library?, (b) Where the library is?, (c) Is the library where?", "a"),
        52: ("'When'", "La pregunta '¿Cuándo empieza la clase?' es: (a) When the class begins?, (b) When does the class begin?, (c) When begins the class?", "b"),
        53: ("Verbos Modales", "Para preguntar '¿Debo hacerlo?', la forma correcta es: (a) Should I do it?, (b) Do I should do it?, (c) I should do it?", "a"),
        54: ("Preguntas Indirectas", "¿Es correcta la pregunta 'Do you know where is the post office?'? (a) Sí, (b) No.", "b"),
        55: ("'Question Tags'", "La 'question tag' para 'They will come,' es: (a) will they?, (b) won't they?, (c) don't they?", "b"),
        56: ("Futuro Simple", "Para preguntar '¿Cuándo me llamarás?', la estructura es: (a) When you will call me?, (b) When will you call me?, (c) Will you call me when?", "b"),
        57: ("Presente Perfecto", "La pregunta '¿Has terminado ya?' se traduce como: (a) Have you finished yet?, (b) Did you finish yet?, (c) Do you have finished yet?", "a"),
        58: ("'Who' vs. 'Whom'", "En la mayoría de los casos, 'whom' se reemplaza por 'who'. (Verdadero/Falso)", "verdadero"),
        59: ("Estructura de la Pregunta", "En la pregunta 'Is the food hot?', 'the food' es el: (a) sujeto, (b) verbo, (c) objeto.", "a"),
        60: ("Verbos Irregulares", "La forma pasada del verbo 'go' en una pregunta es: (a) went, (b) gone, (c) go.", "c"),
        61: ("Estructura", "La pregunta 'What time is it?' es un ejemplo de: (a) inversión de sujeto y verbo, (b) pregunta con verbo auxiliar, (c) pregunta directa.", "a"),
        62: ("Presente Continuo", "La pregunta '¿Está lloviendo?' se traduce como: (a) Does it rain?, (b) Is it raining?, (c) It is raining?", "b"),
        63: ("Verbos Modales", "Para preguntar '¿Podrías pasarme la sal?', es más educado que 'Can you...'. (Verdadero/Falso)", "verdadero"),
        64: ("Preguntas con 'How'", "Para preguntar por un precio, usamos: (a) How much is it?, (b) How many is it?, (c) What is the price?", "a"),
        65: ("'Question Tags'", "La 'question tag' para 'You can't be serious,' es: (a) can you?, (b) can't you?, (c) do you?", "a"),
        66: ("Estructura", "En la pregunta 'When did you arrive?', 'you' es el: (a) verbo, (b) sujeto, (c) objeto.", "b"),
        67: ("Pasado Simple", "¿Qué pregunta usa el verbo auxiliar 'did' de manera incorrecta? (a) Did she speak?, (b) Did she spoke?, (c) Did you go?", "b"),
        68: ("Futuro 'Going to'", "La pregunta '¿Vas a estudiar esta noche?' se traduce como: (a) Are you going to study tonight?, (b) Do you go to study tonight?, (c) You are going to study tonight?", "a"),
        69: ("'Question Tags'", "Una 'question tag' para una oración afirmativa es generalmente: (a) afirmativa, (b) negativa, (c) neutra.", "b"),
        70: ("'Question Tags'", "Una 'question tag' para una oración negativa es generalmente: (a) afirmativa, (b) negativa, (c) neutra.", "a"),
        71: ("Estructura", "En 'Where did they find it?', 'find' es el verbo: (a) principal, (b) auxiliar, (c) modal.", "a"),
        72: ("Presente Perfecto", "La pregunta '¿Ha ido él al supermercado?' es: (a) Has he gone to the supermarket?, (b) Does he go to the supermarket?, (c) Is he gone to the supermarket?", "a"),
        73: ("Verbos Modales", "La forma correcta de preguntar '¿Deberíamos empezar?' es: (a) We should start?, (b) Do we should start?, (c) Should we start?", "c"),
        74: ("'What' vs. 'What kind of'", "Para preguntar '¿Qué tipo de música te gusta?', usamos: (a) What kind of music do you like?, (b) What music do you like?, (c) What of music do you like?", "a"),
        75: ("Preguntas con Verbos Modales", "En una pregunta con un verbo modal, ¿el verbo principal va en su forma base? (Verdadero/Falso)", "verdadero"),
        76: ("Estructura", "La pregunta 'Who is calling?' es una pregunta de: (a) objeto, (b) sujeto.", "b"),
        77: ("'WH' Questions", "Para preguntar por la posesión de algo, usamos: (a) Who, (b) Whom, (c) Whose.", "c"),
        78: ("Pasado Simple", "La pregunta '¿Viste la película?' es: (a) Did you see the movie?, (b) You saw the movie?, (c) Did you saw the movie?", "a"),
        79: ("Preguntas Indirectas", "La pregunta 'Do you know where the hotel is?' es: (a) directa, (b) indirecta.", "b"),
        80: ("Verbos Auxiliares", "El verbo 'to be' en preguntas no necesita un verbo auxiliar adicional. (Verdadero/Falso)", "verdadero"),
        81: ("'Question Tags'", "La 'question tag' para 'You work here,' es: (a) you don't?, (b) don't you?, (c) do you?", "b"),
        82: ("Futuro Simple", "Para preguntar '¿Vendrá mañana?', la forma correcta es: (a) Will she come tomorrow?, (b) Will she comes tomorrow?, (c) She will come tomorrow?", "a"),
        83: ("Presente Perfecto", "En la pregunta 'Have you ever been to Paris?', 'ever' significa: (a) alguna vez, (b) siempre, (c) nunca.", "a"),
        84: ("'How' Questions", "Para preguntar por la frecuencia, usamos: (a) How many, (b) How much, (c) How often.", "c"),
        85: ("Estructura", "En la pregunta 'Did it rain yesterday?', el verbo principal es: (a) did, (b) rain, (c) yesterday.", "b"),
        86: ("Preguntas de Sujeto", "En 'Who made this?', 'who' actúa como el: (a) objeto, (b) verbo, (c) sujeto.", "c"),
        87: ("'What' vs. 'Which'", "Para preguntar '¿Cuál de estos dos libros prefieres?', usamos: (a) What of these books?, (b) Which of these two books..., (c) What is your preference of these two books?", "b"),
        88: ("Futuro Continuo", "La pregunta '¿Estarás trabajando mañana a esta hora?' es: (a) Will you be working at this time tomorrow?, (b) Are you working tomorrow?, (c) You will be working?", "a"),
        89: ("Preguntas Indirectas", "La pregunta 'Could you tell me what your name is?' es más formal que 'What is your name?'. (Verdadero/Falso)", "verdadero"),
        90: ("'Question Tags'", "La 'question tag' para 'She's not coming,' es: (a) isn't she?, (b) is she?, (c) does she?", "b"),
        91: ("Verbos Modales", "Para preguntar por una posibilidad, usamos: (a) can, (b) could, (c) may.", "c"),
        92: ("Estructura", "En la pregunta 'Why did you call me?', 'call' está en: (a) pasado, (b) infinitivo sin 'to'.", "b"),
        93: ("Preguntas con 'Have'", "La pregunta '¿Tienes un coche?' es: (a) Do you have a car?, (b) Are you having a car?, (c) You have a car?", "a"),
        94: ("Pasado Continuo", "La pregunta '¿Estabas estudiando cuando te llamé?' es: (a) Were you studying when I called you?, (b) Did you study when I called?, (c) You were studying...?", "a"),
        95: ("'How' Questions", "Para preguntar por la distancia, usamos: (a) How long, (b) How far, (c) How much.", "b"),
        96: ("Estructura", "En la pregunta 'Is he a student?', 'he' es el: (a) verbo, (b) objeto, (c) sujeto.", "c"),
        97: ("Verbos Auxiliares", "En la mayoría de las preguntas en presente simple y pasado simple se usa un verbo auxiliar. (Verdadero/Falso)", "verdadero"),
        98: ("Preguntas Indirectas", "En 'I don't know what time it is', la cláusula interrogativa 'what time it is' tiene el orden de una oración: (a) afirmativa, (b) interrogativa.", "a"),
        99: ("Voz Pasiva", "La forma correcta de preguntar '¿La casa fue vendida?' es: (a) Was the house sold?, (b) Did the house sell?, (c) The house was sold?", "a"),
        100: ("Repaso Final", "¿Qué palabra es fundamental para iniciar una pregunta en inglés para un hablante de español? (a) Do/Does/Did/Auxiliares, (b) Verbo principal, (c) Sujeto.", "a"),
    }

    print("¡Bienvenido al reto de Preguntas en Inglés!")
    print("-------------------------------------------------------------")
    print("Responda las preguntas o introduzca 'salir' para terminar.")

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
