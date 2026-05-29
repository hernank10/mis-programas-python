def show_menu():
    print("1. التدرب على المرادفات")
    print("2. الخروج")

def practice_synonyms():
    words = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for word, synonyms in words.items():
        print(f"الكلمة: {word}")
        print(f"المرادفات: {', '.join(synonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("اختر خيارًا: ")
        if option == "1":
            practice_synonyms()
        elif option == "2":
            break
        else:
            print("خيار غير صحيح. حاول مرة أخرى.")

if __name__ == "__main__":
    main()
