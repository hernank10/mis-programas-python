def show_menu():
    print("1. תרגול מילים רב-משמעיות")
    print("2. יציאה")

def practice_polysemies():
    words = {
        "banco": ["ספסל לישיבה של מספר אנשים", "מוסד פיננסי"],
        "carta": ["מסמך כתוב", "קלף משחק"],
        "corte": ["פעולת החיתוך", "בית משפט"]
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
            practice_polysemies()
        elif option == "2":
            break
        else:
            print("אפשרות לא תקינה. נסה שוב.")

if __name__ == "__main__":
    main()
