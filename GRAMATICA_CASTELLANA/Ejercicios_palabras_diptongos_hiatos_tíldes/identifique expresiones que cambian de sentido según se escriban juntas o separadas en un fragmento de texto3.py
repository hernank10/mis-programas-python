def identificar_expresiones(texto):
    expresiones = ["a bajo", "por venir", "sin número", "sin vergüenza"]
    palabras = texto.split()
    for i in range(len(palabras) - 1):
        palabra_actual = palabras[i]
        palabra_siguiente = palabras[i+1]
        if palabra_actual + " " + palabra_siguiente in expresiones:
            print(f"La expresión '{palabra_actual} {palabra_siguiente}' cambia de sentido según se escriba junta o separada.")
        elif palabra_actual in expresiones and palabra_siguiente not in expresiones:
            print(f"La expresión '{palabra_actual}' cambia de sentido según se escriba junta o separada.")

texto = input("Por favor, ingrese un fragmento de texto: ")
identificar_expresiones(texto)
