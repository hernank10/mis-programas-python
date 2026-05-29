def show_menu():
    print("1. 同音異義語を練習する")
    print("2. 終了")

def practice_homonyms():
    words = {
        "vino": ["アルコール飲料", "動詞 'venir' の過去形"],
        "llama": ["南米の動物", "火", "動詞 'llamar' の形"],
        "banco": ["ベンチ", "金融機関"]
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
            practice_homonyms()
        elif option == "2":
            break
        else:
            print("無効なオプションです。もう一度試してください。")

if __name__ == "__main__":
    main()
