def show_menu():
    print("1. Practice polysemous words")
    print("2. Exit")

def practice_polysemies():
    words = {
        "banco": ["Seat for several people", "Financial institution"],
        "carta": ["Written document", "Playing card"],
        "corte": ["Action of cutting", "Court of justice"]
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
            practice_polysemies()
        elif option == "2":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
