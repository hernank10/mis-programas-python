def show_menu():
    print("1. 여러 의미를 가진 단어 연습")
    print("2. 종료")

def practice_multiple_meanings():
    words = {
        "cabeza": ["몸의 상단", "그룹의 리더"],
        "lengua": ["입 안의 근육 기관", "언어"],
        "ojo": ["시각 기관", "바늘귀"]
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
            practice_multiple_meanings()
        elif option == "2":
            break
        else:
            print("잘못된 옵션입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
