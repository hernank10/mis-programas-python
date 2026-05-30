def pokaz_menu():
    print("\nWitamy w uniwersalnym programie do nauki alfabetów!")
    print("1. Angielski")
    print("2. Hiszpański")
    print("3. Portugalski")
    print("4. Francuski")
    print("5. Niemiecki")
    print("6. Polski")
    print("7. Zakończ")

alfabety = {
    "Angielski": {
        "A": "Apple",
        "B": "Ball",
        "C": "Cat",
        "D": "Dog",
        "E": "Elephant",
        "F": "Fish",
        "G": "Goat",
        "H": "Hat",
        "I": "Ice",
        "J": "Jar",
        "K": "Kite",
        "L": "Lion",
        "M": "Monkey",
        "N": "Nose",
        "O": "Orange",
        "P": "Pen",
        "Q": "Queen",
        "R": "Rabbit",
        "S": "Sun",
        "T": "Tiger",
        "U": "Umbrella",
        "V": "Violin",
        "W": "Whale",
        "X": "Xylophone",
        "Y": "Yak",
        "Z": "Zebra"
    },
    "Hiszpański": {
        "A": "Amor",
        "B": "Beso",
        "C": "Casa",
        "D": "Dedo",
        "E": "Elefante",
        "F": "Flor",
        "G": "Gato",
        "H": "Hombre",
        "I": "Isla",
        "J": "Jardín",
        "K": "Koala",
        "L": "Lápiz",
        "M": "Mujer",
        "N": "Niño",
        "O": "Oso",
        "P": "Perro",
        "Q": "Queso",
        "R": "Rosa",
        "S": "Sol",
        "T": "Toro",
        "U": "Uva",
        "V": "Vaca",
        "W": "Wafle",
        "X": "Xilófono",
        "Y": "Yate",
        "Z": "Zapato"
    },
    "Portugalski": {
        "A": "Amor",
        "B": "Bola",
        "C": "Cachorro",
        "D": "Dado",
        "E": "Elefante",
        "F": "Faca",
        "G": "Gato",
        "H": "Homem",
        "I": "Igreja",
        "J": "Jacaré",
        "K": "Kiwi",
        "L": "Leão",
        "M": "Mulher",
        "N": "Navio",
        "O": "Olho",
        "P": "Pássaro",
        "Q": "Queijo",
        "R": "Rato",
        "S": "Sol",
        "T": "Tigre",
        "U": "Uva",
        "V": "Vaca",
        "W": "Waffle",
        "X": "Xadrez",
        "Y": "Yak",
        "Z": "Zebra"
    },
    "Francuski": {
        "A": "Arbre",
        "B": "Bateau",
        "C": "Chat",
        "D": "Dauphin",
        "E": "Etoile",
        "F": "Fleur",
        "G": "Guitare",
        "H": "Hibou",
        "I": "Ile",
        "J": "Jardin",
        "K": "Koala",
        "L": "Lune",
        "M": "Maison",
        "N": "Nuage",
        "O": "Oiseau",
        "P": "Poisson",
        "Q": "Quatre",
        "R": "Rivière",
        "S": "Soleil",
        "T": "Tigre",
        "U": "Univers",
        "V": "Vache",
        "W": "Wagon",
        "X": "Xylophone",
        "Y": "Yaourt",
        "Z": "Zèbre"
    },
    "Niemiecki": {
        "A": "Apfel",
        "B": "Ball",
        "C": "Clown",
        "D": "Dach",
        "E": "Elefant",
        "F": "Fisch",
        "G": "Giraffe",
        "H": "Haus",
        "I": "Igel",
        "J": "Junge",
        "K": "Kuh",
        "L": "Lampe",
        "M": "Mond",
        "N": "Nacht",
        "O": "Obst",
        "P": "Pferd",
        "Q": "Qualle",
        "R": "Regen",
        "S": "Sonne",
        "T": "Tiger",
        "U": "Uhr",
        "V": "Vogel",
        "W": "Wald",
        "X": "Xylophon",
        "Y": "Yak",
        "Z": "Zebra"
    },
    "Polski": {
        "A": "Ananas",
        "B": "Banan",
        "C": "Cebula",
        "D": "Dom",
        "E": "Ekierka",
        "F": "Foka",
        "G": "Gęs",
        "H": "Herbata",
        "I": "Igła",
        "J": "Jabłko",
        "K": "Kot",
        "L": "Lampa",
        "Ł": "Łódź",
        "M": "Mleko",
        "N": "Nos",
        "O": "Okno",
        "P": "Pies",
        "R": "Rzeka",
        "S": "Samochód",
        "Ś": "Ślimak",
        "T": "Talerz",
        "U": "Ul",
        "W": "Woda",
        "Z": "Zebra",
        "Ż": "Żerafa",
        "ź": "Żaba"
    }
}

def pokaz_alfabet(jezyk):
    print(f"\nAlfabet dla języka {jezyk}:")
    for litera, slowo in alfabety[jezyk].items():
        print(f"{litera} : {slowo}")

def cwicz_litery(jezyk):
    import random
    litery = list(alfabety[jezyk].keys())
    random.shuffle(litery)

    print(f"\nĆwiczenie: Podaj odpowiednie słowo dla podanej litery w języku {jezyk}.")
    punkty = 0
    for litera in litery:
        odpowiedz = input(f"Jakie słowo zaczyna się na literę '{litera}'? ").strip()
        if odpowiedz.lower() == alfabety[jezyk][litera].lower():
            print("Poprawnie!")
            punkty += 1
        else:
            print(f"Błąd. Poprawna odpowiedź to '{alfabety[jezyk][litera]}'")
    print(f"\nTwój wynik końcowy to: {punkty}/{len(alfabety[jezyk])}")

def glowny_program():
    while True:
        pokaz_menu()
        opcja = input("Wybierz opcję: ")

        if opcja in ["1", "2", "3", "4", "5", "6"]:
            jezyki = ["Angielski", "Hiszpański", "Portugalski", "Francuski", "Niemiecki", "Polski"]
            wybrany_jezyk = jezyki[int(opcja) - 1]
            print(f"\nWybrano język: {wybrany_jezyk}")

            print("\n1. Pokaż alfabet")
            print("2. Ćwicz litery")
            pod_opcja = input("Wybierz opcję: ")

            if pod_opcja == "1":
                pokaz_alfabet(wybrany_jezyk)
            elif pod_opcja == "2":
                cwicz_litery(wybrany_jezyk)
            else:
                print("\nWybierz poprawną opcję.")
        elif opcja == "7":
            print("\nDziękujemy za skorzystanie z programu. Do zobaczenia!")
            break
        else:
            print("\nWybierz poprawną opcję.")

if __name__ == "__main__":
    glowny_program()
