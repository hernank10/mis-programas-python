matplotlib.pyplot as plt

def caida_libre():
    g = 9.8
    t = float(input("Introduce el tiempo en segundos: "))
    h = 0.5 * g * t ** 2
    print(f"Distancia recorrida: {h:.2f} metros\n")

def conversion_unidades():
    print("1. Km a metros\n2. Gramos a kilogramos\n3. Litros a mililitros")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        km = float(input("Introduce kilómetros: "))
        print(f"Son {km * 1000} metros\n")
    elif opcion == "2":
        g = float(input("Introduce gramos: "))
        print(f"Son {g / 1000} kilogramos\n")
    elif opcion == "3":
        l = float(input("Introduce litros: "))
        print(f"Son {l * 1000} mililitros\n")
    else:
        print("Opción no válida\n")

def registro_datos():
    temperaturas = []
    for i in range(5):
        temp = import float(input(f"Temperatura {i+1}: "))
        temperaturas.append(temp)
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"Temperatura promedio: {promedio:.2f} °C\n")

def graficar_temperaturas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    temperaturas = [21.5, 23.0, 22.2, 24.1, 23.3]
    plt.plot(dias, temperaturas, marker='o')
    plt.title("Temperaturas semanales")
    plt.xlabel("Día")
    plt.ylabel("Temperatura °C")
    plt.grid()
    plt.show()

def tabla_periodica():
    elementos = {
        1: "Hidrógeno", 2: "Helio", 3: "Litio", 4: "Berilio",
        5: "Boro", 6: "Carbono", 7: "Nitrógeno", 8: "Oxígeno"
    }
    numero = int(input("Introduce número atómico (1-8): "))
    if numero in elementos:
        print(f"Elemento: {elementos[numero]}\n")
    else:
        print("Número no disponible en esta tabla simplificada\n")

def menu():
    while True:
        print("=== Menú de Ciencias ===")
        print("1. Simulación de caída libre")
        print("2. Conversión de unidades")
        print("3. Registro de temperaturas")
        print("4. Gráfico de temperaturas")
        print("5. Consulta tabla periódica")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            caida_libre()
        elif opcion == "2":
            conversion_unidades()
        elif opcion == "3":
            registro_datos()
        elif opcion == "4":
            graficar_temperaturas()
        elif opcion == "5":
            tabla_periodica()
        elif opcion == "6":
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")

# Ejecutar el menú
menu()
