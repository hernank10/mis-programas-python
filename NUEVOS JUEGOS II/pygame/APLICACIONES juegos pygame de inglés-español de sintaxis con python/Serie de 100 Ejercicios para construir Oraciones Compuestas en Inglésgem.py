# -*- coding: utf-8 -*-
#
# Serie de 100 Ejercicios para construir Oraciones Compuestas en Inglés
# Diseñado para hablantes de español.
#
# Este programa de consola presenta ejercicios sobre el uso de conjunciones
# coordinantes, subordinantes y pronombres relativos.

import random

def main():
    """
    Función principal del programa.
    Contiene el diccionario con los 100 ejercicios de oraciones compuestas en inglés
    y el bucle principal para presentarlos al usuario.
    """
    exercises = {
        1: ("Conjunciones Coordinantes", "Traduce: 'Me gusta el café, pero a ella le gusta el té.'", "I like coffee, but she likes tea."),
        2: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Él está feliz porque pasó el examen.'", "He is happy because he passed the exam."),
        3: ("Pronombres Relativos ('Who')", "Traduce: 'El hombre que me llamó es mi hermano.'", "The man who called me is my brother."),
        4: ("Conjunciones Coordinantes", "Traduce: 'Puedes comer una manzana o puedes comer una naranja.'", "You can eat an apple or you can eat an orange."),
        5: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Te llamaré cuando llegue a casa.'", "I will call you when I get home."),
        6: ("Pronombres Relativos ('Which')", "Traduce: 'El libro, que es azul, es nuevo.'", "The book, which is blue, is new."),
        7: ("Conjunciones Coordinantes", "Traduce: 'Estaba cansado, así que fui a dormir.'", "I was tired, so I went to sleep."),
        8: ("Conjunciones Subordinantes (Condición)", "Traduce: 'Si estudias, pasarás el examen.'", "If you study, you will pass the exam."),
        9: ("Pronombres Relativos ('That')", "Traduce: 'La casa que compramos es grande.'", "The house that we bought is big."),
        10: ("Conjunciones Correlativas ('Either/Or')", "Traduce: 'O bien comes o bien bebes.'", "You can either eat or drink."),
        11: ("Conjunciones Subordinantes (Contraste)", "Traduce: 'Aunque es rico, es infeliz.'", "Although he is rich, he is unhappy."),
        12: ("Conjunciones Coordinantes", "Traduce: 'Ella no canta, ni tampoco baila.'", "She does not sing, nor does she dance."),
        13: ("Pronombres Relativos", "Traduce: 'La chica que está hablando es mi amiga.'", "The girl who is talking is my friend."),
        14: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Antes de que te vayas, por favor, cierra la puerta.'", "Before you leave, please close the door."),
        15: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Nos quedamos en casa ya que estaba lloviendo.'", "We stayed home since it was raining."),
        16: ("Conjunciones Coordinantes", "Traduce: 'Lo intenté, mas no pude.'", "I tried, yet I could not."),
        17: ("Pronombres Relativos", "Traduce: 'El perro que vive en la casa de al lado es ruidoso.'", "The dog that lives next door is loud."),
        18: ("Conjunciones Correlativas ('Both/And')", "Traduce: 'Ambos mi madre y mi padre trabajan aquí.'", "Both my mother and my father work here."),
        19: ("Conjunciones Subordinantes (Lugar)", "Traduce: 'Ve a donde quieras.'", "Go wherever you want."),
        20: ("Conjunciones Subordinantes (Condición)", "Traduce: 'No puedes pasar a menos que tengas un boleto.'", "You cannot enter unless you have a ticket."),
        21: ("Conjunciones Coordinantes", "Traduce: 'Llovía, y el viento soplaba.'", "It was raining, and the wind was blowing."),
        22: ("Pronombres Relativos", "Traduce: 'El coche, que es viejo, funciona bien.'", "The car, which is old, works well."),
        23: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Él no vino al colegio porque estaba enfermo.'", "He did not come to school because he was sick."),
        24: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Mientras yo estaba cocinando, él estaba viendo la televisión.'", "While I was cooking, he was watching television."),
        25: ("Conjunciones Correlativas ('Neither/Nor')", "Traduce: 'Ni mi hermano ni mi hermana están aquí.'", "Neither my brother nor my sister is here."),
        26: ("Conjunciones Subordinantes (Propósito)", "Traduce: 'Estudio para que pueda pasar.'", "I study so that I can pass."),
        27: ("Pronombres Relativos", "Traduce: 'La persona a quien le hablé es mi jefa.'", "The person to whom I spoke is my boss."),
        28: ("Conjunciones Subordinantes (Manera)", "Traduce: 'Se comporta como si fuera el jefe.'", "He acts as if he is the boss."),
        29: ("Conjunciones Coordinantes", "Traduce: 'Ella es bonita, y también es inteligente.'", "She is pretty, and she is also smart."),
        30: ("Conjunciones Subordinantes (Grado)", "Traduce: 'Es más grande de lo que pensaba.'", "It is bigger than I thought."),
        31: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Cuando llegué, ella ya se había ido.'", "When I arrived, she had already left."),
        32: ("Pronombres Relativos", "Traduce: 'La película que viste es muy buena.'", "The movie that you saw is very good."),
        33: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Dado que él no está aquí, podemos empezar.'", "Since he is not here, we can start."),
        34: ("Conjunciones Correlativas", "Traduce: 'Ambos el azul y el rojo me gustan.'", "I like both blue and red."),
        35: ("Conjunciones Subordinantes (Contraste)", "Traduce: 'A pesar de que tiene dinero, no lo gasta.'", "Even though he has money, he does not spend it."),
        36: ("Conjunciones Coordinantes", "Traduce: 'No tengo dinero, ni tengo un coche.'", "I have no money, nor do I have a car."),
        37: ("Conjunciones Subordinantes (Lugar)", "Traduce: 'Puedes sentarte donde quieras.'", "You can sit wherever you want."),
        38: ("Pronombres Relativos", "Traduce: 'El coche que está estacionado afuera es mío.'", "The car which is parked outside is mine."),
        39: ("Conjunciones Subordinantes (Condición)", "Traduce: 'No iremos a menos que él venga.'", "We will not go unless he comes."),
        40: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Mientras esperabas, yo estaba leyendo.'", "While you were waiting, I was reading."),
        41: ("Conjunciones Coordinantes", "Traduce: 'El examen fue difícil, pero lo pasé.'", "The exam was difficult, but I passed it."),
        42: ("Pronombres Relativos", "Traduce: 'Las personas que viven allí son amables.'", "The people who live there are kind."),
        43: ("Conjunciones Correlativas", "Traduce: 'Ni el agua ni la comida estaban disponibles.'", "Neither the water nor the food was available."),
        44: ("Conjunciones Subordinantes (Manera)", "Traduce: 'Él canta como un profesional.'", "He sings as if he is a professional."),
        45: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Tan pronto como él llegó, la fiesta comenzó.'", "As soon as he arrived, the party started."),
        46: ("Conjunciones Subordinantes (Contraste)", "Traduce: 'Él es alto, mientras que su hermano es bajo.'", "He is tall, whereas his brother is short."),
        47: ("Conjunciones Coordinantes", "Traduce: 'Ella habló, y todos la escucharon.'", "She spoke, and everyone listened to her."),
        48: ("Pronombres Relativos", "Traduce: 'El libro del que estás hablando es interesante.'", "The book that you are talking about is interesting."),
        49: ("Conjunciones Subordinantes (Condición)", "Traduce: 'Puedes llamarme si necesitas ayuda.'", "You can call me if you need help."),
        50: ("Conjunciones Subordinantes (Propósito)", "Traduce: 'Trabajo duro para que pueda ganar dinero.'", "I work hard so that I can earn money."),
        51: ("Conjunciones Coordinantes", "Traduce: 'Ella es bonita, por lo tanto, tiene muchos amigos.'", "She is pretty, therefore she has many friends."),
        52: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Estoy cansado porque no dormí.'", "I am tired because I did not sleep."),
        53: ("Pronombres Relativos", "Traduce: 'Los niños, que estaban jugando, estaban felices.'", "The children, who were playing, were happy."),
        54: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Desde que te vi, he sido feliz.'", "Since I saw you, I have been happy."),
        55: ("Conjunciones Correlativas", "Traduce: 'Puedes elegir o bien el rojo o bien el azul.'", "You can choose either red or blue."),
        56: ("Conjunciones Subordinantes (Lugar)", "Traduce: 'Vive donde pueda.'", "He lives wherever he can."),
        57: ("Conjunciones Subordinantes (Contraste)", "Traduce: 'Aunque está lloviendo, voy a salir.'", "Although it is raining, I am going out."),
        58: ("Conjunciones Coordinantes", "Traduce: 'Estudió, por lo tanto, no reprobó.'", "He studied, so he did not fail."),
        59: ("Pronombres Relativos", "Traduce: 'El restaurante que me recomendaste es bueno.'", "The restaurant that you recommended is good."),
        60: ("Conjunciones Subordinantes (Condición)", "Traduce: 'No lo compraré a menos que sea barato.'", "I will not buy it unless it is cheap."),
        61: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Ella se fue después de que yo llegué.'", "She left after I arrived."),
        62: ("Conjunciones Coordinantes", "Traduce: 'Estaba enfermo, por lo que no fui a trabajar.'", "I was sick, so I did not go to work."),
        63: ("Pronombres Relativos", "Traduce: 'El libro, el cual es muy viejo, es valioso.'", "The book, which is very old, is valuable."),
        64: ("Conjunciones Correlativas", "Traduce: 'Ella es tanto un buen doctor como una buena persona.'", "She is both a good doctor and a good person."),
        65: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Llegué tarde porque el bus estaba retrasado.'", "I was late because the bus was delayed."),
        66: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Tan pronto como él vio al perro, corrió.'", "As soon as he saw the dog, he ran."),
        67: ("Conjunciones Coordinantes", "Traduce: 'No me gusta la leche, ni me gusta el queso.'", "I don't like milk, nor do I like cheese."),
        68: ("Pronombres Relativos", "Traduce: 'La mujer que vive al lado es amable.'", "The woman who lives next door is kind."),
        69: ("Conjunciones Subordinantes (Contraste)", "Traduce: 'Aunque estaba cansado, no me rendí.'", "Although I was tired, I did not give up."),
        70: ("Conjunciones Subordinantes (Condición)", "Traduce: 'No lo haré si no me pagas.'", "I will not do it unless you pay me."),
        71: ("Conjunciones Subordinantes (Propósito)", "Traduce: 'Ahorro dinero para que pueda comprar un coche.'", "I save money so that I can buy a car."),
        72: ("Conjunciones Coordinantes", "Traduce: 'Ella habla español, y él habla francés.'", "She speaks Spanish, and he speaks French."),
        73: ("Pronombres Relativos", "Traduce: 'La idea que tienes es muy buena.'", "The idea that you have is very good."),
        74: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Mientras el sol brilla, podemos jugar.'", "While the sun is shining, we can play."),
        75: ("Conjunciones Correlativas", "Traduce: 'Puedes o bien quedarte o bien irte.'", "You can either stay or leave."),
        76: ("Conjunciones Subordinantes (Manera)", "Traduce: 'Ellos actúan como si fueran famosos.'", "They act as if they are famous."),
        77: ("Conjunciones Subordinantes (Lugar)", "Traduce: 'Él va donde el dinero lo lleva.'", "He goes wherever the money takes him."),
        78: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Como llegaste tarde, te perdiste el principio.'", "Since you arrived late, you missed the beginning."),
        79: ("Conjunciones Coordinantes", "Traduce: 'Él es pobre, mas es feliz.'", "He is poor, yet he is happy."),
        80: ("Pronombres Relativos", "Traduce: 'La película, la cual es muy popular, es divertida.'", "The movie, which is very popular, is fun."),
        81: ("Conjunciones Subordinantes (Condición)", "Traduce: 'Si necesitas ayuda, házmelo saber.'", "If you need help, let me know."),
        82: ("Conjunciones Coordinantes", "Traduce: 'Quería ir, pero no pude.'", "I wanted to go, but I could not."),
        83: ("Pronombres Relativos", "Traduce: 'El profesor que nos enseña es bueno.'", "The teacher who teaches us is good."),
        84: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Después de que comimos, caminamos.'", "After we ate, we walked."),
        85: ("Conjunciones Correlativas", "Traduce: 'Ni el blanco ni el negro se ven bien en ti.'", "Neither white nor black looks good on you."),
        86: ("Conjunciones Subordinantes (Lugar)", "Traduce: 'El restaurante está donde solía estar la tienda.'", "The restaurant is where the store used to be."),
        87: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Estoy feliz porque te veo.'", "I am happy because I see you."),
        88: ("Conjunciones Subordinantes (Contraste)", "Traduce: 'Aunque estaba lloviendo, fuimos a caminar.'", "Although it was raining, we went for a walk."),
        89: ("Conjunciones Coordinantes", "Traduce: 'Toma un paraguas, o te mojarás.'", "Take an umbrella, or you will get wet."),
        90: ("Pronombres Relativos", "Traduce: 'El coche, que es de mi padre, es nuevo.'", "The car, which is my father's, is new."),
        91: ("Conjunciones Subordinantes (Condición)", "Traduce: 'Si no vas, yo tampoco iré.'", "If you don't go, I won't go either."),
        92: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Ella se fue a dormir después de que terminó de leer.'", "She went to sleep after she finished reading."),
        93: ("Conjunciones Coordinantes", "Traduce: 'No tengo dinero, por lo que no puedo comprarlo.'", "I have no money, so I cannot buy it."),
        94: ("Pronombres Relativos", "Traduce: 'El perro que está ladrando es mío.'", "The dog that is barking is mine."),
        95: ("Conjunciones Correlativas", "Traduce: 'Tanto mi padre como mi madre están trabajando.'", "Both my father and my mother are working."),
        96: ("Conjunciones Subordinantes (Manera)", "Traduce: 'Habla como si fuera un experto.'", "He talks as if he were an expert."),
        97: ("Conjunciones Subordinantes (Causa)", "Traduce: 'Estaba cansado, por lo que me acosté.'", "I was tired, for I went to bed."),
        98: ("Conjunciones Subordinantes (Tiempo)", "Traduce: 'Ella lloró cuando vio la película.'", "She cried when she saw the movie."),
        99: ("Conjunciones Coordinantes", "Traduce: 'Tenía hambre, pero la nevera estaba vacía.'", "I was hungry, but the fridge was empty."),
        100: ("Repaso Final", "Traduce: 'Si me llamas, iré, y te ayudaré.'", "If you call me, I will go, and I will help you."),
    }

    print("¡Bienvenido al reto de Oraciones Compuestas en Inglés!")
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

            if clean_user_response == clean_correct_answer or (clean_user_response + '.') == clean_correct_answer or (clean_user_response + '?') == clean_correct_answer:
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
