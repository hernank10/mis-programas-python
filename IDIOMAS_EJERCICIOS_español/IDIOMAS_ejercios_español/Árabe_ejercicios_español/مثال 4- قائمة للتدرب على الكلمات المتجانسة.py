def show_menu():
    print("1. التدرب على الكلمات المتجانسة")
    print("2. الخروج")

def practice_homonyms():
    words = {
        "vino": ["مشروب كحولي", "صيغة الماضي للفعل 'venir'"],
        "llama": ["حيوان أمريكي جنوبي", "نار", "صيغة الفعل 'llamar'"],
        "banco": ["مقعد", "مؤسسة مالية"]
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
            practice_homonyms()
        elif option == "2":
            break
        else:
            print("خيار غير صحيح. حاول مرة أخرى.")

if __name__ == "__main__":
    main()
