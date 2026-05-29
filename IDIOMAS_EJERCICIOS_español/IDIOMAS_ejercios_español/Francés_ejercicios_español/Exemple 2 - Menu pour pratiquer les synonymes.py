def afficher_menu():
    print("1. Pratiquer les synonymes")
    print("2. Quitter")

def pratiquer_synonymes():
    mots = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for mot, synonymes in mots.items():
        print(f"Mot : {mot}")
        print(f"Synonymes : {', '.join(synonymes)}")
        print()

def main():
    while True:
        afficher_menu()
        option = input("Sélectionnez une option : ")
        if option == "1":
            pratiquer_synonymes()
        elif option == "2":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
