def show_menu():
    print("1. 练习同义词")
    print("2. 退出")

def practice_synonyms():
    words = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for word, synonyms in words.items():
        print(f"单词: {word}")
        print(f"同义词: {', '.join(synonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("选择一个选项: ")
        if option == "1":
            practice_synonyms()
        elif option == "2":
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()
