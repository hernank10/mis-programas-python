def mostra_menu():
    print("1. Praticare omonimi")
    print("2. Uscire")

def pratica_omonimi():
    parole = {
        "vino": ["Bevanda alcolica", "Passato del verbo 'venir'"],
        "llama": ["Animale sudamericano", "Fiamma", "Forma del verbo 'llamar'"],
        "banco": ["Panchina", "Istituto finanziario"]
    }
    for parola, significati in parole.items():
        print(f"Parola: {parola}")
        for i, significato in enumerate(significati, 1):
            print(f"{i}. {significato}")
        print()

def main():
    while True:
        mostra_menu()
        opzione = input("Seleziona un'opzione: ")
        if opzione == "1":
            pratica_omonimi()
        elif opzione == "2":
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
