def show_menu():
    print("1. 练习多义词")
    print("2. 退出")

def practice_multiple_meanings():
    words = {
        "cabeza": ["身体的顶部", "团队的领导者"],
        "lengua": ["口腔中的肌肉器官", "语言"],
        "ojo": ["视觉器官", "针眼"]
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
            practice_multiple_meanings()
        elif option == "2":
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()
