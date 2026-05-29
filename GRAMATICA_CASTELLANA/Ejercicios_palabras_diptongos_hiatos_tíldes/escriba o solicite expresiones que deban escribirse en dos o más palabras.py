import re

def identificar_expresiones_separadas(frase):
    # Definir patrón para identificar expresiones separadas
    patron_expresiones_separadas = re.compile(r'\b\w+\b', re.IGNORECASE)

    # Encontrar expresiones separadas en la frase
    expresiones_separadas = re.findall(patron_expresiones_separadas, frase)

    return expresiones_separadas

# Solicitar al usuario un fragmento de texto
fragmento_texto = input("Ingrese un fragmento de texto: ")

# Identificar expresiones separadas en el fragmento de texto
expresiones_separadas = identificar_expresiones_separadas(fragmento_texto)

# Mostrar las expresiones separadas identificadas
print("\nExpresiones separadas identificadas:")
for expresion in expresiones_separadas:
    print(expresion)
