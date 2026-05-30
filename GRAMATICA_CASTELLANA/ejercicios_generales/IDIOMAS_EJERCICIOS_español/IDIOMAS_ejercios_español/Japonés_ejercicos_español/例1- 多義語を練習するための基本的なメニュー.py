def show_menu():
    print("1. 多義語を練習する")
    print("2. 終了")

def practice_polysemies():
    words = {
        "banco": ["複数人が座るベンチ", "金融機関"],
        "carta": ["書かれた文書", "トランプのカード"],
        "corte": ["切る動作", "裁判所"]
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
            practice_polysemies()
        elif option == "2":
            break
        else:
            print("無効なオプションです。もう一度試してください。")

if __name__ == "__main__":
    main()
