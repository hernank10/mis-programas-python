def show_menu():
    print("1. Практиковать многозначные слова")
    print("2. Выход")

def practice_polysemies():
    words = {
        "banco": ["Скамейка для нескольких человек", "Финансовое учреждение"],
        "carta": ["Письменный документ", "Игральная карта"],
        "corte": ["Действие разрезания", "Суд"]
    }
    for word, meanings in words.items():
        print(f"Слово: {word}")
        for i, meaning in enumerate(meanings, 1):
            print(f"{i}. {meaning}")
        print()

def main():
    while True:
        show_menu()
        option = input("Выберите опцию: ")
        if option == "1":
            practice_polysemies()
        elif option == "2":
            break
        else:
            print("Неверная опция. Попробуйте снова.")

if __name__ == "__main__":
    main()
