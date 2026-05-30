def show_menu():
    print("1. תרגול מילים הומונימיות")
    print("2. יציאה")

def practice_homonyms():
    words = {
        "vino": ["משקה אלכוהולי", "צורת העבר של הפועל 'venir'"],
        "llama": ["חיה דרום אמריקאית", "אש", "צורת הפועל 'llamar'"],
        "banco": ["ספסל", "מוסד פיננסי"]
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
            practice_homonyms()
        elif option == "2":
            break
        else:
            print("אפשרות לא תקינה. נסה שוב.")

if __name__ == "__main__":
    main()
