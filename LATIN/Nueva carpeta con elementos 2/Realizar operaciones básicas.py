# Definir dos números
numero1 = 20
numero2 = 5.899393939383838

# Realizar operaciones básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Verificar la división por cero antes de realizar la operación
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero."

# Imprimir resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
# Realizando la suma de 10 + 100
resultado = 10 + 100

# Imprimiendo el resultado
print("La suma de 10 + 100 es:", resultado)
# Solicitar al usuario que ingrese su peso y altura
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el Índice de Masa Corporal (IMC)
imc = peso / (altura ** 2)

# Imprimir el resultado
print("Tu Índice de Masa Corporal (IMC) es:", imc)

# Interpretar el IMC según la clasificación de la Organización Mundial de la Salud (OMS)
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Clasificación: Obesidad Clase 1 (Moderada)")
elif 35 <= imc < 39.9:
    print("Clasificación: Obesidad Clase 2 (Severa)")
else:
    print("Clasificación: Obesidad Clase 3 (Muy severa o mórbida)")
# Solicitar al usuario que ingrese la temperatura en Celsius
temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Calcular la temperatura en Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Imprimir el resultado
print(f"{temperatura_celsius} grados Celsius son equivalentes a {temperatura_fahrenheit} grados Fahrenheit.")
# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para obtener su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar hasta 10
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para obtener su tabla de multiplicar: "))
limite = int(input("Ingresa el número hasta el cual quieres mostrar la tabla: "))

# Imprimir la tabla de multiplicar hasta el número específico
print(f"Tabla de multiplicar del {numero} hasta {limite}:")

for i in range(1, limite + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
limite = int(input("Ingrese un número límite para encontrar los números primos: "))

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Números primos hasta el límite:")
for i in range(2, limite + 1):
    if es_primo(i):
        print(i, end=" ")
