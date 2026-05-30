def show_menu():
    print("1. 练习反义词")
    print("2. 退出")

def practice_antonyms():
    words = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for word, antonyms in words.items():
        print(f"单词: {word}")
        print(f"反义词: {', '.join(antonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("选择一个选项: ")
        if option == "1":
            practice_antonyms()
        elif option == "2":
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()
