def show_menu():
    print("1. التدرب على الأضداد")
    print("2. الخروج")

def practice_antonyms():
    words = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for word, antonyms in words.items():
        print(f"الكلمة: {word}")
        print(f"الأضداد: {', '.join(antonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("اختر خيارًا: ")
        if option == "1":
            practice_antonyms()
        elif option == "2":
            break
        else:
            print("خيار غير صحيح. حاول مرة أخرى.")

if __name__ == "__main__":
    main()
