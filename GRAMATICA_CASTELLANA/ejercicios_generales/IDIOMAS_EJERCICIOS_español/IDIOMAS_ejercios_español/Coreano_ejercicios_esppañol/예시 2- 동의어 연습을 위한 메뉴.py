def show_menu():
    print("1. 동의어 연습")
    print("2. 종료")

def practice_synonyms():
    words = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for word, synonyms in words.items():
        print(f"단어: {word}")
        print(f"동의어: {', '.join(synonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("옵션을 선택하세요: ")
        if option == "1":
            practice_synonyms()
        elif option == "2":
            break
        else:
            print("잘못된 옵션입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
