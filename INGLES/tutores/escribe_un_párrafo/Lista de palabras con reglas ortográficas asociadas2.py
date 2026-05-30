# Function to display predefined words with their spelling rules
def display_words_and_rules():
    words_rules = {
        "believe": "The rule 'i before e except after c'",
        "receive": "The rule 'i before e except after c'",
        "separate": "Commonly misspelled word: Remember it's 'a' in the middle, not 'e'",
        "accommodate": "Commonly misspelled word: Remember it has double 'c' and double 'm'",
        "privilege": "Commonly misspelled word: Remember the ending is 'lege', not 'ledge'",
    }
    
    print("Words and their spelling rules:\n")
    for word, rule in words_rules.items():
        print(f"Word: {word}\nRule: {rule}\n")

# Function to evaluate the user's spelling
def evaluate_spelling():
    words_rules = {
        "believe": "The rule 'i before e except after c'",
        "receive": "The rule 'i before e except after c'",
        "separate": "Commonly misspelled word: Remember it's 'a' in the middle, not 'e'",
        "accommodate": "Commonly misspelled word: Remember it has double 'c' and double 'm'",
        "privilege": "Commonly misspelled word: Remember the ending is 'lege', not 'ledge'",
    }
    
    errors = 0
    print("Now, type the correct spelling of the following words based on their rules:\n")
    
    for word, rule in words_rules.items():
        answer = input(f"Type the correct word for the rule: '{rule}': ").strip().lower()
        
        if answer == word:
            print("Correct!")
        else:
            print(f"Incorrect. The correct spelling is: {word}")
            errors += 1

    # Show final results
    total_words = len(words_rules)
    correct_answers = total_words - errors
    print(f"\nFinal Result: Correct Answers: {correct_answers} / {total_words}")
    print(f"Errors: {errors}")

    if errors == 0:
        print("Excellent work! No mistakes.")
    elif errors <= total_words / 2:
        print("Good job, but there's room for improvement.")
    else:
        print("You need more practice. Keep trying!")

# Main program execution
if __name__ == "__main__":
    display_words_and_rules()
    evaluate_spelling()
