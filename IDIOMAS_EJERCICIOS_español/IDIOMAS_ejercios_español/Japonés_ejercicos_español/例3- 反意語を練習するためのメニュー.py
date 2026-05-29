def show_menu():
    print("1. 反意語を練習する")
    print("2. 終了")

def practice_antonyms():
    words = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for word, antonyms in words.items():
        print(f"単語: {word}")
        print(f"反意語: {', '.join(antonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("オプションを選択してください: ")
        if option == "1":
            practice_antonyms()
        elif option == "2":
            break
        else:
            print("無効なオプションです。もう一度試してください。")

if __name__ == "__main__":
    main()
