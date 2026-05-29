def show_menu():
    print("1. Practice homonyms")
    print("2. Exit")

def practice_homonyms():
    words = {
        "vino": ["Alcoholic beverage", "Past tense of the verb 'venir'"],
        "llama": ["South American animal", "Fire", "Form of the verb 'llamar'"],
        "banco": ["Seat", "Financial institution"]
    }
    for word, meanings in words.items():
        print(f"Word: {word}")
        for i, meaning in enumerate(meanings, 1):
            print(f"{i}. {meaning}")
        print()

def main():
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == "1":
            practice_homonyms()
        elif option == "2":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
