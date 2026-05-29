def afficher_menu():
    print("1. Pratiquer les mots polysémiques")
    print("2. Quitter")

def pratiquer_polysemies():
    mots = {
        "banco": ["Banc pour plusieurs personnes", "Institution financière"],
        "carta": ["Document écrit", "Carte à jouer"],
        "corte": ["Action de couper", "Tribunal de justice"]
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
            pratiquer_polysemies()
        elif option == "2":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
