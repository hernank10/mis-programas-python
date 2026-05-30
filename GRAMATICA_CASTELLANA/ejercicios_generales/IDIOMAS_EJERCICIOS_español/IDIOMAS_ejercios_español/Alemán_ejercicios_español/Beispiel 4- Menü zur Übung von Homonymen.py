def zeige_menu():
    print("1. Homonyme üben")
    print("2. Beenden")

def uebe_homonyme():
    woerter = {
        "vino": ["Alkoholisches Getränk", "Vergangenheitsform des Verbs 'venir'"],
        "llama": ["Südamerikanisches Tier", "Flamme", "Form des Verbs 'llamar'"],
        "banco": ["Bank", "Finanzinstitut"]
    }
    for wort, bedeutungen in woerter.items():
        print(f"Wort: {wort}")
        for i, bedeutung in enumerate(bedeutungen, 1):
            print(f"{i}. {bedeutung}")
        print()

def main():
    while True:
        zeige_menu()
        option = input("Wählen Sie eine Option: ")
        if option == "1":
            uebe_homonyme()
        elif option == "2":
            break
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
