import random

# Bienvenida
def bienvenida():
    print("¡🏛️ Bienvenido a la Biblioteca Romana 🏛️ !")
    print("Eres un aprendiz📜️🕵️✏ de latín y tu misión es completar desafíos gramaticales.")
    print("En tu aventura, personajes históricos⏳ y mitológicos te ayudarán o desafiarán.")
    print("Cada logro desbloqueará nuevas recompensas y títulos honoríficos.🎶🧭🎉")
    print("Buena suerte en tu misión, ¡Orador de Roma!")

# Menú principal
def menu_principal():
    print("\nElige una opción:")
    print("1. 🌟📌Conocer a los personajes📜️🕵")
    print("2. 🌟📌Realizar un desafío📜️🕵")
    print("3. 🌟📌Ver recompensas🎶🧭🎉")
    print("4. Salir")

# Personajes históricos
def conocer_personajes():
    print("\nPersonajes de la Biblioteca Romana:")
    print("1. 🌟📌Virgilio📜️🕵 - Poeta épico que te guiará en la poesía latina.")
    print("2. 🌟📌Cicerón 📜️🕵- Orador y filósofo que te desafiará en gramática avanzada.")
    print("3. 🌟📌Minerva 📜️🕵- Diosa de la sabiduría que te enseñará etimología y vocabulario.")
    print("Habla con ellos en los desafíos para obtener recompensas y aprender más.")

# Desafíos de gramática
def desafio_virgilio():
    print("\nVirgilio📜️🕵: 'Salve, aprendiz. Te daré una línea de la *Eneida*.'")
    print("🌟📌Traduce y elige el caso correcto del sustantivo 'puella' en esta frase: 'Puella rosas amat.'")
    respuesta = input("Elige el caso: Nominativo, Genitivo, Acusativo, Vocativo: ").strip().lower()
    if respuesta == "acusativo":
        print("¡Correcto!🎶🧭🎉 'Puella' es el objeto directo aquí.")
        recompensas.append("Pergamino de Virgilio: Dominio del Acusativo")
    else:
        print("Respuesta incorrecta. Intenta de nuevo cuando estés listo.")

def desafio_ciceron():
    print("\nCicerón📜️🕵: 'Saludos, joven aprendiz. Resuelve esta construcción en latín.'")
    print("🌟📌Completa la oración usando la conjugación correcta del verbo 'amo' en primera persona singular.")
    respuesta = input("Conjugación de 'amo' en primera persona singular: ").strip().lower()
    if respuesta == "amo":
        print("¡Excelente🎶🧭🎉! La conjugación es correcta.📜️🕵")
        recompensas.append("Insignia de Cicerón: Dominio de la primera conjugación")
    else:
        print("Incorrecto. Recuerda la primera persona singular.")

def desafio_minerva():
    print("\nMinerva👋: 'Soy la diosa de la sabiduría. Te ayudaré con vocabulario.'")
    print("🌟📌Dime la raíz latina de la palabra inglesa 'manual'.")
    respuesta = input("Raíz en latín: ").strip().lower()
    if respuesta == "manus":
        print("¡Exacto🧭⚡😄🌟! 'Manus' significa 'mano' en latín.")
        recompensas.append("Estatuilla de Minerva: Conocimiento de raíces latinas")
    else:
        print("Respuesta incorrecta. La raíz es 'manus'.🤔🤔⚡😄")

# Menú de desafíos
def realizar_desafio():
    print("\nElige un desafío🤔:")
    print("1. 📟🌟📌Desafío de Virgilio (Poesía)")
    print("2. 📟🌟📌Desafío de Cicerón (Oratoria)")
    print("3. 📟🌟📌Desafío de Minerva👋 (Etimología)")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        desafio_virgilio()
    elif opcion == "2":
        desafio_ciceron()
    elif opcion == "3":
        desafio_minerva()
    else:
        print("Opción no válida. Vuelve a intentarlo.📟🤔🤔⚡😄")

# Recompensas
recompensas = []

def ver_recompensas():
    if recompensas:
        print("\nTus recompensas:")
        for recompensa in recompensas:
            print(f"- {recompensa}")
    else:
        print("\nAún no tienes recompensas. Completa desafíos para obtenerlas📟🤔.")

# Juego principal
def juego():
    bienvenida()
    while True:
        menu_principal()
        opcion = input("Selecciona una opción🤔: ")
        if opcion == "1":
            conocer_personajes()
        elif opcion == "2":
            realizar_desafio()
        elif opcion == "3":
            ver_recompensas()
        elif opcion == "4":
            print("🏛️ ¡Gracias por jugar! ¡Ave Roma!🏛️ ")
            break
        else:
            print("Opción no válida. Intenta de nuevo.🤔🤔⚡😄")

# Iniciar el juego
juego()
