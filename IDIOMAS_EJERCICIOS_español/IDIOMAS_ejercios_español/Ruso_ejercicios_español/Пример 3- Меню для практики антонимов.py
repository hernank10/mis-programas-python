def show_menu():
    print("1. Практиковать антонимы")
    print("2. Выход")

def practice_antonyms():
    words = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for word, antonyms in words.items():
        print(f"Слово: {word}")
        print(f"Антонимы: {', '.join(antonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("Выберите опцию: ")
        if option == "1":
            practice_antonyms()
        elif option == "2":
            break
        else:
            print("Неверная опция. Попробуйте снова.")

if __name__ == "__main__":
    main()
