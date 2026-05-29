def obtener_fragmento_texto():
    fragmento_texto = (
        "El perro está en la puerta esperando. "
        "La tarde cae y el sol se pone. "
        "Quiere salir para disfrutar del aire libre."
    )
    return fragmento_texto

def identificar_expresiones_sensibles(fragmento_texto):
    expresiones_sensibles = ["soltero", "extraño", "de repente", "sin embargo"]

    print("\nFragmento de texto:")
    print(fragmento_texto)

    print("\nIdentifica expresiones que cambian de sentido según se escriban juntas o separadas:")

    for i in range(len(expresiones_sensibles)):
        expresion_usuario = input(f"Expresión ({i+1}/{len(expresiones_sensibles)}): ").strip().lower()

        if expresion_usuario == expresiones_sensibles[i]:
            print(f"¡Correcto! La expresión '{expresiones_sensibles[i]}' cambia de sentido según se escriba junta o separada.")
        else:
            print(f"Incorrecto. La expresión correcta es '{expresiones_sensibles[i]}'.")

def main_expresiones_sensibles():
    fragmento_texto = obtener_fragmento_texto()
    identificar_expresiones_sensibles(fragmento_texto)

if __name__ == "__main__":
    main_expresiones_sensibles()
