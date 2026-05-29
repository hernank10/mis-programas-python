def mostra_menu():
    print("1. Praticare parole polisemiche")
    print("2. Uscire")

def pratica_polisemie():
    parole = {
        "banco": ["Panchina per più persone", "Istituto finanziario"],
        "carta": ["Documento scritto", "Carta da gioco"],
        "corte": ["Azione di tagliare", "Tribunale"]
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
            pratica_polisemie()
        elif opzione == "2":
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
