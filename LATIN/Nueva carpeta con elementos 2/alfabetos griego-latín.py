# Greek Alphabet
greek_alphabet = [
    {"Uppercase": "Α", "Lowercase": "α", "Name": "Alfa", "Sound": "a"},
    {"Uppercase": "Β", "Lowercase": "β", "Name": "Beta", "Sound": "b"},
    {"Uppercase": "Γ", "Lowercase": "γ", "Name": "Gamma", "Sound": "ɣ"},
    {"Uppercase": "Δ", "Lowercase": "δ", "Name": "Delta", "Sound": "d"},
    {"Uppercase": "Ε", "Lowercase": "ε", "Name": "Epsilon", "Sound": "e"},
    {"Uppercase": "Ζ", "Lowercase": "ζ", "Name": "Zeta", "Sound": "z"},
    {"Uppercase": "Η", "Lowercase": "η", "Name": "Eta", "Sound": "i"},
    {"Uppercase": "Θ", "Lowercase": "θ", "Name": "Theta", "Sound": "θ"},
    {"Uppercase": "Ι", "Lowercase": "ι", "Name": "Iota", "Sound": "i"},
    {"Uppercase": "Κ", "Lowercase": "κ", "Name": "Kappa", "Sound": "k"},
    {"Uppercase": "Λ", "Lowercase": "λ", "Name": "Lambda", "Sound": "l"},
    {"Uppercase": "Μ", "Lowercase": "μ", "Name": "Mu", "Sound": "m"},
    {"Uppercase": "Ν", "Lowercase": "ν", "Name": "Nu", "Sound": "n"},
    {"Uppercase": "Ξ", "Lowercase": "ξ", "Name": "Xi", "Sound": "ks"},
    {"Uppercase": "Ο", "Lowercase": "ο", "Name": "Omicron", "Sound": "o"},
    {"Uppercase": "Π", "Lowercase": "π", "Name": "Pi", "Sound": "p"},
    {"Uppercase": "Ρ", "Lowercase": "ρ", "Name": "Rho", "Sound": "r"},
    {"Uppercase": "Σ", "Lowercase": "σ", "Name": "Sigma", "Sound": "s"},
    {"Uppercase": "Τ", "Lowercase": "τ", "Name": "Tau", "Sound": "t"},
    {"Uppercase": "Υ", "Lowercase": "υ", "Name": "Upsilon", "Sound": "y"},
    {"Uppercase": "Φ", "Lowercase": "φ", "Name": "Phi", "Sound": "f"},
    {"Uppercase": "Χ", "Lowercase": "χ", "Name": "Chi", "Sound": "x"},
    {"Uppercase": "Ψ", "Lowercase": "ψ", "Name": "Psi", "Sound": "ps"},
    {"Uppercase": "Ω", "Lowercase": "ω", "Name": "Omega", "Sound": "o"}
]

# Latin Alphabet
latin_alphabet = [
    {"Uppercase": "A", "Lowercase": "a", "Name": "A", "Sound": "a"},
    {"Uppercase": "B", "Lowercase": "b", "Name": "Be", "Sound": "b"},
    {"Uppercase": "C", "Lowercase": "c", "Name": "Ce", "Sound": "k"},
    {"Uppercase": "D", "Lowercase": "d", "Name": "De", "Sound": "d"},
    {"Uppercase": "E", "Lowercase": "e", "Name": "E", "Sound": "e"},
    {"Uppercase": "F", "Lowercase": "f", "Name": "Efe", "Sound": "f"},
    {"Uppercase": "G", "Lowercase": "g", "Name": "Ge", "Sound": "g"},
    {"Uppercase": "H", "Lowercase": "h", "Name": "Hache", "Sound": "h"},
    {"Uppercase": "I", "Lowercase": "i", "Name": "I", "Sound": "i"},
    {"Uppercase": "J", "Lowercase": "j", "Name": "Jota", "Sound": "x"},
    {"Uppercase": "K", "Lowercase": "k", "Name": "Ka", "Sound": "k"},
    {"Uppercase": "L", "Lowercase": "l", "Name": "Ele", "Sound": "l"},
    {"Uppercase": "M", "Lowercase": "m", "Name": "Eme", "Sound": "m"},
    {"Uppercase": "N", "Lowercase": "n", "Name": "Ene", "Sound": "n"},
    {"Uppercase": "O", "Lowercase": "o", "Name": "O", "Sound": "o"},
    {"Uppercase": "P", "Lowercase": "p", "Name": "Pe", "Sound": "p"},
    {"Uppercase": "Q", "Lowercase": "q", "Name": "Cu", "Sound": "k"},
    {"Uppercase": "R", "Lowercase": "r", "Name": "Ere", "Sound": "r"},
    {"Uppercase": "S", "Lowercase": "s", "Name": "Ese", "Sound": "s"},
    {"Uppercase": "T", "Lowercase": "t", "Name": "Te", "Sound": "t"},
    {"Uppercase": "U", "Lowercase": "u", "Name": "U", "Sound": "u"},
    {"Uppercase": "V", "Lowercase": "v", "Name": "Uve", "Sound": "v"},
    {"Uppercase": "W", "Lowercase": "w", "Name": "Doble uve", "Sound": "w"},
    {"Uppercase": "X", "Lowercase": "x", "Name": "Equis", "Sound": "ks"},
    {"Uppercase": "Y", "Lowercase": "y", "Name": "Ye", "Sound": "j"},
    {"Uppercase": "Z", "Lowercase": "z", "Name": "Zeta", "Sound": "θ"}
]

# Numbers
numbers = [
    {"Number": "0", "Spanish": "Cero", "English": "Zero"},
    {"Number": "1", "Spanish": "Uno", "English": "One"},
    {"Number": "2", "Spanish": "Dos", "English": "Two"},
    {"Number": "3", "Spanish": "Tres", "English": "Three"},
    {"Number": "4", "Spanish": "Cuatro", "English": "Four"},
    {"Number": "5", "Spanish": "Cinco", "English": "Five"},
    {"Number": "6", "Spanish": "Seis", "English": "Six"},
    {"Number": "7", "Spanish": "Siete", "English": "Seven"},
    {"Number": "8", "Spanish": "Ocho", "English": "Eight"},
    {"Number": "9", "Spanish": "Nueve", "English": "Nine"},
    {"Number": "10", "Spanish": "Diez", "English": "Ten"}
]

def display_alphabet(alphabet):
    for letter in alphabet:
        print(f"Uppercase: {letter['Uppercase']}, Lowercase: {letter['Lowercase']}, Name: {letter['Name']}, Sound: {letter['Sound']}")

def display_numbers(numbers):
    for number in numbers:
        print(f"Number: {number['Number']}, Spanish: {number['Spanish']}, English: {number['English']}")

def test_alphabet(alphabet):
    for letter in alphabet:
        user_input = input(f"Type the {letter['Name']} letter (Uppercase: {letter['Uppercase']}): ")
        if user_input.lower() == letter['Lowercase']:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {letter['Lowercase']}")

def test_numbers(numbers):
    for number in numbers:
        user_input = input(f"Type the number {number['Number']} in Spanish: ")
        if user_input.lower() == number['Spanish'].lower():
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {number['Spanish']}")

def main():
    print("Select the option:")
    print("1. Display Greek Alphabet")
    print("2. Display Latin Alphabet")
    print("3. Display Numbers")
    print("4. Test Greek Alphabet")
    print("5. Test Latin Alphabet")
    print("6. Test Numbers")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        display_alphabet(greek_alphabet)
    elif choice == "2":
        display_alphabet(latin_alphabet)
    elif choice == "3":
        display
