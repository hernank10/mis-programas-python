def show_menu():
    print("1. التدرب على الكلمات متعددة المعاني")
    print("2. الخروج")

def practice_polysemies():
    words = {
        "banco": ["مقعد لعدة أشخاص", "مؤسسة مالية"],
        "carta": ["وثيقة مكتوبة", "ورقة لعب"],
        "corte": ["فعل القطع", "محكمة"]
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
            practice_polysemies()
        elif option == "2":
            break
        else:
            print("خيار غير صحيح. حاول مرة أخرى.")

if __name__ == "__main__":
    main()
