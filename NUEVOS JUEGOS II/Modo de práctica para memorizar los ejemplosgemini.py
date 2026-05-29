import json
import os
import random

FILE_NAME = "ejemplos_entonces.json"

EJEMPLOS_INICIALES = [
    {
        "id": 1,
        "es": "Si no hay pan, entonces compremos galletas.",
        "en": "If there's no bread, then let's buy cookies.",
        "fr": "S'il n'y a pas de pain, alors achetons des biscuits."
    },
    {
        "id": 2,
        "es": "Él era muy feliz entonces.",
        "en": "He was very happy then.",
        "fr": "Il était très heureux alors."
    },
    {
        "id": 3,
        "es": "Ya que llegas tarde, entonces no te esperaré.",
        "en": "Since you're late, then I won't wait for you.",
        "fr": "Puisque tu es en retard, alors je ne t'attendrai pas."
    },
    {
        "id": 4,
        "es": "Si es de día, entonces hay sol.",
        "en": "If it's daytime, then there is sun.",
        "fr": "S'il fait jour, alors il y a du soleil."
    },
    {
        "id": 5,
        "es": "No estudié, por lo tanto, fallé el examen.",
        "en": "I didn't study, therefore, I failed the exam.",
        "fr": "Je n'ai pas étudié, par conséquent, j'ai échoué à l'examen."
    },
    {
        "id": 6,
        "es": "Había una vez un rey. Entonces, el dragón llegó.",
        "en": "Once upon a time there was a king. Then, the dragon arrived.",
        "fr": "Il était une fois un roi. Alors, le dragon arriva."
    },
    {
        "id": 7,
        "es": "Si la puerta está abierta, entonces entra.",
        "en": "If the door is open, then come in.",
        "fr": "Si la porte est ouverte, alors entre."
    },
    {
        "id": 8,
        "es": "Me gradué en el 2010. En aquel entonces, no había smartphones.",
        "en": "I graduated in 2010. Back then, there were no smartphones.",
        "fr": "J'ai obtenu mon diplôme en 2010. À cette époque, il n'y avait pas de smartphones."
    },
    {
        "id": 9,
        "es": "No tengo dinero, así que no puedo ir.",
        "en": "I have no money, so I can't go.",
        "fr": "Je n'ai pas d'argent, donc je ne peux pas y aller."
    },
    {
        "id": 10,
        "es": "Si te duele, entonces ve al médico.",
        "en": "If it hurts, then go to the doctor.",
        "fr": "Si tu as mal, alors va chez le médecin."
    },
    {
        "id": 11,
        "es": "Éramos niños, entonces la vida era simple.",
        "en": "We were children, then life was simple.",
        "fr": "Nous étions des enfants, alors la vie était simple."
    },
    {
        "id": 12,
        "es": "Si el tráfico es denso, entonces llegaremos tarde.",
        "en": "If the traffic is heavy, then we will be late.",
        "fr": "Si la circulation est dense, alors nous serons en retard."
    },
    {
        "id": 13,
        "es": "El motor falló, por lo tanto, el avión aterrizó de emergencia.",
        "en": "The engine failed, therefore, the plane made an emergency landing.",
        "fr": "Le moteur est tombé en panne, par conséquent, l'avion a atterri en urgence."
    },
    {
        "id": 14,
        "es": "Si el tren no llega, entonces buscaré un taxi.",
        "en": "If the train doesn't arrive, then I'll look for a taxi.",
        "fr": "Si le train n'arrive pas, alors je chercherai un taxi."
    },
    {
        "id": 15,
        "es": "Ya que no contestas, entonces asumo que estás de acuerdo.",
        "en": "Since you don't answer, then I assume you agree.",
        "fr": "Puisque tu ne réponds pas, alors je suppose que tu es d'accord."
    },
    {
        "id": 16,
        "es": "La primera vez que te vi, entonces me enamoré.",
        "en": "The first time I saw you, then I fell in love.",
        "fr": "La première fois que je t'ai vue, alors je suis tombé amoureux."
    },
    {
        "id": 17,
        "es": "Él era solo un niño, en ese entonces.",
        "en": "He was just a child, at that time.",
        "fr": "Il n'était qu'un enfant, à ce moment-là."
    },
    {
        "id": 18,
        "es": "Si necesitas ayuda, entonces llama.",
        "en": "If you need help, then call.",
        "fr": "Si tu as besoin d'aide, alors appelle."
    },
    {
        "id": 19,
        "es": "Está lloviendo, por consiguiente, el partido se cancela.",
        "en": "It's raining, consequently, the game is canceled.",
        "fr": "Il pleut, par conséquent, le match est annulé."
    },
    {
        "id": 20,
        "es": "Él llegó, y entonces todos se callaron.",
        "en": "He arrived, and then everyone went silent.",
        "fr": "Il est arrivé, et alors tout le monde s'est tu."
    },
    {
        "id": 21,
        "es": "Si no lo sabes, entonces pregunta.",
        "en": "If you don't know, then ask.",
        "fr": "Si tu ne le sais pas, alors demande."
    },
    {
        "id": 22,
        "es": "Vivíamos en una casa pequeña entonces.",
        "en": "We lived in a small house then.",
        "fr": "Nous vivions dans une petite maison alors."
    },
    {
        "id": 23,
        "es": "Ya que no funciona, entonces lo reemplazaremos.",
        "en": "Since it doesn't work, then we'll replace it.",
        "fr": "Puisque ça ne marche pas, alors nous le remplacerons."
    },
    {
        "id": 24,
        "es": "La batería está baja, por lo tanto, el teléfono se apagó.",
        "en": "The battery is low, therefore, the phone turned off.",
        "fr": "La batterie est faible, par conséquent, le téléphone s'est éteint."
    },
    {
        "id": 25,
        "es": "Si te gusta, entonces cómpralo.",
        "en": "If you like it, then buy it.",
        "fr": "Si tu l'aimes, alors achète-le."
    },
    {
        "id": 26,
        "es": "Cuando yo era joven, en ese entonces, la televisión era en blanco y negro.",
        "en": "When I was young, at that time, television was in black and white.",
        "fr": "Quand j'étais jeune, à cette époque, la télévision était en noir et blanc."
    },
    {
        "id": 27,
        "es": "El resultado es negativo, entonces no tienes la enfermedad.",
        "en": "The result is negative, then you don't have the disease.",
        "fr": "Le résultat est négatif, donc tu n'as pas la maladie."
    },
    {
        "id": 28,
        "es": "Llegó un fuerte huracán, de modo que el vuelo fue cancelado.",
        "en": "A strong hurricane arrived, so the flight was canceled.",
        "fr": "Un fort ouragan est arrivé, de sorte que le vol a été annulé."
    },
    {
        "id": 29,
        "es": "Si no comes, entonces no crecerás.",
        "en": "If you don't eat, then you won't grow.",
        "fr": "Si tu ne manges pas, alors tu ne grandiras pas."
    },
    {
        "id": 30,
        "es": "Ella se casó en 1999, entonces vivía en España.",
        "en": "She got married in 1999, she lived in Spain then.",
        "fr": "Elle s'est mariée en 1999, elle vivait en Espagne à ce moment-là."
    },
    {
        "id": 31,
        "es": "Si es una emergencia, entonces ven ahora.",
        "en": "If it's an emergency, then come now.",
        "fr": "Si c'est une urgence, alors viens maintenant."
    },
    {
        "id": 32,
        "es": "El camino estaba bloqueado, por consiguiente, dimos la vuelta.",
        "en": "The road was blocked, consequently, we turned around.",
        "fr": "La route était bloquée, par conséquent, nous avons fait demi-tour."
    },
    {
        "id": 33,
        "es": "Comienza a llover, entonces cierra la ventana.",
        "en": "It's starting to rain, then close the window.",
        "fr": "Il commence à pleuvoir, alors ferme la fenêtre."
    },
    {
        "id": 34,
        "es": "Si el agua hierve, entonces apaga la estufa.",
        "en": "If the water boils, then turn off the stove.",
        "fr": "Si l'eau bout, alors éteins le poêle."
    },
    {
        "id": 35,
        "es": "La computadora se sobrecalentó, así que se apagó.",
        "en": "The computer overheated, so it shut down.",
        "fr": "L'ordinateur a surchauffé, donc il s'est éteint."
    },
    {
        "id": 36,
        "es": "Ella sonrió, y entonces él supo la respuesta.",
        "en": "She smiled, and then he knew the answer.",
        "fr": "Elle a souri, et alors il a su la réponse."
    },
    {
        "id": 37,
        "es": "Si lo haces mal, entonces repítelo.",
        "en": "If you do it wrong, then repeat it.",
        "fr": "Si tu le fais mal, alors répète-le."
    },
    {
        "id": 38,
        "es": "En ese entonces, yo no sabía la verdad.",
        "en": "Back then, I didn't know the truth.",
        "fr": "À cette époque-là, je ne connaissais pas la vérité."
    },
    {
        "id": 39,
        "es": "Si el autobús no pasa, entonces caminaremos.",
        "en": "If the bus doesn't pass, then we will walk.",
        "fr": "Si le bus ne passe pas, alors nous marcherons."
    },
    {
        "id": 40,
        "es": "El examen era difícil, por lo tanto, nadie lo aprobó.",
        "en": "The exam was difficult, therefore, no one passed it.",
        "fr": "L'examen était difficile, par conséquent, personne ne l'a réussi."
    },
    {
        "id": 41,
        "es": "Estudiaba por la noche, y entonces dormía durante el día.",
        "en": "I studied at night, and then I slept during the day.",
        "fr": "J'étudiais la nuit, et alors je dormais pendant la journée."
    },
    {
        "id": 42,
        "es": "Si me necesitas, entonces avísame.",
        "en": "If you need me, then let me know.",
        "fr": "Si tu as besoin de moi, alors fais-le-moi savoir."
    },
    {
        "id": 43,
        "es": "No hay más boletos, así que ya no podemos entrar.",
        "en": "There are no more tickets, so we can't enter anymore.",
        "fr": "Il n'y a plus de billets, donc nous ne pouvons plus entrer."
    },
    {
        "id": 44,
        "es": "Si él no está, entonces pregunta a otra persona.",
        "en": "If he's not here, then ask someone else.",
        "fr": "S'il n'est pas là, alors demande à une autre personne."
    },
    {
        "id": 45,
        "es": "Recuerdo mi infancia, en ese entonces éramos pobres.",
        "en": "I remember my childhood, back then we were poor.",
        "fr": "Je me souviens de mon enfance, à cette époque nous étions pauvres."
    },
    {
        "id": 46,
        "es": "Si el auto se averió, entonces tomaremos el autobús.",
        "en": "If the car broke down, then we'll take the bus.",
        "fr": "Si la voiture est tombée en panne, alors nous prendrons le bus."
    },
    {
        "id": 47,
        "es": "Se cortó la luz, por lo tanto, no pude trabajar.",
        "en": "The power went out, therefore, I couldn't work.",
        "fr": "Le courant a été coupé, par conséquent, je n'ai pas pu travailler."
    },
    {
        "id": 48,
        "es": "Llegó al final, y entonces se rindió.",
        "en": "He reached the end, and then he gave up.",
        "fr": "Il a atteint la fin, et alors il a abandonné."
    },
    {
        "id": 49,
        "es": "Si ella no llama, entonces no iré.",
        "en": "If she doesn't call, then I won't go.",
        "fr": "Si elle n'appelle pas, alors je n'irai pas."
    },
    {
        "id": 50,
        "es": "Los precios eran más bajos en ese entonces.",
        "en": "Prices were lower back then.",
        "fr": "Les prix étaient plus bas à cette époque."
    },
    {
        "id": 51,
        "es": "El niño se cayó, entonces empezó a llorar.",
        "en": "The boy fell, then he started to cry.",
        "fr": "Le garçon est tombé, alors il a commencé à pleurer."
    },
    {
        "id": 52,
        "es": "Si el resultado es cero, entonces la operación es inválida.",
        "en": "If the result is zero, then the operation is invalid.",
        "fr": "Si le résultat est zéro, alors l'opération est invalide."
    },
    {
        "id": 53,
        "es": "No tenemos suficientes ingredientes, por lo tanto, no podemos hornear el pastel.",
        "en": "We don't have enough ingredients, therefore, we can't bake the cake.",
        "fr": "Nous n'avons pas assez d'ingrédients, par conséquent, nous ne pouvons pas faire le gâteau."
    },
    {
        "id": 54,
        "es": "Él se mudó en el 2005. En ese entonces, vivía solo.",
        "en": "He moved in 2005. At that time, he lived alone.",
        "fr": "Il a déménagé en 2005. À cette époque, il vivait seul."
    },
    {
        "id": 55,
        "es": "El clima es frío, así que usa un abrigo.",
        "en": "The weather is cold, so wear a coat.",
        "fr": "Le temps est froid, donc porte un manteau."
    },
    {
        "id": 56,
        "es": "Llegó un perro, entonces la gata se escondió.",
        "en": "A dog arrived, then the cat hid.",
        "fr": "Un chien est arrivé, alors la chatte s'est cachée."
    },
    {
        "id": 57,
        "es": "Si el cliente no paga, entonces no entregues el producto.",
        "en": "If the client doesn't pay, then don't deliver the product.",
        "fr": "Si le client ne paie pas, alors ne livre pas le produit."
    },
    {
        "id": 58,
        "es": "Era un bebé entonces.",
        "en": "He was a baby then.",
        "fr": "Il était un bébé alors."
    },
    {
        "id": 59,
        "es": "El motor se averió, por consiguiente, el viaje terminó.",
        "en": "The engine broke down, consequently, the trip ended.",
        "fr": "Le moteur est tombé en panne, par conséquent, le voyage s'est terminé."
    },
    {
        "id": 60,
        "es": "Si no lo puedes hacer, entonces pídele ayuda a alguien.",
        "en": "If you can't do it, then ask someone for help.",
        "fr": "Si tu ne peux pas le faire, alors demande de l'aide à quelqu'un."
    },
    {
        "id": 61,
        "es": "Leí el libro, y entonces entendí la película.",
        "en": "I read the book, and then I understood the movie.",
        "fr": "J'ai lu le livre, et alors j'ai compris le film."
    },
    {
        "id": 62,
        "es": "Si el sol se pone, entonces se hace de noche.",
        "en": "If the sun sets, then it gets dark.",
        "fr": "Si le soleil se couche, alors il fait nuit."
    },
    {
        "id": 63,
        "es": "No hay espacio en el disco duro, así que no puedo instalarlo.",
        "en": "There is no space on the hard drive, so I can't install it.",
        "fr": "Il n'y a pas d'espace sur le disque dur, donc je ne peux pas l'installer."
    },
    {
        "id": 64,
        "es": "En ese entonces, no existían los teléfonos inteligentes.",
        "en": "Back then, smartphones didn't exist.",
        "fr": "À cette époque-là, les smartphones n'existaient pas."
    },
    {
        "id": 65,
        "es": "Si la tienda está cerrada, entonces iremos a otra.",
        "en": "If the store is closed, then we'll go to another one.",
        "fr": "Si le magasin est fermé, alors nous irons à un autre."
    },
    {
        "id": 66,
        "es": "La primera vez que fuimos, entonces el lugar estaba vacío.",
        "en": "The first time we went, then the place was empty.",
        "fr": "La première fois que nous sommes allés, alors l'endroit était vide."
    },
    {
        "id": 67,
        "es": "El carro se averió, por lo tanto, llegamos tarde.",
        "en": "The car broke down, therefore, we arrived late.",
        "fr": "La voiture est tombée en panne, par conséquent, nous sommes arrivés en retard."
    },
    {
        "id": 68,
        "es": "El niño no se siente bien, por consiguiente, no irá a la escuela.",
        "en": "The child is not feeling well, consequently, he will not go to school.",
        "fr": "L'enfant ne se sent pas bien, par conséquent, il n'ira pas à l'école."
    },
    {
        "id": 69,
        "es": "Si hace calor, entonces enciende el aire acondicionado.",
        "en": "If it's hot, then turn on the air conditioner.",
        "fr": "S'il fait chaud, alors allume le climatiseur."
    },
    {
        "id": 70,
        "es": "La batería se agotó, así que ya no podemos usar la linterna.",
        "en": "The battery ran out, so we can't use the flashlight anymore.",
        "fr": "La batterie est épuisée, donc nous ne pouvons plus utiliser la lampe de poche."
    },
    {
        "id": 71,
        "es": "Primero hicimos la cena, entonces comimos.",
        "en": "First we made dinner, then we ate.",
        "fr": "D'abord nous avons fait le dîner, alors nous avons mangé."
    },
    {
        "id": 72,
        "es": "Si la señal es mala, entonces reinicia el router.",
        "en": "If the signal is bad, then restart the router.",
        "fr": "Si le signal est mauvais, alors redémarre le routeur."
    },
    {
        "id": 73,
        "es": "Ella se enfermó, entonces fue al hospital.",
        "en": "She got sick, then she went to the hospital.",
        "fr": "Elle est tombée malade, alors elle est allée à l'hôpital."
    },
    {
        "id": 74,
        "es": "La economía era fuerte en ese entonces.",
        "en": "The economy was strong back then.",
        "fr": "L'économie était forte à cette époque-là."
    },
    {
        "id": 75,
        "es": "El camino estaba resbaladizo, por lo tanto, manejamos con cuidado.",
        "en": "The road was slippery, therefore, we drove carefully.",
        "fr": "La route était glissante, par conséquent, nous avons conduit prudemment."
    },
    {
        "id": 76,
        "es": "Si la luz es roja, entonces detente.",
        "en": "If the light is red, then stop.",
        "fr": "Si le feu est rouge, alors arrête-toi."
    },
    {
        "id": 77,
        "es": "No hay más agua, así que no podemos lavar los platos.",
        "en": "There is no more water, so we can't wash the dishes.",
        "fr": "Il n'y a plus d'eau, donc nous ne pouvons pas faire la vaisselle."
    },
    {
        "id": 78,
        "es": "El niño no quiso comer, entonces le dimos un jugo.",
        "en": "The boy didn't want to eat, then we gave him a juice.",
        "fr": "Le garçon n'a pas voulu manger, alors nous lui avons donné un jus."
    },
    {
        "id": 79,
        "es": "Si no llegas a tiempo, entonces el juego comenzará sin ti.",
        "en": "If you don't arrive on time, then the game will start without you.",
        "fr": "Si tu n'arrives pas à l'heure, alors le jeu commencera sans toi."
    },
    {
        "id": 80,
        "es": "Él era más joven, en aquel entonces.",
        "en": "He was younger, back then.",
        "fr": "Il était plus jeune, à cette époque-là."
    },
    {
        "id": 81,
        "es": "La llamada se cortó, entonces volví a marcar.",
        "en": "The call was cut off, then I redialed.",
        "fr": "L'appel a été coupé, alors j'ai recomposé le numéro."
    },
    {
        "id": 82,
        "es": "Si el perro ladra, entonces hay alguien en la puerta.",
        "en": "If the dog barks, then there's someone at the door.",
        "fr": "Si le chien aboie, alors il y a quelqu'un à la porte."
    },
    {
        "id": 83,
        "es": "El sol se ocultó, por consiguiente, la temperatura bajó.",
        "en": "The sun hid, consequently, the temperature dropped.",
        "fr": "Le soleil s'est caché, par conséquent, la température a baissé."
    },
    {
        "id": 84,
        "es": "No había internet en ese entonces.",
        "en": "There was no internet back then.",
        "fr": "Il n'y avait pas d'internet à cette époque-là."
    },
    {
        "id": 85,
        "es": "Si no hay gasolina, entonces no podemos conducir.",
        "en": "If there's no gas, then we can't drive.",
        "fr": "S'il n'y a pas d'essence, alors nous ne pouvons pas conduire."
    },
    {
        "id": 86,
        "es": "El paquete se perdió, por lo tanto, pedimos un reembolso.",
        "en": "The package was lost, therefore, we asked for a refund.",
        "fr": "Le paquet a été perdu, par conséquent, nous avons demandé un remboursement."
    },
    {
        "id": 87,
        "es": "Si el niño llora, entonces abrázalo.",
        "en": "If the child cries, then hug him.",
        "fr": "Si l'enfant pleure, alors serre-le dans tes bras."
    },
    {
        "id": 88,
        "es": "Terminó la película, y entonces nos fuimos.",
        "en": "The movie ended, and then we left.",
        "fr": "Le film s'est terminé, et alors nous sommes partis."
    },
    {
        "id": 89,
        "es": "Si te sientes mal, entonces quédate en casa.",
        "en": "If you feel bad, then stay home.",
        "fr": "Si tu te sens mal, alors reste à la maison."
    },
    {
        "id": 90,
        "es": "La impresora no tiene tinta, así que no puedo imprimir.",
        "en": "The printer has no ink, so I can't print.",
        "fr": "L'imprimante n'a pas d'encre, donc je ne peux pas imprimer."
    },
    {
        "id": 91,
        "es": "El coche se quedó sin gasolina, entonces tuvimos que caminar.",
        "en": "The car ran out of gas, then we had to walk.",
        "fr": "La voiture est tombée en panne d'essence, alors nous avons dû marcher."
    },
    {
        "id": 92,
        "es": "Si el clima es bueno, entonces saldremos a caminar.",
        "en": "If the weather is good, then we'll go for a walk.",
        "fr": "Si le temps est bon, alors nous irons faire une promenade."
    },
    {
        "id": 93,
        "es": "Se hizo de noche, por lo tanto, encendimos las luces.",
        "en": "It got dark, therefore, we turned on the lights.",
        "fr": "Il a fait nuit, par conséquent, nous avons allumé les lumières."
    },
    {
        "id": 94,
        "es": "Si no entiendes, entonces te lo explicaré de nuevo.",
        "en": "If you don't understand, then I'll explain it to you again.",
        "fr": "Si tu ne comprends pas, alors je te l'expliquerai à nouveau."
    },
    {
        "id": 95,
        "es": "La alarma sonó, entonces me levanté de la cama.",
        "en": "The alarm went off, then I got out of bed.",
        "fr": "Le réveil a sonné, alors je me suis levé du lit."
    },
    {
        "id": 96,
        "es": "Si el precio es demasiado alto, entonces no lo compres.",
        "en": "If the price is too high, then don't buy it.",
        "fr": "Si le prix est trop élevé, alors ne l'achète pas."
    },
    {
        "id": 97,
        "es": "La comida estaba salada, por lo tanto, no la comimos.",
        "en": "The food was salty, therefore, we didn't eat it.",
        "fr": "La nourriture était salée, par conséquent, nous ne l'avons pas mangée."
    },
    {
        "id": 98,
        "es": "Si quieres ver la película, entonces ven esta noche.",
        "en": "If you want to watch the movie, then come tonight.",
        "fr": "Si tu veux voir le film, alors viens ce soir."
    },
    {
        "id": 99,
        "es": "No sabía la respuesta, así que adiviné.",
        "en": "I didn't know the answer, so I guessed.",
        "fr": "Je ne connaissais pas la réponse, donc j'ai deviné."
    },
    {
        "id": 100,
        "es": "Recuerdo mi primer teléfono, en ese entonces era enorme.",
        "en": "I remember my first phone, back then it was huge.",
        "fr": "Je me souviens de mon premier téléphone, à cette époque, il était énorme."
    }
]

def cargar_ejemplos():
    """Carga los ejemplos desde un archivo JSON o usa los ejemplos iniciales."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Guarda los ejemplos iniciales si el archivo no existe
        guardar_ejemplos(EJEMPLOS_INICIALES)
        return EJEMPLOS_INICIALES

def guardar_ejemplos(ejemplos):
    """Guarda los ejemplos en el archivo JSON."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, indent=4, ensure_ascii=False)
    print("Ejemplos guardados correctamente.")

def mostrar_menu():
    """Muestra el menú principal de la consola."""
    print("\n--- Gestor de Ejemplos 'Entonces' ---")
    print("1. Practicar/Memorizar")
    print("2. Ver todos los ejemplos")
    print("3. Agregar nuevo ejemplo")
    print("4. Salir")

def practicar(ejemplos):
    """Modo de práctica para memorizar los ejemplos."""
    print("\n--- Modo de Práctica ---")
    if not ejemplos:
        print("No hay ejemplos para practicar. Añade algunos primero.")
        return

    while True:
        ejemplo = random.choice(ejemplos)
        print(f"\nTraduce la siguiente frase:")
        print(f"Español: {ejemplo['es']}")
        
        input("Presiona Enter para ver las traducciones...")
        
        print(f"  Inglés: {ejemplo['en']}")
        print(f"  Francés: {ejemplo['fr']}")
        
        continuar = input("\n¿Quieres practicar con otro ejemplo? (s/n): ")
        if continuar.lower() != 's':
            break

def ver_ejemplos(ejemplos):
    """Muestra la lista completa de ejemplos."""
    print("\n--- Lista de Ejemplos ---")
    if not ejemplos:
        print("No hay ejemplos guardados.")
        return
    for ejemplo in ejemplos:
        print("-" * 20)
        print(f"ID: {ejemplo['id']}")
        print(f"  Español: {ejemplo['es']}")
        print(f"  Inglés: {ejemplo['en']}")
        print(f"  Francés: {ejemplo['fr']}")
    print("-" * 20)

def agregar_ejemplo(ejemplos):
    """Permite al usuario agregar un nuevo ejemplo."""
    print("\n--- Agregar Nuevo Ejemplo ---")
    es = input("Introduce la frase en español: ")
    en = input("Introduce la traducción en inglés: ")
    fr = input("Introduce la traducción en francés: ")
    
    nuevo_id = 1
    if ejemplos:
        nuevo_id = max(e['id'] for e in ejemplos) + 1
    
    ejemplos.append({
        "id": nuevo_id,
        "es": es,
        "en": en,
        "fr": fr
    })
    guardar_ejemplos(ejemplos)
    print("Ejemplo agregado exitosamente.")

def main():
    """Función principal para ejecutar el programa."""
    ejemplos = cargar_ejemplos()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            practicar(ejemplos)
        elif opcion == '2':
            ver_ejemplos(ejemplos)
        elif opcion == '3':
            agregar_ejemplo(ejemplos)
        elif opcion == '4':
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
