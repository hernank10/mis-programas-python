import re

def identificar_expresiones_unidas(frase):
    # Definir patrón para identificar expresiones unidas
    patron_expresiones_unidas = re.compile(r'\b\w+\b', re.IGNORECASE)

    # Encontrar expresiones unidas en la frase
    expresiones_unidas = re.findall(patron_expresiones_unidas, frase)

    return expresiones_unidas

# Solicitar al usuario un fragmento de texto
fragmento_texto = input("Ingrese un fragmento de texto: ")

# Identificar expresiones unidas en el fragmento de texto
expresiones_unidas = identificar_expresiones_unidas(fragmento_texto)

# Mostrar las expresiones unidas identificadas
print("\nExpresiones unidas identificadas:")
for expresion in expresiones_unidas:
    print(expresion)
