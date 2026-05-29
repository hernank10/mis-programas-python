import random

def indovina_significato():
    dizionario = {"correre": "correre", "brillante": "luminoso"}
    parola, significato = random.choice(list(dizionario.items()))
    opzioni = [significato, "Risposta sbagliata 1", "Risposta sbagliata 2"]
    random.shuffle(opzioni)
    print(f"Qual è il significato della parola '{parola}'?")
    for i, opzione in enumerate(opzioni, 1):
        print(f"{i}. {opzione}")
    risposta = int(input("Scegli la risposta corretta: "))
    print("Corretto!" if opzioni[risposta - 1] == significato else "Sbagliato.")

def sinonimi_contrari():
    sinonimi = {"felice": "allegro", "veloce": "rapido"}
    contrari = {"felice": "triste", "veloce": "lento"}
    parola = random.choice(list(sinonimi.keys()))
    print(f"Scrivi un sinonimo o un contrario per '{parola}':")
    risposta = input().strip()
    if risposta in (sinonimi[parola], contrari[parola]):
        print("Corretto!")
    else:
        print(f"Sbagliato. Risposta attesa: Sinonimo '{sinonimi[parola]}', Contrario '{contrari[parola]}'")

def completa_frase():
    frasi = {"brillante": "Il sole è molto ______ oggi."}
    parola, frase = random.choice(list(frasi.items()))
    print(frase)
    risposta = input("Inserisci la parola corretta: ").strip()
    if risposta == parola:
        print("Corretto!")
    else:
        print(f"Sbagliato. Risposta attesa: '{parola}'")

def categorizza_parola():
    categorie = {"scientifico": "tecnico", "pittoresco": "letterario"}
    parola, categoria = random.choice(list(categorie.items()))
    print(f"A quale categoria appartiene la parola '{parola}'?")
    risposta = input("Scegli tra: tecnico, letterario, quotidiano: ").strip().lower()
    if risposta == categoria:
        print("Corretto!")
    else:
        print(f"Sbagliato. Risposta attesa: '{categoria}'")

def definisci_parola():
    parola = "correre"
    print(f"Definisci la parola '{parola}':")
    input()
    print("Grazie! La definizione corretta è 'muoversi rapidamente'.")

def menu():
    while True:
        print("\nMenu di Esercizi di Vocabolario")
        print("1. Indovina il significato")
        print("2. Sinonimi e contrari")
        print("3. Completa la frase")
        print("4. Categorizza la parola")
        print("5. Definisci la parola")
        print("6. Esci")
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            indovina_significato()
        elif scelta == "2":
            sinonimi_contrari()
        elif scelta == "3":
            completa_frase()
        elif scelta == "4":
            categorizza_parola()
        elif scelta == "5":
            definisci_parola()
        elif scelta == "6":
            print("Arrivederci!")
            break
        else:
            print("Ingresso non valido. Riprova.")

menu()
