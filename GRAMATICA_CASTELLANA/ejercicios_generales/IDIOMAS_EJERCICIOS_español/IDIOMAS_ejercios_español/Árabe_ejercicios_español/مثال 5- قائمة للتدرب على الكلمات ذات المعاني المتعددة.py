def show_menu():
    print("1. التدرب على الكلمات ذات المعاني المتعددة")
    print("2. الخروج")

def practice_multiple_meanings():
    words = {
        "cabeza": ["الجزء العلوي من الجسم", "قائد المجموعة"],
        "lengua": ["عضو عضلي في الفم", "لغة"],
        "ojo": ["عضو الرؤية", "ثقب الإبرة"]
    }
    for word, meanings in words.items():
        print(f"الكلمة: {word}")
        for i, meaning in enumerate(meanings, 1):
            print(f"{i}. {meaning}")
        print()

def main():
    while True:
        show_menu()
        option = input("اختر خيارًا: ")
        if option == "1":
            practice_multiple_meanings()
        elif option == "2":
            break
        else:
            print("خيار غير صحيح. حاول مرة أخرى.")

if __name__ == "__main__":
    main()
