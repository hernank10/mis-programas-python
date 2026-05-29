def mostra_menu():
    print("1. Praticare sinonimi")
    print("2. Uscire")

def pratica_sinonimi():
    parole = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for parola, sinonimi in parole.items():
        print(f"Parola: {parola}")
        print(f"Sinonimi: {', '.join(sinonimi)}")
        print()

def main():
    while True:
        mostra_menu()
        opzione = input("Seleziona un'opzione: ")
        if opzione == "1":
            pratica_sinonimi()
        elif opzione == "2":
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
