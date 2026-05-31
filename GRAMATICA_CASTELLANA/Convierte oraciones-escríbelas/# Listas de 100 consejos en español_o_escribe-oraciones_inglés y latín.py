import random

# Listas de consejos en español, inglés y latín
consejos_espanol = [
    "Cree en ti mismo.",
    "Nunca te rindas.",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "Cree en ti mismo.",
    "Haz lo que puedas con lo que tienes, donde estés.",
    "La única manera de hacer un gran trabajo es amar lo que haces.",
    "El fracaso es la oportunidad de comenzar de nuevo con más experiencia.",
    "Mantén una actitud positiva en todo momento.",
    "El esfuerzo de hoy será la recompensa de mañana.",
    "No importa lo despacio que vayas, siempre y cuando no te detengas.",
    "El éxito es un viaje, no un destino.",
    "La perseverancia es la clave del éxito.",
    "El poder está dentro de ti.",
    "Atrévete a soñar en grande.",
    "El cambio empieza por ti.",
    "Transforma tus sueños en metas.",
    "La actitud es todo.",
    "Elimina la palabra imposible de tu vocabulario.",
    "Nunca es tarde para empezar de nuevo.",
    "El éxito no es la clave de la felicidad, la felicidad es la clave del éxito.",
    "Lo que no te mata te hace más fuerte.",
    "El esfuerzo constante vence al talento natural.",
    "Cada día es una nueva oportunidad para ser mejor.",
    "La disciplina tarde o temprano vencerá la inteligencia."
    "La paciencia es amarga, pero sus frutos son dulces.",
    "El fracaso es solo la oportunidad de comenzar de nuevo de manera más inteligente.",
    "No dejes que el miedo te detenga.",
    "El éxito es la suma de los detalles."
    "No esperes el momento perfecto, toma el momento y hazlo perfecto.",
    "El trabajo duro supera al talento cuando el talento no trabaja duro.",
    "No sueñes tu vida, vive tu sueño.",
    "Aprende de tus errores y sigue adelante.",
    "El coraje es resistencia al miedo, dominio del miedo, no ausencia de miedo.",
    "La acción es la llave fundamental para todo éxito.",
    "El futuro pertenece a aquellos que creen en la belleza de sus sueños.",
    "No tengas miedo de renunciar a lo bueno para ir a por lo mejor.",
    "La única limitación es tu imaginación.",
    "Vive como si fueras a morir mañana, aprende como si fueras a vivir para siempre.",
    "El éxito es la suma de pequeños esfuerzos, repetidos día tras día.",
    "No importa cuántas veces caigas, lo importante es cuántas veces te levantes.",
    "Las grandes cosas nunca vienen de zonas de confort.",
    "Tú eres el autor de tu propia vida.",
    "El éxito llega para quienes están dispuestos a trabajar duro.",
    "La clave del éxito es empezar antes de estar listo.",
    "El optimismo es la fe que conduce al logro.",
    "La vida es 10% lo que te sucede y 90% cómo reaccionas a ello.",
    "Haz de cada día una obra maestra.",
    "Cambia tus pensamientos y cambiarás tu mundo.",
    "El éxito no se mide por lo que logras, sino por los obstáculos que superas.",
    "El conocimiento no es poder hasta que se aplica.",
    "El único límite a nuestra realización de mañana serán nuestras dudas de hoy.",
    "Vive cada día como si fuera el último, pero aprende como si fueras a vivir para siempre.",
    "El éxito es la capacidad de ir de fracaso en fracaso sin perder el entusiasmo.",
    "Sé el cambio que deseas ver en el mundo.",
    "No te compares con los demás, compite contigo mismo.",
    "Las dificultades están destinadas a despertarnos, no a desalentarnos.",
    "Confía en el proceso.",
    "El sacrificio de hoy es el éxito de mañana.",
    "Nunca subestimes el poder de tus sueños.",
    "Tu actitud determina tu altitud.",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "La grandeza no está en nunca caer, sino en levantarse cada vez que se cae.",
    "No cuentes los días, haz que los días cuenten.",
    "El poder de la mente es infinito."
    "La clave del éxito es convertir los sueños en metas y las metas en acciones."
    "El momento adecuado es ahora."
    "Las cosas buenas vienen a aquellos que trabajan duro y esperan.",
    "Haz lo que amas y nunca trabajarás un día en tu vida.",
    "La mejor manera de predecir el futuro es crearlo.",
    "No dejes que el ayer ocupe demasiado espacio en el hoy.",
    "El éxito no es cuestión de suerte, sino de esfuerzo.",
    "Nunca te disculpes por ser tú mismo.",
    "Los obstáculos son esas cosas espantosas que ves cuando apartas los ojos de tu meta.",
    "El éxito es la habilidad de ir de fracaso en fracaso sin perder el entusiasmo.",
    "Si puedes soñarlo, puedes lograrlo.",
    "El éxito es una elección",
    "No hay atajos para alcanzar el éxito.",
    "El verdadero fracaso es no intentarlo.",
    "El mayor riesgo es no correr ningún riesgo.",
    "Vive sin excusas y ama sin arrepentimientos.",
    "Todo lo que siempre has querido está al otro lado del miedo.",
    "Nunca es demasiado tarde para ser lo que podrías haber sido.",
    "No te preocupes por fallar, preocúpate por no intentarlo.",
    "La felicidad no es tener lo que quieres, es querer lo que tienes.",
    "El éxito no está en lo que tienes, sino en quién eres.",
    "No hay ascensor para el éxito, tienes que tomar las escaleras.",
    "La vida no se trata de encontrarte a ti mismo, se trata de crearte a ti mismo.",
    "Hazlo con pasión o no lo hagas.",
    "El dolor es temporal, pero rendirse dura para siempre.",
    "El éxito no es cuestión de suerte, sino de esfuerzo.",
    "No tengas miedo de ser diferente, ten miedo de ser igual que todos los demás.",
    "El éxito es 1% inspiración y 99% transpiración.",
    "No esperes oportunidades, créalas.",
    "El éxito es la recompensa de la perseverancia.",
    "Los límites solo existen en tu mente.",
    "El fracaso es solo el condimento que da sabor al éxito.",
    "No busques excusas, busca resultados.",
    "La única manera de hacer un gran trabajo es amar lo que haces.",
    "No te detengas cuando estés cansado, detente cuando hayas terminado.",
    "La disciplina es el puente entre metas y logros.",
    "Nunca te canses de hacer el bien.",
]

consejos_ingles = [
    "Believe in yourself.",
    "Never give up.",
    "Success is the sum of small efforts repeated day after day.",
    "Do what you can with what you have, where you are.",
    "The only way to do great work is to love what you do.",
    "Failure is the opportunity to begin again with more experience.",
    "Keep a positive attitude at all times.",
    "Today's effort will be tomorrow's reward.",
    "It doesn't matter how slowly you go, as long as you don't stop.",
    "Success is a journey, not a destination.",
    "Perseverance is the key to success.",
    "The power is within you.",
    "Dare to dream big.",
    "Change starts with you.",
    "Turn your dreams into goals.",
    "Attitude is everything.",
    "Remove the word impossible from your vocabulary.",
    "It's never too late to start again.",
    "Success is not the key to happiness, happiness is the key to success.",
    "What doesn't kill you makes you stronger.",
    "Consistent effort beats natural talent.",
    "Each day is a new opportunity to be better.",
    "Discipline will sooner or later overcome intelligence.",
    "Patience is bitter, but its fruit is sweet.",
    "Failure is only the opportunity to begin again more intelligently.",
    "Don't let fear stop you.",
    "Success is the sum of details.",
    "Don't wait for the perfect moment, take the moment and make it perfect.",
    "Hard work beats talent when talent doesn't work hard.",
    "Don't dream your life, live your dream.",
    "Learn from your mistakes and move on.",
    "Courage is resistance to fear, mastery of fear, not absence of fear.",
    "Action is the foundational key to all success.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Don't be afraid to give up the good to go for the best.",
    "The only limitation is your imagination.",
    "Live as if you were to die tomorrow, learn as if you were to live forever.",
    "Success is the sum of small efforts, repeated day after day.",
    "It doesn't matter how many times you fall, what matters is how many times you get up.",
    "Great things never come from comfort zones.",
    "You are the author of your own life.",
    "Success comes to those who are willing to work hard.",
    "The key to success is starting before you're ready.",
    "Optimism is the faith that leads to achievement.",
    "Life is 10% what happens to you and 90% how you react to it.",
    "Make every day a masterpiece.",
    "Change your thoughts and you change your world.",
    "Success is not measured by what you achieve, but by the obstacles you overcome.",
    "Knowledge is not power until it is applied.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Live each day as if it were your last, but learn as if you were to live forever.",
    "Success is the ability to go from failure to failure without losing enthusiasm.",
    "Be the change you wish to see in the world.",
    "Don't compare yourself to others, compete with yourself.",
    "Difficulties are meant to rouse, not discourage.",
    "Trust the process.",
    "Today's sacrifice is tomorrow's success.",
    "Never underestimate the power of your dreams.",
    "Your attitude determines your altitude.",
    "Success is the sum of small efforts repeated day after day.",
    "Greatness is not in never falling, but in rising every time you fall.",
    "Don't count the days, make the days count.",
    "The power of the mind is infinite.",
    "The key to success is turning dreams into goals and goals into actions.",
    "The right time is now.",
    "Good things come to those who work hard and wait."
    "Do what you love and you'll never work a day in your life."
    "The best way to predict the future is to create it.",
    "Don't let yesterday take up too much of today.",
    "Success is not a matter of luck, but of effort.",
    "Never apologize for being yourself.",
    "Obstacles are those frightful things you see when you take your eyes off your goal.",
    "Success is the ability to go from failure to failure without losing enthusiasm.",
    "If you can dream it, you can achieve it.",
    "Success is a choice.",
    "There are no shortcuts to success."
    "The real failure is not trying."
    "The greatest risk is not taking any risks.",
    "Live without excuses and love without regrets.",
    "Everything you've ever wanted is on the other side of fear.",
    "It's never too late to be what you might have been.",
    "Don't worry about failure, worry about not trying.",
    "Happiness is not having what you want, it's wanting what you have.",
    "Success is not about what you have, but who you are.",
    "There's no elevator to success, you have to take the stairs.",
    "Life is not about finding yourself, it's about creating yourself.",
    "Do it with passion or not at all.",
    "Pain is temporary, but quitting lasts forever.",
    "Success is not a matter of luck, but of effort.",
    "Don't be afraid to be different, be afraid to be the same as everyone else.",
    "Success is 1% inspiration and 99% perspiration.",
    "Don't wait for opportunities, create them.",
    "Success is the reward of perseverance.",
    "Limits only exist in your mind.",
    "Failure is only the seasoning that gives success its flavor.",
    "Don't look for excuses, look for results.",
    "The only way to do great work is to love what you do.",
    "Don't stop when you're tired, stop when you're done.",
    "Discipline is the bridge between goals and accomplishments.",
    "Never tire of doing good.",
]

consejos_latin = [
    "Crede in te ipsum.",
    "Numquam desiste.",
    "Successus est summa parvorum conatuum die post diem repetitorum.",
    "Fac quod potes cum eo quod habes, ubi es.",
    "Unicus modus ad magnum opus faciendum est amare quod facis.",
    "Defectus est occasio iterum incipere cum experientia.",
    "Semper positivum habitum habe.",
    "Hodierna conatus erit crastina merces.",
    "Non refert quam tarde vadis, modo ne desistas.",
    "Successus est iter, non destinatio."
    "Perseverantia est clavis ad successum.",
    "Potestas intra te est.",
    "Aude magnos somniare.",
    "Mutatio a te incipit.",
    "Somnia tua in metas converte.",
    "Habitus est omnia.",
    "Verbum impossibile e tuo vocabulario remove.",
    "Numquam sero est ut iterum incipias.",
    "Successus non est clavis ad felicitatem, felicitas est clavis ad successum.",
    "Quod non te occidit te fortiorem facit.",
    "Continuus conatus ingenium naturale vincit.",
    "Unusquisque dies nova occasio est melioris fieri.",
    "Disciplina tandem ingenium superabit.",
    "Patientia est amara, sed fructus eius dulcis est.",
    "Defectus est tantum occasio iterum incipere cum maiori intelligentia.",
    "Ne timeas, ne te impediat.",
    "Successus est summa singularium.",
    "Ne expecta momentum perfectum, accipe momentum et fac perfectum.",
    "Durus labor ingenium superat, cum ingenium non laborat.",
    "Non somniare vitam tuam, vive somnium tuum.",
    "Disce ex erroribus tuis et progredere.",
    "Virtus est resistentia timori, dominatus timoris, non absentia timoris.",
    "Actio est clavem ad omnem successum.",
    "Futurum pertinet ad eos qui in pulchritudinem somniorum suorum credunt.",
    "Ne timeas cedere bonum ut melius consequi possis.",
    "Unicus limitatio est imaginatio tua.",
    "Vive quasi cras moriturus, disce quasi in aeternum victurus.",
    "Successus est summa parvorum conatuum, die post diem repetitorum.",
    "Non refert quoties cadis, quod refert quoties surgis.",
    "Magnarum rerum origo non in zonis commodi est.",
    "Tu auctor vitae tuae es.",
    "Successus venit ad eos qui laborare parati sunt.",
    "Clavis ad successum est incipere antequam paratus sis.",
    "Optimismus est fides quae ducit ad effectum.",
    "Vita est 10% quid tibi accidit et 90% quomodo ei respondeas.",
    "Fac omnem diem opus perfectum.",
    "Mutato cogitationes tuas et mutabis mundum tuum.",
    "Successus non metitur per quod assequeris, sed per obstacula quae superas.",
    "Scientia non est potestas donec adhibeatur.", 
    "Unicus limitatio nostrarum rerum futura est dubitatio hodierna."
]

# Función para practicar consejos en un idioma específico
def practicar_consejos(consejos, idioma):
    print(f"\nPracticando consejos en {idioma}:\n")
    random.shuffle(consejos)  # Mezcla los consejos para hacer la práctica más interesante
    puntaje = 0

    for i, consejo in enumerate(consejos):
        print(f"Consejo {i+1}: {consejo}")
        respuesta = input("Escribe correctamente: ")

        if respuesta.strip().lower() == consejo.lower():
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {consejo}\n")

    print(f"Tu puntaje final en {idioma}: {puntaje}/{len(consejos)}\n")

# Menú principal
def menu_principal():
    while True:
        print("Seleccione el idioma en el que desea practicar:")
        print("1. Español")
        print("2. Inglés")
        print("3. Latín")
        print("4. Salir")

        opcion = input("Ingrese el número de su elección: ")

        if opcion == '1':
            practicar_consejos(consejos_espanol, "Español")
        elif opcion == '2':
            practicar_consejos(consejos_ingles, "Inglés")
        elif opcion == '3':
            practicar_consejos(consejos_latin, "Latín")
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, elija de nuevo.\n")

# Ejecución del programa
menu_principal()
