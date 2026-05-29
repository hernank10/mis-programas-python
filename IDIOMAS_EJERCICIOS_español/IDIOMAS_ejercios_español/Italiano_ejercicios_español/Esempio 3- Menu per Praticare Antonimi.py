def mostra_menu():
    print("1. Praticare antonimi")
    print("2. Uscire")

def pratica_antonimi():
    parole = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for parola, antonimi in parole.items():
        print(f"Parola: {parola}")
        print(f"Antonimi: {', '.join(antonimi)}")
        print()

def main():
    while True:
        mostra_menu()
        opzione = input("Seleziona un'opzione: ")
        if opzione == "1":
            pratica_antonimi()
        elif opzione == "2":
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
