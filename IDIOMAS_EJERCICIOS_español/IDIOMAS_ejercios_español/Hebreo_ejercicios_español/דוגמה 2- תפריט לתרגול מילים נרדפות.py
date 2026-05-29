def show_menu():
    print("1. תרגול מילים נרדפות")
    print("2. יציאה")

def practice_synonyms():
    words = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["apenado", "desdichado", "melancólico"],
        "rápido": ["veloz", "ágil", "ligero"]
    }
    for word, synonyms in words.items():
        print(f"מילה: {word}")
        print(f"מילים נרדפות: {', '.join(synonyms)}")
        print()

def main():
    while True:
        show_menu()
        option = input("בחר אפשרות: ")
        if option == "1":
            practice_synonyms()
        elif option == "2":
            break
        else:
            print("אפשרות לא תקינה. נסה שוב.")

if __name__ == "__main__":
    main()
