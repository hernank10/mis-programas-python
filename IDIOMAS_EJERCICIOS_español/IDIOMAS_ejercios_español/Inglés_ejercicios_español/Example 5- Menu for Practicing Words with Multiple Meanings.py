def show_menu():
    print("1. Practice words with multiple meanings")
    print("2. Exit")

def practice_multiple_meanings():
    words = {
        "cabeza": ["Upper part of the body", "Leader of a group"],
        "lengua": ["Muscular organ in the mouth", "Language"],
        "ojo": ["Organ of vision", "Eye of a needle"]
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
            practice_multiple_meanings()
        elif option == "2":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
