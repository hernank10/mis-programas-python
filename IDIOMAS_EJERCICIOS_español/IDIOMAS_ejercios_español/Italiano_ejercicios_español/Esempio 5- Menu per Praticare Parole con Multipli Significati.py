def mostra_menu():
    print("1. Praticare parole con multipli significati")
    print("2. Uscire")

def pratica_multipli_significati():
    parole = {
        "cabeza": ["Parte superiore del corpo", "Capo di un gruppo"],
        "lengua": ["Organo muscolare nella bocca", "Lingua"],
        "ojo": ["Organo della vista", "Cruna dell'ago"]
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
            pratica_multipli_significati()
        elif opzione == "2":
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
