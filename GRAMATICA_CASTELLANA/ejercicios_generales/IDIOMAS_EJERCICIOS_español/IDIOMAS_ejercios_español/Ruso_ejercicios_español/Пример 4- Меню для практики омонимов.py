def show_menu():
    print("1. Практиковать омонимы")
    print("2. Выход")

def practice_homonyms():
    words = {
        "vino": ["Алкогольный напиток", "Прошедшее время глагола 'venir'"],
        "llama": ["Южноамериканское животное", "Огонь", "Форма глагола 'llamar'"],
        "banco": ["Скамейка", "Финансовое учреждение"]
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
            practice_homonyms()
        elif option == "2":
            break
        else:
            print("Неверная опция. Попробуйте снова.")

if __name__ == "__main__":
    main()
