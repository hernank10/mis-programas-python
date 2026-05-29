def zeige_menu():
    print("1. Wörter mit mehreren Bedeutungen üben")
    print("2. Beenden")

def uebe_mehrfache_bedeutungen():
    woerter = {
        "cabeza": ["Oberer Teil des Körpers", "Leiter einer Gruppe"],
        "lengua": ["Muskelorgan im Mund", "Sprache"],
        "ojo": ["Sehorgan", "Nadelöhr"]
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
            uebe_mehrfache_bedeutungen()
        elif option == "2":
            break
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
