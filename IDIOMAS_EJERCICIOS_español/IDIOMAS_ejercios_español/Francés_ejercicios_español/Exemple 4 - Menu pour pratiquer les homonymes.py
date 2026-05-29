def afficher_menu():
    print("1. Pratiquer les homonymes")
    print("2. Quitter")

def pratiquer_homonymes():
    mots = {
        "vino": ["Boisson alcoolisée", "Passé du verbe 'venir'"],
        "llama": ["Animal sud-américain", "Flamme", "Forme du verbe 'llamar'"],
        "banco": ["Banc", "Institution financière"]
    }
    for mot, significations in mots.items():
        print(f"Mot : {mot}")
        for i, signification in enumerate(significations, 1):
            print(f"{i}. {signification}")
        print()

def main():
    while True:
        afficher_menu()
        option = input("Sélectionnez une option : ")
        if option == "1":
            pratiquer_homonymes()
        elif option == "2":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
