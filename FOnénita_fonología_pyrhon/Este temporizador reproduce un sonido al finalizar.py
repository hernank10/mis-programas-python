import time
from playsound import playsound

def temporizador_con_sonido(segundos):
    print("Temporizador iniciado:")
    for i in range(segundos, 0, -1):
        print(f"Tiempo restante: {i} segundos", end="\r")
        time.sleep(1)
    print("\n¡Tiempo terminado!")
    playsound('ruta/del/sonido.mp3')  # Cambia esta ruta por un archivo de sonido válido.

# Uso del temporizador
segundos = int(input("Ingresa la cantidad de segundos para el temporizador: "))
temporizador_con_sonido(segundos)
