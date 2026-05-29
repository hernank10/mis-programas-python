def read_rule(rule):
    print(f"Please read the {rule} rule:")
    user_input = input()
    return user_input.strip().lower()

def verify_rule(rule, user_input):
    if user_input == rule:
        print("Correct! Let's move on to the next rule.")
        return True
    else:
        print(f"Incorrect. The correct rule was: {rule}")
        return False

def main():
    rules = {
        "b": [
            "Words starting with 'bl' or 'br'",
            "Before a consonant, always use 'b'",
            # ... other rules for the letter "b"
        ],
        "v": [
            "Words containing the sequence N + V",
            "Some forms of the verb 'ir'",
            # ... other rules for the letter "v"
        ],
        "w": [
            "Words with 'w' in loanwords",
            "Adaptation to Spanish",
            # ... other rules for the letter "w"
        ]
    }

    for letter, rule_list in rules.items():
        print(f"Rules for the letter '{letter}':")
        for i, rule in enumerate(rule_list, start=1):
            user_entry = read_rule(rule)
            if not verify_rule(rule.lower(), user_entry):
                print("Try again!")
                break
        else:
            print(f"Excellent! You've completed the rules for the letter '{letter}'.")

if __name__ == "__main__":
    main()
