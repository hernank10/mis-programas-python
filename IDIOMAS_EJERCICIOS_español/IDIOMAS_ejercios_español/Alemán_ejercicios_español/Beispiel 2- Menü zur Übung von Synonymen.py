def zeige_menu():
    print("1. Synonyme üben")
    print("2. Beenden")

def uebe_synonyme():
    woerter = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for wort, synonyme in woerter.items():
        print(f"Wort: {wort}")
        print(f"Synonyme: {', '.join(synonyme)}")
        print()

def main():
    while True:
        zeige_menu()
        option = input("Wählen Sie eine Option: ")
        if option == "1":
            uebe_synonyme()
        elif option == "2":
            break
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
