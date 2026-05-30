def show_menu():
    print("1. Practice antonyms")
    print("2. Exit")

def practice_antonyms():
    words = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for word, antonyms in words.items():
        print(f"Word: {word}")
        print(f"Antonyms: {', '.join(antonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == "1":
            practice_antonyms()
        elif option == "2":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
