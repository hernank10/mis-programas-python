import random
import os

# Datos de los ejercicios
EJERCICIOS = {
    "cazador": [
        {"es": "El sol calienta la tierra.", "en": "The sun heats the earth.", "sujeto_es": "El sol", "predicado_es": "calienta la tierra", "sujeto_en": "The sun", "predicado_en": "heats the earth"},
        {"es": "Mi hermana lee un libro.", "en": "My sister reads a book.", "sujeto_es": "Mi hermana", "predicado_es": "lee un libro", "sujeto_en": "My sister", "predicado_en": "reads a book"},
        {"es": "El perro duerme tranquilamente.", "en": "The dog sleeps peacefully.", "sujeto_es": "El perro", "predicado_es": "duerme tranquilamente", "sujeto_en": "The dog", "predicado_en": "sleeps peacefully"},
        {"es": "Los estudiantes estudian mucho.", "en": "The students study a lot.", "sujeto_es": "Los estudiantes", "predicado_es": "estudian mucho", "sujeto_en": "The students", "predicado_en": "study a lot"},
        {"es": "El tren llega a la estación.", "en": "The train arrives at the station.", "sujeto_es": "El tren", "predicado_es": "llega a la estación", "sujeto_en": "The train", "predicado_en": "arrives at the station"},
        {"es": "Ella canta una canción hermosa.", "en": "She sings a beautiful song.", "sujeto_es": "Ella", "predicado_es": "canta una canción hermosa", "sujeto_en": "She", "predicado_en": "sings a beautiful song"},
        {"es": "Nosotros vamos al cine.", "en": "We go to the movies.", "sujeto_es": "Nosotros", "predicado_es": "vamos al cine", "sujeto_en": "We", "predicado_en": "go to the movies"},
        {"es": "Tú escribes una carta.", "en": "You write a letter.", "sujeto_es": "Tú", "predicado_es": "escribes una carta", "sujeto_en": "You", "predicado_en": "write a letter"},
        {"es": "Ellos juegan fútbol.", "en": "They play soccer.", "sujeto_es": "Ellos", "predicado_es": "juegan fútbol", "sujeto_en": "They", "predicado_en": "play soccer"},
        {"es": "El pájaro vuela alto.", "en": "The bird flies high.", "sujeto_es": "El pájaro", "predicado_es": "vuela alto", "sujeto_en": "The bird", "predicado_en": "flies high"},
        {"es": "El agua fluye por el río.", "en": "Water flows through the river.", "sujeto_es": "El agua", "predicado_es": "fluye por el río", "sujeto_en": "Water", "predicado_en": "flows through the river"},
        {"es": "Mi padre repara el coche.", "en": "My father repairs the car.", "sujeto_es": "Mi padre", "predicado_es": "repara el coche", "sujeto_en": "My father", "predicado_en": "repairs the car"},
        {"es": "La luna brilla en la noche.", "en": "The moon shines at night.", "sujeto_es": "La luna", "predicado_es": "brilla en la noche", "sujeto_en": "The moon", "predicado_en": "shines at night"},
        {"es": "El bebé llora mucho.", "en": "The baby cries a lot.", "sujeto_es": "El bebé", "predicado_es": "llora mucho", "sujeto_en": "The baby", "predicado_en": "cries a lot"},
        {"es": "Los chefs cocinan la cena.", "en": "The chefs cook dinner.", "sujeto_es": "Los chefs", "predicado_es": "cocinan la cena", "sujeto_en": "The chefs", "predicado_en": "cook dinner"},
        {"es": "La maestra enseña matemáticas.", "en": "The teacher teaches math.", "sujeto_es": "La maestra", "predicado_es": "enseña matemáticas", "sujeto_en": "The teacher", "predicado_en": "teaches math"},
        {"es": "El artista pinta un cuadro.", "en": "The artist paints a picture.", "sujeto_es": "El artista", "predicado_es": "pinta un cuadro", "sujeto_en": "The artist", "predicado_en": "paints a picture"},
        {"es": "El conductor maneja el autobús.", "en": "The driver drives the bus.", "sujeto_es": "El conductor", "predicado_es": "maneja el autobús", "sujeto_en": "The driver", "predicado_en": "drives the bus"},
        {"es": "El doctor cura al paciente.", "en": "The doctor cures the patient.", "sujeto_es": "El doctor", "predicado_es": "cura al paciente", "sujeto_en": "The doctor", "predicado_en": "cures the patient"},
        {"es": "Mi abuela prepara el desayuno.", "en": "My grandmother prepares breakfast.", "sujeto_es": "Mi abuela", "predicado_es": "prepara el desayuno", "sujeto_en": "My grandmother", "predicado_en": "prepares breakfast"}
    ],
    "puzzle": [
        {"es": "El perro persigue al gato.", "en": "The dog chases the cat."},
        {"es": "La profesora enseña a los estudiantes.", "en": "The teacher teaches the students."},
        {"es": "Mi hermano juega con la pelota.", "en": "My brother plays with the ball."},
        {"es": "El sol brilla en el cielo.", "en": "The sun shines in the sky."},
        {"es": "Ella lee un libro interesante.", "en": "She reads an interesting book."},
        {"es": "Nosotros viajamos en un coche.", "en": "We travel in a car."},
        {"es": "Los pájaros cantan por la mañana.", "en": "The birds sing in the morning."},
        {"es": "El chef cocina una deliciosa sopa.", "en": "The chef cooks a delicious soup."},
        {"es": "Tú escribes una historia.", "en": "You write a story."},
        {"es": "Los niños construyen un castillo de arena.", "en": "The children build a sandcastle."},
        {"es": "El tren llega a la estación a tiempo.", "en": "The train arrives at the station on time."},
        {"es": "La luna ilumina la noche.", "en": "The moon illuminates the night."},
        {"es": "Él corre muy rápido en la pista.", "en": "He runs very fast on the track."},
        {"es": "El bebé duerme en su cuna.", "en": "The baby sleeps in his crib."},
        {"es": "Mi madre hornea galletas.", "en": "My mother bakes cookies."},
        {"es": "El gato maúlla en el tejado.", "en": "The cat meows on the roof."},
        {"es": "Ellas bailan en la fiesta.", "en": "They dance at the party."},
        {"es": "El doctor ayuda a la gente.", "en": "The doctor helps people."},
        {"es": "La flor florece en la primavera.", "en": "The flower blooms in the spring."},
        {"es": "El viento sopla fuerte.", "en": "The wind blows hard."}
    ]
}

def clear_screen():
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Muestra el menú principal y maneja la selección del usuario."""
    while True:
        clear_screen()
        print("--- 🎮 Menú de Juegos Sintácticos Ampliado 🎮 ---")
        print("1. Cazador de Sujeto y Predicado 🎯")
        print("2. El Puzzle de la Oración 🧩")
        print("3. Salir 🚪")
        
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "1":
            jugar_cazador()
        elif opcion == "2":
            jugar_puzzle()
        elif opcion == "3":
            print("¡Hasta la próxima! 👋")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar...")

def jugar_cazador():
    """Ejecuta una ronda del juego Cazador de Sujeto y Predicado."""
    ejercicios_disponibles = EJERCICIOS["cazador"].copy()
    random.shuffle(ejercicios_disponibles)
    
    for i, ejercicio in enumerate(ejercicios_disponibles):
        clear_screen()
        print(f"--- Cazador de Sujeto y Predicado (Ejercicio {i+1} de 20) ---")
        
        idioma = input("Selecciona un idioma (es/en): ").lower()
        
        if idioma == "es":
            frase = ejercicio["es"]
            sujeto_correcto = ejercicio["sujeto_es"]
            predicado_correcto = ejercicio["predicado_es"]
            print(f"Oración: {frase}\n")
            
            sujeto_ingresado = input("Identifica el Sujeto: ")
            predicado_ingresado = input("Identifica el Predicado: ")
            
            if sujeto_ingresado.lower().strip() == sujeto_correcto.lower().strip() and predicado_ingresado.lower().strip() == predicado_correcto.lower().strip():
                print("¡Correcto! ✅ Has identificado ambos correctamente.")
            else:
                print(f"Incorrecto ❌. El sujeto es: '{sujeto_correcto}' y el predicado es: '{predicado_correcto}'.")

        elif idioma == "en":
            frase = ejercicio["en"]
            sujeto_correcto = ejercicio["sujeto_en"]
            predicado_correcto = ejercicio["predicado_en"]
            print(f"Sentence: {frase}\n")
            
            sujeto_ingresado = input("Identify the Subject: ")
            predicado_ingresado = input("Identify the Predicate: ")
            
            if sujeto_ingresado.lower().strip() == sujeto_correcto.lower().strip() and predicado_ingresado.lower().strip() == predicado_correcto.lower().strip():
                print("Correct! ✅ You identified both correctly.")
            else:
                print(f"Incorrect ❌. The subject is: '{sujeto_correcto}' and the predicate is: '{predicado_correcto}'.")
        
        else:
            print("Idioma no válido.")
            input("Presiona Enter para continuar...")
            continue
            
        input("\nPresiona Enter para continuar con el siguiente ejercicio...")
    
    print("\n¡Has completado todos los ejercicios! 🎉")
    input("Presiona Enter para volver al menú...")

def jugar_puzzle():
    """Ejecuta una ronda del juego El Puzzle de la Oración."""
    ejercicios_disponibles = EJERCICIOS["puzzle"].copy()
    random.shuffle(ejercicios_disponibles)
    
    for i, ejercicio in enumerate(ejercicios_disponibles):
        clear_screen()
        print(f"--- El Puzzle de la Oración (Ejercicio {i+1} de 20) ---")
        
        idioma = input("Selecciona un idioma (es/en): ").lower()
        
        if idioma == "es":
            frase_correcta = ejercicio["es"]
            palabras = frase_correcta.split()
            random.shuffle(palabras)
            
            print("Ordena las siguientes palabras para formar una oración correcta:")
            print(" ".join(palabras))
            
            respuesta = input("Escribe la oración ordenada: ")
            
            if respuesta.lower().strip() == frase_correcta.lower().strip():
                print("¡Felicidades! 🎉 Has resuelto el puzzle correctamente.")
            else:
                print(f"Incorrecto ❌. La oración correcta es: '{frase_correcta}'.")
                
        elif idioma == "en":
            frase_correcta = ejercicio["en"]
            palabras = frase_correcta.split()
            random.shuffle(palabras)
            
            print("Order the following words to form a correct sentence:")
            print(" ".join(palabras))
            
            respuesta = input("Type the ordered sentence: ")
            
            if respuesta.lower().strip() == frase_correcta.lower().strip():
                print("Congratulations! 🎉 You solved the puzzle correctly.")
            else:
                print(f"Incorrect ❌. The correct sentence is: '{frase_correcta}'.")
                
        else:
            print("Idioma no válido.")
            input("Presiona Enter para continuar...")
            continue
            
        input("\nPresiona Enter para continuar con el siguiente ejercicio...")
        
    print("\n¡Has completado todos los ejercicios! 🎉")
    input("Presiona Enter para volver al menú...")

if __name__ == "__main__":
    menu()
