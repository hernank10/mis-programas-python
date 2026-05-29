import time

def temporizador_hh_mm_ss(segundos):
    print("Temporizador iniciado:")
    while segundos:
        mins, secs = divmod(segundos, 60)
        tiempo = f"{mins:02d}:{secs:02d}"
        print(f"\rTiempo restante: {tiempo}", end="")
        time.sleep(1)
        segundos -= 1
    print("\r¡Tiempo terminado!        ")

# Uso del temporizador
segundos = int(input("Ingresa la cantidad de segundos para el temporizador: "))
temporizador_hh_mm_ss(segundos)
