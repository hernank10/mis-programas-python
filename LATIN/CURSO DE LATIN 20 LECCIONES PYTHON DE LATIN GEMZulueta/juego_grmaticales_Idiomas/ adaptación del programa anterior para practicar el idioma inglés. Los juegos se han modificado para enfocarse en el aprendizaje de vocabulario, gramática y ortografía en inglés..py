import random

# Variables para almacenar el progreso del usuario
progreso = {
    "Hangman (Ahorcado)": 0,
    "Word Search (Sopa de letras)": 0,
    "Spelling Domino (Dominó ortográfico)": 0,
    "Word Bingo (Bingo de palabras)": 0,
    "Word Chain (Cadena de palabras)": 0
}

# Función para el juego de Hangman (Ahorcado)
def hangman():
    palabras = ["apple", "banana", "computer", "elephant", "guitar"]
    palabra = random.choice(palabras)
    adivinanza = ["_"] * len(palabra)
    intentos = 6
    letras_usadas = []

    print("\nWelcome to Hangman!")
    print(" ".join(adivinanza))

    while intentos > 0 and "_" in adivinanza:
        letra = input("Enter a letter: ").lower()

        if letra in letras_usadas:
            print("You've already used that letter. Try another one.")
            continue

        letras_usadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    adivinanza[i] = letra
            print("Correct!")
        else:
            intentos -= 1
            print(f"Incorrect. You have {intentos} attempts left.")

        print(" ".join(adivinanza))

    if "_" not in adivinanza:
        print("Congratulations! You've guessed the word.")
        progreso["Hangman (Ahorcado)"] += 1
    else:
        print(f"Oh no! The word was '{palabra}'. Better luck next time.")

# Función para el juego de Word Search (Sopa de letras)
def word_search():
    print("\nWelcome to Word Search!")
    print("Find the misspelled words and correct them.")
    # Aquí podrías implementar una sopa de letras interactiva
    print("(This game is under development).")
    progreso["Word Search (Sopa de letras)"] += 1

# Función para el juego de Spelling Domino (Dominó ortográfico)
def spelling_domino():
    print("\nWelcome to Spelling Domino!")
    print("Connect the tiles according to spelling rules.")
    # Aquí podrías implementar un dominó interactivo
    print("(This game is under development).")
    progreso["Spelling Domino (Dominó ortográfico)"] += 1

# Función para el juego de Word Bingo (Bingo de palabras)
def word_bingo():
    print("\nWelcome to Word Bingo!")
    print("Mark the correct words on your card.")
    # Aquí podrías implementar un bingo interactivo
    print("(This game is under development).")
    progreso["Word Bingo (Bingo de palabras)"] += 1

# Función para el juego de Word Chain (Cadena de palabras)
def word_chain():
    print("\nWelcome to Word Chain!")
    print("Continue the word chain without making spelling mistakes.")
    # Aquí podrías implementar una cadena de palabras interactiva
    print("(This game is under development).")
    progreso["Word Chain (Cadena de palabras)"] += 1

# Función para mostrar el progreso del usuario
def show_progress():
    print("\n--- Your Progress ---")
    for game, score in progreso.items():
        print(f"{game}: {score} points")
    input("\nPress Enter to return to the main menu.")

# Menú principal
def menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play Hangman")
        print("2. Play Word Search")
        print("3. Play Spelling Domino")
        print("4. Play Word Bingo")
        print("5. Play Word Chain")
        print("6. View Progress")
        print("7. Exit")

        option = input("Select an option: ")

        if option == "1":
            hangman()
        elif option == "2":
            word_search()
        elif option == "3":
            spelling_domino()
        elif option == "4":
            word_bingo()
        elif option == "5":
            word_chain()
        elif option == "6":
            show_progress()
        elif option == "7":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")

# Iniciar el programa
if __name__ == "__main__":
    menu()
