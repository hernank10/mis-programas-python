# Simulador de Elección de Historia

def mostrar_mensaje(mensaje):
    print("\n" + mensaje)

def inicio():
    mostrar_mensaje("Te despiertas en un bosque oscuro. Ves dos caminos: uno hacia la montaña y otro hacia el río.")
    elección = input("¿Qué camino eliges? (montaña/río): ").lower()
    if elección == 'montaña':
        montaña()
    elif elección == 'río':
        rio()
    else:
        mostrar_mensaje("Elección no válida.")
        inicio()

def montaña():
    mostrar_mensaje("Subes por el camino hacia la montaña. Encuentras una cueva.")
    elección = input("¿Entrar en la cueva o continuar subiendo? (cueva/subir): ").lower()
    if elección == 'cueva':
        mostrar_mensaje("Dentro de la cueva, encuentras un tesoro escondido. ¡Has ganado!")
    elif elección == 'subir':
        mostrar_mensaje("Sigues subiendo y llegas a la cima, disfrutando de una vista espectacular. Fin del viaje.")
    else:
        mostrar_mensaje("Elección no válida.")
        montaña()

def rio():
    mostrar_mensaje("Te diriges hacia el río y ves un bote abandonado.")
    elección = input("¿Usar el bote o seguir caminando? (bote/caminar): ").lower()
    if elección == 'bote':
        mostrar_mensaje("Navegas río abajo y descubres una aldea amigable. ¡Has encontrado ayuda!")
    elif elección == 'caminar':
        mostrar_mensaje("Sigues caminando y te pierdes en el bosque. Fin del viaje.")
    else:
        mostrar_mensaje("Elección no válida.")
        rio()

inicio()
