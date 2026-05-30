import random

def zgadnij_znaczenie():
    slownik = {"biegać": "poruszać się szybko", "błyszczący": "jasny"}
    slowo, znaczenie = random.choice(list(slownik.items()))
    opcje = [znaczenie, "Niepoprawna odpowiedź 1", "Niepoprawna odpowiedź 2"]
    random.shuffle(opcje)
    print(f"Jakie jest znaczenie słowa '{slowo}'?")
    for i, opcja in enumerate(opcje, 1):
        print(f"{i}. {opcja}")
    odpowiedz = int(input("Wybierz poprawną odpowiedź: "))
    print("Poprawnie!" if opcje[odpowiedz - 1] == znaczenie else "Niepoprawnie.")

def synonimy_antonymy():
    synonimy = {"szczęśliwy": "wesoły", "szybki": "prędki"}
    antonimy = {"szczęśliwy": "smutny", "szybki": "wolny"}
    slowo = random.choice(list(synonimy.keys()))
    print(f"Podaj synonim lub antonim dla '{slowo}':")
    odpowiedz = input().strip()
    if odpowiedz in (synonimy[slowo], antonimy[slowo]):
        print("Poprawnie!")
    else:
        print(f"Niepoprawnie. Oczekiwane: Synonim '{synonimy[slowo]}', Antonim '{antonymy[slowo]}'")

def uzupelnij_zdanie():
    zdania = {"błyszczący": "Słońce jest dziś bardzo ______."}
    slowo, zdanie = random.choice(list(zdania.items()))
    print(zdanie)
    odpowiedz = input("Wpisz poprawne słowo: ").strip()
    if odpowiedz == slowo:
        print("Poprawnie!")
    else:
        print(f"Niepoprawnie. Oczekiwane: '{slowo}'")

def kategoryzuj_slowo():
    kategorie = {"naukowy": "techniczny", "malowniczy": "literacki"}
    slowo, kategoria = random.choice(list(kategorie.items()))
    print(f"Do której kategorii należy słowo '{slowo}'?")
    odpowiedz = input("Wybierz spośród: techniczny, literacki, codzienny: ").strip().lower()
    if odpowiedz == kategoria:
        print("Poprawnie!")
    else:
        print(f"Niepoprawnie. Oczekiwane: '{kategoria}'")

def zdefiniuj_slowo():
    slowo = "biegać"
    print(f"Zdefiniuj słowo '{slowo}':")
    input()
    print("Dziękujemy! Poprawna definicja to 'poruszać się szybko'.")

def menu():
    while True:
        print("\nMenu Ćwiczeń Słownictwa")
        print("1. Zgadnij znaczenie")
        print("2. Synonimy i antonimy")
        print("3. Uzupełnij zdanie")
        print("4. Kategoryzuj słowo")
        print("5. Zdefiniuj słowo")
        print("6. Wyjście")
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            zgadnij_znaczenie()
        elif wybor == "2":
            synonimy_antonymy()
        elif wybor == "3":
            uzupelnij_zdanie()
        elif wybor == "4":
            kategoryzuj_slowo()
        elif wybor == "5":
            zdefiniuj_slowo()
        elif wybor == "6":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowe wejście. Spróbuj ponownie.")

menu()
