def show_menu():
    print("1. 同義語を練習する")
    print("2. 終了")

def practice_synonyms():
    words = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for word, synonyms in words.items():
        print(f"単語: {word}")
        print(f"同義語: {', '.join(synonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("オプションを選択してください: ")
        if option == "1":
            practice_synonyms()
        elif option == "2":
            break
        else:
            print("無効なオプションです。もう一度試してください。")

if __name__ == "__main__":
    main()
