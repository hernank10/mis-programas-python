def leer_regla(regla):
    print(f"Por favor, lee la regla {regla}:")
    entrada = input()
    return entrada.strip().lower()  # Elimina espacios y convierte a minúsculas

def verificar_regla(regla, entrada):
    if entrada == regla:
        print("¡Correcto! Continuemos con la siguiente regla.")
        return True
    else:
        print(f"Incorrecto. La regla correcta era: {regla}")
        return False

def main():
    reglas = {
        "b": [
            "Palabras que comienzan con 'bl' o 'br'",
            "Ante consonante siempre se escribe 'b'",
            # ... otras reglas para la letra "b"
        ],
        "v": [
            "Palabras que contienen la secuencia N + V",
            "Algunas formas del verbo 'ir'",
            # ... otras reglas para la letra "v"
        ],
        "w": [
            "Palabras con 'w' en préstamos lingüísticos",
            "Adaptación al castellano",
            # ... otras reglas para la letra "w"
        ]
    }

    for letra, lista_reglas in reglas.items():
        print(f"Reglas para la letra '{letra}':")
        for i, regla in enumerate(lista_reglas, start=1):
            entrada_usuario = leer_regla(regla)
            if not verificar_regla(regla.lower(), entrada_usuario):
                print("¡Inténtalo de nuevo!")
                break
        else:
            print(f"¡Excelente! Has completado las reglas para la letra '{letra}'.")

if __name__ == "__main__":
    main()
