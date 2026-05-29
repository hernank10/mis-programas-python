def show_menu():
    print("1. Практиковать слова с множественными значениями")
    print("2. Выход")

def practice_multiple_meanings():
    words = {
        "cabeza": ["Верхняя часть тела", "Лидер группы"],
        "lengua": ["Мышечный орган во рту", "Язык"],
        "ojo": ["Орган зрения", "Ушко иглы"]
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
            practice_multiple_meanings()
        elif option == "2":
            break
        else:
            print("Неверная опция. Попробуйте снова.")

if __name__ == "__main__":
    main()
