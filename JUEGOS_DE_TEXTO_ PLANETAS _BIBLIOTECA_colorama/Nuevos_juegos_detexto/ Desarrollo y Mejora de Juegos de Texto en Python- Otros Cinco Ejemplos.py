import time

tiempo_restante = 300  # 5 minutos en segundos

def cuenta_regresiva():
    while tiempo_restante > 0:
        print(f"Tiempo restante: {tiempo_restante // 60}:{tiempo_restante % 60}")
        time.sleep(1)
        tiempo_restante -= 1
    print("¡El tiempo se ha agotado!")

inventario = ['cuerda', 'llave rota']

def combinar(objetos):
    if 'cuerda' in objetos and 'llave rota' in objetos:
        inventario.remove('cuerda')
        inventario.remove('llave rota')
        inventario.append('llave completa')
        print("Has combinado los objetos para formar una llave completa.")

def ia_enemigo(vida_enemigo, vida_jugador):
    if vida_enemigo < 30:
        print("El enemigo usa una poción de curación.")
        vida_enemigo += 20
    else:
        if vida_jugador > 50:
            print("El enemigo te ataca con un golpe poderoso.")
        else:
            print("El enemigo usa un ataque débil.")
equipo = {'arma': 'espada básica', 'armadura': 'armadura ligera'}

def mejorar_equipo():
    equipo['arma'] = 'espada encantada'
    equipo['armadura'] = 'armadura pesada'
    print("Has mejorado tu equipo.")

ciclo = ['día', 'noche']

def avanzar_tiempo():
    global ciclo
    if ciclo[0] == 'día':
        print("El día ha terminado. La noche ha caído.")
        ciclo[0] = 'noche'
    else:
        print("La noche ha terminado. El sol ha salido.")
        ciclo[0] = 'día'

salud = 100
hambre = 100

def comer(comida):
    global hambre
    hambre += comida
    if hambre > 100:
        hambre = 100
    print(f"Has comido. Hambre actual: {hambre}")

reputacion = 50

def entrevista(personaje):
    if reputacion > 60:
        print(f"{personaje} confía en ti y te da una pista importante.")
    else:
        print(f"{personaje} no confía en ti y te da información incorrecta.")
def seguir_pista(decision):
    if decision == 'correcta':
        print("Has seguido la pista correcta.")
    else:
        print("Te has desviado de la investigación.")

moral = 100

def batalla(resultado):
    global moral
    if resultado == 'victoria':
        moral += 10
        print("Tu ejército ha ganado. Moral aumentada.")
    else:
        moral -= 20
        print("Tu ejército ha perdido. Moral disminuida.")

mapa = {
    'ciudad1': {'control': 'enemigo', 'recursos': 100},
    'ciudad2': {'control': 'aliado', 'recursos': 200}
}

def atacar_ciudad(ciudad):
    if mapa[ciudad]['control'] == 'enemigo':
        print(f"Atacando {ciudad}.")
        mapa[ciudad]['control'] = 'aliado'
    else:
        print(f"{ciudad} ya está bajo tu control.")

