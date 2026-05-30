import time

def temporizador(segundos):
    print(f"El temporizador se ha iniciado por {segundos} segundos.")
    for i in range(segundos, 0, -1):
        print(f"Quedan {i} segundos...")
        time.sleep(1)  # Pausa de 1 segundo
    print("¡El tiempo se ha agotado!")

# Uso del temporizador
segundos = int(input("Ingresa la cantidad de segundos para el temporizador: "))
temporizador(segundos)
