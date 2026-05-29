def main():
    # Solicitar al usuario leer el ejemplo suministrado
    ejemplo = input("Ingrese el ejemplo suministrado: ")

    # Abbreviar países
    paises = ["Argentina", "España", "Venezuela", "Holanda", "Puerto Rico"]
    paises_abreviados = [pais[:3] + "." for pais in paises]

    # Abbreviar nombres
    nombres = ["Juan Pérez", "María González", "Pedro López"]
    nombres_abreviados = [nombre.split()[0] + "." for nombre in nombres]

    # Abbreviar oficinas internacionales
    oficinas = ["Organización Mundial del Comercio (OMC)", "Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura (UNESCO)"]
    oficinas_abreviadas = [oficina[:3] + "." for oficina in oficinas]

    # Generar memorándum
    memorandum = generar_memorandum(paises_abreviados, nombres_abreviados, oficinas_abreviadas)

    # Imprimir memorándum
    print(memorandum)

def generar_memorandum(paises_abreviados, nombres_abreviados, oficinas_abreviadas):
    # Reemplazar abreviaturas en el ejemplo suministrado
    ejemplo_abreviado = ejemplo

    for pais, pais_abreviado in zip(paises, paises_abreviados):
        ejemplo_abreviado = ejemplo_abreviado.replace(pais, pais_abreviado)

    for nombre, nombre_abreviado in zip(nombres, nombres_abreviados):
        ejemplo_abreviado = ejemplo_abreviado.replace(nombre, nombre_abreviado)

    for oficina, oficina_abreviada in zip(oficinas, oficinas_abreviadas):
        ejemplo_abreviado = ejemplo_abreviado.replace(oficina, oficina_abreviada)

    return ejemplo_abreviado

if __name__ == "__main__":
    main()

