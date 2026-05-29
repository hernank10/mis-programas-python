def show_menu():
    print("1. 동음이의어 연습")
    print("2. 종료")

def practice_homonyms():
    words = {
        "vino": ["알코올 음료", "동사 'venir'의 과거형"],
        "llama": ["남미 동물", "불", "동사 'llamar'의 형태"],
        "banco": ["벤치", "금융 기관"]
    }
    for word, meanings in words.items():
        print(f"단어: {word}")
        for i, meaning in enumerate(meanings, 1):
            print(f"{i}. {meaning}")
        print()

def main():
    while True:
        show_menu()
        option = input("옵션을 선택하세요: ")
        if option == "1":
            practice_homonyms()
        elif option == "2":
            break
        else:
            print("잘못된 옵션입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
