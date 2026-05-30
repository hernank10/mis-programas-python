import time
import sys

def temporizador_visual(segundos):
    print("Temporizador iniciado:")
    for i in range(segundos, 0, -1):
        sys.stdout.write(f"\rTiempo restante: {i} segundos")  # Actualiza la misma línea
        sys.stdout.flush()  # Asegura que el texto se muestra inmediatamente
        time.sleep(1)
    sys.stdout.write("\r¡Tiempo terminado!                 \n")  # Limpia la línea final

# Uso del temporizador
segundos = int(input("Ingresa la cantidad de segundos para el temporizador: "))
temporizador_visual(segundos)
