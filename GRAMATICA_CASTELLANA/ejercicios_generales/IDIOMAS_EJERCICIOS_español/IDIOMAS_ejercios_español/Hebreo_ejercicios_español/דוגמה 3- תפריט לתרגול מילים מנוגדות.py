def show_menu():
    print("1. תרגול מילים מנוגדות")
    print("2. יציאה")

def practice_antonyms():
    words = {
        "feliz": ["triste", "infeliz", "desdichado"],
        "rápido": ["lento", "pausado", "tardío"],
        "alto": ["bajo", "pequeño", "reducido"]
    }
    for word, antonyms in words.items():
        print(f"מילה: {word}")
        print(f"מילים מנוגדות: {', '.join(antonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("בחר אפשרות: ")
        if option == "1":
            practice_antonyms()
        elif option == "2":
            break
        else:
            print("אפשרות לא תקינה. נסה שוב.")

if __name__ == "__main__":
    main()
