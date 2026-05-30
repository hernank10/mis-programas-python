# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios para construir Oraciones Simples en Inglés
# Diseñado para hablantes de español, enfocándose en estructuras básicas y errores comunes.
#
# Este programa de consola presenta ejercicios que abordan la construcción de
# oraciones afirmativas, negativas e interrogativas en diferentes tiempos verbales.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de oraciones simples en inglés
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Presente Simple - Afirmativa", "Traduce: 'Ella come manzanas.'", "She eats apples."),
        2: ("Presente Simple - Negativa", "Traduce: 'Nosotros no hablamos español.'", "We do not speak Spanish."),
        3: ("Presente Simple - Interrogativa", "Traduce: '¿Ellos trabajan los sábados?'", "Do they work on Saturdays?"),
        4: ("Verbo 'To Be' - Afirmativa", "Traduce: 'Él es un doctor.'", "He is a doctor."),
        5: ("Verbo 'To Be' - Negativa", "Traduce: 'Yo no estoy en casa.'", "I am not at home."),
        6: ("Verbo 'To Be' - Interrogativa", "Traduce: '¿Estás cansado?'", "Are you tired?"),
        7: ("Pasado Simple - Afirmativa", "Traduce: 'Ellos jugaron fútbol.'", "They played soccer."),
        8: ("Pasado Simple - Negativa", "Traduce: 'Ella no compró el coche.'", "She did not buy the car."),
        9: ("Pasado Simple - Interrogativa", "Traduce: '¿Ustedes vieron la película?'", "Did you see the movie?"),
        10: ("Presente Continuo - Afirmativa", "Traduce: 'Él está durmiendo.'", "He is sleeping."),
        11: ("Presente Continuo - Negativa", "Traduce: 'Nosotros no estamos comiendo.'", "We are not eating."),
        12: ("Presente Continuo - Interrogativa", "Traduce: '¿Estás escuchando música?'", "Are you listening to music?"),
        13: ("Futuro Simple ('Will')", "Traduce: 'Yo iré mañana.'", "I will go tomorrow."),
        14: ("Futuro Simple ('Will') - Negativa", "Traduce: 'Ella no vendrá a la fiesta.'", "She will not come to the party."),
        15: ("Futuro Simple ('Will') - Interrogativa", "Traduce: '¿Hablarás con él?'", "Will you talk to him?"),
        16: ("Presente Perfecto - Afirmativa", "Traduce: 'Yo he terminado mi tarea.'", "I have finished my homework."),
        17: ("Presente Perfecto - Negativa", "Traduce: 'Él no ha ido a casa.'", "He has not gone home."),
        18: ("Presente Perfecto - Interrogativa", "Traduce: '¿Alguna vez has estado en París?'", "Have you ever been to Paris?"),
        19: ("Pasado Continuo", "Traduce: 'Ella estaba estudiando cuando llamé.'", "She was studying when I called."),
        20: ("Pasado Continuo - Negativa", "Traduce: 'Ellos no estaban mirando televisión.'", "They were not watching TV."),
        21: ("Pasado Continuo - Interrogativa", "Traduce: '¿Estaba él trabajando ayer?'", "Was he working yesterday?"),
        22: ("Verbos Modales - 'Can'", "Traduce: 'Yo puedo nadar.'", "I can swim."),
        23: ("Verbos Modales - 'Can' - Negativa", "Traduce: 'Nosotros no podemos ir.'", "We cannot go."),
        24: ("Verbos Modales - 'Can' - Interrogativa", "Traduce: '¿Puedes ayudarme?'", "Can you help me?"),
        25: ("Futuro ('Going to')", "Traduce: 'Voy a estudiar esta noche.'", "I am going to study tonight."),
        26: ("Futuro ('Going to') - Negativa", "Traduce: 'Él no va a comprarlo.'", "He is not going to buy it."),
        27: ("Futuro ('Going to') - Interrogativa", "Traduce: '¿Van a venir a la cena?'", "Are they going to come to the dinner?"),
        28: ("Pasado Simple - Verbos Irregulares", "Traduce: 'Ella fue al cine.'", "She went to the cinema."),
        29: ("Pasado Simple - Verbos Irregulares (Negativa)", "Traduce: 'Nosotros no hicimos la cena.'", "We did not make dinner."),
        30: ("Pasado Simple - Verbos Irregulares (Interrogativa)", "Traduce: '¿Él te dio el libro?'", "Did he give you the book?"),
        31: ("Presente Simple - Sujeto", "Traduce: 'Los pájaros vuelan.'", "The birds fly."),
        32: ("Presente Simple - 'He/She/It'", "Traduce: 'La casa tiene un jardín.'", "The house has a garden."),
        33: ("Pasado Simple - 'He/She/It'", "Traduce: 'Ella escribió una carta.'", "She wrote a letter."),
        34: ("Verbo 'To Be' - Contracción", "Traduce: 'Nosotros somos amigos.'", "We're friends."),
        35: ("Verbo 'To Be' - Contracción Negativa", "Traduce: 'Ellos no son estudiantes.'", "They aren't students."),
        36: ("Verbos Modales - 'Should'", "Traduce: 'Deberías estudiar más.'", "You should study more."),
        37: ("Verbos Modales - 'Should' - Negativa", "Traduce: 'No deberías fumar.'", "You should not smoke."),
        38: ("Verbos Modales - 'Should' - Interrogativa", "Traduce: '¿Debería llamarlo?'", "Should I call him?"),
        39: ("Presente Simple - Afirmativa", "Traduce: 'El sol brilla.'", "The sun shines."),
        40: ("Pasado Simple - Negativa", "Traduce: 'Yo no corrí rápido.'", "I did not run fast."),
        41: ("Presente Continuo - Afirmativa", "Traduce: 'Ellos están jugando ajedrez.'", "They are playing chess."),
        42: ("Verbo 'To Be' - Interrogativa", "Traduce: '¿Es ella alta?'", "Is she tall?"),
        43: ("Futuro Simple - Afirmativa", "Traduce: 'Él trabajará mañana.'", "He will work tomorrow."),
        44: ("Presente Perfecto - Negativa", "Traduce: 'Ella no ha visto esa película.'", "She has not seen that movie."),
        45: ("Verbos Modales - 'Must'", "Traduce: 'Debes ir ahora.'", "You must go now."),
        46: ("Futuro ('Going to')", "Traduce: 'Vamos a comer pronto.'", "We are going to eat soon."),
        47: ("Pasado Simple - Interrogativa", "Traduce: '¿Comiste pizza?'", "Did you eat pizza?"),
        48: ("Presente Simple - Negativa", "Traduce: 'Él no vive aquí.'", "He does not live here."),
        49: ("Verbo 'To Be' - Negativa", "Traduce: 'Ellos no están felices.'", "They are not happy."),
        50: ("Verbos Modales - 'Could'", "Traduce: 'Yo podría ayudarte.'", "I could help you."),
        51: ("Futuro Simple - Negativa", "Traduce: 'No lloverá mañana.'", "It will not rain tomorrow."),
        52: ("Presente Perfecto - Afirmativa", "Traduce: 'Hemos estado aquí antes.'", "We have been here before."),
        53: ("Pasado Continuo - Interrogativa", "Traduce: '¿Estaba ella llorando?'", "Was she crying?"),
        54: ("Verbos Modales - 'May'", "Traduce: 'Puedo pasar?'", "May I come in?"),
        55: ("Presente Simple - Afirmativa", "Traduce: 'Los perros ladran.'", "Dogs bark."),
        56: ("Pasado Simple - Afirmativa", "Traduce: 'El avión aterrizó.'", "The plane landed."),
        57: ("Verbo 'To Be' - Afirmativa", "Traduce: 'Soy un estudiante.'", "I am a student."),
        58: ("Futuro ('Going to')", "Traduce: 'Va a ser un día hermoso.'", "It is going to be a beautiful day."),
        59: ("Presente Perfecto - Interrogativa", "Traduce: '¿Has visto mi teléfono?'", "Have you seen my phone?"),
        60: ("Verbos Modales - 'Might'", "Traduce: 'Podría llover.'", "It might rain."),
        61: ("Pasado Simple - Negativa", "Traduce: 'La puerta no se abrió.'", "The door did not open."),
        62: ("Presente Continuo - Negativa", "Traduce: 'Ella no está leyendo.'", "She is not reading."),
        63: ("Futuro Simple - Interrogativa", "Traduce: '¿Comerás con nosotros?'", "Will you eat with us?"),
        64: ("Pasado Continuo - Afirmativa", "Traduce: 'El gato estaba durmiendo.'", "The cat was sleeping."),
        65: ("Presente Simple - Interrogativa", "Traduce: '¿El canta?'", "Does he sing?"),
        66: ("Verbo 'To Be' - Contracción", "Traduce: 'Ella es mi hermana.'", "She's my sister."),
        67: ("Verbos Modales - 'Must' - Negativa", "Traduce: 'No debes decir eso.'", "You must not say that."),
        68: ("Presente Perfecto - Afirmativa", "Traduce: 'Él ha vivido aquí por 5 años.'", "He has lived here for 5 years."),
        69: ("Futuro ('Going to') - Interrogativa", "Traduce: '¿Va a llover?'", "Is it going to rain?"),
        70: ("Pasado Simple - Interrogativa", "Traduce: '¿Ella te llamó?'", "Did she call you?"),
        71: ("Verbos Modales - 'Should' - Interrogativa", "Traduce: '¿Qué debería hacer?'", "What should I do?"),
        72: ("Presente Simple - Afirmativa", "Traduce: 'El agua hierve a 100 grados Celsius.'", "Water boils at 100 degrees Celsius."),
        73: ("Pasado Continuo - Negativa", "Traduce: 'Yo no estaba pensando en eso.'", "I was not thinking about that."),
        74: ("Presente Perfecto - Negativa", "Traduce: 'Ellos no han regresado.'", "They have not returned."),
        75: ("Verbo 'To Be' - Interrogativa", "Traduce: '¿Son ustedes estudiantes?'", "Are you students?"),
        76: ("Futuro Simple - Negativa", "Traduce: 'No iremos mañana.'", "We will not go tomorrow."),
        77: ("Pasado Simple - Verbos Irregulares", "Traduce: 'Nosotros comimos en el restaurante.'", "We ate at the restaurant."),
        78: ("Presente Continuo - Interrogativa", "Traduce: '¿Por qué estás sonriendo?'", "Why are you smiling?"),
        79: ("Verbos Modales - 'Can' - Negativa", "Traduce: 'Ella no puede correr rápido.'", "She cannot run fast."),
        80: ("Verbo 'To Be' - Afirmativa", "Traduce: 'El cielo es azul.'", "The sky is blue."),
        81: ("Presente Simple - Negativa", "Traduce: 'Nosotros no vivimos en la ciudad.'", "We do not live in the city."),
        82: ("Futuro ('Going to')", "Traduce: 'Va a ser un día soleado.'", "It is going to be a sunny day."),
        83: ("Pasado Simple - Interrogativa", "Traduce: '¿Él fue a la fiesta?'", "Did he go to the party?"),
        84: ("Presente Perfecto - Afirmativa", "Traduce: 'Yo he leído ese libro.'", "I have read that book."),
        85: ("Verbos Modales - 'Could'", "Traduce: 'El podría estar en casa.'", "He could be at home."),
        86: ("Pasado Continuo - Afirmativa", "Traduce: 'Estábamos caminando en el parque.'", "We were walking in the park."),
        87: ("Presente Continuo - Negativa", "Traduce: 'Ella no está hablando.'", "She is not talking."),
        88: ("Verbo 'To Be' - Interrogativa", "Traduce: '¿Dónde está el baño?'", "Where is the bathroom?"),
        89: ("Futuro Simple - Afirmativa", "Traduce: 'Ellos lo sabrán pronto.'", "They will know it soon."),
        90: ("Presente Simple - Afirmativa", "Traduce: 'Yo tengo dos hermanos.'", "I have two brothers."),
        91: ("Pasado Simple - Negativa", "Traduce: 'El no me llamó.'", "He did not call me."),
        92: ("Verbos Modales - 'Should'", "Traduce: 'Deberías descansar.'", "You should rest."),
        93: ("Presente Perfecto - Interrogativa", "Traduce: '¿Ha llovido hoy?'", "Has it rained today?"),
        94: ("Pasado Continuo - Interrogativa", "Traduce: '¿Qué estabas haciendo?'", "What were you doing?"),
        95: ("Futuro ('Going to') - Negativa", "Traduce: 'No vamos a comprar un coche nuevo.'", "We are not going to buy a new car."),
        96: ("Verbo 'To Be' - Afirmativa", "Traduce: 'Mi coche es rojo.'", "My car is red."),
        97: ("Presente Simple - Interrogativa", "Traduce: '¿Vives en la ciudad?'", "Do you live in the city?"),
        98: ("Futuro Simple - Interrogativa", "Traduce: '¿Ellos vendrán?'", "Will they come?"),
        99: ("Pasado Simple - Verbos Irregulares", "Traduce: 'Ella se sintió enferma.'", "She felt sick."),
        100: ("Repaso Final", "Traduce: 'Él no es un héroe.'", "He is not a hero."),
    }

    print("¡Bienvenido al reto de Oraciones Simples en Inglés!")
    print("-------------------------------------------------------------")
    print("Responda con la traducción correcta o escriba 'salir' para terminar.")

    while True:
        try:
            exercise_number = random.choice(list(exercises.keys()))
            title, task, correct_answer = exercises[exercise_number]

            print(f"\n[Ejercicio {exercise_number}: {title}]")
            print(task)

            user_response = input("Tu respuesta: ").strip()

            if user_response.lower() == 'salir':
                print("¡Gracias por practicar! ¡Hasta la próxima!")
                break
            
            clean_user_response = user_response.strip(".").strip().lower()
            clean_correct_answer = correct_answer.strip(".").strip().lower()

            # For questions, allow both with and without the question mark at the end
            if clean_user_response == clean_correct_answer or (clean_user_response + '?') == clean_correct_answer:
                print("¡Correcto! ¡Excelente trabajo!")
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
