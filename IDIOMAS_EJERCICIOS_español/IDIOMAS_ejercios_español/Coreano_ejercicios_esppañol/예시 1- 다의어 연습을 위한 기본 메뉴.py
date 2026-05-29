def show_menu():
    print("1. 다의어 연습")
    print("2. 종료")

def practice_polysemies():
    words = {
        "banco": ["여러 사람이 앉을 수 있는 벤치", "금융 기관"],
        "carta": ["문서", "플레잉 카드"],
        "corte": ["자르는 행위", "법원"]
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
            practice_polysemies()
        elif option == "2":
            break
        else:
            print("잘못된 옵션입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
