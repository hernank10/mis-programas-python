abreviaturas = {
    "EE. UU.": "Estados Unidos",
    "C. Rica": "Costa Rica",
    "Arg.": "Argentina",
    # Agrega más abreviaturas aquí
}

def reemplazar_abreviaturas(texto):
    for abrev, completo in abreviaturas.items():
        texto = texto.replace(abrev, completo)
    return texto

ejemplo_texto = "Viajé a los EE. UU. desde C. Rica."
texto_actualizado = reemplazar_abreviaturas(ejemplo_texto)
print(texto_actualizado)
