# Function for the user to input 50 words with their spelling rules
def enter_words():
    user_words_rules = {}
    
    print("Enter 50 words with their respective spelling rules:")
    for i in range(1, 51):
        word = input(f"\nWord {i}: ").strip().lower()
        rule = input(f"Spelling rule for the word '{word}': ").strip()
        user_words_rules[word] = rule

    return user_words_rules

# Function to display the words and rules entered by the user
def display_words(user_words_rules):
    print("\nHere are the words you entered with their spelling rules:")
    for word, rule in user_words_rules.items():
        print(f"\nWord: {word}\nRule: {rule}")

# Function to evaluate the user's spelling with the entered words
def evaluate_spelling(user_words_rules):
    errors = 0
    print("\nNow type the correct spelling of the words you entered based on their rules.")
    
    for word in user_words_rules.keys():
        answer = input(f"Type the correct word for the rule: '{user_words_rules[word]}': ").strip().lower()
        
        if answer == word:
            print("Correct!")
        else:
            print(f"Incorrect. The correct spelling is: {word}")
            errors += 1
    
    # Show final results
    total_words = len(user_words_rules)
    correct_answers = total_words - errors
    print(f"\nFinal Result: Correct Answers: {correct_answers} / {total_words}")
    print(f"Errors: {errors}")

    if errors == 0:
        print("Excellent work! No mistakes.")
    elif errors <= total_words / 2:
        print("Good job, but there's room for improvement.")
    else:
        print("You need more practice. Keep trying!")

# Interactive menu
def menu():
    user_words_rules = {}

    while True:
        print("\nMenu Options:")
        print("1. Enter words and spelling rules")
        print("2. Display entered words and rules")
        print("3. Evaluate spelling")
        print("4. Exit")
        
        option = input("Select an option (1/2/3/4): ")
        
        if option == "1":
            user_words_rules = enter_words()
        elif option == "2":
            if user_words_rules:
                display_words(user_words_rules)
            else:
                print("You must first enter words and spelling rules.")
        elif option == "3":
            if user_words_rules:
                evaluate_spelling(user_words_rules)
            else:
                print("You must first enter words and spelling rules.")
        elif option == "4":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid option, try again.")

# Program execution
if __name__ == "__main__":
    menu()
