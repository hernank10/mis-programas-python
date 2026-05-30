# Programa para practicar reglas de signos

def reglas_de_signos():
    print("Multiplicación y División con Reglas de Signos")
    
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "Indefinido"
    
    print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division}")

reglas_de_signos()
