def show_menu():
    print("1. Practice synonyms")
    print("2. Exit")

def practice_synonyms():
    words = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for word, synonyms in words.items():
        print(f"Word: {word}")
        print(f"Synonyms: {', '.join(synonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == "1":
            practice_synonyms()
        elif option == "2":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
