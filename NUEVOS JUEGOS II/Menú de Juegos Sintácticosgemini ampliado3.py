import random
import os

# Datos de los ejercicios
EJERCICIOS = [
    {
        "es": "No fui a la fiesta ____ estaba enfermo.",
        "opciones_es": ["porque", "sin embargo"],
        "correcta_es": "porque",
        "en": "I didn't go to the party ____ I was sick.",
        "opciones_en": ["because", "however"],
        "correcta_en": "because"
    },
    {
        "es": "Estudié mucho, ____ no pasé el examen.",
        "opciones_es": ["por lo tanto", "sin embargo"],
        "correcta_es": "sin embargo",
        "en": "I studied a lot, ____ I didn't pass the exam.",
        "opciones_en": ["therefore", "however"],
        "correcta_en": "however"
    },
    {
        "es": "Tenía frío, ____ me puse un abrigo.",
        "opciones_es": ["entonces", "además"],
        "correcta_es": "entonces",
        "en": "I was cold, ____ I put on a coat.",
        "opciones_en": ["so", "in addition"],
        "correcta_en": "so"
    },
    {
        "es": "Me gusta el café ____ no el té.",
        "opciones_es": ["ni", "pero"],
        "correcta_es": "pero",
        "en": "I like coffee ____ not tea.",
        "opciones_en": ["and", "but"],
        "correcta_en": "but"
    },
    {
        "es": "Ella es inteligente ____ graciosa.",
        "opciones_es": ["y", "o"],
        "correcta_es": "y",
        "en": "She is smart ____ funny.",
        "opciones_en": ["and", "or"],
        "correcta_en": "and"
    },
    {
        "es": "No sé si ir al cine ____ quedarme en casa.",
        "opciones_es": ["y", "o"],
        "correcta_es": "o",
        "en": "I don't know whether to go to the movies ____ stay home.",
        "opciones_en": ["and", "or"],
        "correcta_en": "or"
    },
    {
        "es": "Aprobé el curso ____ estudié mucho.",
        "opciones_es": ["a pesar de que", "porque"],
        "correcta_es": "porque",
        "en": "I passed the course ____ I studied hard.",
        "opciones_en": ["even though", "because"],
        "correcta_en": "because"
    },
    {
        "es": "Salió el sol, ____ aún hace frío.",
        "opciones_es": ["sin embargo", "entonces"],
        "correcta_es": "sin embargo",
        "en": "The sun came out, ____ it is still cold.",
        "opciones_en": ["however", "so"],
        "correcta_en": "however"
    },
    {
        "es": "Me gusta la pizza ____ el helado.",
        "opciones_es": ["y", "o"],
        "correcta_es": "y",
        "en": "I like pizza ____ ice cream.",
        "opciones_en": ["and", "or"],
        "correcta_en": "and"
    },
    {
        "es": "Tenía sueño, ____ me fui a la cama.",
        "opciones_es": ["por lo tanto", "además"],
        "correcta_es": "por lo tanto",
        "en": "I was sleepy, ____ I went to bed.",
        "opciones_en": ["therefore", "in addition"],
        "correcta_en": "therefore"
    },
    {
        "es": "El coche es viejo, ____ funciona bien.",
        "opciones_es": ["pero", "y"],
        "correcta_es": "pero",
        "en": "The car is old, ____ it runs well.",
        "opciones_en": ["but", "and"],
        "correcta_en": "but"
    },
    {
        "es": "No tenía hambre, ____ comí.",
        "opciones_es": ["así que", "pero"],
        "correcta_es": "pero",
        "en": "I wasn't hungry, ____ I ate.",
        "opciones_en": ["so", "but"],
        "correcta_en": "but"
    },
    {
        "es": "El proyecto fue difícil, ____ lo completamos.",
        "opciones_es": ["a pesar de que", "así que"],
        "correcta_es": "a pesar de que",
        "en": "The project was difficult, ____ we completed it.",
        "opciones_en": ["even though", "so"],
        "correcta_en": "even though"
    },
    {
        "es": "El perro es grande, ____ el gato es pequeño.",
        "opciones_es": ["mientras que", "porque"],
        "correcta_es": "mientras que",
        "en": "The dog is big, ____ the cat is small.",
        "opciones_en": ["while", "because"],
        "correcta_en": "while"
    },
    {
        "es": "Ganó la lotería, ____ es muy rico.",
        "opciones_es": ["a menos que", "por lo tanto"],
        "correcta_es": "por lo tanto",
        "en": "He won the lottery, ____ he is very rich.",
        "opciones_en": ["unless", "therefore"],
        "correcta_en": "therefore"
    },
    {
        "es": "Te llamaré ____ regrese a casa.",
        "opciones_es": ["antes de que", "tan pronto como"],
        "correcta_es": "tan pronto como",
        "en": "I will call you ____ I get home.",
        "opciones_en": ["before", "as soon as"],
        "correcta_en": "as soon as"
    },
    {
        "es": "No voy a ir ____ me invites.",
        "opciones_es": ["aunque", "a menos que"],
        "correcta_es": "a menos que",
        "en": "I'm not going ____ you invite me.",
        "opciones_en": ["even if", "unless"],
        "correcta_en": "unless"
    },
    {
        "es": "Ella es mi amiga, ____ la respeto.",
        "opciones_es": ["a pesar de", "y"],
        "correcta_es": "y",
        "en": "She is my friend, ____ I respect her.",
        "opciones_en": ["despite", "and"],
        "correcta_en": "and"
    },
    {
        "es": "El motor no enciende ____ no tiene gasolina.",
        "opciones_es": ["porque", "pero"],
        "correcta_es": "porque",
        "en": "The engine won't start ____ it has no gas.",
        "opciones_en": ["because", "but"],
        "correcta_en": "because"
    },
    {
        "es": "Mi casa está lejos, ____ iré caminando.",
        "opciones_es": ["no obstante", "por lo tanto"],
        "correcta_es": "no obstante",
        "en": "My house is far away, ____ I will walk.",
        "opciones_en": ["however", "therefore"],
        "correcta_en": "however"
    }
]

def clear_screen():
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def carrera_de_conectores():
    """Juego: Carrera de Conectores."""
    clear_screen()
    print("--- 🏁 Carrera de Conectores 🏁 ---")
    
    ejercicios_disponibles = EJERCICIOS.copy()
    random.shuffle(ejercicios_disponibles)
    
    puntaje = 0
    total_ejercicios = len(ejercicios_disponibles)
    
    for i, ejercicio in enumerate(ejercicios_disponibles):
        clear_screen()
        print(f"--- Ejercicio {i+1} de {total_ejercicios} ---")
        
        idioma = input("Selecciona un idioma (es/en): ").lower()
        
        if idioma == "es":
            frase = ejercicio["es"]
            opciones = ejercicio["opciones_es"]
            correcta = ejercicio["correcta_es"]
            
            print(f"Oración: {frase.replace('____', '______')}")
            print(f"Opciones: 1. {opciones[0]}   2. {opciones[1]}")
            
            try:
                respuesta = input("Elige 1 o 2: ")
                if opciones[int(respuesta)-1] == correcta:
                    print("¡Correcto! ✅ Avanzas un punto.")
                    puntaje += 1
                else:
                    print(f"Incorrecto ❌. La respuesta correcta era: '{correcta}'.")
            except (ValueError, IndexError):
                print("Respuesta no válida.")
                
        elif idioma == "en":
            frase = ejercicio["en"]
            opciones = ejercicio["opciones_en"]
            correcta = ejercicio["correcta_en"]
            
            print(f"Sentence: {frase.replace('____', '______')}")
            print(f"Options: 1. {opciones[0]}   2. {opciones[1]}")
            
            try:
                respuesta = input("Choose 1 or 2: ")
                if opciones[int(respuesta)-1] == correcta:
                    print("Correct! ✅ You gain a point.")
                    puntaje += 1
                else:
                    print(f"Incorrect ❌. The correct answer was: '{correcta}'.")
            except (ValueError, IndexError):
                print("Invalid response.")
        
        else:
            print("Idioma no válido.")
            input("Presiona Enter para continuar...")
            continue
            
        input("\nPresiona Enter para continuar...")
        
    print(f"\n¡Carrera terminada! 🎉")
    print(f"Tu puntaje final es: {puntaje} de {total_ejercicios}")
    input("Presiona Enter para volver al menú principal...")

# Esta es solo la función del juego. Puedes integrarla en el menú principal
# de tu programa anterior, agregando una nueva opción para "carrera_de_conectores".
# Por ejemplo:
# if opcion == "5":
#     carrera_de_conectores()
