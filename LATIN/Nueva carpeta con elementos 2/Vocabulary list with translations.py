# Vocabulary list with translations
vocabulary = {
    "Variable": "Variable",
    "Function": "Función",
    "Array": "Arreglo",
    "Object": "Objeto",
    "String": "Cadena de texto",
    "Number": "Número",
    "Boolean": "Booleano",
    "Conditional": "Condicional",
    "Loop": "Bucle",
    "Event": "Evento",
    "Method": "Método",
    "DOM (Document Object Model)": "DOM (Modelo de Objetos del Documento)",
    "Callback": "Función de Retorno",
    "Variable Scope": "Ámbito de la Variable",
    "Operator": "Operador",
    "Closure": "Cierre",
    "Prototype": "Prototipo",
    "Asynchronous": "Asíncrono",
    "Promise": "Promesa",
    "Module": "Módulo",
    "Selector": "Selector",
    "Property": "Propiedad",
    "Value": "Valor",
    "Class": "Clase",
    "ID": "ID",
    "Declaration": "Declaración",
    "Rule": "Regla",
    "Box model": "Modelo de Caja",
    "Display": "Mostrar",
    "Positioning": "Posicionamiento",
    "Flexbox": "Flexbox",
    "Grid": "Cuadrícula",
    "Pseudo-class": "Pseudo-clase",
    "Media queries": "Consultas de Medios",
    "Opacity": "Opacidad",
    "Transition": "Transición",
    "Transform": "Transformar",
    "Gradient": "Gradiente",
    "Font-family": "Familia de Fuentes",
    "Margin": "Margen",
    "URL": "URL (Localizador Uniforme de Recursos)",
    "Protocol": "Protocolo",
    "Address": "Dirección",
    "Resource": "Recurso",
    "Domain": "Dominio",
    "Path": "Ruta",
    "Query Parameters": "Parámetros de Consulta",
    "Fragment Identifier": "Identificador de Fragmento",
    "HTTP": "HTTP (Protocolo de Transferencia de Hipertexto)",
    "HTTPS": "HTTPS (Protocolo de Transferencia de Hipertexto Seguro)",
    "Transfer": "Transferir",
    "Secure": "Seguro",
    "Encryption": "Cifrado",
    "Client": "Cliente",
    "Server": "Servidor",
    # Nuevas palabras y expresiones
    "Framework": "Marco de trabajo",
    "Library": "Biblioteca",
    "Syntax": "Sintaxis",
    "Compile": "Compilar",
    "Debug": "Depurar"
}

def disp# Vocabulary list with translations
vocabulary = {
    "Variable": "Variable",
    "Function": "Función",
    "Array": "Arreglo",
    "Object": "Objeto",
    "String": "Cadena de texto",
    "Number": "Número",
    "Boolean": "Booleano",
    "Conditional": "Condicional",
    "Loop": "Bucle",
    "Event": "Evento",
    "Method": "Método",
    "DOM (Document Object Model)": "DOM (Modelo de Objetos del Documento)",
    "Callback": "Función de Retorno",
    "Variable Scope": "Ámbito de la Variable",
    "Operator": "Operador",
    "Closure": "Cierre",
    "Prototype": "Prototipo",
    "Asynchronous": "Asíncrono",
    "Promise": "Promesa",
    "Module": "Módulo",
    "Selector": "Selector",
    "Property": "Propiedad",
    "Value": "Valor",
    "Class": "Clase",
    "ID": "ID",
    "Declaration": "Declaración",
    "Rule": "Regla",
    "Box model": "Modelo de Caja",
    "Display": "Mostrar",
    "Positioning": "Posicionamiento",
    "Flexbox": "Flexbox",
    "Grid": "Cuadrícula",
    "Pseudo-class": "Pseudo-clase",
    "Media queries": "Consultas de Medios",
    "Opacity": "Opacidad",
    "Transition": "Transición",
    "Transform": "Transformar",
    "Gradient": "Gradiente",
    "Font-family": "Familia de Fuentes",
    "Margin": "Margen",
    "URL": "URL (Localizador Uniforme de Recursos)",
    "Protocol": "Protocolo",
    "Address": "Dirección",
    "Resource": "Recurso",
    "Domain": "Dominio",
    "Path": "Ruta",
    "Query Parameters": "Parámetros de Consulta",
    "Fragment Identifier": "Identificador de Fragmento",
    "HTTP": "HTTP (Protocolo de Transferencia de Hipertexto)",
    "HTTPS": "HTTPS (Protocolo de Transferencia de Hipertexto Seguro)",
    "Transfer": "Transferir",
    "Secure": "Seguro",
    "Encryption": "Cifrado",
    "Client": "Cliente",
    "Server": "Servidor",
    # Nuevas palabras y expresiones
    "Framework": "Marco de trabajo",
    "Library": "Biblioteca",
    "Syntax": "Sintaxis",
    "Compile": "Compilar",
    "Debug": "Depurar"
}

def display_vocabulary(vocab):
    """Display the vocabulary list."""
    print("Study the following vocabulary list:\n")
    for word, translation in vocab.items():
        print(f"{word}: {translation}")

def study_vocabulary(vocab):
    """Allow the user to study the vocabulary."""
    display_vocabulary(vocab)
    input("\nPress Enter when you are ready to start the quiz...\n")

def take_quiz(vocab):
    """Conduct the quiz and return the number of correct answers."""
    correct = 0
    for word, translation in vocab.items():
        answer = input(f"What is the translation of '{word}' in Spanish? ")
        if answer.strip().lower() == translation.lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is '{translation}'.\n")
    return correct

def show_results(correct, total):
    """Display the results of the quiz."""
    print(f"You got {correct} out of {total} correct!")

# Main function to run the quiz
def main():
    study_vocabulary(vocabulary)
    correct_answers = take_quiz(vocabulary)
    show_results(correct_answers, len(vocabulary))

# Run the main function
if __name__ == "__main__":
    main()
lay_vocabulary(vocab):
    """Display the vocabulary list."""
    print("Study the following vocabulary list:\n")
    for word, translation in vocab.items():
        print(f"{word}: {translation}")

def study_vocabulary(vocab):
    """Allow the user to study the vocabulary."""
    display_vocabulary(vocab)
    input("\nPress Enter when you are ready to start the quiz...\n")

def take_quiz(vocab):
    """Conduct the quiz and return the number of correct answers."""
    correct = 0
    for word, translation in vocab.items():
        answer = input(f"What is the translation of '{word}' in Spanish? ")
        if answer.strip().lower() == translation.lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is '{translation}'.\n")
    return correct

def show_results(correct, total):
    """Display the results of the quiz."""
    print(f"You got {correct} out of {total} correct!")

# Main function to run the quiz
def main():
    study_vocabulary(vocabulary)
    correct_answers = take_quiz(vocabulary)
    show_results(correct_answers, len(vocabulary))

# Run the main function
if __name__ == "__main__":
    main()
