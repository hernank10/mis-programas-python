import sympy as sp

def mostrar_menu():
    print("\n--- Ábaco Mental para Álgebra ---")
    print("1. Resolver una ecuación lineal")
    print("2. Resolver una ecuación no lineal")
    print("3. Operaciones con polinomios")
    print("4. Resolver un sistema de ecuaciones lineales")
    print("5. Salir")

def resolver_ecuacion_lineal():
    print("\n--- Resolver Ecuación Lineal ---")
    ecuacion = input("Ingresa una ecuación lineal (ejemplo: 2*x + 3 = 5): ")
    x = sp.symbols('x')
    solucion = sp.solve(sp.Eq(*map(sp.sympify, ecuacion.split('='))), x)
    print(f"La solución para la ecuación {ecuacion} es: {solucion}")

def resolver_ecuacion_no_lineal():
    print("\n--- Resolver Ecuación No Lineal ---")
    ecuacion = input("Ingresa una ecuación no lineal (ejemplo: x**2 - 4 = 0): ")
    x = sp.symbols('x')
    solucion = sp.solve(sp.sympify(ecuacion), x)
    print(f"La solución para la ecuación {ecuacion} es: {solucion}")

def operaciones_polinomios():
    print("\n--- Operaciones con Polinomios ---")
    x = sp.symbols('x')
    polinomio1 = sp.sympify(input("Ingresa el primer polinomio (ejemplo: x**2 + 2*x + 1): "))
    polinomio2 = sp.sympify(input("Ingresa el segundo polinomio (ejemplo: x + 1): "))
    operacion = input("Selecciona una operación (+, -, *, /): ")

    if operacion == '+':
        resultado = polinomio1 + polinomio2
    elif operacion == '-':
        resultado = polinomio1 - polinomio2
    elif operacion == '*':
        resultado = polinomio1 * polinomio2
    elif operacion == '/':
        resultado = sp.simplify(polinomio1 / polinomio2)
    else:
        print("Operación no válida.")
        return

    print(f"El resultado de {polinomio1} {operacion} {polinomio2} es: {resultado}")

def resolver_sistema_ecuaciones():
    print("\n--- Resolver Sistema de Ecuaciones Lineales ---")
    num_ecuaciones = int(input("¿Cuántas ecuaciones tiene el sistema? (Ejemplo: 2): "))
    variables = sp.symbols(' '.join([f'x{i+1}' for i in range(num_ecuaciones)]))
    ecuaciones = []

    for i in range(num_ecuaciones):
        ecuacion = input(f"Ingresa la ecuación {i+1} (Ejemplo: x1 + x2 = 3): ")
        ecuaciones.append(sp.Eq(*map(sp.sympify, ecuacion.split('='))))

    solucion = sp.solve(ecuaciones, variables)
    print(f"La solución para el sistema es: {solucion}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            resolver_ecuacion_lineal()
        elif opcion == '2':
            resolver_ecuacion_no_lineal()
        elif opcion == '3':
            operaciones_polinomios()
        elif opcion == '4':
            resolver_sistema_ecuaciones()
        elif opcion == '5':
            print("¡Gracias por usar el Ábaco Mental para Álgebra! Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
