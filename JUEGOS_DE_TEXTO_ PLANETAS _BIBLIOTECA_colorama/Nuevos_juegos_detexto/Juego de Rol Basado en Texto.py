# Juego de Rol Basado en Texto

import random

def crear_personaje():
    nombre = input("Ingresa el nombre de tu personaje: ")
    clase = input("Elige una clase (guerrero/mago): ").lower()
    if clase == 'guerrero':
        salud = 120
        ataque = 15
    elif clase == 'mago':
        salud = 80
        ataque = 25
    else:
        salud = 100
        ataque = 10
    return {'nombre': nombre, 'clase': clase, 'salud': salud, 'ataque': ataque}

def mostrar_estado(jugador):
    print(f"\n{jugador['nombre']} - Clase: {jugador['clase'].capitalize()} | Salud: {jugador['salud']} | Ataque: {jugador['ataque']}")

def explorar(jugador):
    enemigos = ['Goblin', 'Orco', 'Espectro']
    enemigo = random.choice(enemigos)
    salud_enemigo = random.randint(50, 100)
    print(f"\nHas encontrado un {enemigo} con {salud_enemigo} de salud.")
    while salud_enemigo > 0 and jugador['salud'] > 0:
        acción = input("¿Qué quieres hacer? (atacar/huir): ").lower()
        if acción == 'atacar':
            daño = jugador['ataque'] + random.randint(-5, 5)
            salud_enemigo -= daño
            print(f"Atacas al {enemigo} y le haces {daño} de daño. Salud del {enemigo}: {salud_enemigo}")
            if salud_enemigo > 0:
                daño_recibido = random.randint(5, 15)
                jugador['salud'] -= daño_recibido
                print(f"El {enemigo} te ataca y recibes {daño_recibido} de daño. Tu salud: {jugador['salud']}")
        elif acción == 'huir':
            print("Decides huir del combate.")
            break
        else:
            print("Acción no válida.")
    if jugador['salud'] <= 0:
        print("Has sido derrotado. Fin del juego.")
        exit()

def main():
    jugador = crear_personaje()
    mostrar_estado(jugador)
    while jugador['salud'] > 0:
        elección = input("\n¿Qué quieres hacer? (explorar/ver estado/salir): ").lower()
        if elección == 'explorar':
            explorar(jugador)
        elif elección == 'ver estado':
            mostrar_estado(jugador)
        elif elección == 'salir':
            print("Gracias por jugar.")
            break
        else:
            print("Elección no válida.")

if __name__ == "__main__":
    main()
