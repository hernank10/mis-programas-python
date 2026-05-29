def show_menu():
    print("1. 练习同音异义词")
    print("2. 退出")

def practice_homonyms():
    words = {
        "vino": ["酒精饮料", "动词'venir'的过去式"],
        "llama": ["南美动物", "火焰", "动词'llamar'的形式"],
        "banco": ["长椅", "金融机构"]
    }
    for word, meanings in words.items():
        print(f"单词: {word}")
        for i, meaning in enumerate(meanings, 1):
            print(f"{i}. {meaning}")
        print()

def main():
    while True:
        show_menu()
        option = input("选择一个选项: ")
        if option == "1":
            practice_homonyms()
        elif option == "2":
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()
