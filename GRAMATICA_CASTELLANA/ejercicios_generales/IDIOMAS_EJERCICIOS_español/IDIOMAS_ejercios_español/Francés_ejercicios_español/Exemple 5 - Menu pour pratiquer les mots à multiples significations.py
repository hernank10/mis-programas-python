def afficher_menu():
    print("1. Pratiquer les mots à multiples significations")
    print("2. Quitter")

def pratiquer_multiples_significations():
    mots = {
        "cabeza": ["Partie supérieure du corps", "Chef d'un groupe"],
        "lengua": ["Organe musculaire dans la bouche", "Langue"],
        "ojo": ["Organe de la vision", "Chas d'une aiguille"]
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
            pratiquer_multiples_significations()
        elif option == "2":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
