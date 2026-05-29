def show_menu():
    print("1. תרגול מילים עם משמעויות מרובות")
    print("2. יציאה")

def practice_multiple_meanings():
    words = {
        "cabeza": ["החלק העליון של הגוף", "מנהיג הקבוצה"],
        "lengua": ["איבר שרירי בפה", "שפה"],
        "ojo": ["איבר הראייה", "חור המחט"]
    }
    for word, meanings in words.items():
        print(f"מילה: {word}")
        for i, meaning in enumerate(meanings, 1):
            print(f"{i}. {meaning}")
        print()

def main():
    while True:
        show_menu()
        option = input("בחר אפשרות: ")
        if option == "1":
            practice_multiple_meanings()
        elif option == "2":
            break
        else:
            print("אפשרות לא תקינה. נסה שוב.")

if __name__ == "__main__":
    main()
