def show_menu():
    print("1. 练习多义词")
    print("2. 退出")

def practice_polysemies():
    words = {
        "banco": ["多人坐的长椅", "金融机构"],
        "carta": ["书面文件", "扑克牌"],
        "corte": ["切割的动作", "法院"]
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
            practice_polysemies()
        elif option == "2":
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()
