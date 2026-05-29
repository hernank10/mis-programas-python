class LugarSenderismo:
    def __init__(self, nombre, dificultad, distancia, duracion):
        self.nombre = nombre
        self.dificultad = dificultad
        self.distancia = distancia
        self.duracion = duracion

def main():
    lugares = []

    # Agregar lugares de senderismo
    lugares.append(LugarSenderismo("Picos de Europa", "Difícil", 15, 8))
    lugares.append(LugarSenderismo("Parque Natural de Saja-Besaya", "Moderada", 10, 6))
    lugares.append(LugarSenderismo("Monte Buciero", "Moderada", 8, 5))
    lugares.append(LugarSenderismo("Ruta de los Cahorros", "Difícil", 12, 7))
    lugares.append(LugarSenderismo("Costa Quebrada", "Moderada", 10, 6))
    lugares.append(LugarSenderismo("Ruta de las Cascadas de Lamina", "Fácil", 5, 3))
    lugares.append(LugarSenderismo("Monte Cilda", "Moderada", 9, 5))
    lugares.append(LugarSenderismo("Parque Natural de los Collados del Asón", "Difícil", 18, 9))
    lugares.append(LugarSenderismo("Ruta de la Cueva del Soplao", "Moderada", 11, 6))
    lugares.append(LugarSenderismo("Monte Candina", "Difícil", 14, 8))

    print("Bienvenido a la planificación de ruta de senderismo en Santander.")
    print("Estos son los 10 lugares de senderismo recomendados:")

    # Mostrar los lugares
    for i, lugar in enumerate(lugares, start=1):
        print(f"{i}. {lugar.nombre} - Dificultad: {lugar.dificultad} - Distancia: {lugar.distancia} km - Duración: {lugar.duracion} horas")

    # Preguntar al usuario por su selección
    seleccion = input("Por favor, seleccione el número de la ruta que desea explorar: ")
    seleccion = int(seleccion)

    # Validar selección
    if seleccion < 1 or seleccion > len(lugares):
        print("Selección inválida. Por favor, elija un número válido.")
        return

    lugar_seleccionado = lugares[seleccion - 1]
    print(f"\n¡Excelente elección! Estás planeando explorar {lugar_seleccionado.nombre}.")
    print(f"Dificultad: {lugar_seleccionado.dificultad}")
    print(f"Distancia: {lugar_seleccionado.distancia} km")
    print(f"Duración estimada: {lugar_seleccionado.duracion} horas")

if __name__ == "__main__":
    main()
