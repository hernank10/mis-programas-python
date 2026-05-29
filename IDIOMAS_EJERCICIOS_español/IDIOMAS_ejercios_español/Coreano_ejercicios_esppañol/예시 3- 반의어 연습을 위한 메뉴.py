def show_menu():
    print("1. 반의어 연습")
    print("2. 종료")

def practice_antonyms():
    words = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for word, antonyms in words.items():
        print(f"단어: {word}")
        print(f"반의어: {', '.join(antonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("옵션을 선택하세요: ")
        if option == "1":
            practice_antonyms()
        elif option == "2":
            break
        else:
            print("잘못된 옵션입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
