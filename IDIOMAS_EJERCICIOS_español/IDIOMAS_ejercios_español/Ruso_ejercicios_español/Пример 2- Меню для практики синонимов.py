def show_menu():
    print("1. Практиковать синонимы")
    print("2. Выход")

def practice_synonyms():
    words = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for word, synonyms in words.items():
        print(f"Слово: {word}")
        print(f"Синонимы: {', '.join(synonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("Выберите опцию: ")
        if option == "1":
            practice_synonyms()
        elif option == "2":
            break
        else:
            print("Неверная опция. Попробуйте снова.")

if __name__ == "__main__":
    main()
