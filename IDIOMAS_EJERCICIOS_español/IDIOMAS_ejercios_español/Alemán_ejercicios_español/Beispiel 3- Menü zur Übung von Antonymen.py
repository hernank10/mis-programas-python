def zeige_menu():
    print("1. Antonyme üben")
    print("2. Beenden")

def uebe_antonyme():
    woerter = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for wort, antonyme in woerter.items():
        print(f"Wort: {wort}")
        print(f"Antonyme: {', '.join(antonyme)}")
        print()

def main():
    while True:
        zeige_menu()
        option = input("Wählen Sie eine Option: ")
        if option == "1":
            uebe_antonyme()
        elif option == "2":
            break
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
