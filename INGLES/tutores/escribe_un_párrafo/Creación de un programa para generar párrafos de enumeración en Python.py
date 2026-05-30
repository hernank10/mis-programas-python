import random

def generate_organizer_phrase(type):
    if type == 'count':
        return "The following is a list of properties:"
    elif type == 'summary':
        return "The following properties summarize the object in question:"
    elif type == 'framing':
        return "The object described is characterized by several important properties:"
    else:
        return random.choice([
            "The following is a list of properties:",
            "The following properties summarize the object in question:",
            "The object described is characterized by several important properties:"
        ])

def add_property(properties):
    property = input("Enter a new property: ")
    properties.append(property.strip())
    print(f"Property '{property}' added successfully.")

def delete_property(properties):
    print("Current properties:")
    for i, property in enumerate(properties, 1):
        print(f"{i}. {property}")
    try:
        delete = int(input("Enter the number of the property you want to delete: "))
        if 1 <= delete <= len(properties):
            deleted_property = properties.pop(delete - 1)
            print(f"Property '{deleted_property}' deleted successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input. Try again.")

def generate_enumeration_paragraph(phrase_type, object_name, properties):
    # Generate the organizer phrase
    organizer_phrase = generate_organizer_phrase(phrase_type)

    # Generate the enumeration paragraph
    paragraph = f"{organizer_phrase}\n"  # Add the organizer phrase
    paragraph += f"The {object_name} has the following characteristics:\n"

    # Enumerate the properties
    for i, property in enumerate(properties, 1):
        paragraph += f"{i}. {property.capitalize()}\n"

    return paragraph

def generate_descriptive_paragraph(object_name, properties):
    paragraph = f"The {object_name} is characterized by its ability to:\n"
    paragraph += ', '.join(properties) + ".\n"
    return paragraph

def generate_argumentative_paragraph(object_name, properties):
    paragraph = f"The {object_name} is considered important because:\n"
    for property in properties:
        paragraph += f"- {property.capitalize()}.\n"
    return paragraph

def show_main_menu():
    print("\nMain Menu:")
    print("1. Add a property")
    print("2. Delete a property")
    print("3. View current properties")
    print("4. Generate enumeration paragraph")
    print("5. Generate descriptive paragraph")
    print("6. Generate argumentative paragraph")
    print("7. Exit")

def main():
    object_name = input("Enter the object, fact, or idea you want to describe: ")
    properties = []

    while True:
        show_main_menu()
        option = input("Select an option: ")

        if option == '1':
            add_property(properties)

        elif option == '2':
            if properties:
                delete_property(properties)
            else:
                print("There are no properties to delete.")

        elif option == '3':
            if properties:
                print("Current properties:")
                for i, property in enumerate(properties, 1):
                    print(f"{i}. {property}")
            else:
                print("No properties have been added.")

        elif option == '4':
            if properties:
                print("\nSelect the type of organizer phrase:")
                print("1. Count")
                print("2. Summary")
                print("3. Framing")
                print("4. Random")
                phrase_option = input("Select an option: ")

                if phrase_option == '1':
                    phrase_type = 'count'
                elif phrase_option == '2':
                    phrase_type = 'summary'
                elif phrase_option == '3':
                    phrase_type = 'framing'
                else:
                    phrase_type = 'random'

                paragraph = generate_enumeration_paragraph(phrase_type, object_name, properties)
                print("\nGenerated enumeration paragraph:\n")
                print(paragraph)
            else:
                print("No properties have been added to generate the paragraph.")

        elif option == '5':
            if properties:
                paragraph = generate_descriptive_paragraph(object_name, properties)
                print("\nGenerated descriptive paragraph:\n")
                print(paragraph)
            else:
                print("No properties have been added to generate the paragraph.")

        elif option == '6':
            if properties:
                paragraph = generate_argumentative_paragraph(object_name, properties)
                print("\nGenerated argumentative paragraph:\n")
                print(paragraph)
            else:
                print("No properties have been added to generate the paragraph.")

        elif option == '7':
            print("Thank you for using the program!")
            break

        else:
            print("Invalid option. Try again.")

# Run the program
if __name__ == "__main__":
    main()
