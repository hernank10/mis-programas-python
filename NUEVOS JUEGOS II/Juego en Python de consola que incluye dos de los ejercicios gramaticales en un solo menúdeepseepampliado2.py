import random
import os

# Data for all games
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
    ],
    "corrector": [
        {"es": "La casa es muy grandes.", "es_correcta": "La casa es muy grande.", "es_incorrectas": ["La casas es muy grande.", "El casa es muy grande.", "Las casa es muy grande."],
         "en": "The houses is very big.", "en_correcta": "The house is very big.", "en_incorrectas": ["The house are very big.", "The houses are very big.", "The house is very bigs."]},
        {"es": "Mis amigos irán a la playa.", "es_correcta": "Mis amigos irán a la playa.", "es_incorrectas": ["Mi amigos irán a la playa.", "Mis amigas irán a la playa.", "Mi amigas irán a la playa."],
         "en": "My friend go to the beach.", "en_correcta": "My friend goes to the beach.", "en_incorrectas": ["My friends goes to the beach.", "My friend going to the beach.", "My friends go to the beach."]},
        {"es": "Yo no tengo dinero, pero necesito comprar comida.", "es_correcta": "Yo no tengo dinero, pero necesito comprar comida.", "es_incorrectas": ["Yo no tengo dinero, porque necesito comprar comida.", "Yo no tengo dinero, o necesito comprar comida.", "Yo no tengo dinero, entonces necesito comprar comida."],
         "en": "I dont have money, and I need to buy food.", "en_correcta": "I don't have money, but I need to buy food.", "en_incorrectas": ["I have not money, and I need to buy food.", "I dont have money, so I need to buy food.", "I dont has money, but I need to buy food."]},
        {"es": "Cuando yo comí el pastel, me dio dolor de estómago.", "es_correcta": "Cuando yo comí el pastel, me dio dolor de estómago.", "es_incorrectas": ["Cuando yo como el pastel, me dio dolor de estómago.", "Cuando yo comer el pastel, me dio dolor de estómago.", "Cuando yo comía el pastel, me dio dolor de estómago."],
         "en": "When I ate the cake, I got a stomachache.", "en_correcta": "When I ate the cake, I got a stomachache.", "en_incorrectas": ["When I eat the cake, I got a stomachache.", "When I eating the cake, I got a stomachache.", "When I did eat the cake, I got a stomachache."]},
        {"es": "El libro que me prestaste, lo leí anoche.", "es_correcta": "El libro que me prestaste, lo leí anoche.", "es_incorrectas": ["El libro cual me prestaste, lo leí anoche.", "El libro cual me prestaste, lo leí anoche.", "El libro que me prestaste, lo lei anoche."],
         "en": "The book what you lent me, I read it last night.", "en_correcta": "The book that you lent me, I read it last night.", "en_incorrectas": ["The book which you lent me, I read it last night.", "The book who you lent me, I read it last night.", "The book where you lent me, I read it last night."]},
        {"es": "Mi amigo y yo vamos al cine.", "es_correcta": "Mi amigo y yo vamos al cine.", "es_incorrectas": ["Mi amigo y yo iré al cine.", "Mi amigo y yo iremos al cine.", "Mi amiga y yo vamos al cine."],
         "en": "My friend and I am going to the movies.", "en_correcta": "My friend and I are going to the movies.", "en_incorrectas": ["My friend and me are going to the movies.", "My friend and I is going to the movies.", "Me and my friend are going to the movies."]},
        {"es": "La niña canta muy bien.", "es_correcta": "La niña canta muy bien.", "es_incorrectas": ["La niña cantas muy bien.", "El niña canta muy bien.", "La niña canta muy bueno."],
         "en": "The girl sing very good.", "en_correcta": "The girl sings very well.", "en_incorrectas": ["The girl sings very good.", "The girl singing very well.", "The girls sings very well."]},
        {"es": "Ellos vieron la película en casa.", "es_correcta": "Ellos vieron la película en casa.", "es_incorrectas": ["Ellos ven la película en casa.", "Ellos vio la película en casa.", "Ellos vieron la pelicula en casa."],
         "en": "They saw the movie at home.", "en_correcta": "They saw the movie at home.", "en_incorrectas": ["They see the movie at home.", "They seen the movie at home.", "They sees the movie at home."]},
        {"es": "El coche rojo es mío.", "es_correcta": "El coche rojo es mío.", "es_incorrectas": ["El coche rojo son mío.", "Los coche rojo es mío.", "El coche rojo es mió."],
         "en": "The red car is mines.", "en_correcta": "The red car is mine.", "en_incorrectas": ["The red car are mine.", "The red car is my.", "The red cars is mine."]},
        {"es": "Quiero que tú vengas conmigo.", "es_correcta": "Quiero que tú vengas conmigo.", "es_incorrectas": ["Quiero que tú ven conmigo.", "Quiero que tú vienes conmigo.", "Quiero que tú vas conmigo."],
         "en": "I want you to came with me.", "en_correcta": "I want you to come with me.", "en_incorrectas": ["I want you coming with me.", "I want you to comes with me.", "I want you to went with me."]},
        {"es": "El libro está sobre la mesa.", "es_correcta": "El libro está sobre la mesa.", "es_incorrectas": ["El libro están sobre la mesa.", "El libro esta sobre la mesa.", "El libros está sobre la mesa."],
         "en": "The book is on the table.", "en_correcta": "The book is on the table.", "en_incorrectas": ["The book are on the table.", "The books is on the table.", "The book is in the table."]},
        {"es": "Ayer fui al supermercado y compré fruta.", "es_correcta": "Ayer fui al supermercado y compré fruta.", "es_incorrectas": ["Ayer fui al supermercado y compra fruta.", "Ayer fue al supermercado y compré fruta.", "Ayer fui al supermercado y compre fruta."],
         "en": "Yesterday I went to the supermarket and buy fruit.", "en_correcta": "Yesterday I went to the supermarket and bought fruit.", "en_incorrectas": ["Yesterday I went to the supermarket and boughts fruit.", "Yesterday I goed to the supermarket and buy fruit.", "Yesterday I went to the supermarket and buying fruit."]},
        {"es": "A mi me gusta el chocolate.", "es_correcta": "Me gusta el chocolate.", "es_incorrectas": ["A mí gusta el chocolate.", "A mi me gustan el chocolate.", "Me gustan el chocolate."],
         "en": "To me I like chocolate.", "en_correcta": "I like chocolate.", "en_incorrectas": ["To me I likes chocolate.", "Me like chocolate.", "I likes chocolate."]},
        {"es": "Ella corre rápido.", "es_correcta": "Ella corre rápido.", "es_incorrectas": ["Ella corren rápido.", "Ella corre rápido.", "El corre rápido."],
         "en": "She runs fast.", "en_correcta": "She runs fast.", "en_incorrectas": ["She run fast.", "She running fast.", "They runs fast."]},
        {"es": "Los niños juegan al fútbol.", "es_correcta": "Los niños juegan al fútbol.", "es_incorrectas": ["Los niños juegan el fútbol.", "Los niños juegan fútbol.", "Los niños juegan al futbol."],
         "en": "The children play the soccer.", "en_correcta": "The children play soccer.", "en_incorrectas": ["The childrens play soccer.", "The children plays soccer.", "The children play a soccer."]},
        {"es": "Mi casa es más grande que la tuya.", "es_correcta": "Mi casa es más grande que la tuya.", "es_incorrectas": ["Mi casa es más grande que tuya.", "Mi casa es mas grande que la tuya.", "Mi casa es más grandes que la tuya."],
         "en": "My house is more bigger than yours.", "en_correcta": "My house is bigger than yours.", "en_incorrectas": ["My house are more bigger than yours.", "My house is more bigger than you.", "My house is more big than yours."]},
        {"es": "El agua de este vaso.", "es_correcta": "El agua de este vaso.", "es_incorrectas": ["El agua de esta vaso.", "El agua de este vasa.", "El agua del este vaso."],
         "en": "The water of this glass.", "en_correcta": "The water in this glass.", "en_incorrectas": ["The water on this glass.", "The water into this glass.", "The water of this glasses."]},
        {"es": "El hombre que trabaja conmigo.", "es_correcta": "El hombre que trabaja conmigo.", "es_incorrectas": ["El hombre quién trabaja conmigo.", "El hombre quien trabaja conmigo.", "El hombre que trabaja con mi."],
         "en": "The man who work with me.", "en_correcta": "The man who works with me.", "en_incorrectas": ["The man which works with me.", "The man which work with me.", "The man who work with I."]},
        {"es": "Por favor, dame el libro.", "es_correcta": "Por favor, dame el libro.", "es_incorrectas": ["Por favor, dame libro.", "Por favor, da me el libro.", "Porfavor, dame el libro."],
         "en": "Please, gives me the book.", "en_correcta": "Please, give me the book.", "en_incorrectas": ["Please, give to me the book.", "Please, giving me the book.", "Please, gave me the book."]},
        {"es": "Los perros son animales.", "es_correcta": "Los perros son animales.", "es_incorrectas": ["Los perros son animales.", "Los perros es un animal.", "Los perros es animales."],
         "en": "The dogs is animals.", "en_correcta": "The dogs are animals.", "en_incorrectas": ["The dog are animals.", "The dogs is animal.", "The dog is animals."]}
    ],
    "constructor": [
        {"es": ["El", "perro", "persigue", "al", "gato", "."], "en": ["The", "dog", "chases", "the", "cat", "."]},
        {"es": ["Mi", "mamá", "cocina", "un", "pastel", "."], "en": ["My", "mom", "cooks", "a", "cake", "."]},
        {"es": ["El", "sol", "calienta", "la", "tierra", "."], "en": ["The", "sun", "heats", "the", "earth", "."]},
        {"es": ["Los", "niños", "juegan", "en", "el", "parque", "."], "en": ["The", "children", "play", "in", "the", "park", "."]},
        {"es": ["Ella", "lee", "un", "libro", "cada", "noche", "."], "en": ["She", "reads", "a", "book", "every", "night", "."]},
        {"es": ["Nosotros", "viajamos", "en", "avión", "."], "en": ["We", "travel", "by", "plane", "."]},
        {"es": ["La", "luna", "brilla", "en", "la", "noche", "."], "en": ["The", "moon", "shines", "at", "night", "."]},
        {"es": ["Ellos", "compran", "frutas", "en", "el", "mercado", "."], "en": ["They", "buy", "fruits", "at", "the", "market", "."]},
        {"es": ["El", "profesor", "explica", "la", "lección", "."], "en": ["The", "teacher", "explains", "the", "lesson", "."]},
        {"es": ["Yo", "escribo", "una", "carta", "a", "mi", "amigo", "."], "en": ["I", "write", "a", "letter", "to", "my", "friend", "."]},
        {"es": ["El", "tren", "llega", "a", "la", "estación", "."], "en": ["The", "train", "arrives", "at", "the", "station", "."]},
        {"es": ["La", "flor", "crece", "en", "el", "jardín", "."], "en": ["The", "flower", "grows", "in", "the", "garden", "."]},
        {"es": ["El", "avión", "vuela", "sobre", "las", "montañas", "."], "en": ["The", "plane", "flies", "over", "the", "mountains", "."]},
        {"es": ["El", "coche", "corre", "muy", "rápido", "."], "en": ["The", "car", "runs", "very", "fast", "."]},
        {"es": ["Las", "estrellas", "brillan", "en", "el", "cielo", "."], "en": ["The", "stars", "shine", "in", "the", "sky", "."]},
        {"es": ["Tú", "comes", "una", "manzana", "roja", "."], "en": ["You", "eat", "a", "red", "apple", "."]},
        {"es": ["La", "computadora", "tiene", "un", "virus", "."], "en": ["The", "computer", "has", "a", "virus", "."]},
        {"es": ["El", "estudiante", "estudia", "para", "su", "examen", "."], "en": ["The", "student", "studies", "for", "his", "exam", "."]},
        {"es": ["Mi", "abuela", "prepara", "la", "cena", "."], "en": ["My", "grandmother", "prepares", "the", "dinner", "."]},
        {"es": ["El", "agua", "fluye", "por", "el", "río", "."], "en": ["The", "water", "flows", "through", "the", "river", "."]}
    ]
}


def clear_screen():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Displays the main menu and handles user selection."""
    while True:
        clear_screen()
        print("--- 🎮 Main Syntax Games Menu 🎮 ---")
        print("1. Subject & Predicate Hunter 🎯")
        print("2. The Sentence Puzzle 🧩")
        print("3. The Sentence Corrector ✅")
        print("4. Build Your Own Sentence 🏗️")
        print("5. Exit 🚪")
        
        opcion = input("\nSelect an option (1-5): ")
        
        if opcion == "1":
            jugar_cazador()
        elif opcion == "2":
            jugar_puzzle()
        elif opcion == "3":
            jugar_corrector()
        elif opcion == "4":
            jugar_constructor()
        elif opcion == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")

def jugar_cazador():
    """Runs a round of the Subject & Predicate Hunter game."""
    ejercicios_disponibles = EJERCICIOS["cazador"].copy()
    random.shuffle(ejercicios_disponibles)
    
    for i, ejercicio in enumerate(ejercicios_disponibles):
        clear_screen()
        print(f"--- Subject & Predicate Hunter (Exercise {i+1} of 20) ---")
        
        idioma = input("Select a language (es/en): ").lower()
        
        if idioma == "es":
            frase = ejercicio["es"]
            sujeto_correcto = ejercicio["sujeto_es"]
            predicado_correcto = ejercicio["predicado_es"]
            print(f"Sentence: {frase}\n")
            
            sujeto_ingresado = input("Identify the Subject: ")
            predicado_ingresado = input("Identify the Predicate: ")
            
            if sujeto_ingresado.lower().strip() == sujeto_correcto.lower().strip() and predicado_ingresado.lower().strip() == predicado_correcto.lower().strip():
                print("Correct! ✅ You identified both correctly.")
            else:
                print(f"Incorrect ❌. The subject is: '{sujeto_correcto}' and the predicate is: '{predicado_correcto}'.")

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
            print("Invalid language.")
            input("Press Enter to continue...")
            continue
            
        input("\nPress Enter to continue with the next exercise...")
    
    print("\nYou have completed all exercises! 🎉")
    input("Press Enter to return to the menu...")

def jugar_puzzle():
    """Runs a round of The Sentence Puzzle game."""
    ejercicios_disponibles = EJERCICIOS["puzzle"].copy()
    random.shuffle(ejercicios_disponibles)
    
    for i, ejercicio in enumerate(ejercicios_disponibles):
        clear_screen()
        print(f"--- The Sentence Puzzle (Exercise {i+1} of 20) ---")
        
        idioma = input("Select a language (es/en): ").lower()
        
        if idioma == "es":
            frase_correcta = ejercicio["es"]
            palabras = frase_correcta.split()
            random.shuffle(palabras)
            
            print("Order the following words to form a correct sentence:")
            print(" ".join(palabras))
            
            respuesta = input("Type the ordered sentence: ")
            
            if respuesta.lower().strip() == frase_correcta.lower().strip():
                print("Congratulations! 🎉 You solved the puzzle correctly.")
            else:
                print(f"Incorrect ❌. The correct sentence is: '{frase_correcta}'.")
                
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
            print("Invalid language.")
            input("Press Enter to continue...")
            continue
            
        input("\nPress Enter to continue with the next exercise...")
        
    print("\nYou have completed all exercises! 🎉")
    input("Press Enter to return to the menu...")

def jugar_corrector():
    """Runs a round of The Sentence Corrector game."""
    ejercicios_disponibles = EJERCICIOS["corrector"].copy()
    random.shuffle(ejercicios_disponibles)
    
    for i, ejercicio in enumerate(ejercicios_disponibles):
        clear_screen()
        print(f"--- The Sentence Corrector (Exercise {i+1} of 20) ---")
        
        idioma = input("Select a language (es/en): ").lower()
        
        if idioma == "es":
            frase_incorrecta = ejercicio["es"]
            correcta = ejercicio["es_correcta"]
            opciones = [correcta] + ejercicio["es_incorrectas"]
            random.shuffle(opciones)
            
            print(f"Correct the following sentence:\n'{frase_incorrecta}'\n")
            
            for j, opcion in enumerate(opciones):
                print(f"{j+1}. {opcion}")
            
            try:
                respuesta = int(input("Select the correct option (1-4): "))
                if opciones[respuesta-1] == correcta:
                    print("¡Correcto! ✅")
                else:
                    print(f"Incorrecto ❌. La opción correcta era: '{correcta}'.")
            except (ValueError, IndexError):
                print("Respuesta no válida.")

        elif idioma == "en":
            frase_incorrecta = ejercicio["en"]
            correcta = ejercicio["en_correcta"]
            opciones = [correcta] + ejercicio["en_incorrectas"]
            random.shuffle(opciones)
            
            print(f"Correct the following sentence:\n'{frase_incorrecta}'\n")
            
            for j, opcion in enumerate(opciones):
                print(f"{j+1}. {opcion}")
            
            try:
                respuesta = int(input("Select the correct option (1-4): "))
                if opciones[respuesta-1] == correcta:
                    print("Correct! ✅")
                else:
                    print(f"Incorrect ❌. The correct option was: '{correcta}'.")
            except (ValueError, IndexError):
                print("Invalid response.")
        
        else:
            print("Invalid language.")
            input("Press Enter to continue...")
            continue
            
        input("\nPress Enter to continue with the next exercise...")
    
    print("\nYou have completed all exercises! 🎉")
    input("Press Enter to return to the menu...")

def jugar_constructor():
    """Runs a round of the Build Your Own Sentence game."""
    ejercicios_disponibles = EJERCICIOS["constructor"].copy()
    random.shuffle(ejercicios_disponibles)

    for i, ejercicio in enumerate(ejercicios_disponibles):
        clear_screen()
        print(f"--- Build Your Own Sentence (Exercise {i+1} of 20) ---")
        
        idioma = input("Select a language (es/en): ").lower()
        
        if idioma == "es":
            frase_correcta_lista = ejercicio["es"]
            frase_correcta_str = " ".join(frase_correcta_lista)
            palabras_desordenadas = frase_correcta_lista.copy()
            random.shuffle(palabras_desordenadas)
            
            print("Build a correct sentence using the following words:")
            print(", ".join(palabras_desordenadas))
            
            print("\nEnter the words one by one in the correct order. Press Enter after each word. Type 'DONE' when you are finished.")
            
            respuesta_lista = []
            while True:
                palabra = input(f"Word {len(respuesta_lista) + 1}: ").strip()
                if palabra.lower() == 'done':
                    break
                respuesta_lista.append(palabra)
            
            respuesta_str = " ".join(respuesta_lista)

            if respuesta_str.lower() == frase_correcta_str.lower():
                print("Congratulations! 🎉 You built the sentence correctly.")
            else:
                print(f"Incorrect ❌. The correct sentence was: '{frase_correcta_str}'.")

        elif idioma == "en":
            frase_correcta_lista = ejercicio["en"]
            frase_correcta_str = " ".join(frase_correcta_lista)
            palabras_desordenadas = frase_correcta_lista.copy()
            random.shuffle(palabras_desordenadas)

            print("Build a correct sentence using the following words:")
            print(", ".join(palabras_desordenadas))

            print("\nEnter the words one by one in the correct order. Press Enter after each word. Type 'DONE' when you are finished.")

            respuesta_lista = []
            while True:
                palabra = input(f"Word {len(respuesta_lista) + 1}: ").strip()
                if palabra.lower() == 'done':
                    break
                respuesta_lista.append(palabra)
            
            respuesta_str = " ".join(respuesta_lista)

            if respuesta_str.lower() == frase_correcta_str.lower():
                print("Congratulations! 🎉 You built the sentence correctly.")
            else:
                print(f"Incorrect ❌. The correct sentence was: '{frase_correcta_str}'.")

        else:
            print("Invalid language.")
            input("Press Enter to continue...")
            continue
            
        input("\nPress Enter to continue with the next exercise...")
    
    print("\nYou have completed all exercises! 🎉")
    input("Press Enter to return to the menu...")

if __name__ == "__main__":
    menu()
