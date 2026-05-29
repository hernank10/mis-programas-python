def zeige_menu():
    print("1. Polyseme Wörter üben")
    print("2. Beenden")

def uebe_polysemie():
    woerter = {
        "banco": ["Bank für mehrere Personen", "Finanzinstitut"],
        "carta": ["Geschriebenes Dokument", "Spielkarte"],
        "corte": ["Aktion des Schneidens", "Gerichtshof"]
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
            uebe_polysemie()
        elif option == "2":
            break
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
