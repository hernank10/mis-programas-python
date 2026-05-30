def afficher_menu():
    print("1. Pratiquer les antonymes")
    print("2. Quitter")

def pratiquer_antonymes():
    mots = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for mot, antonymes in mots.items():
        print(f"Mot : {mot}")
        print(f"Antonymes : {', '.join(antonymes)}")
        print()

def main():
    while True:
        afficher_menu()
        option = input("Sélectionnez une option : ")
        if option == "1":
            pratiquer_antonymes()
        elif option == "2":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
