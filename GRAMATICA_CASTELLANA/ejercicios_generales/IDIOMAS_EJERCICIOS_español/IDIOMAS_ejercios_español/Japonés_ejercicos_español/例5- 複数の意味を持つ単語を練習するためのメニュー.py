def show_menu():
    print("1. 複数の意味を持つ単語を練習する")
    print("2. 終了")

def practice_multiple_meanings():
    words = {
        "cabeza": ["体の上部", "グループのリーダー"],
        "lengua": ["口の中の筋肉器官", "言語"],
        "ojo": ["視覚器官", "針の穴"]
    }
    for word, meanings in words.items():
        print(f"単語: {word}")
        for i, meaning in enumerate(meanings, 1):
            print(f"{i}. {meaning}")
        print()

def main():
    while True:
        show_menu()
        option = input("オプションを選択してください: ")
        if option == "1":
            practice_multiple_meanings()
        elif option == "2":
            break
        else:
            print("無効なオプションです。もう一度試してください。")

if __name__ == "__main__":
    main()
